
<!--
title: 谁来拯救开源？维护者生存现状堪忧
cover: https://regmedia.co.uk/2020/03/04/highpressure.jpg
-->

工作过度、压力过大，还遭受虐待——这一切真的值得吗？

> 译自 [Open source maintainers are feeling the squeeze](https://www.theregister.com/2025/02/16/open_source_maintainers_state_of_open/)，作者 Richard Speed。

State Of Open 近期发生的一些事件将开源维护者的困境推到了风口浪尖，但这些问题已经酝酿多年。

在 2025 年的 State Of Open 大会上，这个主题被反复提及，来自科技巨头的演讲者和志愿者维护者都阐述了这些挑战。 大部分开源生态系统依赖于志愿者投入过多的时间，但获得的支持却太少，裂痕正在扩大。

每月四个小时……根本无法满足用户的需求以及那些认为“这有多难？”的人。 维护者无疑承受着巨大的压力，许多人已经退出或正在考虑退出……

本周，Asahi Linux 项目（一个用于 Apple Silicon 的 Linux 发行版）的负责人 Hector Martin，[突然辞职](https://www.theregister.com/2025/02/13/ashai_linux_head_quits/)，理由包括开发者倦怠和用户要求过高等因素。

Jamie Tanna，给自己起了个“疲惫的维护者”的头衔，[简单地说](https://youtu.be/PK8CMcePn2A)：“成为一名开源维护者真的很有回报……除非不是。”

Tanna 在开源领域活跃了几年，尽管他谈论的是作为 `oapi-codgen` 维护者的经历。 对于不熟悉的人来说，[oapi-codgen](https://github.com/oapi-codegen/oapi-codegen) 是一个将 OpenAPI 规范转换为 Go 代码的工具。

“很多公司都在使用它……还有很多愤怒的用户。”

这是一个熟悉的故事。 Tanna 帮助解决了项目中的一些问题，并自愿承担了维护者的职责。 曾经有一段时间发布很频繁，但不久之后，每次发布之间的时间开始变长。 他解释说，作为一名维护者，无论是大型项目还是小型项目（尤其是大型项目），都意味着要与那些非常乐于表达自己感受的“有趣”用户，以及不断增加的请求清单打交道。

在感到压力、孤立无援，面对越来越多的工作，同时收到来自有优越感的用户的偶尔发来的令人不快的消息，他们要求 *立即* 处理他们的问题，或者 *立即* 合并贡献，这种经历太常见了。

Tanna 相对幸运——他的雇主每月给他四个小时来处理这个项目。 然而，这根本无法满足用户的需求以及那些认为“这有多难？”的人。 维护者无疑承受着巨大的压力，许多人已经退出或正在考虑退出。

许多项目，即使是那些被认为是“关键基础设施”的项目，也只有极少数人支持（通常是一个人完成大部分工作）……

谷歌开源项目和运营分析师兼研究员 Sophia Vargas 告诉 *The Register*，“绝对”维护者承受着压力。 Vargas 补充说，这种压力“既是系统性的，也是在个人社区层面上的。

“开源领域的许多参与者认为，开源项目长期以来都得不到足够的支持，尤其是在人们对使用开源软件的需求日益增长的情况下。

“这种感觉也反映在数字中：许多项目，即使是那些被认为是‘关键基础设施’的项目，也只有极少数人支持（通常是一个人完成大部分工作），许多维护者已经考虑过退出，而且许多项目可能根本无人维护。”

Vargas 使用了一些数据，包括 [2024 年 Tidelift 调查](https://explore.tidelift.com/2024-tidelift-survey/2024-tidelift-state-of-the-open-source-maintainer-report)，该调查显示，有 60% 的维护者已经退出或正在考虑退出，以及 Linux 基金会的 [另一份](https://www.linuxfoundation.org/hubfs/Research%20Reports/lfr_harvard_censusII_mar2022_042824b.pdf) [PDF] 文件，该文件显示，大多数广泛使用的自由开源软件仅由少数贡献者开发。

Kubernetes 维护者 Kat Cosgrove 和 Jeremy Rickard 也参与了讨论。 Rickard 是微软的员工，也参与 CNCF 的行为准则工作。 这两人进行了一项调查，收集维护者和项目贡献者的经验。

Cosgrove 指出，受访者人数太少，不具有统计意义，但问题不仅仅是维护者承受压力和辱骂。 这些问题也延伸到了旁观者用户。“他们不太喜欢这个项目，百分之七十的人考虑过是否应该为该项目做出贡献。”

解决这个问题很困难。 维护者是否只需要获得报酬来认可他们的努力？ Vargas 不确定所有问题都有经济上的解决方案，并指出了今年 FOSDEM 上提出的研究 (https://dl.acm.org/doi/10.1145/3674805.3686667)。 Vargas 告诉 *The Register*，“金钱无法解决所有问题。”

每个维护者和项目都有他们自己的背景和挑战 - 尽管许多维护者会受益于经济上的支持，但其他人实际上可以使用更多的贡献者来补充他们的工作，并减轻他们的责任 - 尤其是在非代码任务方面，如指导、社区管理、问题分类、推广和筹款等。

*   [为什么年轻的程序员难以突破 FOSS 老手障碍？](https://www.theregister.com/2025/02/14/youngsters_in_foss/)
*   [在 Linux 中 Rust 发生冲突后，Asahi 负责人退出发行版，抨击 Linus 的内核领导](https://www.theregister.com/2025/02/13/ashai_linux_head_quits/)
*   [LibreOffice 仍然活跃了 40 年，现在有了浏览器技巧和实时协作](https://www.theregister.com/2025/02/13/libreoffice_wasm_zetaoffice/)
*   [Murena 老板说客户即将从云存储噩梦中醒来](https://www.theregister.com/2025/02/12/murena_ceo_de_googling_android/)

Rickard 还担心经济不确定性会给预算带来潜在的压力，并谈到在 GitHub 等平台上提高对赞助的认识，因为公司对项目的资助正在减少。

“你必须有一些东西作为变革的催化剂。我们作为一个人类群体，似乎不太擅长积极主动。”

Cosgrove 说：“我担心需要一个重要的项目失败才能说服他们[用户]为开源维护者付费是值得的，而且实际上可能是一个要求。”

“我不希望看到这种情况发生，因为后果将是丑陋和令人厌恶的，但我担心这就是它所需要的。” 
39