# Kubecon 2022 中关于平台的内容

*本文翻译自[Josh Gavant]个人博客。关于 CNCF 平台的白皮书，目前可以看这个 [v1alpha1](https://github.com/cncf/tag-app-delivery/blob/platforms-v1alpha1/platforms-whitepaper/v1alpha1/paper.md) 版本。*

10 月 25 日的 Kubecon 是一个很好的机会，可以与人们会面并讨论使云计算对从业者和企业更容易和更高效的新兴想法。云平台和平台工程是一个热门的讨论项目，似乎有望最终为企业提供一条最大限度地提高开发/运营合作和效率的途径。作为 CNCF 平台工作组 (WG) 的负责人，为了更好地理解此类平台的要求，我花时间与领导者和项目维护人员交谈，为他们开发构建模块。工作组计划在 2022 年底之前提供有关典型平台的功能和要求的指南。

尤其是，平台工作组举办了一场“非见面会”（幻灯片在[这里](https://docs.google.com/presentation/d/1LoAzgZe3rJuxHT86Cdj6Tv4-0XpL7nN6SMCl6oN4JbU/)），几家平台组件提供商在会上自我介绍并分享了对其项目的简要技术介绍，以促进认识和合作。 Crossplane、Score、Dapr、Rukpak、VCluster、Kratix、kcp 和 servicebinding.io 都在我们寻求分类功能和增加兼容性以最终降低平台工程师的复杂性并帮助他们成功的过程中进行了代表和讨论。

我在我们的聚会中分享了对云平台的一些必需功能进行分类的早期尝试，请在我们的 [Slack 频道](https://cloud-native.slack.com/archives/C020RHD43BP)中讨论它：

![](https://blog.joshgav.com/assets/platform_components.png)

## 值得注意的趋势

以下是我在 Kubecon 上注意到的与平台构建者相关的一些趋势：

1. **正在出现一些项目来帮助组合和抽象 Kubernetes 资源集合。** 大多数平台工程师乐于通过 YAML 清单使用 Kubernetes API 作为从他们的平台配置和管理服务和功能的基础；但大多数人希望为他们的产品开发人员提供对这些资源的简化抽象，只公开那些与他们的环境相关的参数。虽然 Helm 及其 values.yaml 文件已经提供了这样的范例，但已经出现了几个更高级的项目，允许平台工程师管理简化的 API：Crossplane 的 [Composite Resources](https://crossplane.io/docs/v1.9/concepts/composition.html)、Kratix 的 [Promises](https://kratix.io/docs/workshop/installing-a-promise) 和 Google 的 [kpt](https://kpt.dev/book/02-concepts/01-packages) 就是例子。

比较这些组合模式以及来自 Terraform、AWS Cloud Formation 和 Azure Resource Manager 的相关模型并一起向前迭代会很有帮助。

2. **服务目录正在出现，以收集和宣传精选服务。** 现代数字产品和服务依赖于平台的许多功能和服务，从块和对象存储到数据库、身份和监控系统。这些数字产品还可能使用其他业务线服务。 [kcp](https://docs.kcp.io/kcp/main/concepts/quickstart-tenancy-and-apis/#publish-some-apis-as-a-service-provider) 和 [kubectl-bind](https://github.com/kube-bind/kube-bind) 等项目使平台工程师可以通过 Kubernetes API 提供自我管理和提供商管理的服务，就像 pod、卷和网络网关一样。 [Ortellius](https://ortelius.io/) 等内部服务目录可以整理业务线服务。并且可以使用像 [Backstage](https://backstage.io/) 这样的门户来使所有这些服务易于查找、提供和按需观察。开发人员可以从目录中选择他们需要的服务并创建可重现的环境，甚至可以在像 [vcluster](https://www.vcluster.com/) 这样的虚拟集群中。

3. **服务绑定模式正在激增。** 随着通过 Kubernetes 提供额外的服务和功能变得越来越容易，用户需要在服务准备好后检索“绑定”信息的方法。服务“绑定”可以包括用于数据平面访问的 URL、用于授权的凭据以及用于日志和指标的端点。 Hashicorp 的 [Vault Agent](https://developer.hashicorp.com/vault/docs/agent/template) 及其 [secrets 引擎](https://developer.hashicorp.com/vault/docs/secrets)是获得此类绑定的一种方式，但也存在其他机制，如 Crossplane 的 [secrets 商店](https://github.com/crossplane/crossplane/blob/master/design/design-doc-external-secret-stores.md#api)和 [servicebinding.io](https://servicebinding.io/) 。许多工具将连接详细信息写入资源状态或命名的 Kubernetes Secret 或 ConfigMap，并要求用户阅读文档并了解每个工具的约定。

汇聚到一组标准的绑定生成器和标准位置以将此信息放入资源描述符和运行时环境中将很有帮助。

4. 基于 OCI 的构建和部署很受欢迎。现在有几个项目提供将容器镜像与 OCI（开放容器计划）包中的基础设施描述符捆绑在一起；这些包随后会被运行在 Kubernetes 集群中的自定义控制器检索、解绑和应用。示例包括 [porter](https://porter.sh/architecture/)、[acorn](https://docs.acorn.io/publishing)、Carvel 的 [imgpkg](https://carvel.dev/imgpkg/) 和 Operator Lifecycle Manager 的 [bundles](https://github.com/operator-framework/operator-registry/blob/master/docs/design/operator-bundle.md)。有价值的是，[rukpak](https://github.com/operator-framework/rukpak) 项目旨在提供一个包管理器，它通过 [Provisioner](https://github.com/operator-framework/rukpak/blob/main/docs/provisioners/overview.md) 支持许多不同的包格式。

如果能在像 Rukpak 这样的控制器中看到多种不同格式的 unbundlers 和 provisioners，那就太好了。

## 结论永久链接

云平台和平台团队承诺让云原生应用开发更高效；许多工具和模式正在出现，使平台构建者的工作更轻松。

我们在 CNCF 平台工作组中的下一项工作旨在通过定义云原生平台的关键组件来支持这些构建者。我们还将汇集类似组件类型的供应商，并寻求约定和模式以提高兼容性并使平台工程师更容易使用。加入我们