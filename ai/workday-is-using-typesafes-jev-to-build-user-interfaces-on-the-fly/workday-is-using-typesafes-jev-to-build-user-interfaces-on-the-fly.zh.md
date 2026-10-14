[Workday](https://thenewstack.io/workday-ai-inference-guardrails/) 于周二将其 AI 助手 Sana 打造成了人力资源、财务和 IT 软件的全新主屏幕。如果你不是人力资源专业人士，这可能不会让你感到多么兴奋，但该团队构建此功能的方式可能是 [TypeSafe 决策模型 Jev](https://thenewstack.io/typesafe-jev-system-one/) 最有趣的用例之一。Workday 正在动态构建用户界面——这一切都由 Jev 进行管理。

在发布会前的记者吹风会演示中，例如，关于工资单的问题会弹出一张金额隐藏在点击背后的卡片，而请假请求则会生成一个日期选择器，由 Sana 填写表单的其余部分。

Sana 是 Workday 去年以 [11 亿美元收购](https://newsroom.workday.com/2025-09-16-Workday-Signs-Definitive-Agreement-to-Acquire-Sana)的，现已正式上线，管理员可以将其向用户推出，但不会将其设为默认。

## 选择组件而不是编写组件

Workday 首席 AI 官兼 Sana 创始人 Joel Hellermark 在记者吹风会上表示，传统的[生成式 UI](https://thenewstack.io/generative-ui-for-devs-more-than-ai-assisted-design/) 方法（即模型生成完整的界面）“相当慢”。

“如果你改用分类模型，只给它提供所有可供选择的设计构件，你实际上可以瞬间完成，”他说。

Hellermark 表示，Workday 为 Jev 提供了其设计系统中的每个原子组件，并且没有硬编码任何选择逻辑，不过该团队还必须正确处理数据预加载。例如，在演示中，工资单卡片在他打完字之前就已经出现了。

[TypeSafe 声称](https://typesafe.ai/blog/introducing-system-one-models-and-jev) Jev 的响应时间在 70 到 500 毫秒之间，这使其非常适合这种实时用例。

Hellermark 表示，在许多情况下，通过真实界面元素发挥作用的 AI 比纯粹的来回聊天表现要好得多。

## 专为选择而生的模型

根据 TypeSafe 的说法，开发人员向 Jev 发送应用程序数据和一组类型化的问题，它会返回一个从最多 255 个选项列表中的选择、一个分数或一个是或否的答案，每个答案都带有相应的概率。它不生成文本。

TypeSafe 于 9 月 15 日推出了 Jev，并获得了由 DCVC 领投的 4000 万美元种子轮融资。周五，该公司表示获得了一笔由 Andreessen Horowitz 领投的 [8.7 亿美元 A 轮融资](https://typesafe.ai/blog/series-ai)，估值达到 75 亿美元。TypeSafe 称，财富 500 强中有三分之一已经在使用 Jev，但并未透露他们的名字。[Andreessen Horowitz 自己的公告](https://a16z.com/announcement/investing-in-typesafe-ai)将这一数字定为 25%，而 TypeSafe 唯一公开的案例研究涉及 AI 招聘市场 [Jack & Jill](https://typesafe.ai/blog/jack-jill-jev-case-study)。

当然，这一领域的竞争并不匮乏。[OpenAI](https://thenewstack.io/openai-decision-api-luna/)、[Amazon](https://thenewstack.io/aws-strands-decider-model/)、Cloudflare 和 Perplexity 也已经推出了它们的[决策模型](https://thenewstack.io/openai-decision-models-deployment/)，[Microsoft](https://thenewstack.io/microsoft-decision-model-foundry/) 则紧随其后，于上周发布。

## 开发人员已经在测试的模式

不过，使用 Jev 和类似模型来构建用户界面并不是完全新鲜的事情。CopilotKit 是一个用于向应用程序添加 AI 智能体的开源框架，它发布了一个[方案](https://docs.copilotkit.ai/cookbook/jev-generative-ui)，其中 Jev 选择显示哪个预构建面板，并以 OpenAI 模型作为后备。

Vercel Labs 正在其用于从开发人员定义的组件渲染 AI 生成的 UI 的框架 [json-render](https://thenewstack.io/vercels-json-render-a-step-toward-generative-ui/) 中测试 Jev 模式。

应用开发商 Very Good Ventures 的解决方案架构负责人 Andrew King [上个月写道](https://verygood.ventures/blog/genui-division-of-labor-problem/)，将每一个封闭式问题（具有固定答案集的问题）交由 Jev 处理，使他的生成式仪表板的中位渲染时间从前沿模型组合时的 29 秒缩短至 3.8 秒。他的测试是在合成数据上运行的。

“意料之外的形态不可能出现在屏幕上，”King 写道。Jev 以低于 50% 的置信度回答的任何内容都会转交给语言模型，他将这种设置称为“带门的笼子”。

在 [OpenRouter 博客上的测试](https://openrouter.ai/blog/insights/jev-vs-claude-opus-5-classification/)中，使用 Banking77 意图分类集，Jev 的中位响应时间为 175 毫秒，准确率为 81%。Claude Opus 5 的得分为 84.4%，但耗时 2.3 秒，成本约为前者的 22 倍。

TypeSafe 自己的[文档](https://docs.typesafe.ai/model-jaggedness/jev-1.13)指出，Jev 在计数、算术和日期方面存在困难，倾向于列出的第一个选项，并且默认情况下不将注入的内容视为敌意内容。

Workday 尚未透露其设计系统的规模有多大，或者当没有组件组合符合条件时 Sana 会做什么。King 在 9 月份写道，他一直将客户端数据保存在 Jev 之外，因为该供应商“成立仅几周，尚未发布安全认证”。TypeSafe 现在可应要求提供 [SOC 2 类型 II 报告](https://typesafe.ai/enterprise)。

## Workday 移交的内容

Workday 最近将 TypeSafe 添加到了其[子处理商名单](https://www.workday.com/content/dam/web/en-us/documents/legal/workday-subprocessors.pdf)中，这些外部公司可以处理客户数据（只有当您订阅的 SaaS 服务向您发送关于您会迅速忘掉的子处理商更改的电子邮件时，您才会想起它们）。值得注意的是，此条目涵盖了 Workday 的所有产品线，不仅仅是 Sana，用于自然语言处理、意图分类和置信度评分。

根据 TypeSafe 的说法，Jev 仅在其[托管 API](https://typesafe.ai/enterprise) 上运行并在美国处理数据，该公司向企业客户提供零数据保留。

## 留在 Workday 内部

Hellermark 还展示了在 Anthropic 的 Claude 内部运行的 Sana。Workday 产品与技术总裁 Gerrit Kazmaier 在吹风会上表示，这是一次 AI 到 AI 的集成，在这个过程中用户失去了由 Jev 驱动的界面和部分上下文。

Workday [5 月与谷歌云的合作](https://newsroom.workday.com/2026-05-28-Workday-and-Google-Cloud-Expand-Strategic-Partnership-to-Bring-AI-Agents-for-HR-and-Finance-Into-Employees-Daily-Workflows)已经涵盖了 [A2UI](https://thenewstack.io/agent-ui-standards-multiply-mcp-apps-and-googles-a2ui/)（谷歌用于智能体描述宿主应用程序随后渲染的界面的规范）。[MCP Apps](https://thenewstack.io/anthropic-extends-mcp-with-an-app-framework/)（模型上下文协议扩展）将交互式 UI 引入了 Claude 和 ChatGPT。这两者都没有出现在 Workday 本周的公告中，因此目前看来，通过 Claude 接触 Sana 的员工只能获得对话，而没有日期选择器。