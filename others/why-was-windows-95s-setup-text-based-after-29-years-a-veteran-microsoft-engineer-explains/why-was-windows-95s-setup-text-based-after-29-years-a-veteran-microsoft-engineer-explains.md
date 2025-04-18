
<!--
title: Windows 95 安装界面背后的秘密，竟是工程师的无奈之举？29年后，一位资深微软工程师承认“MS-DOS可以做图形”，但公司选择了平庸的UI——因为Windows 3.1运行时已经满足了缺失的功能。
cover: https://cdn.mos.cms.futurecdn.net/wB3p4ESGaRCJYqX5FykaxN-1200-80.jpg
-->

微软员工Raymond Chen揭示了为什么基于文本的设置如此常见，尽管MS-DOS支持图形。

微软员工Raymond Chen揭示了为什么尽管MS-DOS支持图形，但基于文本的设置如此常见的原因。

2025年8月24日，微软的Windows 95操作系统将迎来30周年。感觉老了吗？Windows Central非常喜欢这个操作系统，经常报道怀旧的内容，包括它的生日、[标志性的开始菜单引入革命性的任务栏](https://www.windowscentral.com/software-apps/celebrating-29-years-of-windows-95)以及[开始菜单作为Windows 95功能的开发故事](https://www.windowscentral.com/software-apps/windows-11/microsoft-veteran-software-engineer-explains-the-development-of-the-start-menu-as-a-windows-95-feature-before-it-turned-into-a-windows-11-billboard)。

随着[Windows 10即将寿终正寝](https://www.windowscentral.com/software-apps/windows-10/microsoft-gives-a-subtle-reminder-about-the-upcoming-death-of-windows-10)以及微软加倍努力进行其[Windows 11宣传活动](https://www.windowscentral.com/software-apps/windows-11/microsoft-temporarily-pumps-the-brakes-on-its-intrusive-windows-11-ads-after-receiving-constant-backlash-from-windows-10-users)以吸引更多用户升级，一个问题仍然没有得到解答，直到最近才得到解答。*Windows 95的设置团队是否忘记了MS-DOS可以做图形？*

微软资深工程师Raymond Chen，他参与了Windows操作系统的演变超过30年，揭示了为什么公司决定使Windows 95设置基于文本而不是使用图形。

## 为什么微软的Windows 95设置是基于文本的？

![](https://cdn.mos.cms.futurecdn.net/d4ZAFjyj5y62XMmHGHyg3i-1200-80.png.webp)

与更新的微软操作系统相比，Windows 95脱颖而出。这很明显，因为它缺乏光彩的用户界面，与单调的文本一致，与其后续操作系统相比，后者在安装过程中具有丰富的图形元素。

微软工程师Raymond Chen透露，“MS-DOS（Microsoft Disk Operating System）可以做图形”。为什么微软选择基于文本的Windows 95？尽管能够支持图形，但Chen指出，操作系统对图形的支持是原始的且耗时的：

"是的，MS-DOS可以做图形，因为它并没有积极地阻止你做图形。不过，你仍然需要自己负责所有事情。除了一个绘制单个像素的BIOS调用之外，没有其他图形原语。其他一切都要靠你自己，而且你也不想使用BIOS调用来绘制像素，因为它很慢。如果你想要任何一点性能，你必须直接访问帧缓冲区。" 

这位微软工程师透露，在Windows 95的设置中加入图形将是一项艰巨的任务，因为它的原语仅限于用于绘制单个像素的BIOS调用。Chen进一步补充说，利用这种方法将图形引入设置并不是一个好主意，因为它速度很慢。解决性能瓶颈的唯一方法是直接访问帧缓冲区。

但这只是冰山一角。这个过程要复杂得多，包括编写一个用于绘制复杂图形而不是单个像素的图形库。幸运的是，Windows 95附带了最低VGA显卡系统要求，消除了对CGA或EGA的担忧。但是，你仍然需要调整平面模式，这并非易事。

![](https://cdn.mos.cms.futurecdn.net/3gEGX3NgVC6fBFUwAAywq5-1200-80.jpg.webp)

*回顾：Windows 95 于 1995 年 7 月 14 日发布生产，并于 1995 年 8 月 24 日正式向公众开放。此版本标志着个人计算领域的一个重要里程碑，其“开始”菜单和任务栏等功能至今仍为用户所熟悉（图片来源：Getty Images |Brooks Kraft）*

除了像素，安装程序还需要对话框，这也就需要你编写一个窗口管理器来补充你图形库内的标准GUI对话框界面。它还需要键盘支持，以便在元素之间切换标签并分配热键。

这个过程还包括添加对日语等非字母语言字符输入的支持。幸运的是，你可以依靠位于东京的Windows专家团队，他们正在研究日语输入法，但时差会对你的进度产生负面影响。这还不包括UI团队开发的新控件，这些控件将遵循类似的协议。

不要忘记动画需要一个调度程序来根据系统硬件定时器触发事件。你需要编写一些甚至不是Windows 95安装过程一部分的代码。也许更令人担忧的是，在付出所有努力之后，要把所有东西都压缩到只有640KB的存储空间中将是一项艰巨的任务。你可以通过编写一个保护模式管理器来利用为保护模式分配的额外存储空间来规避这个问题。

这些努力似乎适得其反，因为微软已经有一款类似的产品——Windows 3.1运行时。“它已经完全调试完毕，包括视频驱动程序、图形库、对话框管理器、调度程序、保护模式管理器和输入法。”