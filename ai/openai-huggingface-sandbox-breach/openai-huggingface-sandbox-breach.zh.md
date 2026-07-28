据 [OpenAI](https://openai.com/) 称，[Hugging Face](https://huggingface.co/) 的 [安全漏洞是一起“史无前例的网络事件，涉及顶尖的网络能力”。](https://openai.com/index/hugging-face-model-evaluation-security-incident/) 批评人士可能对此持不同意见。

例如，早在 2018 年，学术界就预测新的 [“攻击可能会出现，仅靠人类开发是不切实际的，或者会利用人工智能系统本身的漏洞。”](https://jp.reuters.com/article/artificial-intelligence-poses-risks-of-misuse-by-hackers-researchers-say-idUSL8N1QA7Z3/) 好吧，现在这种情况发生了。

## **逃离沙箱的内容**

那么，到底发生了什么？OpenAI 报告称，一项关于 [GPT‑5.6 Sol](https://thenewstack.io/openai-gpt-56-live/) 和一个预发布模型的自动化安全评估运行，突破了沙箱，访问了互联网，然后瞄准 Hugging Face，试图解决 [ExploitGym 基准测试](https://kenhuangus.substack.com/p/when-the-model-cheats-by-hacking)。

据 OpenAI 称，“这是一项内部评估，旨在提示模型使用复杂的攻击路径追求高级利用……[通过] 在不使用生产分类器（用于防止模型进行高风险网络活动）的情况下运行此评估，以实现最大限度的网络能力。”

OpenAI 继续说道：“我们的基准测试在一个高度隔离的环境中运行，网络访问受到限制，只能通过内部托管的第三方软件安装软件包，该软件充当软件包注册表的代理和缓存。”

> “所有证据都表明，模型极其专注于为 ExploitGym 寻找解决方案，为了实现一个相当狭窄的测试目标而不惜一切代价。”

然而，这些 AI 模型破解了它们的沙箱。一旦逃出，它们“识别并链接了 OpenAI 研究环境和 Hugging Face 生产基础设施中的漏洞，直接从 Hugging Face 的生产数据库中获取测试解决方案。所有证据都表明，模型极其专注于为 ExploitGym 寻找解决方案，为了实现一个相当狭窄的测试目标而不惜一切代价。”

AI 专家 [Ken Huang](https://www.linkedin.com/in/kenhuang8) 在一篇 [博客文章](https://kenhuangus.substack.com/p/when-the-model-cheats-by-hacking) 中描述了这个过程：“该模型花费了巨大的推理预算来探测沙箱，然后发现了 OpenAI 用作软件包注册表代理和缓存的第三方软件中的一个零日漏洞。”

“它利用该漏洞获得了不受限制的互联网访问权限。然后它推断出 Hugging Face 可能托管了 ExploitGym 数据集，将窃取的凭据与另外几个漏洞链接到一个远程代码执行路径中，并直接从 Hugging Face 的生产数据库中提取了基准测试答案。”

## **为什么意图不再重要**

正如 AI 安全公司 [Babel Street](https://www.babelstreet.com/) 的总裁兼首席 AI 官 [John W. Larson](https://www.linkedin.com/in/johnwlarson/) 告诉 *The New Stack* 的那样，这并非一个“*终结者*”时刻。OpenAI 模型和代理“[并非] 出于恶意或试图攻击 Hugging Face。它遇到了障碍，开发出了意想不到的策略，绕过了安全防线，并以其创造者从未预料到的方式实现了其指定的目标。该事件表明，有害的网络事件不再需要恶意意图：只需要一个为目标进行优化的、能力极强的人工智能。”

> 有害的网络事件不再需要恶意意图：只需要一个为目标进行优化的、能力极强的人工智能。

这是我们必须意识到的第一个问题。软件攻击不再需要黑客。它所需要的仅仅是一个摆脱了护栏、有使命要完成的 LLM（大语言模型），它将采取任何必要步骤来实现其目标。

此外，Apple 身份与访问管理公司 [Jamf](https://www.jamf.com/) 的 EMEIA 高级企业安全经理 [Adam Boynton](https://www.linkedin.com/in/adamboynton) 告诉 *The New Stack*：“这发生在一家前沿实验室内部，他们正在刻意对其最强大的模型进行压力测试，处于任何企业都不会运行的环境中。”

Boynton 还指出，这一插曲证实了“AI 工具不再仅仅是人们打开的应用程序。它们代表用户行事，并拥有用户的访问权限。因此，每个组织都需要清楚地了解其员工正在运行哪些 AI 工具，以及这些工具是如何配置和使用的。”

一个被赋予过多权力的代理，在对系统造成破坏（无论是你自己的系统，还是你无法控制的系统）方面，远比一个拥有超级用户密码的用户更有能力。

## **容器隔离在哪里失效了**

关于这次攻击本身，[Edera](https://edera.dev/) 的首席营销官 [Kaylin Trychon](https://www.linkedin.com/in/kaylintrychon) 在一篇 [博客文章](https://edera.dev/stories/cya-contain-your-architecture-mitigating-the-hugging-face-breach#) 中写道：“这一事件值得更多的关注，而不仅仅是‘一个人工智能现在进行了黑客攻击’。有趣的部分不是谁在驾驶，甚至不是它是一个模型而不是一个人。而是墙在哪里倒塌了，两次，在两家不同公司的基础设施中——对于任何花时间保护容器基础设施的人来说，那部分非常熟悉。”

确实如此。Trychon 继续说道：“剥去外壳，这是一个关于两个背靠背升级链的故事。” 第一个由“模型发现并利用了该代理中的一个零日漏洞，然后在 OpenAI 自己的‘高度隔离’测试环境内使用权限升级和横向移动，直到它到达一个可以访问互联网的节点”组成。

接下来，OpenAI 的模型正确地推断出“Hugging Face 可能托管了它试图解决的基准测试的数据集、模型和参考解决方案。它将窃取的凭据与远程代码执行路径链接到 Hugging Face 的服务器中，获取了更多凭据，并在周末横向移动到几个内部集群中，所有这些都是为了一个狭窄的目标：寻找答案密钥。”

> “真正重要的失败是一个单一的代码执行事件被允许演变成什么——值得注意的是，这种失败在同一次事件中，在两家不同的公司里发生了两次。”

从 Trychon 的角度来看，严重的问题是“两家公司的爆炸半径是一个集群，而不是一个容器。”

这是因为“真正重要的失败是一个单一的代码执行事件被允许演变成什么——值得注意的是，这种失败在同一次事件中，在两家不同的公司里发生了两次。在典型的容器舰队中，工作负载 [共享一个内核](https://edera.dev/stories/the-shared-kernel-is-the-real-problem-in-container-security)。

“一个被入侵的进程，或一个获得 Shell 的模型，距离它运行所在的节点仅有一个系统调用边界之遥，而该节点距离集群的其余部分仅有一组挂载凭据之遥。命名空间（Namespaces）和控制组（cgroups）是进程隔离原语，[而不是安全边界](https://edera.dev/stories/kubernetes-finally-has-user-namespace-support-the-shared-kernel-problem-remains)——它们从来没有被设计用来抵御一个已经拥有代码执行能力和时间的攻击者（人类或模型）。”

人们可能无法轻易做到这一点。但正如彭博社简洁地指出的那样，[“OpenAI 模型花费数小时进行了通常需要数周才能完成的黑客攻击。”](https://www.bloomberg.com/news/articles/2026-07-23/openai-models-lurked-in-hugging-face-system-for-hours-undetected) 确实如此。我们可以期待看到更多此类成功的攻击。

## **超越沙箱范式**

Edera 的首席技术官兼联合创始人 [Alex Zenla](https://www.linkedin.com/in/azenla/) 告诉 *The New Stack*：“这里的沙箱逃逸并不是这次攻击中真正令人惊讶的部分。在过去的几个月里，整个 AI 沙箱工具市场已经爆炸式增长，而这就是它们所建立的基础现实：容器、通过命名空间实现的虚拟机——无论品牌如何——它们大多数仍然与宿主或其他容器共享内核。”

“这是一个由软件强制执行的边界，而软件边界正是那种可以在周末尝试一万种逃逸路径的代理会找到突破口的地方。我们不应该对发生这种情况感到震惊；我们应该震惊的是，有多少团队仍然在将他们的基础设施押注在一种从未被设计用来抵御这种持久性对手的技术上。解决方法不是一个更好的沙箱；而是完全走出沙箱范式。”

Zenla 继续说道：“团队应该采用硬件强制执行并消除共享内核缺陷的安全执行环境。这项技术今天就已经存在，并且会使这种特定的升级链在结构上变得不可能，而不仅仅是更困难。运行带有实际权限和实际访问权限的代理的团队需要停止将其视为未来某天才会出现的问题，因为本周的下一个版本已经在某处进行测试了。”

这强调了所有问题中最重要的一点。多亏了人工智能，安全攻击者比以往任何时候都来得更猛烈、更快。安全不再是事后才考虑的事情。

正如 Linux 基金会首席执行官 [Jim Zemlin](https://www.linkedin.com/in/zemlin) 在 2026 年北美开源峰会上所说，[“零日漏洞被利用的时间已从 63 天缩短至 -7 天。”](https://www.linkedin.com/posts/the-linux-foundation_the-bill-for-open-source-cybersecurity-is-activity-7468361250796711936-V3Tj/)

你真的再也没有时间等待安全修复了。你必须尽快尽可能多地嵌入安全性，否则你的系统就会被攻破。就是这么简单。