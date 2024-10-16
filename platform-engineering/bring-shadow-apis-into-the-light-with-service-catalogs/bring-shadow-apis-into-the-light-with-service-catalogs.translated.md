# 利用服务目录揭示影子 API

![Bring Shadow APIs Into the Light With Service Catalogs 的专题图像](https://cdn.thenewstack.io/media/2024/10/1c413708-shadowapis-servicecatalogs-1024x576.jpg)

随着组织继续向[基于微服务的架构](https://thenewstack.io/microservices/)迁移，实施实时数据策略并转向 API 优先的方法，管理和治理 API 通常变得越来越复杂。

## API 激增和影子 API 增加了复杂性和风险

拥有的 API 越多，需要保护、管理和治理的 API 就越多。 不久之后就会出现“[API 激增](https://thenewstack.io/heres-how-to-tame-your-api-sprawl-and-why-you-should/)”，即有成百上千个未正确记录的新 API。

虽然这一切看起来简单且可预测，但许多组织仍在为此苦苦挣扎。 这些挣扎通常表现为“[影子 API](https://thenewstack.io/shadow-zombie-and-misconfigured-apis-are-a-security-issue/)”——未被发现和未被管理的遗留 API，这些 API 通常仍在生产环境中运行。 这些 API 给任何企业都带来了严重的风险。

### API 安全漏洞日益增多

对快速增长的 API 环境缺乏可见性，为安全漏洞创造了温床。 影子 API 通常不受监控或维护不善，成为攻击者的主要目标，他们会利用不正确的身份验证逻辑或弱加密标准。Kong 的研究强调了这种风险，预计到 2030 年，年度攻击次数将[增长 548%](https://konghq.com/resources/reports/ai-and-api-adoption-challenges)，仅在美国就将达到 42,000 次 API 攻击。

### 数据泄露和敏感信息泄露

由于这些 API 通常不受跟踪或监控，因此它们可能会无意中泄露敏感数据，例如客户个人身份信息 (PII)、财务记录或专有业务信息。 例如，为现已失效的服务开发的遗留 API 可能仍然可以访问敏感数据库，从而无意中将数据泄露给任何知道如何调用它的人。 最令人担忧的是，这些数据泄露通常是静默发生的，组织中的任何人都不会注意到，直到为时已晚。

### 违反监管标准

无法完全考虑所有 API 意味着组织难以遵守行业法规。 处理敏感数据的 API 可能不在强制合规性检查范围内，例如 [GDPR](https://gdpr-info.eu/) 或 [HIPAA](https://www.hhs.gov/hipaa/index.html) 审计，仅仅是因为它们未被列为组织官方 API 清单的一部分。 这种缺乏监督可能会导致代价高昂的监管罚款，更不用说对客户信任的潜在损害。

## 利用服务目录改进 API 治理

就像图书馆目录可以帮助读者查找资料一样，[服务目录](https://thenewstack.io/microservices/what-is-a-microservice-catalog-and-why-do-you-need-one/) 充当组织服务和 API 的集中记录系统。 服务目录是所有 API 和服务的发现和可见性机制。 换句话说，它是 API 激增和影子 API 的克星。 让我们进一步细分。

服务目录最强大的功能之一是其发现引擎，它会在部署新服务和停用非活动服务时动态更新目录。 发现引擎允许服务目录在无需人工干预的情况下保持其准确性和可靠性，使其成为可靠的信息来源。

然而，需要注意的是，并非所有服务目录都是一样的。

某些目录的发现引擎没有与关键基础设施（如 API 网关和服务网格）深度集成，通常需要手动填充和维护。 这些手动流程极易出错，并导致目录几乎立即过时。

换句话说，如果您的服务目录无法自动填充，则会破坏采用此类解决方案的全部目的。 您不妨尝试在 Excel 表格中手动管理、衡量和治理每个 API 和服务。 对于拥有庞大服务范围的组织来说，这是站不住脚的。

构建为与各种基础设施应用程序深度集成的自动化服务目录可以全面了解组织的南北和东西 API 流量。 这允许目录显示有关服务的分析（例如请求计数、错误率和延迟），这些分析反映了其动态的实际使用情况，而不是静态的过时数据。

## 掌控您的 API 环境
企业不能再承担将关键客户数据、PII 和授权凭证“漂浮”在生产环境中，看不见的风险。希望不能成为你的 API 安全策略。

认识到对良好集成、自动化的服务目录的需求，我们构建了 [Konnect 服务目录](https://konghq.com/products/kong-konnect/features/api-service-catalog)，现在已在 [公开测试版](https://konghq.com/blog/product-releases/service-catalog) 中提供。 立即登录 [Kong Konnect](https://cloud.konghq.com/login?utm_medium=syndication&utm_source=newstack&utm_campaign=konnect-demo) 试用，注册 [30 天免费试用](https://konghq.com/products/kong-konnect/register?utm_medium=syndication&utm_source=newstack&utm_campaign=konnect-demo) 或查看 [此实时演示](https://www.youtube.com/watch?v=MctyzrVMCfQ) 以了解其 UI/UX。

[YOUTUBE.COM/THENEWSTACK
技术发展日新月异，请勿错过任何一集。 订阅我们的 YouTube
频道，观看我们所有的播客、采访、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)