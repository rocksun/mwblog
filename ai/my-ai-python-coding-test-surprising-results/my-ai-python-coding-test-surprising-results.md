
<!--
title: 我的AI Python编程测试： 令人惊讶的结果
cover: https://cdn.thenewstack.io/media/2025/02/0aee6a55-jeshoots-com-2vd8lihdnw-unsplash-1.jpg
-->

使用 Ollama 和各种 LLM 的这个实践实验揭示了使用 AI 生成 Python 代码的当前局限性、陷阱和最佳实践。

> 译自 [My AI Python Coding Test: Surprising Results](https://thenewstack.io/my-ai-python-coding-test-surprising-results/)，作者 Jack Wallen。


你知道它要来了。

你已经听到了抱怨声。

你已经阅读了备忘录，听取了谈话。

AI正在编写代码。

相信我，我理解这种担忧。我也是一位小说家，我读到过其他作家使用AI以人类无法企及的速度创作书籍的报道。一线希望是，使用AI进行的创作往往非常糟糕。

但是编码方面呢？

我决定测试一下[Ollama](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/)，让它编写一些[Python](https://thenewstack.io/python/)程序，看看效果如何。

我没有留下深刻的印象。

首先，让我告诉你我是怎么做的。

## 我使用了什么

首先，我决定使用本地安装的Ollama实例，以及[Msty](https://msty.app/)前端。我决定将前端添加到组合中，因为我希望它尽可能高效。虽然Ollama的终端使用非常简单，但Msty使某些功能更容易访问（例如添加新模型和知识栈，以及使用提示库）。

最初，我决定使用llama-3.2模型进行第一轮测试。我向Ollama提供了以下提示：

```
Write a Python application that asks the user how many dice to roll, how many sides are on each dice, and then roll the dice the user has entered
```

这是llama-3.2吐出的代码：

```py
import random

 def get_num_dice():
     """Asks user for number of dice, continues asking if invalid."""
    while True:

         try:
            num_dice = int(input("How many dice would you like to roll? "))
            if num_dice < 1:
                print("Please enter a positive integer.")
            else:
                 return num_dice
        except ValueError as e:
            print(f"Invalid input: {e}")

def get_num_sides():
    """Asks user for number of sides, continues asking if invalid."""
    while True:
         try:
            num_sides = int(input("How many sides does each dice have? "))
            if num_sides <= 0:
                print("Please enter a positive integer.")
            else:
                return num_sides
        except ValueError as e:
            print(f"Invalid input: {e}")

def roll_dice(num_dice, num_sides):
    """Rolls specified number of dice with specified number of sides."""
    results = [random.randint(1, num_sides) for _ in range(num_dice)]
    
return str(results).replace("'", ', ').strip('[]')

def main():
    print("Welcome to Dice Roller!")
        num_dice = get_num_dice()
    if num_dice == 0:
        print("Not rolling any dice.")
        return
    num_sides = get_num_sides()
    results_str = roll_dice(num_dice, num_sides)

    # Display the results
    print(f"Rolling {num_dice}d{num_sides}")
    if len(results_str) > 5:
        half_points = (len(results_str) + 4) // 2 
        first_half = ', '.join([str(result)[:half_points] for result in results.split(',')[0:-1]])
        second_half= [result[half_points:]for result in results.split(',')]
     else: 
        print(f'{results_str}')

if __name__ == "__main__":
    main()
```

猜猜怎么着？它不起作用。它看起来好像可以完美运行，但最终陷入了一个循环，询问*你想掷多少个骰子？*

代码中存在一些明显的错误。看看第49行，它是这样的：

```
first_half = ', '.join([str(result)[:half_points] for result in results.split(',')[0:-1]])
```

应该是：

```
first_half = ', '.join([str(result)[:half_points] for result in result.split(',')[0:-1]])
```

Ollama的输出是*results.split*，而应该是*result.split*。这是一个非常愚蠢的错误，但很容易修复。

下面一行也有一个类似的错误，它是：

```
second_half= [result[half_points:]for result in results.split(',')]
```

应该是：

```
second_half= [results[half_points:]for result in results.split(',')]
```

在进行这些更改后，程序终于可以运行了。

即便如此，如果在被问到要掷多少个骰子时输入一个较大的数字，错误会再次出现，只是这次告诉你*results.split*应该是*result.split*。猜猜怎么着……这也不会运行！

然后，我尝试使用gemma2:2b模型进行相同的提示。正如你可能预料的那样，生成的代码无法工作。同样，它最终陷入了一个循环，询问要掷多少个骰子。

如果我将程序简化为仅创建一个应用程序来掷随机骰子数字，gemma2:2b就能正确完成。

我回到每个模型并运行不同的查询，让它创建各种[Python应用程序](https://thenewstack.io/how-to-use-pyscript-to-create-python-web-apps/)（难度各不相同），发现结果好坏参半。例如，我为gemma2:2b编写了这个查询：

```
write a python program that accepts input for a users clothing choices and then reports what they should wear
```

该查询的输出工作正常。然后，我使用Llama 3.2模型运行了相同的查询，它生成的代码截然不同，但也能运行。

接下来事情变得令人恼火。

我将[DeepSeek R1](https://thenewstack.io/how-to-run-deepseek-r1-on-aws-using-infrastructure-as-code/)模型添加到Msty中，每次我查询时，响应似乎更像是关于如何编写代码的冗长讨论。llama和gemma大约需要30秒才能吐出的东西，[DeepSeek](https://thenewstack.io/icymi-deepseek-is-an-open-source-success-story/)运行了10分钟，除了冗长的来回交流之外，没有给我任何有用的东西，这种交流感觉既随机又受引导。

## 我的发现

最后，这是我发现的关于使用AI编写代码的内容：

1. 从一个简单的查询开始，例如编写一个掷骰子的程序。
2. 测试输出。
3. 然后要求AI使用如下查询更新原始程序：*采用相同的程序，并允许它询问用户要掷多少个骰子。*
4. 测试输出。
5. 进一步，使用另一个查询来改进应用程序。
6. 测试输出。
7. 不断改进，直到完成。

每当我使用 Ollama 和 Msty 以上述策略编写 Python 程序时，结果都比直接深入研究更复杂的东西要好得多。另一个重要结论是，不同的模型更适合此目的。例如，直接跳过 DeepSeek，使用 Qwen 模型之一（例如 Qwen2.5 Coder）。当我尝试使用 Qwen2.5 Coder LLM 进行相同的实验时，事情变得更加可预测。几乎每次我使用这个模型，结果都有效。更好的是，它生成的代码远没有那么复杂，因此更容易阅读和调试（在需要时）。

另一件事是不要期望完美的结果。你 *将* 不得不调整一些东西，甚至尝试不同的模型。我甚至遇到了 Msty 崩溃的问题，这帮助我得出了这个简单的结论：

创建 AI 的公司希望你相信他们的工具和你一样有能力编写代码，但这并不完全正确。当你使用 AI 编写代码时，必须仔细检查输出中的每一行并进行测试，因为很可能你将花费大量时间进行调试。

实际上，我对写这篇文章感到兴奋，因为我用一些相当基本的应用程序测试了 Ollama 和 Msty，它的表现非常出色。然而，当事情变得更加复杂时，AI 让我失望了。

最后，请记住以下关键事项：

- 选择合适的模型。
- 从简单开始。
- 审查代码。
