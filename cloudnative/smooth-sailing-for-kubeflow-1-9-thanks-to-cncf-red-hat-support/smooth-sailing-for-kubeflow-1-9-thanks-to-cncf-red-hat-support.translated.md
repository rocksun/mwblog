### 借助 CNCF 和 Red Hat 支持，KubeFlow 1.9 顺利发布

![KubeFlow 1.9 顺利发布，得益于 CNCF 和 Red Hat 支持的特色图片](https://cdn.thenewstack.io/media/2024/03/50b6aa8b-kubeflow-1024x680.jpg)

自去年以来，开源 [MLOps](https://thenewstack.io/mlops-needs-a-better-way-to-manage-gpus/) 平台 [KubeFlow](https://thenewstack.io/kubeflow-where-machine-learning-meets-the-modern-infrastructure/) 受益于许多强大的新支持者，包括开放治理的 [Cloud Native Computing Community](https://cncf.io/?utm_content=inline+mention) 和提供了大量工程帮助的 Red Hat。

下个月，用户将开始看到此支持的成果。计划 [发布](https://github.com/kubeflow/community/blob/master/releases/release-1.9/READM) 于 7 月 8 日，下一版本的 KubeFlow 将带来一个备受期待的模型注册表，该注册表基于 [Red Hat 的 Quay](https://thenewstack.io/red-hats-quay-3-container-supports-multiple-architectures/)。它还带来了使用 [CNCF Argo 项目](https://thenewstack.io/argo-cd-and-flux-are-cncf-grads-but-what-now/) 创建构建流以及修订的笔记本格式的能力。

[2018 年](https://thenewstack.io/kubeflow-manage-ai-workflows-with-kubernetes/) 首次亮相，KubeFlow 在 Kubernetes 上运行，因此可以在云中或内部服务器上运行。KubeFlow 在可用时使用现有的开源项目。组件包括用于实验的笔记本（基于 [Jupyter Notebooks](https://thenewstack.io/introduction-to-jupyter-notebooks-for-developers/)）、管道、用户控制台和训练操作员。

## Red Hat 为何对 KubeFlow 感兴趣？

就像 [OpenShift](https://www.openshift.com/try?utm_content=inline+mention) 基于 [Kubernetes](https://thenewstack.io/Kubernetes/) 容器编排器一样，Red Hat [Open Data Hub](https://opendatahub.io/) 也建立在 KubeFlow 之上，Red Hat 卓越工程师 [Jeremy Eder](https://research.redhat.com/blog/project_member/jeremy-eder/) 在接受 TNS 采访时指出。它还用于该公司商业支持的 [OpenShift AI](https://www.redhat.com/en/technologies/cloud-computing/openshift/openshift-ai)，该 AI 基于 Open Data Hub。

与公司软件组合的其他部分保持一致，Red Hat 并未在内部构建 MLOps 工具，而是采用了开源社区中已得到良好支持的软件，然后将工程帮助分配给上游。

虽然开源企业软件公司已经支持 Kubeflow 一段时间了——Red Hat 客户已经在 OpenShift 上运行 AI 和 ML 工作负载，部分原因是它支持 GPU——但 Red Hat [增加了投资](https://www.redhat.com/en/blog/open-source-ai-red-hat-our-journey-kubeflow-community)去年，当 KubeFlow 被转移到 CNCF 时，Eder 指出。

KubeFlow 1.9 将是第一个受益于 Red Hat 增加投资的版本，他说。

“我们已经开始运行了，”Eder 说。“几乎每个工作流中都有地面工程师的代表。”

## KubeFlow 1.9 有什么新功能？

Red Had 有很多客户在本地运行 AI 操作，因此，他们需要一个本地存储系统来构建和存储模型和其他构建工件。这是 Red Hat 为 KubeFlow 主导的第一个功能，一个用于保存模型和其他构建工件（例如数据集和指标日志）的注册表。

如果你运行一个 MLops 系统，你需要一个注册表，虽然你可以使用一个库存容器注册表，例如 [Red Hat Quay](https://quay.io/)，但“有细微的不同和重要的工作负载方式，我们希望它能专门迎合数据科学角色，”Eder 说。

此注册表实现了 [开放容器接口 1.1](https://thenewstack.io/how-bumblebee-eases-ebpf-observability-with-oci/) 标准，该标准也由 Quay 实现。注册表与 KubeFlow 管道集成，允许用户直接从注册表部署。

模型注册表将作为 alpha 版提供，尽管对于模型注册表应该如何工作仍有一些遗留问题。因此，一个新成立的工作组正在寻求用户社区的更多意见。

此版本将附带 Kubeflow Notebooks 2.0，它带有一对 Kubernetes 友好的自定义资源定义（Workspace 和 WorkspaceKind），以提供对工作空间的更多控制。

一旦用户在笔记本中完成实验，他们将能够将代码移到管道中，为软件的生产使用做好准备。

新版本还更新了 KubeFlow 管道。此功能最初是
[由](https://thenewstack.io/create-machine-learning-apps-in-your-notebook-with-tecton/) [Tecton Pipelines](https://www.reddit.com/r/kubernetes/comments/12x6f2b/is_tekton_still_alive_comparing_tekton_pipelines/)构建，随着 1.9 版本的发布，该管道还将支持 CNCF [Argo](https://thenewstack.io/how-far-can-you-go-with-argo/) 项目，以“与上游社区保持一致”，Eder 说。

“能够将你的操作参数表示为管道代码，从自动化的角度来看，这是非常有帮助的，”Eder 说。

管道功能将 KubeFlow 的两个用户联系在一起：数据科学家和机器学习工程师。

KubeFlow 社区一直在致力于的一个辅助项目是 [KServe](https://www.kubeflow.org/docs/external-add-ons/kserve/)，一个基于无服务器的推理前端，最近已从 KubeFlow 孵化器毕业，成为其自己的项目。最近已为 HuggingFace 和 vLLM 添加了开箱即用的运行时。

“KServe 将允许我们自动提供推理服务，”Eder 说，并补充说这是一个尚未完全解决的难题。

## KubeFlow 需要完成哪些工作？

在今年早些时候的 KubeFlow 峰会上，“[Kubeflow 的优点、缺点和缺失部分](https://www.youtube.com/watch?v=GbqwY-KZtjE)”，Red Hat 高级软件工程师 [Ricardo Martinelli de Oliveira](https://github.com/rimolive) 担任 Kubeflow 1.9 的发行经理，讨论了仍需要完成的工作。

在最近的一项用户调查中，KubeFlow 用户表示他们喜欢使用管道和笔记本，但希望这些功能具有更高的稳定性。在同一次调查中，用户抱怨安装薄弱——许多人从原始清单中安装。有发行版（例如 Red Hat 的发行版），但需要进行更多的符合性测试。有关可用发行版的文档已过时。一些组件几乎没有文档，或者根本没有文档。

“[安装文档] 的某些部分对用户来说看起来并不好，”Martinelli de Oliveira 承认。

未来，该项目还致力于达到成为 CNCF 毕业项目的标准。需要成立一个技术监督委员会，项目负责人正在考虑将软件移植到 ARM64 架构。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。