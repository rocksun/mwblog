AI正让代码库充斥着机器生成的输出，但如果没有战略框架，我们不仅仅是在创新；我们正在自动化地制造遗留烂摊子，一位企业软件领导者认为。

通过[氛围编程](https://thenewstack.io/why-there-might-be-something-to-vibe-coding-after-all/)，开发者只需向[AI编程助手](https://thenewstack.io/what-are-ai-code-assistants-and-how-should-you-use-them/)输入几个提示，就能在几秒钟内创建一个功能齐全的应用程序。但如果一个工程组织重复这一过程数千次，所有这些AI生成的代码可能意味着今天的生产力提升会变成明天的[技术债务](https://thenewstack.io/technical-debt-vs-architecture-debt-dont-confuse-them/)。

SAP咨询和托管服务公司[Syntax](https://www.syntax.com/)的全球业务创新副总裁 Matthias Steiner 告诉《The New Stack》，缺乏治理的生产力正在为问题打开大门。

Steiner 说：“没有人是为了写代码而获得报酬，而是为了创造结果。编码只是工作的一部分。”

## AI应用于SDLC的每个阶段

在一次采访中，Steiner 强调了[规范驱动开发](https://thenewstack.io/is-spec-driven-development-key-for-infrastructure-automation/)的概念，这是一种将生成式AI不仅应用于代码生成，而且应用于软件开发生命周期的每个阶段——从市场分析和构思到需求工程、实施、测试和DevOps。

Steiner 表示，这里所说的“规范”是功能性规范，它作为AI代理一致生成设计、代码、测试和文档的单一事实来源。

Futurum Group 分析师 Brad Shimmin 告诉《The New Stack》：“我将规范驱动开发视为代理时代软件开发的未来成熟方向。在这种情况下，我们正在借鉴旧有的想法——还记得文学化编程吗？——并利用它们更好地定义我们的‘意图’，以指导代理工作流。”

## 超越氛围编程

这是超越氛围编程的下一个重要步骤，其前期结构最小化。

Steiner 说：“自由式代码可能也非常危险，因为它会炸毁代码库。如果你想构建生命周期为10到20年的企业级软件，那么你可能需要一些更模块化、更受治理的东西。”

他并没有完全否定氛围编程。他认为它在产品生命周期的早期、原型设计和探索阶段很有用。但在涉及为长期使用而构建的企业软件时，他划清了界限。

氛围编程不足以满足企业软件的复杂性和治理需求。

Steiner 在一篇[博客文章](https://www.syntax.com/blog/how-genai-is-transforming-software-engineering-but-not-replacing-it/)中写道：“一种更持久的模型正在随着*规范驱动开发*而兴起，其中结构化的规范成为系统的单一事实来源。”

他补充说：“根据该规范，AI可以一致地生成设计、创建代码、编写测试、制作文档并编排工作流。”

Steiner 进一步指出，SpecKit、OpenSpec和Claude Task Master等开放框架正在促成这一转变，使[AI代理](https://www.syntax.com/blog/agentic-ais-transformative-impact-across-industries/)能够以更高的可靠性解释和执行规范。

Steiner 写道：“这种模型减少了摩擦，改善了一致性，并加强了工程工作与业务成果之间的联系。”

## 治理需求

Steiner 认为，治理问题是AI驱动的生产力提升的后果。行业领导者经常引用数据显示，AI将编写60%到90%的生产代码，并且比人类快55%。

尽管取得了这些进步，Steiner 表示他将其视为[杰文斯悖论](https://en.wikipedia.org/wiki/Jevons_paradox)：更高的生产力意味着更多的软件被构建，这意味着更多的软件需要维护。在这种情况下，Steiner 解释说，随着AI使软件开发更快、更便宜，正在构建的软件总量将急剧增加——这意味着对工程工作的总体需求（以及维护所有这些软件的治理负担）随之增长。

他说：“随着生产力的提高，应用程序的数量将大大增加。而谁来管理这一切呢？”

他的答案是架构。他坚持认为，优秀的软件工程始终关乎组件化、复用性和模块化。AI改变的是构建的速度，而不是工艺的基本原则。

## 风险投资模式

Steiner 说，在Syntax，他的30人工程师团队目前正在并行进行10个产品构建，将风险投资风格的投资组合模式应用于软件开发。

假设一半的产品无法实现市场契合并将被放弃。规范驱动开发缩短了从构思到市场的周期，使得这种并行实验在经济上可行。

Steiner 说：“我们假设我们构建的一半产品不会成功，所以我们直接将其淘汰。可能两到三个会表现良好。也许其中会有一个独角兽。”

一款已上市的产品是[ShiftBook](https://info.syntax.com/hubfs/5843035/Syntax-ShiftBook-Datasheet-EN_V02.pdf)，这是一款与SAP Manufacturing Cloud集成的制造班次交接应用程序。它是Syntax首个端到端的规范驱动构建，Steiner 表示它的成功正在推动团队将该方法应用于所有新项目。

Steiner 说，在工具方面，他的团队使用Anthropic的Claude进行编码，使用Task Master进行规范驱动的工作流管理。TypeScript是团队的主要语言，因为它为当前一代工程师在类型化语言和非类型化语言之间提供了一个折衷方案。

## 软件工程依然重要

Steiner 向《The New Stack》强调，他并不认为随着AI接管代码生成，软件工程作为一门学科正在变得不那么重要。

他说：“不要过早地宣称软件工程已死。我认为恰恰相反。”

Steiner 表示，虽然AI可以处理代码生成的微观决策，但宏观决策——边界定义、依赖管理、模式治理以及技术选择与业务成果的对齐——仍然需要人类的判断。