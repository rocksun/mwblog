<!--
title: Sudo-rs：为Ubuntu 26.04注入现代内存安全
cover: https://cdn.thenewstack.io/media/2024/07/7bf564a8-jigar-panchal-rmxbyhgbxru-unsplash-sudo.jpg
summary: Ubuntu 26.04将引入Rust版sudo-rs，与C版sudo并存。它提升安全性、可维护性，代码更精简。已在Ubuntu 25.10中，并获原sudo维护者支持，目标是日常sudo的替代。
-->

Ubuntu 26.04将引入Rust版sudo-rs，与C版sudo并存。它提升安全性、可维护性，代码更精简。已在Ubuntu 25.10中，并获原sudo维护者支持，目标是日常sudo的替代。

> 译自：[Why Sudo-rs Brings Modern Memory Safety to Ubuntu 26.04](https://thenewstack.io/why-sudo-rs-brings-modern-memory-safety-to-ubuntu-26-04/)
> 
> 作者：Steven J. Vaughan-Nichols

伦敦 — 首先，冷静一下。是的，[Ubuntu](https://ubuntu.com/)的下一个长期支持版本Ubuntu 26.04将包含[sudo-rs](https://github.com/trifectatechfoundation/sudo-rs)，这是一个用内存安全的Rust编写的[sudo](https://www.sudo.ws/)版本。不，它不会取代老旧的基于C的sudo。两者都将存在。深呼吸。放松。

不，说真的。它已经出现在Ubuntu 25.10中。对我来说一直运行良好。如果你不信任它，你可以使用以下命令控制使用哪个版本：

```
update-alternatives --config sudo
```

正如sudo-rs项目的首席工程师Marc Schoolderman在[Ubuntu Summit 25.10](https://www.reuters.com/business/autos-transportation/us-agency-asking-tesla-about-mad-max-driver-assistance-mode-2025-10-24/)上的一次演讲中所解释的那样，用Rust重写关键的[sudo命令](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/)不仅仅是为了“为了Rust而移植”。这是一项深思熟虑的重新设计，旨在解决Linux权限边界核心深层的安全性、可维护性和灵活性问题。

当有人给他发消息问：“‘你愿意将一份有巨大影响力的工作，用一种漂亮、现代的编程语言来完成，作为你日常工作的一部分吗？’为什么不呢？这是我诚实的回答。”他明确表示，这次重写是“重新思考需求的好时机”，不仅能带来更大的技术自由，还能促进更深入的社区贡献。Sudo-rs减小的代码量和富有表现力的Rust语义，使得外部贡献者更容易提出改进建议。

他与他的同事开发者正与[Todd Miller](https://www.linkedin.com/in/millert/)密切合作。Todd是谁？你知道那个sudo的唯一维护者，目前正在寻找赞助商来资助sudo持续维护的人。你知道那个[xkcd漫画](https://xkcd.com/2347/)吗，现代数字基础设施依赖于内布拉斯加州的一位开发者？那个人就是Miller，只不过他住在科罗拉多州。我们需要一个现代的、更内存安全的sudo版本，那就是sudo-rs，而Miller也需要我们的支持。

## 用Rust重写Sudo的动机

话虽如此，Schoolderman解释说，sudo-rs于2023年通过[互联网安全研究小组](https://www.abetterinternet.org/)启动，作为其[Prossimo](https://www.memorysafety.org/)倡议的一部分，旨在用安全语言重写关键的开源工具。特别是，他们瞄准了位于安全边界上但尚未用现代内存安全语言实现的普遍存在的工具。

尽管改进内存安全性——[Rust的标志性优点](https://thenewstack.io/rust-programming-language-guide/)——是核心，因为sudo高达30%的严重漏洞历来都源于内存问题，Schoolderman强调，Rust富有表现力的类型系统以及它提供的重构便利性，对于可维护性和审计同样具有变革性意义。

sudo-rs团队没有盲目复制每一个遗留功能，而是借此机会重新思考需求并精简功能，从而优化了现代系统中的安全性和相关性。

## 了解Ubuntu中的Sudo-rs

这意味着sudo-rs的目标是作为sudo所有日常用例的即插即用替代品。对于sudo配置语法，这意味着它支持常见Linux发行版和FreeBSD的默认配置文件。“我们的实现应该支持原始sudo实现中所有常用的命令行选项。”

但是，重要的是，原始sudo的某些部分明确不在范围内。Sudo有着悠久而丰富的历史，原始sudo实现中的某些功能大多未被使用或仅适用于旧平台。

因此，它没有克隆所有遗留sudo的方面，并非所有“古怪”的功能或不常用的能力都被包含在内。是的，这意味着你“必不可少”的sudo功能可能不会被包含。但你真的需要它吗？检查一下就知道了。而且，如果你真的、真的需要它，请告诉开发者，也许他们会包含它。此外，请记住，sudo不会消失。你仍然可以使用它。

除了使sudo-rs更安全之外，重构的另一个原因是：“sudo中存在大量的业务逻辑，如果你使用Rust，你将拥有一种具有非常富有表现力的类型系统的现代语言，并且以可维护和可读的方式表达逻辑要容易得多。”

此外，Schoolderman表示：“我们团队使用Rust开发sudo-rs的最大好处不一定是内存安全问题——尽管这很好，而且是免费获得的。最大的好处是拥有一个更小的代码库，外部用户更容易深入了解。”

他继续说道：“我们给sudo‘减肥’了，实际上我们把它减少到，我想，三个直接依赖项，而且它们都由Rust项目维护。所以我认为sudo是一个非常精简的项目，我们希望保持这种状态。”

## 与原始Sudo维护者的协作

Schoolderman接着说，sudo-rs汲取了数十年来sudo开发的经验，并积极与Miller协作。他既为Schoolderman的团队提供了建议，也为sudo-rs的错误修复做出了贡献。这促成了项目间的直接相互影响：sudo-rs的全面测试甚至发现了原始sudo中的漏洞，Miller迅速进行了修补。

sudo-rs和sudo并非竞争对手，而是互补的，它们的开发者正在互相帮助，让两者都变得更好。

2025年，[Canonical决定将sudo-rs作为Ubuntu 25.10的默认sudo实现](https://thenewstack.io/ubuntu-25-10-replaces-sudo-with-a-rust-based-equivalent/)。这包括Ubuntu兼容性的资金里程碑，例如NOEXEC shell逃逸预防和AppArmor控制。通过在关键方面（遗留脚本和工作流）实现向后兼容性，Canonical确保了平稳过渡，并严格测试sudo-rs在即将于2026年发布的Ubuntu LTS版本中的性能和可靠性。Canonical的领导层希望激励其他主要发行版加入他们。

[Trifecta Tech Foundation](https://trifectatech.org/)现在负责项目的治理和资金。这确保了一个维护良好且多样化的团队，超越了单维护者风险的“巴士系数”。

希望过渡到sudo-rs将带来更少的安全补丁、减少因漏洞造成的停机时间，以及一个现代化、精简的代码库，方便新手和维护者进行审计和扩展。

## Sudo-rs的“少即是多”设计理念

因此，sudo-rs秉承“少即是多”的理念，省略了冗余，专注于健壮的必需品。系统管理员和安全工程师应该会喜欢这一改变。

它会奏效吗？敬请关注，或者从Ubuntu 25.10或今天支持它作为选项的许多其他发行版（如Arch、Fedora、Debian或NixOS）开始实验。