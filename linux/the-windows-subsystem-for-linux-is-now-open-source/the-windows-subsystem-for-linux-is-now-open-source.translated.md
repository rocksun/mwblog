# Windows Linux 子系统现已开源

![Windows Linux 子系统现已开源的特色图片](https://cdn.thenewstack.io/media/2025/05/1e9dffe9-img_20160925_175258-1024x576.jpg)

在年度 Build 开发者大会上，微软宣布将 Windows Linux 子系统 (WSL) 开源，该子系统允许开发者在 Windows 内部轻松运行 Linux 发行版。

“我们希望 Windows 成为一个出色的开发环境，”负责 Windows 和设备的微软公司副总裁 [Pavan Davuluri](https://www.linkedin.com/in/pavand/) 告诉我。“归根结底，一个好的开发环境意味着很多不同的东西。其中之一就是拥有出色的 WSL 性能和功能，使其成为我们开发者在一个 Windows 原生体验中生活的一站式商店，并能够利用他们在 Linux 中所需的一切。”

开发者现在可以下载代码，从源代码构建 WSL，并贡献功能和修复错误。

WSL 的第一个版本于 2016 年发布。当时，Windows 实际上模拟了一个 Linux 内核（使用 lxcore.sys 和 lxss.sys），但随着 2019 年 WSL 2 的发布，该团队切换到 Linux 内核本身，以提供更好的兼容性。从那时起，WSL 增加了对 GPU、图形应用程序和 systemd 的支持。

![Windows Linux 子系统架构图](https://cdn.thenewstack.io/media/2025/05/c9bc2541-screenshot-2025-05-16-at-12.58.03%E2%80%AFpm.png)

WSL 架构。来源：微软。

Davuluri 指出，该团队收到了很多开发者关于开源 WSL 的请求，但在项目早期，该团队的重点完全放在发布项目并了解开发者将如何使用它。随着 WSL 2 的发布，重点放在性能和添加新功能上。现在，在对 Windows 的一些核心组件进行重大重构，以便 WSL 可以成为一个独立的系统之后，[微软觉得已经准备好开源](https://thenewstack.io/microsoft-open-sources-openhcl-a-linux-based-paravisor/)该项目。

“我的直觉是，Windows 的 Linux 服务，或者 Linux 的 Windows 服务，是我们将会看到大量工作的地方，我认为这会减少 [开发者原生 Windows 体验](https://thenewstack.io/how-the-developer-experience-is-changing-with-cloud-native/) 与他们在 Linux 端进行设置和执行之间的摩擦，” Davuluri 在我问他期望开发者从哪里开始为该项目做出贡献时说。“这是我们看到人们投入最多精力来积极执行或解决对人们日常工作至关重要的事情的第一个地方。”

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，即可观看我们所有的播客、访谈、演示等。