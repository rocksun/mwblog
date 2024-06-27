
<!--
title: 微软押注AI吸引开发者使用ARM架构的Windows
cover: https://cdn.thenewstack.io/media/2024/06/b17172cf-joel-overbeck-amkdlzfdmia-unsplash-1.jpg
-->

随着微软及其合作伙伴推出 AI 驱动的 Copilot+ PC，开发者必须权衡在 Windows on Arm 上进行开发的潜力。

> 译自 [Microsoft Bets on AI to Lure Devs to Windows on Arm](https://thenewstack.io/microsoft-bets-on-ai-to-lure-devs-to-windows-on-arm/)，作者 Darryl K Taft。

微软的 AI 驱动的 [Copilot+ PC](https://thenewstack.io/copilot-pcs-understanding-microsofts-evolving-ai-pc-stack/) 平台支持基于 Windows 的 [Arm 设备](https://thenewstack.io/arm-pushes-ai-into-the-smallest-iot-devices-with-cortex-m52-chip/)，它会成为吸引开发者使用基于 ARM 的 Windows 的 “[杀手级应用](https://thenewstack.io/tomorrows-5g-killer-apps-will-need-a-strong-foundation-in-ci-cd/)” 吗？

也许吧。虽然有些人认为这可能只是一个花招或吸引更多开发者关注微软的闪光点。事实上，微软及其 PC 合作伙伴一直在努力吸引开发者——以及一般客户——使用 [基于 ARM 的 Windows 超过十年](https://www.directionsonmicrosoft.com/blog/will-windows-on-arm-pcs-finally-be-worth-buying/)。

也许更好的看待这种情况的方式是 [“梦幻之地](https://en.wikipedia.org/wiki/Field_of_Dreams)” 主题的变体。如果微软建造它，他们会来吗？好吧，微软建造了它。现在，开发者会来吗？

“这是一个棘手的陷阱……如果你没有很多客户要求，你就无法将所有应用程序转换为 ARM，而如果你没有机器运行他们需要的应用程序，你就无法获得客户，”长期微软 MVP [Richard Campbell](https://www.linkedin.com/in/richjcampbell/?originalSubdomain=ca) 告诉 The New Stack。

“我认为 Copilot 的策略是一种变通方法，”Campbell 补充道。“微软之前尝试过销售基于 ARM 的 Windows，但效果并不理想。所以也许 Copilot 是打造成功 ARM 产品的秘诀？”

公平地说，现在有越来越多的基于 ARM 的原生 Windows 应用程序可用。但它们是否足以说服开发者这是一个好的平台？目前还不清楚。

## Copilot+ 和 SoC

微软在上个月的 [Build 开发者大会](https://thenewstack.io/microsofts-net-aspire-the-spring-boot-of-net-development/) 上推出了 Copilot+，这些 PC 本月开始由微软及其合作伙伴（包括宏碁、华硕、[戴尔](https://www.delltechnologies.com/en-us/index.htm?utm_content=inline+mention)、惠普、联想和三星）提供，起价为 1000 美元。

基于 ARM 的 Windows 设备运行在高通最新的骁龙 X 系列处理器上。骁龙 X 是一个系统级芯片 (SoC) 家族，提供强大的 CPU 性能、设备上 AI 推理等功能。骁龙 X Elite 是一款 ARM64 SoC。此外，Copilot+ PC 还配备了 [神经处理单元 (NPU)](https://thenewstack.io/qualcomm-amd-add-fuel-to-the-ai-pc-engine/)，能够提供每秒超过 40 万亿次运算 (TOPS) 的计算能力。该公司表示，与传统 PC 相比，这款新型 PC 在运行 AI 工作负载时性能提高了 20 倍，效率提高了 100 倍。

不可否认，新的骁龙 SoC 令人印象深刻，部分原因是其 NPU 具有如此高的性能。因此，各种 Copilot 应该能够在这款硬件上出色运行。此外，Campbell 表示，长电池续航的承诺也是一个吸引人的地方。

[Rockford Lhotka](https://www.linkedin.com/in/rockfordlhotka/)，[Xebia](https://xebia.com/) 的战略副总裁，也是另一位长期微软 MVP，表示他对新的硬件和操作系统功能持谨慎乐观的态度，但他想尝试一下。“我非常期待看看电池续航时间是否真的像宣传的那样。我喜欢我的 Surface 设备，但电池续航时间一直是一个严峻的挑战，”他说。

## 巨大潜力

然而，一些微软开发者看到了 Copilot+ 和 AI 用例的潜力。

“AI 可以成为基于 ARM 的 Windows 的杀手级应用，推动采用和开发者兴趣，”VBU Consulting 的项目经理和软件开发顾问 [Vasil Buraliev](https://www.linkedin.com/in/vasbu/?originalSubdomain=mk) 说。“性能优势、原生优化和战略生态系统开发的结合，可以将基于 ARM 的 Windows 打造成 AI 创新的领先平台。”

此外，他指出，微软“始终如一地展示了其在任何战略举措中都能够达到顶峰的能力，无论需要一年、五年还是十年，”他说。

## Copilot 运行时
微软将 Copilot 堆栈带到了 Windows，并推出了 [Windows Copilot 运行时](https://learn.microsoft.com/en-us/windows/ai/overview)，将 AI 融入 Windows 的各个层级。Windows Copilot 运行时包含 Windows Copilot 库，这是一个由 40 多个随 Windows 附带的设备上 AI 模型提供支持的 API 集。微软表示，它还包括 [AI 框架](https://thenewstack.io/how-ray-a-distributed-ai-framework-helps-power-chatgpt/) 和工具链，帮助开发人员将他们自己的设备上模型带到 Windows。

## 回忆被召回？
此外，该公司还推出了 Windows 语义索引，这是一种新的操作系统功能，它可以增强 Windows 上的搜索功能，并为新的体验提供支持，例如新的 [Recall](https://learn.microsoft.com/en-us/windows/ai/apis/recall) 功能。“借助 Recall，从 6 月 18 日开始的预览版，您可以以类似于拥有照相记忆的方式访问您在 PC 上看到或做过的几乎所有内容，”微软执行副总裁兼消费者首席营销官 [Yusuf Mehdi](https://www.linkedin.com/in/yusufmehdi/) 在一篇 [博客文章](https://blogs.microsoft.com/blog/2024/05/20/introducing-copilot-pcs/) 中表示。

然而，Recall 遇到了障碍，已被推迟。微软 Windows + 设备部门副总裁 [Pavan Davuluri](https://www.linkedin.com/in/pavand/) 在一篇 [博客文章](https://blogs.windows.com/windowsexperience/2024/06/07/update-on-the-recall-preview-feature-for-copilot-pcs/) 中表示，Recall 预览版将在“未来几周内”发布。

他的文章写道：“今天，我们分享了关于 Copilot+ PC 的 Recall（预览版）功能的更新，包括有关设置体验、隐私控制以及我们安全方法的更多信息。”

## 吸引人的黑眼圈？
Recall 事件对微软来说是一个黑眼圈，因为该公司在发布会上重点介绍了它。他们希望 Recall 成为这些 Copilot+/Windows on Arm PC 的展示应用程序，但现在它正在吓跑一些人，分析师指出。

然而，Recall 功能的承诺对开发人员来说仍然很有吸引力。

“就 AI 和 NPU 而言，如果 Windows 可以可靠地搜索、查找和汇总我跨本地设备和 OneDrive 的内容，那将是一个游戏规则的改变者，”Lhotka 说。

## 艰难的开局
事实上，虽然片上 AI 加速趋势目前正在整个市场中发挥作用，主要参与者正在努力在越来越小的占地面积内提供设备上 AI 服务，但“微软目前的实施，例如 Copilot+ PC，与谷歌早期的工作相比，却有一个相对艰难的开局，谷歌在其手机中配备了基本的 AI 功能，例如其照片应用程序中的魔术橡皮擦，”Omdia 分析师 [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/) 告诉 The New Stack。

此外，“微软更激进的、系统范围内的做法，例如 Recall，只是让人质疑该公司以安全的方式提供 AI 服务的能力，”Shimmin 争论道。“我相信该公司及其硬件合作伙伴最终会找到能力和隐私之间的更好平衡，例如，但就目前而言，该公司几乎没有真正‘惊艳’其庞大的软件开发人员生态系统，尤其是那些对隐私问题敏感的开发人员。”

## 长期游戏？
与此同时，AI 游戏可能不是微软的杀手级应用，而是更大战略的一部分。

Intellyx 分析师 [Jason Bloomberg](https://www.linkedin.com/in/jasonbloomberg/?originalSubdomain=nl) 告诉 The New Stack：“Windows on Arm 是一场持久战。”“今天，为微软 Surface 等平台编写代码的开发人员正在利用这项技术，但总的来说，Windows on Arm 缺乏使其与更流行的 Arm 操作系统竞争的广泛生态系统。然而，这种弱点更多地是微软长期游戏中的一个暂时症状，而不是其战略中的缺陷。”
