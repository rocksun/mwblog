<!--
title: 需避免的7个Java编码错误
cover: https://cdn.thenewstack.io/media/2024/01/d4bf99ca-java-1024x576.jpg
-->

深入探讨Java项目中最常见的错误，这些错误来自涵盖该语言的600多条规则，同时考虑了质量和安全性。

> 译自 [7 Java Mistakes to Conquer](https://thenewstack.io/seven-java-mistakes-to-conquer/)，作者 Jonathan Vila 是 Sonar 的开发者倡导者。他是 Java 大师和西班牙 JBCNConf 和 DevBcn 会议的共同创始人，巴塞罗那 Java 用户组 (JUG) 的组织者，以及 BarcelonaJUG 的成员。

无可否认，[整洁的代码](https://www.sonarsource.com/solutions/clean-code/)是必不可少的 —— 一致、有意图、可适应和负责任的代码。询问任何开发人员，他们都会同意，在创建项目时，这应该是首要考虑的事项。但是，代码只会像它最薄弱的环节一样好，正如 [SonarLint](https://www.sonarsource.com/products/sonarlint/) 的遥测数据所显示的，在经过分析的大量项目中，仍然存在大量问题。   

即使某些问题看起来微不足道，但当涉及到软件的安全性、性能和维护时，它们可能会对软件产生重大影响。这就是为什么我编制了一份 [Java 项目](https://thenewstack.io/java-usage-keeps-climbing-according-to-new-survey/)中我们发现的最常见错误的清单，涵盖了该语言的 [600 多条规则](https://rules.sonarsource.com/java/?_gl=1*1uy5l9t*_gcl_au*MTEyOTM1MjE3OS4xNzAzNjA5NDE5*_ga*MTkwNzY0MDIyNi4xNjg3ODA1ODQ3*_ga_9JZ0GZ5TC6*MTcwNTU4ODAxNi4yMTMuMS4xNzA1NTk3MjE2LjIuMC4w)，并考虑了质量和安全性。记住这些，你可以更好地为自己创造连续一致、有意图、可适应和负责任的代码 —— 全部以巨大的利益和低劳动强度。

## 一、已注释代码 

已注释的代码只是对其可读性的挑战，因此应该删除以提高清晰度。这消除了读者的不确定性，因为读者很难判断代码是临时注释掉的还是应该直接删除。对此有一个有用的提示: 如果它不适用于提交的功能，请将其删除或取消注释(如果是临时禁用)。

下面是一个例子:

```java
public void println(String x) {
   if (getClass() == PrintStream.class) {
       writeln(String.valueOf(x));
   } else {
       synchronized (this) {
           print(x);
           //newLine();
       }
   }
}
```

好消息是，如果以后[需要注释的代码](https://thenewstack.io/why-your-code-needs-abstraction-layers/)，你可以简单地从版本控制系统中检索出来。

## 二、忽略的“TODO”标记

在源代码中留下这些注释，而源代码可能有很长的寿命，会导致不完整的代码，可能在多个方面影响软件。例如，在团队内进行协作时，一些成员可能不知道哪些功能将包含在最终发布中。这些标记还可能使人看起来似乎可以在以后处理，而不是现在实施这些部分，从而减少未来出现错误的机会。此外，TODO块可能导致未来性能泄漏。

这里有一个名为Apache Camel的项目的实际例子，其中引入了一个几乎十年前的TODO行。

```java
SslHandler sslHandler = configureClientSSLOnDemand();
    if (sslHandler != null) {
         //TODO  must close on SSL exception
         //sslHandler.setCloseOnSSLException(true);
         LOG.debug("Client SSL handler configured and added to the ChannelPipeline: {}", sslHandler);
         addToPipeline("ssl", channelPipeline, sslHandler);
     }
```

为避免这些问题，请不要添加新的待办事项块。相反，在提交最终代码前实现该功能 —— 或将这些任务记录到任务管理器中，以便清楚如何在未来解决它们。

## 三、重复的字符串字面量

重复的字符串会导致在必须更改这些值以适应新条件时出现额外工作或遗漏更改。相反，使用常量来存储字符串字面量。这使重构更容易，并提高了代码库的一致性。 

如何做到这一点的示例:

```java
// Compliant
private static final String ACTION = "action1";

public void run() {
  prepare(ACTION);   
  execute(ACTION);
  release(ACTION);
}
```

## 四、函数的高认知复杂度

更常见的是，我们听说循环复杂度，它测量代码中使用的路径数量，并帮助确定给定代码部分的阅读复杂度。但这个概念无法帮助确定需要比条件语句或循环数量更多考虑的实际可维护性水平。

降低代码复杂性是使重构、修复和演进更容易的关键，因为开发人员花在阅读代码上的时间远远多于编写代码的时间。项目通常很难阅读或理解，这个问题使得难以了解其意图并解决维护和发展。开发人员应该投资于重构具有高认知复杂度的代码，以便代码库在长期内更容易理解和维护。

对于新代码，最好参考复杂性指标，并投入时间将其降低到配置的阈值，该阈值应该足够低。

## 五. 未使用的元素

对于开发人员来说，在编写新功能时，很容易创建最终没有用途的代码元素。这些元素不会导致[运行时错误或测试失败](https://thenewstack.io/beyond-api-security-testing-runtime-protection/)，因此即使它们需要被移除，也可能很难识别。但在最坏的情况下，它们可能迫使我们重新考虑整个代码。

这些未使用的元素降低了代码的可读性，这使得更难准确找出代码的意图，并可能导致对其完成缺乏信心。将它们移除。检查未使用的代码，并删除不再有用的部分，或者考虑它们是否缺少可能使用这些元素的代码。看一下：

```java
public class MyClass {
    private int foo = 42;   //private field not used

    public int compute(int a, int b) { //b argument not used
       int c = 10; //local variable not used
       return a * 42;
    }

  public int run() {
    int value=10; //assignment not used
    value=compute(2, 5);
  }
}
```

## 六. 原始类型

在Java中，不要使用没有类型参数的泛型类型——这会避免在编译过程中进行类型检查和捕获不安全的代码，使一切在运行时可见。相反，使用具体的类型，让那些使用这些变量的用户能够理解真正期望的是什么，并在运行时消除意外。参见下文：

```java
// Compliant solution
List<String> myList;
Set<? extends Number> mySet;
```

## 七、抛出泛型异常

使用泛型异常会阻止调用方法处理不同的系统生成异常和应用程序生成错误。为避免这种情况，创建一个自定义的异常系统，为调用者提供足够的信息，以便他们可以决定如何操作，并具有详细和差异化的缓存列表。

```java
// Compliant
public void fooException(String bar) {  
   if (bar.isEmpty()) {  
    throw new EmpyValueException();     
  }
  if (bar == "jello") {
    throw new InvalidArgumentException();
  }
  System.out.println("This is bar: " + bar);
}
```

## 避免错误导致更好的软件

所有开发人员在编程时都希望最终产出高质量、可靠、可适应和安全的产品。但是，这些看似微小的日常错误很容易阻碍实现这个目标。注意这些问题的发生，并尽最大努力避免它们，将只会为你创造一种干净的代码软件，这种软件可以支持企业的繁荣发展。
