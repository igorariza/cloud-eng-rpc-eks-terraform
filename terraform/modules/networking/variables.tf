variable "vpc_cidr_block" {
  description = "CIDR block for the VPC"
  type = string
}

variable "public_subnets" {
  description = "List of public subnet CIDR blocks"
  type        = list(string)
}

variable "private_subnets" {
  description = "List of private subnet CIDR blocks"
  type        = list(string)
}

variable "name" {
  description = "Name prefix for resources"
  type = string
}