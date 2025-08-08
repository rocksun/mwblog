用于部署和运行 Kubernetes 的数据序列化语言已经过全面改进。

Kubernetes 的 [即将发布的 1.34 版本](https://kubernetes.io/blog/2025/07/28/kubernetes-v1-34-sneak-peek/) 可能会附带 KYAML，它是 YAML 的一个严格子集，专门为 [Kubernetes 用户](https://thenewstack.io/kubernetes/) 格式化。

“YAML 是 Kubernetes 的编程语言，”云原生软件包管理服务 [Cloudsmith](https://cloudsmith.com/company/about) 的开发者关系主管 [Nigel Douglas](https://allthingsopen.org/authors/nigel-douglas) 在接受 TNS 采访时表示。

然而，许多用户对 YAML 中的许多 [设计怪癖](https://thenewstack.io/yall-against-my-lingo-why-everyone-hates-on-yaml/) 感到沮丧，这些怪癖导致额外的工作和额外的调试（即使创建者本人正在努力使 [YAML 成为一个成熟的编程语言](https://thenewstack.io/with-yamlscript-yaml-becomes-a-proper-programming-language/)）。

解决 YAML 困境的方案是什么？加入少量的 [JSON](https://thenewstack.io/an-introduction-to-json/)。

## 呼叫 Null 医生

YAML [贯穿](https://thenewstack.io/from-yaml-to-platforms-the-kubernetes-deployment-journey/) 整个 Kubernetes 生态系统：用于创建网络策略，编写部署清单或用于 Helm 部署文件。

一个问题是：YAML 不能很好地处理 [空格](https://thenewstack.io/spaces-vs-tabs-a-20-year-debate-and-now-this-what-the-hell-is-wrong-with-go/)。特别是，当用户使用嵌套指令时，他们必须密切注意使用的缩进数量。格式化对于 [云原生战士](https://thenewstack.io/cloud-native/) 来说是一项繁琐的工作，但是代码中错误的 idents 数量可能会绊倒 Helm。

同样，YAML 中可选的引号导致了歧义，这对于计算机来说始终是危险的。引号的挑战通过“[挪威问题](https://hitchdev.com/strictyaml/why/implicit-typing-removed/)”得到了恰当的说明，其中未能用一组引号封装一个两位数的国家/地区缩写可能会绊倒寻找保留关键字的解析器，例如挪威的“NO”。

或者，在另一种情况下，`Last_Name=Null` 实际上是为名叫 Richard Null 的人准备的。

正如许多人指出的那样，JSON 也可以用来代替 YAML，尽管它在 Kubernetes 环境中也有其自身的局限性：没有注释支持，并且严格遵守尾随逗号和带引号的键。

## 另一种标记语言

“YAML 最令人沮丧的部分是它不必这么糟糕。YAML 是一个非常广泛的规范。在该规范中，有一个合理的语法尖叫着要被释放出来，”Kubernetes 提案 [KEP 5295](https://github.com/kubernetes/enhancements/issues/5295) 断言。

KYAML 就是该规范，至少对于 Kubernetes 用户而言。Douglas 说，KYAML“以一种方式构建，它与 Kubernetes 对象周围的现有设计完全兼容”。

KYAML 是 YAML 的一个严格子集。所有 KAYML 文件也是有效的 YAML，它们可用于编写清单和 [Helm charts](https://thenewstack.io/what-the-helm-the-tool-we-all-love-and-sometimes-hate/)，而无需 K8s 的其他标志。

如果包含在 Kubernetes 1.34 中（仍在最终确定），KYAML 将与 `kubectl` Kubernetes 命令行一起使用，该命令行将使用特殊标志以 KYAML 格式输出（即，`kubectl get -o kyaml`）。

以下是 KYAML 的其他规则。

* 双引号是值字符串。
* 键不带引号，除非可能不明确。
* 映射（关联数组）使用大括号 `{}`。
* 列表使用方括号 `[]`。

这些规则模仿 JSON，尽管与 JSON 不同，KYAML 支持注释和尾随逗号，并且不需要带引号的键。

此外，KYAML 对 [空格不敏感](https://github.com/kubernetes/enhancements/blob/master/keps/sig-cli/5295-kyaml/README.md)。

以下是提案提供的示例：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | $ kubectl get -o kyaml svc hostnames |
|  | --- |
|  | { |
|  | apiVersion: "v1", |
|  | kind: "Service", |
|  | metadata: { |
|  | creationTimestamp: "2025-05-09T21:14:40Z", |
|  | labels: { |
|  | app: "hostnames", |
|  | }, |
|  | name: "hostnames", |
|  | namespace: "default", |
|  | resourceVersion: "37697", |
|  | uid: "7aad616c-1686-4231-b32e-5ec68a738bba", |
|  | }, |
|  | spec: { |
|  | clusterIP: "10.0.162.160", |
|  | clusterIPs: [ |
|  | "10.0.162.160", |
|  | ], |
|  | internalTrafficPolicy: "Cluster", |
|  | ipFamilies: [ |
|  | "IPv4", |
|  | ], |
|  | ipFamilyPolicy: "SingleStack", |
|  | ports: [{ |
|  | port: 80, |
|  | protocol: "TCP", |
|  | targetPort: 9376, |
|  | }], |
|  | selector: { |
|  | app: "hostnames", |
|  | }, |
|  | sessionAffinity: "None", |
|  | type: "ClusterIP", |
|  | }, |
|  | status: { |
|  | loadBalancer: {}, |
|  | }, |
|  | } |

## 但我仍然讨厌它

与任何修改后的数据格式一样，这些更改将 [受到激烈争论](https://thenewstack.io/typescript-vs-javascript/)。开发人员预计到这一点。

“语法一直是我们行业中争论的焦点。我们预计这也不例外。理性的人会不同意我们的选择，这很好，但我们应该对此持有强烈的意见，”开发人员在 [ReadMe 文件](https://github.com/kubernetes/enhancements/blob/master/keps/sig-cli/5295-kyaml/README.md) 中警告说，该文件最初由 [Tim Hockin](https://thenewstack.io/tim-hockin-kubernetes-needs-a-complexity-budget/) 撰写。

而且反应已经到来了。

“它比 JSON 更好，我明白为什么这比 YAML 更好，但我仍然讨厌它，”一位 [Reddit 用户写道](https://www.reddit.com/r/kubernetes/comments/1md8wle/kyaml_looks_like_json_but_named_after_yaml/)。

快速搜索显示，至少已经为 [Go 编程语言](https://pkg.go.dev/sigs.k8s.io/kustomize/kyaml) 制作了一个特定于编程语言的 KYAML 实现。

已经采取了其他方法，包括精简的 [StrictYAML](https://hitchdev.com/strictyaml/features-removed/)，尽管 KYAML 在新的 Kubernetes 版本中具有快速通道。让我们看看它还可以在哪里使用。

*Kubernetes 1.34 预计将于 8 月下旬发布。*