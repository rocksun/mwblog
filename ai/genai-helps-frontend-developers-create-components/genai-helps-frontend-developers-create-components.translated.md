# GenAI 助力前端开发者创建组件

![GenAI 助力前端开发者创建组件的特色图片](https://cdn.thenewstack.io/media/2025/01/674ff385-frontendwebdevelopment-1024x683.jpg)

当开发者兼律师开发WordPress网站时，她发现了一个基于开源PHP内容管理系统的插件生态系统，但当她尝试在JavaScript世界中寻找类似的东西时，却什么也没找到。

她想将微前端方法——通过将Web应用程序分解成更小、更独立的组件来构建Web应用程序——应用于JavaScript Web开发。

因此，她启动了[WebCrumbs](https://github.com/webcrumbs-community/webcrumbs)，这是一个为JavaScript社区创建组件的开源解决方案。它允许你创建与React和Angular等框架兼容的组件和插件，以及CSS/Tailwind和HTML中的插件。结果是开源的。

WebCrumbs的目标是创建一个“现代Web开发的行业标准解决方案，为JavaScript社区和相关框架（如React、Nextjs、Vue、Svelte等）创建第一个开放的插件生态系统”。

这本身就是一个有趣的项目，但最近更受关注的是[Frontend AI](https://tools.webcrumbs.org/frontend-ai)，它是原始Webcrumbs的一个分支。

## Frontend AI

Frontend AI是一个生成式AI模型，它为开发者创建插件或模板，并将代码导出为CSS/[Tailwind](https://thenewstack.io/tailwind-css-for-developers-style-without-using-css-code/)、HTML、[React](https://thenewstack.io/new-york-public-library-on-choosing-react-to-rebuild-website/)、[Angular](https://thenewstack.io/angular-shares-potential-ideas-for-2025-improvements/)、[Svelte](https://thenewstack.io/youll-write-less-code-with-svelte-5-0-promises-rich-harris/)或[Next.js](https://thenewstack.io/next-js-canary-supports-partial-pre-rendering-for-faster-sites/)。它还包含一个代码编辑器和可视化工作室，使开发者可以轻松定制它创建的组件。

她的团队上周发布了Frontend AI的第3版。它最初于5月份悄然发布，最初是作为团队学习如何构建组件的工具。

Frontend AI并没有试图与[Vercel的v0 Gen AI聊天](https://v0.dev/)等产品竞争，将其归类为更专注于创建完整网站的产品。

[一位评论者这样描述它](https://hackernoon.com/should-you-try-v0-webcrumbs-or-both)：v0生成与Shadcn UI和Tailwind CSS兼容的React代码，“这对于想要构建现代、精美UI的开发者来说非常完美”。作者写道：“Webcrumbs的核心是使用人工智能直接从图像或文本描述生成代码组件。”“你可以描述任何UI元素，甚至上传视觉参考，Webcrumbs会立即将其转换为React、Vue、Svelte甚至HTML。”

与Vercel v0不同，Frontend AI专注于创建微前端的插件和代码。开发者可以使用自然语言描述或图像来创建组件。

“你首先注意到的是我们速度快得多——……你点击提交，它就会生成请求，”她说。“另一件事是，一旦你完成，你就不必每次都询问AI你正在做的每一个细微的更改。”

![Frontend AI组件（此处为博客）的屏幕截图——它创建代码，图片在弹出式代码编辑器中显示代码。](https://cdn.thenewstack.io/media/2025/01/897c59ed-frontendai.png)
Frontend AI的屏幕截图。

最终目标是创建一个全栈解决方案。她还打算在未来的某个时间点将Webcrumbs和Frontend AI合并。但目前，Frontend AI专注于……前端。

从技术上讲，你可以要求Frontend AI创建一个完整的网站[——这使其成为一个低代码选项](https://thenewstack.io/terraform-cloud-now-offers-less-code-and-no-code-options/)——但这并不是它的重点。

而且，那样有什么乐趣呢？

## 使用模板

创建组件后，开发者可以选择将其提交以进行[开源许可](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/)。已经有超过100个模板的下拉列表可以帮助使用开源代码快速启动流程。她说，公司可能会在某个时候允许开发者在一个市场上销售这些模板。
代码结果显示在一个可视化界面中，允许开发者调整前端AI生成的任何元素的主题、字体、颜色和间距。Machado说，随着团队添加更多客户能够通过拖放修改工具的功能，该界面也在不断发展。

“我们不是在设计之后[生成代码]，”Machado说。“我们是一起生成的，所以你永远不会遇到像Figma那样，生成的东西和代码显示的东西不一样的问题。”

她补充说，最终，使用前端AI构建的组件将可以通过一行代码嵌入。目前，开发者可以从代码编辑器复制代码、下载代码或获取PNG。

## 将规则应用于组件
前端AI还允许你创建你可以编写的规则——例如，Machado演示了将橙色应用于她的组件的规则。

还可以选择在移动设备、平板电脑和台式机上测试组件。有时，组件与特定屏幕尺寸不兼容。

![A screenshot showing how Frontend AI auto-detects problems a component might encounter on a particular type of device, and then offers to fix that problem.](https://cdn.thenewstack.io/media/2025/01/c6882626-runthefixfrontendai.png)
前端AI可以检测组件在特定设备上可能遇到的问题，并提供修复这些问题的方案。前端AI截图。

她说：“我们另一个新功能是这里的响应式按钮，你可以看到组件的显示效果——比如这里你可以看到它在移动设备上显示效果不好。”“它会提示你，‘你想修复吗？’然后你运行修复程序，你就会看到代码为你重新生成，以适应那种屏幕。”

[YouTube](https://youtube.com/thenewstack?sub_confirmation=1) 科技发展日新月异，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。