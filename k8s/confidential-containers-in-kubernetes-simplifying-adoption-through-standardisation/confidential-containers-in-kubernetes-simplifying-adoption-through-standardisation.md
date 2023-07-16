# Kubernetes 中的机密容器

*通过标准化简化采用过程*

翻译自 [Confidential Containers in Kubernetes](https://itnext.io/confidential-containers-in-kubernetes-simplifying-adoption-through-standardisation-75c28bfce5e9) 。

![](http://yylives.cc/wp-content/uploads/2023/07/cover-1.jpg)

## 介绍

对于处理敏感数据的组织来说，机密计算变得越来越重要。随着 Kubernetes 的普及，通过在容器工作负载的 Pod 层面标准化机密计算将使用户受益。云原生计算基金会（CNCF）的 [Confidential Containers（CoCo）](https://github.com/confidential-containers) 项目旨在通过提供标准化的方法在 Kubernetes 上部署机密容器工作负载来满足这种需求。在本文中，我们将探讨这种标准化方法的好处，以及 CoCo 项目如何为使用机密计算的新业务工作负载提供基础。

## 为什么标准化有助于采用？

标准化在任何技术的广泛采用中起着关键作用。对于 Kubernetes 中的机密计算而言，标准化带来了多重好处：

1. **互操作性**：标准化确保不同的机密计算技术实现可以无缝地协同工作。它允许用户在保证兼容性和减少供应商锁定的同时，从多个提供商中进行选择。
2. **部署简易性**：标准化通过提供一致且熟悉的框架简化了部署。 Kubernetes 用户可以利用现有的工作流程和工具，无需深入了解底层机密计算技术。
3. **安全性**：标准化加速并有助于安全评估和审核，增强了采用这些技术的组织的信心。
4. **社区合作**：标准化促进了社区内的合作，允许专家们共同努力，共同开发最佳实践、指南和工具。这种合作努力推动创新，并确保机密计算技术的持续改进。

最终，从技术中获得业务效益应该是一种无聊的部署和维护过程。这就是 CNCF CoCo 项目的整个前提。

## 对 CNCF CoCo 项目的简要介绍

CoCo 项目为使用基于虚拟机（VM）或进程的可信执行环境（TEE）在 Kubernetes 上部署机密容器提供了一个共同的基础。CoCo 项目旨在使用户能够在任何 Kubernetes 集群上以最小的变更运行机密容器，而无需改动现有的应用程序和工作流程。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*-VHiUR0E7m3q5wpTxdCyTw.png)

CoCo 项目提供了**三**种不同的方法来部署和管理机密容器，以适应广泛的机密计算环境：

1. **使用基于 VM 的 TEE 在本地虚拟机监视器上部署机密容器**
2. **使用基于 VM 的 TEE 在远程虚拟机监视器上部署机密容器**
3. **使用基于进程的 TEE 部署机密容器**

此外，CoCo 项目提供了一种远程证明 TEE（和工作负载） 的标准机制，使用证明代理和密钥代理服务。

让我们简要了解一下这**三**种部署方法和远程证明。

**使用基于 VM 的 TEE 在本地虚拟机监视器上部署机密容器**

这种方法主要需要支持 AMD SEV、Intel TDX 或带有 QEMU 的 IBM SE 等裸机 Kubernetes 工作节点。下图显示了架构概述图。

支持机密计算的 **Guest Components**、**Key Broker Service**、**Attestation Service** 和  **Kata 运行时**通过 CoCo 项目提供，并在不同的方法中共享。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*7ss3GX6C65JGckhzoW2sMg.png)
*使用本地虚拟机监视器在 Kubernetes 工作节点上部署机密容器*

**使用基于 VM 的 TEE 在远程虚拟机监视器上部署机密容器**

这种方法也称为 peer-pods 方法，它依赖于 Kata Containers 的远程虚拟机监视器支持和 CoCo [cloud-api-adaptor](https://github.com/confidential-containers/cloud-api-adaptor/) 项目。这种方法可以在任何 Kubernetes 集群上工作，而无需为工作节点提供机密计算硬件。它使用公共云或第三方基础设施即服务（IaaS）提供商提供的机密虚拟机服务。下图显示了这种方法的高级架构。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*tYtHJgItHIFoN-I9r8EkSA.png)
*在与Kubernetes工作节点无关的远程虚拟机监视器上部署机密容器*

**使用基于进程的 TEE 部署机密容器**

这种方法需要具备 Intel SGX 支持的 Kubernetes 工作节点，并使用 CoCo [enclave-cc](https://github.com/confidential-containers/enclave-cc) 项目。下图显示了高级架构概述。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*vAVg0daUIhzgD_jPNgpUow.png)
*使用基于进程的TEE部署机密容器*

正如您所看到的，根据您选择的机密容器部署和管理方法，CoCo 项目提供了构建块。

**CoCo 中的远程证明**

远程证明是一种机制，允许在机密计算环境中运行的软件组件向外部的受信任服务证明其可信性。它涉及生成和验证一组关于系统和软件堆栈状态的声明，这些声明由硬件密钥签名。

Confidential Containers（CoCo）项目遵循 [IETF Remote Attestation Procedures（RATS）](https://datatracker.ietf.org/doc/rfc9334/) 的规定，如下图所示：

![](https://miro.medium.com/v2/resize:fit:640/format:webp/0*8mjCB6rLlD0gTnf3.png)

**Attester** 是生成并发送**证据**给受信任服务的组件，该服务充当**依赖方**。CoCo 项目实现了作为 Kubernetes Pod 的 **Attester** 的 [attestation-agent](https://github.com/confidential-containers/guest-components) 。 Attester 需要从依赖方获取密钥以解密或验证组成 Pod 的容器映像。 Attester 还可以用于获取部署在 Pod 中的工作负载的密钥。

**Key Broker Service (KBS)** 是充当 Attester 的依赖方的受信任服务。它使用 Attestation Service 对证据进行验证，将其与参考值和策略进行比较。如果验证成功，它将从密钥管理服务中检索密钥并将其发送回 Attester 。 KBS 确保只有可信任的 Attester 可以访问密钥并运行 Pod 工作负载。 CoCo 项目提供了一个 [KBS](https://github.com/confidential-containers/kbs) 实现。

有关证明过程的更多详细信息，请参阅我之前的[博客](https://pradiptabanerjee.medium.com/understanding-attestation-process-in-a-confidential-computing-solution-ef8f876f34eb)。

## CNCF CoCo 项目如何帮助？

CoCo 项目的目标是在 Kubernetes Pod 层面为机密计算建立一个标准。它通过利用可信执行环境（TEE）来保护容器和数据来实现这一目标。通过使用 CoCo ，在 Kubernetes 中使用机密计算变得更加容易。

利用 CoCo 项目进行机密容器使用的几个好处如下：

1. **简化部署**：CoCo 项目提供了一个 Kubernetes 操作员，可以快速在 Kubernetes 集群上建立机密容器环境。这消除了复杂的手动配置需求，使用户能够专注于应用程序而不是底层基础设施。
2. **增强安全性**：组织可以自信地部署敏感工作负载，知道它们在 TEE 中得到了良好的保护。在 Kubernetes 工作负载中使用 TEE 为您的深度防御策略提供了额外的保护。
3. **简化工作流程**：通过 CoCo 项目，您可以将机密计算无缝集成到现有的 DevOps 工作流程和工具链中。您可以继续使用熟悉的 Kubernetes 工作流程，利用机密计算功能部署容器工作负载。
4. **活跃社区**：作为 CNCF 项目， CoCo 受益于积极而充满活力的云原生社区。用户和开发人员参与每周会议，贡献代码，报告问题，并在项目的发展中进行合作。这种积极的社区参与确保了标准化机密计算解决方案的持续改进和维护。

## 结论

在 Kubernetes 的 Pod 层面对机密计算进行标准化带来了众多好处，包括互操作性、部署简易性、增强安全性和社区协作。

云原生计算基金会（CNCF）的 Confidential Containers（CoCo） 项目旨在通过提供一个标准化和熟悉的框架，简化在 Kubernetes 中使用机密计算。CoCo 项目有望对机密计算产生重大影响，因为它使组织能够安全地执行敏感工作负载并利用机密计算的能力，即使对底层技术了解不深。

通过接受标准化，行业更接近一个未来，其中机密计算成为一种广泛接受的实践，实现了新的工作负载，并确保敏感数据的安全处理和保护。

请考虑加入社区，并为容器工作负载的机密计算的发展做出贡献。您可以参加我们的[每周会议](https://docs.google.com/document/d/1E3GLCzNgrcigUlgWAZYlgqNTdVwiMwCRTJ0QnJhLZGA/)。此外，您可以加入 [Slack](https://slack.cncf.io/) 上的 **#confidential-containers** 频道进行讨论。