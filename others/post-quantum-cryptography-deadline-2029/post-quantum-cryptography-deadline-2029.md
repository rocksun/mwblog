<!--
title: 微软、谷歌和Cloudflare将量子安全期限提前至2029年
cover: https://cdn.thenewstack.io/media/2026/07/be34eb79-getty-images-aligedqnf6a-unsplash-scaled.jpg
summary: 由于量子计算研发进展加速及“现在拦截，未来解密”的威胁加剧，微软、谷歌与Cloudflare等科技巨头已将量子安全部署期限提前至2029年。文章呼吁企业尽早进行密码学资产梳理，并构建具备“密码灵活性”的防御体系以应对未来风险。
-->

由于量子计算研发进展加速及“现在拦截，未来解密”的威胁加剧，微软、谷歌与Cloudflare等科技巨头已将量子安全部署期限提前至2029年。文章呼吁企业尽早进行密码学资产梳理，并构建具备“密码灵活性”的防御体系以应对未来风险。

> 译自：[Microsoft, Google and Cloudflare just made 2029 the new quantum deadline](https://thenewstack.io/post-quantum-cryptography-deadline-2029/)
> 
> 作者：Adrian Bridgwater

通往[量子计算](https://thenewstack.io/quantum-computing-use-cases/)的必经之路，也带来了应对后量子密码学的同等且相反的责任。

包括[美国](https://www.whitehouse.gov/presidential-actions/2026/06/securing-the-nation-against-advanced-cryptographic-attacks/)和[法国](https://www.reuters.com/legal/litigation/france-stop-certifying-products-without-quantum-safe-encryption-2026-06-16/)在内的多国政府此前已设定了本十年末的时间表，规定公共部门机构和“关键运营商”应在2030年前采购并部署专门的[量子安全技术](https://thenewstack.io/nist-secures-encryption-for-a-time-after-classical-computing/)。

现在，这个时间表变了。

包括[Microsoft](https://www.microsoft.com/en-us/security/blog/2026/06/30/microsoft-advances-quantum-safe-security-as-the-risk-timeline-shifts/)、[Google](https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/#:~:text=Mar%2025%2C%202026,to%20encryption%20and%20digital%20signatures.)和[Cloudflare](https://blog.cloudflare.com/post-quantum-roadmap/)在内的技术供应商已公开声明，他们将把量子安全截止日期提前到2029年。

> “我们认为，具有密码学意义的量子计算机可能比预期更快到来，所需的准备工作量巨大，因此组织现在就需要开始行动。”

## 新的风险地平线

Microsoft Azure 首席技术官 [Mark Russinovich](https://www.linkedin.com/in/markrussinovich/) 表示，量子研发的进展现在已经“改变了每个人的风险地平线”。

“我们认为，具有密码学意义的量子计算机可能比预期更快到来——所需的准备工作量巨大，因此组织现在就需要开始行动，”Russinovich 在最近的一篇博客文章中写道。

Russinovich 指出，人们日益认识到，向量子安全密码学的转型是一项“多年的工程工作”，得益于早期的规划和行动，因此推迟工作会增加成本和风险。

Microsoft 量子安全计划 (QSP) 的时间表以及在2029年前将产品和服务迁移到 PQC 的目标，意味着 Redmond 也将 PQC 要求纳入其[安全未来倡议](https://www.microsoft.com/en-us/trust-center/security/secure-future-initiative) (SFI)。

“这使量子安全就绪状态纳入了我们用于其他关键安全成果的严格工程框架：明确的所有权、可衡量的里程碑和透明的进度。将这些能力嵌入我们的平台，使客户能够更早、更自信地采取行动，”Russinovich 补充道。

> “具有密码学意义的量子计算机尚不存在，但全球许多实验室正在寻求不同的构建方法。”——Bas Westerbaan, Cloudflare。

## 后量子密码学有哪些变化？

PQC 只能在具有密码学意义的量子计算机上实现，[目前此类计算机尚不存在](https://quantumsequrity.com/blog/pqc-state-2026#:~:text=As%20of%20early%202026%2C%20the,quantum%22%20(NISQ)%20devices.)。我们在2026年所能拥有的最接近的技术是“含噪声中等规模量子”(NISQ) 设备，它们运行 [IBM Heron](https://www.ibm.com/quantum/hardware#processors) 或 [Google Willow](https://blog.google/innovation-and-ai/technology/research/google-willow-quantum-chip/) 芯片，可处理大约1,000到1,500个物理量子比特。

为了强调这种迫在眉睫的威胁，Cloudflare 后量子专家 [Bas Westerbaan](https://www.linkedin.com/in/baswesterbaan/) 将“Q-Day”定义为具备足够能力的量子计算机能够破解当前保护数据和系统访问的关键加密技术的那一天。

“具有密码学意义的量子计算机尚不存在，但全球许多实验室正在寻求不同的构建方法。Google 最近宣布在超导量子计算机之外还[追求中性原子](https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/)，其背后的动机现在变得显而易见了，”Westerbaan 指出。

当今的公钥密码学标准，如 RSA 和 ECC（椭圆曲线密码学），建立在大整数分解或计算离散对数的困难性之上。这些防御系统在量子计算机面前可能会被[Shor算法](https://en.wikipedia.org/wiki/Shor%27s_algorithm)迅速瓦解，该算法利用量子叠加和干涉来计算相关函数的周期。

具有密码学意义的量子计算机使用大整数上的替代数学问题来实现后量子密码学，包括基于格或基于哈希的结构，据称这两者在面对量子威胁时仍保持计算难度。

根据 Google 安全工程副总裁 [Heather Adkins](https://www.linkedin.com/in/argvee/) 和公司密码学负责人 [Sophie Schmieg](https://www.linkedin.com/in/sophie-schmieg-14367499/) 的说法，工作已经开始。“作为我们持续致力于 PQC 的一个例子，Android 17 正在集成符合美国国家标准与技术研究院 (NIST) 标准的使用 ML-DSA 的 PQC 数字签名保护，”两人在 Google 的创新博客上写道。

> “大多数组织对其应用程序、基础设施、遗留系统和数据流中密码学的存在位置没有清晰的认识，” Certes 的 Simon Pamplin 说道。

## “现在拦截，未来解密”的威胁

量子安全数据保护公司 [Certes](https://certes.ai/) 的首席技术官 [Simon Pamplin](https://www.linkedin.com/in/simonpamplin/) 告诉 *The New Stack*，政府和全球最大技术平台的“前进方向”现在已经明确，步伐正在加快。

“值得探讨的是原因，”Pamplin 说。“标准的解释指向量子硬件的进步。这确实是原因之一。但更直接的驱动因素是‘[现在拦截，未来解密](https://www.hashicorp.com/en/blog/harvest-now-decrypt-later-why-today-s-encrypted-data-isn-t-safe-forever)’活动的威胁。对手，包括具有长远眼光的国家级参与者，今天已经在拦截和囤积加密数据。保护这些数据的密码学基础不需要立即被破解。它们最终会被破解，而这个‘最终’正在临近。”

Pamplin 对整个讨论持宿命论态度，并暗示截止日期是2027年、2029年还是2030年，在某些方面并不重要。他提醒我们，这是因为今天被拦截的数据不会等待合规时间表。

“大多数组织对其应用程序、基础设施、遗留系统和数据流中密码学的存在位置没有清晰的认识，”Pamplin 强调。“投资于多年来部署的相同基础设施控制措施的新版本，并不能解决潜在的暴露问题。数据不会停留在组织控制的环境中。它会在第三方平台、供应商网络和遗留基础设施之间移动，而这正是需要应用保护的地方。”

他说，那些正在创造和部署真正韧性的组织，是那些将以数据为中心的量子安全保护直接应用于数据本身的组织，确保无论数据经过什么系统，或者对手何时试图使用它，数据始终保持不可读和主权。

## 不要等到2026年；现在就是行动的时候

距离现在还有三年时间并不长，因此对许多组织来说，2029年将让人感到那件新的大事（坏事）近在咫尺。Microsoft 的建议是，今天就考虑这种变化，并为多年的密码学转型确定所有权、范围和里程碑。

对于对路线图有一定了解的系统架构师和软件工程师来说，这意味着为变革而设计，并将密码灵活性（crypto-agility）构建到新的软件和数据产品中，这样未来的标准转换就是更新，而不是紧急情况。

Microsoft 的 Russinovich 敦促公司从盘点开始，创建并维护“动态密码学清单”，以识别、优先排序并最终实现应用程序依赖关系的现代化。量子时代即将来临，它不可避免地会与人工智能发生交叉；接下来会发生什么是一个未知数。