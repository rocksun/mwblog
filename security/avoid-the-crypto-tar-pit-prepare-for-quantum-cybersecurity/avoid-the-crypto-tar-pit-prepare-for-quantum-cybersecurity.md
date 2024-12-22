
<!--
title: 避免量子密码陷阱：为量子密码安全做准备
cover: https://cdn.thenewstack.io/media/2024/11/093978f6-mud.jpg
-->

量子计算日益临近，如果现在不适应，可能会导致您的加密方法过时，成为负债而非保障。

> 译自 [Avoid the Crypto Tar Pit: Prepare for Quantum Cybersecurity](https://thenewstack.io/avoid-the-crypto-tar-pit-prepare-for-quantum-cybersecurity/)，作者 Tomas Gustavsson。

美国国家标准与技术研究院 (NIST) 等政府网络安全机构普遍认为，具有密码学意义的量子计算机最早可能在 2035 年出现，甚至可能更早。

随着量子计算的到来日益临近，您当前的安全措施可能已经面临风险。未能及时适应可能会使您的关键基础设施陷入加密泥潭，过时的加密方法将成为负债而不是保障。

时间紧迫，各组织必须准备过渡到[抗量子密码学](https://thenewstack.io/nist-secures-encryption-for-a-time-after-classical-computing/)，否则将措手不及。

不必惊慌。总有办法。在泥潭吞噬您之前，请考虑以下五个关键因素：

## 1. 过渡到抗量子算法

我们今天依赖的加密算法，如[RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem))（Rivest-Shamir-Adleman）和[ECC](https://www.vmware.com/topics/elliptic-curve-cryptography)（椭圆曲线密码学），将无法抵御量子计算。NIST 正在敦促完全过渡到抗量子算法。当量子计算机开始出现时，不要指望在攻击者开始破解您的密钥之前会得到友好的提示。十年似乎遥不可及，但实际上比您想象的要近。

**这对您意味着什么**：即使量子计算机尚未出现，攻击者现在也可以拦截和存储您的加密数据，等待他们有能力解密的那一天。如果您的信息需要长期安全，您的数据可能已经面临风险。[威胁是真实的](https://thenewstack.io/real-time-sbom-focuses-supply-chain-security-on-real-threats/)，现在是采取行动的时候了。

## 2. 加密敏捷性：不可协商的因素

加密敏捷性是您未来安全保障的通行证。您未来设计的每个系统都必须支持算法和加密格式的无缝切换。就像您不会坚持使用过时的技术一样，您也不应该坚持使用僵化的加密方法。

您的系统在旧标准和抗量子密码学之间切换时需要像体操运动员一样灵活。同样，抗量子算法的研究仍在积极进行中，因此，您既不想被困在过去，也需要适应未来的许多变化。

## 3. 制定您的逃生计划：算法变更

您不能在 2029 年除夕（NIST 和国土安全部预计每个人都将目标定为 2030 年实现量子就绪）简单地翻转开关，并期望您的系统能够神奇地支持抗量子密码学。

您现在需要开始规划。可以将其视为您的加密[灾难恢复计划](https://thenewstack.io/supercharge-your-disaster-recovery-plan-in-5-simple-steps/)。确定哪些系统风险最大，优先处理它们，制定安全的迁移策略以保持加密敏捷性，并开始推出更新。量子威胁是严重的，但如果提前足够的时间，您可以避免仓促的最后一刻的混乱。

## 4. 加固您的软件供应链

保护您的数据免受基于量子的攻击不仅仅涉及更新您的应用程序；攻击可能发生在您的[软件供应链](https://thenewstack.io/are-we-thinking-about-supply-chain-security-all-wrong/)的任何地方。从代码库到第三方集成，链中的每个环节都可能成为漏洞。

从今天开始。通过利用软件供应链安全实践来保护您的软件供应链，并确保您的供应商也了解转向量子安全算法的必要性。必须将抗量子密码学应用于开发过程的每一层，以确保您的代码及其交互的系统都是安全的。

## 5. 如果您也是制造商，固件是您的未来

对于硬件制造商来说，抗量子固件签名是必须的——它是保持您安全完整的数字胶带。没有它，您的设备很快就会变成黑客的游乐场，相信我，那可不是您想待的沙盒。

除此之外，保护设备身份和信任根至关重要。您的数字基础设施的每个部分都需要为量子飞跃做好准备，以领先于未来的威胁。

## 底线

现在就开始。当量子计算最终到来时，加密泥潭可不是您想被困住的地方。
一些政府已经开始强制迁移到抗量子密码学。RSA、[Diffie-Hellman](https://www.techtarget.com/searchsecurity/definition/Diffie-Hellman-key-exchange)和基于椭圆曲线的加密算法的淘汰最终期限即将公布。满足这些需求意味着过渡到抗量子密码学，通过融入密码敏捷性、保护您的软件供应链和升级您的基础设施来确保您的未来。

尝试使用开源软件[EJBCA](https://www.ejbca.org/use-cases/try-quantum-safe-cryptography-pki/)、[SignServer](https://www.signserver.org/)或[Bouncy Castle](https://www.bouncycastle.org/)加密API进行抗量子密码学，以保护您的工作负载身份、服务网格、Kubernetes基础设施和软件供应链。

查看Keyfactor及其基于SaaS的免费公钥基础设施沙箱，以快速[测试抗量子证书](https://www.keyfactor.com/post-quantum-cryptography-lab/)。

*要了解有关Kubernetes和云原生生态系统的更多信息，请加入我们于11月12日至15日在犹他州盐湖城举行的**KubeCon + CloudNativeCon北美**会议。*
