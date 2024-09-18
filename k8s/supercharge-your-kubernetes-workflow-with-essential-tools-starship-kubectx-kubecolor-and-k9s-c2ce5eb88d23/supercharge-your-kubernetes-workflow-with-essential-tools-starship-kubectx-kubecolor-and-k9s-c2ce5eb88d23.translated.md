## 使用必备工具提升 Kubernetes 工作流：Starship、Kubectx、Kubecolor 和 K9s

如果您正在使用 Kubernetes，您将很快了解保持井然有序以避免错误的重要性。

我发现结合使用 **Starship**、**Kubectx/Kubens**、**Kubecolor** 和 **K9s** 可以为您提供一个干净、响应迅速的提示，帮助您保持专注，同时仍然拥有易于维护的最小插件集。让我们逐一了解它们。

### 1. Starship：速度和简单性

[Starship](https://starship.rs/) 是一个快速、最小且不可知的 shell 提示符，您可以对其进行自定义以显示关键信息，例如您所在的 Kubernetes 集群和命名空间。

无需再等待提示加载——只需速度和效率。

- 始终了解您的上下文，如集群和命名空间
- 在生产和测试之间进行颜色区分以减少错误
- 与 Git 集成良好

将其放入您的 `starship.toml` 配置中：

```
[kubernetes]
disabled = false
symbol = "⎈"
format = '[$symbol](bright-black) [$context( \($namespace\))]($style)'
[[kubernetes.contexts]]
context_pattern = "^production$"
context_alias = "production"
style = "green"
```

### 2. Kubectx/Kubens：即时切换集群和命名空间

[Kubectx](https://github.com/ahmetb/kubectx) 和 [Kubens](https://github.com/ahmetb/kubens) 允许您使用一个简单的命令在集群和命名空间之间切换。

**使用此命令：**

```
kubectx <cluster>
kubens <namespace>
```

**而不是此命令：**

```
kubectl config use-context <cluster>
kubectl config set-context --current --namespace=<namespace>
```

而且您永远不必猜测您处于什么上下文，因为 Starship 会直接在提示中显示它！

- 节省大量时间
- 减少使用 `namespace` 命令。

### 3. Kubecolor：颜色编码的 Kubectl 输出

[Kubecolor](https://github.com/kubecolor/kubecolor) 通过添加颜色高亮使 `kubectl` 输出易于阅读。

在您对集群进行故障排除或管理时，将混乱的文本转换为清晰、可读的信息，这是一个改变游戏规则的功能。

- 更快地概述错误和部署
- 减少眼睛疲劳
- 颜色编码 `kubectl` 日志

### 4. K9s：可视化和管理 Kubernetes 资源

[K9s](https://github.com/derailed/k9s) 为您提供了一个交互式的基于终端的 UI，用于管理您的 Kubernetes 集群。

它非常适合快速查看日志、监视 Pod，以及了解在您的环境中发生的事情，尤其是在新部署期间。

### 5. 奖励：使用 VS Code 编辑 Kubectl

将 `export KUBE_EDITOR='code --wait'` 添加到您的 `.bashrc` 中，以将 VS Code 添加为默认的 `kubectl` 编辑器。通过大量可用的扩展，可以更轻松地调试您的 YAML 文件。

- 与 `kubectl edit` 集成
- 与 K9s 中的编辑集成

### 迈向完美工作流之路

这些工具共同创造出流畅且信息丰富的体验。Starship 向您展示您所在的位置，Kubectx/Kubens 帮助您在集群之间跳转，Kubecolor 使您的输出更有意义，而 K9s 为您提供完整的可视化概览，同时在 Visual Studio Code 中编辑有助于您避免缩进错误。尝试一下，您将永远不想再回去了！

### 我是否遗漏了什么？

留下评论并告诉我您是否使用了其他工具！