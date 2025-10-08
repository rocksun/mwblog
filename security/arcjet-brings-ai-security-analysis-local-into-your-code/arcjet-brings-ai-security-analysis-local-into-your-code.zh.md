安全平台提供商 [Arcjet](https://arcjet.com/) 今日宣布推出一款本地 [AI 模型](https://thenewstack.io/frontier-ai-models-now-becoming-available-for-takeout/)，该模型可直接在应用程序请求处理程序内部运行 [安全分析](https://thenewstack.io/startup-embeds-ai-security-analysis-in-dev-workflow/)。该模型无需通过 [云端安全](https://thenewstack.io/zero-trust-in-cloud-security-never-trust-always-verify/) 服务路由流量，而是在应用程序运行的地方直接分析威胁，从而使其能够访问外围工具无法看到的业务上下文。

这是对多年来一直困扰开发人员的一个问题的回应：安全工具在阻止实际威胁的同时也阻止了合法用户。如果规则过于严格，你就会赶走真正的客户。如果过于宽松，攻击就会趁虚而入。对于电商网站和 [软件即服务 (SaaS) 应用程序](https://thenewstack.io/service-as-software-how-ai-agents-are-transforming-saas/) 来说，这种权衡直接影响利润。

Arcjet 创始人兼首席执行官 David Mytton 告诉 The New Stack：“传统的外围解决方案只看到数据包，而不是用户或业务上下文。我们的本地 AI 模型将 [上下文感知安全分析](https://thenewstack.io/why-context-aware-ai-is-quickly-replacing-code-only-tools/) 引入请求路径，在那里你才能真正理解应用程序中发生的事情。”

## 为什么误报很重要

误报问题在安全最关键的地方变得更糟。在结账时阻止某人，你就失去了一笔销售。将一个合法的注册标记为可疑，你可能就扼杀了一次转化。Mytton 表示，传统安全工具在网络层面运行，将模式与流量进行匹配，而不了解该流量是真实客户还是机器人。

Arcjet 的模型在你的应用程序安全规则（机器人检测、速率限制、[Web 应用程序防火墙 (WAF)](https://thenewstack.io/how-attackers-bypass-commonly-used-web-application-firewalls/) 保护）触发后运行，并利用其平台上的信号训练的机器学习 (ML) 分析请求。因为它在本地运行并可访问你的应用程序状态，所以它可以查看会话历史、用户行为模式和业务逻辑等信息，这些信息可以判断请求是否真正可疑。

其结果是 Arcjet 称之为“精炼”的安全建议，它结合了基于规则的分析和学习到的信号。开发人员可以检查确定性规则结果和 AI 建议，然后在代码中决定如何处理每个请求。

Mytton 在一篇博客文章中写道：“Arcjet 的 AI 模型将确定性规则与学习到的信号相结合，分析每个请求并返回一个精炼的建议，你可以在代码中对其采取行动。”

## 开发者如何使用它

该 AI 模型作为单独的 npm 包与 Arcjet 的 SDK 一同发布。集成是可选且直接的。以下是它在 Next.js 表单处理程序中的样子：

此文件包含隐藏或双向 Unicode 文本，其解释或编译方式可能与下面显示的不同。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)








| | |
| --- | --- |
| | typescript |
| | |
| | const aj = arcjet({ |
| | key: process.env.ARCJET\_KEY!, |
| | rules: [ |
| | detectBot({ mode: "LIVE" }), |
| | shield({ mode: "LIVE" }), |
| | ], |
| | }); |
| | |
| | export async function POST(req: NextRequest) { |
| | // Run deterministic rules |
| | const decision = await aj.protect(request); |
| | |
| | // Use the AI model as an additional layer |
| | const aiDecision = await refine(decision); |
| | |
| | if (aiDecision.isDenied()) { |
| | return NextResponse.json( |
| | { error: "Unauthorized" }, |
| | { status: 403 } |
| | ); |
| | } |
| | |
| | // Your form logic here |
| | } |

该模型增加了 1 到 2 毫秒的延迟——速度足够快，可以在实时请求处理中工作。Mytton 表示，团队尝试了 [小型语言模型](https://thenewstack.io/should-you-try-small-language-models-for-ai-app-development/)，但发现它们需要大约半千兆字节的内存，这在无服务器环境中是不可行的。相反，他们构建了一个轻量级的 ML 模型，可以在 CPU 上运行，且资源需求极低。

Mytton 表示，由于所有内容都在本地运行，因此敏感数据永远不会离开你的生产环境。你可以在笔记本电脑上测试与生产环境相同的安全配置，这解决了长期以来安全工具与被保护应用程序分离的问题。

## 选择你的战场

Arcjet 将 AI 模型定位为更广泛安全策略中的一个层，而不是现有措施的替代品。开发人员可以选择在何处应用 AI 驱动的分析——也许只在注册和结账流程等误报成本最高的地方，而在其他地方使用更快的确定性规则。

该模型与 Arcjet 的现有功能协同工作：机器人检测、速率限制、电子邮件验证、敏感信息检测和 Shield WAF 保护。该公司认为，开发人员想要的是能够融入其工作流程的安全工具，而不是需要管理单独基础设施层的安全工具。

RedMonk 高级分析师 Kate Holterhoff 在一份声明中表示：“开发人员并非对安全漠不关心，他们只是还没有拥有合适的工具，能够理解他们的语言并适应他们的工作流程。那些无法与现代开发工作流程整合的安全工具根本不会被使用。”

## 更广阔的图景

这种方法反映了现代应用程序安全工作方式的更广泛转变。Mytton 表示，现在机器人数量已超过在线人类用户，而 AI 正在使攻击更具适应性，更难通过简单的模式匹配来检测。传统的周边防御难以跟上。

Mytton 表示，Arcjet 主要在两种情况下获得采用：用户注册（阻止合法用户会损害增长）和电子商务（误报会直接导致收入损失）。一个早期用户客户通过在应用程序层而非处理请求来阻止爬虫，将无服务器成本降低了 66%。

Arcjet 拥有约 1,000 名开发者，在 500 多个生产应用程序中使用其技术。该公司拥有一个 10 人团队，工程师分布在凤凰城、旧金山、费城和纽约。Mytton 最近从伦敦搬到纽约，并计划在曼哈顿熨斗区开设办事处。

本地 AI 模型将作为预览版向 Arcjet 客户推出。Mytton 表示，该平台目前支持在 [Node.js](https://thenewstack.io/node-js-22-release-improves-developer-experience/)、[Bun](https://thenewstack.io/node-removes-corepack-bun-runs-native-c-from-javascript/) 和 [Deno](https://thenewstack.io/denos-response-to-nodes-recent-support-for-typescript/) 上运行的 [JavaScript](https://thenewstack.io/introduction-to-javascript/) 应用程序，并支持 [Next.js](https://thenewstack.io/next-js-deployment-spec-simplifies-frontend-hosting/)、[Remix](https://thenewstack.io/remix-takes-on-next-js-in-battle-of-the-react-frameworks/)、[SvelteKit](https://thenewstack.io/rich-harris-talks-sveltekit-and-whats-next-for-svelte/) 等框架。

Mytton 的愿景是对应用程序安全发展方向的一个有趣押注。Arcjet 认为，与其将所有流量都路由到集中式安全基础设施，不如让安全更接近代码，因为在那里你可以了解应用程序正在做什么，并可以就阻止什么和允许什么做出明智的决定。