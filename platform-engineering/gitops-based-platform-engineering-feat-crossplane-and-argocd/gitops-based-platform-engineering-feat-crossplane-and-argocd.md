
<!--
title: 基于GitOps的平台工程：Crossplane与ArgoCD实战
cover: https://hashnode.com/utility/r?url=https%3A%2F%2Fcdn.hashnode.com%2Fres%2Fhashnode%2Fimage%2Fstock%2Funsplash%2F9v1cuPQ5hKM%2Fupload%2Fbce9e496c42c0edc83e584db1fe16375.jpeg%3Fw%3D1200%26h%3D630%26fit%3Dcrop%26crop%3Dentropy%26auto%3Dcompress%2Cformat%26format%3Dwebp%26fm%3Dpng
summary: Crossplane结合ArgoCD，通过抽象和自助服务，简化了云基础设施（如EKS）的管理与创建，提升开发效率和成本效益。
-->

Crossplane结合ArgoCD，通过抽象和自助服务，简化了云基础设施（如EKS）的管理与创建，提升开发效率和成本效益。

> 译自：[GitOps based Platform Engineering feat. Crossplane and ArgoCD](https://srujanpakanati.com/gitops-based-platform-engineering-feat-crossplane-and-argocd)
> 
> 作者：Srujan Reddy

如果你仔细想想，一生中总会有一次重大发明，深刻地影响我们做事的方式。直到20世纪90年代末，我们都在实体店购物，然后互联网的出现带来了电子商务。现在随着AI现象，我们的购物方式再次改变。每一次重大创新都会带来小的流程改进，给我们提供选择。

自互联网问世以来，我们一直在提供基础设施。首先，曾有实体硬件，你需要采购并手动设置，然后在上面运行软件。然后出现了云，它带来了Terraform、CF等IaC工具。这是对现有流程的改进。你可以根据需要快速设置基础设施，而不是进行手动点击操作（clickOps），但也存在许多缺点，如随时间推移的配置漂移、状态文件管理等。但随后Kubernetes出现了……

Kubernetes的日益普及催生了大量新的云原生工具，这些工具在现有工具和应用程序的基础上提供了一些流程改进。Crossplane就是这样一种工具，它提供了更好的基础设施创建和管理方式。它防止了配置漂移，并允许我们创建抽象以实现自助服务。这有助于我们左移，让开发人员可以按需配置和管理所需的基础设施。这里有一篇X帖子对比Crossplane和Terraform之间的区别：

- https://x.com/ianmiell/status/1788973776996028813

在本文中，让我们快速了解Crossplane中使用的基本术语。它有5个主要组件

[复合资源(XR)](https://docs.crossplane.io/latest/composition/composite-resources/) - 它可以定义为一堆不同的资源打包成一个资源。如果你的应用程序需要IAM角色、策略和S3存储桶来访问该存储桶，那么这三个资源可以组合成一个XR。

[复合资源定义(XRD)](https://docs.crossplane.io/latest/composition/composite-resource-definitions/) - 复合资源定义（`XRDs`）定义了自定义API的 schema。用户使用XRD定义的API schema创建复合资源（`XRs`）。

[组合](https://docs.crossplane.io/latest/composition/compositions/) - 组合包含XR请求创建的实际内容的定义。它包含了所有逻辑。

[提供者](https://docs.crossplane.io/latest/packages/providers/) - Crossplane提供者是扩展，使Crossplane能够管理外部服务（如云提供商）上的基础设施和资源。可以将它们视为连接Kubernetes集群与第三方API的桥梁。

[函数](https://docs.crossplane.io/latest/packages/functions/) - 函数使你能够根据XR动态填充资源。你可以使用不同的*组合函数*来配置当有人创建或更新[复合资源(XR)](https://docs.crossplane.io/latest/composition/composite-resources/)时Crossplane执行的操作。

这是来自Crossplane文档的图片，可以更好地理解它们是如何工作的

[![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757537067976/2133e350-02ca-4e0c-bd8b-98e8c3c766b7.png?auto=compress,format&format=webp)](https://docs.crossplane.io/latest/composition/composite-resources/)

在基于GitOps的方法中使用Crossplane和ArgoCD的原因是Git管理着提交历史，因此你可以快速查阅对任何Crossplane资源所做的更改。ArgoCD可以帮助你可视化正在创建的基础设施，并允许你设置同步波次等。除了这里提到的，还有更多好处，但你应该明白我的意思。

## Crossplane实战

> 本博客中使用的[GitHub仓库](https://github.com/HighonAces/crossplane-argocd#)在这里

我们来设想一个场景，开发团队需要新的EKS集群进行一些测试。通常，这些请求会通过Jira提交给DevOps团队，DevOps团队根据他们的规范创建集群并交付给他们。这带来了很多摩擦，因为开发团队不想让运维团队在周末关闭集群，因为他们周一又要再次提交Jira，并且不得不等待集群再次创建。如果我们让开发团队根据需要创建集群，但又不想处理HCL或VPC、子网等低级组件，该怎么办？

以下是作为开发人员平台的EKS集群的构建模块。

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757536041748/b80cc3df-4700-4e16-b313-fe2175cd2d9c.png?auto=compress,format&format=webp)

首先，开发团队必须创建所需的网络，以便在其上部署EKS集群。因此，他们会将eksnetworking XR文件推送到指定的GitHub仓库中：

```yaml
apiVersion: srujanpakanati.com/v1alpha1
kind: EKSNetwork
metadata:
  name: my-eks-network
  namespace: default
spec:
  parameters:
    region: us-east-2
    networkType: "dev"
    vpcCidrBlock: "10.0.0.0/16"
    availabilityZones:
    - "us-east-2a"
    - "us-east-2b"
    publicSubnetCidrBlocks:
    - "10.0.1.0/24"
    - "10.0.2.0/24"
  crossplane:
    compositionSelector:
      matchLabels:
        provider: aws
        workload: eksnetwork
```

使用这个XR，开发团队能够配置区域、CIDR范围、子网数量等。然而，在所需参数以及如何输入等方面，它受到了严格的限制。这由复合资源定义（XRD）控制。你可以在下面看到所需的章节和枚举。

```yaml
apiVersion: apiextensions.crossplane.io/v2
kind: CompositeResourceDefinition
metadata:
  name: eksnetworks.srujanpakanati.com
spec:
  scope: Namespaced
  group: srujanpakanati.com
  names:
    kind: EKSNetwork
    plural: eksnetworks
  versions:
  - name: v1alpha1
    served: true
    referenceable: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          spec:
            type: object
            properties:
              crossplane:
                type: object
                properties:
                  compositionSelector:
                    type: object
                    properties:
                      matchLabels:
                        type: object
                        additionalProperties:
                          type: string
              parameters:
                type: object
                properties:
                  networkType:
                    type: string
                    description: "The type of network to provision."
                    enum:
                    - "dev"
                    - "prod"
                  region:
                    type: string
                    description: "AWS region to provision the network in."
                  vpcCidrBlock:
                    type: string
                    description: "CIDR block for the VPC."
                  availabilityZones:
                    type: array
                    description: "List of Availability Zones to create subnets in."
                    items:
                      type: string
                  publicSubnetCidrBlocks:
                    type: array
                    description: "List of CIDR blocks for public subnets. Must match the number of AZs."
                    items:
                      type: string
                  privateSubnetCidrBlocks:
                    type: array
                    description: "List of CIDR blocks for private subnets. Must match the number of AZs."
                    items:
                      type: string
                required:
                - region
                - vpcCidrBlock
                - availabilityZones
                - networkType
          status:
            type: object
            properties:
              vpcId:
                type: string
              publicSubnetIds:
                type: array
                items:
                  type: string
              privateSubnetIds:
                type: array
                items:
                  type: string
              clusterSecurityGroupId:
                type: string
```

现在，组合是配置所有所需资源的地方。它使用一个或多个函数来获取XR中给定的值以创建资源。KCL是流行的首选语言，但你也可以使用go-template或Python。这里是所使用的[组合](https://gist.github.com/HighonAces/46e348b57481800f854605d6e3cc7a1a)。

请记住，XRD和组合必须始终由运维团队拥有，他们规定了XR如何创建以及将作为其一部分创建哪些资源。以下是ArgoCD中已创建资源的快速截图

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757537977592/a878a327-edec-4974-91e0-6f6308f7d3d4.png?auto=compress,format&format=webp)

这让人们对正在创建的资源以及XR的整体健康状况有了全面的了解。现在你已经有了网络，接下来可以创建EKS控制平面。它也遵循类似的创建XRD和组合的模式。以下是供参考的ekscluster XR

```yaml
apiVersion: srujanpakanati.com/v1alpha1
kind: EKSCluster
metadata:
  name: my-eks-cluster
  namespace: default
spec:
  parameters:
    clusterName: my-eks-cluster
    region: us-east-2
    kubernetesVersion: "1.33"
    accessList:
      - name: developer-role
        roleARN: "arn:aws:iam::xxxxxxxxx:role/eks-dev-role-to-test-crossplane" 
        policies:
          - "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
          - "arn:aws:iam::aws:policy/AmazonEKSServicePolicy"
    addons:
      - name: vpc-cni
        version: "v1.20.1-eksbuild.3"
      - name: coredns
        version: "v1.12.3-eksbuild.1"
      - name: kube-proxy
        version: "v1.33.3-eksbuild.6"
    vpcId: "vpc-07ddbab7b7c6a6fef" 
    subnetIds:
      - "subnet-0c7420944a320ddff" 
      - "subnet-095925a4561365bf5"
  crossplane:
    compositionSelector:
      matchLabels:
        provider: aws
        workload: ekscluster

```

在这里，我们可以看到组件在ArgoCD中实时创建

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757618940319/7143a6ba-4124-43f3-a4bb-2184ecc6fe48.png?auto=compress,format&format=webp)

一旦控制平面创建完毕，我们就可以继续创建NodeGroup。以下是我的nodegroup XR

```yaml
apiVersion: srujanpakanati.com/v1alpha1
kind: EKSNodeGroup
metadata:
  name: my-nodegroup
  namespace: default
spec:
  parameters:
    clusterName: cluster-my-eks-cluster 
    region: us-east-2
    nodeGroupName: my-managed-nodes
    instanceTypes:
      - "t3.medium"
    scalingConfig:
      minSize: 1
      maxSize: 3
      desiredSize: 2
    subnetIds: 
      - subnet-0c7420944a320ddff
  crossplane:
    compositionSelector:
      matchLabels:
        provider: aws
        workload: eksnodegroup

```

这是ArgoCD中的相同XR。

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757621184804/0a215c73-c3d2-4ca6-8e86-acf0f99d2d6b.png?auto=compress,format&format=webp)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757621834599/9a5cfae0-0999-41fd-ab1a-3d433e2fbeb2.png?auto=compress,format&format=webp)

如果现在我们退后一步，看看我们创建了什么，我们不仅创建了一个集群和节点组。我们还创建了一个模板，可以根据需要创建任意数量的集群。0→1已经完成，现在1→n就很容易了。这不仅仅是新的控制平面，你还可以将节点组添加到现有的EKS集群中。通过这种方式，我们可以为开发团队创建自助服务平台，从而防止与基础设施相关的瓶颈。

## 结论

Crossplane和ArgoCD是云原生时代不可或缺的工具。团队以周期性迭代，这些工具在迭代周期中提供了显著的改进，进一步提升了开发人员体验和成本效率。回报将是多方面的，最令人兴奋的是这些工具都是开源的。如果你的工作负载运行在Kubernetes上，那么是时候采用适合这项工作的工具了。