<!-- 
# Codeanywhere 创始人用 Daytona 抗衡 GitHub Codespaces
Codeanywhere Founders Take on GitHub Codespaces with Daytona
https://thenewstack.io/codeanywhere-founders-take-on-github-codespaces-with-daytona/
https://cdn.thenewstack.io/media/2023/09/8813aa02-1692021975-daytona_illustration_91-1024x574.jpeg
Image via Daytona
 -->

云开发环境能自托管吗? Codeanywhere 创始人的新产品 Daytona，旨在做到这一点。

译自 [Codeanywhere Founders Take on GitHub Codespaces with Daytona](https://thenewstack.io/codeanywhere-founders-take-on-github-codespaces-with-daytona/) 。

Codeanywhere 是 2009 年发布的[最早的网络代码编辑器之一](https://thenewstack.io/why-cloud-ides-are-shifting-to-a-platform-as-a-service-model/)(以 PHPanywhere 之名)。从那时起，整个开发者环境已经迁移到云端，Codeanywhere 发现自己在极具竞争力的[云 IDE](https://thenewstack.io/integrated-development-environments-moving-cloud/) 市场中落后，GitHub Codespaces 和 [Replit](https://thenewstack.io/developers-get-a-quick-start-to-coding-with-replit-ide/) 等较新产品已经占据主导地位。为了扭转这一点，三位 Codeanywhere 老将 —— Ivan Burazin、Vedran Jukic 和 Goran Draganić —— 正在启动一个全新的公司，名为 [Daytona](https://www.daytona.io/)。

Daytona 被吹捧为 “GitHub Codespaces 的安全替代品”，并以允许企业“自我管理” Daytona 的自己的基础设施这一新奇的云 IDE 方案。我与联合创始人兼首席执行官 [Ivan Burazin](https://www.linkedin.com/in/ivanburazin/) 进行了交谈，以了解更多信息。

## Daytona 与 GitHub Codespaces 有何不同？

在我们谈到与 GitHub Codespaces 的竞争之前，首先要澄清 Daytona 与其前身 Codeanywhere 的不同之处。

“主要的是 Codeanywhere 更像是一个界面产品，而这个(Daytona)更像是一个基础设施，”Burazin 说。

他说的“界面”是指 Codeanywhere 仅仅为它托管的开发者环境提供了一个云界面。但 Daytona 比这更复杂。

“我们从构建 Codeanywhere 中学到的实际上是我们在下面启动的基础设施，” Burazin 继续说道。“以及如何有效启动这些开发环境的知识，基本上就是 Daytona 的内容。”

通过 Daytona，开发者可以使用他们的本地 IDE，而不是(或与之并存)基于云的 IDE。因此，如果他们已经使用诸如 VS Code 或 JetBrains IDE 之类的软件产品，则它与 Daytona 兼容。

“我们所做的就是将开发环境从本地机器移到云端或远程服务器等处，” Burazin说，“并且这个远程开发环境与 IDE 的所有连接都是我们在后台做的；我们启动它们然后关闭它们。用户，即开发人员，会觉得他们在本地工作。”

现在，值得注意的是，GitHub Codespaces 也允许其用户在本地环境上工作。 在其主页上，GitHub 指出，Codespace 用户可以“使用 Visual Studio Code、Jupyter 或 JetBrains”。 这是通过这些特定桌面软件产品中的扩展实现的。 但是，GitHub 在其 FAQ 中明确指出，codespace 的实际托管是在 GitHub 的云端完成的。

Daytona 提供的本质上是自托管开发环境的能力防火墙后面。 这是与 GitHub Codespaces 的核心区别。

![](https://cdn.thenewstack.io/media/2023/09/1ef9ae94-screenshot-2023-09-06-at-16.06.14.png)
*来自 Daytona*

## 又一个云 IDE ... 呃，SDE

为了完全专注于 Daytona，Burazin 和他的联合创始人停止了对 Codeanywhere 的工作 —— Burazin 说它“最终会被逐渐停用”。

那么，在这个已经非常拥挤的领域建立另一个云 IDE 产品的动机是什么？Burazin 回答说，他们所做的研究表明，企业公司希望一个安全、可扩展的开发环境，可以跨本地机器和云工作。

顺便说一下，“安全”这个词在这里起着非常重要的作用。 当 Daytona 说它是“GitHub Codespaces 的安全替代品”时，它简单地意味着自托管(在防火墙后面)的能力本质上比在外部提供商(如 GitHub)上托管更安全。

根据 Burazin 的说法，市场上提供自托管的选择不多，因此他说许多公司构建内部产品以满足该需求。 他提到 Uber、Shopify、LinkedIn 和 Eventbrite 作为例子。

Burazin 继续说，其他公司倾向于依靠 Citrix Server 等技术来启用企业防火墙外的 IDE 远程访问。

“为了确保代码的安全，他们基本上会在防火墙内给他们一个 VM(虚拟机)，开发人员与之交互的唯一方式是通过 Citrix Terminal Services。 所以他们不得不流式传输 IDE; 因此它缓慢、缓慢、非常麻烦。 因此，像 Daytona 这样的产品允许企业将这些开发环境安全地托管在防火墙后面，但工程师或开发人员可以使用本地 IDE，以便他们感觉在本地工作。”

除了 GitHub Codespaces，我问 Burazin 还有谁是 Daytona 的竞争对手。

“最接近的竞争对手[...]是 Codespaces 和 Gitpod，就这些产品的创建方式而言——但其中没有一个允许你自行管理它，”他说，并补充说“唯一可以做到这一点的产品是 Coder。”

我们之前在 The New Stack 上[报道](https://thenewstack.io/coder-speeds-build-time-with-multicloud-platform/)过 [Coder](https://coder.com/)，它将自己推广为“您的自托管远程开发平台”。

也许为了区别于其他，Daytona 为其产品创造了一个新的缩写：SDE，代表“标准化开发环境”。

“SDE 不仅提供基于云的开发平台，还能确保整个开发生命周期的一致性，”该公司在其发布新闻稿中指出。

我不确定一个新的首字母缩略词是否有助于一个已经对什么是或不是“云 IDE”感到困惑的市场。 Daytona 的另一个主要竞争对手 Gitpod 使用“云开发环境”(CDE)这一术语。 根据 Burazin 的说法，CDE 是 SDE 概念的“一个子集”。

## 结论

尽管所有的首字母缩略词，但自托管开发环境的能力对企业来说似乎是一个有吸引力的产品优势。 一个大问题是，微软拥有的 GitHub(当然是微软拥有的) 是否也会在适当的时候提供这个功能。 但就目前而言，Daytona 已准备好用这种功能来对抗 Coder。
