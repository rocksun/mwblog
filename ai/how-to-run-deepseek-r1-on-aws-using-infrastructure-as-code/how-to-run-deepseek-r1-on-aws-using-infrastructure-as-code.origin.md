# How To Run DeepSeek R1 on AWS Using Infrastructure as Code
![Featued image for: How To Run DeepSeek R1 on AWS Using Infrastructure as Code](https://cdn.thenewstack.io/media/2025/02/62854451-nubelson-fernandes-gts2w7bu3qo-unsplash-1024x683.jpg)
[Nubelson Fernandes](https://unsplash.com/@nublson?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/man-in-black-long-sleeve-shirt-wearing-black-headphones-sitting-on-chair-gTs2w7bu3Qo?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
This weekend, I changed my perspective on open source AI deployment. While scrolling through my social feeds, I noticed many posts about DeepSeek, a new open-source language model, causing a stir in the AI community. As someone who regularly deploys infrastructure for production environments, I was intrigued by DeepSeek’s promise of competitive performance at a fraction of the cost of major commercial models.

What caught my attention wasn’t just the benchmark numbers. However, DeepSeek’s 79.8% score on AIME 2024 mathematics tests is impressive, but rather the practical possibility of running these models on standard cloud infrastructure. I decided to put this to the test by deploying DeepSeek on [AWS](https://aws.amazon.com/?utm_content=inline+mention) using Pulumi for infrastructure as code. Here’s what I learned from the experience.

**Understanding DeepSeek’s Place in the AI Landscape**
DeepSeek emerged from a Chinese AI startup founded in 2023. It brings something unique: High-performance language models released under the MIT license. While companies like OpenAI and Meta spend enormous resources on their models, DeepSeek achieves comparable results with significantly less investment.

![](https://cdn.thenewstack.io/media/2025/02/c8b1197b-deepseek1-1024x610.png)
Source: DeepSeek

In my testing, DeepSeek R1 demonstrated capabilities that make it particularly valuable for practical applications:

- Mathematics processing with 79.8% accuracy on AIME 2024 tests.
- Software engineering tasks with 49.2% accuracy on SWE-bench Verified.
- General knowledge handling with a 90.8% score on MMLU.
What makes this especially interesting for development teams is the availability of distilled versions with 1.5B to 70B parameters, allowing deployment on various hardware configurations, from local machines to cloud instances.

**Deploying DeepSeek: A Practical Infrastructure Approach**
After evaluating DeepSeek’s capabilities, I created a reproducible deployment process using [Pulumi](https://www.pulumi.com/) and AWS. The goal was to establish a GPU-powered environment that could efficiently handle the model while remaining cost-effective.

The deployment architecture I developed consists of three main components:

- A GPU-enabled EC2 instance (g4dn.xlarge) for model hosting.
- Ollama for
[model management and API](https://thenewstack.io/7-llm-risks-and-api-management-strategies/)compatibility. - Open WebUI for interaction and testing.
Here’s the real-world deployment process I developed, focusing on maintainability and scalability:

### Prerequisites
Before embarking on our self-hosted DeepSeek model journey, ensure you have:

- An
[AWS account;](https://aws.amazon.com/account/) - Pulumi CLI installed;
[AWS CLI](https://aws.amazon.com/cli/)installed;- A basic understanding of
[Ollama](https://ollama.com/), a tool that simplifies running large language models (LLMs) on your hardware.
Creating the Infrastructure

To get started, I created a new Pulumi project:

1 |
pulumi new aws-typescript |
I chose TypeScript for this example, but you can select any language you prefer.
After setting up the project, I deleted the sample code and replaced it with the following configurations.

### Create an Instance Role With S3 Access
To download the NVIDIA drivers, I [needed to create](https://thenewstack.io/security-needs-create-more-work-for-open-source-maintainers/) an instance role with S3 access (AmazonS3ReadOnlyAccess is enough here)

1234567891011121314151617181920212223242526272829303132 |
import * as pulumi from "@pulumi/pulumi";import * as aws from "@pulumi/aws";import * as fs from "fs";const role = new aws.<em>iam</em>.Role("deepSeekRole", { name: "deepseek-role", assumeRolePolicy: <em>JSON</em>.stringify({ Version: "2012-10-17", Statement: [ { Action: "sts:AssumeRole", Effect: "Allow", Principal: { Service: "ec2.amazonaws.com", }, }, ], }),});new aws.<em>iam</em>.RolePolicyAttachment("deepSeekS3Policy", { policyArn: "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess", role: role.name,});const instanceProfile = new aws.<em>iam</em>.InstanceProfile("deepSeekProfile", { name: "deepseek-profile", role: role.name,}); |
### Create the Network
Next, I needed to create a VPC, subnet, Internet Gateway, and route table. This is all done with the following code snippet:

12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364 |
const vpc = new aws.<em>ec2</em>.Vpc("deepSeekVpc", { cidrBlock: "10.0.0.0/16", enableDnsHostnames: true, enableDnsSupport: true,});const subnet = new aws.<em>ec2</em>.Subnet("deepSeekSubnet", { vpcId: vpc.id, cidrBlock: "10.0.48.0/20", availabilityZone: pulumi.interpolate`${aws.<em>getAvailabilityZones</em>().then(it => it.names[0])}`, mapPublicIpOnLaunch: true,});const internetGateway = new aws.<em>ec2</em>.InternetGateway("deepSeekInternetGateway", { vpcId: vpc.id,});const routeTable = new aws.<em>ec2</em>.RouteTable("deepSeekRouteTable", { vpcId: vpc.id, routes: [ { cidrBlock: "0.0.0.0/0", gatewayId: internetGateway.id, }, ],});const routeTableAssociation = new aws.<em>ec2</em>.RouteTableAssociation("deepSeekRouteTableAssociation", { subnetId: subnet.id, routeTableId: routeTable.id,});const securityGroup = new aws.<em>ec2</em>.SecurityGroup("deepSeekSecurityGroup", { vpcId: vpc.id, egress: [ { fromPort: 0, toPort: 0, protocol: "-1", cidrBlocks: ["0.0.0.0/0"], }, ], ingress: [ { fromPort: 22, toPort: 22, protocol: "tcp", cidrBlocks: ["0.0.0.0/0"], }, { fromPort: 3000, toPort: 3000, protocol: "tcp", cidrBlocks: ["0.0.0.0/0"], }, { fromPort: 11434, toPort: 11434, protocol: "tcp", cidrBlocks: ["0.0.0.0/0"], }, ],}); |
### Create the EC2 Instance
Finally, I can create the EC2 instance. For this, I need to [create a SSH key](https://thenewstack.io/create-and-manage-shh-keys-for-third-party-integration/) pair and retrieve the Amazon Machine Images to use in our instances.

I also use a `g4dn.xlarge`
, but you can change the instance type to any other instance type that supports GPU. You can find more information about the [instance types](https://aws.amazon.com/ec2/instance-types/g4/).

If you need to create the key pair, run the following command:

123 |
openssl genrsa -out deepseek.pem 2048openssl rsa -in deepseek.pem -pubout > deepseek.pubssh-keygen -f mykey.pub -i -mPKCS8 > deepseek.pem |
1234567891011121314151617181920212223242526272829303132333435363738394041 |
const keyPair = new aws.<em>ec2</em>.KeyPair("deepSeekKey", { publicKey: pulumi.output(fs.readFileSync("deepseek.rsa", "utf-8")),});const deepSeekAmi = aws.<em>ec2</em><em> </em>.<em>getAmi</em>({ filters: [ { name: "name", values: ["amzn2-ami-hvm-2.0.*-x86_64-gp2"], }, { name: "architecture", values: ["x86_64"], }, ], owners: ["137112412989"], // Amazon mostRecent: true, }) .then(ami => ami.id);const deepSeekInstance = new aws.<em>ec2</em>.Instance("deepSeekInstance", { ami: deepSeekAmi, instanceType: "g4dn.xlarge", keyName: keyPair.keyName, rootBlockDevice: { volumeSize: 100, volumeType: "gp3", }, subnetId: subnet.id, vpcSecurityGroupIds: [securityGroup.id], iamInstanceProfile: instanceProfile.name, userData: fs.readFileSync("cloud-init.yaml", "utf-8"), tags: { Name: "deepSeek-server", },});export const <em>amiId </em>= deepSeekAmi;export const <em>instanceId </em>= deepSeekInstance.id;export const <em>instancePublicIp </em>= deepSeekInstance.publicIp; |
Then, we configure the GPU instance with proper drivers and dependencies, install Ollama and run DeepSeek with this cloud config.
1234567891011121314151617181920212223242526272829303132333435 |
#cloud-configusers:- defaultpackage_update: truepackages:- apt-transport-https- ca-certificates- curl- openjdk-17-jre-headless- gccruncmd:- yum install -y gcc kernel-devel-$(uname -r)- aws s3 cp --recursive s3://ec2-linux-nvidia-drivers/latest/ .- chmod +x NVIDIA-Linux-x86_64*.run- /bin/sh ./NVIDIA-Linux-x86_64*.run --tmpdir . --silent- touch /etc/modprobe.d/nvidia.conf- echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append /etc/modprobe.d/nvidia.conf- yum install -y docker- usermod -a -G docker ec2-user- systemctl enable docker.service- systemctl start docker.service- curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo- yum install -y nvidia-container-toolkit- nvidia-ctk runtime configure --runtime=docker- systemctl restart docker- docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama --restart always ollama/ollama- sleep 120- docker exec ollama ollama run deepseek-r1:7b- docker exec ollama ollama run deepseek-r1:14b- docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main |
### Deploying the Infrastructure
With all configurations in place, we can deploy the infrastructure using:

1 |
pulumi up |
This command provides a preview of the changes, allowing you to confirm before proceeding. Once confirmed, Pulumi creates the resources, and after some time, the EC2 instance is ready with DeepSeek R1 running.
### Access the Ollama Web UI
To retrieve the public IP address of our EC2 instance, I used the following command to instruct Pulumi to print out the configuration:

12 |
pulumi stack output instancePublicIp<yout-ip> |
I then opened web UI with this address: `http://<ip>:3000/`
### Use DeepSeek R1
Head to the dropdown in the upper right corner and select the model you want to use.

I selected deepseek-r1:14b to test my model.

Finally, I used the central chat box to begin using the model. My example prompt is: **What are Pulumi’s benefits?**
### Cleaning up
After you are done experimenting with DeepSeek, I clean up the resources by running the following command:

1 |
pulumi destroy |
**Looking Forward**
DeepSeek represents a significant step forward in accessible AI deployment. The combination of MIT licensing and competitive performance could make it a viable option for production environments.

For teams considering DeepSeek deployment, I recommend:

- Starting with the 7B model for a balanced performance/resource ratio.
- Using infrastructure as code (like Pulumi) for reproducible deployments.
- Implementing proper monitoring and scaling policies.
- Testing thoroughly with production-like workloads before deployment.
My GitHub repository [contains the code and configuration files from this deployment](https://thenewstack.io/deploy-mongodb-in-a-container-access-it-outside-the-cluster/), allowing others to build upon this foundation for their AI infrastructure needs.

This experience has shown me that enterprise-grade AI deployment is increasingly accessible to smaller teams. As we continue to see advances in [model efficiency and deployment](https://thenewstack.io/5-steps-to-deploy-efficient-cloud-native-foundation-ai-models/) tools, the barrier to entry for production AI will continue to lower, opening new possibilities for innovation across the industry.

If you’re interested in exploring AI models or need a robust setup for your projects, consider trying DeepSeek with Pulumi. Remember, while the setup is straightforward, [securing your instance and understanding](https://thenewstack.io/understanding-nist-csf-and-mitre-attck-security-frameworks/) the model’s capabilities are crucial steps before going live.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)