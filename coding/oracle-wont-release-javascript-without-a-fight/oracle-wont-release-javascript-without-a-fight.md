
<!--
title: 甲骨文不会轻易放弃“JavaScript”
cover: https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2.png
-->

其他开发者新闻方面，Node.js 将很快默认支持 TypeScript，谷歌发布了面向 Android 开发者的 Home API。

> 译自 [Oracle Won’t Release ‘JavaScript’ Without a Fight](https://thenewstack.io/oracle-wont-release-javascript-without-a-fight/)，作者 Loraine Lawson。

据[Deno](https://deno.com/?utm_content=inline+mention) [最近在Mastodon上发布的一篇文章](https://fosstodon.org/@deno_land/113793964751001617)显示，甲骨文不会自愿放弃其对“JavaScript”一词的商标权。

[Deno是由Ryan Dahl创建的JavaScript、TypeScript和WebAssembly的开源运行时](https://thenewstack.io/how-oop-developers-can-get-to-know-typescript-through-deno/)。Dahl也是JavaScript运行时环境Node.js的创建者。

[Deno于2024年11月向美国专利商标局提交了一份申请](https://ttabvue.uspto.gov/ttabvue/v?pno=92086835&pty=CAN&eno=1)，[要求撤销甲骨文的商标](https://thenewstack.io/deno-petitions-to-cancel-oracles-javascript-trademark/)。该申请认为，“JavaScript”是编程语言的通用名称。Deno的主张是，甲骨文既不控制也不曾控制过该语言的规范或使用。

Mastodon帖子指出：“接下来：他们将提交答复，我们将开始调查以证明‘JavaScript’被广泛认为是一个通用术语，而不是由甲骨文控制的。”

Dahl还声称，甲骨文在2019年续展[JavaScript商标](https://tsdr.uspto.gov/#caseNumber=75026640&caseSearchType=US_APPLICATION&caseType=DEFAULT&searchType=statusSearch)时向USPTO提交了虚假证据。

最后，该申请基于这样一个主张：甲骨文（通过2009年收购Sun Microsystems获得该商标）由于未经使用而实际上已放弃了该商标，这可能是丧失商标的理由。

## 谷歌发布面向Android开发人员的Home API

如果您正在寻找一个周末项目，[谷歌刚刚发布了其Home API的公开开发者测试版](https://developers.googleblog.com/en/build-the-future-of-home-with-google-home-apis/)，适用于Android。

谷歌本周在其开发者博客上指出，iOS版本将于未来几个月推出。

谷歌Home平台负责人高级工程总监[Matt Van Der Staay](https://www.linkedin.com/in/matt-van-der-staay-7325523/)写道：“在公开测试版期间，开发者可以开始构建和测试他们的应用程序，最多可容纳100个用户，为今年晚些时候Home API的正式发布做准备。”“我们构建Home API是为了帮助应用程序和智能家居开发者桥接数字交互和物理设备，从而提供下一代令人愉悦的体验。”

他继续分享说，Home API包括：

- 设备和结构API，让您可以访问连接到谷歌Home的超过6亿台设备，以及一个统一的界面来管理和控制谷歌Home上的云连接设备和Matter设备；
- 配置API，简化了在30亿台Android设备上使用Fast Pair进行设备设置；以及
- 自动化API，为用户提供必要的工具，以便直接在您的应用程序中创建和管理家庭自动化，“利用广泛的信号、命令和谷歌特有的AI驱动功能，实现个性化和智能的家庭体验”。

Eve、Nanoleaf和LG是已经推出基于Home API并通过Google Play商店提供的体验的谷歌合作伙伴之一。Eve用它为用户在Eve Thermo上创建了一个自动加热计划。Nanoleaf使用Home API让客户可以使用简单的语音命令来打开他们的Nanoleaf 4D屏幕镜像灯条。LG使用[API](https://thenewstack.io/how-sdks-can-reduce-api-integration-time/)将其谷歌Home设备集成到其电视智能家居产品中。

## Node将默认支持TypeScript

据Total TypeScript博主[Matt Pocock](https://linkedin.com/in/mapocock/)称，开源的跨平台JavaScript运行时环境[Node.js将很快默认支持TypeScript](https://www.totaltypescript.com/typescript-is-coming-to-node-23)，无需额外配置。

他引用了[Marco Ippolito最近提交的请求](https://github.com/nodejs/node/pull/56450)，并在更新中指出，Node似乎将在23.6.0版本中支持此功能。

他写道：“Marco Ippolito在过去一年中一直在推动Node中的TypeScript支持，他提交了一个PR，取消了–experimental-strip-types标志在Node 23中的使用。”然后他解释说，从实际角度来看，这意味着开发人员可以创建一个包含TS语法的index.ts文件（例如类型注释），并运行node index.ts而无需其他标志。

他继续说道：“Node将使用swc的一个版本去除类型，然后运行生成的代码。”

[他补充说，它现在可以在](https://x.com/satanacchio/status/1872574795390530000)[Node Nightly](https://nodejs.org/download/nightly/v24.0.0-nightly20241227ba5992831b/)版本中使用。
