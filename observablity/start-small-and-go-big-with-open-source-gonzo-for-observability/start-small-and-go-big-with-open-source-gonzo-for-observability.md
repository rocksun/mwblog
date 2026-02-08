<!--
title: 开源Gonzo：从小处着手，构建大规模可观测系统
cover: https://cdn.thenewstack.io/media/2026/01/2fd392c5-daniele-levis-pelusi-4mpsem3egak-unsplash.jpg
summary: Gonzo是开源日志分析和可观测性工具，可利用LLM辅助分析。它支持从小规模部署扩展至多云环境，并能轻松集成Kubernetes日志，有望成为云原生可观测性领域的有力竞争者。
-->

Gonzo是开源日志分析和可观测性工具，可利用LLM辅助分析。它支持从小规模部署扩展至多云环境，并能轻松集成Kubernetes日志，有望成为云原生可观测性领域的有力竞争者。

> 译自：[Start Small and Go Big With Open Source Gonzo for Observability](https://thenewstack.io/start-small-and-go-big-with-open-source-gonzo-for-observability/)
> 
> 作者：B. Cameron Gain

[日志](https://thenewstack.io/observability-2-0-or-just-logs-all-over-again/)本质上是一种语言，如果你将正确的信息输入到[大型语言模型（LLM）](https://thenewstack.io/introduction-to-llms/)中，它就可以帮助解释发生了什么。Gonzo中有一个[钩子](https://www.linkedin.com/pulse/introducing-gonzo-better-way-analyze-logs-your-jonathan-m-reeve-phd-r0i2c/)，用户可以通过后端API将日志抛给他们喜欢的LLM。这有助于发现重复的关键指标等模式，并协助进行模式分析和热力图，从而从噪音中分离出信号。随着AI生成更多代码，日志的复杂性并未简化，这使得有必要回顾数据分析的基本原理。

“日志就是语言，所以如果你把正确的信息输入到LLM中，它就能真正帮助解释日志中发生了什么……它会查看你所有的日志，并将其浮现出来，进行大量的模式分析，”[可观测性](https://thenewstack.io/introduction-to-observability/)初创公司ControlTheory的联合创始人兼首席执行官Bob Quillin[告诉我](https://www.linkedin.com/in/bob-quillin-46802511/)。

我们来看看如何在笔记本电脑上安装Gonzo，看看从运行在你的笔记本电脑或大规模多云环境中的应用程序生成有用日志是多么容易（或不容易）。在使用Gonzo之后，我发现不能将其简单性误认为是其为大型操作设计的可扩展性。类似于Stripe最初支持小型客户的方式，Gonzo旨在让组织能够随意扩展其[监控和可观测性](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/ "监控和可观测性")范围。

我建议使用Brew来快速安装，而不是直接在控制台中从GitHub拉取所有内容。

如果你已经安装了[Homebrew](https://thenewstack.io/install-homebrew-on-macos-for-more-dev-tool-options/)，那么在安装Gonzo时，更新将自动安装。此命令下载并安装Homebrew：

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

从发布页面下载适用于您平台的最新版本。

使用[Nix](https://thenewstack.io/flox-gears-up-nix-for-the-enterprise/)包管理器（测试版支持）：

```
nix run github:control-theory/gonzo
```

从源代码构建Gonzo：

```
git clone https://github.com/control-theory/gonzo.git cd gonzo make build
```

创建一个生成日志的模拟应用程序。我推荐这个，通过剪切并粘贴以下命令到你的终端来激活它：

`while true; do  
echo "$(date) INFO Starting request" >> application.log  
echo "$(date) ERROR Something failed" >> error.log  
echo "$(date) DEBUG Debug details here" >> debug.log  
sleep 2  
done`

在第二个终端窗口中使用此命令检查你的模拟应用程序是否正在生成日志：

`tail -n 5 application.log`

你应该会看到类似这样的内容（这意味着你的应用程序正在生成日志）：

[![](https://cdn.thenewstack.io/media/2026/02/a6c6ca01-screenshot-2026-01-14-at-4.22.29-pm.png)](https://cdn.thenewstack.io/media/2026/02/a6c6ca01-screenshot-2026-01-14-at-4.22.29-pm.png)

现在，让我们打开第三个终端窗口并运行以下命令，让Gonzo发挥它的魔力，列出并分析你的日志：

`gonzo -f application.log -f error.log -f debug.log`

你应该会看到类似这样的内容：

[![](https://cdn.thenewstack.io/media/2026/02/8f86cace-screenshot-2026-01-14-at-4.24.32-pm-1024x643.png)](https://cdn.thenewstack.io/media/2026/02/8f86cace-screenshot-2026-01-14-at-4.24.32-pm-1024x643.png)

现在，让我们将Gonzo扩展到它能做的下一件大事。虽然不是成熟的Kubernetes，但我们从Minikube开始，这是一个可以在笔记本电脑上的虚拟机（VM）或容器中运行的本地节点Kubernetes集群，你可以在[此处](https://minikube.sigs.k8s.io/docs/start/?arch=%2Fmacos%2Farm64%2Fstable%2Fbinary+download)下载它：

`minikube start`

一旦启动并运行（尽管我的构建中存在潜在问题），你应该会得到类似这样的内容：

[![](https://cdn.thenewstack.io/media/2026/02/75eeb1eb-screenshot-2026-01-14-at-9.08.54-pm-1024x349.png)](https://cdn.thenewstack.io/media/2026/02/75eeb1eb-screenshot-2026-01-14-at-9.08.54-pm-1024x349.png)

运行一个简单的nginx应用程序：

`kubectl create deployment nginx --image=nginx`

将这些日志流式传输到Gonzo：

`kubectl logs -f deployment/nginx | gonzo`

Gonzo界面弹出，日志开始进入：

[![](https://cdn.thenewstack.io/media/2026/02/645873c4-screenshot-2026-01-14-at-9.01.57-pm-scaled.png)](https://cdn.thenewstack.io/media/2026/02/645873c4-screenshot-2026-01-14-at-9.01.57-pm-scaled.png)

让我们点击一个错误日志，看看它揭示了什么：

[![](https://cdn.thenewstack.io/media/2026/02/a5cf48a3-screenshot-2026-01-14-at-9.23.23-pm-1024x386.png)](https://cdn.thenewstack.io/media/2026/02/a5cf48a3-screenshot-2026-01-14-at-9.23.23-pm-1024x386.png)

看起来AI链接的API尚未配置。我们将在未来的帖子中探讨这一点，看看Gonzo中AI可观测性特定功能有哪些以及它们如何工作。

## 结语

Gonzo是一个新项目，在许多方面它让我想起了[Jaeger](https://www.jaegertracing.io/)。不是Jaeger的早期，而是现在的Jaeger。Gonzo的开发已经投入了大量的工程工作，像用于跟踪的Jaeger一样，它简洁、快速、简单。正如你上面所看到的，你可以几乎立即开始观测一个Kubernetes集群，尽管存在一些bug（尽管在这种情况下，它是一个Minikube而不是一个功能齐全的Kubernetes部署）。

Jaeger和Gonzo都面向云原生部署，因此我预计Gonzo将复制Jaeger的成功。它就是有效。同样，这只是本教程中的一个简单介绍，对Gonzo功能的一个初步了解，我相信创建者所说的它可以跨多云、多部署和不同应用程序进行扩展。它对不同的数据流不挑剔，数据和日志文本无论是来自文件还是来自不同来源的应用程序进入其终端，都无关紧要。

当然，AI将在其开发中扮演重要角色，无论是AI应用程序的[可观测性](https://thenewstack.io/introduction-to-observability/)，还是它如何集成以支持可观测性分析，都将非常有趣。

可观测性与开源的未来令人期待。