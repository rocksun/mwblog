
<!--
title: 供应商：为什么你仍然忽视安全漏洞
cover: https://cdn.thenewstack.io/media/2024/03/869fcc10-glass-3983411_1280.jpg
-->

来自 Nix 社区的 FOSDEM 警示演讲，关于所有可能仍被您系统忽视的易受攻击软件。

> 译自 [Vendoring: Why You Still Have Overlooked Security Holes](https://thenewstack.io/vendoring-why-you-still-have-overlooked-security-holes/)，作者 Joab Jackson。


# 供应商：为什么你仍然忽视了安全漏洞？

![供应商的特色图片：为什么你仍然忽视了安全漏洞](https://cdn.thenewstack.io/media/2024/03/869fcc10-glass-3983411_1280-1024x640.jpg)

[CVE-2023-4863](https://nvd.nist.gov/vuln/detail/CVE-2023-4863) 漏洞揭示了 Nix 存储库中供应商问题变得多么严重，Nix Packages 维护者 [Delroth](https://github.com/delroth)（Pierre Bourdon）在 2 月 5 日的 FOSDEM 演讲中回忆道，“[修复 nixpkgs 中的 1000 多个未跟踪漏洞](https://video.fosdem.org/2024/h1302/）”，最近在线发布。

在 Google Chromium 浏览器中发现了 libwebp 图像解码器 (v1.3.2) 中的堆缓冲区溢出。Chromium 向用户发送消息，要求立即更新，因为野外存在利用此漏洞的攻击。

因此，[Nix 人员](https://thenewstack.io/nixos-a-combination-linux-os-and-package-manager/)迅速修补了他们的 Chromium 版本，并且由于该漏洞实际上存在于 [libwebp](https://chromium.googlesource.com/webm/libwebp) 中，因此 Nix 版本的该库也得到了修补。

但是，然后维护人员开始想知道，该解码器在其他地方被使用了。Nix 是一个为 Nix-OS（一个 Linux 发行版）紧密运行的[包管理系统](https://search.nixos.org/packages)，允许用户下载超过 80,000 个软件包和实用程序。

当然，其他软件包（例如其他网络浏览器）肯定也必须在其自己的开源应用程序中捆绑 libwebp，这种包含被称为“供应商”。

事实证明有几十个，甚至更多。如果没有工具来对软件包进行分类，团队大约花了一个月的时间才追踪到他们估计的一半左右。至少有 10 位贡献者花费了“数百小时”来更新软件包。

最初，他们试图替换他们发现的该库的每个易受攻击的实例，但很快放弃了，认识到这项任务的艰巨性。虽然大多数高风险案例都已更新，但那些不太可能受到影响的软件包已被延迟，可能无限期延迟。

教训很明显：当漏洞发生时，软件包和存储库管理器不能再假设在他们修补有问题的软件的规范版本后问题就已解决。

如果 Nix 创始人发现了他们自己的库，那么很可能在所有地方都会发生这种情况。

## 是什么导致了供应商？

懒惰的程序员？他们不会声明依赖项并利用系统资源，而是会直接将库剪切并粘贴到他们自己的应用程序源目录中。偷偷摸摸地将开源库的副本放在你自己的应用程序库中。

公平地说，这样做有一些实际原因：最大的好处是您不必担心外部依赖项会破坏您的应用程序，因为它丢失了或以某种方式破坏您自己的应用程序的方式进行了更新。

毕竟，将其保留在内部将使事情永远有效。

直到发现漏洞为止。虽然在发现系统资源不安全时会立即对其进行修补，但埋在某些应用程序代码目录中的这些资源副本很可能不会更新，因此仍然可以被利用。

有多少聪明的程序员意识到，通过将外部库添加到自己的堆栈中，他们也承担了*维护*该资源的责任，就像他们对自己代码负责一样？

## 伟大分歧

至少在 Nix 社区中，供应商的情况“不太好”，Delroth 承认。这是一个不容易解决的问题。

在想知道重复库的问题有多严重时，Delroth 创建了一些工具来解决这个问题：自描述的[grep-nixos-cache](https://github.com/delroth/grep-nixos-cache) 和更[特定于语言的供应商漏洞扫描程序](https://github.com/delroth/nixpkgs-vendored-vulns-scan)。

事实证明，在 Nix 存储库中的各种 nixpkgs 中还有 116 个其他 libwebp 副本。而且它远非唯一被捆绑的图像解码器：他发现了 237 个 libpng 副本和 253 个 libjpeg 副本分散在各处。并且在 761 个不同的地方发现了通用 zlib 压缩库。

谁知道其中有多少（如果有的话）正在更新。一些版本的 libpng 可以追溯到 2004 年！

![](https://cdn.thenewstack.io/media/2024/03/4fbf31b4-fosdem-vendoring-01-1024x546.png)

继续！nix 构建它并从 2004 年获取一个二进制文件！它仍然有漏洞吗？你敢打赌！
## Rust 编程语言

[Rust 编程语言](https://thenewstack.io/rust-on-the-rise-new-advocacy-expected-to-advance-adoption/) 对这个问题有自己独特的看法，他指出，通过使用 [LockFiles](https://docs.rs/fslock/latest/fslock/struct.LockFile.html) 就能解决。使用 LockFiles 时，应用程序将需要特定版本的资源，该资源由数字哈希标识。因此，当程序调用外部系统资源时，它需要特定版本，该版本可能永远不会得到修补。

Delroth 强调了 Rust
*crates* 包 [带有 LockFile 依赖项](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html)。在确定的 1,844 个 Rust 包中，1,149 个（62%）具有锁定依赖项，这意味着在 Rust 语言中，它们无法更改。

“上游不理解这一点，或者不在乎，”Delroth 说。而其中 40% 的包（744 个）具有高或严重的漏洞。

当然，并非所有这些漏洞都是可利用的，这取决于它们的使用方式，但有些可能是可利用的。

## 如何处理供应商？

Delroth 承认 Nix 社区尚未制定任何形式的合规性或准则来阻止编程供应商。

仅被认为是使用外部系统库的良好做法，但没有法律规定你必须这样做。毕竟，它是
[开源](https://thenewstack.io/open-source/)。

甚至没有明确说明从源代码构建的首选项。用户可以转到
[AppImages](https://appimage.org/) 并下载已编译的二进制文件。Delroth 说：“人们在获取二进制文件方面非常有创造力”，并补充说
[Debian](https://www.debian.org/) 是保持二进制文件新颖的黄金标准。

（并且这是假设上游有人仍在维护包。Delroth 承认，许多人没有。）

Delroth 说，对于 Nix，最佳方法可能是用户教育。也许是一个新标签，比如
**knownVulnerable**，可用于标记甚至以编程方式引导用户远离过时的包，

## 供应商对其他开源意味着什么？

请记住，与之相比，Nix 人员运行的是一个非常严格的打包系统。因此，如果供应商在这里存在问题，你可以打赌其他开源存储库也会存在问题。其他 Linux 或 Docker 分发点，或
[JavaScript 框架丛林](https://thenewstack.io/jamstack-panel-multiple-javascript-frameworks-are-a-good-thing/)，甚至
[C/C++ 库的狂野西部前沿](https://thenewstack.io/bjarne-stroustrups-plan-for-bringing-safety-to-c/) 呢？

在
[Linux 基金会](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline-mention) 的 2022 年调查中，只有 18% 的开源贡献者表示他们确信其组织依赖的间接（传递）依赖项没有恶意或受到损害（传递依赖项是你用作依赖项的包的依赖项）。

即使有现有的开源安全策略，这一数字也只上升到 27%。

“我认为人们担心，如果他们报告使用依赖项，那么这将减慢他们的开发速度并让他们看起来很糟糕，”TNS 分析师
[Lawrence Hecht](https://thenewstack.io/author/lawrence-hecht/) 在 Slack 对话中指出。

他们也必须应对官僚主义。
[Tidelift 调查](https://blog.tidelift.com/finding-4-getting-approval-to-use-new-open-source-components-in-large-organizations-is-often-slow-and-tedious) 发现，在拥有 10,000 名以上员工的企业中，56% 的开源开发人员表示获得使用开源组件的批准需要一周以上的时间。

## SBOM 能解决供应商问题吗？

这是一个可以通过
[软件物料清单](https://thenewstack.io/sboms-sboms-everywhere/)（[SBOM](https://thenewstack.io/a-good-sbom-is-hard-to-find/)）解决的用户级问题吗？该清单列出了所有可以使用的单一源组件？

安全平台公司 [Kusari](https://www.kusari.dev/about) 的联合创始人兼 [GUAC SBOM 可视化工具](https://thenewstack.io/kubecon-24-guac-reveals-where-the-vulnerabilities-hide/) 的创建者之一
[Michael Lieberman](https://www.linkedin.com/in/michael-lieberman-65786ba/) 在一封电子邮件中指出：“这在很大程度上取决于代码或软件的供应商方式，以及用于生成 SBOM 的 SBOM 工具是否可以处理这种情况。”

例如，Go 编程语言“以相当直接的方式处理供应商”，他说。“只要你不修改供应商代码，SBOM 工具就应该能够处理拾取它。”

然而，并非所有情况都像这样简单。“人们有时会通过将源代码直接下载到另一个项目中来手动供应商代码。一旦你修改了供应商项目的一行代码，你现在就分叉并修改了该软件，将其变成了其他东西。”
**在这些情况下，您面临 SBOM 工具无法识别代码的风险。您破坏了它，您购买了它。**

“供应商”一词似乎是从商业软件领域借用的，在该领域，商业供应商会出于自身目的控制某个库。在开源世界中，“每个开源分发点”都是一个供应商，[Synopsys Software Integrity Group](https://www.synopsys.com/software-integrity.html) 的软件供应链风险策略主管 [Tim Mackey](https://www.linkedin.com/in/mackeytim/) 在一封电子邮件中指出。

以几乎普遍使用的 [OpenSSL](https://thenewstack.io/update-now-openssl-1-1-1s-shelf-life-has-ended/) 库为例。官方来源是 [GitHub 存储库](https://github.com/openssl/openssl)，但大多数用户从 Linux 发行版（如 [Red Hat](https://www.openshift.com/try?utm_content=inline-mention) 或 Debian）中获取它。这两个发行版中的代码可能完全相同，但它们是针对不同的目标编译的（因此得名“供应商”）。现实情况是，OpenSSL 在野外可能存在数千个不同的分支或中间源代码副本。

“整个生态系统使得补丁管理变得非常困难，”Mackey 写道。“针对 OpenSSL 一个分支设计的补丁可能无法在另一个分支上正常工作，因为我对我代码的独立分支进行了更改。”

一个好的 SBOM 会查看软件包的 pUrl（[持久统一资源定位符](https://datatracker.ietf.org/doc/html/rfc3986#section-1.2.3)），它标识软件包的省份。

“如果该 pUrl 指向应用程序使用的 OpenSSL 版本的正确 GitHub 存储库，那么我们就能识别谁负责任何补丁。同样，如果 OpenSSL 版本源自 Debian 等发行版，那么 Debian 就是任何补丁的责任方，”Mackey 指出。

观察者指出，供应商也可能使 SBOM 的情况变得更糟。

然而，SBOM 并不了解在生成的二进制文件中运送的代码。为了解决此问题，可以使用 [VEX](https://www.vexforum.com/t/design-build-workflows/33854) 来映射应用程序的组装工作流。

“SBOM 应记录组件及其版本，但由组件供应商确定其代码中是否存在漏洞，以及是否可以利用或在没有补丁的情况下缓解该漏洞，”Mackey 写道。“这就是 VEX 工作流是解决供应商问题的重要组成部分的原因。”

其他人不确定供应商是否是一个大问题。

“供应商可能会混淆许多 SBOM 生成工具，从而导致 SBOM 不完整。但聪明的工程师也可能只是教这些工具如何识别供应商，”[Chainguard](https://www.chainguard.dev/?utm_content=inline-mention) 的首席研究科学家 [John Speed Meyers](https://www.linkedin.com/in/john-speed-meyers-66b6a740/) 在一封电子邮件中写道。

Meyers 指出，SBOM 还存在许多其他潜在更严重的威胁，例如“混乱、低质量的漏洞数据或根本不会影响相关软件的漏洞”。

“软件通常就像邻家猫一样：它对被追踪不感兴趣，想做什么就做什么，”Meyers 总结道。“对于那些想知道其软件内部情况的人来说，这可能很难，真的很难。”

可以在这里查看 Delroth 的整个演示文稿：

*TNS 分析师 Lawrence Hecht 为此帖子做出了贡献。*

*编辑注，2024 年 3 月 8 日：此帖子已更新，增加了进一步的行业评论。*

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。