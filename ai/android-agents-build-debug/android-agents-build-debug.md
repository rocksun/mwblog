<!--
title: 谷歌刚刚把安卓的钥匙交给了竞争对手
cover: https://cdn.thenewstack.io/media/2026/10/fe17422f-mohamed-nohassi-bpvdngbw1c-unsplash-scaled.jpg
summary: 谷歌向Anthropic的Claude Code和OpenAI的Codex等40多款第三方智能体开放安卓开发工具，使其能够深入参与调试、测试和错误修复，标志着安卓开发迎来AI智能体时代。
-->

谷歌向Anthropic的Claude Code和OpenAI的Codex等40多款第三方智能体开放安卓开发工具，使其能够深入参与调试、测试和错误修复，标志着安卓开发迎来AI智能体时代。

> 译自：[Google just handed its rivals the keys to Android](https://thenewstack.io/android-agents-build-debug/)
> 
> 作者：Amanda Caswell

**谷歌正在让像 Anthropic 的 Claude Code 和 OpenAI 的 Codex 这样的编码智能体更深入地访问**其安卓开发工具，包括设备、性能分析器和生产环境崩溃报告；现在，智能体可以调查漏洞、测试更改并验证它们自己的修复方案。

这一举措涵盖了 Android Studio 和基于终端的 Android CLI，谷歌向第三方智能体开放了这两者，而不是将开发者强行引导向 Gemini。安卓产品副总裁 [Matthew McCullough](https://www.linkedin.com/in/matthewjmmccullough/) 强调，要给予开发者自由选择自己模型和编码智能体的权利。

在周三的一篇[博文](https://developer.android.com/blog/posts/android-dev-summit-26-developer-tools-performance)中，安卓开发工具高级产品经理 [Adarsh Fernando](https://www.linkedin.com/in/adarsh-fernando-87905462/) 将这一目标描述为：为开发者及其智能体提供“更快构建高质量安卓应用所需的工具和知识”。这些更新是在周三的 [Android Dev Summit](https://developer.android.com/events/dev-summit) 上宣布的。

## 自带智能体

该公司推出的“自带智能体”（Bring Your Own Agent）功能现在支持 40 多个使用开放式 [Agent 客户端协议](https://agentclientprotocol.com/)的编码智能体，其中包括 Anthropic 的 Claude Agent、OpenAI 的 Codex 以及谷歌自己的 Antigravity。谷歌表示，该功能在周三发布的 Android Studio Rabbit 2 中已趋于稳定。

开发者可以安装多个智能体并在它们之间进行切换，而无需离开 IDE。连接的智能体可以继承 IDE 对项目的理解——包括其结构、构建配置、符号以及诸如 Compose Preview、模拟器和 Logcat 等工具——否则这些上下文他们必须通过代码搜索和终端猜测来重新构建。

除此之外，一项新的“更改审查”（Change Review）功能可以扫描智能体的待处理更改以查找常见问题，并能在应用任何修改之前引导开发者浏览大量修改。谷歌还通过为 Claude Code 和 Codex 提供官方 Android CLI 插件，将这一影响力扩展到 IDE 之外，这些插件涵盖了项目创建、模拟器管理、UI 检查以及其安卓文档。

## 从终端进行 Compose 预览

另一项公告包括全新的 `android preview` 命令，该命令允许编码智能体直接在终端中渲染 Jetpack Compose 预览，而无需启动 IDE 或模拟器。

该公司表示，使用该命令的智能体完成 UI 任务的速度快了 77%，同时使用的 Token 减少了最多三倍，尽管它很少透露是如何衡量这些结果的。CLI 还添加了 `android device remote`，让智能体能够访问谷歌实验室中的物理设备进行测试。

> 使用该命令的智能体完成 UI 任务的速度快了 77%，同时使用的 Token 减少了最多三倍，尽管它很少透露是如何衡量这些结果的。

## 用 Claude 查找内存泄漏

谷歌还为智能体提供了更多在应用构建后调查问题的方法，包括性能问题、生产环境崩溃和内存泄漏。在一个演示中，Claude Code 与开源泄漏检测库 LeakCanary 合作，使用开发者的一条指令检查关键用户旅程中的内存泄漏。

Claude Code 在多台设备上并行运行这些旅程，通过 CLI 的 LeakCanary 集成分析堆转储（heap dumps），并将泄漏追溯到出问题的代码。然后，它进行了修复并重新运行测试以确认它们有效。谷歌表示，该工具帮助有能力的智能体完成这些调查的速度快了近一倍，同时使用的 Token 减少了高达 25%。

> 自主查找漏洞的速度可能会超过自主修复漏洞的速度——Anthropic 扫描器在开源代码中标记了大约 29,000 个可能的漏洞，而真正得到修复的只有几百个。

这个演示非常令人印象深刻，但它也伴随着需要耐心的记录，因为自主查找漏洞的速度可能会超过自主修复漏洞的速度——Anthropic 扫描器[在开源代码中标记了大约 29,000 个可能的漏洞，而真正得到修复的只有几百个](https://thenewstack.io/anthropic-oss-scanner-vulnerabilities/)。

配套的 `android signals` 命令现在将 Android vitals 和 Firebase Crashlytics 数据管道传输到同一个终端工作流中，这为智能体提供了通往生产环境崩溃、ANR 和内存问题的直接途径，但这并不能让循环中的人类退休，正如那些目睹了 [Claude Code 提交了一个 Linux 内核修复却被评审人员抓出一个竞态条件的开发者](https://thenewstack.io/torvalds-claude-code-kernel/)所能证明的那样。

> 配套的 `android signals` 命令现在将 Android vitals 和 Firebase Crashlytics 数据管道传输到同一个终端工作流中

## 使用 Android Bench 对智能体进行基准测试

谷歌还推出了 Android Bench 2.0，以评估模型和智能体框架在更复杂的安卓开发任务上的表现。它测试完成的应用是否实际运行，分配的任务从从模型构建应用到迁移现有界面不等。有些任务仿照了需要安卓工程师几天时间才能完成的工作，该基准测试还测量了完成时间和成本。