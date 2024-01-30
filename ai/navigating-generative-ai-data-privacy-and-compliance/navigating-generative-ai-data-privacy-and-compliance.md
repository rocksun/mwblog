<!--
title: 生成式AI数据隐私与合规指南
cover: https://cdn.thenewstack.io/media/2024/01/6af0d8d8-navigating-ai-privacy-compliance-1024x576.jpg
-->

当今数据安全日益受关注，开发负责任的生成式AI既是法定义务，也是道德责任。

> 译自 [Navigating Generative AI Data Privacy and Compliance](https://thenewstack.io/navigating-generative-ai-data-privacy-and-compliance/)，作者 Sharon Kisluk 是Apono的首席产品经理，负责公司的短期和长期战略产品计划。她拥有10多年作为技术人员和产品建造者的经验。 在加入Apono之前，Sharon曾担任过许多产品......

在人工智能(AI)快速发展的环境中，将生成式AI集成到软件即服务(SaaS)产品组合中成为努力的热潮。

然而，这波创新带来了指数级的风险增长，因为这些生成式AI产品会摄入敏感数据，如客户信息或其他个人身份信息(PII)。在严格的数据隐私法时代，巨额罚款和更高的公众意识，[保护客户数据](https://thenewstack.io/llms-and-data-privacy-navigating-the-new-frontiers-of-ai/)从未如此关键。

## 保护免受AI相关责任

开发人员在保护公司免受生成式AI产品相关的法律和伦理挑战方面发挥着至关重要的作用。面对无意中暴露信息的风险(一个长期存在的问题)，或者现在生成式AI工具自己泄露它(正如当ChatGPT用户报告[看到其他人的对话历史记录](https://www.pcmag.com/news/chatgpt-users-report-seeing-other-peoples-conversation-histories)时发生的那样)，公司可以实施以下策略来最大限度地减少责任，并有助于确保对客户数据的负责任处理。

### 数据匿名化和聚合

使用匿名化和聚合的数据可作为防止意外暴露个人客户信息的初始障碍。将数据匿名可剥离个人身份信息，以便生成式AI系统可以学习和操作，而不会将特定详细信息与单个用户相关联。此外，聚合数据通过将信息汇总成更广泛的模式，进一步增强了隐私，减少了识别敏感详细信息的机会。

### 严格的访问控制

大多数公司已经实施了强大的访问控制，但在生成式AI的时代，其影响被放大。通过仔细的访问管理，开发人员可以将数据访问权限[严格限制](https://www.apono.io/just-in-time-access-to-databases?utm_source=tns&utm_medium=blog&utm_campaign=genai)于具有特定任务和职责的个人。通过创建一个严格控制的环境，开发人员可以积极减少数据泄露的可能性，以确保只有授权人员可以在生成式AI系统内与客户数据进行交互和操作。

### 定期审计和测试

维护生成式AI系统的弹性和合规性需要定期审计和测试的承诺。对访问控制、敏感数据存储库的访问日志以及数据卫生的定期审查只是几种先发制人地寻找和测试新兴风险的方式。

## 评估对DevOps团队的影响

理论上，这三种做法很容易值得实施。但实际上，采用这些保护措施显著增加了开发和运维([DevOps](https://thenewstack.io/devops/))团队的日常责任，常常导致他们在决定优先考虑哪些措施时做出妥协。

### 对合规性的关注加强

虽然数据保护法规是标准实践并且在不断发展，但[针对AI的新兴法规则是新的](https://www.pillsburylaw.com/en/news-and-insights/ai-regulations-us-eu-uk-china.html)。预计这些迫在眉睫的法规将扩大合规性的范围，并需要更高水平的先发制人的教育。在实践中，开发人员很快就需要分配额外的时间来遵守法规，或与法律团队合作以降低潜在的责任。

### 增强的安全性集成

稳健的安全措施，包括加密协议和访问控制，将继续成为开发过程的关键部分，以防止未经授权的访问和数据泄露。但是，对透明度和用户同意的新要求将推动开发人员采用更以用户为中心的设计原则，其中隐私考虑贯穿整个开发生命周期。

## 底线

随着我们将生成式AI集成到SaaS产品提供中的浪潮，开发人员有责任在创新和隐私保护之间维持微妙的平衡。[Apono的权限管理自动化平台](https://www.apono.io/?utm_source=tns&utm_medium=blog&utm_campaign=genai)等自助服务工具可以使DevOps更容易管理跨云服务、Kubernetes、数据存储库和其他应用程序的权限。

通过实施严格的保护措施，开发团队可以帮助确保生成式AI产品不仅满足数字时代的需求，而且还尊重和保护用户委托给它们的敏感信息。在这种数据敏感度更高的时代，负责任地开发生成式AI不仅仅是法律要求，更是道德义务。
