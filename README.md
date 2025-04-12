# Cloud Engineering RPC EKS Terraform Project

This project is a cloud-native microservices architecture deployed on **Amazon Elastic Kubernetes Service (EKS)** using **Terraform** for infrastructure provisioning. It includes two services: `account-service` and `transaction-service`. The project uses **AWS CodeBuild** for CI/CD, **Amazon ECR** for container image storage, and Kubernetes for orchestration.

---

## Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Setup and Deployment](#setup-and-deployment)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This project demonstrates how to deploy and manage microservices on AWS EKS using Terraform. The services are containerized using Docker and deployed to Kubernetes. The infrastructure is fully automated, including CI/CD pipelines for building, pushing, and deploying the services.

---

## Architecture

### Key Components:
1. **Amazon EKS**: Kubernetes cluster for running the microservices.
2. **Terraform**: Infrastructure as Code (IaC) for provisioning EKS, IAM roles, and security groups.
3. **Amazon ECR**: Container registry for storing Docker images.
4. **AWS CodeBuild**: CI/CD pipeline for building and deploying services.
5. **Kubernetes**: Orchestrates the deployment and scaling of the microservices.

---

## Prerequisites

Before you begin, ensure you have the following installed and configured:

1. **AWS CLI** (v2 or later)
   - [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
   - Configure it with your AWS credentials:
     ```bash
     aws configure
     ```

2. **Terraform** (v1.3 or later)
   - [Install Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)

3. **kubectl** (Kubernetes CLI)
   - [Install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

4. **Docker**
   - [Install Docker](https://docs.docker.com/get-docker/)

5. **IAM Permissions**
   - Ensure your AWS IAM user/role has the following permissions:
     - `AmazonEKSClusterPolicy`
     - `AmazonEKSWorkerNodePolicy`
     - `AmazonEC2ContainerRegistryReadOnly`
     - `IAMFullAccess`

---

## Setup and Deployment

### 1. Clone the Repository
```bash
git clone https://github.com/igorariza/cloud-eng-rpc-eks-terraform.git
cd cloud-eng-rpc-eks-terraform
```
### 2. Initialize Terraform
```bash
cd terraform
terraform init
```
### 3. Configure Terraform Variables
- Create a `terraform.tfvars` file in the `terraform` directory and set the following variables:
```hcl
aws_region = "us-east-1" 
cluster_name = "cloud-eng-rpc-eks-terraform"
```
### 4. Apply Terraform Configuration
```bash
terraform apply
```
- Review the plan and type `yes` to proceed with the deployment.
### 5. Configure kubectl
- Update your kubeconfig to use the new EKS cluster:
```bash
aws eks --region us-east-1 update-kubeconfig --name cloud-eng-rpc-eks-terraform
```
### 6. Deploy codebuild
- Create commit to the `main` branch of the `codebuild` repository. This will trigger the CodeBuild project and deploy the services to EKS.
### 7. Verify Deployment
- Check the status of the pods:
```bash
kubectl get pods
```
### port-forwarding services
- To access the services locally, you can use port forwarding:
```bash
kubectl port-forward -n default service/banking-service 50052:50051
kubectl port-forward -n default service/transaction-service 50053:50051
```
- Access the services in your browser:
  - Account Service: `http://localhost:50001`
  - Transaction Service: `http://localhost:50002`

### Request Postman rpc
- You can use Postman to test the services. Import the `postman_collection.json` file located in the `postman` directory to your Postman workspace.
- The collection contains requests for both the `account-service` and `transaction-service`.
- Make sure to update the URLs in the Postman collection to match your local port forwarding settings.
- For example, the `account-service` URL should be `http://localhost:50001/account`.
- The `transaction-service` URL should be `http://localhost:50002/transaction`.
