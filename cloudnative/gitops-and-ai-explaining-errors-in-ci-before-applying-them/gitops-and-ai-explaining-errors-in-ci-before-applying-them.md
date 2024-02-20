<!--
title: GitOps和AI：在将错误应用到K8S之前进行解释
cover: ./cover.png
-->

在部署过程中向左转：使用 Kubectl 与 Azure OpenAI，在将其部署到 K8S 之前解释 Kubernetes 部署清单中的错误！

> 译自 [GitOps and AI: Explain Errors before applying them to K8S](https://itnext.io/gitops-and-ai-explaining-errors-in-ci-before-applying-them-d248dee7b5dd)。作者 patst 。

[内部开发者平台](https://internaldeveloperplatform.org/)（IDPs）已成为开发人员和组织的宝贵工具。它们简化并标准化了应用程序的开发和部署。

其中许多是基于 Kubernetes 的。另一个正在兴起的模式，我称之为基础设施和应用程序部署的新标准，是 [GitOps](https://www.gitops.tech/) 模式。

通过 [Flux](https://fluxcd.io/) 和 [ArgoCD](https://argo-cd.readthedocs.io/en/stable/)，CloudNativeComputingFoundation 有两个优秀的成熟工具可用。

（简化的）流程如下：

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*moqLXMGtTl5LTxs00TrUhw.png)

*简化的 GitOps 流程（图片由 patst 提供）*

本文将描述我观察到的一个挑战。此外，我将描述如何使用 OpenAI 来改进开发人员的体验，解释发生的错误消息。

## 挑战

在实现了所有工具之后，我花时间查看了基础设施存储库的 Git 提交历史记录。我发现，有很多提交消息，如“修复部署”，“修复 2”，“这次它会工作（真的！）”。

看到这一点，很明显在这个 GitOps 过程中仍然缺少一个重要的拼图：**变更验证！**

作为一名软件开发者，我非常习惯于在拉取请求中进行检查，例如检查 CI 测试是否仍在运行，应用程序是否能够编译，等等。

但在我们当前的 GitOps 过程中，我们一直在做的是：**没有！**

## 如何摆脱“试错循环”？

解决方案将取决于您使用的工具，但我们的目标是在 ArgoCD 或 Flux 应用变更之前获得有关变更的反馈。

> 我们可以称之为基础设施变更的向左转。

使用 Kubernetes，一切都以 `kubectl apply` 结束。无论您是使用 Helm Charts、纯 Kubernetes YAML 还是 Kustomize：您都可以生成 **YAML 格式的 Kubernetes 资源定义**。

我们将与 kubectl --dry-run 功能一起使用这个共同的基准来获得所需的验证。

该过程将如下所示：

1. 开发者/运维人员在基础设施存储库的特性分支上进行更改
2. CI 流水线将对更改进行模板化（=> 生成 Kubernetes 资源 YAML）
3. 模板化的 YAML 将以 --dry-run 模式发送到 Kubernetes API 服务器
4. 我们将保存任何错误消息到一个文件中

## 实施

在我们开始之前，这些是**先决条件**：

- 已安装 [Kubectl](https://kubernetes.io/docs/reference/kubectl/)
- 拥有对 Kubernetes 集群的访问权限的（只读）用户
- 已安装 [Helm](https://helm.sh/)

> 在这一步中，我假设您正在使用 Helm Charts。如果您使用的是其他工具，请确保您将拥有可以发送到 Kubernetes API 服务器的 YAML 文件。

确保你在包含 Helm Chart 的目录中，并运行：

```bash
# set the Kubernetes context to the namespace, the changes should be applied to later
helm template "my-release" . --debug  > templated.yaml
```

你看到了吗？你已经实现了你的第一个检查！

如果您的 Helm Chart 的语法不正确，“helm template” 将失败。在这种情况下，helm 将返回退出码“1”，并且您的流水线将失败。我们的第一个成功是，开发者**再也不能意外地合并语法错误的定义！**

> 您可以将 helm 退出码保存在变量中，使用 HELM_EXIT_CODE=$? 实现更好的错误处理

下一步是将 YAML 发送到 Kubernetes API 服务器以获得进一步的反馈：

```bash
# set the Kubernetes context to the namespace, the changes should be applied to later
helm template "my-release" . --debug  > templated.yaml
```

重要的是要使用 `--dry-run=server` 。[Kubectl 文档](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands)描述了其中的区别：

**dry-run**：必须是“none”、“server”或“client”。如果是客户端策略，则仅打印将要发送的对象，而不发送它。如果是服务器策略，则提交不保存资源的服务器端请求。

在服务器模式下运行可确保 API 服务器验证请求，因为集群内部调用了 Webhook。我经常观察到的一些错误包括：

- 使用了错误的 StorageClass
- 设置错误的 SecurityContext（例如，runAsNonRoot: false）
- …

确保将上面写入的 validation_errors.txt 文件的内容**附加**到**拉取请求**中作为**评论**。这提高了开发者的体验，因为错误直接在拉取请求中可见，用户无需打开流水线运行的输出。

## 利用 Azure OpenAI 改进错误消息

与其仅向开发者呈现错误消息，不如为他们提供解决方案更好。有时，Kubernetes 的错误消息可能会令人困惑，解决方案可能不会立即清晰。

由于人工智能的进步，我们可以利用语言模型做大部分工作。在这个示例中，我们使用 Azure OpenAI，但与原始 OpenAI 或任何其他语言模型都可以类似地工作。

在我们开始之前，这些是**先决条件**：

- [Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/) 部署（例如，使用 GPT-3.5 或 GPT-4）
- Azure OpenAI API 密钥
- [cURL](https://curl.se/)
- [jQ](https://jqlang.github.io/jq/)

我们将使用上面一步生成的输出（`validation_errors.txt`），并向我们的验证流程添加另一个步骤。

我们将为 Azure OpenAI 服务创建一个负载，其中包括：

- 设置上下文以说明我们要做什么的[系统消息](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/system-message)
- 我们的 helm dry-run 的错误消息

```bash
request=$(jq --arg errorMsg "$(cat validation_errors.txt)" -n '{
  "messages": [
    {"role": "system", "content": "Your are a helpful assistant. \n Context: \n- You are answering question about kubernetes deployments\n - Each answer ends with a joke about Kubernetes \n - You get error messages from the Kubernetes API Server \n - you provide YAML code snippets how to fix the error"},
    {"role": "user", "content": $errorMsg}
  ],
  "max_tokens": 800,
  "temperature": 0.9,
  "frequency_penalty": 0,
  "presence_penalty": 0,
  "top_p": 0.95,
  "stop": null
}')
```

完整的 API 描述可在 [Azure OpenAI REST API 参考](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)中找到。

下一步是创建一个 REST 调用并将负载发送到 Azure OpenAI。然后，我们使用 jQ 从响应消息中提取文本：

```bash
# make sure to replace "<your-openai-instance-name>" with the name of your instance
deploymentName="gpt-4" # make sure the deployment exists in your instance
apiKey="" # set your api-key
curl "https://<your-openai-instance-name>.openai.azure.com/openai/deployments/${deploymentName}/chat/completions?api-version=2023-12-01-preview" \
    -H "Content-Type: application/json" \
    -H "api-key: $apiKey" \
    --output response.json \
    --data "$request"
jq -r '.choices[0].message.content' response.json > output.txt
# add the content of "output.txt" to your pull request!
```

确保将 `output.txt` 的内容作为评论添加到您的拉取请求中。

这个过程将帮助开发人员更好地理解错误消息，更快地找到解决方案，从而提高生产力和效率。

为了改善反馈，您可以调整系统消息模板。

欢迎在评论中分享您的经验！

进一步阅读：

- Azure OpenAI 文档 — https://learn.microsoft.com/en-us/azure/ai-services/openai/
- Helm 模板文档 — https://helm.sh/docs/helm/helm_template/
- 提示工程技术 — https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced-prompt-engineering?pivots=programming-language-chat-completions
- ArgoCD: https://argo-cd.readthedocs.io/en/stable/


