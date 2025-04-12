output "eks_cluster_name" {
  value = module.eks.cluster_name
}

output "load_balancer_dns" {
  value = aws_lb.app_lb.dns_name
}

output "node_role_arn" {
  value = aws_iam_role.eks_node_role.arn
}
