<!-- 
# 平台工程:从 Kubernetes API 学习
 -->


不要左移而要下移。为开发者简化困难的事情。从 Kubernetes 的流行及其 API 学习。

译自 [Platform Engineering: Learning From The K8s API](https://blog.hans-knecht.com/platform-engineering-learning-from-the-k8s-api-401424ca9946) 。本文所要表达的思想，其实已经在 crossplane 这些框架上已经体现了，Kubernetes 本身就是一个很好的平台工程的控制层面基础平台。


Richard Seroter 最近发表了一篇题为《[The Modernization Imperative: Shifting left is for suckers. Shift down instead](https://cloud.google.com/blog/products/application-development/richard-seroter-on-shifting-down-vs-shifting-left)》的文章。这是一篇非常棒的文章，探讨了开发者在过去十年随着DevOps和云计算席卷科技界所经历的许多问题。开发者被要求掌握越来越多知识，提高了他们使用开发平台的认知复杂度。Heroku这样的平台深受开发者喜爱就不难理解了！它们通过简化部署做得非常出色。

随着Kubernetes(K8s)平台的兴起，团队终于有了一个绝佳的机会和工具，可以通过将服务所需的一切放在K8s API后面来降低开发者的认知复杂度。正如《[Building a Successful SRE Team](https://medium.com/@hans.knechtions/building-a-successful-sre-team-283232bc2694)》一文中讨论的，专注于自助服务对扩展平台团队至关重要。如果不这样做，随着每个开发团队的增加，你最终不得不线性扩展人员，而不是让团队自主上线，从而支持大量更多的工程师。专注于自助服务还带来其他好处，它对使开发者满意和释放平台潜力也至关重要。为什么说K8s API模型是自助服务的关键所在？因为它提供了以下关键特性：

- 它是幂等的。提交相同的对象两次不会导致两个对象，只会导致一个对象。
- 它是声明式的。工程师不需要编写长长的命令式步骤来实现特定的结果，他们只需要描述想要什么，其他的问题就让编排器来处理。
- 它鼓励容错。这并不意味着在K8s上部署的每个应用本身就是容错的，任何试图部署切换应用的人都知道这不是真的。相反，K8s API和模型简单地要你失败后重试，直到操作成功。如果一个pod无法启动，kubelet不会停止尝试，而是会一直重试，直到成功，即使在不进行干预的情况下这种条件可能永远不会变为true。
- 它管理协调。我非常喜欢Terraform。我写过很多Terraform代码。我也[写过](https://medium.com/capital-one-tech/treating-your-terraform-like-an-application-why-terraform-in-a-docker-container-31e802314b4)[许多](https://medium.com/capital-one-tech/treating-your-terraform-like-an-application-how-to-dockerize-terraform-5d7edac741fc)关于[Terraform的文章](https://medium.com/capital-one-tech/terraform-poka-yokes-writing-effective-scalable-dynamic-and-error-resistant-terraform-dcbd6a0ada6a)。Terraform的最大缺点是会漂移。使用Terraform管理漂移尤其是在无法锁定云环境中手动更改的情况下几乎是不可能的。在K8s世界中情况并非如此。如果有人手动删除了一个pod，K8s可能会将其重新创建。
- 它鼓励GitOps。在K8s中管理2-3个应用程序之后，你会看到GitOps的价值所在，特别是如果不止一个人帮助管理它们的时候。有人会忘记提交helm chart的values.yaml或deployment/service的修改，然后其他人随后编辑它，从而破坏你的资源，因为更改从未被提交或管理。与其手动进行更改，不如使用像ArgoCD或Flux这样的工具实现单一信息源来描述基础设施。
- 它允许构建operator。如果你只使用过K8s作为容器编排引擎，可能没有意识到operator模式的强大功能。它允许注册自定义资源、监视任何资源的更改以及通过内置的扇出队列对这些资源采取行动，实现的自定义程度远远超出任何人的想象。在K8s上管理Elasticsearch与在ECS或EC2上管理之间的不同程度和支持需要是如此之大，以至于这简直令人难以置信。在K8s上，你可以使用Elastic Operator，它处理管理ES约90%的所有痛点。如果在其他地方完成，你必须自己编写所有自动化、托管它们的位置、订阅事件等。

扩展所有这些优势使我们拥有了诸如[Config Connector](https://cloud.google.com/config-connector/docs/reference/overview)(面向GCP)和[Crossplane](https://www.crossplane.io/)(与云无关)之类的工具，以便我们甚至可以设置存在于K8s集群之外的所有其他服务基础设施部件。这些工具允许平台团队让开发人员使用单一API与服务所需的所有基础设施进行交互。服务需要一个数据库吗？使用CNRM建立一个Cloud SQL实例。团队需要将Pagerduty服务连接到他们的K8s服务吗？使用Crossplane的terraform provider。允许团队只通过单一API设置所有资源是非常强大的，并为开发者的成功奠定了基础。

但是好处并不止于此。从平台团队的角度来看，要求通过K8s API创建服务资源允许你构建一致的工具来管理创建和审批流程。

你是否希望应用策略以防止创建某些资源，要求某些元数据，限制可以创建资源的位置或要求特定的命名模式？使用一个准入控制器，如[Kyverno](https://kyverno.io/)或[OPA Gatekeeper](https://github.com/open-policy-agent/gatekeeper)就可以实现。如果可以[在K8s中使用CEL](https://kubernetes.io/docs/reference/using-api/cel/)，则甚至可能不需要它。好处是你不必为K8s资源编写一个流水线，为Terraform/Cloud Formation/CDK编写另一个流水线。作为平台团队，你为一个API编写一致的工具集，这允许你为任何策略构建有效的RBAC和测试，限制更改的范围和影响，并利用K8s API的所有优势。

作为平台团队，你是否想编写抽象以确保服务团队创建的资源的一致性？你是否想提供明智的、固执己见的默认值？你是否想管理依赖关系的单一集合升级？然后选择你最喜欢的K8s包管理器([helm](https://helm.sh/)、[jsonnet](https://jsonnet.org/)、[kustomize](https://kustomize.io/))并大展身手！编写一组可组合的charts，让开发人员可以轻松启用和关闭服务所需的基础设施。他们可以从一开始就以安全的配置方式获得它，而要获取新功能，他们只需要升级chart版本，甚至还有[自动化工具](https://github.com/renovatebot/renovate)可以完成此操作！

这不仅仅是我在吹捧K8s的优点。我看到这在Mission Lane非常成功。我们拥有250多种使用Mission Lane服务Helm Chart的微服务。我们用一个非常小的基础设施团队支持200多名开发人员。该 Chart 允许你建立一个简单的部署、服务和虚拟服务。但是如果你需要一个数据库，它会使用CNRM在你的项目中创建一个Cloud SQL实例，启动一个Cloud SQL代理，配置IAM和GCP/K8s服务帐户，所有这些只需要三行yaml。当然，也有大量的自定义机会。开发人员可以覆盖几乎任何设置，但是大多数人不需要这样做。他们可以立即获得一个安全配置的数据库。GCS存储桶、Redis实例、使用[Flagger](https://flagger.app/)的金丝雀发布、Istio配置、open telemetry边车等也是如此，所有这些都来自helm chart，并允许团队快速从POC转变为完全生产化的服务。

将开发者不需要交互的堆栈部分抽象出来，在服务所需的基础设施方面提供有益的固执己见，并采用单一API和开发者交互的心智模型，会使你的平台团队从仅仅高效，从良好跃升到卓越，从是一个有用的、有贡献的团队成长为是一个对组织的力量倍增器。

你甚至不必使用K8s API，可以使用Nomad或自制API。但你至少应该从K8s API所做的非常出色的工作中吸取教训，因为它的使用不仅仅是盲从，它提供了令人难以置信的自动化效果。
