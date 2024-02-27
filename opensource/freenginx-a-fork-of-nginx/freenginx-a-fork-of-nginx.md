<!--
title: Freenginx: Nginx的分叉
cover: https://cdn.thenewstack.io/media/2024/02/52f38ce8-freeginx-1024x683.png
-->

Freenginx Web服务器致力于重现开源开发“造福公众”的精神，摆脱企业控制。

> 译自 [Freenginx: A Fork of Nginx](https://thenewstack.io/freenginx-a-fork-of-nginx/)，作者 Steven J. Vaughan-Nichols 也称为 sjvn，自从 CP/M-80 成为尖端的 PC 操作系统，300bps 成为快速的互联网连接，WordStar 成为最先进的文字处理器以来，他就一直撰写有关技术和技术业务的文章，而我们也很享受这一切。

一名志愿的 Nginx 开发者正在把 [Nginx](https://www.nginx.com/?utm_content=inline-mention)(发音为 EngineX，是世界上最流行的 Web 服务器分叉为 Freenginx。
 
根据 [Netcraft](https://www.netcraft.com/) 的统计，Nginx 是[世界上最受欢迎的 Web 服务器](https://www.netcraft.com/blog/january-2024-web-server-survey/)。因此，当 Nginx 的顶级开发者 Maxim [Dounin](https://mailman.nginx.org/pipermail/nginx-devel/2024-February/K5IC6VYO2PB7N4HRP2FUQIBIBCGP4WAU.html) [宣布他要分支 Nginx](https://mailman.nginx.org/pipermail/nginx-devel/2024-February/K5IC6VYO2PB7N4HRP2FUQIBIBCGP4WAU.html) 时，这可能是一个巨大的举动。
 
Dounin 做出这个决定是因为他对 Nginx 的企业所有者 [F5](https://www.f5.com/) 在项目管理方面的过度干预感到不满。具体来说，他讨厌管理层在安全策略方面所做的事情，以及他们现在如何在 Nginx 的实验性 HTTP/3 代码中分配常见漏洞和披露(CVE)错误。
 
正如 Dounin 写的:"F5 的一些新的非技术管理人员最近决定他们更了解如何运行开源项目。特别是，他们决定干预 Nginx 多年来使用的安全策略，无视策略和开发者的立场。" 具体来说，Douin 反对将这些错误视为安全问题，而是将其视为普通错误，这并不值得进行安全公布。
 
然而，与其说是这个具体问题，不如说是 F5 的态度，正如他在另一个说明中解释的那样。"[并没有公开讨论](https://freenginx.org/pipermail/nginx-devel/2024-February/000002.html)。我所知道的唯一讨论发生在 security-alert@ 邮件列表中，共识是该错误应该作为普通错误进行修复。尽管如此，我还是在几天前收到信息，说一些无名的管理层不管政策和开发者的立场，坚持要求发布安全公告和安全版本。"
  
被忽视的高级程序员就是火气很大的程序员。

根据他自己的说法，自从 F5 公司因入侵乌克兰而在 2022 年[退出俄罗斯](https://my.f5.com/manage/s/article/K59427339)以来，Dounin 就不再是 F5 的员工。相反，在过去两年中，他一直是重要的志愿贡献者。

现在，他觉得虽然由于“我不再能够控制 F5 内的 Nginx 更改，也不再将 nginx 视为为公共利益开发和维护的自由开源项目”，F5 有权随意处置这个项目，但他不会再为 Nginx 工作。相反，他将为 [Freenginx](https://freenginx.org/) 工作，“这是一个替代项目，它将由开发者而不是企业实体来运行。” 

正因如此，Dounin 没有加入之前的开源 Nginx 分支 [Angie](https://angie.software/en/)。这个程序是由在 F5 退出莫斯科后遭遇困境的俄罗斯 Nginx 开发者创建的。Angie 属于俄罗斯公司 Web Server，Dounin 担心任何营利公司都可能干扰代码的适当开发和维护。

这一发展的背景复杂，涉及地缘政治紧张局势、企业收购以及在商业利益与开源理念之间寻求平衡的固有挑战。Nginx 的历史一直很动荡。[F5 在 2019 年收购 Nginx](https://www.zdnet.com/home-and-office/networking/f5-acquires-nginx-what-to-expect-from-the-deal/) 被视为一个带来财务稳定和增长的新篇章。然而，随后[俄罗斯国家代理人代表](https://www.zdnet.com/article/russian-police-raid-nginx-moscow-office/)俄罗斯网络公司 Rambler 突袭 Nginx 在莫斯科的办公室，声称拥有 Nginx 代码的所有权，这使该公司陷入困境。F5 关闭莫斯科办事处只增加了叙述的复杂性。

Dounin 的新创业 Freenginx 旨在重拾开源开发的精神，“为公共利益”服务，摆脱企业控制。Freenginx 的第一个代码版本 [freenginx-1.25.4](https://freenginx.org/en/download.html) 已于 2022 年 2 月 20 日发布。这是一个旧代码库的克隆，只做了几项较小的更改。其中一项是[修复导致分叉的错误](https://freenginx.org/pipermail/nginx/2024-February/000031.html)。

那么 F5 对此作何反应呢?一位公司代表说:“F5 致力于提供成功的开源项目，这需要大量不同的贡献者社区，以及运用严格的行业标准来分配和评分已识别的漏洞。我们认为这是为客户和社区开发高度安全软件的正确方法，我们鼓励开源社区加入我们的努力。” 在我看来，他们对这个分支并不担心。

因此，至少就目前而言，Dounin 似乎可以自由地尝试在无干扰的情况下获得网络服务器的关注度。但是，[根据 Freenginx 邮件列表中的低活跃度](https://freenginx.org/mailman/listinfo/nginx)，似乎兴趣不大，但只有时间才能告诉我们这个项目是否会在用户或开发者中获得热度。

