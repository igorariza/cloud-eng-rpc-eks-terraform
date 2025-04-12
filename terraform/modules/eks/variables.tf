variable "cluster_name" {
  description = "Nombre del clúster EKS"
  type        = string
}

variable "vpc_id" {
  description = "ID de la VPC donde se desplegará EKS"
  type        = string
}

variable "subnets" {
  description = "IDs de las subredes (subnets) donde se desplegará EKS"
  type        = list(string)
}
variable "node_role_arn" {
  description = "ARN del rol de IAM para los nodos de EKS"
  type        = string
}
variable "security_groups" {
  description = "Lista de grupos de seguridad para el clúster EKS"
  type        = list(string)
}
variable "role" {
  description = "ARN del rol de IAM para el servicio EKS"
  type        = string
}

variable "region" {
  description = "Región de AWS donde se desplegará EKS"
  type        = string
}