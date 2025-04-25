resource "aws_iam_role" "eks_node_role" {
  name = "eks-node-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = "ec2.amazonaws.com"
      }
      Action = "sts:AssumeRole"
    }]
  })

  tags = {
    Name = "eks-node-role"
  }
}

resource "aws_iam_role_policy_attachment" "AmazonEKSWorkerNodePolicy" {
  policy_arn = "arn:aws:iam::147997139534:role/aws-service-role/eks.amazonaws.com/AWSServiceRoleForAmazonEKS"
  role       = aws_iam_role.eks_node_role.name
}

resource "aws_iam_role_policy_attachment" "AmazonEKS_CNI_Policy" {
  policy_arn = "arn:aws:iam::147997139534:role/aws-service-role/eks.amazonaws.com/AWSServiceRoleForAmazonEKS"
  role       = aws_iam_role.eks_node_role.name
}

resource "aws_iam_role_policy_attachment" "AmazonEC2ContainerRegistryReadOnly" {
  policy_arn = "arn:aws:iam::147997139534:role/aws-service-role/eks.amazonaws.com/AWSServiceRoleForAmazonEKS"
  role       = aws_iam_role.eks_node_role.name
}

resource "aws_iam_role_policy_attachment" "admin_access" {
  policy_arn = "arn:aws:iam::147997139534:role/aws-service-role/eks.amazonaws.com/AmazonEKSClusterAdminPolicy"
  role       = aws_iam_role.eks_node_role.name
}
