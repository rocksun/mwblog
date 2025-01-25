# Tailwind CSS 4.0 版本“从零重写”

![Tailwind CSS 4.0 版本特色图片](https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2-1024x577.png)

“我的天，终于完成了——我们刚刚发布了[Tailwind CSS v4.0](https://tailwindcss.com/blog/tailwindcss-v4),” Tailwind CSS 创建者周二写道。

考虑到这个版本是对框架的彻底重写，这样的反应是可以理解的。团队利用“多年来我们在架构方面学到的所有知识，并对其进行了优化，使其速度尽可能快，”写道。

首先，是新的基于 Rust 的性能引擎——一度被称为[Oxide](https://tailwindcss.com/blog/tailwindcss-v4-alpha)——被整合到这个版本中。据称，它使完整构建和增量构建都更快。

“在我们自己的项目中进行基准测试时，我们发现完整重建的速度提高了 3.5 倍以上，增量构建的速度提高了 8 倍以上，”他写道。“最令人印象深刻的改进是在实际上不需要编译任何新的[CSS](https://thenewstack.io/css-in-js-and-react-server-components-a-developer-guide/)的增量构建上——这些构建速度提高了 100 倍以上，并在微秒内完成。”

但这还不是全部。指出[Tailwind CSS](https://thenewstack.io/tailwind-css-for-developers-style-without-using-css-code/) v4.0 还包含最先进的 CSS 功能，例如：

- 原生级联层，他表示这提供了对不同样式规则如何相互作用的更多控制；
- 注册的自定义属性，这使得诸如动画渐变之类的功能成为可能，同时也显著提高了大型页面的性能；
- `color-mix()`，允许开发者调整任何颜色值的透明度，包括 CSS 变量和 `currentColor`；以及
- 逻辑属性，简化了 RTL 支持并减小了生成的 CSS 的大小。

一位名为 的前端作家是众多对新版本给予[正面评价](https://xiuerold.medium.com/tailwind-css-4-0-is-here-whats-new-and-why-it-matters-580849f70820)的前端开发者之一。

“Tailwind CSS 4.0 不仅仅是一个更新——它是对 CSS 框架可以实现什么的重新构想，”写道。“通过将原始性能与现代 CSS 功能和无摩擦的设置相结合，它使[开发者能够更快](https://thenewstack.io/newly-stable-next-js-compiler-faster-supports-larger-builds/)、更具创造性地进行构建。”


## 16% 的组织已经标准化了开发者环境

根据[SlashData 的《2025 年开发者环境现状》](https://coder.com/blog/insights-and-key-findings-from-the-state-of-development-environments-2025-report)报告，在接受调查的 550 多名软件专业人员中，79% 使用完全托管的云托管开发者环境。然而，同一项研究发现，84% 的受访者表示他们的组织不依赖于一个标准化的开发环境工具。

这种脱节是因为关于使用什么开发环境的决策有时是在组织层面做出的，而有时则是在团队或个人层面做出的。

尽管如此，大多数组织确实拥有通用的开发工作流程或标准。

所有研究参与者都在大型公司（拥有 100 名开发者或 1000 名员工）工作，这些公司要么使用，要么提供开发环境。值得注意的是，只有 27% 的人主要担任开发者角色，其余的人则担任 IT 领导和管理角色。

只有 36% 的这些开发者表示他们的组织允许[开发者完全控制](https://thenewstack.io/ambassador-labs-combats-tool-sprawl-with-developer-control-plane/)他们的开发环境。

相比之下，52% 的管理员/领导者报告说他们完全控制着他们的开发环境。此外，管理员更有可能对他们环境的治理和配置持积极态度。

只有 36% 的这些开发者表示他们的组织允许

[开发者完全控制]他们的开发环境。

目前，只有 13% 的人能够使用[自动化](https://thenewstack.io/gitpod-brings-automated-environments-to-jetbrains-ides/)系统独立创建新的环境。虽然其他人已经标准化了处理器来独立创建新的环境，但 45% 的人必须事先获得经理或 IT 的批准，或者至少要与其他团队/部门协调。

展望未来，78% 的研究参与者计划在明年开展更多关于开发者环境标准化的工作。总的来说，42% 的这些组织预计将依靠内部[平台或 DevOps](https://thenewstack.io/how-platform-engineering-helps-manage-innovation-responsibly/)团队来实现这种标准化。
The New Stack的研究分析师预测，如果开发人员继续与他们依赖的管理和供应这些环境的专业人员抱有截然不同的看法，那么他们可能会对这些努力的进展感到不满。

## Bun 1.2被称为“重大更新”
Bun发布了1.2版本，Bun的产品经理称其为“重大更新”。Bun旨在成为Node.js的直接替代品，但这并非易事。在一篇博文中，Partovi概述了他们如何优先处理和修复Node.js错误。使用Bun 1.2，他们决定为对Bun所做的每一个更改运行Node.js测试套件。

Bun 1.2还增加了对S3的内置支持，这是云中事实上的对象存储标准。此支持允许开发人员使用与Web标准（如Blob）兼容的API读取、写入和删除S3存储桶中的文件。

还有一个内置的Postgres客户端：`Bun.sql`。Partovi补充说，MySQL即将推出。

`bun install`现在使用基于文本的锁文件：`bun.lock`，并且Partovi指出，在Bun中，Express的速度提高了三倍。

## JavaScript Temporal迎来实验性浏览器版本
Mozilla MDN Web Docs团队的技术作家表示，通过浏览器实现新的JavaScript Temporal对象，可以“极大地简化和现代化”JavaScript中的日期处理。

在一篇最近的文章中，Smith探讨了JavaScript Temporal对象。首先，他解释了JavaScript的`Date`对象的作⽤，该对象可以追溯到JavaScript的早期，并且是从Java早期的有缺陷的`java.util.Date`实现中复制的。

“Java在1997年替换了这个实现，但JavaScript却使用了近30年的相同API，尽管存在已知问题，”Smith解释道。

“Temporal增加了对时区和日历表示的支持，许多用于转换、比较和计算、格式化等的内置方法。”

——Brian Smith，Mozilla MDN Web Docs技术作家
这种方法的主要问题是它只支持用户的本地时间和UTC，因此没有时区支持。

所有这些都使得使用起来有点麻烦，导致开发人员依赖Moment.js和date-fns等库来处理应用程序中的日期和时间。

Temporal替换了[Data对象](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)，并且它以一种使日期和时间管理可靠且可预测的方式进行替换。

“Temporal增加了对时区和日历表示的支持，许多用于转换、比较和计算、格式化等的内置方法，”他写道。“API表面有超过200个实用程序方法，您可以在MDN上的[Temporal文档](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal)中找到所有这些方法的信息。”

在文章的其余部分，他解释了有关Temporal对象如何使用代码示例工作以及探讨了浏览器支持的更多信息。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)