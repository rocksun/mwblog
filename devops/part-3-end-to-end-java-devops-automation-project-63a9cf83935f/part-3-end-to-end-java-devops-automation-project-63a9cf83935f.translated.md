# 第 3 部分：端到端 Java DevOps 自动化项目

**先决条件**: [第 2 部分：端到端 Java DevOps 自动化项目](https://medium.com/p/0b94eedad757/edit)

## 使用 Jenkins 设置 CI/CD

### 在 Jenkins 中安装插件

**1. Eclipse Temurin 安装程序**

— 自动安装和配置 Eclipse Temurin JDK。

— 安装：

— Jenkins 仪表板 -> 管理 Jenkins -> 管理插件 -> 可用选项卡。

— 搜索“Eclipse Temurin Installer”并选择它。

— 点击“不重启安装”。

**2. Pipeline Maven 集成**

— 为 Jenkins Pipeline 提供 Maven 支持。

**3. 配置文件提供程序**

— 允许您在 Jenkins 中集中定义和使用配置文件。

**4. SonarQube 扫描程序**

— 将 Jenkins 与 SonarQube 集成，用于代码质量和安全分析。

**5. Kubernetes CLI**

— 允许 Jenkins 使用 `kubectl` 与 Kubernetes 集群交互。

**6. Kubernetes**

— 将 Jenkins 与 Kubernetes 集成，允许 Jenkins 代理作为 Pod 运行。

**7. Docker**

— 使 Jenkins 能够与 Docker 交互以构建和管理容器。

**8. Docker Pipeline**

— 使用 Docker 特定步骤扩展 Jenkins Pipeline。

**9. Maven 集成**

— 使您的项目保持同步，并确保它们始终使用最新更新进行测试。

### 在 Jenkins 服务器上安装和配置 Trivy

- 注意：没有用于 Trivy 的 Jenkins 插件，因此请直接在 Jenkins 服务器上安装它，并将其添加到您的 Jenkins Pipeline 阶段。

Trivy 安装命令

```bash
sudo apt-get install wget apt-transport-https gnupg lsb-release -y
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | sudo tee -a /etc/apt/sources.list.d/trivy.list
sudo apt-get update -y
sudo apt-get install trivy -y
trivy -v
```

# 预期输出：版本：0.53.0（或最新版本）

### 全局工具配置：

“全局工具配置”部分（以前称为“管理 Jenkins -> 配置工具”）是您定义和管理 Jenkins 在所有作业中使用的工具的地方。这包括编译器、构建工具以及构建项目所需的其它实用程序。

### 创建 Git 凭据作为全局凭据

使用 GitHub 用户名作为用户名，使用我们在第 2 部分（设置私有存储库时）创建的令牌作为密码值

“**凭据**”部分允许您管理 Jenkins 用于安全地与外部系统交互的凭据。凭据可以包括用户名和密码、SSH 密钥、API 令牌等等。

从这里开始，我们将开始编写 Jenkins Pipeline 代码，您可以从该文件获取完整代码：[pipeline.groovy](https://github.com/navin5556/devops-pipeline-kubernetes/blob/main/phase-3/pipeline.groovy)，并逐步执行。

### Jenkins Pipeline 设置步骤：

- 创建作业名称：**BoardGame**，类型为 Pipeline
- 启用 — 丢弃旧构建（要保留的最大构建数 = 2）

### 管理 Jenkins -> 系统

“**系统**”部分位于“管理 Jenkins”下，您可以在其中配置 Jenkins 的整体系统设置。这包括影响整个 Jenkins 安装及其运行方式的设置。

### 配置 SonarQube 服务器

在 Jenkins Pipeline 中编写 SonarQube 分析阶段之前，您需要在 Jenkins 中配置 SonarQube 服务器。以下是执行此操作的步骤：

**1. 获取 SonarQube 服务器凭据**:

. 转到 SonarQube 服务器 -> 管理 -> 安全 -> 用户 -> 令牌

**2. 在 Jenkins 中创建全局凭据**:

**3. 在 Jenkins 中配置 SonarQube 服务器**:

在 Jenkins Pipeline 中编写 SonarQube 质量门阶段之前的步骤，

转到 SonarQube 服务器 -> 管理 -> 配置 -> Webhook -> 令牌

添加 Jenkins IP：

以下是 SonarQube 和 Jenkins 集成完整架构的参考：

## 配置 Nexus

在编写 **发布到 Nexus** 工件阶段的代码之前，我们需要在 POM 文件中添加存储库 URL。

要配置 Jenkins 中的全局 Maven 设置，请执行以下步骤：

**1. 导航到配置：**

- 转到 **管理 Jenkins**->**管理文件**。
- 添加一个新的配置文件。

**2. 设置配置类型和 ID：**

- 选择配置类型为 **全局 Maven settings.xml**。
- 将配置文件的 ID 设置为 `global-settings`.

**3. 编辑内容：**

- 通过在 `<servers>` 标签内添加以下代码来编辑配置文件的内容：

```xml
<servers>
<server>
<id>maven-releases</id>
<username>nexus username</username>
<password>nexus password</password>
</server>
<server>
<id>maven-snapshots</id>
<username>nexus username</username>
<password>nexus password</password>
</server>
</servers>
```

将 `nexus username` 和 `nexus password` 替换为您的实际 Nexus 凭据。

通过执行这些步骤，您将在 Jenkins 中配置全局 Maven 设置，以包含必要的 Nexus 存储库凭据。
Jenkins 的“管理 Jenkins”下的“管理文件”部分用于处理集中管理的配置文件，这些文件可以在 Jenkins 作业中引用。此功能是 Config File Provider 插件的一部分。

## 设置 Docker-hub 凭据：
**阶段：部署到 Kubernetes 集群**
通过运行以下命令在 Jenkins 服务器上安装 **KUBECTL**

```
curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.19.6/2021-01-05/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin
kubectl version --short --client
```

为了正确且安全地将应用程序部署到 Kubernetes 集群，我们需要遵循正确的流程，例如创建服务帐户和使用基于角色的访问控制 (RBAC)。

RBAC 代表基于角色的访问控制。假设我们的项目中有三个用户：

- 用户 1：具有全面知识的架构师。
- 用户 2：中级人员。
- 用户 3：实习生或非常新的人。在使用 Kubernetes 时，我们不能授予新人或中级人员完全访问权限。因此，我们创建角色：

1.

角色 1：集群管理员访问权限
— 对集群拥有完全访问权限。
— 此角色分配给架构师（用户 1）。2.

角色 2：中级访问权限
— 具有良好的权限级别，但不是完全的管理员。
— 此角色分配给中级人员（用户 2）。3.

角色 3：只读访问权限
— 仅允许查看资源，没有修改权限。
— 此角色分配给实习生（用户 3）。这种方法通过不向所有人授予完全访问权限来确保安全性。相反，我们创建具有适当权限的特定角色，并将它们分配给相应的用户。

现在，让我们继续通过创建服务帐户来使我们的部署安全。

1. 创建服务帐户：
— 此帐户将用于管理权限和控制访问级别。通过遵循这些步骤，我们确保我们的 Kubernetes 部署安全且得到妥善管理。现在，让我们进入实际部分并创建服务帐户。

请参考此文件：[service-role-for-jenkins.md](https://github.com/navin5556/devops-pipeline-kubernetes/blob/main/phase-3/service-role-for-jenkins.md) 创建用于 Jenkins 的服务帐户。

创建服务帐户后，将 **secret/mysecretname** 的复制令牌粘贴到 **Jenkins 全局凭据**中：

**在 Jenkins 中设置 HTML 电子邮件通知**
在 Jenkins 中配置电子邮件的步骤：

现在使用此应用程序密码在 Jenkins 中创建凭据：

提供的命令是 Jenkins 管道 `post`
块，它始终在主管道阶段运行后执行某些操作。此特定块发送包含 Jenkins 构建详细信息的电子邮件通知。以下是其使用情况和功能的细分：

# 关键组件：
:**post { always { ... } }**
- 此块确保在每次构建后执行封闭的脚本，无论结果如何（成功、失败等）。
**环境变量和参数**:
`jobName = env.JOB_NAME`
: 获取 Jenkins 作业的名称。`buildNumber = env.BUILD_NUMBER`
: 获取构建编号。`pipelineStatus = currentBuild.result ?: 'UNKNOWN'`
: 获取当前构建结果；如果结果为空，则默认为 'UNKNOWN'。`bannerColor = pipelineStatus.toUpperCase() == 'SUCCESS' ? 'green' : 'red'`
: 根据构建状态设置横幅颜色（成功为 'green'，否则为 'red'）。
**电子邮件正文构建**:
- 使用 HTML 模板构建电子邮件正文，显示作业名称、构建编号和构建状态。横幅的背景颜色根据构建结果而变化。
**emailext**** 步骤**:
: 将电子邮件主题设置为包含作业名称、构建编号和构建状态。**subject**
: 设置电子邮件的 HTML 正文。**body**
: 指定收件人的电子邮件地址（您的电子邮件：'naveenkumarsingh5556@gmail.com'）。**to****from****and**
: 设置发件人的电子邮件地址（此处为 'jenkins@example.com'）。**replyTo**
: 指定电子邮件内容类型为 HTML。**mimeType**
: 包含附件模式以附加指定的报告文件（此处为 'trivy-image-report.html'）。**attachmentsPattern**
**总结**:
**目的**: 通过电子邮件通知 Jenkins 作业构建状态。**执行**: 始终在构建后执行。**电子邮件中的详细信息**: 作业名称、构建编号、构建状态、控制台输出链接以及附加的报告。**自定义**: 横幅颜色根据构建结果而变化（成功为绿色，失败或其他状态为红色）。
此命令有助于通过自动电子邮件通知系统使利益相关者了解构建状态。

最终结果：

总结：
## 本文介绍了使用 Jenkins 为 Java DevOps 自动化项目设置全面的 CI/CD 管道的步骤。关键步骤包括安装必要的 Jenkins 插件，配置 SonarQube、Nexus、Docker 和 Kubernetes 等工具，以及设置全局凭据。我们还演示了如何使用基于角色的访问控制 (RBAC) 将应用程序安全地部署到 Kubernetes 集群，以及如何配置 HTML 电子邮件通知以获取构建状态更新。通过遵循这些步骤，您可以确保为您的 Java 应用程序建立一个健壮、自动化和安全的部署管道。