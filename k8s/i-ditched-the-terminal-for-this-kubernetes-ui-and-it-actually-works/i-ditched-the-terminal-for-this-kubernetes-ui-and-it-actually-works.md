
<!--
title: 告别终端！我被这款Kubernetes UI彻底征服，效率飙升！
cover: https://miro.medium.com/v2/resize:fit:1024/1*3WaYF0aSuvRL9yr4IUfUcQ.png
summary: Headlamp轻量、启动快，支持多集群无需切换上下文。UI尊重RBAC，有原生插件，实时监控。它专注于提供无废话的UI，不替代kubectl，优于笨重臃肿的Lens。
-->

Headlamp轻量、启动快，支持多集群无需切换上下文。UI尊重RBAC，有原生插件，实时监控。它专注于提供无废话的UI，不替代kubectl，优于笨重臃肿的Lens。

> 译自：[I ditched the terminal for this Kubernetes UI and it actually works](https://medium.com/@devlinktips/i-ditched-the-terminal-for-this-kubernetes-ui-and-it-actually-works)
> 
> 作者：Devlink Tips

## 为什么我选择 Headlamp 而不是 kubectl 和 Lens

老实说：我们大多数人都生活在终端中。`kubectl get pods` 在此时基本上已经是肌肉记忆了。当然，对于某些事情，没有什么能比得上 CLI。但当你同时处理多个集群、检查 RBAC、查看日志、编辑 YAMLs，并向 Zoom 上的某人解释到底发生了什么时——你就会开始渴望一个不那么糟糕的 UI。

这就是 **Headlamp** 的作用，它比我预期的要好。

## kubectl：强大但痛苦

*   非常适合脚本和快速命令
*   对于多集群工作流来说很糟糕
*   除非你已经知道要找什么，否则无法提供可见性
*   你离搞砸生产环境只有一步之遥

## Lens：强大但臃肿

*   Lens 很强大，毫无疑问
*   但它 **Electron-laden**，启动慢，对我来说有点过于“IDE 感”
*   多集群？可以，但你必须手动管理上下文，并祈祷你的 kubeconfig 是干净的
*   有些功能现在需要通过他们的云登录才能使用，不，谢谢

## Headlamp：恰到好处的 UI，没有废话

*   即时启动，可在浏览器或桌面运行
*   读取你的 kubeconfig，支持**无需上下文切换技巧的多个集群**
*   不试图成为 Kubernetes 界的 VSCode
*   感觉像是**由**开发者构建的 UI，而不是为了市场营销截图

它不替代 `kubectl`，也无意替代。相反，当精度很重要且时间紧迫时，Headlamp 提供了一种更简单的方式来导航集群。特别是如果你在一个团队中，不能假设每个人都是 CLI 高手。

我仍然使用 `kubectl` 编写脚本，但对于探索、调试和实时操作呢？Headlamp 就是…好用。

按 Enter 键或点击以全尺寸查看图像

![](https://miro.medium.com/v2/resize:fit:700/1*wdEy1IMRigr68UZXcT7B4w.png)

## 让我留下来的功能

Headlamp 不仅仅以简洁的 UI 赢得了我。它之所以能留下来，是因为它在不贪多嚼烂的情况下解决了实际痛点。以下是让我将其安装在我所有机器（和集群）上的突出功能。

## 多集群支持（做得很好）

大多数工具都声称支持多集群。它们**真正**的意思是：“你可以手动切换 kubeconfig 上下文，并希望它能正常工作。”

Headlamp 真的做到了。

你可以在 UI 中同时加载**多个集群**。它从你的 kubeconfig 中提取信息，每个集群都显示在侧边栏中，方便切换。你无需重新认证或管理环境变量，即可查看跨集群的工作负载。它甚至对它们进行了颜色编码——简单，但某种程度上是救星。

## RBAC 感知 UI

你是否遇到过这样的情况：一个初级工程师问“为什么我看不到 pod？”，然后你意识到他们的角色没有权限——但他们自己却无从知晓？

Headlamp **尊重 Kubernetes RBAC**，因此如果用户以受限权限登录，UI 只显示他们被允许查看的内容。没有奇怪的错误，也没有禁止访问的屏幕。这很微妙，但它在实际团队中保持了理智。

## 真正感觉原生的插件

与其他将插件作为营销复选框附加的仪表板不同，Headlamp 拥有一个使用 React 和 TypeScript 构建的**真正的插件架构**。

想为你的 CRD 添加自定义可视化？尽管去做。需要从 Prometheus 或你堆栈中的自定义组件中获取指标？你可以扩展 UI，而无需修补核心代码。

我构建了一个基本插件，用于从带有额外解析的 sidecar 容器中获取日志，感觉就像编写一个迷你 React 应用，而不是修补一些脆弱的 YAML。

[**插件文档在此**](https://github.com/headlamp-k8s/headlamp/blob/main/docs/extensions.md)

## 实时资源监控

你不需要像 2004 年那样每 5 秒点击一次“刷新”。Headlamp 支持部署、pod、事件、日志等的**实时更新**——应有尽有。实时观看滚动更新或崩溃的 pod 实际上……令人愉快？

此外，YAML 编辑器支持内联编辑，并在应用前验证更改。这比在脆弱的东西上进行实时的 `kubectl edit` 要轻松得多。

## 内置终端

如果你**确实**想进入终端，Headlamp 内置了一个。你可以直接从界面打开 pod 的 shell——无需单独的标签页，无需输入冗长的 pod 名称。它不如 `k9s` 强大，但对于快速检查或从文档中复制粘贴命令来说，它非常方便。

这就是这个工具悄悄地展现实力的地方。它不试图超越 Lens 或取代终端——它专注、可扩展、快速。