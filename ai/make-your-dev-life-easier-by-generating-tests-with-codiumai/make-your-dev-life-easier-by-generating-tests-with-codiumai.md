
<!--
title:  用CodiumAI生成测试，让开发生活更轻松
cover: https://cdn.thenewstack.io/media/2023/11/54f5685e-codiumai-1024x598.jpg
-->

许多开发人员还在抱怨编写测试麻烦，所以用AI生成测试代码的想法一直很诱人。CodiumAI就是这样一款工具。

> 译自 [Make Your Dev Life Easier by Generating Tests with CodiumAI](https://thenewstack.io/make-your-dev-life-easier-by-generating-tests-with-codiumai/)，作者 David Eastman 一直是伦敦的专业软件开发人员，曾在甲骨文公司和英国电信工作，也是一个顾问，帮助团队以更敏捷的方式工作。他写了一本关于UI设计的书，从那时起就一直在撰写技术文章......

许多开发人员仍然声称他们不喜欢编写测试，因此使用AI生成测试的想法总是有吸引力的。  

当然，测试不一定是次要问题——使用测试驱动开发(TDD)方法，你会先编写测试。虽然这是每个团队都应该尝试的好事，但常见的做法是首先创建一个最小可行产品(MVP)，如果有证据表明它有前景，然后再使用完整的单元测试继续项目。

我以前没有见过 [CodiumAI](https://www.codium.ai/)，但由于它在主页上生成了一个简单明了的电梯演说——“为繁忙的开发人员生成有意义的测试”，我已经准备好给它一个试试了。显然，他们正在试图进入 OpenAI 的 GPT 模型开辟的工具空间——事实上，它是由“GPT-3.5&4 和 TestGPT-1”提供支持的。

CodiumAI 的实现目前只适用于 Visual Studio Code 和 JetBrains；我将使用前者。我发现 VSC 有点尴尬，但至少它应该能处理 C#，这是我偏爱的语言。但我也知道 JetBrains 的工具非常受欢迎。

作为测试示例，我将使用一个非常简单的银行账户类，其中有三个方法：withdraw、deposit 和 balance。让我们假设这是一个简单的账户，没有透支功能。我们应该已经对要测试的内容有了强烈的感觉:

- 我们不能提款超过我们拥有的金额。
- 如果输入的存款或提款金额为零，我们不应继续操作。
- 请求的存款或提款金额都不应该是负数。

我们对这些规则的推理来自不同的地方。第一个测试反映了账户的业务规则。第二个测试反映出使用真正的银行系统需要一定的费用；所以虽然零可能是一个有效的值，但如果是这种情况，我们不应该发出调用。第三条规则只是输入范围的限制——这应该通过使用无符号输入来处理。

回到 Codium。在市场页面上，它似乎更偏爱 Python、JavaScript 和 TypeScript，但它也明确显示了一个菜单操作，用于为其他语言生成示例。和往常一样，Visual Studio Code 以一片混乱的窗口群打开，但我还是能继续。

一个小对话框在屏幕底部要求我登录 Github —这在任何地方几乎都是常态。

![](https://cdn.thenewstack.io/media/2023/11/6b6b072b-untitled.png)

通过一些身份验证，我进去了。在某个时候，.NET 加载进来，我让它创建了一个简单的控制台项目。这里是代码:


```csharp
public class BankAccount  
{  
  private uint balance;  
  public string ShowBalance() => $"{CURRENCYSIGN}{balance}";  
  private const string CURRENCYSIGN = "$";  
  
  public void Deposit(uint funds)  
  {  
     balance = balance + funds;  
     Console.WriteLine($"{CURRENCYSIGN}{funds} deposited. Balance now {ShowBalance()}");   
  }   
  
  public void Withdraw(uint funds)  
  { 
    if (funds > balance) throw new Exception($"Cannot withdraw {CURRENCYSIGN}{funds}, balance is {ShowBalance()}");   
    balance = balance - funds; 
    Console.WriteLine($"{CURRENCYSIGN}{funds} withdrawn. Balance now {ShowBalance()}");
  }
  
  static void Main(string[] args)  
  {  
    BankAccount ba = new BankAccount();  
    try {
      // Money in  
      ba.Deposit(20);
    
      //Money out  
      ba.Withdraw(5);
    
      //Too much ba.Withdraw(25); 
    }  
    catch (System.Exception ex)  
    {  
       Console.WriteLine($"Error {ex.Messag}");   
    }
  }
}
```

从控制台中，主方法的测试给出了预期的结果:

```
BankAccount> dotnet run
$20 deposited. Balance now $20  
$5 withdrawn. Balance now $15
Error Cannot withdraw $25， balance is $15
```

现在这并不非常复杂，例如也不需要任何模拟框架。然而，我们感兴趣的是这个工具是否呈现了可用的测试。

好的，我们现在可以要求 CodiumAI 生成测试了。在类的正上方整齐地提示了如何生成测试：

![](https://cdn.thenewstack.io/media/2023/11/67625b29-untitled-1.png)

首先，AI 生成了一个非常可接受的该类的英文总结:

> The **BankAccount** class represents a bank account and provides methods for depositing and withdrawing funds. It also has a method to display the current balance.

它为三个方法都提供了英文解释。它还生成了“代码建议”，这些在某种程度上都是合理的。例如，它建议使用十进制值而不是无符号整数。我将让读者自己去考虑这方面的利弊(如果感兴趣的话)。

这使我对它生成的测试充满信心。而且测试确实不错。

呈现非常漂亮。它生成了一些测试，并总结了它可以生成的其他测试。首先是快乐路径:

![](https://cdn.thenewstack.io/media/2023/11/cf067ee5-untitled-2-1024x444.png)

这里是生成的两个快乐路径示例:

```csharp
[Test]  
public void test_deposit()   
{
  BankAccount ba = new BankAccount();
  ba.Deposit(20); 
  Assert.AreEqual("$20"， ba.ShowBalance());
}

[Test]
public void test_withdraw_more_than_balance() 
{
  BankAccount ba = new BankAccount();
  Assert.Throws<Exception>(() => ba.Withdraw(25));
} 
```

从技术上讲，抛出异常不是“快乐路径”的一部分，但要面对现实——两年前，如果一个应用程序能够理解“快乐路径”是什么，我会感到惊讶。所以，欢呼吧。

每个可以消费的测试都很好地呈现了在测试框架中：

![](https://cdn.thenewstack.io/media/2023/11/a531fe9e-untitled-3-1024x323.png)

好的，让我们看看边缘案例：

![](https://cdn.thenewstack.io/media/2023/11/e197f120-untitled-4-1024x441.png)

这些处理零元提款的情况——这暗示着我可以扩展这些测试和代码来满足我不在必要时调用实际系统的需求。注意，您可以根据需要生成和重新生成测试。

最后是“其他”案例：

![](https://cdn.thenewstack.io/media/2023/11/6db3c205-untitled-5-1024x391.png)

这里我们感兴趣的是一个测试账户的最大值——如果我们对使用无符号整数不是很确定，我们会想要检查与账户大小变化相关的任何回归情况。

## 结论

在可用的AI工具背景下查看这个工具，我认为它是一个很好的例子，说明AI如何帮助开发人员进行琐碎的测试工作，而不做任何出人意料的事情。当你构建测试框架时，你需要设置和拆除方法，以及支持函数，这意味着你可能无法直接将生成的测试放入代码中进行更改。但从我自己的测试来看，我建议尝试使用 CodiumAI，看看它是否可以成为你工作中的一部分。不管怎样，先给它来一次测试运行吧。
