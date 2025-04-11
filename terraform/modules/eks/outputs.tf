output "eks_cluster_name" {
  value = module.eks.cluster_name
}

output "load_balancer_dns" {
  value = aws_lb.app_lb.dns_name
}