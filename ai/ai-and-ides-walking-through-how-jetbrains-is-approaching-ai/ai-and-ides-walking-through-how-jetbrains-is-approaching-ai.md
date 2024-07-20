
<!--
title: AI与IDE：探索JetBrains对AI的应用
cover: https://cdn.thenewstack.io/media/2024/07/7e18e438-getty-images-0oviynbjwes-unsplash.jpg
-->

我们测试了 JetBrains AI，这是一款针对其集成开发环境 (IDE) 集合的新型多语言模型 AI 助手。

> 译自 [AI and IDEs: Walking Through How JetBrains Is Approaching AI](https://thenewstack.io/ai-and-ides-walking-through-how-jetbrains-is-approaching-ai/)，作者 David Eastman。

一直以来，使用 Java 的同事都对 [IntelliJ](https://www.jetbrains.com/idea/) 赞赏有加，最近对 C# 的 Rider 也是如此。因此，当我得到试用 [JetBrains AI](https://www.jetbrains.com/ai/) 的机会时，我感到非常好奇。JetBrains AI 是一款人工智能服务，它自称为“AI 助手”。**据称它“由 OpenAI 和 Google 作为主要第三方提供商提供支持”。**我不确定在 LLM 能力不断变化的情况下，尝试将不同的 LLM 能力与特定任务匹配是否是一个好主意，但不受限于单一供应商确实很有道理。

现在，谈到使用 LLM，专业开发人员都有略微不同的需求——没有一个是“为我编写代码”。但最突出的两种模式是代码补全和“解释这段代码”，这对面对不熟悉代码库的顾问很有用。[生成单元测试](https://thenewstack.io/make-your-dev-life-easier-by-generating-tests-with-codiumai/) 也可能适合，尽管不为自己的单元测试负责在某种程度上违反了敏捷规范。我个人并不喜欢在 IDE 中有示例，因为我可以直接浏览它们——但我了解有些人喜欢。例如，大多数开发人员都发现 *Time* 和 *Date* 函数可能变得非常不直观；有时复杂的系统无法简化。这些示例非常有用。

虽然这篇文章是对 AI 助手的评论，但这将是我第一次在我的 Mac 上使用 JetBrains IDE，因此我必须第一次进行管理。我有一个他们 AI 服务的“许可证密钥”，我将尝试将其移植到社区版或等效版本上。ReSharper 似乎位于 Visual Studio 上，而 Rider 是一个独立的 IDE——所以我选择了 Rider，以便查看 C#。我希望 AI 服务能够连接到它；这一点没有完全说明白。

我最终安装了 Rider 的试用版。导入设置的步骤非常棒。

![](https://cdn.thenewstack.io/media/2024/07/25741f58-untitled.png)

在下一节中，我的问题立即得到了解答。太棒了。

![](https://cdn.thenewstack.io/media/2024/07/dfb7fb13-untitled-1.png)

这让我对客户路径是否得到考虑有了更大的信心。在开始时这样做似乎很明显，但我见过太多产品没有给予自己的服务足够的关注。JetBrains 在我注册后给我发了电子邮件，让我创建一个帐户，并为我提供了免费许可证用于测试。

![](https://cdn.thenewstack.io/media/2024/07/a8b631b2-untitled-2.png)

需要注意的是，LLM 服务被视为一种附加功能，这使得“AI”感觉像是一种附加功能。我认为这不是 IDE 制造商目前的错——最终，这种类型的产品将在 OS 堆栈中更靠后的地方出现。现在，我们必须等待大公司在 LLM 主导地位方面展开竞争，这将把个人用户推向明确的消费者地位。

## 代码解释

我打开了一个游戏项目的代码，并要求解释：

```
...
static private List<Archetype> archetypes = new List<Archetype>(); 
... 
public static List<Archetype> FetchArchetypes() { 
  if (!archetypes.Any()) { 
    ArchetypeTemplates tt = BackEnd.DataLoader<ArchetypeTemplates>.LoadGameData("Archetypes.json"); 
    foreach (ArchetypeTemplate t in tt.Archetypes) { 
      archetypes.Add(new Archetype(t)); 
    } 
  } 
 
  return archetypes; 
}
```

`Archetype` 只是一个来自游戏的任意结构。最初，我将其从 JSON 文件中读入为数组，并在列表中本地重新创建了结构。如果列表已经创建，我只需传递列表。

那么 AI 认为这段代码在做什么呢？它返回了一个非常全面的答案，其中包含以下两个重点：

- “最后，该方法返回 Archetypes 列表，该列表包含根据 JSON 文件中的模板创建的 Archetype 实例。Archetype 类似乎代表游戏中的一种特定原型，而此方法用于根据 JSON 文件中的数据填充所有原型的列表。”
- ”在此特定方法中，值得注意的是，数据加载和对象实例化仅在 Archetypes 列表为空时执行。这意味着一旦 Archetypes 被获取一次，后续对该方法的调用将返回相同的列表，而不会进行任何额外的处理。这是一种常见的模式，适用于加载或对象创建是一个繁重过程且结果数据在应用程序的生命周期内不会改变的情况。”

这里有很多优点。该原型很可能用于游戏。这一点很重要——在快速理解代码时，理解意图和效用同样重要。它识别出我使用了延迟实例化，以及我使用它的原因，并且它是一个真正的**模式**。它还理解读取 JSON 文件是在其他地方完成的，但我们依赖于输入。

然后，我从上下文菜单中直接请求了**建议的重构**：

![](https://cdn.thenewstack.io/media/2024/07/7b05a608-untitled-3-1024x128.png)

它建议将加载操作分离到一个单独的方法中，以简化代码。我认为几乎所有开发人员都会同意这种改进。它也可能抱怨缺乏错误检测。

如果你想做一个简单的对比，使用 Meta 的 Llama 3 进行[使用 JSON 持久性的编码创建](https://thenewstack.io/coding-test-for-llama-3-implementing-json-persistence/)并不完全成功。请注意，三个月在 LLM 发展中是一个漫长的时期。

## 代码补全
让我们尝试一些代码补全。我将尝试一个类似于我为[使用 C# FlagsAtribute 的 Copilot](https://thenewstack.io/the-changing-role-of-human-developers-in-an-ai-and-llm-world/)所做的示例。从那篇文章中：“C# 中的 FlagsAttribute 用于当你想要有效地存储一个标志集时——也就是说，一组使用按位运算操作的布尔值。”

这是一个简单的例子：

```csharp
[Flags] public enum Pets 
{
  None = 0, 
  Dog = 1, 
  Cat = 2, 
  Bird = 4, 
  Rabbit = 8, 
  Other = 16 
}
```

只要标志值以二进制幂递增，你就可以构建一个二进制标志集。查看那篇文章以获取更多解释。

我删除了我的实际代码，并要求助手仅使用签名重新生成它。我得到了紫色波浪线，它给了我生成选项。首先，检查标志是否在当前集合中的方法。它给出了这个函数体：

```csharp
public bool CheckFullGameFlags(FullGameFlags flag) 
{ 
  return (InGameFullFlags & flag) != 0; 
}
```

这是我最初的代码：
```csharp
public bool CheckGameFlag(FullGameFlags flag) => (InGameFullFlags.HasFlag(flag));
```

虽然它错过了现有的 C# 方法 `HasFlag`，但它正确地推断出我想将传入的标志与集合进行比较。它从上面的代码中找到了本地集合 `InGameFullFlags`。

然后我给它提供了 SetFullGameFlag 的补充签名。同样，命名约定中包含足够的线索，表明我想添加新的标志：

![](https://cdn.thenewstack.io/media/2024/07/fbb2734f-untitled-4.png)

我再次点击波浪线，并使用“使用 AI 实现”，它生成了下面的代码。同样，它附带了完整的解释。

```csharp
void SetFullGameFlag(FullGameFlags flag) 
{ 
 InGameFullFlags = InGameFullFlags | flag; 
}
```

这与我拥有的代码相同（除了表达式体标记 ⇒）：

```csharp
public void SetGameFlag(FullGameFlags flag) => InGameFullFlags |= flag;
```

最后，ClearGameFlag 也一样。这只是对集合进行按位取反。同样，它也完全正确地做到了这一点。

我希望结果可以直接写入编辑器，或者作为代码补全，但通过在侧边栏中写入辅助信息，它附带了大量的解释。

## 结论

总的来说，我认为 AI 助手表现出色；对于许多开发人员来说，AI 可能已经是 IDE 的一项预期功能。将 AI 助手视为注册报名仍然是一个小麻烦，但这最终会改变。我很快就把整个 IDE 和 AI 助手运行起来，而且运行速度相当快。

在某种程度上，“嘿！看！我们有 AI”是 IDE 在环境扩展和达成共识的预期仍在形成过程中的当前业务需求。到明年，其中大部分将作为 IDE 体验的一部分存在，就像今天的剪切和粘贴一样。
