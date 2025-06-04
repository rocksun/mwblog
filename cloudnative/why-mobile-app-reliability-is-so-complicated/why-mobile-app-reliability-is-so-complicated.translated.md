# 为什么移动应用可靠性如此复杂

![为什么移动应用可靠性如此复杂 的特色图片](https://cdn.thenewstack.io/media/2025/05/a581826a-apps-1024x576.jpg)

移动开发没有得到足够的重视。虽然 Web 和后端工程师通常受益于相对标准化的环境，但移动开发人员面临着一个庞大而分散的局面，这使得交付高性能、可靠的应用程序非常困难。

在 Embrace，我们[分析了数据](https://get.embrace.io/mobile-app-complexity-6-charts?utm_source=the-new-stack&utm_medium=paid&utm_campaign=mobile-app-complexity)，这些数据来自使用我们的可观测性 SDK 的众多移动应用客户，以了解移动环境的真实范围和混乱程度。这些数字描绘了一个清晰的画面：移动端非常混乱。我们正在分享这些数据，供工程领导和可靠性团队了解移动团队每天面临的复杂性规模，以及这如何影响最终用户。

以下是移动端如此复杂的一些原因。

## 公司通常支持数十个移动应用版本

与自动更新的基于浏览器的应用程序不同，[移动应用程序通常与用户行为相关联](https://thenewstack.io/5-user-flows-to-trace-in-your-mobile-app/)，尤其是在更新方面。用户跳过版本、忽略通知或受到过时操作系统的限制。这导致了大量活跃的应用程序版本。

- 31% 的应用程序同时运行 5 到 10 个活跃版本。
- 25% 的应用程序支持 10 个以上的版本。
- 6% 的应用程序在生产环境中运行 50 多个版本。

支持如此广泛的旧版本不仅仅是测试覆盖率的挑战。这是一个性能、崩溃和可观测性的噩梦。旧版本通常速度较慢、稳定性较差且更容易出现回归。然而，工程团队需要保持所有版本平稳运行。真有趣！

## 硬件差异比你想象的更严重

设备类型带来了自身的挑战，因为[手机的运行](https://thenewstack.io/choosing-manual-or-auto-instrumentation-for-mobile-observability/)具有不同的内存和处理能力级别。Android 生态系统以其碎片化而闻名，26% 的 Android 开发人员发现他们的应用程序在 1,000 多种独特的设备类型中使用。

由于每个设备提供不同级别的内存、CPU 和操作系统级别的功能，因此大规模优化性能几乎变得不可能。在独特的设备类型方面，iOS 生态系统受到更多控制，但仍然远非简单。

## 网络连接非常不稳定

网络情况因 iOS 和 Android 以及地理位置而异。移动应用用户依赖于 Wi-Fi 和蜂窝网络的不同组合，这种不一致可能导致[不可预测的应用程序体验](https://thenewstack.io/best-practices-for-monitoring-network-conditions-in-mobile/)，具体取决于本地基础设施。例如，非洲 30% 的用户和亚洲 50% 的用户完全依赖蜂窝网络进行连接。

## 将监控数据发送回服务器的延迟

由于网络中断、应用程序崩溃或用户行为，移动遥测数据在到达服务器时可能会[显着延迟](https://thenewstack.io/why-your-mobile-app-needs-client-side-network-monitoring/)。移动用户并非生活在真空中——他们会移动！他们在蜂窝网络、Wi-Fi 连接和盲区之间切换。他们丢失数据包，在会话中途离线，并在几小时后恢复。想想你最喜欢的徒步旅行应用程序。当您脱离网络时，移动工程师一片茫然。这些连接间隙会导致不可预测的遥测延迟。

- 17% 的移动遥测数据延迟超过一小时到达。
- 7% 的数据需要 12 小时以上才能到达可观测性后端。

这通常意味着工程师在[对应用程序健康状况的了解不完整](https://www.cncf.io/blog/2024/03/25/why-you-may-be-dropping-key-mobile-data-from-your-observability-solution/)的情况下进行操作。他们无法修复他们不知道已损坏的东西。幸运的是，人们已经对[时间如何在聚合移动数据的可观测性中发挥关键作用](https://thenewstack.io/how-time-plays-a-crucial-role-in-aggregating-mobile-data/)以及最佳实践进行了大量思考。

## 可观测性正在为真实世界的复杂性而发展
传统的可观测性工具是为稳定的服务器端环境构建的，但[移动应用在复杂多变的环境中运行](https://get.embrace.io/mobile-observability-guide?utm_source=the-new-stack&utm_medium=paid&utm_campaign=mobile-app-complexity)。工程师需要了解真实用户设备上发生的情况，包括他们无法控制的不可预测的网络状况和硬件差异。仅仅依靠后端信号会[错过用户感知到的关键移动性能问题](https://thenewstack.io/sending-mobile-signals-to-the-opentelemetry-collector/)。想想应用卡顿、启动缓慢、特定设备上的崩溃、黑屏、网络掉线、行为异常的第三方SDK、跨应用版本的不一致行为以及无响应的UI交互。如今的可观测性策略必须包含真实的用户上下文，包括用户看到了什么、何时发生以及为什么这对成功的移动业务至关重要。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的YouTube
频道，观看我们所有的播客、访谈、演示等。