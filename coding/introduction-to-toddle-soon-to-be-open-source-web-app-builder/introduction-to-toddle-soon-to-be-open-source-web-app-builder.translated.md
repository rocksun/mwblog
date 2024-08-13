# 认识 Toddle：下一代开源 Web 应用构建器

![Meet Toddle: the Next Open Source Web App Builder 的特色图片](https://cdn.thenewstack.io/media/2024/08/5c6b6f6c-kelly-sikkema-jrvxgakzism-unsplash-1024x678.jpg)

我通常写的文章都是针对那些控制着大部分甚至全部技术栈的开发者。但也有必要了解如何使用 [低代码](https://thenewstack.io/the-highs-and-lows-of-low-code-tools/) 解决方案。

[Toddle](https://toddle.dev) 最近宣布了 [开源计划](https://toddle.dev/blog/toddle-is-soon-open-source?ref=dailydev)，它就是一个这样的低代码/无代码 Web 应用构建器。它专注于前端的组件层次结构，并在后端采用数据。（我的第一个想法是，如果 Toddle 生成了“toddlers”，那么我认为 [Tiddlywiki](https://tiddlywiki.com/)，它有“tiddlers”，可能想说点什么。）

## 开始使用 Toddle

注册后，Toddle 会直接进入 onboarding，询问你的编程经验。实际上，它是在检查你的角色：产品设计师、无代码开发者或软件工程师。对于最后一种，它建议，“你需要一个专业的开发环境来与开发者协作”，这有时可能是真的。

它会提供一个来自创始人（Andreas Møller）的预备视频，该视频简短且信息丰富，同时还明确表示有示例应用程序，这也是我通常探索功能的方式。

我喜欢这两个“开始”选项，因为它们表达了人们分解事物的方式的自然分叉。遗憾的是，这两个按钮都没有起作用，我不得不重新开始——但这可能只是我老旧的 Mac 的问题。再次进入后，一切正常。

## 使用示例项目进行尝试

它为我创建的示例项目是一个实时天气应用程序，该应用程序已经填充了我的本地区域的天气预报。我印象深刻。

没有对 Toddle 喜欢制作的 Web 应用程序类型进行非常明确的定义，但我之前暗示过这意味着 [前端](https://thenewstack.io/frontend-development/) 控制与 [后端](https://thenewstack.io/backend-development/) API 支持，而天气应用程序就是一个完美的例子：

左侧是一个组件层次结构，包含标准 HTML、自定义部分以及称为 **公式** 结果的东西，我将继续讨论。应用程序的当前视图位于中间。我可以看到一个 **前进** 按钮来测试它，以及一个 **发布** 按钮供以后使用。

我第一个想尝试的地方（我本可以从任何地方开始）是检查天气 API 调用。毕竟，我在它建议的位置运行它，所以天气应用程序显然使用的是实时数据。

通过点击右侧的“天气”API 按钮（**数据面板**），我可以清楚地看到它来自 [https://toddle.dev/_api/weather](https://toddle.dev/_api/weather)，我猜想这是一种受保护的 API：

下一个问题是，如何从 API 中提取正确的值并将其粘贴到文本框中？看起来值“broken clouds”已添加到此示例中的多云图像中。

当我点击层次结构中的文本框时，我可以看到文本框公式放置的位置：

然后我可以访问它的公式：

是的，我注意到结果被大写了，以确保一致性。我首先看到的是流程连接框，它们也存在于 [虚幻引擎蓝图](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine) 中，这些蓝图足够强大，可以运行 Fortnite。

现在，在我深入研究此过程的最后部分之前，让我简要地批评一下。从技术上讲，你不必是程序员才能使用这些流程框流（公式）。但是，你需要像程序员一样 **思考**。我建议，如果你像我一样，意识到产生输出所需的步骤可以用代码或这个稍微冗长的图表整齐地呈现，那么你已经走得太远了，无法挽救——你已经是一个开发者了。我很抱歉。你可能也应该开始编码。话虽如此，这个过程更加透明，完全有效，如果客户喜欢它，那么就不需要进一步证明。

我有点难以弄清楚如何返回显示 API 的数据面板，但我正在 Macbook 上操作——自然，屏幕越大，操作大量视觉元素就越容易。帮助功能确实指出了我如何恢复 **数据面板**：

Escape 键不起作用，但点击画布外部可以。我最终会找到的。但要记住，这不仅仅是一个游乐场；它是一个工具，需要学习。

查看数据，我可以看到描述键值的路径：

（我在英国，所以天气在我说话的时候正在变化。）我可以看到，后台 JSON 中结果的路径是“Response” / “data” / “current” / “weather” / “description”。这个键现在给出了值“overcast clouds”。
看着公式中的那个天气框，我有：

出于某种原因，我无法展开框本身，但我可以滚动路径部分，它们显示“weather” / “data” / “current” / “weather” / “description”，这与数据的路径匹配（其中“Response”被 API 名称“weather”替换）。

我在编辑器中犯了一个错误，但我能够使用底部的控件后退。通过使用块内的工具操作 API，我将路径的“description”部分替换为“main”，并且值“Clouds”立即在主应用程序中可见：

我发现编辑过程进行此简单更改有点繁琐，但除此之外很简单。正如我提到的，这与在虚幻引擎编辑器中使用蓝图并没有太大区别。此外，工具确实需要时间来学习。

在幕后，Toddle 明显创建了一个随机的项目页面，正如您从我使用的冗长的 URL 中看到的那样。它还维护了一些关于我的编辑视图的状态信息：

1 |
https://toddle.dev/projects/weather_web_app_3nhqjtm/branches/start/components/HomePage?mode=design&leftpanel=design&rightpanel=style&canvas-width=800&canvas-height=800&selection=nodes.WVNFMOKheuHNxO7t_BoFU |
我可以测试应用程序，我看到一个发布按钮。按下它，我实际上签入了我的应用程序：
最后，我得到一个可以查看的实时应用程序，在 URL 中保留项目名称，您可以[访问它](https://weather_web_app_3nhqjtm.toddle.site/)。

我不在兰贝斯 - 但所有位置 API 似乎都有些不准确。重新加载它解决了这个问题。

## 决定 Toddle 是否适合您的团队
要决定这是否是你自己或你的团队用来制作网络应用程序的开发方法，请考虑以下几点：

- 注意 Toddle 如何识别其客户的**角色**。检查您的团队是否有视觉创作者和数据人员，以及这些边界在您的团队中如何运作。- 如果您使用此工具来制作工作原型，您可以立即开始。但是，如果您想超越这一点，请了解您拥有什么以及平台维护哪些服务。在这种情况下，Toddle 明显正在转向[开源](https://toddle.dev/terms/open-source-terms)，这是件好事。- 确保每个人都有一个漂亮的大屏幕。幸运的是，它们便宜且充足。
- 确保创作者了解如何操作公式，或者如何将其交给开发人员。
- 确定可以在哪里使用传统的编码来挽救任何工作，然后再需要这样做。这并不是悲观，只是确保您了解您的增长和对效率的需求可能超出工具限制的边界。
[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)