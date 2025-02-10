# [美国]阻止这些国家的开源“帮助”

![[美国]阻止这些国家的开源“帮助”的特色图片](https://cdn.thenewstack.io/media/2025/01/9bc965e3-sarah-kilian-xit3ljrvkvm-unsplash-1024x683.jpg)

很久以前，当我成为一名程序员时，我最不认为自己需要了解的是知识产权 (IP) 法。好吧，我真是个傻瓜。现在，几十年后，新一代开发人员发现自己面临着政府法规，这将使他们的生活变得复杂。

为了应对这一发展，[Linux 基金会](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention)发布了一份综合指南，以帮助[开源开发人员了解美国外国资产控制办公室 (OFAC) 制裁的复杂情况](https://www.linuxfoundation.org/blog/navigating-global-regulations-and-open-source-us-ofac-sanctions)。

OFAC 制裁是[美国]政府法规，用于限制或禁止与某些国家、实体和个人（称为“制裁目标”）的交易。

这些规则旨在实现经济、外交政策和国家安全目标，适用于各种互动，包括开源社区中的互动。总的[制裁计划和国家/地区](https://ofac.treasury.gov/sanctions-programs-and-country-information)列表包含超过 17,000 个条目，范围从个人到恐怖组织再到国家/地区。

如果这听起来很熟悉，那是因为在 2024 年 10 月，Linux 内核开发人员遇到了这个问题。Linux 内核的领导层，包括 [Greg Kroah-Hartman](https://thenewstack.io/greg-kroah-hartman-lessons-for-developers-from-20-years-of-linux-kernel-work/)（稳定的 Linux 内核维护者）和 [Linus Torvalds](https://thenewstack.io/linus-torvalds-on-security-ai-open-source-and-trust/)（[Linux](https://thenewstack.io/learning-linux-start-here/) 的创始人），宣布已将 11 名[俄罗斯内核开发人员从他们从事 Linux 内核工作的岗位上移除](https://www.zdnet.com/article/why-remove-russian-maintainers-of-linux-kernel-heres-what-torvalds-says/)。

为什么？因为正如 Torvalds 所说，由于“俄罗斯制裁”。他补充说，在 Linux 内核邮件列表 (LKML) 消息中，这是因为[“各种合规性要求”不仅仅是[美国]的事情。](https://lore.kernel.org/all/CAHk-=whNGNVnYHHSXUAsWds_MoZ-iEgRMQMxZZ0z-jY4uHT+Gg@mail.gmail.com/)

对于开发人员来说，这意味着要谨慎对待与谁互动以及他们的贡献来自哪里。制裁针对特定国家、地区和个人或组织，其中许多列在[特别指定国民和被阻止人员 (SDN) 名单](https://ofac.treasury.gov/faqs/topic/1631)上。

## 这对开发人员意味着什么

Linux 基金会的指南强调了开源开发人员的几个关键方面：

- 超出 SDN 名单：建议开发人员不要仅仅依赖 OFAC SDN 名单，因为它并不详尽。该指南强调了“50% 规则”，即 SDN 拥有 50% 或以上所有权的实体也受到制裁。
- 信息豁免：大多数 OFAC 制裁都对“信息材料”豁免，这通常包括开源代码。但是，这仅适用于现有代码，不适用于对新代码或修改的请求。因此，例如，与俄罗斯开发人员合作开发代码补丁可能会让您陷入困境。
- 避免双向互动：虽然审查来自受制裁地区贡献者的非主动请求的补丁通常是可以接受的，但积极与他们进行讨论或改进可能会跨越法律界限。
- 间接贡献：警告开发人员要警惕受制裁实体试图通过第三方或“单独”行动的开发人员间接做出贡献。

Linux 基金会的指南旨在帮助您平衡法律合规性和开源协作的精神。虽然承认开源社区不能独立于国际制裁运作的令人失望的现实，但该基金会强调了理解和遵守这些法规的重要性。

这绝非易事。我请著名的开源许可律师 [Heather Meeker](https://www.linkedin.com/in/heathermeeker) 谈谈她的看法。她回答说：“世界正变得越来越保护主义，而开源则相反——是典型的自由贸易。看看本周 DeepSeek 发生了什么——[热门的、基于开源的新人工智能程序](https://thenewstack.io/icymi-deepseek-is-an-open-source-success-story/)——你就可以知道保护主义的效果如何了。”
但你能做什么呢？[米克]说：“说实话，小公司通常会忽略这样的规定，因为他们没有资源来分析这些规定，而政府通常会忽略小公司，因为它没有资源来对它们进行强制执行。受到关注的大公司需要专门的顾问。一般的商业律师无法跟上新法规的步伐，更不用说遵守这些法规的最佳实践了。”

随着开源和政府监管环境在全球政治紧张局势中不断演变，本指南是开发人员应对技术、法律和国际关系复杂交叉领域的一个很好的资源。

祝大家好运。我很高兴只是在报道这些法规，而不是试图去遵守它们。

[目前受到制裁的]国家包括：

- 古巴
- 伊朗
- 朝鲜
- 俄罗斯
- 叙利亚
- 乌克兰的以下地区：克里米亚、乌克兰的顿涅茨克和卢甘斯克地区。

其他制裁可能会阻止其他国家的特定公司。接受之前请检查。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，即可观看我们所有的播客、访谈、演示等。