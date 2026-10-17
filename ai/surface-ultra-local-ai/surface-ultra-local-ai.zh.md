微软将全新的 [Surface Laptop Ultra](https://www.microsoft.com/en-us/store/configure/surface-laptop-ultra/8wg5vqp0x4b8) 定位为苹果 MacBook Pro 的替代品，面向创意工作者和开发者——尤其是 AI 开发者。

它基于英伟达的 [N1X 架构 RTX Spark 平台](https://www.nvidia.com/en-us/products/rtx-spark/) 构建，配备了拥有高达 6,144 个核心的 Blackwell RTX GPU、最多 20 核的 CPU、高达 128GB 的统一内存，且价格比苹果更具优势。如果你想运行本地 AI 模型，同时又需要一台性能强大的机器随时随地进行视频剪辑和游戏，它是一个极具诱惑力的替代选择。

这里是 *The New Stack*，所以我把游戏基准测试和创作者用例留给其他人。我在测试该设备时的重点是运行 AI 工作负载。

在过去的一周里，我一直在使用高端配置的 Surface Laptop Ultra（配备 64GB RAM 和 1TB SSD，售价 4,300 美元），包括在出差途中。

![](https://cdn.thenewstack.io/media/2026/10/2aba66eb-img_5752-1024x768.jpg)

通常，我在家里使用搭载 M4 Max 芯片的 Mac Studio，它能愉快地运行我丢给它的绝大多数本地模型（只要它们能塞进 48 GB 的内存中）。我在笔记本电脑上安装了平时用来运行本地模型的所有常规工具。比如 Unsloth Studio、Ollama、Hermes Agent 等等。

在任何时候，我都觉得在笔记本电脑上运行这些东西并没有做任何妥协。甚至，如果非要说有什么不同的话，Blackwell GPU 的速度通常比我的 Mac Studio 还要快一点。

## 快速本地推理（使用正确的模型）

由于全新的 [Nemotron 3.5 Bolt 模型](https://thenewstack.io/nvidia-nemotron-bolt-laptop/) 在本周早些时候发布，我也拿它进行了试用。它以令人印象深刻的每秒 56 到 60 个 Token 的速度回答查询——有时甚至更快。这使得它成为在 Hermes Agent 或 OpenCode 中运行的绝佳模型。当然，这是一个经过大量量化、拥有 9B 活跃参数的模型，所以你自然会期望它速度很快。

然而，虽然该笔记本拥有运行它的统一内存，但采用 8 位量化的稠密模型 [Qwen 3.8 27B](https://thenewstack.io/qwen38-27b-local-inference/) 在 Unsloth Studio 中的速度从未超过每秒 8 或 9 个 Token。这几乎无法使用，但对于这些稠密模型来说，这几乎总是由于内存带宽限制造成的。不过，将其降至 4 位量化后，速度提升到了可观的每秒 25 到 28 个 Token。

使用 8 位的 [Gemma 4 26B-A4B](https://thenewstack.io/google-gemma-local-ai/) 表明，混合专家技术（Mixture-of-Experts）确实是以合理速度在本地运行几乎任何模型所必需的。对于这个模型，Surface Laptop Ultra 的运行速度通常在每秒 40 个 Token 左右。

我手头没有基于 M5 的 MacBook 或 Mac Studio，但据 [Tom’s Hardware](https://www.tomshardware.com/laptops/we-test-the-rtx-spark-superchip-in-microsofts-surface-laptop-ultra-nvidias-windows-on-arm-platform-impresses-in-local-ai-but-gaming-isnt-its-strong-suit) 报道，Ultra 在 AI 用例中的表现通常优于 MacBook Pro 中的 M5 Max。

![](https://cdn.thenewstack.io/media/2026/10/98714f00-unsloth_nvidia_bolt-1024x512.png)

运行在 Surface Pro Ultra 上的 Unsloth。图片来源：The New Stack。

## 拔掉电源后性能下降

以上所有数字都是在笔记本电脑连接 140W 充电器的情况下测得的。微软表示，他们对系统进行了调优，即使在使用电池供电时，也能让用户获得绝大部分的完整性能。微软声称其基准测试显示，笔记本在电池供电时保留了 99.6% 的性能，但至少在我测试的 AI 工作负载中，性能下降要明显得多。

例如，4 位的 Qwen 3.8 模型在使用电池时，速度从插电时的每秒 25-28 个 Token 降至每秒 18 个 Token 左右。对于 Nemotron 3.5 Bolt，性能下降到每秒 42 到 45 个 Token 左右。总体而言，在运行 AI 工作负载时，使用电池供电时性能大约会下降 20% 到 25%（游戏也表现出非常相似的降幅）。

我没有进行任何正式的电池续航测试。微软表示，用户可以期待 12 小时的活跃网页浏览时间。不过，根据我的观察，如果你持续运行本地 AI 工作负载，我预计续航不会超过几个小时。

## 内存（RAM）的疑问

拥有 64GB 的 RAM 让你处在一个有些尴尬的境地，因为目前大多数较小的模型都处于 27B 到 30B 的量级。额外的 RAM 为 KV 缓存和其他应用程序提供了充足的余量，但例如并没有太多该机器也能处理的 32-48GB 范围内的模型。

选择 128GB 的 RAM 会将 Surface Laptop Ultra 的价格推高至 5,900 美元。

## 强大性能的代价：发热与噪音

不出所料，所有的计算能力（微软称你可获得高达 1 petaflop 的 FP4 AI 性能）会产生一些热量。

没有人会说 Surface Laptop Ultra 在运行 AI 应用程序时安静得像耳语。它的双风扇产生的噪音并不极端，但在你工作时足以让人感到有点心烦。当 Hermes 或你最喜欢的编码智能体在一个更复杂的查询上持续运行一段时间时，这一点尤为明显。

毕竟，建立在同一 N1X 平台之上的 [Surface RTX Spark Dev Box](https://www.microsoft.com/en-us/store/configure/surface-rtx-spark-dev-box/8wg5vqp0x4gr) 拥有上千个散热孔是有原因的（这也可能使其性能超越笔记本电脑中的 N1X）。

除此之外，这款笔记本非常安静，在大多数日常使用场景下风扇都保持关闭状态。一旦 GPU 负载再次下降，它也会非常迅速地安静下来。

![](https://cdn.thenewstack.io/media/2026/10/eb1f838c-img_5754-768x1024.jpg)

全新 Surface 磁吸连接器和 140W 充电头。图片来源：The New Stack。

## 更多观察

如果我不强调在测试 Ultra 时发现的其他一些事情，我会觉得自己失职了。毕竟，这是微软迄今为止最具野心的笔记本电脑。

* 触控板非常巨大，并且具有触觉反馈。到目前为止，只有少数应用程序支持它，例如 DaVinci Resolve。拥有这种反馈使编辑速度更快，因为例如你可以感觉到播放头吸附到位的时间点。我希望有更多具备此功能的触控板。
* 微软对扬声器的处理创造了奇迹。笔记本电脑前部附近有侧面通气孔，可以营造出令人惊叹的宽广立体声场，你在游戏中绝对会注意到这一点。
* 全新的磁吸式 USB-C 充电连接器很好用。它感觉很像其他 Surface 设备上的磁吸 Connect。我只是担心我很快就会把线弄丢。
* 微软并没有将这定位为游戏 PC，但凭借该 GPU，人们会尝试玩一些游戏，我也是如此。在 Windows ARM 机器上进行游戏仍处于早期阶段，但多亏了微软的模拟技术，它通常在没有太大开销的情况下运行良好。
* 更多依赖 GPU 而非 CPU 的游戏表现会更好，但我能够以 2K 分辨率、开启光线追踪的情况下以大约 60fps 的速度玩《赛博朋克 2077》。通过帧生成和一些设置调整，甚至 4K 游戏也是一种选择。
* 在关闭光线追踪的情况下，《巫师 3》重制版也可以在 4K 分辨率下以 60fps 愉快地运行。
* 但由于 15 英寸、3:2 的触摸屏（3270×2180）本质上是一个更好的 3K 屏幕，除非你插入外接显示器，否则你无论如何也不会想在 4K 下运行游戏。
* 屏幕看起来很棒，而且可以变得很亮，但它也高度反光。这经常让人分心。
* 总的来说，Windows on ARM 现在感觉比一年前稳固得多。当然，确实有一些应用程序和游戏无法运行（或运行不佳），但我没有遇到任何问题。越来越多的开发者（如 OpenCode）提供桌面应用程序的 Windows ARM64 版本。
* 如果你有任何旧配件，拥有两个 USB-C、一个 USB-A 和一个 HDMI 端口简直是一种享受。再加上耳机插孔和 SD 卡读卡器，你甚至不需要携带 USB-C 扩展坞。
* 我已经习惯了我的 MacBook Air。Laptop Ultra 很重，达到了 4.41 磅（2 公斤）。
* SSD 是可更换的。笔记本电脑底部有四个螺丝，打开机器不会使你的保修失效。苹果应该注意这一点。

![](https://cdn.thenewstack.io/media/2026/10/5780c39c-img_5822-1-scaled.jpg)