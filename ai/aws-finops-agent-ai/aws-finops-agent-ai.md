<!--
title: AWS账单飙升为何？全新AI智能体为您排忧解难
cover: https://cdn.thenewstack.io/media/2026/06/8bca0875-getty-images-am3wyiikxo4-unsplash.jpg
summary: AWS推出公开预览版FinOps Agent，通过AI技术分析账单异常，能用自然语言解答支出疑问，自动识别根源并关联相关负责人，有效减轻工程团队在财务审查上的负担，实现云成本管理的持续自动化。
-->

AWS推出公开预览版FinOps Agent，通过AI技术分析账单异常，能用自然语言解答支出疑问，自动识别根源并关联相关负责人，有效减轻工程团队在财务审查上的负担，实现云成本管理的持续自动化。

> 译自：[Why did my AWS bill spike? There's now an agent for that](https://thenewstack.io/aws-finops-agent-ai/)
> 
> 作者：Darryl K. Taft

[Amazon Web Services](https://thenewstack.io/a-cascade-of-failures-a-breakdown-of-the-massive-aws-outage/) 为其日益增长的 IT 运营 AI 工具组合新增了第三个专业的“前沿智能体”——该智能体专注于云账单。

[AWS FinOps Agent](https://docs.aws.amazon.com/finops-agent/latest/userguide/what-is.html) 于上周进入公开预览阶段，此前 AWS 已相继推出了 [AWS Security Agent](https://aws.amazon.com/security-agent/) 和 [DevOps Agent](https://aws.amazon.com/devops-agent/)。该智能体进入了一个历来依赖仪表板、电子表格和人工分析师经验的领域，通过它，用户可以使用简单的英语提问，且当发现异常时，智能体能够自动采取行动。

在本例中，该领域即为 [FinOps](https://thenewstack.io/how-to-build-a-finops-strategy-that-works/) ——即促使工程、财务和业务团队共同承担云支出责任的准则。AWS 将这个新智能体定位为对当前行业趋势的回应：FinOps 工作正从周期性的、基于仪表板的审查，转向工程团队已经在使用的工具（即 Jira 和 Slack）中运行的持续工作流。

## 该智能体的功能

其核心工作流从 [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/) 结束的地方开始。目前，异常警报只能告诉团队发生了变化，却无法说明原因。FinOps Agent 旨在迈出下一步——将成本激增与 AWS CloudTrail 关于“谁在何时更改了什么”的记录相关联，识别触发变更的原因，并汇总一份调查摘要，明确可能的根本原因及相关负责人。此后，它可以自动创建 Jira 工单或向 Slack 频道发送消息。

该智能体可以回答自然语言成本问题，例如“为什么我上个月的 AWS 成本增加了？”它是通过从 Cost Explorer、Cost Optimization Hub 和 Compute Optimizer 中获取数据，并将答案关联到特定服务和使用驱动因素来实现的。企业可以上传映射账户到所有者、团队和标签约定的上下文文件，智能体利用这些文件将诸如“X 团队的成本是多少”之类的问题，转化为正确的账户集合。

公开预览版还增加了定期成本报告（可按日、按周或按月导出为 HTML、PDF 或 PPT 格式），以及一项将 Cost Optimization Hub 和 Compute Optimizer 的建议打包进 Jira 工单的功能，以便工程师进行处理。

## 权限模型主要是只读的

对于一个能够全面查看账户账单、使用情况和运营数据的工具，AWS 设置了严格的访问权限限制。根据 AWS 的文档，FinOps Agent 使用的 [IAM](https://thenewstack.io/a-deep-dive-into-the-security-of-iam-in-aws/) 角色在账单、优化、监控、日志记录和基础设施服务方面主要是只读的——足以分析成本、调查异常并发现节省机会，但不足以接触资源本身。

其获得的唯一写入权限是用于管理智能体自身的 EventBridge 调度规则，以驱动其周期性自动化任务。它不能创建、修改或删除 EC2 实例、[RDS 数据库](https://thenewstack.io/diving-into-aws-databases-amazon-rds-and-dynamodb-explained/)、Lambda 函数或网络组件。该智能体基于 Amazon Bedrock 构建，AWS 表示这其中包含了其标准的自动化滥用检测防护栏。

## 早期客户

AWS 的公告提到了四个客户账户，每个账户都描述了该智能体旨在解决的略有不同的痛点。[Workday](https://www.workday.com/en-us/homepage.html) 的 AI 平台基础设施团队在多个 AWS 账户上运行该公司的 AI 平台，其软件开发工程经理 [Serjesh Sharma](https://www.linkedin.com/in/serjeshsharma/) 表示，该工具的吸引力在于将两个耗时的工作——“在成本异常演变成预算问题前进行追查”以及“汇总领导层审查的月度报告”——合并到一个自然语言界面中。

新西兰最大的家居零售商 [Mitre 10](https://www.mitre10.co.nz/) 则从精简平台团队的竞争优先级角度进行了阐述。该公司平台工程经理 Eduard Kleynhans 表示，定期的成本审查和异常检查历来“与可靠性和改进工作直接冲突”，而该智能体的吸引力在于让这些检查“在后台持续运行”，只有在“真正需要关注时”才显示结果。

商业支付公司 [Convera](https://convera.com/) 在受监管的环境中运营，指出了一个更具体的故障模式：小的、无意的成本变化在共享队列中被忽略。该公司基础设施工程与运营主管 [Ramesh Singaraj](https://www.linkedin.com/in/rameshsingaraj/) 表示，该智能体的价值在于它能将 Jira 工单发送“给拥有该资源的工程团队，从而让正确的工程师看到它，而不是淹没在一个无人关注的共享队列中。”

而经营着法国、德国和比利时数字房地产市场的 [AVIV Group](https://www.aviv-group.com/) 在中央 FinOps 团队下管理着数百个 AWS 账户，他们将该智能体视为卸载一线问题的手段，例如“按需定价与 Savings Plan 定价之间的差异”或“某个特定异常为何触发”等问题。这些问题以前都需要反馈给一个小型的中央团队，资源所有者才能采取行动。FinOps 总监 [Jordi Espasa](https://www.linkedin.com/in/jordiespasa/) 表示，直接为工程师解答这些问题，使中央团队能够专注于“分摊逻辑、优化策略和领导层报告”。

## 尚待完善之处

目前预览版仅在美国东部（弗吉尼亚北部）区域可用，但当从管理账户部署时，它可以管理其他 AWS 区域和账户的成本与使用数据（不包括 GovCloud 以及中国北京/宁夏区域）。在预览期间可免费使用，但受每月使用限额限制，不过智能体在此过程中涉及的其他 AWS 服务仍需按标准收费。

AWS 表示该智能体将随时间推移进行扩展，包括专门针对 AI 工作负载的成本分析。考虑到 AI 基础设施支出正成为 FinOps 团队被要求解释的主要项目之一，这一点非常值得注意。