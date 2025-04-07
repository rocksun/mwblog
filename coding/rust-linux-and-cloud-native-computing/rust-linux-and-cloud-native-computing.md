
<!--
title: Rust、Linux和云原生计算
cover: https://cdn.thenewstack.io/media/2025/04/6d6504ec-rust-programming-image-1.jpg
summary: Linux内核拥抱Rust！每年76000个变更，用Rust编写GPU驱动等新程序，减少CVE漏洞，提升云原生计算安全性。即使Linus Torvalds合并Rust也失败了！倒逼C代码审查，让编译器提前工作，保障未来30年安全。
-->

Linux内核拥抱Rust！每年76000个变更，用Rust编写GPU驱动等新程序，减少CVE漏洞，提升云原生计算安全性。即使Linus Torvalds合并Rust也失败了！倒逼C代码审查，让编译器提前工作，保障未来30年安全。

> 译自：[Rust, Linux and Cloud Native Computing](https://thenewstack.io/rust-linux-and-cloud-native-computing/)
> 
> 作者：Steven J Vaughan-Nichols

伦敦 — Linux 稳定版本维护者 [Greg Kroah-Hartman](https://thenewstack.io/greg-kroah-hartman-lessons-for-developers-from-20-years-of-linux-kernel-work/) 在 [KubeCon + CloudNativeCon Europe](https://thenewstack.io/kubecon-cloudnativecon-eu-2025/) 的主题演讲中表示，Linux 每年接受 76,000 个变更，拥有 380 名维护者和 700 名开发人员，正在缓慢但肯定地在 Linux 内核中拥抱 Rust。

为什么 C 编程的代表要采用相对较新的 Rust 呢？很简单：Rust 更安全。Kroah-Hartman 举了一个蓝牙安全漏洞的例子，该漏洞几年前已修复，但是，哎呀，在最初几年看起来没问题之后，事实证明该修复引入了一个新漏洞。对于 C 来说，这太常见了。很难编写内存安全的 C 代码。

Kroah-Hartman 解释说，当“我们用 Rust 编写代码时”，“不仅可以捕获错误，编译器还会为您捕获错误，这非常非常重要。我们希望编译器在维护者再次查看这些内容之前就注意到该错误。”

## 更少的 CVE

由于 Rust 的编译器可以强制执行在编译时防止许多此类问题的规则，因此减少了内核中[常见漏洞和暴露](https://thenewstack.io/how-linux-kernel-deals-with-tracking-cve-security-issues/) (CVE) 的数量。

反过来，这对于云原生计算非常重要，实际上对于在 Linux 上运行的所有内容（例如服务器和洗衣机）也很重要，因为当今的 Linux 漏洞几乎总是安全漏洞，因为 Linux 在如此低的级别上工作。

目前，Linux 内核包含大约 3400 万行 C 代码，只有 2.5 万行是用 Rust 编写的。但是，[新的程序（例如 GPU 驱动程序）正在用 Rust 编写](https://thenewstack.io/rust-integration-in-linux-kernel-faces-challenges-but-shows-progress/)。预计这种转变将使代码更易于理解和审查，从而随着时间的推移提高稳定性。

这很棒，但是将 Rust 合并到 [Linux 内核](https://thenewstack.io/linux-kernel-6-14-enhanced-drivers-security-performance-improvements/) 中并不容易。即使 Linux 的创建者 Linus Torvalds 在准备下一个 Linux 内核版本时也表示，将 Rust 合并到 Linux 中并不容易。“[我决定尝试自己进行合并，但失败了。](https://lore.kernel.org/lkml/CAHk-=wjpDpK0cd=tBk2t005nrddL0hXRQ+h+iZPHfVsi6qQY+w@mail.gmail.com/) 我差点成功，但是很高兴看到您的示例合并，看看我哪里出错了。我最终会学会的，在此期间，请继续给我示例合并，我将它们用作训练轮。”

## 先为人编写代码，然后为编译器编写代码

正如 Kroah-Hartman 指出的那样，“改变内核开发人员的想法很难。” 例如，著名的软件工程师和 Linux 内核维护者 Christoph Hellwig 是一位 C 专家，但他可以理解地不乐意也需要学习 Rust。

您可能没有想到的另一个原因是 - 我认为每个人都可以理解不想学习一门新的编程语言 - 以及为什么“我们对此 [迁移到 Rust] 感到不满，是因为它迫使我们审查我们的 C 代码，并且我们的代码在过去 30 年中以我们有时不理解的方式发展。”

因此，他继续说，“有时我们需要回头看看它，并强制执行 Rust 允许我们强制执行的规则，以强制执行我们以前不知道的内核中 C API 的规则。因此，它使我们重新审查旧代码，这很难。老维护人员不想做新事情。他们有时不想看他们的旧东西，但是改变可能是好的。”

这是因为这将使维护代码更容易。同样，我们首先为人编写代码，然后为编译器编写代码。这将使我们能够持续未来 30 到 40 年，让编译器为我们完成工作，并且我认为这让我们维护人员更加有趣，因为，同样，编译器可以提前工作。”

通过使维护人员和开发人员更容易，它还将“使 Linux 对您来说更安全。您可以去解决您的云原生计算问题，这对您来说非常重要。