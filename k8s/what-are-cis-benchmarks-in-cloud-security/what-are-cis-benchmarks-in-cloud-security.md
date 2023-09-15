<!-- 
# 云安全中的 CIS 基准 是什么？
What Are CIS Benchmarks in Cloud Security?
https://thenewstack.io/what-are-cis-benchmarks-in-cloud-security/
https://cdn.thenewstack.io/media/2023/09/28e0f396-zetong-li-ckpacfj8ixy-unsplash-1024x768.jpg
Feature image by Zetong Li on Unsplash. 
-->

本文涵盖了 CIS 基准，包括它们是什么，为什么建立它们以及如何在云安全环境下有效评估它们。

保护软件、IT 系统和网络基础设施需要采用最佳实践、工具和技术，才能做到有价值。在建立网络安全运营的最低要求状态方面，没有一刀切的规则。

如今，有几种选择可以保护基础设施服务，使组织能够采用强大的安全态势(并改善其现有安全态势)。 [Center for Internet Security (CIS) 基准](https://www.cisecurity.org/cis-benchmarks)(作为安全最佳实践的基线使用的广泛标准目录)位居此列表的首位。通过拥有最小安全控制的参考指南，组织可以将其实践与共识水平进行比较。

本文探讨了 CIS 基准，包括它们是什么、为什么建立它们，[以及如何在云安全环境下对其进行有效评估](https://orca.security/resources/press-releases/orca-security-cis-benchmarks-certification-24-cloud-frameworks/)。

## 什么是 CIS 基准？

CIS 基准是针对系统安全的基于共识的配置基线和最佳实践。它们被细分成不同的类别，每个类别专注于一种特定的技术。这些类别包括：

- 操作系统
- 服务器软件
- 桌面软件
- 移动设备
- 网络
- 云提供商
- 打印机

换句话说，CIS 基准框架提供了运行安全工作负载所需的最小安全控制和实践的清单。

基准随附完整的参考文档，这些文档使用特定的标准(如适用性、严重性、论证和审计步骤)逐一列出它们。

![](https://cdn.thenewstack.io/media/2023/09/b516b80d-example-of-cis-for-linux.png)

除了基准文档之外，CIS 还为主要的公共提供商提供了加固镜像。这些镜像可以节省安全团队从头开始将建议烘焙到其虚拟机中的时间。

在我们深入讨论基准规则之前，让我们回顾一个 基准 的示例。

## 基准示例

让我们看看来自 [CIS 独立发型版 Linux 发行版](https://www.cisecurity.org/benchmark/distribution_independent_linux)指南的一个 基准：

**1.3.2 确保定期检查文件系统完整性(得分)。**

**配置文件适用性:**

级别1 — 服务器
级别1 — 工作站

**描述:** 需要定期检查文件系统的完整性，以检测对文件系统的更改。

**原理:** 定期文件的检查允许系统管理员定期确定是否以未经授权的方式更改了关键文件。

**审计:** 运行以下命令以验证 aidcheck.service 和 aidcheck.timer 是否启用并正在运行:

```bash
# systemctl is-enabled aidcheck.service

# systemctl status aidcheck.service 

# systemctl is-enabled aidcheck.timer

# systemctl status aidcheck.timer
```

**补救:** 运行以下命令:

```bash
# cp ./config/aidecheck.service /etc/systemd/system/aidecheck.service

# cp ./config/aidecheck.timer /etc/systemd/system/aidecheck.timer

# chmod 0644 /etc/systemd/system/aidecheck.*

# systemctl reenable aidecheck.timer

# systemctl restart aidecheck.timer

# systemctl daemon-reload
```

每个 基准 都有一些重要特性，您需要详细了解：

- **适用性** — 显示此基准适用于哪些系统或服务(由于当前指南针对 Linux，主要选项是服务器或工作站)。
- **得分与未得分** — 得分或自动化状态意味着基准可以自动化到工作流程中(这将导致更快的实施和更快的识别不匹配)。另一方面，未得分或手动状态意味着您无法使用自动化工具提供合格/不合格的评估分数(这使审计更加困难)。
- **包含审计步骤** — 在可能的情况下，会包括审计步骤列表，以便读者可以快速检查基准。
- **包含补救步骤** — 这是一系列命令，可以在基准失败后设置或恢复基准到正确状态。

现在您对 基准 的样子有了更好的了解，我们将为您提供一些如何在云安全工作负载中使用它们的具体建议。

## 如何在云安全中使用 CIS 基准

以下我们将讨论用 CIS 覆盖 基准 建议的关键领域。

### CIEM

与任何值得信赖的云提供商交互都需要身份安全服务。另一方面，访问控制策略的无效使用或错误配置可能会大大削弱组织的整体安全态势。

在配置[云基础设施访问权限管理(CIEM)](https://orca.security/resources/blog/ciem-role-in-cloud-security-strategy/)时的一个常见风险是拥有过于宽松的身份或太多的策略，以至于安全团队无法维护。CIS 基准要求您查看个别云提供商的文档(AWS、Azure 等)，以获取特定的身份安全规则。

例如，如果您使用 AWS，CIS Amazon Web Services 基础基准包含与 IAM 相关的超过 23 个基准。这些建议需要针对帐户持有人进行评估、应用和合规性审计。

这就是为什么许多组织使用自动化工具来监控 CIS 合规性。CIS 还提供免费和高级工具，您可以用它们来扫描 IT 系统并生成 CIS 合规报告。如果现有配置不符合 CIS 基准建议，这些工具会向系统管理员发出警报。

另一方面，您可以通过将风险转移给专用的云安全管理员来解决这个问题。例如，通过使用 [Orca 的 IAM 补救](https://orca.security/resources/blog/elevate-ciem-with-iam-remediation/)等新颖的解决方案来管理和提供准确的 IAM 策略建议，您可以减轻团队手动准确实施基线控制的负担。

![](https://cdn.thenewstack.io/media/2023/09/36e31687-iamm-recommendations.png)
*图. 2 — IAM 建议 (来源: https://orca.security/)*

## 数据安全

数据安全代表了另一个需要正确遵守的关键领域。数据泄露和敏感个人身份信息的暴露在财务上可能造成破坏(因为缺乏安全控制可能导致诉讼和罚款)，同时也会损害声誉。

由于私人数据是对手攻击和外国特工的主要目标，它在 CIS 基准列表的许多区域中出现。例如，有专门的基准用于密钥轮换、为磁盘上存储的数据设置正确的权限，以及确保静态加密和传输中的加密。以下是一些示例：

- 在 Kubernetes 中：6.9 存储 6.9.1 — 考虑为 GKE 持久磁盘(PD)启用客户管理的加密密钥(CMEK)。
- 在 AWS 中：2.8 — 确保启用客户创建的 CMK 的轮换。
- 在 Red Hat Linux 中：2.2.20 — 确保未安装 rsync 或 rsyncd 服务被屏蔽(自动)。
- 在 Red Hat Linux 中：1.3.1 — 确保安装 AIDE(自动)。

同样，为了支持这些基准，您需要拥有组织系统和软件的目录，验证现有的安全配置文件，并在需要时进行调整以覆盖基线 CIS 建议。

Orca Cloud Security 平台提供了一个开箱即用的[数据安全态势管理(DSPM)](https://orca.security/platform/data-security-and-posture-management-dspm/)模块，专门处理数据安全补救。它为组织的数据存储中的任何敏感数据暴露、错误配置和当前风险提供上下文驱动的视图。拥有持续的[数据安全合规性](https://orca.security/resources/blog/securing-sensitive-data-across-clouds-with-data-security-posture-management-dspm/)服务简化了安全运营，提高了整体安全性。

## Kubernetes 基准

现在 [Kubernetes 安全](https://orca.security/resources/blog/cis-benchmarks-improve-kubernetes-security/)备受关注，因为许多组织正在将其工作负载迁移到此技术。为了确保合规性和可靠性，拥有 Kubernetes 工作负载的最新和可靠的安全基线是必须的。

更具体地说，需要相关的安全控制意识到 Kubernetes 架构组件及其安全漏洞。CIS 为保护 [K8s 工作负载](https://www.cisecurity.org/benchmark/kubernetes)提供了广泛的基准材料，涵盖了基础发行版和云提供商。

遵循 K8s 的推荐方法需要广泛的引导过程，因为典型的部署由许多移动部件和组件组成。例如，到目前为止，CIS Google Kubernetes 引擎(GKE)中有超过 60 个建议。

![到目前为止，CIS Google Kubernetes引擎(GKE)中有超过60个建议。](https://cdn.thenewstack.io/media/2023/09/dfba4719-gke-recommmendations.png)
*图. 3 — GKE 建议 (来源: https://www.cisecurity.org/benchmark/kubernetes)*

Pod 的短暂性质并没有使这项工作变得更容易。您需要投入大量时间和资源来实现覆盖 CIS 基准水平的安全自动化。

无 Agent 的安全范例可以帮助扩展安全建议和最佳实践，同时支持成千上万的容器和节点。使用 [Orca 的容器和 Kubernetes 安全](https://orca.security/platform/container-and-kubernetes-security/)模块，您可以在几分钟内更好地洞察 K8s 群集中的任何安全缺陷。

## CIS 基准的下一步

如果您想了解更多关于 CIS 基准的信息，我推荐您从[官方网站](https://downloads.cisecurity.org/#/)下载免费资源。花些时间查看基准建议，并检查您应该关注的领域。这将为您提供一个更合适的上下文来学习如何正确保护东西以及为什么。

接下来，您将想要评估和自动化与您的组织相关的 CIS 基准。这将确保您从不必要的控制或策略中区分出最小必需规则，以整体提高安全级别。

最后，您将想要通过利用像 Orca Security 这样的[云原生应用程序保护平台(CNAPP)](https://orca.security/resources/blog/cnapp-cloud-native-application-protection-platform-security/)来提升基础设施安全基线。由于它们可以通过自动化和先进的技术卸载大部分繁琐的任务，这种服务的好处是成倍的。[请求演示](https://orca.security/demo/)或[注册免费的云风险评估](https://orca.security/lp/cloud-security-risk-assessment/)，以查看 [Orca Cloud Security 平台](https://orca.security/platform/)如何帮助您在云中实现新的安全性和可见性水平。

## 扩展阅读

- [Not all Risks Are Equal: Why Context Matters in Cloud Security](https://orca.security/resources/blog/not-all-risks-are-equal-why-context-matters-in-cloud-security/)
- [CIEM: Securing Identities and Entitlements across Multi-Cloud Environments with Orca Security](https://orca.security/resources/blog/securing-identities-and-entitlements-across-multi-cloud-with-orca-ciem/)
- [Kubernetes Hardening Guide: A Perfect Complement to the CIS Kubernetes Benchmarks](https://orca.security/resources/blog/kubernetes-hardening-guide/)