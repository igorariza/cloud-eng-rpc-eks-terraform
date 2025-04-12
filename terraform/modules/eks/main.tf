provider "aws" {
  region = "us-east-1"
}


# Security group for EKS control plane
resource "aws_security_group" "eks_control_plane" {
  name        = "${var.cluster_name}-eks-control-plane-sg"
  description = "Security group for EKS control plane"
  vpc_id      = var.vpc_id

  # Allow inbound traffic on port 443 from worker nodes
  ingress {
    from_port       = 443
    to_port         = 443
    protocol        = "tcp"
    security_groups = [aws_security_group.eks_worker_nodes.id]
  }

  # Allow all outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Security group for EKS worker nodes
resource "aws_security_group" "eks_worker_nodes" {
  name        = "${var.cluster_name}-eks-worker-nodes-sg"
  description = "Security group for EKS worker nodes"
  vpc_id      = var.vpc_id

  # Allow all inbound traffic from the control plane
  ingress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    security_groups = [aws_security_group.eks_control_plane.id]
  }

  # Allow all outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# EKS module configuration
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "18.0.0"

  cluster_name    = var.cluster_name
  cluster_version = "1.31"
  vpc_id          = var.vpc_id
  subnet_ids      = var.subnets
  

  # Remove map_users and manage user access via aws-auth ConfigMap

  # Pass security groups to the EKS module
  cluster_security_group_id = aws_security_group.eks_control_plane.id

  eks_managed_node_groups = {
    default = {
      desired_size   = 2
      max_size       = 3
      min_size       = 1
      instance_types = ["t3.medium"]
      iam_role_arn   = module.aim.node_role_arn
    }
  }
}

provider "kubernetes" {
  host                   = module.eks.cluster_endpoint
  token                  = data.aws_eks_cluster_auth.cluster.token
  cluster_ca_certificate = base64decode(module.eks.cluster_certificate_authority_data)
}

resource "kubernetes_manifest" "iariza_admin_binding" {
  manifest = {
    apiVersion = "rbac.authorization.k8s.io/v1"
    kind       = "ClusterRoleBinding"
    metadata = {
      name = "iariza-admin-binding"
    }
    subjects = [{
      kind      = "User"
      name      = "arn:aws:iam::147997139534:user/iariza" # Replace with your IAM user ARN
      apiGroup  = "rbac.authorization.k8s.io"
    }]
    roleRef = {
      kind     = "ClusterRole"
      name     = "cluster-admin"
      apiGroup = "rbac.authorization.k8s.io"
    }
  }
}