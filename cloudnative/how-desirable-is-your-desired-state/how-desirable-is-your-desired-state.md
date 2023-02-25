# 您理想的状态有多理想？

循环系统就是 Kubernetes 如何处理大量移动部件和不断变化的变量的持续变化，就像有人试图平衡太多的盘子一样。

![](https://cdn.thenewstack.io/media/2023/02/2eaa8e8c-woman-2-1024x662.jpg)

深入了解 Kubernetes，您很快就会遇到“期望状态”的概念。不，它与你的梦想工作、完美的云原生工具套件或你想要如何设计 Kubernetes 集群没有任何关系，如果你的意见很重要的话。

这个概念比这更简单：所需状态代表您希望应用程序和集群如何运行，而 Kubernetes“控制器”创建一个反馈循环以到达那里。尽管如此，云原生生态系统已经造成了文化和技术障碍，使您比以往任何时候都更难以实现您想要的状态。障碍如：

* 只有一些人对 Kubernetes 有足够的了解，可以在概念上或清单级别定义所需的状态。
* 理想状态会随着市场和客户（您拥有多少以及他们的期望）而变化。
* 所需的状态取决于您使用的云原生工具。一些公司仅使用 YAML，其他公司为他们的部署生成 Helm Charts 或使用 Kustomize 来区分环境。
* 它还取决于应用程序源代码、打包方式以及应用程序存储的数据。
* 随着您的组织的发展，您希望拥有对所需状态的每一次更改的历史记录，就像您对版本控制所做的那样——您如何以及为什么对所需状态进行这些更改。

所有这一切让我们想知道理想状态首先是多么可取。

## Kubernetes 中的“期望状态”是什么？

关于有助于区分当前状态和所需状态的控制回路，有一个常见的类比。当您将恒温器设置为特定温度时，您就建立了所需的状态。在 HVAC 设备的帮助下，恒温器的工作是将房间从当前状态（当前温度）调整到所需状态（设定温度）。恒温器反复循环检查更改循环以保持状态对齐。

在 Kubernetes 中，理想状态是您的基础架构或应用程序在运行后应如何运行。控制器是 HVAC 设备——所有让你从 0 到理想状态的神秘机器。您设置的温度就是您的配置。

在云原生世界中，所有这一切都是通过声明式方法发生的。您无需通过列出步骤来配置基础设施（称为命令式配置），您可以定义集群的每个部分应如何运行，并让 Kubernetes 担心脏工作。这也非常适合基础架构即代码 (IaC)，其中管理和配置您的基础架构是一个自动化的过程，而不是手动的过程。

> 在 Kubernetes 中，理想状态是您的基础架构或应用程序在运行后应如何发挥功能。

Kubernetes 控制器连续运行并跟踪关联对象（pod、服务等），寻找 YAML 配置中提供的 spec 字段（所需状态）和存储当前状态的 status 字段之间的变化。如果有变化，它会通过调用 API 服务器自动采取行动，进行所需的更改以缩小差距。

这个循环系统是 Kubernetes 如何处理大量移动部件和不断变化的变量的持续变化，就像有人试图平衡太多的盘子一样。例如，您的实际应用程序状态是应用程序镜像、Kubernetes 的期望状态和应用程序状态的混合，这些状态通常存储在集群本身之外的数据库中。

这种复杂性意味着您的集群通常不可能达到所需的状态，使其更像是一个白日梦，一个总是在移动的目标。

那么，你想要的状态取决于四件事：


* 代码及其运行所在的操作系统（作为镜像存储在容器注册表中）。
* 将镜像部署到 Kubernetes 所需的配置。
* 使用配置部署镜像的 CD 过程的输出，并在需要时进行修改。
* 存储在应用程序中的数据（通常在数据库中）。

## 容器注册表和您的清单

Kubernetes 控制器总是试图同步所需状态和实际状态，但您的应用程序状态还取决于其他因素。您正在处理的其中一个板块是您的容器注册表，它负责存储为您的容器和 pod 提供基础的所有镜像——您的整个基础设施。您的镜像将保存正在部署的代码的版本。

随着您的应用程序的发展或底层操作系统的变化，您的应用程序将不得不更新。这些更改通过您的 CI/CD 流水线移动到不同的环境中，这会生成新镜像。在容器中，镜像按设计“分层”，多个层构建在另一层之上以提供最终的容器使用。例如，您可以有一个基础层，即操作系统，您的应用程序在第二层上运行，或者您可以有更多层用于更复杂的应用程序。

> 所有这些编辑、调整和可能性都会对您的容器注册表产生现实影响，因为它会尝试提供使您的集群恢复到所需状态需要的镜像。

由于 Kubernetes（和现代软件开发风格）鼓励持续的应用程序部署，您可能会及时更改这两个层：

* 您将为您的应用程序所依赖的库/服务的新版本更新您的基础操作系统层。
* 您将更新应用程序层以获取应用程序本身的更新依赖项或新功能/错误修复。
Sometimes these changes are also driven by larger architectural shifts. For example, you need to change your database because your customer data is simply too large and is no longer performing adequately, and thus you need to change your desired state, which in fact might mean reckoning with additional tweaks to each layer of your images. Or, if you’re dealing with multiregional deployments, your images need to be configurable so pods are deployed evenly across your global infrastructure.
有时，这些变化也是由更大的架构转变驱动的。例如，您需要更改您的数据库，因为您的客户数据实在是太大了，不再能充分发挥作用，因此您需要更改您想要的状态，这实际上可能意味着需要对镜像的每一层进行额外的调整。或者，如果您正在处理多区域部署，您的镜像需要是可配置的，以便 pod 在您的全球基础设施中均匀部署。

And to manage all these image-level changes, you should be using specific labels to install a verified version of both the OS and application levels, instead of simply using latest and hoping for the best. Then, updating the image version is no longer automatically done by the controller after updates, so you need to trigger the update when you are ready.
为了管理所有这些图像级别的更改，您应该使用特定标签来安装操作系统和应用程序级别的经过验证的版本，而不是简单地使用 latest 并希望获得最佳效果。然后，更新图像版本不再由控制器在更新后自动完成，因此您需要在准备就绪时触发更新。

All these edits, tweaks and possibilities have real-world implications for your container registry as it tries to supply the images required to bring your cluster back to the desired state.
所有这些编辑、调整和可能性都会对您的容器注册表产生现实影响，因为它会尝试提供使您的集群恢复到所需状态所需的图像。