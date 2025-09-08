自从 OpenAI 的最新模型 GPT-5 [发布以来已经过去了几个星期，评价褒贬不一](https://thenewstack.io/gpt-5-a-choose-your-own-adventure-for-frontend-developers/)——一位著名的前端开发者甚至在几天内 180 度大转弯，完全改变了他们的论调。但现在开发者们已经有时间充分测试这个新模型了，我们可以更好地确定 GPT-5 是否像 [OpenAI 声称的那样](https://openai.com/index/introducing-gpt-5-for-developers/)“擅长前端编码”。

我联系了 OpenAI，提出了一系列关于前端开发的问题。OpenAI 的研究员 [Ishaan Singal](https://www.linkedin.com/in/ishaan-singal/) 通过电子邮件回复了我。Singal 曾任职于 Stripe 和 Microsoft 的软件工程师，他告诉我，早期对 GPT-5 的反馈“是积极的，[但]现在还处于早期阶段。”

我的第一个问题是，在 [GPT-5 提示指南](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide) 中，有三个推荐的框架：Next.js (TypeScript)、React 和 HTML。我问道，是否与 Next.js 和 React 项目团队进行了合作，以优化 GPT-5 对这些框架的支持？

“我们选择这些框架是基于它们的受欢迎程度和普遍性，但我们没有与 Next.js 或 React 团队直接合作开发 GPT-5，”Singal 回答说。

我们知道，[负责 Next.js 框架的公司](https://thenewstack.io/vercels-frontend-and-the-rise-of-the-hybrid-developer/) Vercel 是 GPT-5 的粉丝。在发布当天，它称 GPT-5 为“最好的前端 AI 模型”。所以这里发生了一个很好的互惠互利的事情——GPT-5 因为 Next.js 的受欢迎程度而能够成为 Next.js 方面的专家，这大概会进一步提高它的受欢迎程度。这有助于 OpenAI 和 Vercel。

[![来自 OpenAI 的 GPT-5 提示指南中“为 GPT-5 组织代码编辑规则”的示例。](https://cdn.thenewstack.io/media/2025/09/f028e3a8-screenshot-2025-09-05-at-10.55.25.png)](https://cdn.thenewstack.io/media/2025/09/f028e3a8-screenshot-2025-09-05-at-10.55.25.png)

来自 OpenAI 的 [GPT-5 提示指南](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide) 中“为 GPT-5 组织代码编辑规则”的示例。

但是，如果你[不想使用 Next.js](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/)，或者实际上任何 Web 框架呢？我问道，如果只使用核心 Web 平台技术（引用 HTML、CSS、JavaScript 以及 Mozilla MDN 上列出的任何 [Web API](https://developer.mozilla.org/en-US/docs/Web/API)）来创建复杂的 Web 应用程序，GPT-5 会如何应对？

“GPT-5 是一个强大的通用模型，也可以仅使用 HTML / CSS / JavaScript 来制作 Web 应用程序，”Singal 相当含糊地回答说。

我用我的下一个问题尝试了一个不同的角度：开发者，尤其是前端开发者，是否可以“训练”GPT-5 仅使用 Web 平台技术——即使用 GPT-5 来摆脱对框架和/或 [React 的依赖](https://thenewstack.io/web-development-trends-in-2024-a-shift-back-to-simplicity/)？

“GPT-5 是目前最具可控性的模型，开发者在提示工程方面取得了巨大成功，可以从中获得非常具体的行为和结果，”Singal 回答说。“如果 GPT-5 可以帮助解决这个问题，我不会感到惊讶。”

> “GPT-5 是目前最具可控性的模型，开发者在提示工程方面取得了巨大成功，可以从中获得非常具体的行为和结果。”
> **– Ishaan Singal, OpenAI 研究员**

另一个不置可否的答案。让我们再试一次：OpenAI 是否认为 GPT-5 可以加速采用更现代的 Web 原生功能——例如 [CSS Houdini](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_properties_and_values_API/Houdini) 和 [Web Components](https://thenewstack.io/how-microsoft-edge-is-replacing-react-with-web-components/)——这些功能通常被框架所掩盖？

“这在一定程度上取决于利用 GPT-5 为其用户提供构建 UI 组件工具的应用程序，”Singal 回答说。“许多这些应用程序对它们喜欢的技术和功能的类型有自己的看法，我认为这会影响这种采用。”

因此，到目前为止，我们了解到的是，GPT-5 理论上可以涵盖所有前端用例——但这很大程度上取决于你已经使用的工具以及你（开发者）想要采取的方法。同样值得注意的是，OpenAI 本身也在对其推荐用于 GPT-5 的工具采取“有偏见”的态度：Next.js (TypeScript)、React 和 HTML；对于样式设置，它推荐 Tailwind CSS、shadcn/ui 和 Radix Themes。

## 其他人对 GPT-5 有何评价？

如果 OpenAI 在这个阶段（可以理解地）不愿报告实际的开发者体验，那么代码安全公司 Sonar 就不会那么害羞了。它最近发布了 [关于 LLM 个性的代码状态报告](https://www.sonarsource.com/sem/the-coding-personalities-of-leading-llms/?utm_medium=paid&utm_source=newstack&utm_campaign=ss-state-of-llms25&utm_content=newsletter-TNS-newsletter-stateofllm-x-x&utm_term=ww-psp-x&s_category=Paid&s_source=Paid%20Other&s_origin=newstack&utm_content=inline-mention) 的更新，其中包含 [关于 GPT-5 的新数据](https://www.sonarsource.com/blog/the-coding-personalities-of-leading-llms-gpt-5-update/)。

Sonar 得出的结论是，根据其测试，GPT-5 并非编码性能的领导者。

以下是 Sonar 的发现摘要：

* 即使在 GPT-5 到来之后，Claude Sonnet 4 仍然是 Sonar 测试的所有模型中的性能领导者。
* GPT-5 生成的“代码量比任何其他模型都更大、更复杂”，这使其“成为审查和维护的严峻挑战”。
* 对于 GPT-5 成功完成的每项任务，它都会引入“比其竞争对手明显更多的潜在缺陷，从而导致大量的下游技术债务、质量、安全和验证负担”。
* GPT-5 产生的漏洞密度最低，但它具有“更高的代码异味密度”，这意味着代码在质量和可维护性方面较弱。

Sonar 总结说，GPT-5 “无疑是 AI 代码生成领域的一股强大的新力量”，但需要注意的是，该模型“带来了巨大的质量成本，并提出了不同的安全性和可靠性考虑因素”。

> GPT-5 “带来了巨大的质量成本，并提出了不同的安全性和可靠性考虑因素。”
> **– Sonar 关于 GPT-5 和编码的报告**

Sonar 还对 GPT-5 在超过 4,400 个 Java 任务中的 [推理模式进行了单独研究](https://www.sonarsource.com/blog/how-reasoning-impacts-llm-coding-models/)。这揭示了一个明确的权衡：“虽然更高的推理能力提供了同类最佳的功能性能，但它通过生成大量的复杂且难以维护的代码来实现这一点。”

为了给 GPT-5 的分析添加第二个外部声音，让我们回到我们的老朋友 YouTube 用户 Theo Browne——他是那位 180 度大转弯的著名开发者。事实上，他是 OpenAI 发布日视频中出现的开发者之一，当时 [他很喜欢 GPT-5](https://x.com/theo/status/1953516806104056096)。但仅仅一周后，他发布了一个名为“[我误解了 GPT-5](https://www.youtube.com/watch?v=k68ie2GcEc4)”的视频。那么 Browne 现在对 GPT-5 的感觉如何？

在 [他发布后的几周内发布的关于 GPT-5 的最新视频](https://www.youtube.com/watch?v=SOxmiupQm7w) 中，Browne 将他遇到的一些问题归咎于 GPT-5 在 ChatGPT 和 Cursor 中的实现方式。“Cursor 的实现中现在仍然存在很多 UX 失败，”他补充说。“但尽管如此，我仍然认为 5 是一个令人难以置信的模型。它仍然是我用于所有工作的模型。”

[![前端开发影响者 Theo Browne 试图决定他对 GPT-5 的看法。](https://cdn.thenewstack.io/media/2025/09/3de70858-theo-browne-gpt5-3weekslater.jpg)](https://cdn.thenewstack.io/media/2025/09/3de70858-theo-browne-gpt5-3weekslater.jpg)

前端开发影响者 Theo Browne 试图决定他对 GPT-5 的看法。

因此，Sonar 和 Browne 都承认 GPT-5 是一种强大的编码工具，尽管 Sonar 对其代码质量和可维护性更为 критично.

## 一次性完成还是着眼于维护？

回到 OpenAI 对我问题的回答。OpenAI 的指南还指出，“GPT-5 擅长一次性构建应用程序。”这似乎是针对所谓的“[氛围编程](https://thenewstack.io/the-field-cto-view-ai-vibe-coding-and-developer-skillsets/)”；但我问道，是否也鼓励专业开发者在 GPT-5 中“一次性”完成所有事情，或者他们是否应该采取更审慎的方法？例如，考虑到代码的未来维护，正如 Sonar 显然希望的那样。

“GPT-5 经过训练，擅长从零开始构建应用程序，并在仓库中以代理方式开发更完整的全栈应用程序，”Singal 回答说，毫不意外地涵盖了所有用例。但他在回复的下一部分稍微更加热情：

“对于构建新原型的开发者来说，端到端地零样本化一个应用程序可能是验证想法的一种快速方法。对于正在处理现有应用程序或构建需要长期维护的应用程序的开发者来说，使用代理线束并迭代细粒度功能可能更可取。这实际上取决于情况。”

> “归根结底，这是开发者的选择。”
> **– Singal**

互联网供应商通常会将所有责任推回给用户——[Napster 并没有错](https://cybercultural.com/p/napster-1999/)，一些用户下载非法内容，Facebook 并没有错，一些用户有极端的政治观点，等等。同样，OpenAI 对开发者说：嘿，你如何使用 GPT-5 是你的选择。

“归根结底，这是开发者的选择，”Singal 说，“但已建立的仓库从社区获得更好的支持。这有助于开发者进行自助维护。”

关于 GPT-5 目前的使用情况，Singal 补充说，“我们已经看到了氛围编程者/从零开始的应用程序开发者和将此插入到他们现有的巨型应用程序中进行迭代的人的良好组合。”

## 针对 AI 优化的框架

Singal 更具偏见性的回复之一是我为了好玩而提出的一个前瞻性问题。

你如何看待针对 AI 优化的框架的可能性？例如，更小的运行时占用空间或 AI 友好的组件 API。Singal 似乎很感兴趣。

“这是一个有趣的想法！需要考虑的是可维护性以及“人机回路”存在的最佳程度。对 AI 来说最佳的东西可能并不适合人类理解。也就是说，随着 AI 用于编码继续成为主流工作流程的一部分，这最终可能会变得更加普遍。”

因此，请密切关注未来针对 AI 优化的前端框架。与此同时，以最适合你的方式使用 GPT-5——但要注意代码质量和可维护性。