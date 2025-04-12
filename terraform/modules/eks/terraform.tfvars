cluster_name    = "cloud-eng-rpc-eks-terraform"
vpc_id          = "vpc-0ede3b6922c597ea7" 
subnets         = ["subnet-05282aade0d8c18d4", "subnet-084c40fa612a174f1"] # Reemplaza con los IDs de las subredes públicas
node_role_arn   = "arn:aws:iam::147997139534:role/devops"
security_groups = ["sg-0e4bc48ae0d75b4c9"]
role = ["arn:aws:iam::147997139534:role/AmazonEKSAutoNodeRole", "arn:aws:iam::147997139534:role/AmazonEKSAutoClusterRole"]
region         = "us-east-1"
  