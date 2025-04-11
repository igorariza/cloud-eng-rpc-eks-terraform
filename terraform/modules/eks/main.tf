module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "18.0.0"

  cluster_name    = var.cluster_name
  cluster_version = "1.24"
  vpc_id          = var.vpc_id
  # subnets attribute removed as it is not valid here

  # Configuración básica del clúster
  #manage_aws_auth = true
}

module "eks_node_groups" {
  source  = "terraform-aws-modules/eks/aws//modules/node_groups"
  version = "18.0.0"

  cluster_name = module.eks.cluster_name
  cluster_version = "1.24"
}

resource "aws_lb" "app_lb" {
  name               = "${var.cluster_name}-lb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = var.security_groups
  subnets            = var.subnets

  enable_deletion_protection = false
}

resource "aws_lb_listener" "http" {
  load_balancer_arn = aws_lb.app_lb.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type = "fixed-response"
    fixed_response {
      content_type = "text/plain"
      message_body = "Hello from EKS!"
      status_code  = "200"
    }
  }
}

output "eks_cluster_name" {
  value = module.eks.cluster_name
}

output "load_balancer_dns" {
  value = aws_lb.app_lb.dns_name
}