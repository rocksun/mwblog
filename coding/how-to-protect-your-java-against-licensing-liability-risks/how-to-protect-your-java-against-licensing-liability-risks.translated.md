# 如何保护您的 Java 免受许可责任风险

![针对：如何保护您的 Java 免受许可责任风险的特色图片](https://cdn.thenewstack.io/media/2024/08/ec5ebd45-java-1024x576.jpg)

因此，您已从您的环境中删除了所有需要昂贵的 Oracle Java SE 通用许可证的 Oracle JDK，该许可证与 Oracle 主协议 (OMA) 相关。但是，现在您需要阻止 Oracle Java 偷偷潜入并触发对 [Oracle](https://developer.oracle.com/?utm_content=inline+mention) 的新许可义务。以下介绍了禁用 JavaUpdater 和其他当前和常见方法、它们的有效性和缺点，以及提供了一些供您考虑的其他机制。

## 背景

2023 年 1 月，Oracle 将 [Java](https://thenewstack.io/java-22-making-java-more-attractive-for-ai-apps-workloads/) 的许可要求更改为“所有员工指标”。具体内容应在他们的实际协议中进行审查，但为了讨论的目的，让我们将该协议改写为：如果您安装了一个或多个 Oracle Java SE 实例，无论安装位置如何，都属于 Oracle 技术网络 (OTN) 许可证，您的组织可能需要遵守“所有员工”许可要求，无论有多少员工使用 Java 甚至拥有或使用计算机。您组织可能面临的重大财务风险需要持续警惕。

## Oracle Java 如何重新进入？

Oracle Java 可以通过多种方式安装或更新。其中一些方法仅适用于桌面；一些适用于服务器。应考虑这两种环境，因为它们都受相同的 Oracle 许可要求约束。Oracle Java 可以通过多种方式安装或更新。

- 用户直接从 download.java.com 或 oracle.com/downloads 下载。
- 用户从外部维护的镜像站点下载。
- JavaUpdater 后台进程 - （在 Windows 桌面）与 [Oracle Java 开发工具包](https://thenewstack.io/survey-86-of-oracle-java-users-migrating-to-alternatives/)(JDK) 或 Java 运行时环境 (JRE) 一起安装。- Java 控制面板小程序 - 允许一键更新现有 JVM（Java 虚拟机）/JDK。
- 迁移前创建的黄金或其他基本虚拟桌面基础设施 (VDI)/映像。
- 您迁移 Java 之前进行的备份/恢复映像。
- 操作系统便利通知 - 如果系统上未安装 Java，并且用户在命令提示符下键入“Java”，他们将收到一条消息，将他们指向 java.com。
- 许多需要 Java 的传统应用程序可能会提示用户下载 Oracle Java；较新的应用程序通常会请求 OpenJDK，但并非所有应用程序都如此。
- JavaScript - 有几个函数使开发人员可以方便地呈现直接下载或可点击按钮，这些按钮会重定向到 Oracle Java 网站。
以下是针对上述重点内容的一些注意事项：

## 阻止 java.com 和 `oracle.com/java/download`

还不够

Java 已经存在了近 30 年。在此期间，它经历了许多迭代，包括从免费到付费，具体取决于提供商。由于 Java 的普及以及 Oracle Java 在许多用例中免费提供的事实，Oracle Java 通过许多网络渠道、分销合作伙伴和学术机构提供，其中许多机构没有费心维护或删除公开可用的 JDK 和 JRE 的完整功能副本。这些较旧的二进制文件从许可的角度来看通常不会造成麻烦（安全性是另一回事），但附带的 Java 更新程序和 Java 控制面板小程序使用户很容易无意中将其安装更新到需要 Oracle 许可证的版本。

我们将讨论适用于最常见版本（Java 6-21）的策略，但您应该知道，Oracle Java 的某些特定版本需要许可证。这些版本是 8u211+、11、12、13、14、15、16。此外，Oracle 将“商业功能”的使用视为其许可要求的另一个触发因素，例如使用其 MSI ([Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Windows 安装程序) 或使用 JFR（Java Flight Recorder）。

*注意：2024 年 9 月，Oracle Java 17 也将需要付费的 OTN 许可证才能用于商业用途。*

**做：**

- 阻止下载部分（如果可以，请阻止特定版本）。

**不要：**

- 阻止整个域。Java.com 包含大量信息、文档和讨论，对参与 Java 社区的任何人都有帮助。

## 禁用 Java 更新

Oracle Java 包含一个默认情况下启用的后台（TSR 或终止并驻留）进程，用于检查 Java 的新版本。

### EDITOR'S RESPONSE
## 禁用 Java 控制面板小程序

Oracle Java JRE 中包含的控制面板小程序（Windows 上的 `javacpl.exe`）提供了一个图形界面来控制 Oracle JVM 的许多方面。我将在这里提到 WebStart，即使它没有与 Oracle JVM 分开，因为控制面板小程序与 WebStart 关系密切，并且等效功能由开源社区（在 IcedTea-Web 开源项目中）单独实现。控制面板小程序包含一个选项卡，允许用户通过以下几种方式更新他们的 Java：

通过设置自动化或单击“立即更新”按钮，用户可以启动下载其 JRE/JDK 的最新版本。

**操作：**

- 完全禁用此功能，此界面中不再存在任何自助用户级功能（删除对 `javacpl.exe` 的访问权限）。
- 了解此界面操作的底层属性文件，并在管理员级别修改/更新它们。
- 在 Windows 上，您可以禁用 `HLM:\SOFTWARE\JavaSoft\Java Update\Policy` 下的两个注册表项“EnableJavaUpdate”和“EnableJavaUpdateCheck”（DWORD）。
- 应该让高级用户了解 IcedTeaWeb-settings 界面，它取代了此功能的大部分内容。

**不要：**

- 删除 `javacpl.exe` - 这将违反 Oracle 的条款。

## 更新 Golden 或其他基本 VDI/映像

许多企业使用黄金映像来实例化虚拟机，用于各种用例，从快速现场测试和敏捷开发到生产级机器的标准化。这些映像通常包含通用或企业强制执行的软件，并且可能包含用于服务器的 JRE 或用于开发映像的 JDK。由于这些映像在实例化之前一直处于脱机状态，磁盘处于存档状态，因此它们可能处于休眠状态，不会被正常的扫描/观察机制捕获。如果它们仍然存在于您的环境中，如果它们在生产场景中被实例化和使用，它们确实会构成风险。

**操作：**

- 访问您的 VDI/映像存储库以确定 Java 是否包含在标准构建或映像中。如果找到，请使用适当的二进制文件重新构建您的映像。
- 如果您具有映像启动前分类功能，请确保使用更新的 JVM。

**不要：**

- 将替换的负担放在映像用户身上。
- 允许临时使用 Oracle JVM。
- 假设短暂的映像是短暂的。

## 刷新备份、恢复映像和快照

随着时间的推移，备份等将不再是一个问题；它们会自然地老化。但在迁移后的这段时间内，应特别注意跟踪调用任何这些恢复机制的系统。应注意备份本身；据观察，Oracle 在某些情况下已表明备份文件仍然可以轻松获得并轻松启用，因此构成许可证风险违规。从备份恢复的系统将受您现有的软件执行策略的约束，因此请确保尽快捕获并修复它们。修复后，应进行新的备份/快照，如果可能，应将以前的备份移至脱机状态并使其“不可轻松获得”。

**操作：**

- 创建/更新不包含 Oracle Java 的快照。
- 确保执行策略解决不必要的 Oracle Java 二进制文件的执行问题。

**不要：**

- 忽略备份存档，如果它可以使用，它将被使用。
- 假设最终用户会发现这种情况并进行修复。
- 允许即使是更旧的（非 OTN）Java 也在未经检查的情况下运行，至少检查 Java 更新程序和 Java 控制面板设置。

## 禁用操作系统和便捷更新

如果用户在命令提示符下键入“java”或应用程序在未初始化（没有 Java）的 MacOS 系统上请求 Java，您将从操作系统收到一个响应，告诉您访问 java.com：

**操作：**

- 教育您的用户群关于他们应该使用的 Java（基于企业标准或指南）。
- 通过自助服务选项使 Java 易于获得。由于存在许多选项和特定于应用程序的要求，因此期望应用程序和用户遵守特定版本是不合理的。虽然允许 Java 主要版本灵活是安全的，但建议用户尽可能选择最新修补程序版本（主要版本）。
- 考虑一个支持的 OpenJDK，其中包含及时的安全和修补程序更新。
- 通过 `dmg/rpm/msi` 从 [https://www.azul.com/downloads](https://www.azul.com/downloads) 安装 Java 运行时。
- 通过 homebrew 安装/构建 Java
    - Brew
    `install OpenJDK@<java 版本号>`
    - Brew
    不要：
        - 访问 java.com 并安装其中提到的任何版本。
## 处理与应用程序打包在一起的 Java
这种情况需要谨慎处理，并可能需要与软件供应商进行沟通。有些应用程序在安装过程中会合法地包含 Java JRE 或 JDK，例如使用 Java Compact Profile 的低功耗/物联网设备、在网络受限环境中使用的虚拟机映像等。在这些情况下，务必正确理解应用程序的支持要求和许可责任。

在大多数情况下，供应商现在会支持其应用程序在 TCK（技术兼容性工具包）认证的 [OpenJDK 构建](https://thenewstack.io/this-week-in-programming-microsoft-jumps-back-into-java-with-openjdk-build-preview/) 上运行。如果供应商确实将他们的软件认证为 OpenJDK 兼容，那么选择任何你想要的 OpenJDK 发行版就足够了。供应商可能会认证特定发行版，但这可能是由于方便或他们缺乏了解。供应商应该将他们的测试视为针对 OpenJDK 规范，这意味着任何经过认证的 OpenJDK 都足够。如果供应商使用特定于发行版的类，他们应该专门记录该要求。

在一些罕见的情况下，供应商会认为使用任何 JRE 而不是规定的 Oracle JRE 将使他们的支持合同失效。在这种情况下，你应该要求提供上述要求的书面文件，以及一份声明，说明在你的环境中出于此目的使用 Oracle Java 不会使你的组织受到 Oracle 全员许可模式的约束。

请执行以下操作：

- 调查每个符合这种情况的应用程序。访问供应商的网站或联系他们的支持部门是一个好的开始。
- 要求有关将应用程序迁移到 OpenJDK 的说明。不要期望迁移过程会遇到太多麻烦，特别是对于较新的 Java 版本。
不要：

- 忽视这种情况。如果没有明确的声明免除你对 Oracle 的任何许可责任，在第三方应用程序中使用 Oracle JDK 会使你面临许可风险。
## 缓解来自外部网站的 JavaScript 或启用
只需一行简单的脚本就可以创建一个 HTML 按钮，让用户只需单击一下即可下载 Oracle JDK，并创建一个新的许可责任。虽然这些情况通常超出了你的控制范围，但你可以采取一些主动措施。

请执行以下操作：

- 教育你的用户了解他们可用的已批准的 Java 选项。
- 使相应的下载易于获取。
不要

- 允许用户继续使用从 java.com 或 oracle.com 下载的 Java。
## 一般建议
防止持续的 Oracle Java 许可风险是可行的，但现在应该清楚的是，仅靠边界策略不是最佳方法。它需要与缓解策略和合理的警惕性相结合。

- 监控 Oracle Java 并尽快修复任何新的 Oracle Java 实例。用 OpenJDK 发行版替换 Oracle JDK 并不困难，并且几乎不会带来兼容性、稳定性或安全风险。你的新 Java（不是应用程序）供应商也应该能够为此类工作提供指导。
- 如果你有实时桌面管理解决方案可用（如 BeyondTrust、CyberArc 等），请使用它来禁用关键的 Java 安装程序、可执行文件和启动器（
`java.exe`
、`javaw.exe`
、`javaws.exe`
、`jp2launcher.exe`
等）。
- 在 Windows 上尽可能使用组策略。这是控制 Java 是否可以运行或安装的更可靠方法，并且可以通过公司范围的策略集中执行。
- 使用文件系统扫描程序或清单工具来查看安装注册表之外的内容。像 Flexera 或 Microsoft Endpoint Configuration Manager（以前称为 System Center Configuration Manager (SCCM)）这样的工具可以配置为定期运行完整的文件系统扫描。
- Azul 为客户提供访问我们的 Azul 迁移咨询工具，这是一组发现和迁移（shell）脚本示例，我们的团队在协助迁移工作时使用这些脚本。
## 结论
由于 Java 的普遍性和 Oracle Java 许可模式的最新变化，如果你继续允许 Oracle Java 在你的环境中运行，了解你的风险和暴露非常重要。

避免代价高昂的许可责任需要持续的警惕和分类。以上指南作为“尽力而为”的方法提供，我相信还有其他机制可以将 Oracle Java 重新引入你的环境。
请随时发表评论并添加您认为可能影响他人的任何发现，我们将尽力提供有关如何进行分类的建议。如果您需要更多详细信息或有任何不适合在公开论坛上分享的疑虑，请联系 migration@azul.com，我们将直接回复您。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1) 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以收看我们所有的播客、访谈、演示等。