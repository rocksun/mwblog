# 专为开发者提供“减压阀”的Flutter分支

![专为开发者提供“减压阀”的Flutter分支的特色图片](https://cdn.thenewstack.io/media/2025/01/8719e929-flock_a_flutter_fork-1024x683.jpg)

前谷歌高级工程师兼Flutter开发者表示，他亲眼目睹了开源的阴暗面——反应迟钝、误报频发、却忽略真正的问题。

他表示，自己被指控犯下各种错误，从不与Flutter团队沟通到试图破坏这个跨平台框架。这一切是怎么发生的？

他和创建了Flutter的分支[Flock](https://getflocked.dev/)，他们表示，这个替代方案将尽可能保持与Flutter一致，同时充当“减压阀”，直到Flutter能够解决社区提出的各种尚未解决的修复请求。

他希望社区能够听取他的意见，并给Flock一个机会。他最近在一系列播客中辩称，社区中太多人完全误解了他的意图。


## 一些事实

据了解，这并非Flutter第一次被分支。当被问及Flock的创建时，一位谷歌发言人指出，多年来Flutter已被分支数千次，并补充说：“出于多种原因（例如研究实验性想法或针对特定用例调整项目），这是开源中的正常程序。”

还有这一点：Carroll一再表示，Flock实际上并非旨在创建一个完全独立产品的分支。

他在与[Viktor Lidholt](https://github.com/vlidholt)（[Serverpod](https://github.com/serverpod/serverpod)的创始人，一个基于[Dart](https://thenewstack.io/industry-observer-sees-growing-interest-in-dart-flutter/)的服务器解决方案）的[播客](https://www.youtube.com/watch?v=6Xu71_I8Jow)访谈中表示：“我们并非要偏离Flutter。我们说的是，确实有人需要一些Flutter没有提供的东西。所以，如果你的问题都能得到解决，正如你所说，你提交的每个错误都能被合并，那就太好了。我希望你继续向Flutter提交问题，也希望他们继续修复你的错误。”

他补充说，在Flock考虑请求之前，必须向Flutter提交问题。


## 分支背后的原因

Carroll告诉Lidholt，并非每个人都能获得Flutter的快速响应。

Carroll为[Super Editor](https://supereditor.dev/)做贡献，这是一个用于Flutter的开源文档编辑和阅读工具包。他表示，Super Editor团队提交了数十个影响付费客户的问题，但这些问题很少得到解决。

这位Flutter顾问还与遇到类似问题的客户进行了交谈。

Carroll告诉Lidholt：“Flutter社区的人们需要充分理解的一点是，你的良好体验并不排除其他人的糟糕体验。我为那些有糟糕体验的人发声，并不是对那些有良好体验的人的轻视。”

在[Flutter Spaces播客](https://getflocked.dev/blog/posts/flutter-spaces-flock-announcement/)中，Carroll和Ezell讨论了这个分支。Ezell承认人们不喜欢这个分支的想法，但补充道：“几年来，我们一直生活在一个不得不进行分支才能阻止应用程序崩溃的现实中。”

“对于那些提交问题并苦苦哀求却无法得到修复或功能的公司，我们想要一个社区压力释放阀，一个当Flutter团队无法解决问题时可以去的地方。”

——Matt Carroll，Flutter顾问和Flock的共同创建者

“起初，我们试图与Flutter团队合作，并试图提交问题，但我们从未真正获得进展，”Ezell说。“与此同时，我们的应用程序在生产环境中崩溃了，所以我们尝试更努力地改进错误描述，并试图让团队关注它们，但我们从未真正成功。”

他说，Flock可以作为那些问题未得到解决的人的“压力释放阀”。

“对于那些提交问题并苦苦哀求，却无法得到修复或功能的公司，我们想要一个社区压力释放阀，一个当Flutter团队无法解决问题时可以去的地方，”他说。

他的想法是，Flock团队可以创建修复程序或提供修复路径，直到Flutter能够[赶上或添加错误](https://thenewstack.io/meet-early-the-ai-that-catches-bugs-before-they-bite/)修正到核心产品中。

Carroll和Ezell还计划创建一套工具，使人们更容易创建自己的分支。他们称之为Nest。
《The New Stack》询问谷歌Flutter是否有未响应的修复积压问题，谷歌回应称他们持续投资Flutter及其社区。发言人提到了Flutter最近的“[Flutter in Production](https://medium.com/flutter/flutter-in-production-f9418261d8e1)”活动和[Flutter 3.27](https://medium.com/flutter/whats-new-in-flutter-3-27-28341129570c)的发布。

## 反弹

在[宣布fork的博客文章](https://getflocked.dev/blog/posts/we-are-forking-flutter-this-is-why/)中，Carroll概述了大部分内容。但信息在翻译中丢失了，或者可能根本无关紧要，因为出现了强烈反弹——以至于Carroll表达了对这篇文章的担忧，将《The New Stack》引导到[Flock博客](https://getflocked.dev/blog/)和两个播客，他在那里试图澄清Flock的意图。

Carroll面临的一个批评是，他应该在fork Flutter之前与Flutter团队沟通。但Carroll告诉Lidholt，他多年来一直在给他们写信。

“如果他们想和我合作，我们就会一起工作，”他告诉Lidholt。“我从未拒绝过电话；我从未拒绝过电子邮件。我从未忽略过任何一个。我从未采取任何措施不去与那个团队合作。但他们确实让我与他们合作变得非常困难。”

Carroll对Lidholt评论此事感觉“有点像对Flutter社区的挑衅”表示异议。

“这种观点并不新鲜，但是，不，我完全不同意，”他说。“这个社区已经相信，指出令人不安的事实等同于恃强凌弱……我完全不同意这一点。如果你对别人对问题的描述有情绪反应，那不是描述问题的人的错。”

## 接下来的计划

目前，Flock仍在努力吸引负责人来帮助管理项目，以及贡献者。Carroll通过LinkedIn告诉TNS，大约有40人表达了兴趣，他希望为该框架获得一些前进动力。

[YOUTUBE.COM/THENEWSTACK 科技发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)