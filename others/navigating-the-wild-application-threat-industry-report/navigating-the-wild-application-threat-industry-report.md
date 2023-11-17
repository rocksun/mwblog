<!--
title: 荒野游荡：应用威胁产业报告
cover: https://cdn.thenewstack.io/media/2023/11/bc285b8b-wild-1024x683.jpg
-->

现有的大多数安全工具都没有监测或报告客户端应用程序面临的威胁，这一未解决的问题引起了广泛关注。

> 译自 [Navigating the Wild: Application Threat Industry Report](https://thenewstack.io/navigating-the-wild-application-threat-industry-report/)。作者Daniel Shugrue在安全和通信技术领域有超过20年的工作经验。在加入Digital.ai之前,Daniel在微软从事保密计算工作,在CyberX从事物联网安全工作,在Akamai从事Web应用防火墙安全工作,并在RSA从事认证工作。

应用程序已经走出封闭环境，进入创造者无法完全控制的“野外”。虽然局域网内的应用已经存在几十年，但智能手机的大量使用开启了移动应用新时代，无数苹果和谷歌等平台带动的应用现在已经超出这些受控网络。这一转变对理解应用程序面临的威胁至关重要，因为这些应用最容易被威胁者获取，仅2021年移动应用下载量就高达惊人的1000亿次，突显了这个现实。

同样值得注意的是，现有安全工具包括SIEM和WAF在内，几乎没有任何一种监测或报告客户端应用(网页、移动和桌面)的威胁。这一未解决的缺口带来巨大安全隐患，也强化了目前应用监测和研究的不足。

Digital.ai最近发布的[2023年应用威胁报告](https://digital.ai/resource-center/ebooks/2023-app-threat-report/)深入探讨应用安全领域，揭示应用在防火墙之外存在的普遍风险。

## 行业遭受严重威胁

报告发现，游戏和金融应用最有可能受到攻击，分别面临63%和62%的风险。金融应用储存大量敏感数据，成为主要目标。游戏应用由于金钱利益、灰色市场活动以及社区“口碑”，也倍受关注。

![](https://cdn.thenewstack.io/media/2023/11/eb7536fd-image1.png)

除游戏和金融外，其他行业面临54%的攻击风险。可植入医疗设备、汽车蓝牙应用、石油勘探和零售等行业使用的专用工具同样面临威胁。

## iOS与Android

[iOS与Android的竞争](https://thenewstack.io/scoring-comparison-android-ios-development/)不仅是用户偏好，更是代码安全的战场。普遍认为iOS因苹果的封闭环境更安全，但实际复杂得多。iOS和Android都是开放平台，关键区别在生产控制：[苹果完全控制](https://thenewstack.io/apples-browser-engine-ban-is-holding-back-web-app-innovation/)iPhone生产保持排他性，而Android将系统授权给各种设备制造商，更加开放容易被威胁者获取。Android应用遭攻击风险更高(76% vs iOS 55%)，因为Android开放特性更易遭入侵，同时应用也更容易在非安全环境如已破解手机上运行，带来巨大风险。

## 流行不意味安全

与预期相反，报告发现应用的流行度与被攻击概率之间没有相关性，这表明即使是广泛使用的应用也面临网络威胁的风险。事实上，研究显示许多知名应用遭受攻击的频率与不太知名的应用一样高。这一发现强调了在应用中内置安全性的重要性，也再次提醒我们数字世界的表象可能会具有欺骗性。

![](https://cdn.thenewstack.io/media/2023/11/82afd2f5-image2.png)

## 防止攻击

为保护应用，必须在[整个开发过程中深入应用代码安全](https://thenewstack.io/security-as-code-protects-rapidly-developing-cloud-native-architectures/)。代码混淆、检测非安全环境以及自定义或自动化保护等技术，对抵御恶意反编译至关重要。进一步分析显示，在iOS和Android平台上，经常实现的保护措施触发报警更频繁，表明其有效性。令人惊讶的是，即使实施不多的保护措施也有同样高的触发率，这表明实现更多保护措施可能带来价值。这说明应用安全的动态特性——组织必须不断调整和增强防御以跟上不断演变的威胁，不能用“设置后不管”的心态处理安全。

## 展望未来

报告数据可作为基准，帮助相关方了解不断变化的威胁环境。高级反编译工具、加密货币促进犯罪以及国家支持的攻击等因素导致2023年威胁风险升高。这突显一个事实：组织必须警惕并积极应对这些威胁。

在应用肆意游荡的时代，代码安全不能成为事后考量。建立强大安全措施、了解不同行业和平台的风险以及防患于未然，对任何依赖数字应用的组织都至关重要。2023年应用威胁报告为加强应用安全指明方向，面对数字领域的野外挑战。

完整报告请参见[此处](https://digital.ai/resource-center/ebooks/2023-app-threat-report/)。