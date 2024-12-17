
<!--
title: Vercel、Netlify 和 Fastly 等开发者平台如何使用 AI
cover: https://cdn.thenewstack.io/media/2024/12/1261a87d-alexander-mils-fxjtvgrqevg-unsplashb.jpg
-->

我们与几家开发工具公司讨论了他们在内部如何使用人工智能，包括在产品开发和工程方面。

> 译自 [How Dev Platforms Like Vercel, Netlify and Fastly Use AI](https://thenewstack.io/how-dev-platforms-like-vercel-netlify-and-fastly-use-ai/)，作者 Jeff James。

AI 继续深入到各种规模、类型和行业的公司，其中企业技术行业是拥抱 AI 最积极的行业之一。我已经与开发者们讨论过他们如何[采用 AI 工具](https://thenewstack.io/favorite-ai-tools-of-developers-and-tips-for-using-them/)以及[创造性地使用它们](https://thenewstack.io/5-creative-ways-developers-are-using-ai/)在他们自己的工作流程中。我们还讨论了[AI 代理的出现](https://thenewstack.io/make-the-most-of-ai-agents-tips-and-tricks-for-developers/)以及[AI 如何影响 DevOps](https://thenewstack.io/using-ai-for-devops-what-developers-and-ops-need-to-know/)，但一个尚未得到充分讨论的角度是公司如何在内部使用 AI 工具和平台。

出于好奇，我联系了一些开发平台公司，那些同意公开记录的公司在使用 AI 的方法上相当一致，报告称他们各自公司几乎所有部门都以某种形式采用了 AI。

## 在工程和产品开发中使用 AI

所有与我交谈过的开发平台高管都提到，他们正在以某种能力在产品开发和工程中使用（或探索使用）AI。Netlify 首席技术官 Dana Lawson 表示，Netlify 的研发团队正在开发周期内在内部使用 AI，并利用 AI 为某些产品功能提供支持。

“我们正在将 OpenAI 用于我们的‘故障分析功能’，并将 Kapa.ai 用于‘询问 Netlify’文档功能，”她说。“我们还在一些功能开发中使用 Anthropic、Langbase 和 OpenAI……[并且我们]正在使用 Codemod 进行内部代码更改——例如 React 更新和其他系统升级——我们还在软件开发中使用 Github Copilot。”

## 公司采用 AI 的积极程度如何？

“Netlify 从财务到工程的所有部门都采用某种形式的 AI，”Lawson 说。“我们目前正在将 Gemini 与我们的 Google 商务套件工具一起使用。市场营销部门使用各种工具，从 ChatGPT 和 Claude 到 Perplexity、MidJourney、Otter.ai 等等。”

> “Vercel 是一家‘AI 优先’的公司，因此我们所有的部门都在使用 AI 来更快地迭代和交付。”  
>
> – Vercel 人事副总裁 Jenny Molyneaux

“Vercel 是一家‘AI 优先’的公司，因此我们所有的部门，从人事到市场营销，再到工程和客户支持，都在使用 AI 来更快地迭代和交付，”Vercel 人事副总裁 Jenny Molyneaux 说。“当我们开发一个 AI 驱动的代理并将其无缝集成到我们现有的支持工作流程中时，我们的客户支持团队减少了 31% 的工单，[并且]我们的人事和 IT 团队为我们的员工配备了 Notion Q&A AI 和 Glean AI Assistant 等工具，以便在 Notion、Slack、Docs 等平台上提供生成式答案。”

Molyneaux 表示，Vercel 人事团队使用 Brighthire 来总结她团队与申请人面试的记录，她和她的团队正在“……试用各种 AI 工具，涵盖指导、申请筛选以及学习和发展。”

## 市场营销中的 AI：影子写手和 UI 生成器

虽然开发和工程可以说是目前 AI 实验和试用范围最广的领域，但开发平台公司也在转向 AI 来帮助增强他们的营销团队，在过去一年左右的时间里，市场上出现了各种各样的针对营销专业人士的 AI 工具和平台。Vercel 市场营销副总裁 Morgane Palomares 解释了 Vercel 市场营销团队如何利用 AI 工具来提高效率并帮助推动成果。

“我们的市场营销部门使用 AI 来快速分解深奥的技术概念，检查前端使用的工具以帮助进行潜在客户开发，并改进人工撰写的文案以更好地遵循我们公司的风格指南，”Palomares 说。

在扩展使用 AI 创建公司风格指南方面，Palomares 解释说，他们使用他们的企业 ChatGPT 许可证创建了一个“Ghost”（即影子写手），它“……帮助 Vercel 的营销人员快速地从想法转化为文案，并确保我们在众多团队成员中保持一致的语气和声音。”
Palomares还描述了营销团队如何利用他们的[v0 产品](https://vercel.com/blog/announcing-v0-generative-ui)，这是一个由自然语言和人工智能驱动的生成式用户界面系统。“v0 就像开发人员的常驻结对编程伙伴，但它也是非开发人员的强大 UI 生成器，”Palomares 说。“我们的营销团队使用 v0 创建从仪表板到登录页面的所有内容，包括 Google Slide 套件。”

## 人工智能在运营和客户支持中的应用

许多组织已经开始在运营和客户支持工作中使用人工智能，开发平台公司也不例外。据 Netlify 的 Lawson 称，人工智能开始在这些部门得到广泛应用。

> “…我们的开发团队将 AI 用于从代码创建到为客户服务集成的所有方面。”
>
> — Dana Lawson, Netlify 首席技术官

“我们的客户成功团队使用 AI 来了解我们企业客户的健康状况，我们的开发团队将 AI 用于从代码创建到为客户服务集成的所有方面，而我们的支持团队使用 AI 驱动的聊天机器人来帮助客户自助服务，”Lawson 解释说。“我们的技术文档团队也整合了 AI，以更好地帮助寻求产品教育的用户。”

## 来自实践的更多技巧

虽然采用 AI 工具和平台对于许多公司来说仍处于“让我们尝试一下看看”的阶段，但我采访的高管们也鼓励处于 AI 工具采用早期阶段的公司仔细思考他们如何拥抱 AI。

“[Randy Reddig](https://www.linkedin.com/in/ydnar/)（[Fastly](https://www.fastly.com/) 技术研究和孵化副总裁）说：“最终，我们要对我们编写的代码或我们指示 AI 代表我们编写的代码负责。“你应该始终问：我们想要实现什么？这会取代还是增强我们的人力资本？这将用于做出决策，还是用于告知更好、更优（或更快）的决策？”

Netlify 的 Lawson 也赞同这种谨慎的做法，他鼓励 AI 工具和平台的采用者留出必要的时间来学习这些工具并练习使用它们。“如果你在目前的工作中没有使用它们，那么你在下一份工作中很可能需要这些技能，”Lawson 说。“不要过分担心使用这些工具会夺走你的工作。相反，应该将它们视为能够让你更好地完成工作的工具。从在 IDE 中使用提示性 AI 开始；一旦你适应了，就可以开始扩展并将这些平台整合到你正在构建的功能和工具中。”

Vercel 的 Palomares 也鼓励测试和试验 AI。“投资新工具需要投入时间、金钱和一点勇气。但是，当你迈出这一步时，你就能了解 AI 工具对你的工作流程的作用，”Palomares 说。“然后查看数据，再做下一步打算。”

> “人类仍然需要驱动系统来完成软件开发的最后一英里——优化代码、与特定业务环境保持一致以及处理边缘情况。”
>
> — Dana Lawson, Netlify

对于那些正在寻找 AI 使用的简单切入点的组织，Lawson 强调，处理重复的、平凡的任务可以是一个很好的起点。

“就 AI 的优势而言，它在处理重复性任务、构建数据和内容或搭建工作流程方面非常强大。在高质量、细致的输出方面，AI 在内容创作方面还有很长的路要走，”Lawson 说。“人类仍然需要驱动系统来完成软件开发的最后一英里——优化代码、与特定业务环境保持一致以及处理边缘情况。AI 是一个强大的助手，但不能取代开发人员的专业知识。”

## AI 和开发者平台提供商的未来是什么？

除了使用外部 AI 工具和平台之外，公司也开始将 AI 整合到新产品中，并继续推动员工对 AI 的认识和实验。

运行大型语言模型可能非常耗电且昂贵，因此 Reddig 指出 Fastly 的新产品 Fastly AI Accelerator，该产品专注于帮助开发人员应对广泛使用 LLM 的上述挑战。

“[Fastly AI Accelerator](https://community.fastly.com/t/announcing-the-ai-accelerator-beta/2723) 可以卸载来自源站的请求，降低我们客户的总体成本，并通过从 Fastly 的全球边缘缓存提供以前的响应来更快地交付内容，”Reddig 说。“关键区别在于使用了语义缓存——允许 AI Accelerator 提供来自相似（而非相同）查询的响应。结果是更快、响应更及时的基于 LLM 的体验，使我们的客户能够在更短的时间内以更低的总体成本为更多客户提供服务。”

> “人人都能烹饪——这意味着我们正在利用人工智能让优秀的开发者变得更出色，并邀请更多的人参与到构建过程中。”
>
> — Morgane Palomares, Vercel 营销副总裁

据 Palomares 称，Vercel 的 v0 产品激发了 Vercel 的公司理念转变。“人人都能烹饪——这意味着我们正在利用人工智能让优秀的开发者变得更出色，并邀请更多的人参与到构建过程中，” Palomares 说道。“我们鼓励所有开发者拥抱人工智能，并用它来扩展他们的技能，进入新的领域。开始‘烹饪’吧。”

人工智能的出现和日益普及正在持续影响着各类企业以及整个社会。“无论你是消费者还是软件开发者，人工智能都将普遍存在于商业的各个方面，因此我们将继续拥抱这些概念，” Lawson 说道。“随着人工智能技术的进步，人们将更加重视这些服务的价值和消费，数据也将变得更加短暂。在 Web 开发领域，人工智能将改变团队协作和实现体验的方式，从而实现更快的迭代、更灵活的服务组合以及个性化且具有影响力的数字体验。该行业面临的更广泛挑战是确保这些工具能够增强创造力和效率，而不是增加复杂性和摩擦。”
