# 人工智能辅助编码：安全领域的双刃剑

![Featued image for: AI-Assisted Coding: A Double-Edged Sword for Security](https://cdn.thenewstack.io/media/2024/07/9aa57160-bruce-pic-1-1024x768.png)

巴黎——越来越多的开发者正在使用和创建人工智能模型以及[大型语言模型 (LLM)](https://thenewstack.io/llm/)，因为这些工具既可以用于创建代码，也可以用于开发 LLM 应用程序。LLM 的流行程度呈爆炸式增长，但尽管人们对此热情高涨，但由这种快速发展带来的安全问题仍然没有得到解决，没有得到充分理解，最终被忽视。

一些观察人士，尤其是在安全行业，认为我们在安全机制得到妥善实施和管理之前，发展速度过快。这与[Kubernetes](https://thenewstack.io/llm/)等云原生技术的错误类似，在广泛采用之前，安全问题没有得到充分解决。在所有安全问题得到解决之前，很难阻止人们使用尖端技术。

“问题在于代码量——使用[Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/) 和 GPT 等工具编写代码意味着你编写的代码比以前多得多，这对提高生产力很有帮助，但不会加快安全流程。我们实际上是用所有这些新代码堵塞了管道，”[Chainguard](https://www.chainguard.dev/) 的联合创始人兼首席执行官[Dan Lorenc](https://www.linkedin.com/in/danlorenc) 在最近的 Linux 基金会[AI_dev](https://aidevsummit.co/) 大会主题演讲中表示。“安全团队已经难以跟上开发者的步伐，现在编写的代码量增加了十倍……没有哪个安全团队能够处理 100 倍的代码量。”

安全团队通过可观察性来审查和监控安全性的艰辛是众所周知的。但当他们寻找错误和漏洞并测试新功能时，“这种方法无法应对 100 倍的代码量、100 倍的功能数量和 10 倍的开发者数量，”Lorenc 在大会前几天告诉我。

越来越多的开发者正在部署人工智能工作负载，但他们并不真正了解如何安全地进行部署，[Chainguard_dev] 的 [Lorenc_dan] 在 [#AIDev] 大会上表示。[@CloudNativeFdn][@linuxfoundation][@thenewstack][pic.twitter.com/XMqfYKZfgn]— BC Gain (@bcamerongain)

[2024 年 6 月 19 日]

人工智能辅助开发导致了可用的开源代码和[GitHub](https://thenewstack.io/githubs-2fa-push-boosts-adoption-among-developers/) 上的拉取请求激增。正如 Lorenc 指出的那样，在许多情况下，人工智能的 GitHub 存储库在周末获得了数十万颗星，许多人甚至没有人工智能背景，也在编写人工智能代码。“看到新人编写和使用代码真是太好了，这很棒，但我们不能忘记保护底层的所有层级——一切都没有改变。但你必须为那些不了解所有这些小问题的新一代人做好准备，”Lorenc 说。“你必须让他们的安全知识变得不再必要——告诉每个开发者他们必须了解安全知识的做法从未奏效。”

在演讲中，Lorenc 将[人工智能生成的代码](https://thenewstack.io/ai-code-generation-6-faqs-for-developers/) 和模型与热力学进行了比较，我记得大学里的同学声称教授说热力学 99% 是混乱的。

就像无法预测电子的速度和位置一样，我认为。人工智能安全困境与工程中的流体动力学类似，[Chainguard_dev] 的 [Lorenc_dan] 在 [#AIDev] 大会上表示。[@CloudNativeFdn][@linuxfoundation][@thenewstack][pic.twitter.com/bZHAXZ0TAO]— BC Gain (@bcamerongain)

[2024 年 6 月 19 日]

Lorenc 将目前的困境比作流体动力学——我听说这门课很难，当时我在大学。与更可预测的层流不同，人工智能安全就像测量和预测在混乱环境中表现出的湍流模式。当开发者使用人工智能工具编写越来越多的代码时，他们并没有使用相同的技术来帮助审查这些代码，导致目前的情况是“流经管道的流量超出了我们的处理能力，”Lorenc 在主题演讲中说。
“当事物开始从一种模型过渡到另一种模型时，这种过渡状态实际上是最难推理的。这是最难建模的系统类型。在流体动力学中，这种过渡也不是在某个特定时间发生的，”Lorenc 说。“有一些常数和比率可以代入，试图预测和猜测你所处的状态，但大量的工程工作都投入到确保你知道你所处的状态，无论是层流还是湍流。当你处于中间状态时，你真的不知道该怎么做。”

Lorenc 说：“攻击者已经开始使用 LLM 生成新的漏洞或对现有漏洞进行排列组合，以绕过签名检测。”“我们必须摆脱这种过渡状态，才能完全理解并能够再次作为行业共同努力，”Lorenc 说。“然而，当这种过渡完成，你回到湍流状态时，会让大家感到很不舒服，因为科学家和物理学家实际上无法解释它是如何工作的。”

![](https://cdn.thenewstack.io/media/2024/07/db459e4e-img_4850-2.jpg)
Jossef Kadouri 和 Tzachi Zornshtain 都是 Checkmarx 的软件供应链负责人，他们在他们的演讲“AI 的黑暗面：开放中的隐藏供应链风险”中描述了来自 AI 的供应链威胁。

开发人员可以尽力审查 AI 生成的代码，但为了使漏洞检测和修复变得有效，还需要做更多工作。在他们的演讲“AI 的黑暗面：开放中的隐藏供应链风险”中，[Jossef Kadouri](https://www.linkedin.com/in/jossef/) 和 [Tzachi Zornshtain](https://www.linkedin.com/in/tzachi-zornstain/)，他们都是 [Checkmarx](https://checkmarx.com/) 的软件供应链负责人，描述了具体的威胁向量。

当使用带有权重的 ML 模型时——这些参数经过精心调整，以提高特定 LLM 中的神经计算结果——很难确定代码是恶意还是良性。“我并不是说开发人员过去会检查他们下载的代码——大多数人没有这样做，但至少他们有这个选择，”Zornshtain 说。“当你获得一个 [ML 模型](https://thenewstack.io/training-a-ml-model-to-forecast-kubernetes-node-anomalies/) 时，它是好的还是坏的？对我们来说，在某些方面进行更改实际上更麻烦。”

我们当中有多少人在编写程序或生成代码时，没有至少向 [ChatGPT](https://thenewstack.io/how-to-learn-unfamiliar-software-tools-with-chatgpt/) 征求意见，或者使用过 GitHub Copilot 之类的工具？然而，输入 ChatGPT 或其他 LLM 的结果并不总是相同的，这是由于机器学习的神经网络配置以及这些 AI 模型涉及幻觉的其他方面。Zornshtain 说，当使用开源 LLM 来构建服务时，攻击者可以在那里上传一个恶意的 LLM 模型，并“欺骗你使用它”。他说，恶意行为者可以将恶意代码漏洞注入 LLM，并通过社会工程学操纵特定 LLM 的输出，这只是两种风险。

与此同时，Zornshtain 说，使用开源软件包或模型的开发人员应该对他们使用的 LLM 模型的质量和安全性负责。“话虽如此，作为提供这些解决方案的行业，我们是否拥有适当的控制措施？不一定，”Zornshtain 说。“我们知道安全问题在哪里，但这些检查今天正在进行吗？根据我们所看到的，答案不一定是我们想要的。”

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)