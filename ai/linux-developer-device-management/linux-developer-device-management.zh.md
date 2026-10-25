**Linux已经是AI开发者桌面工具包的一部分。** 2025年10月15日开始接受订购的 [Nvidia’s DGX Spark](https://nvidianews.nvidia.com/news/nvidia-dgx-spark-arrives-for-worlds-ai-developers/) 运行的是基于 [Ubuntu 的 DGX OS](https://docs.nvidia.com/dgx/dgx-spark/dgx-os.html)。OpenAI 的 [Codex CLI](https://learn.chatgpt.com/docs/codex/cli) 已经支持 Linux，这是AI工具在开发者工作的地方与他们相遇的又一个例子。

这里只有一个问题。开发者可以在家里爱上 Linux。但要让企业 IT 部门允许他们在工作中使用 Linux，则是另一回事。

[Angelo Huang](https://www.linkedin.com/in/angelokh) 是管理和保护员工设备的平台 [Swif.ai](http://swif.ai/) 的创始人兼 CEO，他希望改变这种状况。Huang 告诉 *The New Stack*，为开发者提供 Linux 机器，首先要赋予 IT 团队管理和保护这些机器的控制权。

Huang 表示，从上周开始，Swif 开始扩展其 Linux 设备管理和合规能力，将 [Omarchy](https://omarchy.us/) 和 [Linux Mint](https://linuxmint.com/) 加入其支持名单。Swif 还在优化的受支持的 Mac、Windows、Linux、iOS 和 Android 环境中的入职流程。他们声称，现在设置 SOC 2、ISO 27001 和 HIPAA 等设备合规标准只需不到 10 分钟。

Huang 说：“Linux 已经运行了AI背后的许多基础设施。越来越多的开发者也希望在他们的办公桌上使用它。问题不在于 Linux 不能做到安全。而是企业 IT 需要能够对其进行管理、强制执行控制措施，并证明这些控制措施在其合规要求下正在发挥作用。这就是我们正在弥合的差距。”

> “问题不在于 Linux 不能做到安全。而是企业 IT 需要能够对其进行管理、强制执行控制措施，并证明这些控制措施正在发挥作用……”

Swif 列出了对 [Linux 发行版](https://help.swif.ai/en/articles/9903836-enroll-linux-devices)的支持，包括 Debian、Ubuntu、Fedora、openSUSE、Arch Linux、Manjaro、MX Linux、Pop!_OS、Red Hat Enterprise Linux、NixOS 和 Universal Blue。

根据 Swif 的 [Omarchy 指南](https://help.swif.ai/en/articles/16777543-manage-omarchy-os-devices-with-swif-linux-mdm)，针对 x86_64 机器测试的配置（4.0.2 版本）支持设备注册、清单跟踪、应用程序阻止以及选定的 OpenClaw 日志记录和工具策略。（该指南指出了登录、主目录加密、远程桌面和更新方面的局限性。）

不过，Linux Mint 的状态没那么直接。

Huang 说：“Linux Mint 今天之所以能运行，是因为它是基于 Ubuntu 构建的，我们有客户在运行它，但它还不在我们官方支持的列表中。对新发行版的请求是通过支持工单和我们的客户成功团队收到的。拥有实际部署的客户、涉及的席位数量以及它与我们已经支持的发行版的偏离程度，会将一个发行版提升到优先级列表的前列。对于基于 Ubuntu 或 Fedora 的发行版，初始支持通常需要一到两周。”

Swif 的[软件管理指南](https://help.swif.ai/en/articles/15384672-installing-and-managing-software-on-windows-and-linux-with-swif)列出了用于基于 APT 的应用程序安装的 Mint，尽管其 Linux 注册列表未命名 Mint。该文档记录了特定的功能，而不是对每个管理策略的全面验证。

Mint 还提供基于 Debian 的版本 LMDE；共同的血缘并不能确保跨版本和版本的兼容性。

## 让企业 IT 能够管理 Linux

Swif 的 Linux 管理功能涵盖了熟悉的 IT 需求：策略强制执行、[LUKS 加密恢复](https://help.swif.ai/en/articles/16000356-linux-encryption-recovery-policy)和自动修复。支持因发行版和策略而异；恢复政策管理对已经加密的磁盘的访问，而不是加密未加密的磁盘。

Swif 每小时将 Linux 设备证据发送到治理、风险和合规 (GRC) 平台 [Vanta](https://help.swif.ai/en/articles/7940111-set-up-swif-integration-with-vanta)。

它还提供每小时同步一次的 Drata 集成。尽管如此，[Swif 的 Drata 指南](https://help.swif.ai/en/articles/7232168-set-up-swif-integration-with-drata)在 Linux 上的表现并不一致：它列出了 Linux 证据字段，但其设备资格列表仅命名了 macOS 和 Windows。Linux 团队在依赖它之前应该与 Swif 确认 Drata 覆盖范围。

这些记录支持合规性评估；它们本身并不能建立合规性。

*The New Stack* 询问开发者如何例如在 [Framework](https://frame.work/) 笔记本电脑上运行 [Wayland](https://wayland.freedesktop.org/)，以及这如何让 IT 确定哪些管理功能可以与该设置配合使用。

Huang 说：“我们的 Agent 在用户空间运行，主要依赖 systemd、包管理器和标准内核接口，因此像 Framework 笔记本电脑这样的硬件很少是问题。显示服务器才是事情变得有趣的地方。通过 PipeWire 和 xdg-desktop-portal 对 Wayland 的支持正在开发中。我们的经验法则：如果它影响我们的 Agent 是否可以强制执行策略、报告清单或证明合规性，那就是我们要修复的问题。”

用户空间并不意味着没有特权：Swif 的 Linux 管理命令可以[以 root 身份运行](https://help.swif.ai/en/articles/6860941-how-does-the-swif-agent-work)。PipeWire 和桌面门户处理屏幕共享等功能；这与基本的设备清单或策略强制执行不同。Swif 的 [Omarchy 指南](https://help.swif.ai/en/articles/16777543-manage-omarchy-os-devices-with-swif-linux-mdm)指出其基于 RustDesk 的远程桌面策略具有实验性的 Wayland 支持。

## 让开发者拥有 Linux

Huang 说：“公司内部的争论不需要在 Mac 与 Windows 与 Linux 之间进行。如果您的AI团队想要 Linux，IT 的回答不应该自动是‘不’。给开发者他们想要的工具来完成工作。给安全部门它需要的控制。”

> “如果您的AI团队想要 Linux，IT 的回答不应该自动是‘不’。”

Swif 专注于企业 IT，但开发者也关心 IT 如何管理他们的机器。*The New Stack* 询问它是否运营 Linux 开发社区。

“通常的故事是，几位工程师要求 IT 摆脱 Windows，它增长到 50、100，有时甚至是 200。然后 IT 需要一种方法来管理 GRC 平台将接受作为证据的机器，这就是他们来找我们的时候。我们还直接通过与客户的共享 Slack 频道、推出期间的入职电话以及最终用户提交的支持工单听到开发者的声音。我们今天不为 Linux 开发者运营社区，但这是一个好主意。”

## AI 监督：文档化功能与路线图

Huang 说：“目前，我们有 MCP 服务器管理、智能体安全、Claude 合规性集成和数据丢失防护处于 Beta 测试阶段。路线图上是与 OpenAI 的合规性 API 和智能体合规性的集成。”

注册 Linux 机器后，安装 Swif 的 MDM Agent 进行设备管理，同时安装[智能体安全 Agent](https://help.swif.ai/en/articles/15610184-getting-started-with-swif-s-agentic-security) 可以提供对受支持的AI智能体活动的可见性。

其[Claude 合规性集成](https://help.swif.ai/en/articles/17073552-integrating-anthropic-claude-compliance-with-swif-agentic-security)收集组织级别的审计事件，而其记录的 [DLP Beta](https://help.swif.ai/en/articles/16007631-data-loss-prevention-dlp) 使用浏览器扩展并需要组织级别的 Beta 选择加入。

其电子邮件文档涵盖网页版 Gmail 和 Outlook，不包括本地桌面邮件客户端。这些功能的范围与监控本地智能体活动不同。

“它将员工端点上AI智能体的监督带入了设备管理层。问题很简单。智能体在可以访问代码、凭据和客户数据的员工端点上运行，几乎没有人监督它们。

> “智能体在可以访问代码、凭据和客户数据的员工端点上运行，几乎没有人监督它们。”

“当 OpenClaw 首次推出时，许多客户要求我们直接阻止它。随着越来越多的人在工作中使用智能体，公司因数据泄露或知识产权盗窃而损失惨重，无法将其置于不受管理的状态，”Huang 说。

OpenClaw 自己的安全文档警告说，不受信任的内容可能会携带[提示词注入](https://docs.openclaw.ai/gateway/security/prompt-injection)。风险取决于智能体的权限、工具和隔离。