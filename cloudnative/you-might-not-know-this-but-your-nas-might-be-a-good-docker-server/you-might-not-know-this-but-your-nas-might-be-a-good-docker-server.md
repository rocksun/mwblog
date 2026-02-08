<!--
title: 没想到吧？你的NAS也能跑Docker！
cover: https://cdn.thenewstack.io/media/2026/01/44ea84d7-lucas-van-oort-bv6svakgbgm-unsplash-1.jpg
summary: 文章讲述NAS可作为Docker服务器，扩展其功能。作者成功在NAS上用Docker Compose部署Nextcloud+MariaDB，展示了其在家庭和小型企业中的巨大潜力。
-->

文章讲述NAS可作为Docker服务器，扩展其功能。作者成功在NAS上用Docker Compose部署Nextcloud+MariaDB，展示了其在家庭和小型企业中的巨大潜力。

> 译自：[You Might Not Know This, but Your NAS Might Be a Good Docker Server](https://thenewstack.io/you-might-not-know-this-but-your-nas-might-be-a-good-docker-server/)
> 
> 作者：Jack Wallen

最近，我购买了一台[Zettlab AI NAS](https://www.kickstarter.com/projects/zettlab/zettlab-ai-nas-personal-cloud-for-smart-data-management?ref=6fpvej&gad_source=1&gad_campaignid=23334065990&gclid=CjwKCAiAmp3LBhAkEiwAJM2JUOP6EzOeloI--9WDIXsPXMpY9EQLbsyNU9UQJiO48lLcMgLXL_VBgxoC5uUQAvD_BwE)。这主要是用来存放我工作所需的大量视频文件，因为我的移动硬盘经常被那些我不再需要处理但又不想删除的片段填满（你懂的……以防万一）。

部署完[NAS](https://thenewstack.io/openmediavault-a-linux-based-solution-for-building-a-nas/)后，我开始摸索，发现它有一个应用商店。好奇心驱使我打开应用商店看了看。正如我所预料的，里面有一大堆常见的应用程序。然而，有一个应用引起了我的注意。

[Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/)。

没错。我的NAS竟然内置了Docker应用。更棒的是，它不是命令行版的Docker；它是一个功能齐全的图形用户界面（GUI）。

有意思。

显然，我安装了Docker应用，虽然完全不确定它是什么。安装完成后，我打开应用，发现它是一个设计精良的GUI，允许我创建Docker项目、管理镜像和容器，以及创建和管理容器和网络。在创建容器时，你可以访问所有你需要的功能（图1），例如环境变量、限制、重启配置、存储路径、网络设置、端口设置和命令。

[![](https://cdn.thenewstack.io/media/2026/01/6e89e49f-screenshot-2026-01-14-at-1.57.19-pm-scaled.png)](https://cdn.thenewstack.io/media/2026/01/6e89e49f-screenshot-2026-01-14-at-1.57.19-pm-scaled.png)

图1：从拉取的镜像创建容器很简单。

在不到两分钟的时间里，我就能够在我的NAS中部署一个Node-Red实例。

是的，就是这么简单。

本质上，这让你能够将NAS的功能集扩展到远远超出其默认包含的范围。

这种设置唯一的缺点是我无法通过SSH访问NAS。当然，这可能不适用于你的NAS。事实上，你的NAS可能没有带有Docker的应用商店。因此，你可能会考虑购买一个支持Docker的NAS。

## 但你为什么要这样做？

这就是我为什么会在NAS上深入研究Docker的原因。当我在应用商店浏览时，我注意到了[Nextcloud](https://thenewstack.io/how-to-deploy-the-nextcloud-cloud-server-on-almalinux/)。作为这个平台的粉丝，我迅速安装了它，却发现我仅限于使用[SQLite数据库](https://thenewstack.io/the-origin-story-of-sqlite-the-worlds-most-widely-used-database-software/)，它比MySQL/MariaDB或[PostgreSQL](https://thenewstack.io/reinventing-postgresql-for-the-next-generation-of-apps/)慢得多。

卸载Nextcloud应用后，我继续寻找是否有可以安装的CMS工具（帮助我从[Google](https://cloud.google.com/?utm_content=inline+mention) Drive/Docs迁移）。就在那时，我看到了Docker的列表。我很自然地想：“我可以安装Docker，然后用MariaDB数据库部署Nextcloud。”

当然，这又带来了我面临的下一个问题。我试图设置一个MariaDB容器，然后将Nextcloud连接到它，但没有成功。我知道一定有办法做到这一点，所以我继续深入研究。

就在那时，我发现了在项目页面中创建Docker Compose文件的功能。我所要做的就是正确配置compose文件，部署它，然后等待一切启动。

搞定。一站式Nextcloud。

在我通过项目页面（和我的Docker Compose文件）部署Nextcloud后，一切都完全按预期运行。是的，我本可以直接从Zettlab应用商店安装Nextcloud应用，但我不想再处理使用SQLite运行Nextcloud的问题。

好的，但这是否回答了你为什么要费心通过NAS使用Docker的问题？毕竟，你的NAS主要是关于存储，对吧？那么，想象一下，如果你愿意，你可以（在Docker的帮助下）创建自己的、内部的Google Workspace替代品。这已经是我一段时间以来的目标了。当然，我可以为此简单地启动一些虚拟机（VM），但是当我有一个拥有足够存储空间的强大系统时，为什么不利用我已有的东西呢？

多亏了Docker，这不仅可能，而且很容易。

我意识到并非所有NAS设备都相同。你的NAS可能不支持Docker。但我知道主要的NAS设备——如群晖（Synology）、威联通（QNAP）和华硕存储（ASUSTOR）——都支持Docker，所以如果你拥有一台这样的设备，请务必启用Docker支持，这样你就可以通过容器扩展功能，并搭建自己的家庭实验室。

我喜欢这种设置的一点是，我不需要记住我为部署不同容器而部署的各种虚拟机的IP地址。我只需要记住分配给每个容器的端口。

这能在企业生产环境中工作吗？可能不行。虽然你可能可以将其用于小型部门，但大多数企业最好还是选择更传统的路径。

但是，如果你需要为你的家庭实验室（或小型企业）快速启动一个Docker容器，这可能是最好的方法。最重要的是，你还有大量的存储空间可以使用（用于容器和非容器）。

这对我来说是双赢。

如果你有NAS设备，检查它是否开箱即支持Docker，或者是否可以通过应用程序添加Docker。如果是这样，那就去玩转那些容器吧！