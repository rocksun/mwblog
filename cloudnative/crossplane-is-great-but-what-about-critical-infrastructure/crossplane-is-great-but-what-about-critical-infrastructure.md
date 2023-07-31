# Crossplane 很棒，但关键基础设施呢？

翻译自 [Crossplane is great, but what about critical infrastructure?](https://www.eficode.com/blog/crossplane-is-great-but-what-about-critical-infrastructure) 。

Crossplane 是 CNCF（云原生计算基金会）推出的一项有前景的工具，它利用 Kubernetes 的能力来管理组织的整个基础设施。通过提供持续的协调和声明式状态管理，它旨在简化基础设施的供应和管理。然而，当涉及到关键基础设施时，仍然有一些重要因素需要考虑。

## Crossplane 是什么？

Crossplane 是运行在 Kubernetes 内部的控制平面。

控制平面是一个概念/范式，指的是一个监视声明状态并确保系统的实际状态与声明状态相符的服务。换句话说，控制平面通过协调系统的当前状态来匹配所需状态。

![](https://www.eficode.com/hs-fs/hubfs/Eficode%202020%20site%20images/Blog%20images/CrossplaneDiagram.png?width=1500&height=750&name=CrossplaneDiagram.png)

Crossplane 通常用于提供和管理云资源。它承诺在云提供商中运行的资源与 Kubernetes 中声明的状态保持同步。

例如，开发人员可以将数据库声明为 Kubernetes 清单（YAML），并将其应用到安装了 Crossplane 的 Kubernetes 集群中。然后， Crossplane 将开始将声明的状态与云提供商中的数据库同步。要在 AWS 上创建数据库资源，开发人员需要创建以下内容：

```yaml
apiVersion: database.aws.crossplane.io/v1beta1
kind: RDSInstance
metadata:
  name: my-new-database
spec:
  forProvider:
    region: eu-central-1
    dbInstanceClass: db.t2.small
    masterUsername: masteruser
    engine: postgres
    engineVersion: '12.10'
    skipFinalSnapshotBeforeDeletion: true
    publiclyAccessible: true
    allocatedStorage: 20
  providerConfigRef:
    name: aws-provider-config
  writeConnectionSecretToRef:
    namespace: crossplane-system
    name: aws-database-conn
```

Crossplane 将读取上述 RDSInstance，并在 AWS 上创建具有这些规格的数据库。如果清单发生变化，Crossplane 将协调状态并相应更新数据库。如果从 AWS 管理控制台手动更改数据库实例，则 Crossplane 将自动还原这些更改以与 Kubernetes 中声明的状态匹配。

使用 Crossplane 进行基础设施管理使得可以同时在多个云提供商上提供资源，这可能是有益的，因为每个云提供商提供的服务不同。目前，Crossplane 支持 AWS、GCP 和 Microsoft Azure 作为云提供商。[DigitalOcean provider](https://www.digitalocean.com/blog/announcing-the-digitalocean-crossplane-provider) 也正在积极开发中。

## 为什么选择 Crossplane 而不是 Terraform ？

在基础设施即代码（IaC）方面，市场上有许多优秀的工具，Terraform 是其中最受欢迎的。Crossplane 和 Terraform 都试图通过允许您将整个基础设施描述为代码来解决相同的问题，但 Crossplane 在一些方面优于 Terraform ：

- Crossplane 轻松地与 GitOps 工作流程集成。
- Crossplane 将自动纠正漂移（即状态偏离所需状态）。
- Crossplane不需要存储状态。

通过使用自动化工具（例如 Atlantis ）或定期运行 terraform apply 的脚本（如 [Flux 的 tf-controller](https://weaveworks.github.io/tf-controller/) ），可以避免 Terraform 的配置漂移。

这样做实际上就创造了一个工作方式类似控制平面的系统。因此，与使用 Terraform 并在某种自动化工具/脚本中包装它相比，使用专门为解决此问题而构建的控制平面工具可能更好。

[只有当您有意暂停协调循环时](https://docs.crossplane.io/v1.10/concepts/managed-resources/#pausing-reconciliations)，Crossplane 才允许配置漂移；否则，只要 Crossplane 在运行，它就会持续同步状态。如果有人通过云提供商的用户界面手动更改云资源，Crossplane 将还原这些更改以与 Kubernetes 中声明的状态匹配。因此，如果您想更改云资源，必须通过 Crossplane 进行。

此外，如果您使用 ArgoCD 或 FluxCD 来管理 Kubernetes 资源，您可以将 Crossplane 资源检入 Git ，并从 Git 存储库中管理整个基础设施配置。这确保在 Git 中有一个审计轨迹，并使团队能够通过拉取请求（或团队可能已经使用的其他 Git 流程）来管理基础设施更改。

Terraform 的一个明显缺点是它的状态，它可能会丢失和损坏，这会导致如果使用它来管理整个基础设施，会产生复杂性。此外，您必须将状态存储在具有正确访问控制的远程位置；否则，整个团队将无法访问它，等等，这可能是麻烦和耗时的设置过程。

当应用更改时，Terraform 查看三个实体：您的本地 Terraform 文件、Terraform 状态和云提供商中的实际状态。如果云提供商中的状态偏离存储的状态，这可能会引起问题。

相比之下，Crossplane 只查看已声明的资源以及在云提供商中运行的内容。它不需要担心可变状态。

与 Terraform 一样，Crossplane 也使用 [provider](https://www.cncf.io/projects/crossplane/) 的概念。Crossplane-providers 的工作方式与 Terraform-providers 类似。服务提供商可以创建一个与 Crossplane 集成的插件，使用户能够在其基础设施上预留外部资源。现在由服务提供商负责管理和确保在其基础设施上运行的状态与 Kubernetes 集群中声明的期望状态相匹配。

## 为什么选择 Terraform 而不是 Crossplane ？

我们已经强调了 Crossplane 的优势，现在让我们看看它相对于 Terraform 的不足之处。

使用 Crossplane 的最大缺点之一是在应用更改之前无法预览这些更改。

使用 Terraform ，开发人员可以运行 terraform plan 命令，在提交新配置之前查看更改的预览。Crossplane 没有这样的功能，意味着无法预览它将创建/修改/删除的资源。开发人员只能应用清单，并希望他们做得正确。

举个例子，假设您如上面的示例中所示将 RDSInstance 重新命名。Crossplane 可能会删除现有的数据库，并使用新名称重新创建一个。这取决于 provider 的实现和您设置了什么样的保障措施，这使得 Crossplane 在处理关键基础设施时具有一定风险。这也在 [GitHub](https://github.com/crossplane/crossplane/issues/1805) 上有所描述。

## 在将更改合并到生产环境之前测试您的 Crossplane 更改

您可以通过在测试环境中测试来限制应用错误配置的风险。但是，值得注意的是，尽管测试环境应该尽可能接近生产环境，但它永远不会完全相同。

在使用 Crossplane 管理关键基础设施时，总会有破坏生产环境的风险。因为没有“计划”步骤让您在将更改应用于生产环境之前预览更改。

即使您可以在 Git 中撤销更改并返回到旧状态，它也不会恢复/重新创建已删除的生产数据库。但它会创建一个全新的（并非完全回滚的机制）。

## Crossplane 的未来

目前还不确定 Crossplane 是否将在未来添加预览功能或 “dry-run” 功能（在不更改任何内容的情况下运行新配置）。目前，有关此功能的讨论已经进行了[两年多](https://github.com/crossplane/crossplane/issues/1805)。我想象，对于控制平面来说，预览功能本质上是很难实现的，因为开发人员在流程的哪个阶段进行更改审查并不明显。

## Crossplane vs. Terraform

尽管 Crossplane 在许多方面优于 Terraform 和类似工具，但由于缺乏 dry-run/plan 功能，它在管理关键基础设施方面仍存在不足。

Terraform 的 `terraform plan` 命令允许开发人员在提交新配置之前查看和验证更改。该功能提供了额外的安全层，并有助于防止意外更改。

相比之下，Crossplane 不提供预览功能。在无法事先评估和验证更改的情况下，错误和对生产环境的干扰风险更大。

不要误会我的意思，我认为 Crossplane 是一个伟大的项目，我也是它的忠实支持者，但如果我运营一家公司，我会对将 Crossplane 用于关键核心基础设施感到犹豫不决。