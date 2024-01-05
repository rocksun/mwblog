<!--
title: Argo可以走多远？
cover: https://cdn.thenewstack.io/media/2023/12/eb878ba9-argocd-simplicity-1024x681.jpg
-->

Kubernetes 持续交付工具的简单性，是优点还是缺点？

> 译自 [How Far Can You Go with Argo?](https://thenewstack.io/how-far-can-you-go-with-argo/)，作者 Joanna Wyganowska 是 Octopus Deploy 的营销副总裁。在她的角色中，她有幸与 DevOps 从业者讨论持续交付的最佳实践，以及从他们的 DevOps 之旅中吸取的教训。Joanna 是一位精益大师，并且......

从自芝加哥的 ArgoCon 返回后，我开始思考 Argo，尤其是 Argo CD 的未来。有两大阵营: 忠实的 Argo 粉丝致力于开源社区，以及更倾向于继续使用他们当前的部署工具并扩展其用于 Kubernetes 部署的人。这两种方法都有其优点。

[使用 Argo CD](https://thenewstack.io/argo-rollouts-how-intuit-does-blue-green-and-canary-deployments-on-kubernetes/) 进行 Kubernetes 持续交付的组织赞扬它的简单性。[VMware](https://tanzu.vmware.com/?utm_content=inline-mention) 的技术负责人 [Navneet Verma](https://github.com/papivot) 表示，Argo CD 提供了直观的图形用户界面(GUI)，由强大的命令行界面(CLI)和 API 支持。他还重视其处理多个集群的单一安装的能力。

## 太简单了？还是过于简单？

然而，许多人发现它过于简单。DeepOpinion 的首席后端开发者 [Diogo Baeder](https://github.com/diogobaeder) 说，Argo CD 缺乏允许开发人员部署特定版本的功能。相反，它依赖于应用程序规范中定义的内容。Codefresh 等公司看到他们构建在 Argo 之上的商业解决方案采用率增长的原因，是对已证实的部署模式的需求。

Octopus Deploy 的高级产品经理 [Nikita Dergilev](https://github.com/nikita-dergilev) 也有同感。在他看来，Argo CD 非常适合集群引导。它易于配置，首次部署会花费一点时间。然而，当团队需要跨许多环境或集群(如云区域)部署应用程序时，他发现使用 Argo CD 存在问题。痛点来自于需要管理许多 Git 仓库、分支或文件夹，并通过自制脚本或手动编排推进的需求。它很快就会变成一团糟。

另一个潜在问题是可扩展性。Dergilev 说，如果组织拥有许多集群、应用程序和团队，他们实际上有两种选择。第一个是集中化的 Argo 实例，这可能会变慢并引入权限和网络流量的问题。第二个是每个集群一个实例，这可能难以管理，并且无法提供单片玻璃来观察。他建议利用现有 DevOps 工具的功能来部署软件。例如，Octopus Deploy 提供了开箱即用的 Kubernetes 部署功能，包括环境推进和控制面板，可在所有项目和环境中查看 Kubernetes 部署。

## 关于 Argo 的战略性讨论

围绕使用 Argo 的讨论也在战略层面上进行，重点关注 Argo 的配置方法。这很好地体现在美国家庭保险公司的首席工程师 [Justin Pullen](https://www.linkedin.com/in/justinpullen/) 身上。他说，尽管他是声明式配置的忠实粉丝，但他看到的任何声明性项目的一个缺点是初始设置后的代码管理。

要对所有代码库进行任何广泛的更改，就需要越来越多的人手参与。Pullen 指出，这不是 Argo 或 [Kubernetes 部署](https://thenewstack.io/kubernetes/a-look-at-kubernetes-deployment/)声明所独有的。这是任何基于声明式语法的系统都会遇到的问题。

那么，如何快速在大规模上管理强制性更改？正如 Pullen 总结的那样: 答案尚不明确，但无论选择哪种解决方案，在大型企业中计划和执行到 Kubernetes 的部署时，都需要进行这方面的讨论。

我同意这种说法，因为这又是一次证明，重要的不是你选择使用的技术，而是你如何将当前的流程和人员整合到面向应用容器化的这种新的技术转变中。
