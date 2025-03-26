# Brex 的 Web 开发改造在设计上对代码 LLM 友好

![Brex 的 Web 开发改造在设计上对代码 LLM 友好的特色图像](https://cdn.thenewstack.io/media/2025/03/3469338d-hooks-1024x578.png)

当 [Brex](https://www.brex.com/) 的工程团队决定改造其前端时，计划是重建以更好地服务于他们的客户。在此过程中，该项目产生了一个不寻常的副作用：它使网站对[大型语言模型](https://thenewstack.io/top-5-large-language-models-and-how-to-use-them-effectively/)（LLM）更加友好。

“我们最初决定重建 Brex 的 [前端堆栈](https://roadmap.sh/frontend)，以便在未来几年更好地服务于我们的客户——从初创公司到财富 500 强企业，”Brex 高级软件工程师负责 AI 产品的 [Marcelo Terreiro Prado](https://www.linkedin.com/in/marcelo-t-prado/?originalSubdomain=br) 通过电子邮件告诉 The New Stack。“我们了解到，当代码易于人们理解时，它也能很好地与 LLM 配合使用。”

## 前端问题

Brex HQ 是一家金融科技公司，提供一套专为企业（尤其是初创公司和高增长公司）设计的金融服务。它提供企业信用卡、现金管理账户、费用管理软件和其他金融服务。

[Terreiro Prado](https://www.linkedin.com/in/marcelo-t-prado/?originalSubdomain=br) 说，Brex 最初的 [基于 React 的前端](https://thenewstack.io/new-york-public-library-on-choosing-react-to-rebuild-website/) 为他们提供了多年的良好服务，但这家金融科技公司的客户群正在发生变化。

他说，在过去的两年里，这家金融科技公司已经更多地向上游市场发展，并开始收购更大的企业客户。

他说：“我们意识到我们已经触及了堆栈的天花板，再也无法承受它带来的限制。”

他们在原始架构中遇到了两个主要问题。首先，由于过多的网络请求和昂贵的 React 重新渲染，它存在性能问题。其次，代码库的复杂性急剧上升。

“[Terreiro Prado](https://www.linkedin.com/in/marcelo-t-prado/?originalSubdomain=br) 通过 X [分享](https://x.com/marceloterreiro/status/1883148631123071228) 说：“我觉得我需要一个博士学位才能理解我们的 FE [前端] 代码库。”他补充说，他并不孤单：新员工也表达了他的沮丧。

## 四个 Web 开发指导“第一性原理”

通过重建，Web 开发团队希望回到 [前端开发](https://thenewstack.io/introduction-to-frontend-development) 的 [第一性原理](https://thenewstack.io/web-development-trends-in-2024-a-shift-back-to-simplicity/)。第一性原理思维包括将复杂的问题分解为最基本的要素，然后从那里向上推理。

工程经理 [Derek Stavis](https://www.linkedin.com/in/derekstavis/)、高级软件工程师 [Victor Magalhães](https://www.linkedin.com/in/vhfmag/?originalSubdomain=br) 和 [Terreiro Prado](https://www.linkedin.com/in/marcelo-t-prado/?originalSubdomain=br) 为重新设计的前端提出了四个指导原则：

*   **所有可以预加载的数据都必须预加载。**“[Terreiro Prado](https://www.linkedin.com/in/marcelo-t-prado/?originalSubdomain=br) 解释说：“给定路由所需的所有数据都应在路由的根组件处请求；预加载需要是最容易的路径。”
*   **应该清楚哪些组件触发查询。**“以前，所有级别的组件都可以触发查询，这使得瀑布式请求成为一个真正的问题，”他说。在新架构中，只有少数组件类型可以启动查询：路由的入口点和在交互时查询的组件（例如，依赖于后端数据的选择输入）。
*   **应该清楚组件依赖哪些数据（数据共址）。**他说：“您应该能够仅通过阅读组件的源代码来准确解释组件的工作方式。”“在 [GraphQL](https://thenewstack.io/how-apollo-makes-llms-more-reliable-with-graphql/) 和渲染的 React 组件之间不应存在任何间接层。我们必须感觉自己正在编写“哑”代码，而不是充满我们可能无法完全理解的巧妙抽象的代码。”
*   **选择约定优于配置。**他说：“[平台团队提供工具，使采用](https://thenewstack.io/platform-teams-adopt-these-7-developer-productivity-drivers/) 黄金路径尽可能简单，例如代码生成器、文档和配方。”“使用新架构编写的功能在 UX 和原始性能方面都表现得更好，我们相信工程师会遵循约定。”

哑代码可能看起来是一个奇怪的补充。但它是他们重新设计的关键组成部分。

[Terreiro Prado](https://www.linkedin.com/in/marcelo-t-prado/?originalSubdomain=br) 在 X 上写道：“我们认为[哑代码是最好的](https://x.com/marceloterreiro/status/1883148626891047309)代码类型。”“哑代码是您公司中的每个人都可以立即阅读和理解的代码，而无需跳入数十个障碍和抽象概念。”

## React Hooks 的问题
该团队对 React 非常满意，他表示，所有“前端界面”都在使用它。他们希望继续使用它，但在改版过程中确实从 React 17 升级到了 React 18。

Terreiro Prado 说，由于并发渲染模型，React 18 的升级进一步增强了新架构的性能优势。

不过，他们遇到的一个大问题是 [React Hooks](https://react.dev/reference/react/hooks)。

React Hooks 是 React 中的一项功能，允许开发人员在函数组件中使用状态和其他 React 功能。它们提供了一种管理组件逻辑（如状态、副作用和上下文）的方式，而无需编写类组件。

但 Terreiro 指出，Hooks 有一个副作用，那就是容易让糟糕的 GraphQL schema 不被注意。

“Hooks 最大的优点也是它最大的问题：它隐藏了复杂性，”Terreiro 说。“在使用 GraphQL 时，应该可以通过读取 graph 轻松访问你的数据。如果你需要多个步骤或花哨的逻辑来计算一个布尔值，那闻起来就像一个糟糕的 schema。

“把它隐藏到一个 hook 中并不能解决你组织的问题——这只是把垃圾扫到地毯下。”

“这就是为什么强大且有主见的原则如此重要。它为整个组织的协作奠定了基础和基调。”

— Marcelo Terreiro Prado，Brex 高级软件工程师

在他的 [X 帖子中，他提供了 Hooks 隐藏糟糕 GraphQL schema 的例子](https://x.com/marceloterreiro/status/1883148624785441144)。

“例如，像 ‘`useCanSubmitReimbursement`’ 这样的 hook 在我们的前端被广泛使用，”他写道。“乍一看很无辜，但充满了大量的瀑布式请求和疯狂的逻辑来计算一个布尔值。”

他指出，有些人可能会反驳说，这是糟糕的 GraphQL schema 的结果，而不是 React Hooks。

“当然，我完全同意。然而，Hooks 使这一点**真的**很容易被忽视，”他在 X 上写道。“而且由于它们的病毒性质，你很快就会有很多地方使用这种糟糕的实现。”

他学到的一个深刻教训是，产品工程师会使用他们可以使用的任何东西，无论实现是好是坏。

“因此，你必须避免发布垃圾 hooks，否则你的性能会随着时间的推移而缓慢下降，”他发推文说。

他还补充说，之前的架构也不鼓励前端和 [后端](https://thenewstack.io/introduction-to-backend-development/) 协作。这导致了更多 Hooks 的使用。

“当一个前端工程师需要的数据不能干净地映射到 schema 时，他们通常会默认使用 hooks 来计算它。该 hook 经常会触发多个查询来获取必要的数据，然后使用前端业务逻辑计算该值，这总是一种代码异味，”他告诉 The New Stack。

他补充说，在新的架构中，这是不可能的，因为它会违反原则 1、2 和 3。

在重新设计下，当前端开发人员需要的数据没有映射到 Brex 的 graph 时，他们必须与后端协作来修复 GraphQL schema。

“这就是为什么强大且有主见的原则如此重要，”Terreiro Prado 说。“它为整个组织的协作奠定了基础和基调。GraphQL 尤其一直是我们的工程领导层关注的重点。”

## 将 Apollo 换成 Relay：它如何改变了 LLM 的站点

为了减少他们遇到的 React Hooks 问题，该团队用 Relay 替换了 [Apollo](https://thenewstack.io/apollo-graphql-now-connects-to-rest-apis-with-little-fuss/)。

Terreiro Prado 解释说，Apollo 在设计上是一个通用的 GraphQL 客户端。

“作为其中的一部分，它使得从组件内部进行查询变得非常容易（这种想法与我们的原则背道而驰），”他说。“另一方面，Relay 的设计考虑了 Meta 的需求。它从未被构建为通用客户端。”

[Relay 是 Meta 的 JavaScript 框架](https://thenewstack.io/facebooks-relay-javascript-framework-building-react-applications/)，用于构建数据驱动的 [React 应用程序](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/)。它专门设计用于与 GraphQL 一起使用，GraphQL 是一种用于 API 的查询语言和运行时。

“Relay 假定你的代码以一种非常特殊的方式编写，因此，它能够推导出一些智能优化，”Terreiro 补充道。“像 fragment masking、预加载查询和数据 colocation 这样的概念都融入了 Relay 的核心。”

切换到 Relay 及其对 colocation 的支持也带来了意想不到的结果，即更容易让 LLM 理解该站点。
![X 帖子显示：“之前，我觉得我需要一个博士学位才能理解我们的 FE 代码库。这是新员工对我们的代码库的普遍看法。由于意外的复杂性，事情变得非常混乱。我们的新架构主要通过一个原则来解决这个问题：局部推理。”](https://cdn.thenewstack.io/media/2025/03/2aa716f9-marcelo_phd_tweet.png)

Brex 高级软件工程师 Marcelo Terreiro Prado 在 X 上的[帖子](https://x.com/marceloterreiro/status/1883148631123071228)。

“事实证明，当你编写更少的查询，并使你的组件与它们的数据需求紧密耦合时，你的整个架构就更容易掌握，”他说。“检查一个组件就足以解释它的工作原理。你不再需要跳转到数十个嵌套的钩子中，或者检查它的父组件来找到它依赖的数据。”

这是一个他称之为局部推理的想法。局部推理是一种以允许[开发者理解](https://thenewstack.io/codesee-helps-developers-understand-the-codebase/)和修改单个组件或代码段的方式来构建和组织代码的实践，而无需全面了解整个应用程序。

“一个模型需要跳转的圈子越少，或者需要加载到其上下文中以理解代码库的文件越少，它就越有效，”他说。

这也是启用 LLM 的关键。

“以一种非常有原则和有主见的方式构建我们的架构，也使得能够对 LLM 进行更结构化的指导，”他说。“我们有很多关于如何解决前端需求的配方和文档。我们将这些提供给 LLM，以便它确切地知道如何解决特定问题，而不是发明一个解决方案。”

数据共址——这是团队采用的第三个“原则——也在这方面发挥了作用，”他继续说道。

LLM 受限于它们的上下文窗口，提示越集中和具体，输出与开发者期望匹配的机会就越高，他说。

“共址是一个与此产生强烈共鸣的原则，”他说。“将大部分代码放在一个文件中意味着 LLM 不需要搜索庞大的代码库来查找特定字段的计算方式。”

## LLM 和 Web 开发的未来

虽然 Brex 的网站[春季发布](https://www.brex.com/spring-2025)——其中包括 React 18 的推出和 Relay 迁移——对 LLM 来说效果很好，但形势正在迅速发展，以前效果好的东西不一定总是适用于较新的模型，他警告说。

“然而，到目前为止，我们的经验表明，有一个关键的见解：让你的代码和 API 易于人类理解，”他说。“这是一个简单但令人惊讶的强大观察。”

Brex 最近发布了一个 [模型上下文协议](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) (MCP) 服务器，该服务器允许 LLM 生成多个组件，例如选项输入、表格、路由和多步骤流程，这些组件严格遵循团队的黄金路径，他说。Terreiro 对一个研究领域感到兴奋，那就是如何使机器能够意识到并能够使用 Brex 庞大的设计系统库。

他分享了关于前端开发的最后一个重要教训：领导层和前端之间的协调对于[解决 Web 开发问题](https://thenewstack.io/top-problems-developers-need-you-to-fix-now/)至关重要。

“如果我们的领导团队只关注尽快交付多项内容，而不关注质量/架构，那么就很难提倡这些改变，”他说。

[
[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。
]