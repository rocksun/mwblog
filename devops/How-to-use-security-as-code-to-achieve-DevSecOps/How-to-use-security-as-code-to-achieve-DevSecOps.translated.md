# 如何使用安全即代码实现 DevSecOps
## 安全即代码帮助组织实现 DevSecOps 和左移安全。了解 SaC 的优势、挑战和实施最佳实践。

传统的应用程序开发方法已经迅速过时——尤其是在应用程序安全方面。软件漏洞和编码错误的日益增长的威胁意味着开发人员不能再创建应用程序，而不在软件开发生命周期的各个阶段包含安全。

安全过去是在开发过程结束时进行检查的，这往往会增加安全和开发团队的工作量，并减缓上市速度。

如今，安全即代码 (SaC) 正在成为实施 [DevSecOps](https://www.techtarget.com/searchitoperations/definition/DevSecOps) 方法的关键。DevOps 代表开发人员和 IT 运维团队之间的协作，而 DevSecOps 则更进一步，还包括安全团队。

## 什么是安全即代码？
SaC 是一种方法，它将自动安全检查、测试和控制集成到整个软件开发生命周期 ([SDLC](https://www.techtarget.com/searchsoftwarequality/definition/software-development-life-cycle-SDLC)) 中。目标是在不影响开发时间或造成瓶颈的情况下识别和缓解应用程序安全威胁。SaC 在开发的每个阶段都将安全放在首位，从最初构思到部署。这被称为 *左移安全*。

![显示软件开发生命周期不同步骤的图表。](https://www.techtarget.com/rms/onlineimages/app_arch-software_dev_lifecycle-f_mobile.png)
通过左移安全，可以在开发周期的早期发现安全缺陷，使团队能够在问题出现时解决问题。

![显示通过实施安全即代码实现左移思维的图表。](https://www.techtarget.com/rms/onlineimages/shift_left_security_with_security_as_code-f_mobile.png)
SaC 包括以下组件，这些组件在持续集成/持续交付 (CI/CD) 管道中自动运行：

* **访问控制**确保只有被授权使用系统的人员才能获得访问权限。
* **策略管理**确定需要哪些安全实践。它对于 [治理、风险和合规性](https://www.techtarget.com/searchsecurity/tip/Exploring-GRC-automation-benefits-and-challenges) 至关重要，因为它们定义了软件的关键属性。
* **漏洞扫描**在每个 SDLC 阶段自动检测软件代码中的漏洞和弱点。
* **安全测试和验证**识别代码中可能影响软件和数据机密性、完整性和可用性的缺陷。

虽然 SaC 主要属于网络安全团队的职责范围，但它也是开发和运维团队的重要活动。DevSecOps 和 SaC 使三个团队能够在同一个框架下工作，从而增强协作。

SaC 与基础设施即代码 (IaC) 相关，后者自动添加和更新基础设施组件，例如数据库、服务器和存储。

没有一个单一的工具可以实现 SaC。相反，以下工具、流程和技术的组合可以帮助组织部署 SaC：

* **静态应用程序安全测试。**[逐行检查代码](https://www.techtarget.com/searchsecurity/tip/Understanding-3-key-automated-DevSecOps-tools)以查找错误配置和安全漏洞。
* **动态应用程序安全测试。**在每个开发阶段运行应用程序以查找操作安全弱点和漏洞。
* **软件物料清单。**记录 [所有正在使用的代码、许可证和库](https://www.techtarget.com/searchsecurity/tip/How-to-create-an-SBOM-with-example-and-template) 以使 DevSecOps 团队能够掌握第三方和依赖项漏洞。
* **漏洞扫描器。**自动发现和缓解常见的错误配置和漏洞。
* **访问控制和策略管理。**限制谁和什么可以查看或使用软件代码以防止未经授权的访问。

## 安全即代码的优势和挑战是什么？
SaC 为组织提供了许多好处，但也带来了一些挑战。

### SaC 的优势包括：
- 在生产前识别和修复安全问题。
- 作为 DevSecOps 的一部分，促进开发、安全和运维团队之间的协作。
- 能够在 SDLC 的所有阶段实施有效的安全配置。
- 自动化跨 CI/CD 的开发过程，降低人为错误的可能性。
- 帮助使用自动安全审查加快开发速度。
- 帮助实现与适用的安全标准和法规的合规性。
- 使软件与公司关于性能和功能的策略和标准保持一致。
- 使组织能够在 SDLC 的早期发现漏洞，从而降低成本。
- 通过在生产之前识别和修复问题，改善发布后的维护。
- 提供一个
[安全审计](https://www.techtarget.com/searchcio/definition/security-audit)跟踪，以便将来分析。- 有助于防止数据泄露，这可能会
[在财务上](https://hbr.org/2023/05/the-devastating-business-impacts-of-a-cyber-breach)和声誉上损害公司。
### SaC 的挑战包括以下内容：
**初始成本。**虽然 SaC 可以帮助组织从长远来看节省资金，但在实施新工具和培训团队时，预计会有很高的投资成本。**管理角色的重新定义。**组织必须确定谁负责 SaC 活动，以确保指挥链。**企业文化。**如果安全和开发团队不习惯协作，团队可能需要根据新的工作流程或其他活动进行调整。**开发延迟。**实施 SaC 时，预计会延迟。教用户如何部署新工具可能会减慢开发过程，添加安全测试和检查也会减慢开发过程。
## 安全即代码最佳实践
以下最佳实践可以确保 SaC 的采用能够产生安全、合规且可投入生产的应用程序：

- 建立一个项目团队，其中包括业务部门、软件开发人员和安全团队成员的代表。
- 制定一个 SaC 项目计划，其中包括如何自动化关键流程和代码实施。
- 确定在不同 SDLC 阶段可能出现的安全问题。
- 收集应用程序用户故事，以从最终用户角度识别功能需求。
- 评估和选择促进 SaC 项目的工具。
- 通过自动化工具确保符合所需的
[标准和法规](https://www.techtarget.com/searchsecurity/tip/IT-security-frameworks-and-standards-Choosing-the-right-one)。- 使用测试阶段验证和优化嵌入式安全措施。
- 定期安排进度会议，并向高级管理层通报情况。
- 建立部署后维护活动，以确保应用程序及其安全措施按设计运行。
*Paul Kirvan，FBCI，CISA，是一位独立顾问和技术作家，拥有超过 35 年的业务连续性、灾难恢复、弹性、网络安全、GRC、电信和技术写作经验。*