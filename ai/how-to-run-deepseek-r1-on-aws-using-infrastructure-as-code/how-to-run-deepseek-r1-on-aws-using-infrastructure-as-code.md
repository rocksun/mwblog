
<!--
title: 使用基础设施即代码在AWS上运行DeepSeek R1
cover: https://cdn.thenewstack.io/media/2025/02/62854451-nubelson-fernandes-gts2w7bu3qo-unsplash-scaled.jpg
-->

MIT 许可证和具有竞争力的性能相结合，使其成为生产环境的可行选择。

> 译自 [How To Run DeepSeek R1 on AWS Using Infrastructure as Code](https://thenewstack.io/how-to-run-deepseek-r1-on-aws-using-infrastructure-as-code/)，作者 Engin Diri Engin。

这个周末，我改变了对开源 AI 部署的看法。在浏览我的社交信息流时，我注意到许多关于 DeepSeek 的帖子，DeepSeek 是一种新的开源语言模型，在 AI 社区引起了轰动。作为一名经常为生产环境部署基础设施的人，DeepSeek 以极低的成本提供具有竞争力的性能的承诺让我很感兴趣。

引起我注意的不仅仅是基准测试数字。然而，DeepSeek 在 AIME 2024 数学测试中获得 79.8% 的分数令人印象深刻，但更重要的是在标准云基础设施上运行这些模型的实际可能性。我决定通过使用 Pulumi 作为基础设施即代码在 [AWS](https://aws.amazon.com/?utm_content=inline+mention) 上部署 DeepSeek 来对此进行测试。以下是我从这次体验中学到的东西。

## 了解 DeepSeek 在 AI 领域中的地位

DeepSeek 诞生于一家 2023 年成立的中国 AI 初创公司。它带来了一些独特的东西：在 MIT 许可下发布的高性能语言模型。虽然 OpenAI 和 Meta 等公司在其模型上投入了巨资，但 DeepSeek 以更少的投资取得了可比的结果。

![](https://cdn.thenewstack.io/media/2025/02/c8b1197b-deepseek1-1024x610.png)

*资料来源：DeepSeek*

在我的测试中，DeepSeek R1 展示了使其对实际应用特别有价值的功能：

- 在 AIME 2024 测试中，数学处理准确率为 79.8%。
- 在 SWE-bench Verified 上，软件工程任务的准确率为 49.2%。
- 在 MMLU 上，一般知识处理得分 90.8%。

对于开发团队来说，特别有趣的是，可以使用参数为 15 亿到 700 亿个的不同版本，允许在各种硬件配置上进行部署，从本地机器到云实例。

## 部署 DeepSeek：一种实用的基础设施方法

在评估了 DeepSeek 的功能后，我使用 [Pulumi](https://www.pulumi.com/) 和 AWS 创建了一个可重复的部署流程。目标是建立一个能够有效处理模型同时保持成本效益的 GPU 驱动环境。

我开发的部署架构包含三个主要组件：

1. 用于模型托管的启用 GPU 的 EC2 实例 (g4dn.xlarge)。
2. 用于[模型管理和 API](https://thenewstack.io/7-llm-risks-and-api-management-strategies/)兼容性的 Ollama。
3. 用于交互和测试的 Open WebUI。

这是我开发的实际部署流程，重点是可维护性和可扩展性：

![](https://cdn.thenewstack.io/media/2025/02/a9d23d80-deepseek12.png)

### 先决条件

在开始我们的自托管 DeepSeek 模型之旅之前，请确保您拥有：

- 一个[AWS 账户；](https://aws.amazon.com/account/)
- 已安装 Pulumi CLI；
- 已安装[AWS CLI](https://aws.amazon.com/cli/)；
- 对[Ollama](https://ollama.com/) 的基本了解，Ollama 是一种简化在您的硬件上运行大型语言模型 (LLM) 的工具。

### 创建基础设施

首先，我创建了一个新的 Pulumi 项目：

```
pulumi new aws-typescript
```

我选择 TypeScript 作为此示例，但您可以选择任何您喜欢的语言。

设置项目后，我删除了示例代码并将其替换为以下配置。

### 创建具有 S3 访问权限的实例角色

为了下载 NVIDIA 驱动程序，我[需要创建一个](https://thenewstack.io/security-needs-create-more-work-for-open-source-maintainers/)具有 S3 访问权限的实例角色（此处 AmazonS3ReadOnlyAccess 足够）

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as fs from "fs";

const role = new aws.iam.Role("deepSeekRole", {
    name: "deepseek-role",
    assumeRolePolicy: JSON.stringify({
        Version: "2012-10-17",
        Statement: [
            {
                Action: "sts:AssumeRole",
                Effect: "Allow",
                Principal: {
                    Service: "ec2.amazonaws.com",
                },
            },
        ],
    }),
});

new aws.iam.RolePolicyAttachment("deepSeekS3Policy", {
    policyArn: "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess",
    role: role.name,
});

const instanceProfile = new aws.iam.InstanceProfile("deepSeekProfile", {
    name: "deepseek-profile",
    role: role.name,
});
```

### 创建网络

接下来，我需要创建一个 VPC、子网、互联网网关和路由表。所有这些都使用以下代码片段完成：

```js
const vpc = new aws.ec2.Vpc("deepSeekVpc", {
   cidrBlock: "10.0.0.0/16",
   enableDnsHostnames: true,
   enableDnsSupport: true,
});
const subnet = new aws.ec2.Subnet("deepSeekSubnet", {
   vpcId: vpc.id,
   cidrBlock: "10.0.48.0/20",
   availabilityZone: pulumi.interpolate`${aws.getAvailabilityZones().then(it =&gt; it.names[0])}`, 
   mapPublicIpOnLaunch: true,
});
 
const internetGateway = new aws.ec2.InternetGateway("deepSeekInternetGateway", {
   vpcId: vpc.id,
 
});
const routeTable = new aws.ec2.RouteTable("deepSeekRouteTable", {
   vpcId: vpc.id,
   routes: [
       {
           cidrBlock: "0.0.0.0/0",
           gatewayId: internetGateway.id,
       },
   ],
});
 
 
const routeTableAssociation = new aws.ec2.RouteTableAssociation("deepSeekRouteTableAssociation", {
   subnetId: subnet.id,
   routeTableId: routeTable.id,
});
 
 
const securityGroup = new aws.ec2.SecurityGroup("deepSeekSecurityGroup", {
   vpcId: vpc.id,
   egress: [
       {
           fromPort: 0,
           toPort: 0,
           protocol: "-1",
           cidrBlocks: ["0.0.0.0/0"],
       },
   ],
   ingress: [
       {
           fromPort: 22,
           toPort: 22,
           protocol: "tcp",
           cidrBlocks: ["0.0.0.0/0"],
       },
       {
           fromPort: 3000,
           toPort: 3000,
           protocol: "tcp",
           cidrBlocks: ["0.0.0.0/0"],
       },
       {
           fromPort: 11434,
           toPort: 11434,
           protocol: "tcp",
           cidrBlocks: ["0.0.0.0/0"],
       },
   ],
});
```

### 创建EC2实例

最后，我可以创建EC2实例。为此，我需要[创建一个SSH密钥对](https://thenewstack.io/create-and-manage-shh-keys-for-third-party-integration/)并检索实例中使用的Amazon机器镜像。

我还使用`g4dn.xlarge`，但是您可以将实例类型更改为任何其他支持GPU的实例类型。您可以找到有关[实例类型](https://aws.amazon.com/ec2/instance-types/g4/)的更多信息。

如果需要创建密钥对，请运行以下命令：

```bash
openssl genrsa -out deepseek.pem 2048
openssl rsa -in deepseek.pem -pubout > deepseek.pub
ssh-keygen -f mykey.pub -i -mPKCS8 > deepseek.pem
```

```js
const keyPair = new aws.ec2.KeyPair("deepSeekKey", {
   publicKey: pulumi.output(fs.readFileSync("deepseek.rsa", "utf-8")),
});
 
const deepSeekAmi = aws.ec2
   .getAmi({
       filters: [
           {
               name: "name",
               values: ["amzn2-ami-hvm-2.0.*-x86_64-gp2"],
           },
           {
               name: "architecture",
               values: ["x86_64"],
           },
       ],
       owners: ["137112412989"], // Amazon
       mostRecent: true,
   })
   .then(ami =&gt; ami.id);
 
const deepSeekInstance = new aws.ec2.Instance("deepSeekInstance", {
   ami: deepSeekAmi,
   instanceType: "g4dn.xlarge",
   keyName: keyPair.keyName,
   rootBlockDevice: {
       volumeSize: 100,
       volumeType: "gp3",
   },
   subnetId: subnet.id,
   vpcSecurityGroupIds: [securityGroup.id],
   iamInstanceProfile: instanceProfile.name,
   userData: fs.readFileSync("cloud-init.yaml", "utf-8"),
   tags: {
       Name: "deepSeek-server",
   },
});
 
export const amiId = deepSeekAmi;
export const instanceId = deepSeekInstance.id;
export const instancePublicIp = deepSeekInstance.publicIp;
```

然后，我们使用正确的驱动程序和依赖项配置GPU实例，安装Ollama并使用此云配置运行DeepSeek。

```yaml
#cloud-config
users:
  - default
package_update: true
packages:
  - apt-transport-https
  - ca-certificates
  - curl
  - openjdk-17-jre-headless
  - gcc
runcmd:
  - yum install -y gcc kernel-devel-$(uname -r)
  - aws s3 cp --recursive s3://ec2-linux-nvidia-drivers/latest/ .
  - chmod +x NVIDIA-Linux-x86_64*.run
  - /bin/sh ./NVIDIA-Linux-x86_64*.run --tmpdir . --silent
  - touch /etc/modprobe.d/nvidia.conf
  - echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append /etc/modprobe.d/nvidia.conf
  - yum install -y docker
  - usermod -a -G docker ec2-user
  - systemctl enable docker.service
  - systemctl start docker.service
  - curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
  - yum install -y nvidia-container-toolkit-nvidia-ctk
  - runtime configure --runtime=docker
  - systemctl restart docker
  - docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama --restart always ollama/ollama
  - sleep 120
  - docker exec ollama ollama run deepseek-r1:7b
  - docker exec ollama ollama run deepseek-r1:14b
  - docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

### 部署基础设施

所有配置就绪后，我们可以使用以下命令部署基础设施：

```bash
pulumi up
```

此命令提供更改预览，允许您在继续之前进行确认。确认后，Pulumi 将创建资源，一段时间后，EC2 实例将准备就绪，并运行 DeepSeek R1。

### 访问 Ollama Web UI

为了检索我的 EC2 实例的公网 IP 地址，我使用以下命令指示 Pulumi 打印出配置：

```bash
pulumi stack output instancePublicIp<yout-ip>
```

然后我使用此地址打开了 Web UI：`http://<ip>:3000/`

### 使用 DeepSeek R1

前往右上角的下拉菜单，选择您要使用的模型。

![](https://cdn.thenewstack.io/media/2025/02/bbce6af4-source-deepseek3-1024x424.png)

我选择了 `deepseek-r1:14b` 来测试我的模型。

![](https://cdn.thenewstack.io/media/2025/02/e90efbef-source-deepseek4-1024x453.png)

最后，我使用中央聊天框开始使用该模型。我的示例提示是：**What are Pulumi’s benefits?**

![](https://cdn.thenewstack.io/media/2025/02/ec596b33-source-deepseek5-1024x512.png)

### 清理

完成 DeepSeek 的实验后，我通过运行以下命令清理资源：

```bash
pulumi destroy
```

## 展望未来

DeepSeek 代表了易于访问的 AI 部署方面的一大进步。MIT 许可证和具有竞争力的性能相结合，使其成为生产环境的可行选择。

对于正在考虑部署 DeepSeek 的团队，我建议：

- 从 7B 模型开始，以获得平衡的性能/资源比率。
- 使用基础设施即代码（如 Pulumi）进行可重复的部署。
- 实施适当的监控和扩展策略。
- 在部署之前使用类似生产环境的工作负载进行彻底测试。

我的 GitHub 仓库[包含此部署的代码和配置文件](https://thenewstack.io/deploy-mongodb-in-a-container-access-it-outside-the-cluster/)，允许其他人以此为基础构建其 AI 基础设施需求。

这次经历向我表明，企业级 AI 部署越来越容易为小型团队所及。随着我们继续看到[模型效率和部署](https://thenewstack.io/5-steps-to-deploy-efficient-cloud-native-foundation-ai-models/)工具的进步，生产 AI 的进入门槛将继续降低，为整个行业的创新开辟新的可能性。

如果您有兴趣探索 AI 模型或需要为您的项目建立强大的设置，请考虑尝试使用 Pulumi 部署 DeepSeek。请记住，虽然设置很简单，但[保护您的实例和理解](https://thenewstack.io/understanding-nist-csf-and-mitre-attck-security-frameworks/)模型的功能是在上线之前至关重要的步骤。
