世界上最古老、[最具影响力的Linux发行版](https://thenewstack.io/choosing-a-linux-distribution/)之一 [Debian](https://www.debian.org/) 已正式宣布计划重组其开发策略，将 [Rust](https://thenewstack.io/rust-programming-language-guide/) 作为系统级工具和未来软件包的核心语言。

Debian资深开发者、[高级软件包工具 (APT)](https://wiki.debian.org/Apt) 的主要维护者 [Julian Andres Klode](https://www.debian.org/vote/2025/platforms/jak) 在Debian开发者邮件列表中宣布，今后，[Rust将成为Debian核心APT软件包管理器的强制性依赖项](https://lists.debian.org/deity/2025/10/msg00071.html)。

具体来说，Klode 写道，他计划“不早于2026年5月，将硬性Rust依赖和Rust代码引入APT。这首先将扩展到Rust编译器、标准库以及Sequoia生态系统。”

Sequoia是一个Debian项目，致力于创建[OpenPGP的Rust实现](https://wiki.debian.org/OpenPGP/Sequoia#:~:text=Sequoia%20PGP%20is%20a%20project,these%20IRC%20channels%20on%20OFTC:)。

为什么？Klode 解释说：“我们用于解析 .deb、.ar、.tar 的代码以及HTTP签名验证代码将极大地受益于内存安全语言和更强大的单元测试方法。”

## 对Ubuntu、Mint及其他基于Debian发行版的影响

APT是Debian的核心组成部分。几乎所有基于Debian的Linux发行版，例如 [Ubuntu](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/)、Mint和MX Linux，都[依赖APT](https://thenewstack.io/debian-retools-apt-for-superior-dependency-management/)进行包管理。这意味着Rust代码将进入所有这些发行版。这对一些发行版架构师来说完全没问题。例如，Canonical 已经[将Rust整合到Ubuntu sudo中](https://thenewstack.io/why-sudo-rs-brings-modern-memory-safety-to-ubuntu-26-04/)。

这些举措的理由是提高操作系统的安全性和稳定性。Rust的[内存安全架构](https://thenewstack.io/moving-from-c-to-rust-clickhouse-has-some-advice/)能够阻止C和C++代码库几十年来一直存在的常见错误，如缓冲区溢出、空指针解引用和竞态条件。

## 基本原理：增强安全性和稳定性

如果你不喜欢？那也没办法。Klonde 补充说：“如果你维护一个没有可用Rust工具链的移植版本，请确保在未来六个月内为其配备一个，否则该移植版本将停止维护。”

哎哟。

一些开发者并不高兴。[John Paul Adrian Glaubitz](https://github.com/glaubitz) 对[APT公告采取了“如此对抗性的方法”](https://lwn.net/ml/all/ad6e60711c8ed3372ed7f324d7b1be23b0722a0d.camel@physik.fu-berlin.de/)感到失望。

与此同时，[Bjørn Mork](https://github.com/bmork) 怀疑将APT迁移到Rust是否真的会有那么大的帮助。“[重写代码意味着引入新错误](https://lwn.net/ml/all/87ldkqt09e.fsf@miraculix.mork.no/)，无论工具是否能捕获其中一些。但为了有趣，让我们假设我们最终在重写后的软件中能减少严重的错误。这需要多长时间？……我们是否应该暂时接受退步，因为Rust的重新实现最终会赶上我们今天所拥有的？”

## 开发者社区的反应与担忧

在Debian开发者邮件列表的后续对话中，Klonde 耸了耸肩。“[Rust已经是大多数Debian移植版本的硬性要求](https://lwn.net/ml/all/20251031223819.GA97356@debian.org/)，所以这并不令人惊讶。”

他还指出，目前只有四种较旧的架构——alpha、hppa、m68k和sh4——尚未与Rust保持同步。如果这些平台的开发者无法提供Rust支持，那么，正如 ebee\_matteo [在Linux Weekly News (LWN)上表示](https://lwn.net/Articles/1044507/)的那样：“这又是一个迹象，表明这些架构没有足够的开发者来保证持续努力确保跨平台兼容性。……这甚至不是Rust/非Rust的争论。这是一个‘这个移植版本到底有没有足够的开发者和用户？’”

展望未来，Debian的下一个主要版本，代号Forky的Debian 14，预计将于2026年中期发布。它将不仅在APT中，还可能在其他核心实用程序、构建基础设施和安全关键模块中实现更深层次的Rust集成。

至于那些不能或不愿采用Rust的Debian发行版，它们始终可以效仿基于Debian的Linux发行版 [antiX](https://antixlinux.com/) 的路径，该发行版继续基于旧的Debian版本（如Debian 12 “Bookworm”）构建，以支持32位硬件。

大多数开发者最终会和Klode一样拥抱Rust。说实话，它并不是一门难学的语言，而且它确实能让编写内存安全的代码变得容易。作为一个曾为C代码绞尽脑汁，试图（而且常常失败）让我的程序内存安全的人，我个人非常欢迎Linux及其发行版现在整合Rust的方式。