provider "aws" {
  region = "us-east-1"
}
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "18.0.0"

  cluster_name    = var.cluster_name
  cluster_version = "1.24"
  vpc_id          = var.vpc_id
  subnet_ids      = var.subnets

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