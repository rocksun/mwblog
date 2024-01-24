<!--
title: 告别互联网时间守护者David Mills
cover: https://cdn.thenewstack.io/media/2024/01/43020ac2-pocket-watch-2036304_1280-1024x576.jpg
-->

设计出了使全球数十亿台设备实现时间同步的网络时间协议(NTP)的远见卓识者David L. Mills博士已离世。

> 译自 [Farewell to the Internet’s Master Timekeeper: David Mills](https://thenewstack.io/farewell-to-the-internets-master-timekeeper-david-mills/)，作者 Steven J. Vaughan-Nichols。

全球时间同步协议(NTP)的设计者（戴维·L·米尔斯）David L. Mills博士于2024年1月17日去世，享年85岁。该协议使数十亿台设备实现全球时间同步。

![](https://cdn.thenewstack.io/media/2024/01/e976ffaa-dl_mills-2_cropped-300x271.jpg)

芝加哥的一首歌里唱道: “[是否有人真正知道现在是什么时间](https://www.youtube.com/watch?v=xoJpyYu_NMk)？是否有人真正在意？”对互联网来说，戴维·L·米尔斯博士回答了这两个问题。

虽然米尔斯博士不及互联网协议发明者Jon Postel和TCP/IP共同创造者[Vint Cerf](https://thenewstack.io/vint-cerfs-mission-to-bring-the-internet-to-outer-space/)那样出名，但他在[网络时间协议(NTP)](https://www.geeksforgeeks.org/network-time-protocol-ntp/)方面的工作对于运行互联网至关重要，从过去到现在都是如此。正如Cerf在宣布米尔斯博士逝世消息时所写的那样: “他是[早期互联网的标志性人物](https://elists.isoc.org/pipermail/internet-history/2024-January/009265.html)。网络时间协议、早期 NSFNET 的 Fuzzball 路由器、INARG任务小组带头人、COMSAT实验室、特拉华大学，等等。”

如今，只有[网络工程师](https://thenewstack.io/networking/)会密切关注 [NTP](https://datatracker.ietf.org/doc/pdf/rfc958)。我们很少考虑在全球范围内以毫秒为单位同步时间有多困难。但是所有事物，我是说所有事物，都依赖于 NTP 的准确性。这不仅仅是互联网，还有金融市场、电网、全球定位系统、密码学，等等。 NTP 每时每刻都在[同步数十亿台设备](https://www.newyorker.com/tech/annals-of-technology/the-thorny-problem-of-keeping-the-internets-time)。

米尔斯博士进入[时间同步](https://thenewstack.io/facebook-rolls-its-own-high-precision-commodity-time-servers/)领域的旅程始于20世纪70年代，当时他在COMSAT工作，参与ARPANET(互联网的前身)的建设。他的努力导致了一套系统的开发，该系统能够以毫秒为单位同步计算机。如今，NTP不可或缺，它在全球范围内的设备上运行，确保跨大陆的协调时钟。

> 戴维·米尔斯设计的NTP每时每刻都在同步数十亿台设备。

我在80年代初几次见过他，可以说，他给我留下了深刻的印象。对于他如何维护NTP提出质疑的人，也深深体会到他不容忍愚蠢的一面。但是，没有他的努力，现代互联网将不复存在。

网络的主要时间守护者是 stratum-0 设备，即原子钟。这些设备通过NTP连接到其他设备，进而为所有联网设备设置时间。

虽然 stratum 设备属于政府机构和企业，但NTP本身是一个免费的开源项目，现在由[网络时间基金会](https://www.nwtime.org/)监督。它只有一个管理员，哈兰·斯滕（Harlan Stenn），是米尔斯亲自挑选的接班人。直到最近，他还是在家中以极小的资源运行着NTP。即便现在，[基金会也必须筹集资金来保持时间同步](https://www.nwtime.org/news/2024-ssd-appeal/)。

虽然我们最尊敬米尔斯创造NTP的贡献(1985年)，但他的 Fuzzball 路由器软件是互联网第一代路由器的基础。没有它们，就不会有互联网。他还参与了[文件传输协议(FTP)](https://www.techtarget.com/searchnetworking/definition/File-Transfer-Protocol-FTP)和[Ping](https://www.rtr.at/TKP/service/rtr-nettest/help/test_result/netztestfaq_testergebnis_0300.en.html)的创建。

随着岁月流逝，米尔斯在与青光眼的终生抗争中失败，最终导致失明。在他的一生中，他一直在致力于NTP的工作。正如他所说，“我被认为是个古板的老家伙”，但对NTP社区来说，这并没有阻止他继续参与其中。

他的成就广受认可，曾获得许多荣誉，例如1999年获选为计算机协会(ACM)会士，2002年获选为电气电子工程师学会(IEEE)会士。2013年，他因在网络协议和时间保持方面的贡献而获得IEEE互联网奖。

有一个著名的 [xkcd 漫画讽刺所有现代数字基础设施都依赖于内布拉斯加州一位无私奉献的开发者谢绝维护](https://xkcd.com/2347/)。多年来，米尔斯和NTP就是这样的例子。我们对他心存感激。我们可以通过[支持网络时间基金会](https://www.nwtime.org/news/support-network-time-foundation/)来感谢他。
