<!-- 
# 3个技巧来保护你的云基础设施和工作负载
https://cdn.thenewstack.io/media/2023/04/f9571259-shutterstock_2-1024x683.jpg
 -->

采用全方位的方法，以可视性、威胁情报和威胁检测为基础，组织可以发挥云的优势而不会牺牲安全性。

译自 [3 Tips to Secure Your Cloud Infrastructure and Workloads](https://thenewstack.io/3-tips-to-secure-your-cloud-infrastructure-and-workloads/) 。

随着公司转向云服务以获得效率和可扩展性的好处，安全团队的工作就是让它们能够安全地这样做。

在这种情况下，IT领导者必须了解威胁者是如何[针对他们的云基础设施](https://www.crowdstrike.com/resources/white-papers/crowdstrike-security-cloud-guidebook/?utm_campaign=blog&utm_medium=syn&utm_source=cont)的。可以想象，攻击者首先瞄准最容易利用的系统和应用程序。

在[2023年CrowdStrike全球威胁报告](https://www.crowdstrike.com/global-threat-report/?utm_campaign=blog&utm_medium=syn&utm_source=cont)中，我们的研究人员注意到:

- 攻击者瞄准计划停用但仍包含敏感数据的被忽视的云基础设施。
- 利用缺乏出站限制和工作负载保护泄露数据。
- 利用常见的云服务来掩盖恶意活动。

### 被忽视或配置错误的云基础设施

被忽视的和即将退役的基础设施通常会成为攻击者的首要目标，因为这些基础设施不再接收安全配置更新和定期维护。 这些资产上已经不存在监控、日志记录、安全架构和规划以及管理状态等安全控制措施。

### 缺乏出站限制和容器生命周期安全性

遗憾的是，我们仍然看到一些被忽视的云基础设施中仍包含关键业务数据和系统。因此，攻击导致需要高昂调查和报告义务的敏感数据泄露。此外，一些针对废弃云环境的攻击导致了重大的服务中断，因为它们仍在提供关键服务，这些服务还没有完全过渡到新基础设施。此外，这些环境中的事件的分类、遏制和恢复对一些组织产生了巨大的负面影响。

### 从云中发起攻击

攻击者不仅针对云基础设施，我们还观察到威胁行为者[利用云使他们的攻击](https://www.crowdstrike.com/resources/reports/threat-landscape-cloud-security/?utm_campaign=blog&utm_medium=syn&utm_source=cont)更有效。过去一年中，威胁行为者使用了众所周知的云服务，如Microsoft Azure，以及数据存储同步服务，如MEGA，来泄露数据和代理网络流量。缺乏出站限制以及缺乏工作负载保护使威胁行为者能够通过代理与云中的IP地址进行交互来访问本地服务。这给攻击者提供了额外的时间来审查系统和从伙伴运营的基于Web的API到数据库等各种服务中窃取数据 - 所有这些看起来都来自受害者网络内部。这些策略使攻击者几乎没有在本地文件系统上留下痕迹，从而避免了检测。

## 那么，我该如何保护我的云环境？

与传统的内部数据中心模型相比，云引入了新的保护难点。安全团队应牢记以下几点，以遵循最佳实践。

- **启用运行时保护以获得实时可视性**。如果你看不到，你就无法保护，即使你有计划要停用基础设施。防止数据泄露的关键是云[工作负载保护(CWP)](https://www.crowdstrike.com/resources/white-papers/cloud-workload-protection-platform-buyers-guide/?utm_campaign=blog&utm_medium=syn&utm_source=cont)提供的运行时保护和可视性。无论工作负载驻留在内部数据中心、虚拟集群还是托管在云中的服务器、工作站和移动设备，使用新一代终端保护保护工作负载仍然至关重要。

- **消除配置错误**。云入侵的[最常见根源](https://www.crowdstrike.com/resources/white-papers/how-to-find-and-eliminate-blind-spots-in-the-cloud/?utm_campaign=blog&utm_medium=syn&utm_source=cont)仍然是管理活动中引入的人为错误和疏漏。在设置新基础设施时采用默认模式非常重要，这可以轻松地采用安全操作。一种方法是使用云帐户工厂轻松创建新的子帐户和订阅。这种策略可以确保以可预测的方式设置新帐户，消除常见的人为错误来源。还要确保设置角色和网络安全组，使开发人员和操作员不需要构建自己的安全配置文件并且不小心地做得很糟糕。

- **利用云安全态势管理(CSPM)解决方案**。确保您的云帐户工厂包括启用详细日志记录和[CSPM](https://www.crowdstrike.com/cybersecurity-101/cloud-security/cloud-security-posture-management-cspm/)，如CrowdStrike [Falcon Cloud Security](https://www.crowdstrike.com/products/cloud-security/)中包含的[安全态势](https://www.crowdstrike.com/products/cloud-security/cloud-security-posture-management-cspm/)，并通知负责云操作和安全运营中心(SOC)团队的各方。主动查找未经管理的云订阅，一旦找到，不要假设它由其他人管理。相反，确保识别并激励负责方停用任何影子IT云环境，或者将其全部纳入管理，连同您的CSPM一起。然后，在帐户或订阅完全关闭之前，对所有基础设施使用CSPM，以确保运营团队具有持续的可视性。

由于云具有动态性，因此保护它所用的工具也必须具有动态性。 只关注特定领域的独立安全产品无法提供从端点到不同云服务的攻击所需的可视性。 但是，通过以可视性、威胁情报和威胁检测为基础的全面方法，组织可以在[不牺牲安全的前提下](https://www.crowdstrike.com/resources/white-papers/the-crowdstrike-security-cloud-ebook/?utm_campaign=blog&utm_medium=syn&utm_source=cont)充分利用云。