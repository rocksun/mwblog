
<!--
title: DevOps与安全：如何构建弹性流水线
cover: https://cdn.thenewstack.io/media/2024/12/df60ae2c-olumuyiwa-sobowale-kqidjlbcgha-unsplash-scaled.jpg
-->

像DarkTrace和K8sgpt这样的AI工具增强了DevOps工作流程中的威胁检测和修复能力。

> 译自 [DevOps and Security: How To Build Resilient Pipelines](https://thenewstack.io/devops-and-security-how-to-build-resilient-pipelines/)，作者 Alexander Simonov。

[DevOps](https://thenewstack.io/devops/)团队已经掌握了流水线、容器和[Terraform](https://thenewstack.io/terraform-and-the-tooling-multiverse-in-the-future-of-iac/)，从而更快更高效地交付应用程序，但安全仍然是一个关键的盲点。随着软件开发基础设施日益复杂，每个流水线阶段都可能存在不安全代码和云配置错误的风险。安全风险转化为敏感数据泄露和交付停机只是时间问题。

被定罪的黑客转型为顾问的 Kevin Mitnick 证明了人为因素一直是安全中最薄弱的环节。快速的人工智能进步使得安全的DevOps比以往更容易实现，但人工智能仍然是一只需要熟练手引导的野狗。与培训和教育DevOps团队同等重要的是掌握持续安全——在保持领先于新出现的威胁的同时，积极保护数字系统。

## 持续安全如何融入DevOps？

DevOps周期是重复性的——计划、代码审查、构建、测试、发布、部署、监控，然后重复。安全措施应在每个步骤中应用。在实际项目中，如果DevOps工程师在计划阶段跳过清单审查，则此疏忽将导致严重的数据泄露，其中一个变量可能会被错误地公开。使用Terraform合规性在每个Terraform周期开始时进行自动化审查至关重要，这可以节省时间并防止代价高昂的错误。

持续安全必须考虑人为因素，即使在经验丰富的团队中，这也是一个高风险因素。例如，初级工程师可能会意外地将访问令牌上传到共享存储库。[DevOps在自动化流水线时可能会面临存储库中的密钥](https://thenewstack.io/use-these-devops-pipelines-to-cut-automation-tool-costs/)——这是一个容易忽视但可能造成灾难性影响的问题。诸如HashiCorp Vault之类的工具和严格的密钥轮换策略可以帮助降低风险。

## 安全的代码编写和存储

周期始于编写和处理代码，安全应从这个初始阶段集成。团队应该[采用左移原则来及时识别和修复安全](https://thenewstack.io/how-to-adopt-shift-left-security-from-the-start/)问题，从而形成一种文化，即从项目开始就人人有责。

DevOps[工程师应该在软件开发](https://thenewstack.io/platform-engineering-the-pioneers-who-built-it/)过程的早期运行各种扫描，以识别可能随着工作进展而出现的框架和潜在风险。例如，开发人员可能会使用具有已知漏洞的过时依赖项。将Dependabot和CodeQL集成到DevOps工作流程中可以帮助自动化依赖项检查，在问题进入生产环境之前标记并解决问题。

## 保护CI/CD阶段

一条黄金法则是不应在存储库中以纯文本形式存储密码。DevOps工程师应使用令牌并始终检查应用程序组件之间的通信协议。

最好将密码、登录名和安全字符串存储在安全且集中的位置，并定期轮换凭据以防止未经授权的访问。一个典型的例子是在生产环境中不安全地使用测试环境API密钥。在这种情况下，最好的安全措施是将敏感信息存储在基于云的密钥库中，例如[HashiCorp Vault](https://www.hashicorp.com/products/vault)，并实施严格的最小权限访问策略。DevOps将在构建过程中或例如根据应用程序请求注入Kubernetes中的密码。此外，他们将配置设置以限制生产密码。[最小权限原则](https://www.techtarget.com/searchsecurity/definition/principle-of-least-privilege-POLP) (PoPL, PoMP, 或PoLA)在这里至关重要，以及[OWASP十大安全风险](https://owasp.org/www-project-top-ten/)，它提供了有关保护DevOps流水线的宝贵信息。

## 保护部署后阶段
最长的阶段，也是维护时间最长的阶段，始于部署之后，通常需要与开发一样多甚至更多的努力。维护安全范围从用户访问和证书到DDoS攻击和SQL注入。DevOps专注于威胁检测、用户行为分析和漏洞评估（已经借助AI）。

项目部署后，DevOps可能会注意到异常的系统行为。DarkTrace可以帮助他们识别试图利用所有生产环境中SQL注入漏洞的企图。这是部署后安全策略中一项基石安全措施的示例。

[DevOps越来越依赖AI](https://devops.com/can-ai-replace-devops-engineers/)来响应事件并扫描、检测和修复基础设施缺陷。扫描需要以下组件：

**Kubernetes**:

* **K8sgpt**: 查找并修复问题，执行安全审计，并针对特定任务训练其模型。
* **KoPilot**: 快速审计Kubernetes资源中已知的漏洞，非常适合理解复杂或继承的Kubernetes配置。
* **Kube-copilot**: 通过在工作流程中提供解释和建议来帮助经验不足的团队成员。

**SaaS**:

* **Spin.ai**: 增强网络弹性，简化安全操作，并保护关键任务应用程序的SaaS数据。
* **IBM**: 一个庞大的平台解决方案，用于解决任何领域的安全性问题。
* **ZAP**: 提供主动和被动扫描以及附加插件。

**VM**:

* **Splunk**: 借助人工辅助自动化，提供全面的上下文和解释、快速的事件检测和更高的生产力。
* **Google的Security Command Center**: 通过虚拟机监控程序级检测和持久性磁盘分析提供威胁检测。
* **Palo Alto**: 扫描并预测网络行为。

## 抵御威胁

DevOps中的安全对于开发稳定性和项目成功同样重要。它是贯穿DevOps流程整个迷宫的一条主线。AI和自动化技术是DevOps工程师的盟友，帮助他们更快、更准确地管理漏洞。此外，工程师应培养安全第一的思维模式，确保在整个开发生命周期中主动检测威胁、最大限度地降低风险和提高流水线弹性。
