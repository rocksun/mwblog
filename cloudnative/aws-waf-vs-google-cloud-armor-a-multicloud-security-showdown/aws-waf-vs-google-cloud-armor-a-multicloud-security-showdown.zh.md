2025年，多云已成为常态，而非新兴趋势。团队现在在AWS、Google Cloud Platform (GCP) 和 Azure 上运行工作负载。这在管理统一应用安全方面带来了复杂的挑战。

安全团队需要跨环境工作的[Web应用防火墙 (WAFs)](https://thenewstack.io/how-attackers-bypass-commonly-used-web-application-firewalls/)。AWS WAF 和 [Google Cloud Armor](https://thenewstack.io/google-cloud-stops-monster-ddos-attack/) 是首选。两者都能防御 [OWASP 威胁](https://thenewstack.io/owasp-top-10-a-guide-to-the-worst-software-vulnerabilities/)、机器人和 [DDoS 攻击](https://thenewstack.io/how-to-manage-xdp-ebpf-effectively-for-better-ddos-protection/)。

但实际应用表明，关键的架构差异显现。集成、规则自定义和自动化在不同平台之间存在显著差异。本指南将比较它们在混合云环境中的性能。

您将了解每个工具如何随着应用程序的增长而扩展。这是您的起点，涵盖成本控制、延迟、合规性和策略同步。

## **Web应用防火墙为何重要**

*   **API和应用层威胁超越基础设施攻击**：现在的威胁目标是逻辑缺陷、输入和会话行为。攻击者越来越关注API和前端逻辑。传统防火墙无法检测这些七层攻击。WAF对于检查HTTP流量，防止注入、跨站脚本攻击以及其他OWASP十大风险至关重要。
*   **生成式AI提升了僵尸网络的规模和复杂性**：如今的机器人很容易绕过CAPTCHA并表现得像真实用户。AI驱动的机器人完美模仿点击、延迟和浏览器头部信息。它们抓取数据、使表单过载并尝试凭证填充。现代WAF能够识别这些模式，有效阻止恶意IP并限制机器人流量。
*   **合规性要求日志、规则和响应策略**：法规现在要求对Web层流量具有可见性。NIS2、PCI DSS 4.0和HIPAA等规则要求强大的应用安全。记录访问和发现问题至关重要。WAF日志有助于轻松通过审计。
*   **多云应用需要一致的安全策略**：应用程序现在运行在AWS、GCP和边缘平台。例如，API可能部署在Google Kubernetes Engine (GKE)上，Web门户在Amazon的Application Load Balancer (ALB)上，而后台作业在Lambda上。如果没有一致的WAF策略，就会出现保护漏洞。AWS WAF和Cloud Armor都允许跨工作负载进行集中规则管理。

## **架构：它们的位置？**

### **Google Cloud Armor**

*   Google Cloud Armor 与 Google Cloud HTTP(S) 负载均衡器无缝协作。
*   它使用基于策略的系统，规则直接在网络边缘强制执行。
*   您还可以为外部云交付网络 (CDN)，例如 Cloud CDN 和 CloudFront，应用边缘安全策略。

**关键部署模型：**

###

### **AWS WAF**

*   AWS WAF 可轻松连接 CloudFront、API Gateway、ALB 和 AppSync。
*   它通过 AWS Firewall Manager 支持集中式规则管理。
*   如果您不使用 CloudFront，WAF 必须按区域部署。

**关键部署模型：**

##

## **规则引擎和威胁防护**

此表详细介绍了Google Cloud Armor和AWS WAF的关键特性。它展示了两者如何处理内置规则、自定义设置、按位置阻断、机器人防护和DDoS防御等。它还比较了它们更新威胁特征码和管理速率限制的速度。这有助于您并排了解每个服务的优势。

| 功能 | **Google Cloud Armor (GCA)** | **AWS WAF** |
| :--- | :--- | :--- |
| **预定义OWASP规则** | 是（Google管理规则集） | 是（AWSManagedRules规则组） |
| **自定义规则** | 基于通用表达式语言 (CEL) 的匹配表达式 | 具有多个条件的JSON逻辑 |
| **地理阻断** | 内置国家匹配 | 内置，带有IP集引用 |
| **机器人管理** | 带有ML的自适应保护 | AWS Bot Control（单独许可） |
| **DDoS防护** | 通过Cloud Armor + Google的边缘DDoS基础设施内置 | 通过AWS Shield Standard / Advanced |
| **速率限制** | 是 – 每个客户端IP或头部 | 是 – 基于令牌或基于速率 |
| **签名更新** | 接近实时 | 自动，但刷新率较慢 |

**关键洞察**：Google Cloud Armor 使用 CEL 来创建简单灵活的规则。AWS WAF 则采用嵌套条件逻辑。GCA 的智能、基于学习的保护可自动发现威胁。这使得Google在快速捕获异常活动方面具有优势。

## **自动化和DevSecOps集成**

### **Cloud Armor**

*   Terraform 允许您轻松设置 Google Cloud Armor 策略。
*   GCP Policy Intelligence 有助于改进您的安全规则。
*   Cloud Logging 和 Pub/Sub 协同工作，用于安全信息和事件管理 (SIEM) 设置。

###

### **AWS WAF**

*   AWS 完全支持 CloudFormation 和 Terraform 工具。
*   Firewall Manager 有助于管理整个组织的策略。
*   它还保护 API Gateway 和 AppSync 服务。

[![](https://cdn.thenewstack.io/media/2025/11/d281357b-image4-1024x709.png)](https://cdn.thenewstack.io/media/2025/11/d281357b-image4-1024x709.png)

## **日志记录、可观测性和成本**

此表显示了Google Cloud Armor和AWS WAF如何处理日志记录、监控和成本。两者都提供强大的SIEM支持，但在定价模型和免费套餐可用性方面有所不同。

| 类别 | **Google Cloud Armor** | **AWS WAF** |
| :--- | :--- | :--- |
| **日志集成** | Cloud Logging + BigQuery + Pub/Sub | CloudWatch Logs, Firehose, Kinesis |
| **SIEM支持** | 轻松导出到Chronicle, Splunk, ELK | Firehose + OpenSearch, Splunk, Datadog |
| **成本模型** | 按规则评估 + 按请求定价 | 按规则组 + 按请求定价 |
| **免费套餐？** | 有限，但包含Shield/DDoS保护 | ALB提供基本免费套餐，Shield额外收费 |

## **真实世界用例：多云GKE和ALB**

### **Google Cloud Armor 用于 GKE Ingress**

*   有效保护GKE工作负载。
*   阻断僵尸网络流量。
*   应用地理IP限制。
*   使用机器学习进行威胁检测。

### **AWS WAF 用于 ALB 和 API Gateway**

*   保护AWS应用负载均衡器和API网关。
*   抵御SQL注入和跨站脚本等攻击。
*   使用托管规则组进行保护。

### **实用建议**

*   在两个WAF之间使用共享的检测逻辑。
*   将两个WAF的日志转发到一个中央SIEM。
*   中央SIEM选项包括Splunk或Chronicle。
*   在云环境中提供更快、更一致的响应。

## **WAF功能摘要矩阵**

| 功能 | **Cloud Armor** | **AWS WAF** |
| :--- | :--- | :--- |
| OWASP预定义规则 | 是 | 是 |
| 基于ML的自适应保护 | 是（内置） | 否 |
| 机器人保护 | 原生 | 付费（Bot Control） |
| 日志记录和SIEM集成 | BigQuery, Splunk, Chronicle | CloudWatch, Kinesis |
| 速率限制 | 是 | 是 |
| 地理/IP阻断 | 是 | 是 |
| Terraform支持 | 是 | 是 |
| 最适合 | GKE, Cloud Run, App Engine | ALB, API Gateway, CloudFront |

## **结论**

Google Cloud Armor和AWS WAF都提供强大的企业级安全性。Cloud Armor在自适应保护和出色的GKE支持方面表现出色。AWS WAF在多云覆盖和通过Firewall Manager进行集中管理方面表现突出。

对于2025年的多云设置，不要只选择一个。采用结合您的工作负载和合规性需求的WAF方法。