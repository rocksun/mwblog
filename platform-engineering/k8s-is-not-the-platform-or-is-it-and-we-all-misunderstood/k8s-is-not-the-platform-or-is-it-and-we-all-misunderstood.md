<!--
# K8s不是平台——或者是我们都理解错了？
https://cdn.thenewstack.io/media/2023/10/307b32dd-yellow-lab-1024x683.jpg
Image from Joseph Gruber on Shutterstock.
图片来源:Joseph Gruber 在Shutterstock上的图片。
 -->

> 本文介绍了 Kubernetse 作为控制层面，通过 crossplane 可以发挥的作用。译自 [K8s Is Not the Platform – Or Is It and We All Misunderstood?](https://thenewstack.io/k8s-is-not-the-platform-or-is-it-and-we-all-misunderstood/) 。

关于Kubernetes和Crossplane作为开发者平台核心的探讨，超越了容器编排。



就在几年前，Kelsey Hightower还在KubeCon北美的主舞台上发言，说[Kubernetes只是一个底层工具](https://www.youtube.com/watch?v=07jq-5VbBVQ)，不是一个开发者平台。

那些构建内部平台来运行业务的公司，必须在Kubernetes之上构建抽象层和机制，来[减少开发者的认知负荷](https://roadmap.sh/kubernetes)。甚至如果做得好的话，Kubernetes会变得不可见，只是一个实现细节。

对我们这些深深投入Kubernetes和它巨大生态系统的人来说，最后这句话听起来有些牵强。如果这句话是真的，那我们最终会致力于让组件变得不可见。

而如今几年后，情况似乎我们都理解错了。Kubernetes无所不在，人们比以往任何时候都更倾向于用Kubernetes作为核心组件来构建平台。那么，到底发生了什么变化呢？让我们来探讨一下我们现在的状况，以及今天和过去有什么不同。

## 从容器编排到更多

Kubernetes最初是一个容器编排平台，首要目的是用于这一单一用例。但是在为开源社区构建最先进的[容器](https://thenewstack.io/containers/)编排器的同时，该项目并没有仅仅停留在编排Pod上。该项目在很早就在系统中构建了扩展点，最显著的是[自定义资源定义](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/)(CRD)。最初，CRD被用来通过辅助资源来扩展计算集群。比如配置资源、[CertManager](https://cert-manager.io/) CAs和CertificateRequests、第三方网络层像[服务网格](https://thenewstack.io/service-mesh/)等等。可能性是无限的，一个繁荣的生态系统在计算领域涌现出来。

但是自定义资源定义打开了通向更多可能性的大门。Kubernetes中的许多概念不仅限于容器编排。当被问及从Kubernetes中最可能持续存在的部分时，许多思想领袖都同意：对象模型和高度固执的CRUD API服务器模型可能会存在最久。

这意味着什么呢？这意味着从2015年Kubernetes 1.0发布以来，我们学到的远不止如何最高效地运行Pod。人们喜欢Kubernetes提供的API的统一性。人们喜欢可以使用一个工具，像kubectl，与不同的对象进行交互；一个GitOps工具用Kubernetes API语言来部署不同的资源；一个像controller-runtime这样的控制器库来为不同领域构建协调循环。你可以看到模式。

我们都还记得关于在Kubernetes上构建解决方案和使用CRD构建API的讨论在这些讨论中，有一个问题浮现：为什么是Kubernetes？任何其他的API机制也可以。这显然是正确的。但与此同时，你也可以问相反的问题：为什么不用Kubernetes及其丰富的生态系统中的API机制来构建平台，比如开发者平台?

这种讨论有点超出实际，并且很快就被现实所取代，人们正是这样做的。人们喜欢Kubernetes生态系统，喜欢围绕CRD和Kubernetes API构建的工具。他们熟悉这些工具，知道如何编写控制器。“那么其他的呢？”这个问题可以简单地回答说：“Kubernetes，因为我们有知识、有工具，使用它我们可以高效工作。”此外，[CNCF](https://www.cncf.io/)及其[所有项目](https://landscape.cncf.io/)拥有一个巨大的社区。

让我们看看如何用Kubernetes来构建每个企业今天都在追求的平台。Kubernetes的核心是API，一个可以对非常不同的对象执行CRUD操作的API，以统一的方式管理它们的生命周期。我们的意思是什么呢？Kubernetes为(集群范围和命名空间的)对象提供服务，称为资源。对象有一个我们都熟悉的通用形状：

```yaml
kind:
apiVersion: 
metadata:
    name:
    namespace:
    labels:
    annotations:
    ...
spec:
    ...
status:
    ...
```

这种通用的形状使通用解决方案成为可能，比如适用于Kubernetes集群提供的各种资源类型的GitOps解决方案。如果我们的开发者平台使用Kubernetes API的语言，所有这些工具就可以正常工作，并立即成为我们工具箱的一部分。

传统上，Kubernetes资源最终需要真正的代码，通常是Golang代码。尽管CRD可以用一堆YAML行声明式地定义，但实际逻辑需要真正的编程。编程意味着成本、维护和更多。这通常是平台构建者会避免拥抱的。

## 进入Crossplane时代

Kubernetes对象模型可以支持定义API逻辑的其他方式。[Crossplane](https://www.crossplane.io/)项目是一个很好的例子。Crossplane，另一个CNCF项目，诞生于2018年，从一个洞察力中诞生：Kubernetes API非常适合编排任意的云资源。在项目进行了一两年后，发明了一种叫做Compositions的概念。Compositions实现了一种Kubernetes中我们都熟悉的模式：想想[Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)、[ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)和[Pod](https://kubernetes.io/docs/concepts/workloads/pods/)。它们形成了一个层次结构：Deployment产生ReplicaSet，ReplicaSet产生Pod。Compositions实现了这种层次结构，定义实例如何展开成其他Kubernetes对象。

开发者平台需要更高层次的抽象来最小化开发者的认知负载。Deployment是Pod的一个抽象。在开发者平台中，想想BigCorp Application，一个BigCorp希望为其开发者提供的高度固执、高度定制的抽象：完全基于API。Crossplane使定义这种抽象变得非常简单，不需要写一行代码:

```yaml
apiVersion: apiextensions.crossplane.io/v1
kind: CompositeResourceDefinition
metadata:	
    name: xapplication.bigcorp.com
spec:
    group: bigcorp.com  
    names:
    kind: XApplication
    plural: xapplications
    claimNames:
    kind: Application
    plural: applications
    versions:
    - name: v1
    schema: ... # OpenAPI CRD schema
    storage: true
```

[复合资源定义( Composite Resource Definition)](https://docs.crossplane.io/latest/concepts/composite-resource-definitions/)(简称XRD)定义了一个带有复合语义的自定义资源定义。具体来说，[Composition](https://docs.crossplane.io/latest/concepts/composite-resources/)对象定义了命名空间Application[声明](https://docs.crossplane.io/latest/concepts/claims/)对象如何生成XApplication，在实例化时生成更多资源:

```yaml
apiVersion: apiextensions.crossplane.io/v1
kind: Composition
metadata:
    name: xapplication-webapp
spec:
    compositeTypeRef:
    apiVersion: bigcorp.com/v1
    kind: XApplication
    resources:
    - name: database
    base:
        apiVersion: sql.gcp.crossplane.io/v1beta1
        kind: Database  
        spec:
        ...
    - name: ingress
    base:
        apiVersion: kubernetes.crossplane.io/v1beta1
        kind: Object
        spec:
        forProvider:
            manifest:
            apiVersion: networking.k8s.io/v1
            kind: Ingress 
            spec:
                rules:
                - http:
                ...
    - name: deployment
    base:
        apiVersion: kubernetes.crossplane.io/v1beta1
        kind: Object
        spec:
        forProvider:
            manifest:
            apiVersion: apps/v1
            kind: Deployment
            spec:
                template:
                ...
```

![](https://cdn.thenewstack.io/media/2023/10/9e4d7c02-cncf-image2.jpg)

想象BigCorp中的一个开发者使用这个API，通过在公司网站的子域上部署新的客户反馈应用程序来创建一个实例：


```yaml
apiVersion: bigcorp.com/v1
kind: Application
metadata:
    name: customer-feedback
    namespace: marketing-team
spec:
    domain: feedback.bigcorp.com
```

复合资源定义(XRD)定义了这个API的模式。Composition `xapplication-webapp` 定义了域值最终如何进入入口定义中([通过Patch和Transforms](https://docs.crossplane.io/latest/concepts/patch-and-transform/)，非常像模板)。

Composition在这个例子中指定了两个普通的Kubernetes对象，但是也指定了一个用于云提供商数据库的基础设施资源。Kubernetes资源可以部署在与声明本身相同的Kubernetes集群上，也可以分布到其他集群，比如你的us-east1应用生产集群，或者欧洲的另一个集群。

请注意，`customer-feedback/marketing-team ` Application只是一个Kubernetes API对象，兼容生态系统中可用的所有工具。比如，平台团队希望对开发者可以对Application做什么进行限制。可以选择[Kyverno](https://kyverno.io/)、[OpenPolicyAgent](https://www.openpolicyagent.org/)或者[jsPolicy](https://www.jspolicy.com/)。财务团队希望降低云端花费，并将成本汇总到BigCorp的Application对象上，使应用程序所有者可以看到成本？可以选择[OpenCost](https://www.opencost.io/)或[KubeCost](https://www.kubecost.com/)。等等。

在所有这些平台工具到位的情况下，开发者将使用kubectl或首选的GitOps工具来创建BigCorp Application声明:

```shell
$ kubectl apply -f customer-feedback-app.yaml
```

对于Kubernetes来说，这只是另一个资源：Kubernetes将管理它的生命周期，定义它的API语义等。对于Crossplane来说，这是`xapplication-webapp`组合的一个实例。Crossplane从上面的Composition和XRD中知道如何赋予声明生命:

- Crossplane将创建一个复合XApplication。
- 它会为XApplication选择`xapplication-webapp`组合作为实现。
- 它会根据所选的组合，将XApplication展开成数据库、入口和部署对象。
- 它会在您选择的云提供商处创建SQL数据库。
- 它会将Kubernetes对象部署到同一集群或您选择的生产集群。
- 或者，它会使用Argo CD作为首选的GitOps工具自动安装并连接到您的应用程序git存储库，来创建另一个专用集群。
- 它会在公司的Backstage实例中注册该应用程序及指定的依赖项。
- 它会监视所有这些步骤的状态，并在BigCorp Application对象的状态中向开发者报告。
- 它会管理所创建的所有资源的生命周期。
- 当开发者决定删除应用程序时，它会拆除所有内容。

所有这些都没有代码。它发生在Kubernetes上，并可能涉及多个Kubernetes集群。它正在实现开发者平台的一部分。开发者平台不是Kubernetes，不是Kube作为容器编排器提供的抽象。但是开发者平台建立在Kubernetes技术和Kubernetes API以及控制器的语言之上。它实现了高级抽象。它为BigCorp提供了构建块的工具包和丰富的生态系统。

Kubernetes提供计算，仅作为副作用。BigCorp Application可以选择部署到某些其他计算服务上，例如通过为customer-feedback 应用程序创建一个 lambda.aws.crossplane.io/v1beta1 对象，而不是 Kubernetes 部署。计算只是开发者平台的一部分，对开发者可能是不可见的。计算只是Kubernetes的一部分，它作为基础来解决真正的业务问题有巨大的潜力。

那么我们现在处于什么状态呢？Kubernetes和像Crossplane这样的工具为我们提供了强大的平台构建工具箱。Kubernetes不是平台。我们误解了它的意思。Kubernetes容器编排对开发者来说不是一个即用的平台，甚至可能是不可见的或不被使用的。但是作为一种技术的Kubernetes比这更大，已经成为构建平台的首选语言。
