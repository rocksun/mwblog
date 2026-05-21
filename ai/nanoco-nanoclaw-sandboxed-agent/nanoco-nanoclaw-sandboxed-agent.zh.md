[NanoCo](https://nanoco.ai) 是开源 [NanoClaw 智能体框架](https://thenewstack.io/nanoclaw-minimalist-ai-agents/) 背后的特拉维夫初创公司。周三，该公司推出了一项托管企业服务，旨在为每位员工提供一个个人 AI 智能体，每个智能体都隔离在各自的 [Docker 沙箱](https://thenewstack.io/nanoclaw-docker-sandboxes-ai-agents/) 中。该公司还在由 Valley Capital Partners 领投的种子轮融资中筹集了 1200 万美元，Docker 和 Vercel 也参与了其中。

目前市场上大多数企业 AI 智能体服务（包括 Microsoft Copilot、ChatGPT Enterprise 和 Glean）通常作为整个公司的单一共享助手进行部署。NanoCo 则押注于一种截然不同的部署方式，即每位员工一个沙箱化的智能体，随着时间的推移，这些智能体会适应那个人的角色和工具。

NanoCo 的联合创始人兼 CEO [Gavriel Cohen](https://www.linkedin.com/in/gavrielco/) 告诉 *The New Stack*：“大多数公司并不想构建一个智能体平台。他们想要的是为每位员工提供一个能工作的助手。”

自 2 月份发布以来，NanoClaw 已经积累了近 29,000 个 GitHub 星标。该项目的开发者社区依然非常活跃，其用户现在包括 Amazon、Google、Meta 和 Accenture 的高管，以及一位有些出人意料的 NanoClaw 超级粉丝：新加坡外交部长 Vivian Balakrishnan（Gavriel Cohen 和他的联合创始人兼兄弟 Lazer Cohen 最近实际上飞往新加坡与他会面）。

![](https://cdn.thenewstack.io/media/2026/05/a9577240-screenshot-2026-05-20-at-08.56.39-1024x895.png)

*NanoClaw 创始人 Lazer Cohen 和 Gavriel Cohen。图片来源：NanoCo。*

## 凭证永远不会触达智能体

只有在安全的情况下，Claw（智能体）才能在商业环境中被接受。通过 NanoClaw，每位员工的智能体都在其专属的 Docker 沙箱中运行。例如，来自用户 Slack 或 Teams 应用的请求通过桥接组件进入 NanoCo 称为“路由器”（Router）的组件，该组件从名为“智能体保险库”（Agent Vault）的独立组件中提取凭证，并在发起出站调用时才注入这些凭证。智能体本身永远看不到它们。

“智能体必须能够在企业最敏感的部分工作，”Gavriel Cohen 说，“比如他们的电子邮件，他们的客户记录。”

默认情况下，该设计假设任何输入都可能是恶意的，因此这种凭证隔离限制了智能体在被误导时所能做的事情。

![](https://cdn.thenewstack.io/media/2026/05/0cdf5a7d-screenshot-2026-05-20-at-09.56.56-1024x572.png)

*NanoClaw 凭证处理机制。图片来源：NanoCo。*

## 批准即身份绑定

当一个动作获得批准时（无论是自动批准还是由人工批准），NanoCo 的系统会使用审批者的凭证而不是智能体的凭证来运行它。这意味着，例如，对 Salesforce CRM 字段的写入操作将记录在批准它的人员名下。

Gavriel Cohen 认为，大多数智能体平台中的审批流程并非如此。它们将“是/否”的决策路由给人类，却不将人类的身份与产生的操作绑定，从而留下了不完整的审计追踪。

每个员工专属的智能体充当监管者，可以根据需求生成专门的子智能体，这些子智能体随后也在各自的沙箱中运行。在 NanoCo 的公关工厂（PR Factory）示例中，一个监管智能体分派任务给独立的评审智能体和测试智能体。测试智能体会启动一个虚拟机来运行实际测试。

## 跳过转化漏斗

在商业模式方面，NanoCo 采取了一种有些不同寻常的方法。该公司并不一定将 NanoClaw 的开源用户视为其企业产品的转化漏斗顶端。

“我们没有做像 Elastic 或 Redis 那样的常规事情，即试图让相同的开源用户并在某个时间点强迫他们进行转化，”Gavriel Cohen 说。

开源核心（Open-core）模式可能对推动采用很有用，商业团队随后可以向这些用户追加销售企业功能，但 NanoCo 团队表示，其目标是那些原本就没有工程团队在 NanoClaw 之上构建自己智能体平台的公司。

## 目前提供“管家式”服务

问题是 NanoCo 如何扩大规模。截至目前，该公司只有 10 名员工。已有 100 多家公司在公司的登记页面上留下了详细信息，寻求部署智能体的帮助。但目前，每次部署都是定制的，可能涉及为金融和其他对数据驻留有严格要求的行业进行本地部署，或者在云端进行完全托管的部署。团队与客户的内部工具集成，然后持续运营助手。

“我们将会在一段时间内面临产能受限，”Gavriel Cohen 说。渠道合作伙伴和转售商是长期的解决方案，但 Gavriel Cohen 也认为，团队从它构建的每一次部署和集成中都能学到东西。

截至目前，NanoCo 尚未披露其定价。