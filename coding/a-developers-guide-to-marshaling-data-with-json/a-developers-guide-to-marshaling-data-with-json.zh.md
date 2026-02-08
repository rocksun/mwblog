虽然代码和数据相互作用形成运行程序，但我们仍然更倾向于关注代码的呈现方式，而非数据的呈现方式。尽管海量的流数据往往在不经意间传输且本身毫无意义，但 [JavaScript 对象表示法（即 JSON）](https://thenewstack.io/an-introduction-to-json/) 被专门设计为一种标准的基于文本的格式，用于表示少量人类可读的结构化数据。

你第一次遇到这种表示需求，可能是在程序中持久化或保存状态时。通常，游戏开发者可能希望“保存”游戏的位置以便稍后重新启动——即保存所有代表游戏当前状态的对象的 상태。我们将对象从内存格式转换为标准存储格式的过程称为“整理”（marshaling）或“序列化”（serialization）。虽然大多数语言都有内部二进制方式来持久化状态，但使用 JSON 可以让你的数据保持开放和可互换。

本文将从一个相对简单的层面探讨 JSON，但希望你会认识到它在页面上的形式非常重要。

## 为什么 JSON 在数据整理方面优于 XML

尽管 JSON 是 JavaScript 的一个子集，但它最初被视为广受诟病的 XML（可扩展标记语言）的受欢迎的替代品，因为 XML 既冗长又复杂难以解析。那是因为它进行了比单纯整理所需更多的自描述。

但 XML 至少是人类可读的。这意味着它可以由非程序员审查，并有助于拓展开发世界。（作为一名资深的 [Ruby](https://thenewstack.io/why-ruby-on-rails-is-still-worth-your-while-as-a-developer/) 用户，我也熟悉另一种名为 [YAML](https://thenewstack.io/with-yamlscript-yaml-becomes-a-proper-programming-language/) 的格式，至今仍受配置文件青睐。）

‘可读’数据的概念需要稍作解释。在这种情况下，它实际上并非指‘我想读取数据’。它的意思是，‘我希望能够理解事物的形态。’存在一个最佳点，在此点上，少量数据可以被高效查看，并且其结构能帮助读者自然地解析它。

因此，JSON 数据非常适合用于存储在文件或代码中的可读数据。JSON 经常用于配置文件，因为无需修改代码即可读取新数据。同种结构略有不同的版本（例如，额外或缺失的键）对于语言解析器来说很容易管理。你可以忽略新的键，或者将键标记为‘可选’。

问题的核心是，如果你与专注于内容的人员合作，你需要依靠工具让他们直接贡献。JSON 在这方面表现出色。

## JSON 的一个实际案例：描述一只猫

我请 ChatGPT 以 JSON 格式‘描述一只普通的猫’。它回复如下：

```
{
  "species": "Felis catus",
  "average_age_years": 4,
  "average_weight_kg": 4.5,
  "body_length_cm": 46,
  "tail_length_cm": 30,
  "fur": {
    "length": "short",
    "texture": "soft",
    "common_colors": ["black", "white", "gray", "brown", "orange"],
    "patterns": ["solid", "tabby", "bicolor", "calico"]
  },
  "eyes": {
    "shape": "round",
    "colors": ["green", "yellow", "blue", "amber"]
  },
  "ears": {
    "shape": "triangular",
    "position": "upright"
  },
  "temperament": {
    "independence": "moderate",
    "affection": "selective",
    "playfulness": "moderate",
    "curiosity": "high"
  },
  "activity_level": "medium",
  "sleep_hours_per_day": 14,
  "diet": "obligate carnivore",
  "vocalization_level": "low to moderate",
  "lifespan_years": {
    "indoor": 15,
    "outdoor": 8
  }
}
```

JSON 无需在帮助 ChatGPT 继续展示猫之前提供猫的预先定义。事实上，这感觉是一个合理的格式来描述任何小型哺乳动物宠物。

即使你以前从未见过 JSON（但涉猎过一些编程），这也很容易阅读。它包含许多键/值对。字符串使用引号，否则是浮点数。你可以（正确地）猜测它也识别 `true` 和 `false` 作为布尔值。它有子结构和数组。例如，‘temperament’（脾性）有效地有四个属性。眼睛颜色有四种可能的值。‘temperament’中的键即使没有实际值，也已经显得很像猫的特征了。

而且我不知道‘中等活动’水平具体是什么。但大型语言模型（LLM）乐于参与我这个略带异想天开的请求，因为 JSON 对此没有问题。事实上，JSON 在 LLM 提示中非常有用，因为它是一种在不编写任何代码的情况下引入设计命名法的巧妙方式。

我向 XML 提出了同样的要求，但结果大约大了 75%，因为它必须重复开放和闭合标签才能正确解析。（JSON 也存在带注释的版本，但这并不完全是标准。）

## 如何在代码中解析 JSON 数据

大多数语言都有解析 JSON 的常用库，这意味着我可以编写一些 Ruby 代码将猫重新读回内存。我将让 ChatGPT 完成这项任务，并编写 Ruby 的解析代码。这假设我将我们前面提到的 JSON 通用猫保存在一个名为 ‘cat.json’ 的文件中：

[![](https://cdn.thenewstack.io/media/2026/01/7d8aabe8-image-1024x834.png)](https://cdn.thenewstack.io/media/2026/01/7d8aabe8-image-1024x834.png)

将此代码保存为 ‘cats.rb’ 后，我在终端中运行它（假设我已安装 Ruby）：

[![](https://cdn.thenewstack.io/media/2026/01/9e736528-image-1.png)](https://cdn.thenewstack.io/media/2026/01/9e736528-image-1.png)

就这样，这只猫复活了。

## 使用 FracturedJson 提升可读性

我最近听说了一个不错的库，名为 [FracturedJson](https://github.com/j-brooke/FracturedJson)，它是一个‘能生成人类可读但相当紧凑输出的 JSON 格式化工具’。我认为这让我们更接近那个最佳点。

这目前还没有 Ruby 库，所以我们首先在 [浏览器](https://j-brooke.github.io/FracturedJson/) 中初步试用它。让我们看看它如何重塑我们持久化的猫：

[![](https://cdn.thenewstack.io/media/2026/01/2b99aad1-image-2-1024x644.png)](https://cdn.thenewstack.io/media/2026/01/2b99aad1-image-2-1024x644.png)

它只做了一些选择，包括修复空间格式和在可能的情况下将属性保留在同一行。

我们也可以在 VS Code 中使用它，因为有 FracturedJson 的 NuGet 库。像往常一样，我在终端中启动了 VS Code，创建了一个控制台项目并添加了 NuGet 库。然后我添加了几行代码来重塑猫：

[![](https://cdn.thenewstack.io/media/2026/01/cac59c3f-image-3-1024x819.png)](https://cdn.thenewstack.io/media/2026/01/cac59c3f-image-3-1024x819.png)

你可以从代码中看到，主要的繁重工作由 .NET `System.Text.Json` 服务完成，而 FracturedJson 只是一个格式化工具。它还有额外的选项可供探索，如你在浏览器示例中看到的。

## 可读 JSON 在开发中的重要性

在信息密集的计算丛林中，快速目视解析 JSON 数据仍然是一项非常有用的技能。任何有助于形成一片宁静空地的工具都受到欢迎。

少量 JSON 在 LLM 提示中也表现良好，无需编程即可引导任务。FracturedJson 试图让你的 JSON 字符串数据更接近可读性和紧凑性的最佳点，帮助我们更容易地欣赏那只持久化的猫。