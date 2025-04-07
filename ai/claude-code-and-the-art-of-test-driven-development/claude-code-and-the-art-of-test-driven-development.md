<!--
title: Claude Code与测试驱动开发艺术
cover: https://cdn.thenewstack.io/media/2025/04/71a5424f-a-c-ixkatobx6y0-unsplashb.jpg
summary: 用Anthropic的 Claude Code 玩转 TDD！这个“终端代理编码工具”基于 LLM，可读取项目代码并辅助开发。实测发现，Claude Code 能生成通过测试的代码，甚至能根据测试反馈进行调试和改进，与 TDD 流程配合良好，助力云原生应用开发。
-->

用Anthropic的 Claude Code 玩转 TDD！这个“终端代理编码工具”基于 LLM，可读取项目代码并辅助开发。实测发现，Claude Code 能生成通过测试的代码，甚至能根据测试反馈进行调试和改进，与 TDD 流程配合良好，助力云原生应用开发。

> 译自：[Claude Code and the Art of Test-Driven Development](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/)
> 
> 作者：David Eastman

虽然我主要喜欢代码补全，但 LLM 助手在 Visual Studio Code 中给了我不少问题。在更改用于审查的大型语言模型 (LLM) 扩展时，VS Code [几乎崩溃了](https://thenewstack.io/gemini-code-assist-review-code-completions-need-improvement/)。因此，虽然我不确定是否要运行一个不在 IDE 内部运行的代码助手，但至少它不必与 VS Code 配合使用。

Anthropic 的 [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) 将自己描述为“存在于终端中的代理编码工具”。它读取您的项目并“简化您的工作流程”。我不太清楚最后一点意味着什么，但其余的流行语都很好。Claude Code 被描述为一个不断发展的 beta 研究预览版，坦率地说，这可以描述所有生成式 AI (GenAI) 产品。我知道这可能是“氛围编码”的计划路径，因为它通过开发人员进行低代码或无代码交互。但我现在忽略这一点。

不过，我确实想看看它是否可以进行一些测试驱动开发 (TDD)。有趣的是，有人反对 [TDD](https://buttondown.com/hillelwayne/archive/verification-first-development)，部分原因是 LLM 在这方面存在困难。LLM 非常擅长在代码完成后生成通过测试；不幸的是，事后编写测试意味着您只是在批改自己的作业。但我被告知 LLM 可以与 TDD 一起工作。

## 安装 Claude Code

它需要 Node.js 18+，所以我打开我的终端：

![](https://cdn.thenewstack.io/media/2025/04/cf147c8c-image-300x63.png)

我对这个没问题，所以让我们投入一些硬币。如果您转到 [Anthropic 控制台](https://console.anthropic.com/)，您可以注册并购买一些令牌。这不是一个巨大的负担，但考虑到我正在尝试实验室中的一些东西，他们本可以更温和一些：

![](https://cdn.thenewstack.io/media/2025/04/77cf15e9-image-1-772x1024.png)

该模型想要查看您的项目代码，因此我将启动一个带有测试的控制台项目，看看我是否可以说服它与我一起进行一些 TDD。如果您查看我在 [Codium](https://thenewstack.io/make-your-dev-life-easier-by-generating-tests-with-codiumai/) 上发布的文章，您将看到一些相同的技术和代码应用。

我从一个新目录打开 VS Code，然后使用命令面板创建一个新项目作为控制台应用程序。我还想使用 Nunit 测试框架，因此我将 [配置](https://docs.nunit.org/articles/nunit/getting-started/installation.html#examples-of-what-you-get) 直接添加到我的 csproj 中。

然后我定义一个最小的 BankAccount 类：

```csharp
namespace BankAccount{ 
    public class SavingsAccount { } 
    class Program { 
        static void Main(string[] args) { 
            SavingsAccount account = new SavingsAccount(1000); 
            account.Deposit(500); 
            account.Withdraw(200); 
            Console.WriteLine($"Current balance: {account.GetBalance()}"); 
        } 
    }
}
```

当然，以上代码不会运行——这就是重点。我添加了基本的测试类，只是为了确保我已正确设置所有内容：

```csharp
using BankAccount; 
using NUnit.Framework; 

public class Tests { 
    [SetUp] 
    public void Setup() { } 

    [Test] 
    public void Test1() { 
        Assert.Pass(); 
    } 
}
```

好的，现在我们可以做我们的高级工程师的工作，并定义测试，以便我们的初级工程师（Claude）可以编写代码。以下是初始测试：

```csharp
using BankAccount;
using NUnit.Framework;

public class Tests{ 
    [SetUp] 
    public void Setup() { } 

    [Test] 
    public void test_deposit() { 
        SavingsAccount ba = new SavingsAccount(); 
        ba.Deposit(20); 
        Assert.AreEqual("$20", ba.ShowBalance()); 
    } 

    [Test] 
    public void test_withdraw_more_than_balance() { 
        SavingsAccount ba = new SavingsAccount(); 
        Assert.Throws<Exception>(() => ba.Withdraw(25)); 
    }
}
```

现在让我们完成 Claude 的安装并让它开始工作。我们进入工作目录并打开 Claude：

![](https://cdn.thenewstack.io/media/2025/04/9a9c07d5-image-2-850x1024.png)

结果是：

![](https://cdn.thenewstack.io/media/2025/04/d8b4b61c-image-3-1024x584.png)


是的，这是一些不错的 [ASCII 艺术](https://thenewstack.io/cascii-and-why-developers-should-use-ascii-diagrams/)。当然，我使用上面的 Anthropic 控制台设置了这个。

然后我们被推出并进入浏览器。我才刚进入终端！

![](https://cdn.thenewstack.io/media/2025/04/a639ae64-image-4-300x274.png)

现在我进来了。请记住，这是一个 beta 研究预览版。

首先，我可以创建一个 [claude.md](http://claude.md) 文件，我可以用它来指示 Claude。希望我可以在这里告诉它我们正在进行 TDD。我在生成的文件中添加了一行描述我的意图，但我不知道它是否有效。

在我要求它通过测试后，Claude 编写了代码，我们通过了测试：

![](https://cdn.thenewstack.io/media/2025/04/a4927a19-image-7-1024x286.png)

为了确认，测试确实通过了：

![](https://cdn.thenewstack.io/media/2025/04/ee322eed-image-8.png)

生成的代码很好。所以我们正在进行 TDD！我想说的是，*不*在 IDE 中进行感觉更好。
当然，这段银行代码既基础又简单，可能在网上随处可见。因此，我将通过测试引入每日利息的概念：

```java
  [Test]
  public void test_daily_interest_rate()
  {
      SavingsAccount ba = new SavingsAccount();
      ba.SetDailyInterestRate(0.05m);
      ba.Deposit(100);
      ba.ApplyDailyInterest();
      Assert.AreEqual("$100.05", ba.ShowBalance());
  }
```

我保存它，然后再次要求Claude编写缺失的方法。它成功地提出了所需的新代码：

![](https://cdn.thenewstack.io/media/2025/04/1101e083-image-9-891x1024.png)

这很好。显然，储蓄账户应该有一个默认的每日利率，但就敏捷编码而言，这个进展很好。现在，如果你仔细观察，你会发现一个错误。我认为每日利率是一个百分比。但是代码直接将余额乘以0.05，这代表5%。对于每日利息来说，这有点高。当我们运行测试时，这个错误是完全可见的：

![](https://cdn.thenewstack.io/media/2025/04/8398113c-image-10-1024x291.png)

![](https://cdn.thenewstack.io/media/2025/04/26f75f39-image-11-1024x166.png)

可以把这看作是与伙伴一起进行TDD。我会告诉Claude，利率应该是百分比：

![](https://cdn.thenewstack.io/media/2025/04/8a132b3c-image-12-1024x609.png)

就这样。我会要求Claude进行更改。一切都很好，但是现在当我们运行测试时，我们遇到了另一个错误：

![](https://cdn.thenewstack.io/media/2025/04/a784f738-image-15-1024x207.png)

这只是一个格式问题。我们只希望余额的精度在小数点后显示两位，以表示美分。

Claude理解这一点并进行了修复：

![](https://cdn.thenewstack.io/media/2025/04/11c38b6c-image-14-1024x388.png)

现在我必须实际修复我的测试，它没有坚持正确的精度。在我修复我的测试之后，我们终于成功了：

![](https://cdn.thenewstack.io/media/2025/04/aa380409-image-16.png)

## 结论

所以我证明了Claude Code原则上可以进行TDD。这让我很高兴，因为它让我拥有了相当安全的代码，而不必希望我的LLM伙伴理解一切。LLM在技术上并不理解任何东西；这不是工具的工作。但是它可以遵循指令。重要的是要注意，我没有让它运行测试——当人类可以挑选出一个方向时，没有必要让它自己循环。

TDD的原则与LLM的辅助配合得很好，因为人类开发人员可以修复质量障碍并定义设计。事实上，这通常是高级工程师与混合团队合作的方式，所以它甚至没有形成一种新型的关系。我只能希望未来的LLM助手能够推进TDD，并缩小他们目前所遭受的信任差距。