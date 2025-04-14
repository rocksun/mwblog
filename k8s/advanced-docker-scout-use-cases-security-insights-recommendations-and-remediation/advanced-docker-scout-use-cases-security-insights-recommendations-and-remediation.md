<!--
title: Docker Scout 高级用例：安全洞察、建议和修复
cover: https://cdn.thenewstack.io/media/2025/04/60c7696d-chuttersnap-xewrfld8eme-unsplash-scaled.jpg
summary: 告别传统漏洞扫描！Docker Scout 深入洞察容器安全，不仅识别 CVE，更提供修复建议和自动化补丁。无缝集成 CI/CD 管道，实现 DevSecOps，保障 Kubernetes 环境安全。用 Docker Scout 提升容器安全策略，告别被动防御！
-->

告别传统漏洞扫描！Docker Scout 深入洞察容器安全，不仅识别 CVE，更提供修复建议和自动化补丁。无缝集成 CI/CD 管道，实现 DevSecOps，保障 Kubernetes 环境安全。用 Docker Scout 提升容器安全策略，告别被动防御！

> 译自：[Advanced Docker Scout Use Cases: Security Insights, Recommendations, and Remediation](https://thenewstack.io/advanced-docker-scout-use-cases-security-insights-recommendations-and-remediation/)
> 
> 作者：Advait Patel

防止容器化应用程序的风险不仅仅是检查已知的威胁。Docker Scout 通过丰富的上下文、自动化的修复以及被动集成到 DevSecOps 流程中，提供了改进的保护。与识别缺陷的传统漏洞扫描工具不同，[Docker Scout 修复了问题](https://thenewstack.io/why-docker-scout-is-changing-how-developers-scan-for-vulnerabilities/)，它集成了[主动确定优先级并提出可行计划](https://thenewstack.io/automate-container-security-audits-with-docker-scout-and-python/)的智能。

本文讨论了 Docker Scout 的用例如何远远超出主要常见漏洞和暴露 (CVE) 扫描。容器安全要求检查安全洞察、自动化、DevOps 集成和策略执行的各个方面。阅读本指南后，您将了解如何使用 Docker Scout 控制安全和风险。

## 了解 Docker Scout 洞察

标准扫描器识别漏洞，但不建议如何修复它们。Docker Scout 通过评估风险并根据漏洞的损害和被利用的可能性对漏洞进行排名来改进。它使安全专业人员能够首先解决最相关的问题。

**Docker Scout 如何增强漏洞分析**

![](https://cdn.thenewstack.io/media/2025/04/b87261fd-image3.png)

**跟踪漏洞以及运行时数据**

Docker Scout 的突出之处在于，它不仅列出漏洞，还提供与每个缺陷相关的运行时行为。现在，您可以了解哪些漏洞正在被积极利用。通过将问题与正在运行的容器相关联，它可以优先考虑哪些容器需要首先关注；而不是追逐每个 CVE，而是专注于重要的内容。

**专注于最需要关注的风险**

并非所有漏洞都需要相同的工作量。有些需要立即关注，而有些则不太可能被利用。Docker Scout 评估归因于攻击媒介、漏洞的存在以及影响严重程度的风险。提出的问题已确定优先级，以便安全团队可以首先处理高风险。

**提供修复已识别问题的建议**

发现漏洞只是成功了一半；修复漏洞同样重要。Docker Scout 通过将风险与补丁和更新的基础镜像相关联，使修复变得更简单。它提供清晰的指导，以便员工可以实施修复，而无需猜测。自动化补丁建议有助于确保安全始终保持最新，并且只需最少的精力。

**真实案例：修复关键漏洞**

假设一家假设的公司在容器化设置中托管一个 Web 应用程序。标准 CVE 扫描表明存在大量漏洞，并建议哪些是最不紧急的。Docker Scout 检测到一个具有主动漏洞的高风险基础镜像 CVE，从而构成直接的安全威胁。它优先考虑此漏洞，并建议用已打补丁的基础镜像替换基础镜像，以实现安全、稳定的部署。

## 分步修复实施

识别易受攻击的基础镜像。运行 Docker Scout 扫描以检测漏洞：

```
docker scout recommendations my-app:latest
```

扫描输出突出显示了基础镜像中的一个关键 CVE。

查找已打补丁的基础镜像。使用 Docker Scout 检查是否有可用的更新：


该工具建议升级到 Ubuntu 20.04.5 作为安全替代方案。

更新 Dockerfile。修改 Dockerfile 以使用已打补丁的基础镜像：

```dockerfile
FROM ubuntu:20.04.5
RUN apt-get update && apt-get install -y \
 openssl
COPY . /app
CMD ["./start-app"]
```

重建并测试更新后的镜像：

```
docker build -t my-app:secure .
docker run --rm my-app:secure
```

部署安全镜像。将更新后的镜像推送到注册表并重新部署：

```
docker push my-app:secure
kubectl rollout restart deployment my-app
```

按照这些步骤可确保组织的应用在安全的基础镜像上运行，从而降低已识别的风险。

## 使用 Docker Scout 自动化安全修复

识别漏洞只是成功了一半；修复是关键。Docker Scout 通过提供可操作的建议并指导用户完成更新过程来自动化安全修复。

**Docker Scout 如何自动化修复**

![](https://cdn.thenewstack.io/media/2025/04/2e494c66-image5.png)

一些更新可能会破坏依赖关系，而另一些更新可能需要某种形式的停机。Docker Scout 通过推荐已修补且与您的设置兼容的基础镜像来缓解此问题。

**修复漏洞补丁的分步说明**

修复容器化应用程序的漏洞可能会令人沮丧。但是，Docker Scout 将漏洞管理分解为离散的步骤。

该软件列出了需要更改的软件包或依赖项，并提供了实施这些更改的说明。没有猜测，只有需要完成的实际任务。

## 与 CI/CD 管道集成的自动化安全修复

毫无疑问，手动修补漏洞是开发最慢的方式。Docker Scout 通过与 CI/CD 管道集成并自动执行安全更新补丁来解决此问题。安全任务完成后，系统会触发更新并构建经过测试和修补的镜像以进行部署。这种机制确保了应用程序的安全，并且不会中断开发。

**示例：以最短的停机时间修复漏洞**

一个开发团队在生产容器中检测到一个高危 OpenSSL 漏洞。他们没有手动搜索修复程序，而是使用 Docker Scout 的建议升级到安全的基础镜像。

更新过程通过其 CI/CD 管道自动执行，确保快速修复而不会中断应用程序。

**将 Docker Scout 与 DevOps 工作流程集成**

![](https://cdn.thenewstack.io/media/2025/04/837d9d7a-image4.png)

Docker Scout 通过将安全检查嵌入到软件开发生命周期中来实现持续的安全监控。

## 关键集成点

**CI/CD 管道：在部署之前自动执行安全性**

在 CI/CD 管道中部署之前，Docker Scout 会扫描容器镜像。它会阻止易受攻击的镜像部署到生产环境中。开发人员会立即收到对任何风险暴露的响应。在每个构建过程中都会自动进行安全检查。这证明了在不暂停开发的情况下保持安全性的有效性。

**安全警报：实时威胁检测**

Docker Scout 最好的功能之一是立即发出警报，通知新发现的威胁。它与 Teams、Slack 甚至电子邮件通知集成。在周期的早期，团队可以减轻安全缺陷。警报允许持续监控，从而减少了跟踪的需要。这降低了大量暴露未被注意到的可能性。

**Kubernetes 集成：持续监控运行中的容器**

![](https://cdn.thenewstack.io/media/2025/04/87e724ff-image2.png)

Kubernetes 下容器化环境中的工作负载由 Docker Scout 持续监控。它提供运行时漏洞和安全风险的即时检测。与静态扫描不同，它会观察活动容器的行为。环境中的变化会不断改变安全策略，从而可以主动保护非托管工作负载。

## 在 CI/CD 管道中自动执行安全性

![](https://cdn.thenewstack.io/media/2025/04/32d3a9a4-image1.png)

将 Docker Scout 集成到 CI/CD 管道中可确保在部署之前自动进行安全检查。它可以防止部署易受攻击的镜像，从而在每个阶段都强制执行安全性。以下是将 Docker Scout 集成到 GitHub Actions CI/CD 工作流程中的示例。

**步骤 1：定义 GitHub Actions 工作流程**

创建一个 `.github/workflows/docker-security.yml` 文件：

```yaml
name: Security Scan and Deployment
on:
  push:
    branches:
      - main
  pull_request:

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
        
      - name: Set up Docker
        uses: docker/setup-buildx-action@v2
        
      - name: Build Docker Image
        run: |
          docker build -t my-app:${{ github.sha }} .
          
      - name: Run Docker Scout Scan
        run: |
          docker scout quickview my-app:${{ github.sha }}
          
      - name: Get Fix Recommendations
        run: |
          docker scout recommendations my-app:${{ github.sha }}
          
      - name: Push to Registry if Secure
        if: success()
        run: |
          docker tag my-app:${{ github.sha }} my-registry/my-app:latest
          docker push my-registry/my-app:latest
          
      - name: Deploy to Kubernetes
        run: |
          kubectl rollout restart deployment my-app
```

**步骤 2：自动执行安全强制**

如果 Docker Scout 检测到高风险漏洞，则管道会失败。如果扫描通过，则会将镜像推送到注册表并进行部署。

**步骤 3：自动应用安全修复**

Docker Scout 会建议修复，而不是手动检查漏洞。然后，CI/CD 管道会使用安全更新重建容器。

这种方法确保了在不减慢开发速度的情况下强制执行安全性。

**使用 Docker Scout 强制执行安全策略**

安全策略确保仅部署安全、合规的容器。Docker Scout 使组织能够定义和执行旨在满足其风险承受能力的安全策略。

**定义和执行安全策略**

*   设置容器部署的风险阈值。
*   阻止具有严重漏洞的构建。
- 自动化合规性检查，以满足法规要求。

**示例：在生产流水线中实施安全门**

以下是使用 Docker Scout 和 GitHub Actions 在生产流水线中实施安全门的示例：

```yaml
name: Security Gate Pipeline
on:
  push:
    branches:
      - main
jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3
      - name: Run Docker Scout Scan
        run: |
          docker scout quickview my-app:latest > scout_report.json
      - name: Enforce Security Policy
        run: |
          HIGH_RISK_COUNT=$(jq '[.vulnerabilities[] | select(.severity=="HIGH" or .severity=="CRITICAL")] | length' scout_report.json)
          if [ "$HIGH_RISK_COUNT" -gt 0 ]; then
            echo "Security policy violation: High-risk vulnerabilities found!"
            exit 1
          fi
          echo "Security scan passed. Proceeding with deployment."
```

**说明：**

- 扫描镜像：流水线触发 Docker Scout 扫描应用程序镜像。
- 提取高风险 CVE：该脚本过滤标记为“HIGH”或“CRITICAL”的漏洞。
- 阻止不安全的部署：如果存在高风险问题，流水线将停止部署。

## 最终结论

Docker Scout 对容器安全采取积极主动的姿态。它提供深入的安全情报，自动执行安全修复，并与 Devops 工作流程集成，从而加强组织的安全态势。此外，实施安全策略可确保合规性，并最大限度地减少风险部署的可能性。

此外，当 Docker Scout 与组织的 DevSecOps 工作流程集成时，有助于提高修复停机期间的安全性。自动化的策略执行使安全团队能够将重点从被动转向主动。因此，集成 Docker Scout 并使您的容器化环境更加安全。