# Introduction:
In today’s fast-paced software development landscape, automating the deployment process is crucial for ensuring efficiency and reliability. In this article, we will dive deep into creating an end-to-end Jenkins pipeline to deploy a Java application. This comprehensive guide is designed to take you through the entire process from scratch, making it accessible even if you are new to DevOps.

We will start by setting up our infrastructure, configuring servers, and setting up essential tools. Next, we will create a Kubernetes cluster and a private repository for our source code. As we proceed, we’ll push the source code, write the Jenkins pipeline, and implement a robust monitoring system to keep track of our application’s performance.

We will divide this project into four parts:

# Part 1: Infrastructure Setup
In the first part, we will lay the groundwork for our CI/CD pipeline by setting up the necessary infrastructure and tools. This involves:

**Setting Up Infrastructure and Tools**: We’ll set up servers, configure them, and install essential tools to create a solid foundation for our CI/CD pipeline.**Creating a Kubernetes Cluster**: Learn how to create and configure a Kubernetes cluster to manage our containerized applications.**Setting Up Jenkins, Nexus, and SonarQube Servers**: We will install and configure Jenkins for automation, Nexus for artifact management, and SonarQube for code quality analysis.
# Part 2: Source Code Management
The second part focuses on managing our source code, including:

**Creating a Private Git Repository**: Set up a Git repository to store our source code securely, ensuring no unauthorized access.**Pushing Source Code**: Push the source code to the repository and verify its visibility and accessibility.
# Part 3: CI/CD Pipeline Configuration
In the third part, we will configure our CI/CD pipeline, which includes:

**Building the Jenkins Pipeline**: Using Jenkins, we’ll write a pipeline that includes stages like source code compilation, running unit tests, and performing code quality checks with SonarQube.**Security Scanning**: Implement vulnerability scanning on the source code and dependencies using tools like Trivy.**Artifact Management**: Package the application, generate artifacts, and publish them to the Nexus repository for version control.**Containerization**: Build Docker images, tag them appropriately, and push them to Docker Hub.**Kubernetes Deployment**: Deploy the application to a secure Kubernetes cluster, ensuring the cluster’s security using tools like kube-audit.
# Part 4: Monitoring and Security
The final part involves setting up comprehensive monitoring and security checks, including:

**Monitoring and Notification**: Set up monitoring using Grafana and Prometheus, including system-level monitoring with node exporter and application-level monitoring with blackbox exporter. We’ll also configure email notifications for pipeline success or failure.
By following these four parts, we will build a robust and secure Jenkins pipeline capable of deploying a Java application efficiently

By the end of this article, you will have a fully functional Jenkins pipeline capable of deploying a Java application from code commit to production, complete with comprehensive monitoring and security practices. Whether you’re a developer or a DevOps engineer, this guide will equip you with the knowledge to implement a robust CI/CD pipeline and streamline your deployment process.

Join me on this journey to master the art of automating Java application deployment with Jenkins. Let’s get started!

**1. Setting Up Infrastructure and Tools**:
For this project, we will utilize a default VPC. In a corporate environment, we typically set up everything within a private VPC to enhance security. The first step is to create a security group that we will attach to each instance we create.

Below are the details of **Inbound -rule** for our security group named **devops-automation-primary-sg****.**

We will create **7 EC2 instances** of Ubuntu Server 20.04 with the following configurations:

**Instance Type:**t3.xlarge**Security Group:**primary-SG**Volumes:**1 volume (gp3) — 30 GiB
The instances will be named accordingly:

- master
- slave-1
- slave-2
- jenkins
- sonarqube
- nexus
- monitoring
**Note:** You can select **t3.medium** instances with **Ubuntu Server 20.04** as well. I encountered errors with **t3.medium**, so I chose **t3.xlarge**, which incurs higher costs. You can also experiment with Linux servers by replacing commands as per **YUM **compatibility. If you encounter errors, resolving them will boost your confidence.
**2. Creating a Kubernetes Cluster**:
I recommend using MobaXterm or MTPuTTY to SSH into the servers.

**Commands to Run on Both Master and Worker Nodes**
`sudo su -`
sudo apt-get update
sudo apt install docker.io -y
sudo chmod 666 /var/run/docker.sock
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
sudo mkdir -p -m 755 /etc/apt/keyrings
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.28/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.28/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt update
sudo apt install -y kubeadm=1.28.1-1.1 kubelet=1.28.1-1.1 kubectl=1.28.1-1.1
**Commands to Run on Master Node Only**
`sudo su -`
# Run the output of the following command on the worker node to join it to the cluster
sudo kubeadm init --pod-network-cidr=10.244.0.0/16
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.49.0/deploy/static/provider/baremetal/deploy.yaml
If you forget to join the worker node, you can retrieve the token using the command below and run it on the worker node:

`kubeadm token create --print-join-command`
Now our k8 cluster is ready you can execute kubectl command

**K8s Cluster Scanning on Master Node**
To scan the Kubernetes cluster, run the following commands on the master node. Note that it will show many errors since we haven’t set up everything like RBAC, etc. The output can be utilized by the infra team.

`wget https://github.com/Shopify/kubeaudit/releases/download/v0.22.1/kubeaudit_0.22.1_linux_amd64.tar.gz`
tar -xvzf kubeaudit_0.22.1_linux_amd64.tar.gz
sudo mv kubeaudit /usr/local/bin/
kubeaudit all
## 3. Setting Up Jenkins
**Install Jenkins Script**
Save the following script in a file, for example, `install_jenkins.sh`
:

`#!/bin/bash`
# Install OpenJDK 17 JRE Headless (pre-requisite)
sudo apt install openjdk-17-jre-headless -y
# Download Jenkins GPG key (official code link - https://www.jenkins.io/doc/book/installing/linux/#debianubuntu)
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
# Add Jenkins repository to package manager sources
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
# Update package manager repositories
sudo apt-get update
# Install Jenkins
sudo apt-get install jenkins -y
Make the script executable and run it:

`chmod +x install_jenkins.sh`
./install_jenkins.sh
This script will automate the installation process of OpenJDK 17 JRE Headless and Jenkins.

**Install Docker Script**
Save the following script in a file, for example, `install_docker.sh`
:

`#!/bin/bash`
# Update package manager repositories
sudo apt-get update
# Install necessary dependencies
sudo apt-get install -y ca-certificates curl
# Create directory for Docker GPG key
sudo install -m 0755 -d /etc/apt/keyrings
# Download Docker's GPG key
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
# Ensure proper permissions for the key
sudo chmod a+r /etc/apt/keyrings/docker.asc
# Add Docker repository to Apt sources
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
# Update package manager repositories
sudo apt-get update
# Install Docker packages
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
Make the script executable and run it:

`chmod +x install_docker.sh`
./install_docker.sh
Give permission to other users to run Docker commands:

`sudo chmod 666 /var/run/docker.sock`
After running these commands, Jenkins will be accessible on your host machine at [http://IP:8080](http://IP:8080.)[.](http://IP:8080.)

## 4. Setting Up Nexus
**Step 1: Install Docker**
First, we need to install Docker. Save the following script in a file named `install_docker.sh`
:

`#!/bin/bash`
# Update package manager repositories
sudo apt-get update
# Install necessary dependencies
sudo apt-get install -y ca-certificates curl
# Create directory for Docker GPG key
sudo install -m 0755 -d /etc/apt/keyrings
# Download Docker's GPG key
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
# Ensure proper permissions for the key
sudo chmod a+r /etc/apt/keyrings/docker.asc
# Add Docker repository to Apt sources
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
# Update package manager repositories again
sudo apt-get update
# Install Docker packages
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
Make the script executable and run it:

`chmod +x install_docker.sh`
./install_docker.sh
Give permission to other users to run Docker commands:

`sudo chmod 666 /var/run/docker.sock`
**Step 2: Create Nexus Docker Container**
To create a Docker container running Nexus 3 and exposing it on port 8081, use the following command:

`docker run -d --name nexus -p 8081:8081 sonatype/nexus3:latest`
This command does the following:

`-d`
: Detaches the container and runs it in the background.`--name nexus`
: Names the container "nexus".`-p 8081:8081`
: Maps port 8081 on the host to port 8081 on the container, allowing access to Nexus through port 8081.`sonatype/nexus3:latest`
: Uses the latest version of Nexus 3 from the Sonatype repository.
After running this command, Nexus will be accessible on your host machine at `http://<your_IP>:8081`
.

**Step 3: Retrieve Nexus Initial Password**
To access the Nexus initial admin password stored in the container, follow these steps:

**Get the Container ID**: List all running containers to find the ID of the Nexus container.
`docker ps`
**2. Access Container’s Bash Shell**: Execute the following command to access the container’s bash shell:
`docker exec -it <container_ID> /bin/bash`
Replace `<container_ID>`
with the actual ID of the Nexus container.

**3. Navigate to Nexus Directory**: Inside the container’s bash shell, navigate to the directory where Nexus stores its configuration:
`cd sonatype-work/nexus3`
**4. View Admin Password**: Display the contents of the `admin.password`
file to view the admin password:
`cat admin.password`
**5. Exit the Container Shell**: Once you have retrieved the password, exit the container’s bash shell:
`exit`
This process allows you to access the Nexus admin password stored within the container. Make sure to keep this password secure, as it grants administrative access to your Nexus instance.

Note: while setting password in nexus — Allow Anonymous Access

Use Case Example :

Example Scenario

Suppose you have a documentation server for an open-source project. You want to make the project’s documentation accessible to everyone without requiring users to create an account. Here’s how you might configure it:

Access: Enable anonymous access.
Username: Set to “anonymous”.
Realm: Set to “Local Authorizing Realm” to define the context in which the anonymous user operates.This setup ensures that anyone can access the documentation without needing to authenticate, making the information widely available and easy to access.

By carefully considering the use cases and configuring the settings appropriately, you can leverage anonymous access to improve accessibility while maintaining security and control over sensitive resources.

## 5. Setting Up SonarQube
**Step 1: Install Docker**
First, we need to install Docker. Save the following script in a file named `install_docker.sh`
:

`#!/bin/bash`
# Update package manager repositories
sudo apt-get update
# Install necessary dependencies
sudo apt-get install -y ca-certificates curl
# Create directory for Docker GPG key
sudo install -m 0755 -d /etc/apt/keyrings
# Download Docker's GPG key
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
# Ensure proper permissions for the key
sudo chmod a+r /etc/apt/keyrings/docker.asc
# Add Docker repository to Apt sources
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo \"$VERSION_CODENAME\") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
# Update package manager repositories again
sudo apt-get update
# Install Docker packages
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
Make the script executable and run it:

`chmod +x install_docker.sh`
./install_docker.sh
Give permission to other users to run Docker commands:

`sudo chmod 666 /var/run/docker.sock`
**Step 2: Create SonarQube Docker Container**
To run SonarQube in a Docker container, use the following command:

`docker run -d --name sonar -p 9000:9000 sonarqube:lts-community`
This command does the following:

`-d`
: Detaches the container and runs it in the background.`--name sonar`
: Names the container "sonar".`-p 9000:9000`
: Maps port 9000 on the host to port 9000 on the container, allowing access to SonarQube through port 9000.`sonarqube:lts-community`
: Uses the long-term support (LTS) community edition of SonarQube from the Docker Hub.
After running this command, SonarQube will be accessible on your host machine at `http://<your_VM_IP>:9000`
.

**Step 3: Access SonarQube**
To access SonarQube, open a web browser and navigate to `http://<your_VM_IP>:9000`
.

This will start the SonarQube server, and you should be able to access it using the provided URL. If you’re running Docker on a remote server or a different port, replace `<your_VM_IP>`
with the appropriate hostname or IP address and adjust the port accordingly.

Note: This is the end of **Part 1: Infrastructure Setup,** part-2 will cover** **Source Code Management