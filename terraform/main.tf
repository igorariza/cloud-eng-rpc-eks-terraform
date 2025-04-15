terraform {
  backend "s3" {
    bucket         = "terrafostatebucket"
    key            = "rpc-eks-terraform/state"
    region         = "us-east-1"
  }
}

provider "aws" {
  region = "us-east-1"
}

module "networking" {
  source          = "./modules/networking"
  vpc_cidr_block  = "10.0.0.0/16"
  public_subnets  = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnets = ["10.0.3.0/24", "10.0.4.0/24"]
  name            = "rpc-network"
}