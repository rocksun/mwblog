Kubernetes的第二春？为什么谷歌要将Anthropic和OpenAI都在使用的代码沙箱gVisor拱手让人

谷歌希望复制其历史上最成功的开源传奇之一，将三个核心的AI智能体基础设施项目捐赠给一个中立基金会，希望它们能像[当年Kubernetes对容器所做的那样](https://techcrunch.com/2015/07/21/as-kubernetes-hits-1-0-google-donates-technology-to-newly-formed-cloud-native-computing-foundation-with-ibm-intel-twitter-and-others/)，成为行业标准。

在周四发表的一篇[博客文章](https://cloud.google.com/blog/products/containers-kubernetes/open-infrastructure-for-autonomous-agents-comes-to-cncf)中，谷歌负责Kubernetes和编排的产品管理副总裁[Drew Bradstock](https://www.linkedin.com/in/drew-bradstock-2002732/)证实，该公司正将[gVisor](https://gvisor.dev/)、[Agent Substrate](https://ate.dev/)和[OpenRL](https://openrl.dev/)捐赠给云原生计算基金会（CNCF）。

此举出台之际，外界对自主AI智能体的安全性日益担忧，尤其是它们执行代码和与外部系统交互的能力。7月份，在OpenAI接受网络安全评估的模型[逃离了其受限环境并突破了](https://thenewstack.io/openai-huggingface-sandbox-breach/)Hugging Face的生产基础设施，这凸显了将日益强大的智能体限制在安全边界内的挑战。

> “我们相信，通过这些项目，这些捐赠将加速智能体工作负载的开发和采用，就像我们当年在Kubernetes上看到的一样。”

就Bradstock而言，他认为应对此类安全风险，同时让智能体的运行和训练更具经济效益，需要底层软件和硬件基础设施的各个方面进行更紧密的合作。他相信，将其技术置于中立治理之下可以鼓励全行业参与，正是这种参与帮助Kubernetes变得无处不在。

Bradstock写道：“我们相信，通过这些项目，这些捐赠将加速智能体工作负载的开发和采用，就像我们当年在Kubernetes上看到的一样。”

## 为什么谷歌要捐出 gVisor

简要回顾一下，[谷歌于2018年开源了gVisor](https://cloud.google.com/blog/products/identity-security/open-sourcing-gvisor-a-sandboxed-container-runtime)，以提高容器安全性。正如*[The New Stack]*同年稍后[解释的那样](https://thenewstack.io/how-to-implement-secure-containers-using-googles-gvisor/)，该技术使用运行在用户空间中的轻量级内核来拦截应用程序系统调用，在容器和底层宿主操作系统之间提供额外的隔离层。这使得它对于运行不受信任的代码（包括AI智能体生成的代码）特别有用。

这项技术[被各大AI公司采用](https://github.com/google/gvisor/blob/master/ADOPTERS.md)，[包括Anthropic](https://www.anthropic.com/research/how-we-contain-claude)，该公司在其网络平台上将Claude生成的代码运行在gVisor容器内部；OpenAI也[使用它来](https://github.com/openai/codex/issues/47973)隔离代码执行。在[本周三刚发布的](https://openai.com/index/a-thousand-fewer-paths-to-root/)安全报告中，OpenAI将gVisor和Firecracker等沙箱列为限制利用Linux内核漏洞造成损害的重要工具。

这项捐赠已经在酝酿好几周了。CNCF于[9月下旬](https://github.com/cncf/sandbox/issues/521)接受了gVisor的申请，谷歌几天后公开[宣布了其计划](https://gvisor.dev/blog/2026/10/02/gvisor-cncf/)。该项目的加入流程[于上周开始](https://github.com/cncf/sandbox/issues/546)，早于周四涵盖所有三个项目的更广泛公告。

在其10月份的最初公告中，gVisor的贡献者和谷歌软件工程师[Etienne Perot](https://www.linkedin.com/in/etienneperot/)和[Jing Chen](https://www.linkedin.com/in/longjingchen/)试图向用户保证，该公司仍然致力于这项技术。随着对经济、安全沙箱的需求不断增长，他们认为独立的治理可以鼓励谷歌内部及外部更广泛的参与和采用。

他们在当时写道：“我们（谷歌的gVisor贡献者）一直在内部推动这一举措，期望这将加速gVisor在谷歌国内外的增长和采用，其方式类似于Kubernetes发生的情况。”

> “我们一直在内部推动这一举措，期望这将加速gVisor在谷歌国内外的增长和采用。”

Agent Substrate解决了另一个挑战：如何在空闲时避免浪费计算资源，同时运行大量的自主智能体。正如*[The New Stack]*在[7月份报道的那样](https://thenewstack.io/kubernetes-ai-agent-runtime/)，该项目在Kubernetes之上引入了一个额外的运行时层，允许智能体在不活动时挂起，在需要时恢复，而无需重复创建和销毁Kubernetes Pod。它通过将智能体的持久状态与执行它的计算资源分离来实现这一点，而gVisor则为安全隔离该执行提供了可用选项之一。

作为本周公告的一部分，谷歌正式发布了Agent Substrate 1.0，并在Google Kubernetes Engine (GKE)上全面可用。

与此同时，OpenRL专注于强化学习，允许开发者在他们自己的Kubernetes基础设施上微调AI模型。[该项目于6月公开推出](https://opensource.googleblog.com/2026/06/introducing-openrl-a-self-hosted-post-training-api-for-fine-tuning-llms.html)，负责协调用于改进模型的训练和评估过程。它还与Agent Substrate集成，允许训练练习在可以使用gVisor进行保护的隔离环境中运行。

总的来说，这三个项目满足了自主AI智能体的执行、安全和训练需求。

## 转向供应商中立

转向CNCF治理也应改变gVisor的开发和维护方式。在10月份的公告中，Perot和Chen概述了将该项目的开发和测试基础设施移至谷歌外部、授予外部维护者合并代码的权限，以及引入防止任何单一公司行使单方面控制权的治理模型的计划。

值得注意的是，在Perot于9月份通过GitHub提交的项目的[CNCF申请中](https://github.com/cncf/sandbox/issues/521)，他指出了gVisor现有采用者之间的分歧。一端是Anthropic和OpenAI等主要科技公司，它们可以投资于根据自身需求调整技术；另一端是其业务严重依赖安全代码执行的专业初创公司。Perot暗示，机会在于接触这两个阵营之间更广阔的市场。

Perot在申请中写道，此类公司“没有资源专门投资于安全，但会乐意采用现成的、广泛可用的沙箱运行时”。

还有一个问题是，为什么更多的云提供商没有将gVisor集成到他们的商业产品中。在10月份的公告中，Perot和Chen指出，Google、DigitalOcean和Modal是少数几家销售由gVisor提供支持的通用计算服务的提供商，尽管有证据表明客户已经在竞争对手的云平台上自行安装了该技术。工程师们暗示，对谷歌控制该项目的担忧可以解释这种差异。

他们写道：“缺乏直接集成的其余解释很可能是该项目（捐赠前）的治理风险。”

但也许最有趣的障碍涉及Linux内核本身。谷歌和其他使用gVisor的公司维护自己的内核修改，以提高其性能，特别是对于I/O密集型应用程序。这些改进并非普遍可用，可能让其他用户陷入较慢的执行环境中。

Bradstock将难以将这些改进纳入主线Linux内核归咎于gVisor迄今为止以谷歌为中心的信誉。

> “当该项目由单一供应商拥有时，上游Linux维护人员拒绝合并它们。”

Bradstock写道：“当该项目由单一供应商拥有时，上游Linux维护人员拒绝合并它们。”

出于技术原因，对至少一项早期与gVisor相关的内核提案也存在有据可查的阻力。正如[LWN在2022年报道的那样](https://lwn.net/Articles/902585/)，Linux内核维护人员对[提出的性能改进](https://lkml.iu.edu/2207.2/08700.html)提出了安全和设计方面的担忧，包括对其在gVisor之外的实用性的质疑。

虽然此类互动并未将谷歌的所有权作为反对的原因，但很明显，转向CNCF治理应该在很大程度上解决对单一供应商控制的担忧。

对于谷歌而言，这一努力现在已经超出了gVisor的范围。随着Agent Substrate和OpenRL也转向CNCF，该公司希望为自主智能体建立一个共同的基础。

Bradstock写道：“供应商中立的所有权让云提供商、硬件供应商和独立软件公司能够平等地参与智能体工作负载的未来增长。”

[Kubernetes路线图
2026年学习Kubernetes的分步指南

引言
容器
设置Kubernetes
运行应用程序
服务与网络
配置管理
资源管理
安全
监控与日志
自动扩缩容](https://roadmap.sh/kubernetes?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=gvisor-cncf-kubernetes-open-source)