# 2024 年 Kubernetes 配置

我在 2017 年 [撰写了一篇关于声明式配置问题空间和可用工具的概述](https://github.com/kubernetes/design-proposals-archive/blob/main/architecture/declarative-application-management.md)，当时我正在 [围绕 kustomize 进行构思](https://github.com/kubernetes/kubectl/pull/65)。[2018 年](https://leebriggs.co.uk/blog/2018/05/08/kubernetes-config-mgmt) 和 [2019 年](https://blog.argoproj.io/the-state-of-kubernetes-configuration-management-d8b06c1205) 有其他人撰写了很好的概述。我最近重新审视了 [我在 2017 年整理的列表](https://docs.google.com/spreadsheets/d/1FCgqz1Ci7_VCz_wdh8vBitZ3giBtac_H8SBw4uxnrsE/edit#gid=0)。不出所料，并非所有这些工具都还在维护。我查看了我知道的、似乎比较流行的开源工具的 Github 星标数量（因为没有其他数据来源），并剔除了那些星标少于 1000 个或不再维护的工具。

据我所知，[Helm](https://github.com/helm/helm)（26100 个星标）和 [Kustomize](https://kustomize.io/)（10600 个星标）是最流行、集成最广泛的工具，例如在 CD 工具、[GitOps](https://medium.com/@bgrant0607/is-gitops-actually-useful-a1c851ba99d8) 工具、包装工具（如 [Helmfile](https://github.com/helmfile/helmfile)（3300 个星标）和 [Helmsman](https://github.com/Praqma/helmsman)（1400 个星标））以及基础设施即代码 (IaC) 工具（如 Terraform ([Terraform Helm provider](https://github.com/hashicorp/terraform-provider-helm)，[Terraform Kustomize provider](https://registry.terraform.io/providers/kbst/kustomization/latest/docs)) 和 [Pulumi](https://github.com/pulumi/pulumi-kubernetes?tab=readme-ov-file#deploying-a-helm-chart)）中。一旦一个工具达到临界质量，围绕它的生态系统就会成为采用它的主要动力。对于 Helm 来说，大量可用的 Helm 图表使其对许多 Kubernetes 用户来说必不可少。这使得选择另一个工具更像是“并且”而不是“或者”，因此它需要易于采用和/或提供比 Helm 更大的优势，或者吸引来自相邻生态系统的用户。

其他顶级工具有哪些？

* [Kompose](https://github.com/kubernetes/kompose)([compose spec](https://compose-spec.io/)): 9200 个星标
* [Cdk8s](http://cdk8s.io)(Typescript, JavaScript, Python, Java, Go): 4200 个星标
* [Tanka](https://github.com/grafana/tanka)([jsonnet](https://jsonnet.org/)): 2300 个星标
* [Kapitan](https://github.com/kapicorp/kapitan)(多语言): 1800 个星标
* [Ytt](https://github.com/carvel-dev/ytt)([starlark](https://github.com/bazelbuild/starlark)，是 [carvel.dev](https://carvel.dev/) 的一部分——注意 [最近的项目变更](https://www.youtube.com/watch?v=6Fp_ysDd-z0)): 1600 个星标
* [Terraform kubernetes provider](https://github.com/hashicorp/terraform-provider-kubernetes): 1500 个星标
* [Timoni](http://timoni.sh)([CUE](http://cuelang.org)): 1400 个星标
* [KCL](https://github.com/kcl-lang/kcl): 1300 个星标

如果我错过了某个流行的工具，请告诉我！

Kompose 使 [Docker compose](https://docs.docker.com/compose/) ([32600 个星标](https://github.com/docker/compose)) 和 Kubernetes 之间能够互操作，无论是为了在本地开发期间使用 Docker 还是为了迁移目的。考虑到 Docker compose 用户的数量，它的流行程度并不令人惊讶。

类似地，cdk8s 的部分流行程度可能是由于 [AWS CDK](https://aws.amazon.com/cdk/) 用户。总的来说，从现有数据来看，使用通用编程语言的配置生成工具的使用率仍然低于非 GPPL 工具。另一方面，GPPL 工具可能比受限的方言（如 Starlark）更受欢迎，Starlark 最近似乎在较少的新的工具中使用。

只有时间才能证明，像 CUE、KCL 或 Pkl 这样的新的工具无关的领域特定语言的优势是否足以与 YAML 和/或其他语言和配置方法竞争，考虑到 YAML 的普遍性和新语言的缺点（缺乏熟悉度、缺乏工具和库支持、缺乏生态系统集成等）。

Kapitan 作为一种 [跨多个工具管理输入变量值的机制](https://kapitan.dev/pages/blog/04/12/2022/kapitan-logo-5-years-of-kapitan/#with-kapitan) 很有趣，它重新利用了 [一种独立于配置管理工具管理节点的机制](https://reclass.pantsfullofunix.net/)，例如 Puppet、Salt 和 Ansible。
用户似乎对[使用 Terraform 管理 Kubernetes 资源](https://www.reddit.com/r/Terraform/comments/120g6l5/to_terraform_or_not_to_terraform_kubernetes/) 是否是一个好主意存在分歧。一方面，使用 Helm 提供程序可能对在创建集群后安装组件有意义，但用户[遇到了问题](https://www.reddit.com/r/kubernetes/comments/cq5bof/anyone_using_terraformhelmprovider_to_deploy/)。由于我不认为集群会像虚拟机那样变得不可变，因此我建议使用 GitOps 工具来配置集群中的资源。

我最近也在[Twitter/X 上询问](https://twitter.com/bgrant0607/status/1787702594229707119)人们除了上述工具之外还使用什么工具。受访者还提到了哪些其他工具？

Kubernetes 特定：

* [qbec](https://github.com/splunk/qbec) (Jsonnet)
* [StackSet Controller](https://github.com/zalando-incubator/stackset-controller) + mustache

非 Kubernetes 特定：

相对大量的工具验证了创建 Kubernetes 配置工具并将 Kubernetes 集成到现有工具中是比较容易的，因为[Kubernetes 资源可以序列化为数据](https://medium.com/@bgrant0607/on-using-the-kubernetes-resource-model-for-declarative-configuration-a5dd11b99546)。这使得在构建或部署时使用您喜欢的 IaC 工具、编程语言、数据序列化语言或模板工具来生成 Kubernetes 配置，或者通过构建[控制器](https://kubernetes.io/docs/concepts/architecture/controller/)（如 StackSet 控制器）来动态管理它成为可能。

但也有许多用户显然在使用领先工具 Helm 时遇到了挑战和摩擦，其中许多挑战都集中在 Helm 图表的复杂性和模板语法上。以下是一些例子，不分先后，包括一些来自创建或使用替代工具的人：
至少部分复杂性是模型和目标固有的。如果想要提供开箱即用的参数驱动配置生成器，使用户能够配置任何东西，那么生成的生成器代码和接口将非常庞大，类似于结构构造函数。这就是[简单性与灵活性之间的权衡](https://medium.com/@bgrant0607/the-tension-between-flexibility-and-simplicity-in-infrastructure-as-code-6cec841e3d16)。它也适用于定制应用程序的通用配置生成器，例如[Ticketmaster 的一站式图表](https://youtu.be/HzJ9ycX1h0c) 和[Gimlet 的 OneChart](https://github.com/gimlet-io/onechart)。在 Kubernetes 的早期，基于 jsonnet 的模板也遇到了类似的挑战。

由于许多抱怨都与 YAML 缩进有关，我一直想知道是否可以广泛地利用[JSON 列表和映射语法](https://helm.sh/docs/chart_template_guide/yaml_techniques/#yaml-is-a-superset-of-json)，从而[不再依赖缩进](https://medium.com/@kasunbg/write-yaml-without-indentation-via-curly-braces-3c05ae8700ce)，例如[stackoverflow 上的这个示例](https://stackoverflow.com/questions/72314961/helm-convert-map-type-data-into-json-object)，与[Jenkins helm 图表](https://github.com/jenkinsci/helm-charts/blob/main/charts/jenkins/templates/jenkins-controller-ingress.yaml) 中的这个示例不同：

```yaml
{{- if .Values.controller.ingress.labels }}
{{ toYaml .Values.controller.ingress.labels | indent 4 }}
{{- end }}
```

那么，自从我 2017 年的写作以来，发生了什么变化？

- Helm 成为 CNCF 的顶级项目，修复了 v3 中的一些问题，并推动了
- 使用 [容器注册表](https://github.com/oras-project/oras) 来管理配置包。不过，有些人对该项目的健康状况表示 [担忧](https://www.youtube.com/watch?v=-ny_SXusAks)。
- Kustomize 已经实现，被 Kubernetes SIG CLI 采用，集成到 kubectl 中，并成为第二受欢迎的工具。
- HashiCorp 实现了一个新的 [基于服务器端应用的 Terraform Kubernetes 提供程序](https://www.hashicorp.com/blog/deploy-any-resource-with-the-new-kubernetes-provider-for-hashicorp-terraform)。
- 使用通用编程语言生成配置更为普遍，并且工具 (cdk8s、Pulumi) 更加先进。
- 新的工具和语言不断涌现，但也出现了相当程度的整合。
- GitOps 成为一种流行的模式，尤其是在 [部署到多个集群](https://medium.com/@bgrant0607/is-gitops-actually-useful-a1c851ba99d8) 方面。

总的来说，我的感觉是这些工具已经成熟，但在过去 7 年中用户体验并没有发生太大变化。

Kubernetes 现在已经 10 岁了。在这个领域还有进化的空间吗？还是说目前的配置工具已经足够好了？现在新的工具有可能像 Helm 一样被广泛采用吗？更广泛的 IaC 工具有可能被广泛用于 Kubernetes 吗？用户采用新工具的动机是什么？在人工智能时代，配置语言还重要吗？还是说新的平台会掩盖低级配置工具？

我希望对新的、更好的工具有需求和激励。这个领域肯定还有 [创新的空间](https://medium.com/@bgrant0607/reflections-on-declarative-configuration-c2fe1c1e50d5)。

您喜欢使用哪些工具，为什么？

欢迎在这里回复，或通过 [LinkedIn](https://www.linkedin.com/in/bgrant0607/) 或 [X/Twitter](https://x.com/bgrant0607/) 给我发消息，我计划将此内容交叉发布。

如果您觉得这篇文章有趣，您可能还会对我的 [基础设施即代码和声明式配置系列](https://medium.com/@bgrant0607/list/infrastructure-as-code-and-declarative-configuration-8c441ae74836) 中的其他文章感兴趣。