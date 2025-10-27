大多数 Web 团队通过合成监控开始其性能之旅。您启动一个 Lighthouse 测试或正常运行时间检查器，设置一些阈值，然后认为一切都好。

但不可避免地，错误报告会接踵而至。您可能会[听到用户抱怨](https://thenewstack.io/why-your-mobile-app-needs-client-side-network-monitoring/)您的网站在移动设备上感觉很慢，或者报告结账或其它应用程序功能在特定地理位置冻结。您可能会注意到真实世界中不同浏览器之间出现的渲染不一致。在这种情况下，您可能会发现您的仪表盘是绿色的，但您的用户却不满意。

这说明了[合成监控](https://thenewstack.io/synthetic-monitoring-can-prevent-a-customers-angry-tweet/)与[真实用户监控 (RUM)](https://thenewstack.io/how-to-fix-performance-issues-error-monitoring-cant-see/) 之间的经典差距。合成测试显示您的网站在受控、相当可预测的条件下应如何运行。另一方面，RUM 揭示了您的网站在不同设备、网络、地理位置和发布版本中实际运行的有时令人不快的事实。

两者都有其作用。诀窍在于知道何时依赖合成数据，何时投资真实用户洞察。

以下是说明这种差异的五个常见 Web 场景。

## 1. 启动新页面或功能 → 从合成监控开始

在发布新着陆页、[结账流程或用户界面 (UI) 改造](https://thenewstack.io/5-user-flows-to-trace-in-your-mobile-app/)之前，合成测试是您的最佳伙伴。它们让您可以在清晰、可重现的条件下基准测试[核心 Web 指标](https://embrace.io/blog/understanding-core-web-vitals-with-embrace-web-rum/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=synthetic-vs-rum)和关键交互。

您可以在 CI/CD 管道中自动化这些测试，或对预发布版本运行它们，以便在用户看到之前捕获回归。合成数据在代码快速迭代时保持了紧密的反馈循环。

然而，一旦部署，您会希望开始监控[真实用户会话](https://embrace.io/blog/embrace-web-rum-user-timeline/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=synthetic-vs-rum)。这是因为真实用户带来了在构建环境中不可预测的混乱：第三方脚本、广告网络、边缘缓存、不理想的网络等。合成检查不会捕获这些多样化的条件。

相反，您会需要一个 RUM 工具，以便通过确认开发中的性能改进确实转化为生产环境中更愉快、更快速的会话来闭环。

## 2. 区域或设备特定投诉 → RUM

合成监控器通常从少数全球数据中心在快速机器上运行。这对正常运行时间来说没问题，但当您的许多用户使用中端 Android 手机通过不稳定的 3G 网络操作时，它无法帮助您预测问题。

另一方面，RUM 捕获了[这些用户实际的体验](https://embrace.io/blog/introducing-embrace-web-rum/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=synthetic-vs-rum)。它旨在为您提供设备、浏览器和网络的分布洞察，这些因素决定了感知性能的好坏。

例如，使用 RUM 工具是唯一能看到您的结账脚本在南美洲的低端手机上无法执行，而美国桌面用户不受影响的方式。

## 3. 跟踪可用性和正常运行时间服务水平协议 → 合成监控

合成 ping 在可靠性监控方面表现出色。它们可预测、成本低廉且易于发出警报。如果您的网站在凌晨 3 点宕机，合成检查会在任何人之前发现。

RUM 对此进行了补充，但它并非为实时正常运行时间强制而设计。相反，它告诉您一旦发生事件，谁受到了影响以及影响的严重程度。这为您提供了重现和解决问题所需的上下文，理想情况下，在太多最终用户感到沮丧之前解决。

将它们一起使用，既能让您快速发现问题，也能了解其规模。例如，一次中断在技术上可能持续三分钟，但您的 RUM 工具显示只有 5% 的会话实际失败。这是仅凭合成监控永远无法获得的细微差别。

## 4. 优化核心 Web 指标和真实世界用户体验 → RUM

合成工具可以估算最大内容绘制 (LCP)、累计布局偏移 (CLS) 和下次绘制互动 (INP)，但它们本质上是在“实验室”条件下运行。然而，真实用户会引入可能影响这些指标的混乱。

RUM 捕获了您的核心 Web 指标在不同浏览器、设备和网络速度下的表现，这是 [Google 的 CrUX 数据集](https://developer.chrome.com/docs/crux)所基于的数据。您可能会发现只有 5% 的会话具有糟糕的 INP，但这 5% 代表了数千名沮丧的移动购物者。这些是合成监控无法发现的洞察。

## 5. 调查后端或 API 变慢 → 两者结合使用

当页面感觉迟缓时，很少仅仅是前端的错。通常，问题出在后端基础设施的某个地方，需要一番调查才能找出。合成测试在这里非常有用。这些测试可以确认您的 API 在 SLO（服务水平目标）内响应，并且关键流程（如登录或结账）没有退步。

然而，RUM 通过显示实际用户影响更进一步。

借助现代分布式追踪（例如，通过 [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/)），您可以将缓慢的 API span 与真实会话追踪中劣化的 LCP 事件关联起来。这让您能够直接连接后端问题如何阻止真实最终用户体验您的网站应有的方式。您不仅看到了后端瓶颈，还看到了它在浏览器中是如何具体表现出来的。要了解有关 RUM 现代方法的更多信息，请查看 [Embrace 提供的这场点播网络研讨会](https://get.embrace.io/getting-started-with-web-rum?utm_source=the-new-stack&utm_medium=paid&utm_campaign=synthetic-vs-rum)。

## 选择适合工作的工具

合成监控和真实用户监控是互补工具。结合使用两者的团队将获得两全其美的效果：合成监控用于受控基线和正常运行时间测试，RUM 用于真实世界情况，以及分布式追踪将它们连接起来。