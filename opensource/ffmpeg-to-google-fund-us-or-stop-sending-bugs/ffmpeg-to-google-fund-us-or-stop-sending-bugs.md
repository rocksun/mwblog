<!--
title: FFmpeg硬核喊话谷歌：不给钱就别再报Bug！
cover: https://cdn.thenewstack.io/media/2025/11/0c7ed4fb-allison-saeng-roanyq5ym74-unsplash.jpg
summary: FFmpeg与谷歌因AI发现漏洞修复责任起争议。FFmpeg志愿者项目资金不足，呼吁大公司提供更多支持，以维持关键开源软件。
-->

FFmpeg与谷歌因AI发现漏洞修复责任起争议。FFmpeg志愿者项目资金不足，呼吁大公司提供更多支持，以维持关键开源软件。

> 译自：[FFmpeg to Google: Fund Us or Stop Sending Bugs](https://thenewstack.io/ffmpeg-to-google-fund-us-or-stop-sending-bugs/)
> 
> 作者：Steven J. Vaughan-Nichols

您可能从未听说过 [FFmpeg](https://www.ffmpeg.org/)，但您使用过它。这款[开源](https://thenewstack.io/the-reality-of-open-source-more-puppies-less-beer/)程序强大的多媒体框架被用于处理众多平台和设备上的视频和音频媒体文件及流。它为音频和视频媒体提供格式转换（即转码）、播放、编辑、流媒体和后期制作效果的工具和库。

FFmpeg 的库，例如 [libavcodec](https://ffmpeg.org/libavcodec.html) 和 [libavformat](https://ffmpeg.org/doxygen/trunk/group__libavf.html)，对于媒体播放器和软件至关重要，包括 VLC、Kodi、Plex、Google Chrome、Firefox，甚至 YouTube 的视频处理后端。与其他许多重要的[开源程序一样，它也面临着资金严重不足的问题](https://thenewstack.io/can-open-source-sustain-itself-without-losing-its-soul/)。

## 企业责任与志愿者劳动

在 Twitter 上，软件供应链安全公司 [Chainguard](https://www.chainguard.dev/?utm_content=inline+mention) 的首席执行官兼联合创始人 [Dan Lorenc](https://www.linkedin.com/in/danlorenc) 与 FFmpeg 项目、[Google](https://cloud.google.com/?utm_content=inline+mention) 以及安全研究人员之间，围绕安全披露和大型科技公司在开源软件中的责任问题，展开了一场激烈的辩论。

讨论的核心围绕漏洞应如何报告、谁负责修复这些漏洞，以及当人工智能被用来发现大量可能毫无意义的安全问题时所带来的挑战。但归根结底，这一切都与金钱有关。

## 一个鲜为人知的漏洞点燃争议

这场讨论已经持续了一段时间。10 月中旬，FFmpeg 在推特上发文称，“[FFmpeg 非常重视安全问题](https://x.com/FFmpeg/status/1979066506030793116)，但修复工作由志愿者完成。” 这一点再怎么强调也不为过。正如 FFmpeg 后来在推特上所说，“[FFmpeg 几乎完全由志愿者编写。](https://x.com/FFmpeg/status/1982592087494398164)”

因此，正如开源政策专家 [Mark Atwood](https://www.linkedin.com/in/-mark-atwood/) 在 Twitter 上指出的那样，他不得不一直告诉 [Amazon](https://aws.amazon.com/?utm_content=inline+mention) 不要做出会搞砸 FFmpeg 的事情，因为他必须不断向他的老板解释：“[他们不是供应商，没有保密协议，我们没有任何影响力，](https://x.com/_Mark_Atwood/status/1978888607298691279) 你们的副总裁拒绝提供资金支持，他们明天就可以通过一封电子邮件扼杀三个主要产品线。所以，停下来，听我说……”

## 开源维护者日益增长的负担

最新一集事件的导火索是 Google 的一个 AI 代理在 FFmpeg 中发现了一个极其鲜为人知的漏洞。有多鲜为人知？这个“[FFmpeg 中的中等影响问题](https://issuetracker.google.com/issues/440183164)”（FFmpeg 开发者确实修补了）是“一个关于[解码 LucasArts Smush 编解码器](https://x.com/FFmpeg/status/1983949866725437791)的问题，具体来说是 1995 年游戏 Rebel Assault 2 的前 10-20 帧。”

哇。

FFmpeg 补充说，“FFmpeg 的目标是播放所有曾制作过的视频文件。” 这固然很好，但这对于汇编程序员的时间来说是一个有价值的用途吗？哦，对了，您可能不知道。FFmpeg 的核心是汇编语言。作为一名前汇编语言程序员，汇编语言绝不是任何形式的易于使用的语言。

正如 FFmpeg 所说，这是“[CVE 漏洞堆积。](https://x.com/ffmpeg/status/1984207514389586050)”

FFmpeg 社区中的许多人有理由认为，像谷歌这样在产品中严重依赖 FFmpeg 的万亿级公司，将修复漏洞的工作量转移给无偿志愿者是不合理的。他们认为谷歌要么在漏洞报告中提供补丁，要么直接支持项目的维护。

此前，FFmpeg 指出，它远不是唯一面临此类问题的开源项目。

具体来说，项目团队提到了 [Nick Wellnhofer](https://www.linkedin.com/in/nwellnhof/)，他是 [libxml2](https://gitlab.gnome.org/GNOME/libxml2) 的前维护者，libxml2 是一个广泛使用的用于解析可扩展标记语言（XML）的开源软件库。[Wellnhofer 最近辞去了 libxml2 维护者的职务](https://discourse.gnome.org/t/stepping-down-as-libxml2-maintainer/31398)，因为他每周必须“花费数小时处理第三方报告的安全问题。这些问题中的大多数都不关键，但仍然是大量的工作。”

“从长远来看，[这对于我这样无偿的志愿者来说是不可持续的。](https://gitlab.gnome.org/GNOME/libxml2/-/issues/913)……从长远来看，对开源软件维护者提出这样的要求而不给予补偿是有害的。……有 Google Project Zero 这样用金钱能买到的最好的白帽安全研究人员紧盯着志愿者，情况就更不可能好转了。”

## 谷歌有争议的安全漏洞披露政策

这件事之所以成为热门话题，是因为早在 7 月份，[Google Project Zero (GPZ)](https://googleprojectzero.blogspot.com/) 就宣布试行其新的[报告透明度](https://googleprojectzero.blogspot.com/2025/07/reporting-transparency.html)政策。根据这一政策变化，GPZ 宣布在发现问题后的一周内向特定项目报告问题，然后，无论补丁是否可用，90 天的安全标准披露倒计时都会开始。

许多志愿开源程序维护者和开发者认为，当谷歌拥有数十亿资金来解决问题时，让他们承受如此大的压力是极其不公平的。

FFmpeg 在推特上发文称：“[我们非常重视安全](https://x.com/FFmpeg/status/1984178359354483058)，但同时，万亿级公司运行人工智能来查找人们兴趣代码中的安全问题，然后期望志愿者修复，这真的公平吗？”

确实，谷歌确实提供了一个[补丁奖励计划](https://bughunters.google.com/about/rules/open-source/4928084514701312/patch-rewards-program-rules)，但正如一位名为 Ignix The Salamander 的 Twitter 用户观察到的，“[FFmpeg 已经提到该计划对他们来说限制太多](https://x.com/ignixsalamander/status/1986111396095074689)，他们指出了每月三个补丁的限制。请不要假设人们抱怨只是为了抱怨，在我看来，企业安全与使用和开源支持之间存在真正的冲突。”

Lorenc 在给我的一封电子邮件中反驳道：“以开源许可证创建和发布软件是对数字公共领域的贡献。发现和发布关于该软件安全问题的信息同样是对同一公共领域的贡献。”

“FFmpeg 的 X 账号的立场是，披露漏洞在某种程度上是一件坏事。谷歌为开源软件项目提供的帮助比几乎任何其他组织都多，而这些辩论更有可能吓跑潜在赞助商，而不是吸引他们。”

## 漏洞披露的不同观点

根本问题仍然是 FFmpeg 团队缺乏财力和开发人员资源来处理大量人工智能生成的 CVE 漏洞。

另一方面，安全专家肯定认为 FFmpeg 是互联网技术框架的关键组成部分，安全问题确实需要负责任地公开和解决。毕竟，黑客可以像谷歌使用其 AI 漏洞查找器 [Big Sleep](https://googleprojectzero.blogspot.com/2024/10/from-naptime-to-big-sleep.html) 一样，使用 AI 来查找漏洞，而谷歌希望在他们之前识别潜在的安全漏洞。

然而，现实情况是，如果没有万亿级公司为从开源中获利而提供更多支持，许多资金严重不足、由志愿者驱动的关键开源项目将根本无法继续维护。

例如，[Wellnhofer 表示他将于 12 月起不再维护 libxml2](https://discourse.gnome.org/t/stepping-down-as-libxml2-maintainer/31398)。Libxml2 是所有网页浏览器、网页服务器、LibreOffice 和众多 Linux 软件包中的关键库。我们不需要更多争论；在发生另一次重大安全漏洞之前，我们需要为关键[开源程序](https://thenewstack.io/open-source/ "开源程序")提供真正的支持。