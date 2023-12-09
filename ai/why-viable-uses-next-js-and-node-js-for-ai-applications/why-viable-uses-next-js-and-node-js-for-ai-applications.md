<!--
title:为什么Viable使用Next.js和Node.js进行AI应用开发
cover: https://cdn.thenewstack.io/media/2023/12/4e01e7fa-pexels-sanket-mishra-16380906-1024x683.jpg
-->

Viable公司是一家客户分析初创企业，在前端开发中结合运用了AI和JavaScript技术。CEO解释采用Next.js和Node.js的原因是这两者能够实现前后端联调，提高开发效率，有利于构建数据密集型的Web应用。

> 译自 [Why Viable Uses Next.js and Node.js for AI Applications](https://thenewstack.io/why-viable-uses-next-js-and-node-js-for-ai-applications/)，作者 Loraine Lawson。

虽然大多数生成式人工智能聊天机器人都是通过聊天界面接入的，但这并不是人工智能唯一的用户界面。[Viable](https://www.askviable.com/) 就是一个不依赖聊天机器人界面使用 AI 的公司的例子。

这家创业公司为公司汇总和分析客户反馈。这些数据可以来自在线评论、调查反馈、社交媒体以及像 ZenDesk 或 Intercom 这样的客户服务平台 —— 基本上是客户与公司交流服务的任何地方。Viable 然后使用 AI 将这些客户反馈与 AI 分析相结合，创建报告而不是聊天，首席执行官兼软件工程师 [Daniel Erickson](https://www.linkedin.com/in/danielerickson/) 说。

“数据进来后，它会处理这些数据，深入挖掘主题并识别数据集中的主题，然后分析这些主题，每个主题输出约 10 段我们分析的段落，它读起来像一份报告，” [软件工程师](https://github.com/techwraith) Erickson 告诉 The New Stack。“当你实际查看 Viable 应用程序时，你所做的就是阅读报告，它们读起来就像人类分析师编写的一样。”

他补充说，这是首批利用 [OpenAI](https://thenewstack.io/why-microsoft-has-to-save-openai/) 的 [GPT API](https://thenewstack.io/security-with-chatgpt-what-happens-when-ai-meets-your-api/) 的公司之一。

## 没有聊天的 AI

Erickson 指出，Honeycomb 是另一个没有利用聊天的 AI 部署的例子。Honeycomb 使用自然语言界面，允许用户用纯文本语言创建查询。 然后，AI 会输出一个更加技术化的类 SQL 查询，他说。他还预见到了聊天机器人以外的自然语言模型的其他用途。

“我认为人们将大大减少切换过滤器和下拉菜单的次数，而是更多地键入他们想要找到的内容，然后他们会得到这些内容，”他说。“我看到的另一件事是，人们经常在与这些 AI 互动时遇到困难，因为需要一定的学习曲线才能理解它们如何‘思考’。”

这就是为什么真正重要的是向客户提供有关他们要求 AI 做什么的反馈，他补充说。为此，Viable 创建了一个提示教练来帮助客户查询。

“我们基本上构建了一种教练东西，它会查看提示并说 ‘这里是如何[改进提示](https://thenewstack.io/improving-chatgpts-ability-to-understand-ambiguous-prompts/)以使 AI 更容易理解并获得更好的输出’，”他说。

## 为什么选择 Next.js 和 Node.js

Viable 使用托管在 [Vercel](https://thenewstack.io/vercel-adds-new-features-designed-to-support-monorepos/) 上的 [Next.js 框架](https://thenewstack.io/vercels-next-js-14-introduces-partial-pre-rendering/)来创建其用户界面和 API。Erickson 说，Next.js 可以轻松地在 UI 中的新页面中启动新的 API 端点。与 Express 等其他[开源选择](https://thenewstack.io/options-for-monetizing-your-open-source-project/)相比，这要容易得多，他补充说。

“它基本上就是这样做的，”他说。“所以许多其他框架，你必须进入并说 ‘我希望我的 API 路由看起来像这样，只接受这些内容，并真正深入做那些细枝末节的工作。Next.js，我所要做的就是创建一个新文件，把页面放到 /API 目录下，这样我就有了一个新的 API 路由。”

对 Erickson 来说，Next.js 的另一个好处是生态系统，他指出，这个生态系统比任何其他框架都大，除了可能是 React 本身。而且无论如何 Next.js 在底层使用了 React，他补充说。

“基本上，如果它与 React 兼容[...]然后还有一堆开源的额外[库](https://thenewstack.io/stacklok-builds-on-sigstore-to-identify-safe-open-source-libraries/)，这些库围绕身份验证、不同的数据源、不同的组件(如 UI 组件)和库构建，”他说。“那里有很多东西，生态系统真的很容易插接，并为我提供了很多我不必自己构建的工具。”

Viable 面临的一个挑战是，其[数据引入管道](https://thenewstack.io/building-reliable-data-pipelines-qa-with-logdna-and-mcafee/)需要能够支持从数据流到暴雨的一切，因为客户反馈可能是“峰值”的，他解释说。

“你不知道那是否会是每天 5 条消息，或者每天 50 万条消息。这完全取决于你的公司在做什么和人们在谈论什么，”他说。“Vercel 的[无服务器体系结构和边缘函数](https://thenewstack.io/vercel-brings-serverless-functions-to-the-edge/)真的帮助我们扩展以满足这些需求。”

他选择了 [JavaScript](https://roadmap.sh/javascript)，因为作为一名 JavaScript 工程师，他从 2009 年开始就一直使用 [Node.js 运行时环境](https://thenewstack.io/what-typescript-brings-to-node-js/)，所以这是他编写代码的默认工具箱的一部分。它也非常擅长处理异步数据处理，他补充说。使其出色的是，它以异步方式运行，这意味着它基本上有一个在[代码运行时发生的运行时循环](https://thenewstack.io/appmap-releases-runtime-code-review-as-a-github-action/)。

“它可以暂停进程的执行，”他说。“它拉入更多的数据，这意味着它的多任务处理能力实际上比许多其他编程语言要好得多。使用 Node 时，你比使用其他东西时更少地考虑多任务处理。”

## 开发 AI 时的注意事项

Erickson 说，开发人员在投入开发 AI 之前应该意识到的一件事是，大多数[ AI 都需要支持实时流](https://thenewstack.io/the-machine-learning-building-blocks-developers-require-to-do-mlops/)。

“如果你与 ChatGPT 或任何东西聊天，当你这样做时，你实际上可以看到文本正在流入，”他说。“它不喜欢有一个小的加载指示器，然后一次性输入所有文本。你需要看到文本的输入，就像计算机正在向你输入一样，这是因为延迟。”

这些模型需要“永远”来生成文本，所以尽快将第一组文本提供给用户是非常重要的，他补充说。他还补充说，Next.js 和 Vercel 的 AI 工具比手动编码来[支持流](https://thenewstack.io/confluent-proactive-support-aims-to-speed-resolution-of-kafka-streaming-data-issues/)更容易。
