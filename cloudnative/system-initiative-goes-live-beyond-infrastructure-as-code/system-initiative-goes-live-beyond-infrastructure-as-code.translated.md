# 超越基础设施即代码：系统倡议正式启动

![Featued image for: Beyond Infrastructure as Code: System Initiative Goes Live](https://cdn.thenewstack.io/media/2024/09/f700e053-system_initiative-1024x683.png)

正如许多[认识他的人](https://x.com/adamhjk)所知，基础设施管理工程师[Adam Jacob](https://www.linkedin.com/in/adamjacob/) [并不喜欢](https://thenewstack.io/adam-jacob-rebuilding-devops-with-system-initiative/)当前的[DevOps 实践](https://thenewstack.io/DevOps/)。

好吧，今天是雅各布的“放手一搏”的日子。

因为今天是他的公司[System Initiative](https://www.systeminit.com/) 推出新自动化平台的日子，该平台可以创建组织 IT 基础设施的详细模型，然后用于管理这些系统。这是一种对基础设施管理方式的彻底反思，旨在避免雅各布所说的 DevOps 中所有令人分心的“微不足道的麻烦”。

通过基于图形网格的工作区，管理员可以使用[小型、反应式函数](https://thenewstack.io/system-initiative-could-be-lego-for-deployment/)将系统拼凑在一起，从而允许将系统管理为“活架构”。该软件会检查每个新添加的容器化组件的要求，并在配置或策略执行方面出现任何问题时提醒用户。然后，它会自动执行将不同系统元素连接在一起的大部分例行工作，并提供工具来快速添加任何缺失的细节。

据该公司称，所有通常在 DevOps 过程中后期出现的问题都可以由该软件立即标记。

“这是一项革命性的技术，我们认为它是 DevOps 自动化的未来，”雅各布告诉 TNS。

## DevOps 和 IaC 的问题

理论上，DevOps 实践通常使用[基础设施即代码](https://thenewstack.io/infrastructure-as-code/) (IaC) 使用代码以自动化方式在系统中部署资源，从而允许系统在一天内多次更新，如果可能的话。一种常见的做法是将配置代码存储在[GitHub](https://thenewstack.io/how-to-use-github-actions-and-apis-to-surface-important-data/) 中，并通过[Terraform](https://thenewstack.io/is-terraform-dead-revive-your-infrastructure-as-code-strategy/) 将工件推送到生产环境。

在[实践中](https://www.amazon.com/stores/author/B0CCGVSJRK)，正如雅各布[指出的那样](https://thenewstack.io/adam-jacob-rebuilding-devops-with-system-initiative/)，这导致了基于静态定义的笨拙、难以更新和难以理解的系统。这些工具与版本控制紧密绑定，使其变得脆弱且难以使用。只有像[谷歌](https://thenewstack.io/despite-the-hype-engineers-not-impressed-with-dora-metrics/) 这样的精英公司才能使用这种方法每天部署多次，正如雅各布（以及其他人）[所争论的那样](https://matthewsanabria.dev/posts/take-the-system-initiative/)。

“这不是一个单一的技术问题，而是我们被要求使用的形状、基础、原语，在绝大多数情况下会导致这些[负面]结果，”雅各布说。

将基础设施作为代码进行管理可能看起来是个好主意，但它会导致“各种下游问题”，他说。

## 系统倡议有何不同

系统倡议的方法不同，因为它将所有工件呈现为数据并一起绘制图表，因此它们之间的关系可以按需重新计算。这提供了服务的“数字孪生”功能，允许用户测试新配置和扩展以查看它们是否真的有效。

图形界面提供了整个基础设施的概述，显示了所有组件之间的关系。可以在系统上线之前对系统更改进行建模和测试。

这使团队能够测试更改并验证配置。该服务允许多个用户测试更改。

服务被呈现为函数。在可视化之下，所有实体和关系都以[TypeScript](https://thenewstack.io/TypeScript/) 形式捕获。

“假设您有一个 Docker 容器，您想在负载均衡服务中的某个地方使用它，”雅各布解释道。“在这种情况下，有一个函数接收该 Docker 容器信息作为输入，其输出是负载均衡器，它知道如何按需配置正确的东西，即负载均衡器。因此，我们更改了运行的端口容器，它会自动更改负载均衡器的池，”他说。

该平台作为托管服务提供，采用基于用量的定价（包括免费层）。它运行的软件是开源的。
Initially, System Initiative was built to manage infrastructure on [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) (AWS), but support for other cloud services will be available in the near future.

## About System Initiative
System Initiative ([Twitter](https://twitter.com/thesysteminit), [Discord](https://discord.com/invite/system-init)) launched in 2019 and has raised $18 million in venture capital from [Amplify Partners](https://www.amplifypartners.com/), [Scale Venture Partners](https://www.scalevp.com/), [Storm Ventures](https://www.stormventures.com/) and [Battery Ventures](https://www.battery.com/).

The service's open-source stack, called [si](https://github.com/systeminit/si), was open-sourced in [June 2023](https://thenewstack.io/system-initiative-a-devops-makeover-by-ex-chef-adam-jacob/) ([Apache 2.0](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/)) and has been downloaded 1,600 times. The project has had 29 contributors to date, and the commercial platform has been used by at least 120 early adopters. It is based on [NixOS](https://thenewstack.io/nixos-a-combination-linux-os-and-package-manager/), using [Docker](https://www.docker.com/?utm_content=inline+mention) and [Flakes](https://nixos.wiki/wiki/Flakes) Nix package manager. It has been forked 68 times and has received 690 stars.

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
Technology is moving fast, don't miss a beat. Subscribe to our YouTube channel to watch all our podcasts, interviews, demos, and more.