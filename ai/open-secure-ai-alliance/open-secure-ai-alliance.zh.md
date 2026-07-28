围绕[开源软件](https://thenewstack.io/open-source/)和[开放权重AI模型](https://thenewstack.io/chinese-frontier-models-quantization/)的使用，当前的[讨论热潮](https://thenewstack.io/microsoft-nvidia-meta-and-open-weights/)似乎在“什么是合法的开放”以及“哪些行为可能构成盗窃并导致新的[网络安全](https://thenewstack.io/ai-is-changing-cybersecurity-fast-and-most-analysts-arent-ready/)漏洞”这两个观点上产生了分歧。

为了直接应对这些行业性的担忧，33家合作伙伴于周一宣布成立全新的[Open Secure AI Alliance](https://www.opensecureaialliance.org/)。该机构将致力于开发各项技术和工具，通过快速识别和修复漏洞来保障软件安全。

## Open Secure AI Alliance创始合作伙伴

Open Secure AI Alliance的创始合作伙伴包括 [Nvidia](https://thenewstack.io/microsoft-nvidia-meta-and-open-weights/)、Adobe、Cadence、[Capital One](https://thenewstack.io/capital-one-developer-enablement/)、[Cisco](https://thenewstack.io/cisco-is-using-ebpf-to-rethink-firewalls-vulnerability-mitigation/)、Cloudera、[Cloudflare](https://thenewstack.io/cloudflare-ai-web-economics/)、[Cognition](https://thenewstack.io/coding-agents-team-infrastructure/)、CrowdStrike、[Databricks](https://thenewstack.io/databricks-is-rebuilding-the-data-stack-for-ai-agents/)、Dell Technologies、[DoorDash](https://thenewstack.io/doordash-cli-agents-order/)、[Elastic](https://thenewstack.io/agentic-ai-observability-operations/)、[HPE](https://thenewstack.io/hpe-agentic-ai-ops-burnout/)、Hugging Face、[IBM](https://thenewstack.io/ibm-bob-agentic-development/)、LangChain、[Linux Foundation](https://thenewstack.io/agentic-ai-foundation-launch/)、[Microsoft](https://thenewstack.io/microsoft-scout-openclaw-runtime/)、[NetApp](https://thenewstack.io/apache-cassandra-6-features/)、Nous Research、[OpenClaw](https://thenewstack.io/persistent-ai-agents-compared/)、[Palantir](https://thenewstack.io/palantir-nvidia-sovereign-ai/)、[Palo Alto Networks](https://thenewstack.io/palo-alto-portkey-ai-gateway/)、[Salesforce](https://thenewstack.io/context-is-everything-sales-force-data-360/)、[ServiceNow](https://thenewstack.io/servicenow-ai-governance-agents/)、[Snowflake](https://thenewstack.io/snowflake-coco-coding-agent/)、Synopsys、Thinking Machines Lab、TrendAI、[Red Hat](https://thenewstack.io/red-hat-introduces-its-first-out-and-out-ai-platform/)、Reflection AI 以及 [SpaceXAI](https://thenewstack.io/musk-spacexai-grok-open-source/)。

这是一群科技领域最具影响力的公司，但其中有两个显著的缺席者：OpenAI 和 Anthropic，这两家属于封闭的专有AI实验室。他们的缺席是可以理解的，因为他们运营着封闭的实验室，而开放权重AI模型实际上就是他们的竞争对手。

[Nvidia](https://thenewstack.io/nvidia-open-weight-letter/) 企业平台副总裁 [Justin Boitano](https://www.linkedin.com/in/justinboitano/) 发表声明称，开放权重模型是美国AI领导地位和网络安全的基础。

“为了保持美国在AI工业革命中的领导地位，支撑我们经济的基础设施需要安全、可靠地访问封闭和开放模型，” Boitano写道，“对于网络安全而言，开放模型和开放工具（harnesses）至关重要，因为它们拓宽了防御能力，提高了防御者的透明度，并以可定制、本地化的控制手段补充了前沿封闭模型。”

随着监管机构努力应对AI安全问题，Boitano预测，将“开放模型和开放工具视为防御资产”将变得非常重要——从而实现透明度、独立评估和共享修复。

## 没有人能传唤一个已下载的权重文件

技术咨询公司 [The Enterprise Edge](https://www.tee5.ai/about) 的创始人兼首席执行官 [Mark Vigoroso](https://www.linkedin.com/in/markvigoroso/) 告诉 *The New Stack*，AI监管机构传统上是“围绕审计少数几家封闭实验室来构建其整个AI安全体系”的。而现在，这种方法已经过时了。

“开放权重模型早在几个月前就超越了那种封闭模型的方法，” Vigoroso说，“该联盟承认，真正的安全工作现在必须在基础设施层面进行：补丁周期、来源证明、以及围绕谁在部署什么的身份识别，因为没有人能传唤一个已下载的权重文件。”

> “该联盟承认，真正的安全工作现在必须在基础设施层面进行：补丁周期、来源证明、以及围绕谁在部署什么的身份识别，因为没有人能传唤一个已下载的权重文件。”

Vigoroso认为，AI安全争论“卡在了模型层面的控制上”，而真正的监管缺口在于基础设施的来源和身份，即不仅要知道模型是否安全，还要知道模型来自哪里、谁部署了模型以及它触及了什么。

“像[欧盟AI办公室](https://digital-strategy.ec.europa.eu/en/policies/ai-office)、NIST的AI标准与创新中心（[CAISI](https://www.nist.gov/caisi)）以及英国的AI安全研究所（[AISI](https://www.aisi.gov.uk/)）这样的组织，几乎*完全*专注于前沿封闭模型。开放权重模型（[Mistral](https://thenewstack.io/mistral-vibe-cloud-agents/)、DeepSeek等）陷入了监管盲区：一旦权重被发布，就没有办法强制执行下游的安全义务。”

当前的AI模型监管框架假设存在单一的可问责部署方；而开源则没有。这就是真正的问题所在：Vigoroso表示，监管机构正在为中心化的世界编写规则，而生态系统正在去中心化。

虽然目前解释该联盟拟采取行动的详细运营信息还很少，但Nvidia强调，它正在为Open Secure AI Alliance贡献扎实的研究成果，以加速开发新的网络安全工具和技术。

## 工具与模型的集成使代理更易于测试

开源的 Nvidia Labs Object-Oriented Agent (NOOA) 项目现已在 GitHub 上发布，旨在让代理（agent）工具更容易获取先进的AI安全能力。该研究框架使工具能够与模型集成，从而使代理行为更易于测试、追踪、审计和治理。

经过验证的身份和端到端加密公司 [Atsign](https://atsign.com/) 的首席执行官 [Aparna Rayasam](https://www.linkedin.com/in/aparna-rayasam/) 告诉 *The New Stack*，“AI闪电战式的讨论已达到一个关键的转折点。”在这个时刻，我们不能建立在Rayasam所称的“遗留的、千疮百孔的基础设施”之上来构建下一个开放认知创新的时代。

> ……“AI闪电战式的讨论已达到一个关键的转折点。”

“Open Secure AI Alliance的成立证明了AI安全不仅仅是一个算法数学问题，它更是一个基础的网络问题，” Rayasam说，“训练和运行现代AI所需的大规模分布式管道要求一种全新的信任范式。真正的安全意味着确保为这些模型提供数据的管道本身是隐形的、不可被攻击的，并且完全剥离了开放的网络边界。”

这里的关键概念是，我们正在从一个保护静态数据的世界，转向一个AI连接组织必须“默认安全”（secure by design）的世界。

## 一个AI供应商就能确保安全？别开玩笑了。

代理身份和权限安全公司 [Reco](https://www.reco.ai/) 的创始人兼首席产品官 [Gal Nakash](https://www.linkedin.com/in/naksec/) 告诉 *The New Stack*，Open Secure AI Alliance的启动是一个“重要的信号”，强调了为什么AI安全不能由单一供应商或单一封闭框架来解决。

“黄仁勋的观点——[每一家SaaS公司都将成为一家GaaS公司](https://www.youtube.com/shorts/XsUvLCQeu1k)，捕捉到了为什么这在当下很重要：软件正在从人们登录的被动工具，转变为访问数据、采取行动并执行工作流的AI代理，” Nakash说，“开源工具和共享标准可以帮助行业更快地发展，但它们需要植根于身份、权限、数据访问和行为等方面的真实企业情境中。”

自动化、身份驱动的微隔离公司 [Zero Networks](https://zeronetworks.com/resource-center/webinars/cyber-security-and-resilience-regulation-uk?cid=701Uc000012QSS2IAO&utm_term=Zero_NetworksZero_Networks&utm_campaign=brand-search-tofu-uki&utm_source=google&utm_medium=cpc&utm_id=23984533379&utm_content=practioner&hsa_acc=1154373649&hsa_cam=23984533379&hsa_grp=199586129484&hsa_ad=814699429847&hsa_src=g&hsa_tgt=kwd-2304959397113&hsa_kw=zero%20networks&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=23984533379&gbraid=0AAAAACkyBiw_MB53L1xqCfSbKA96Sadtp&gclid=Cj0KCQjw4JbTBhCoARIsALWUaBvEF-62etHZVtfKXihNJWwN2jEzDN9C6CIUfRW9Yj3FRjnbeTLN17IaAmk_EALw_wcB) 的现场首席技术官 [Chris Boehm](https://www.linkedin.com/in/chrisboehmii/) 告诉 *The New Stack*，Open Secure AI Alliance的新闻让他感觉似曾相识。

“这看起来就像当年微软可信平台模块（[TPM](https://support.microsoft.com/en-us/windows/security/devicesecurity/enable-tpm-2-0-on-your-pc)）的故事重演，” Boehm说，“这是一个行业组织定义什么是可信硬件，平台供应商随后采用它，几年内它就从建议变成了采购要求的案例。”

他解释说，“Windows 11通过TPM 2.0和安全启动（Secure Boot）正是这样做的”，而且Linux和苹果也都适应了。“我预计AI基础设施也会发生同样的情况，即经过认证的硅片将成为受监管工作负载的底线，供应商名单将缩小到那些能够满足这一要求的企业，” Boehm预测道。

> “这看起来就像是一个行业组织定义什么是可信硬件，平台供应商随后采用它，几年内它就从建议变成了采购要求的案例。”

## 需要一种更全球化和地理上包容的方法

开放技术机构 [OpenUK](https://openuk.uk/) 的首席执行官 [Amanda Brock](https://www.linkedin.com/in/amandabrocktech/) 告诉 *The New Stack*，Open AI Alliance无疑是一个很好的起点，特别是考虑到[OpenAI上周披露的安全困境](https://thenewstack.io/openai-huggingface-sandbox-breach/)。

“但是，正如那封[关于美国在开放权重方面领导地位的公开信](https://www.microsoft.com/en-us/corporate-responsibility/topics/open-weight/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform)一样，这是美国对美国挑战的反应，” Brock说，“[关于即将发布的总统行政命令](https://www.axios.com/2026/07/20/ai-us-china-open-source-kimi)以[关闭开放模型](https://www.semafor.com/article/07/15/2026/white-house-not-ruling-out-action-on-open-source-ai-models)的传言已经流传了数周——而且随着政府因中国[Kimi K3](https://thenewstack.io/kimi-k3-open-weight-coding/)的问题陷入混乱而愈演愈烈。”

Brock坚称，为了让该联盟取得成功，它需要采取一种比美国本土创始成员更“全球化和地理上包容”的方法。

“它还必须让那些正在构建基础设施、代理工具功能和AI开发工具的个人和创新者组成的开源生态系统参与进来。重要的是要认识到，开放的AI基础设施开发将创新掌握在多数人手中，这与少数拥有前沿模型的企业创造者形成了直接对立，” Brock补充道。

Nvidia的Boitano赞同Brock的观点。在 *The New Stack* 审阅过草稿的一篇博文中，他写道，“开放模型将更多的AI用户变成了AI构建者”，扩大了机会，加速了创新，并防止了进步集中在少数几个组织或地区。

Boitano最后说，开放模型还使独立科学研究能够深入了解AI系统的行为，从而使研究人员能够理解、评估和改进它们。这一切都是为了实现他所说的广泛、持续的防御成为可能。

展望未来，感觉下一波AI安全机构、运动或联盟将不仅仅是模型审计师——它们将是信任基础设施标准机构（涵盖身份验证、内容来源、信任度等），使用借鉴来的治理和合规方法。最终，这可能是唯一能够在开放权重激增中幸存下来的强制执行层。