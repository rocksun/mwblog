<!--
title:  JavaScript/React库让开发者构建AI聊天机器人
cover: ./cover.jpg
-->

NLUX是一个前端库，它自带ChatGPT和Hugging Face大型语言模型的适配器，也支持对聊天机器人进行个性化定制。

> 译自 [JavaScript/React Library Lets Developers Build AI Chatbots](https://thenewstack.io/javascript-react-library-lets-developers-build-ai-chatbots/)，作者 Loraine Lawson。

NLUX是一个新的开源Javascript React库，它让开发者可以构建自己的聊天机器人用户界面，并通过自然语言提示自定义机器人的个性。

[NLUX](https://nlux.ai/)可以与任何大型语言模型(LLM)后端服务配合使用，同时它内置了与[OpenAI的ChatGPT](https://thenewstack.io/improving-chatgpts-ability-to-understand-ambiguous-prompts/)和[Hugging Face](https://thenewstack.io/hugging-face-aws-partner-to-help-devs-jump-start-ai-use/)的[大型语言模型](https://thenewstack.io/opportunities-and-limitations-of-deploying-large-language-models-in-the-enterprise/)的连接适配器。也可以[构建定制的流adapters或Promise adapters来连接](https://docs.nlux.ai/learn/adapters/custom-adapters/create-custom-adapter)其他LLM或[API](https://thenewstack.io/a-modern-approach-to-securing-apis/)。

“假设有一个大公司不使用公开的OpenAI大型语言模型，但是他们想要使用托管在自己服务器上的定制模型，”NLUX的创建者[Salmen Hichri](https://github.com/salmenus)说，“他们实际上可以构建和定制自己的模型，但他们仍然可以使用NLUX来连接这些模型。他们需要为自己的模型和API构建一个自定义的适配器。”

Hichri说，有更老的聊天机器人库，但就他所知，NLUX是第一个AI特定的库。

目前，NLUX有两种“味道”:

- NLUX React JS，包括React组件和钩子；以及
- NLUX JS，这是一个可以与任何Web框架一起使用的纯Javascript库。

## 为什么选择React？

Hichri告诉The New Stack，选择React的部分原因是它提供了一种构建应用程序的直观方式。而且，大量的开发者正在使用React，他补充说。这得到了最近发布的2023年[JavaScript Rising Stars调查](https://risingstars.js.org/2023/en#section-all)的支持，该调查发现React保持着第三年JavaScript框架的最受欢迎地位。

“已经有数百万开发者在使用React和JavaScript，这些开发者正处于构建数字体验的前沿，”Hichri说，“他们正在编写网页应用程序，创建网站、移动应用程序，我们希望帮助他们构建直观的会话体验。”

目前，开发者确实需要了解一些React来使用该库，尽管如果开发者只了解JavaScript，他们仍然可以用其他框架使用该库的JavaScript版本。Hichri计划将NLUX扩展到支持[Angular](https://thenewstack.io/the-angular-renaissance-why-frontend-devs-should-revisit-it/)、[React Native](https://thenewstack.io/google-flutter-now-rivals-facebooks-react-in-developer-use/)，可能还有Preact。

## 赋予聊天机器人个性

开发者可以通过自然语言提示和几行代码来[个性化他们的聊天机器人](https://docs.nlux.ai/learn/get-started)，以给对话增添一点个性。他们还可以指示机器人要严肃、幽默、谦虚或自信。

“对于适配器，我们已经为OpenAI和Hugging Face提供了适配器，我们允许通过所谓的系统消息进行定制，”他解释道。“所以当开发者使用NLUX时，系统消息(对用户不可见)就像是开发者告诉聊天机器人以某种方式行事。”

NLUX目前也正在为[LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/)构建一个适配器，以及支持服务器端渲染。语音聊天也在该库的路线图上。

## 超越聊天机器人: AI驱动应用的下一个阶段

现在，对于生成式AI应用开发的关注点是构建本质上是AI驱动聊天机器人的东西。但是Hichri和该领域的其他人士说，重点很快就会转向AI同伴，它们将能够在接收到自然语言命令后在应用程序内执行操作。

“这不仅仅是对话，而是一个可以代表用户执行操作的智能系统，它嵌入在应用程序或软件中，”他说。“用户仍然需要定义在他们的软件上可以执行什么样的操作，但触发器不会是点击或查找菜单，触发器将是自然语言表达式。”

这种同伴模式在NLUX的路线图中，应该很快就会推出，他补充说。

影响AI应用的另一个趋势将是具有空间意识的能力，并将其与增强现实相结合，Hichir预测。具体来说，他指出了苹果在[Vision Pro](https://thenewstack.io/vision-pro-for-devs-easy-to-start-but-ui-not-revolutionary/)方面的[工作](https://thenewstack.io/apple-lays-foundation-for-mixed-reality-headset-at-wwdc22/)，但注意到OpenAI也开始提供一些功能，这会让他们成为增强现实助手。

“对于在办公室工作的人来说这可能不是什么大不了的事，但对于某些行业或建筑中的工作类型，或者其他一些空间意识非常重要的工作，通过增强现实助手访问智能AI系统，这是革命性的，”他说。
