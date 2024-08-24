# 开发者：不要只是阅读设计模式，要动手实现它们

![Featued image for: Devs: Don’t Just Read About Design Patterns, Implement Them](https://cdn.thenewstack.io/media/2024/08/8e6b8f9d-fabrizio-conti-b5rpuibfeme-unsplash-1024x683.jpg)

虽然[设计模式](https://en.wikipedia.org/wiki/Software_design_pattern)有助于将软件作为工程学科进行记录，但它们在作为教学辅助方面并没有太大帮助。在遇到[可重复模式](https://thenewstack.io/serverless/serverless-architecture-five-design-patterns/)后，确认其存在是有用的，但理解示例仍然是准备解决新问题的最佳方法。

这篇文章可能看起来像是关于策略模式（或命令模式），但实际上它描述的是一群英雄动物执行寻找邪恶巢穴的任务。

可扩展软件设计中重要的是什么可以被修改或添加而不会破坏系统。你一定经常听到“ [解耦](https://thenewstack.io/how-decoupling-can-help-you-write-better-software/)”这个词来描述具有这种特性的系统。相反，某些方面将无法修改，或者需要进行很多修改才能更新。

在这个高度人为但轻松愉快的例子中，我们有一支灵活的英雄动物队伍，每个动物的属性决定了哪些动物是任务所必需的。把它想象成接力赛。我本可以使用漫威英雄，但我相信迪士尼雇佣了很多律师。我使用了 C#，但任何面向对象的语言都可以轻松地支持它。

可扩展软件设计中重要的是什么可以被修改或添加而不会破坏系统。

一项任务涉及穿越一个包含两个生物群落（一个表示具有特定气候的区域的专业术语）和一个巢穴的地点。例如，一个森林岛屿城堡。每只英雄动物都熟悉一个家乡生物群落，并拥有一些自然技能。鉴于每只动物只有一个家乡生物群落，一个任务团队可能需要两到三名英雄。

这里重要的是，系统使用你定义的任何动物英雄来完成任务，并且还理解可能没有足够的可用英雄。

因此，设计将任务与英雄队伍解耦。但是，它要求动物技能的定义保持不变，因为这是共同的理解。

我们从英雄动物列表或队伍开始。从技术上讲，这也是一个注册表。

```csharp
public static List<HeroAnimal> roster = new() { new Penguin(), new Shark(), new Goat(), new Gorilla()}; 
```

因此，你可以看到队伍中有四只英雄动物，即必须在其他地方定义的类。
为了指定一个契约，我们通常会定义一个接口，但我使用了[继承](https://thenewstack.io/how-to-use-inheritance-in-python/)。我们的契约是英雄的抽象定义，它定义了技能和家乡生物群落。

```csharp
public abstract class HeroAnimal { 
    public abstract bool canFly(); 
    public abstract bool canSwim(); 
    public abstract bool canClimb(); 
    public abstract bool canCrawl(); 
    public Biome Home { get; protected set; }
}
```

因此，每只英雄动物都拥有可能帮助它潜入邪恶巢穴的技能。巢穴用一个接口定义：

```csharp
public interface Lair { 
    bool CanHeroBreakIn(HeroAnimal hero); 
}
```

巢穴只是一个地方，比如城堡，我们需要知道潜入需要哪些技能：

```csharp
public struct Castle : Lair { 
    public bool CanHeroBreakIn(HeroAnimal hero) { 
        return hero.canFly() || hero.canClimb(); 
    } 
}
```

因此，城堡可以通过飞行英雄从空中潜入，也可以通过攀爬墙壁潜入。
动物生活在特定的生物群落中：

```csharp
public enum Biome { Forest, Ice, Plains, Swamp, Sea }
```

我们有一些通用的类可以用作模板来定义我们的英雄动物，例如：

```csharp
public abstract class Fish : HeroAnimal { 
    public override bool canFly() => false; 
    public override bool canSwim() => true; 
    public override bool canClimb() => false; 
    public override bool canCrawl() => false; 
    public Fish() { 
        Home = Biome.Sea; 
    } 
}
```

最后，我们可以实例化的一个具体示例：

```csharp
public class Shark : Fish { }
```

英雄企鹅是一种鸟类，但不是普通的鸟类：

```csharp
public class Penguin : Bird { 
    public override bool canFly() => false; 
    public override bool canSwim() => true; 
    public Penguin() { 
        Home = Biome.Ice; 
    } 
}
```

一旦任务确定，系统就会选择所需的团队。这只是一个简单的列表搜索和匹配。可以通过在每次运行之前将列表混合起来来改进系统。
我使用了[Programiz 上的 C# 在线编译器](https://www.programiz.com/online-compiler/6gfMhWkH9umce)将所有代码放在一个文件中，这样你就可以从那里运行代码，或者修改它。你可以定义和注册新的动物英雄、巢穴或任务。你也可以添加生物群落，但删除它们可能会破坏现有的英雄。

事实上，你拥有足够的知识来自己编写代码。

以下是在线运行一次的结果：

```csharp
// ... (rest of the code)
```
我们的英雄动物名单：企鹅！鲨鱼！山羊！大猩猩！任务：找到邪恶博士的森林岛城堡

我们的英雄团队执行任务：

* 鲨鱼穿越海洋
* 大猩猩穿越森林
* 山羊潜入城堡巢穴

=== 代码执行成功 === 

从这里我们可以理解，英雄动物可以在不了解任何任务的情况下被定义。反之，任务也未提及可用的英雄。我们可以自由地添加或删除英雄动物。

我们需要的只是一个类实例列表，可以在需要时进行询问。这意味着这些类应该具有相似的接口，以便它们可以对相同的问题做出响应。

显然，更实际的例子应该会浮现在脑海中，例如创建有效的系统配置，其中可用[组件](https://thenewstack.io/the-risks-of-decomposing-software-components/)列表可以增长或缩小。或者安排事件并将它们与可用且合适的场地匹配。

因此，虽然我们应该始终尊重四人帮（[经典书籍](https://en.wikipedia.org/wiki/Design_Patterns)的作者）关于软件设计的论述，但最好是在自己解决问题之后再这样做。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以收看我们所有的播客、访谈、演示等。