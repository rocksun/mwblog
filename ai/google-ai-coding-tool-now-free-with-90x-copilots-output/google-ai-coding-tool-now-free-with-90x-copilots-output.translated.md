# Google AI 编码工具现已免费，输出量是 Copilot 的 90 倍

![Google AI 编码工具现已免费，输出量是 Copilot 的 90 倍的特色图片](https://cdn.thenewstack.io/media/2025/02/9760d8c8-steve-johnson-ugie9ddsmpu-unsplashb-1024x576.jpg)

Google 刚刚发布了其 AI 编码工具 [Gemini Code Assist](https://codeassist.google/) 的免费版本，该工具此前主要面向付费企业计划用户提供，每月起价 19 美元。Google 不仅向个人免费开放该工具，还每月提供高达 180,000 次代码补全——这比其主要竞争对手 GitHub Copilot 提供的 2,000 次代码补全要多得多。

我与 Google Cloud 的高级产品管理总监 Ryan J. Salva 谈到了这个消息。在去年加入 Google 之前，Salva 在 GitHub 担任产品副总裁超过四年。因此，他非常适合比较 GitHub 的市场领先工具。

每月 180,000 次代码补全让人想起 [Google 在 2004 年推出 Gmail](https://cybercultural.com/p/002-the-early-years-of-readwriteweb/)。Gmail 最引人注目的功能是它提供的 1GB 存储空间——是 Yahoo 和 Microsoft 提供存储空间的 100 多倍。重新发布的 Gemini Code Assist 几乎与之匹敌，其提供的代码补全次数是 Microsoft 等效 GitHub 产品的 90 倍。

我问 Salva 为什么他们选择 180,000 次代码补全，这个数字远高于其竞争对手？

> “我们希望有效地提供一项服务，以满足 98-99% 全天候使用该服务的开发人员的需求。”
>
> – Google Cloud 的 Ryan J. Salva

他回答说：“基本上，我们所做的是查看我们一些专业工程师的当前使用情况以及他们使用该工具的频率。”“我们希望有效地提供一项服务，以满足 98-99% 全天候使用该服务的开发人员的需求。因此，我们将上限设定为一个数字，如果超过这个数字，就意味着你必须是一位极其专注的工程师，每天在代码编辑器中工作很多很多小时。所以这里的想法是，让它实际上无限使用。”

显然，这会给 Google 的 AI 计算基础设施带来相当大的负担，但 Salva 指出，Google“以能够处理大规模计算而闻名于世”。考虑到 Google 在扩展 Gmail（更不用说搜索！）方面的经验，谁能反驳这一点呢？

## 它与 GitHub Copilot 的其他区别是什么？

面向个人的 Gemini Code Assist 在全球范围内可用，并由 Google 最新的大型语言模型 [Gemini 2.0](https://deepmind.google/technologies/gemini/) 提供支持，该模型“专为自主时代而构建”。该工具“支持公共领域的所有编程语言”，并且已针对编码进行了优化。从大型语言模型能力的角度来看，这使得 Gemini Code Assist 与 GitHub Copilot 旗鼓相当（Copilot 的免费版本由 OpenAI 的旗舰模型 GPT-4o 提供支持）。

与 GitHub Copilot 一样，Gemini Code Assist 也可作为 VS Code 和 JetBrains IDE 集合中的扩展程序使用。

但是，除了代码补全次数之外，与 GitHub Copilot 还有哪些关键区别？

Salva 首先指出了其免费层中聊天功能的 128,000 个令牌限制。根据 [Google 的博文](https://blog.google/technology/developers/gemini-code-assist-free/)，“这个大型上下文窗口允许开发人员使用大型文件，并让 Gemini Code Assist 对其本地代码库有更广泛的理解。”相比之下，GitHub Copilot 在使用 GPT-4o 时提供 [64,000 个令牌窗口](https://github.blog/changelog/2024-12-06-copilot-chat-now-has-a-64k-context-window-with-openai-gpt-4o/)。

其次，Salva 提到了 Google 今天宣布的另一个新功能：一个名为 [Gemini Code Assist for GitHub](https://github.com/apps/gemini-code-assist) 的代码审查代理，它作为 GitHub 应用提供。

这些是免费计划的主要区别，但 Salva 指出付费计划还有更多区别。其中一项功能是能够从远程存储库中提取数据。

Salva 说：“GitHub 有效地激励人们使用 GitHub。”“你知道，这是有道理的——这是他们的业务。但是有很多组织不仅仅使用 GitHub。也许他们正在使用 GitLab，或者他们正在使用 Bitbucket，或者他们正在使用本地部署的，也就是自管理的版本控制系统。……我们没有参与源代码管理解决方案，因此我们将连接到远程存储库。”

## 自主 IDE 和其他 AI 开发工具
我注意到最近涌现出一批新的[AI 编码工具](https://thenewstack.io/self-driving-software-solver-launches-autonomous-ai-coder/), 其中一些声称是能够从头创建整个应用程序的[自主式 IDE](https://thenewstack.io/beyond-dx-developers-must-now-learn-agent-experience-ax/)。三个比较有趣的例子：[Bolt](https://bolt.new/) 于去年十月从 StackBlitz 分拆出来，[Windsurf](https://codeium.com/windsurf) 于十一月发布，而[Lovable](https://lovable.dev/) 于十二月以目前的迭代形式推出（之前它是一个名为 GPT Engineer 的开源项目）。

对此，Salva 预告了四月将会有更多公告，并作出了如下观察：

“业界普遍追求的是：如何跨多个文件进行批量更改，并且不仅对单个组件进行推理，还要对整个系统进行推理？而这正是你进入自主工作流程的时候。”

所有最新的 AI 编码工具的共同点是它们的目标用户是单个开发者，其中许多人并非专业开发者。[Bolt 的用户群中有 60-70%是非专业人士](https://thenewstack.io/how-developers-are-using-bolt-a-fast-growing-ai-coding-tool/)，Bolt 首席执行官 Eric Simons 本月初告诉我。谷歌显然正试图进军同样的主流用户群——其公告文章特别提到了“学生、业余爱好者、自由职业者和初创企业”。


“……我们的总体方法是将需求文档和自然语言视为基础。”

– Salva

关于[英语成为新的默认编程语言](https://thenewstack.io/can-english-dethrone-python-as-top-programming-language/) 的讨论很多，谷歌的 Ryan Salva 似乎也认同这一点。

他告诉我：“我认为我们的总体方法是将需求文档和自然语言视为基础。因此，开发人员不必仅仅凭借 Python、Java 或 C# 的知识来使用它[Gemini 代码助手](https://codeassist.google/)。他们可以考虑自己想创建什么系统，通过自然语言意图表达出来，然后*通过它*产生结果或产生软件。”


## 更自主功能的基础

Salva 明确表示，对于面向大众的 AI 辅助编码工具而言，这仅仅是谷歌的开始。

“我们正在为如何将基本的工具和 IDE 推广给尽可能多的人，并提供非常宽松的使用限制，并且实际上除了电子邮件地址之外没有任何其他要求奠定基础。”

他暗示，其未来的计划将包括“新的自主功能，坦率地说，不仅仅是在 IDE 中使用 AI——而是在 IDE 之外的各种其他界面中使用 AI”。

AI 辅助编码的“其他界面”是什么，还有待观察。但就目前而言，专业和业余开发者都应该去查看新的[面向个人的 Gemini 代码助手](https://codeassist.google/)，并尽情使用数万个代码补全功能。

[YOUTUBE.COM/THENEWSTACK 科技发展日新月异，不要错过任何一集。订阅我们的 YouTube 频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)