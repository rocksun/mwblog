# DevSecOps 实施：最佳实践

翻译自 [DevSecOps Implementation: Best Practices](https://thenewstack.io/devsecops-implementation-best-practices/) 。

DevSecOps 提供了一种全面加固应用程序和系统的方法。以下是如何拥抱其最佳实践并使你的组织取得成功的方法。

![](https://cdn.thenewstack.io/media/2021/07/3e03fb13-teamworksilhouette-1024x576.jpg)
*来自 Unsplash 的 [Natalie Pedigo](https://unsplash.com/@nataliepedigo)*

组织面临着不断的安全威胁和数据泄露。因此，将[安全](https://thenewstack.io/security/)视为事后事项的传统方法已不足以保护敏感数据和系统。相反，实施 [DevSecOps](https://thenewstack.io/what-is-devsecops/) 已成为软件安全的一个重要转变。

通过在整个软件开发生命周期中无缝集成安全实践，DevSecOps 提供了一种全面加固应用程序和系统的方法。本文深入探讨了拥抱 DevSecOps 作为最佳实践的深远重要性，并突出了它对软件安全的变革性影响。

## DevSecOps 如何在每个阶段增强安全性

### 规划阶段

在规划阶段，[DevSecOps](https://thenewstack.io/ebooks/devsecops/best-of-devsecops-trends-in-cloud-native-security-practices/) 通过在过程早期集成安全需求和风险评估来增强安全性。这涉及安全专家与开发和运维团队的协作，他们一起识别潜在威胁和漏洞。

使用[威胁建模技术](https://thenewstack.io/4-threat-models-for-kubernetes-deployment-security/)来评估风险，并根据确定的威胁和潜在影响来优先考虑安全措施。

###  编码阶段

DevSecOps 提倡安全编码实践，以确保开发出具有弹性和安全性的软件。开发团队遵循编码准则和安全编码标准，将安全最佳实践纳入他们的代码中。

[静态代码分析工具](https://thenewstack.io/checking-linuxs-code-with-static-analysis-tools/)用于自动扫描代码中的安全漏洞，如输入验证错误、不安全的身份验证或不足的数据清理。在进入下一个阶段之前，需要解决和修复发现的漏洞。

### 测试阶段

在测试阶段，DevSecOps 将安全测试作为基本组成部分进行集成。使用自动化安全测试工具，如[静态应用程序安全测试（SAST）和动态应用程序安全测试（DAST）](https://thenewstack.io/why-you-still-need-dynamic-application-security-testing/)，来识别和修复漏洞。SAST 分析源代码以查找潜在的安全弱点，而 DAST 在运行时环境中模拟现实世界的攻击来测试应用程序。

此外，进行渗透测试以验证安全控制的有效性，并识别可能被忽视的漏洞。

### 部署阶段

在这个阶段，DevSecOps 强调安全的配置管理实践和基础设施即代码（IaC）原则。安全的配置管理确保部署的基础设施以适当的安全控制进行正确配置。IaC 工具（如 Terraform 和 Ansible）通过代码实现了安全基础设施配置的定义和执行。

实施适当的访问控制、[安全的秘密管理](https://thenewstack.io/the-challenges-of-secrets-management-from-code-to-cloud/)和加密技术，以保护敏感数据并维护部署过程的完整性。

### 运维阶段

在运维阶段，DevSecOps 促进持续监控，实时检测和响应安全威胁。收集并使用日志分析工具分析来自各种系统和应用程序的日志。利用威胁情报源来了解最新的威胁和漏洞。

使用[安全信息和事件管理（SIEM）](https://thenewstack.io/what-separates-an-siem-platform-from-a-logging-tool/)工具来整合和关联安全事件，实现主动的事件检测和响应。明确定义的事件响应流程使安全团队能够及时处理安全事件，最小化其影响，并从中吸取教训，增强未来的安全措施。