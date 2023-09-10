# 编码中学习：LLM 如何暗中教导你

LLM 可以提供即时的、针对实际编程任务定制的知识；这是学习编码习语和库的绝佳途径。

翻译自 [Learning While Coding: How LLMs Teach You Implicitly](https://thenewstack.io/learning-while-coding-how-llms-teach-you-implicitly/) 。

![](https://cdn.thenewstack.io/media/2023/09/5682e1b8-pexels-somchai-kongkamsri-104757-1-1024x594.jpg)
*图片来自 Pexels*

我一直是动手学习的人，尤其是当涉及学习如何使用和创建软件时。我希望能够从规范中学习协议，通过阅读文档来熟悉应用程序，并通过结构化的课程吸收编码技巧，但在我深入某个项目，专注于一个明确的目标，并能在调试器中运行实时代码之前，这些东西对我来说还不够生动。在我的文章“[Radical just-in-time learning](https://blog.jonudell.net/2023/06/14/radical-just-in-time-learning/)”中，我回忆了《矩阵》中我[最喜欢的场景](https://www.youtube.com/watch?v=SoAk7zBTrvo)。

> **尼奥**:你会开直升机吗?
> 
> (看向直升机)
> 
> **特丽妮蒂**:还不会。
> 
> (拿起电话)
> 
> **坦克**:操作员。
> 
> **特丽妮蒂**:我需要一份 B-212 直升机的飞行员程序。快点。
> 
> (眼皮短暂地颤动)
> 
> **特丽妮蒂**:走吧。
>
> (他们跳上直升机，从房顶飞离)

在那个项目中，我需要学习驾驶的直升机是 React，坦克操作员的角色由一个 LLM(实际上是一组 LLM)担任，及时获得的概念包括 [useState](https://react.dev/reference/react/useState)、[useEffect](https://react.dev/reference/react/useEffect) 和 [JSX](https://react.dev/learn/writing-markup-with-jsx)。我不需要成为一个完全胜任的飞行员，我只需要起飞并进行短途飞行。在 LLM 的指导下，我以比其他方式更快的速度完成了这些，起点几乎是零 React 知识。

我“学习”了 React 吗？几乎没有！这是一次探索性的练习。所产生的概念验证可能会也可能不会发展，但如果需要，我已经打开了大门。在我的初级 React 知识的基础上，我将进行后续的迭代，知道文档和课程不是唯一的方式。我将能够调用及时在特定于任务的上下文中传递的指导。

## 环境学习

我之前文章的亮点是 ChatGPT 及其代码解释器插件的出色表现。在目标导向的自主循环中运行它，这里的目标是通过我编写的测试，这是一次让人大开眼界的体验。但是在练习的过程中——它涉及编写代码来处理 changelogs，然后以各种方式可视化更改——我学到了许多有用的东西。

打印预期值和实际值

这是我编写的测试之一。

```python
def test_extract_contributors():
    expected_contributors = {
        "v0.115.0": ["pdecat"， "rasta-rocket"， "tinder-tder"]，
        "v0.114.0": []，
        "v0.113.0": ["pdecat"， "pdecat"]， 
    }
    actual_contributors = extract_contributors(changelog)
    assert expected_contributors == actual_contributors， f"Expected {expected_contributors}， got {actual_contributors}"
```

我喜欢用最简单的方法做事，所以这里没有测试框架，只是一个基本的assert。我不知道可选的第二个参数(或者可能已经忘记了)，所以我最初使用了第二行代码来打印预期值和实际值。我可以查一下吗?当然可以，但没有重要到要中断我的流程。相反，发生的是:LLM以编写用于通过测试的代码的副产品的形式向我展示了这种惯用法。当你与另一个人一起工作时，这就是可能发生的隐式知识传递，你没有明确提出问题，你的伙伴也没有明确回答它。知识只是自然出现，并通过渗透进行传递。

以下是在过程中发生的其他一些隐性知识传递。

argparse默认值

我已经有一段时间没有使用Python的argparse模块了。另一件我可能从未学过的事，或者忘记了的是这个惯用法:

```python
parser.add_argument("--count_all_plugins"， <em style="color: blue;">action="store_true"</em>， help="Count all plugins")
```

当ChatGPT使用action=”store_true”时，我以为我知道那意味着什么，但要求LLM进行验证。在Cody和Copilot提供的一系列解释中，我发现ChatGPT的这个解释最有帮助:

这使得--count_all_plugins成为一个不需要值的标志。它在命令行上的简单出现意味着“是”或True，它的缺失意味着“否”或False。

我可以从文档中学习这一点吗?同样，可以。我会那样学习吗?同样，不太可能。如果我缺乏命令行上简单出现意味着真概念，我就必须首先想到这个想法，然后在文档中挖掘，看是否可行，如果可行，如何实现。

相反，LLM在需要的上下文中使这个概念浮现出来，向我展示如何应用它，当被要求解释时，它以该特定上下文为基础进行解释。这不仅仅是命令行上简单出现意味着真，而更具体的是count_all_plugins在命令行上简单出现意味着真。

也许我的一个缺点是，我从一个特定的例子中学习最好，基于我自己的情况，从中我可以推广。但我怀疑我不是唯一这样操作的学习者。在任务上有了一些进展之后，我会参阅文档来丰富我的理解。但我很少想从那里开始。仅用文档来回答已知的问题已经够艰难的了，用它们来回答你没有想到的问题就更艰难了。当环境知识可以在做任务时出现时，我是一个更有效的学习者。

re.escape

根据文档:“如果你想匹配可能包含正则表达式元字符的任意文本字符串，这很有用。”多年来，我编写了许多Python正则表达式，从未学过这个，结果，可能给自己造成了很多困扰。有LLM在可教导的时刻以顺带的方式向我展示这种惯用法，是学习它的最佳方式。

否定前瞻断言

这里有一些我很确定我从未学过的东西。它出现在ChatGPT编写的用于匹配changelog中的项目符号的正则表达式中。如果不理解它是什么，我会不舒服地使用它，但没有必要:我不仅得到了代码，还能要求并接收解释。

(?!\s*-):这是否定前瞻断言。它检查下一行是否NOT以可选空格后跟破折号(-)开头。换句话说，它确保下一行不是新列表项的开始。

组合-\s[^\n]*(?:\n(?!\s*-).*)* 匹配可以跨多行的列表项，只要后续行不以新列表项开头。

非本地变量

当我要求ChatGPT重构一个变得太复杂的函数，并在此过程中使用嵌套函数时，我介绍了另一种我从未遇到过的惯用法。我有时使用global关键字引用任何函数范围之外的变量，在这种情况下可能也会(内疚地)这样做。但在这里我学到了 nearest-enclosing-scope-that-is-not-global的变量概念。

快速上手库

一旦我能够可靠地捕获changelog数据，就是使用表格和图表进行可视化的时候了。现在，我最习惯SQL，所以当ChatGPT提供基于pandas.DataFrame的解决方案时，它又创建了一个学习机会。我在几年前使用过pandas，既不广泛也不容易。由于HTML表格是我期望的输出之一，这对pandas.DataFrame.to_html方法是一个很好的介绍。

我也使用过Matplotlib，同样也不广泛，不容易，所以我很感谢ChatGPT向我展示了如何将其应用于手头的任务。有了那里的代码，我的脚本编写了两个文件:一个包含表格的HTML文件和HTML中引用的图像文件。

如果可能的话，我喜欢最小化组成解决方案的移动部分的数量。如果其他条件相同，一件事可以用一个文件完成，我会更喜欢它，而不是一个多文件包。我需要的图表很简单，我知道仅使用HTML和CSS在一个文件中创建它是可能的，该文件还包含HTML表格，但我通常不会特意努力使这种事情发生。然而，现在有了一个乐于助人的助手在场，为什么不试一试呢?

尽管仅使用HTML和CSS的实验没有产生成功的结果，但我也不认为它是失败的。这是CSS flexbox布局机制的快速复习，其中包含我可以在与手头任务相关的运行代码的上下文中玩弄的align-items、flex-direction和gap的示例。基本图表很快就成形了，然后精化的努力产生的回报越来越小。正确设置轴确实很棘手——不出所料!在这个过程中，ChatGPT做出了一个有趣的建议:

让我们试试不同的策略。我们将使用Matplotlib的标准功能，然后使用mpld3将其转换为HTML表示形式。

我顺带学到的另一件有用的事情:Matplotlib可以通过mpld3渲染为HTML，后者可以“将Matplotlib带到浏览器”!这让我更接近了期望的结果，但y轴仍然有问题，所以我从这个滑坡上后退了。然而，这次迂回没有花费很长时间，我与Matplotlib/mpld3的互动感觉像是一个有价值的学习经历。如果我是从零开始，在文档中搜索类似我正在尝试编写的代码的示例，那将是痛苦和耗时的。但ChatGPT意识到我正在工作的上下文，使我能够快速迭代。

当Matplotlib/mpld3的努力停滞不前时，我要求ChatGPT建议另一个可以使用HTML/CSS渲染图表的图表库。它建议plotly、Bokeh和Vega-Altair。我之前与plotly有过简短的经验，对Bokeh或Vega-Altair都没有。所以我会倾向于先试试plotly。ChatGPT对它的描述——从Matplotlib过渡最简单——加强了这种倾向。

plotly的解决方案需要一些调整，当然，但LLM的帮助再次极大地加速了我的学习。我们最终达成的协议是:

```python
fig.update_layout(
    title="Monthly Contributions"， 
    xaxis_title="Month"，
    yaxis_title="Contributions"，
    template="plotly_white"， # 使用白色背景模板
    xaxis=dict(
        tickvals=monthly_counts.index.strftime('%Y-%m').tolist()， # 设置刻度位置
        ticktext=monthly_counts.index.strftime('%Y-%m').tolist()， # 设置刻度标签
        tickfont=dict(size=10)， # 减小字体大小 
        tickangle=-45 # 逆时针旋转
    )，
    bargap=0.15， # 在条之间稍微减少间隙
    width=1000 # 增加绘图的宽度
)
```

在阅读文档和看过代码示例之后，ChatGPT能够比我从零开始时想到的建议更好的策略来管理刻度标签和值。仍然有错误开端和死胡同!但通过一种非常类似配对编程的协作，解决方案很快出现了。

现在，编程更多地涉及找到和应用存在令人困惑的繁多的库和组件。你不太可能编写我们通常认为的代码行，更有可能是调整参数和设置。文档中说明这些参数和设置的含义与当你试图使用它们时实际发生的事情之间存在巨大的鸿沟。LLM帮助弥合这一鸿沟的能力可能最终成为它们提供的最强大的代码编写辅助形式之一。