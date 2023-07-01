# Penpot 吸引开发者，用开源工具挑战 Figma

帮助开发者与设计师协作的工具正成为一种趋势。Figma 和 Canva 一直在宣传他们的开发工具，现在 Penpot 也开始了。

翻译自 [Penpot Woos Developers, Takes on Figma with Open Source Tool](https://thenewstack.io/penpot-woos-developers-takes-on-figma-with-open-source-tool/) 。

![](https://cdn.thenewstack.io/media/2023/06/6a836d1a-penpot_workspace_screenshot2022-1024x506.jpg)

去年 9 月，当 Adobe 宣布以 200 亿美元[收购设计工具 Figma](https://thenewstack.io/adobe-buys-figma-what-does-this-mean-for-web-standards/) 时，一个名为 Penpot 的开源替代品立即开始出现注册激增。 [Penpot](https://penpot.app/) 是由一家名为 Kaleidos 的西班牙公司开发的，自从今年2月正式发布以来，其持续快速增长。据 Kaleidos 报道，自那时以来， Penpot 的注册用户增长了 66％ ，达到了 40 万用户。

在 Kaleidos 首次举办开发者活动 Penpot Fest 之前，我与 Penpot 的创始人兼 Kaleidos 的首席执行官 Pablo Ruiz-Múzquiz 进行了交谈。在该活动上， Kaleidos 推出了一套新工具，旨在“进一步改善设计师和开发者之间的协作”。他们还与 Tokens Studio 合作，这是一个流行的设计代币插件（以前称为 “Figma Tokens” ），以“构建本地 Penpot 兼容性和能够生成设计系统和关键设计工作流的 AI 引擎”。

我首先询问 Ruiz-Múzquiz 关于 Penpot 的起源， Penpot 在 2021 年推出了测试版。他解释说， Penpot 是源于他们注重开源的软件开发机构 Kaleidos 内部对设计和原型工具的需求。当公司开始雇佣内部设计师时， Ruiz-Múzquiz 意识到他需要一些工具来与他们协作。

Kaleidos 首先创建了 [Taiga](https://taiga.io/) ，一个开源的项目管理工具。其目标是将新的设计师员工纳入到 Kaleidos 开发人员坚持的敏捷（具体而言是精益） DevOps 流程中。然后他们开始创建一个开源的设计和原型工具 Penpot ，该工具使设计师能够与公司的开发者一起协作。

Ruiz-Múzquiz 解释说：“我们确保我们构建的任何东西都真正欢迎开发者参与到设计过程中，就像我们欢迎设计师以 Taiga 参与‘精益’流程一样。”

![Using Penpot to prototype an app.](https://cdn.thenewstack.io/media/2023/06/b7ec715a-penpot-workspace_prototyping.png)
*使用 Penpot 搭建原型*


这两个产品一经发布并在开源社区中获得一些初步反响后，Kaleidos 决定全职投入其中。

Ruiz-Múzquiz 说：“在做咨询业务 10 年后，我们决定抛弃所有这些，转型成一个 100％ 开源产品公司，既有 Taiga 也有 Penpot 。”

起初，Penpot 的目标是设计师，因为 Kaleidos 希望迎合一个习惯于使用昂贵工具（比如 Adobe 套件）的挑剔受众。他们希望确保设计师对 Penpot 感到满意，同时考虑到能够吸引开发者的功能。

## 开发者带来可扩展性

Ruiz-Múzquiz 说，Penpot 目前约有三分之一的用户是开发者，但他认为随着时间推移，“由于有更多的开发者存在”，这一比例将会增长。

他认为，仅为设计师构建工具是不可持续的。开发者带来了可扩展性，无论是在受众范围还是在使用工具创建的项目方面。

话虽如此，Ruiz-Múzquiz 还表示，设计师对 Penpot 产品的影响非常大。他的公司在 Penpot 项目上的设计师与开发人员的比例为1:2，他表示这在该行业中是不寻常的，通常情况下是 1:10 、 1:7 或 1:8 。

他还表示，一些与 Penpot 竞争的工具将开发人员视为事后考虑的对象，他们花费了太长时间来"转变"并考虑两个用户群体。他说，当他们决定包括开发人员时，改变工具的目标用户感知变得具有挑战性。相比之下，他说，Penpot 从一开始就被设计为容纳两个用户群体，并将其融入到同一工作流程中，无需使用针对某个用户群体的单独模式或专业工作流程。

## Penpot 与 Figma 的比较

除了开源许可证之外，Penpot与Figma有何不同之处？

Ruiz-Múzquiz解释说，Penpot 提供的设计功能源自工程最佳实践和代码标准。例如，他们拥有“ Flex 布局”和“网格布局”——两者都基于 CSS 标准。换句话说，一旦你在 Penpot 中完成设计，它已经是 CSS 代码。目标是尽量减少设计师和开发者之间的任何“翻译不准确”的问题。

![](https://cdn.thenewstack.io/media/2023/06/be6388a5-07.png)
*Penpot 中选择布局*

他还表示， Penpot 的用户界面对开发者来说也很熟悉。

他说：“开发者的入门过程非常简单。也就是说，他们可以使用的工具、词汇、用户界面。我们努力确保开发者真正感到自在，因为这个工具对他们来说并不陌生。”

然而， Penpot 和 Figma 之间最大的区别在于前者是开源软件。但是如果你超越这个区别， Figma 是最令人印象深刻的符合 Web 标准的工具之一。它利用了 JavaScript 、 WebGL 和 WebAssembly等 标准，以创建一个至少与 Flash 等旧版浏览器插件一样交互性的基于 Web 的工具。正如 Figma 的首席技术官 Kris Rasmussen 今年 2 月告诉我，现代 Web 标准使得 Figma 能够“基本上将传统上无法迁移到 Web 上的东西直接迁移到 Web 上，并使其更高效——与原本被锁定在桌面应用程序中竞争。”

> 现如今，基于浏览器的设计工具已经是基本要求。Penpot 试图通过使许可证成为区别点，从而超越 Figma 。

Ruiz-Múzquiz 坚称， Penpot 为用户提供对技术的完全所有权和控制权。它还为组织提供了自托管的机会，确保它们不依赖第三方云服务，并完全掌控其关键知识产权和设计资产。此外， Penpot 使用的格式都是开放标准，他提到了 SVG 、 CSS 和 JSON 。

他说：“所以我不会将 Penpot 与其他工具之间的开放性进行比较，因为它们也是基于一些标准技术构建的。我认为这是关于许可证的问题。”

在 Penpot 和 Figma 之间并没有太大的不同之处的是使用案例。 Ruiz-Múzquiz 表示， Penpot 的使用案例包括头脑风暴、创建交互原型、低分辨率用户体验设计、高分辨率设计、接收反馈以及构建设计系统、组件和模板。然而， Penpot 不生成 React 或 JavaScript 组件，因为它专注于使用 CSS 和 HTML 提供生产就绪的代码。

## 开发者平台？

最近，与 Figma 和 Penpot 竞争的 Canva 宣布推出了一个新的开发者平台。这个想法是，外部开发者将能够为 Canva 用户创建 JavaScript 应用程序。我问 Ruiz-Múzquiz 是否计划以类似的方式向开发者开放 Penpot ？

他回答说，他们正在建立一个开发者平台，但要到今年晚些时候才会准备就绪。他暗示这个平台将使开发者能够创建“一流”的应用程序，而无需获得应用商店所有者的批准。

他说：“由于我们看到自托管和私有实例的增长加快，我们可能会看到更多基于你在防火墙后面集成的插件。所以你可以做一些非常酷的东西，而不需要从一个仅限于 SaaS 的产品获得批准。”
