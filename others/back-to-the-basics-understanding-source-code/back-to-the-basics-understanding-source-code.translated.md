# Back to Basics: Understanding Source Code

![A featured image about "Back to Basics: Understanding Source Code"](https://cdn.thenewstack.io/media/2024/07/a7636ab3-code-1024x576.jpg)

Whether you're browsing the web, watching a TV show, using an app on your phone, or turning on the air conditioning in your car, source code drives all of these functions.

Developers use source code to describe how computers run electronic devices. But coding is no longer just for programmers. As computers are at the heart of nearly every modern device, programming is becoming increasingly common. Anyone interested in creating and maintaining the foundation of software should understand the importance of code, as well as the logical concepts and design patterns of coding principles.

**What is source code?**

Source code is a set of logical instructions written by programmers to create software. These instructions make up algorithms, which are written in a specific programming language, such as [JavaScript](https://thenewstack.io/rust-growing-fastest-but-javascript-reigns-supreme/), HTML, CSS, [Python](https://thenewstack.io/what-is-python/), [Java](https://thenewstack.io/java-22-making-java-more-attractive-for-ai-apps-workloads/), or C#. These instructions act as a detailed recipe that computers follow, listing every action needed to perform a series of tasks. These tasks are collected in a file called a program, which is written in a language that humans can understand.

Just as DNA carries the instructions that determine how cells grow and function, source code can be thought of as the DNA of every piece of software you use. Code facilitates the creation, maintenance, and enhancement of software. It is the heart of all our digital tools, applications, and systems.

**Why is source code important?**

From calculating basic math to running complex systems that handle billions of transactions, such as stock exchanges, source code is the software foundation of the devices and technologies we use every day.

Source code is essential for software maintenance, from fixing bugs to optimizing and enhancing software in new ways. Through open-source projects, software developers can collaborate to develop applications and shared libraries of reusable functions, fostering innovation and accelerating technological progress.

One of the most critical aspects of coding is security. Identifying and addressing vulnerabilities in code can prevent attackers from exploiting applications. Understanding what constitutes a threat in code is often difficult and is one of the challenges of building secure and stable applications.

**What are some common types of source code?**

While there are many ways to categorize source code, the most common are:

**Open-source vs. proprietary**: As the name suggests, open-source code is available for anyone to use or modify. It is owned by the community and is free for everyone. Typically, the authors of open-source code relinquish their rights to the code so that it can be used without restrictions. The open-source movement is very powerful because it fosters innovation, and technological advancements are immediately disseminated to everyone. Proprietary or closed-source code is private and can only be used by those who own it. Companies or individuals who own proprietary code only allow it to be modified or used with explicit permission. The purpose of keeping code private is to protect the owner's intellectual property, often for profit.

**Compiled vs. interpreted**: Code can be categorized not only by language but also by whether the language is compiled into an executable application or executed by an interpreter. For compiled languages, a compiler translates high-level source code into machine code instructions of 0s and 1s that the CPU understands and packages these instructions into a standalone application. The computer can then read and execute the application directly. Interpreted languages, on the other hand, such as JavaScript, are read and translated into CPU instructions dynamically by an interpreter. Interpreted languages allow for greater flexibility and are easier to test, but performance is typically worse than compiled applications.

**What are some examples of source code?**

Let's quickly look at some examples of JavaScript and C code to see how they differ. Both examples define a function that adds two numbers together into a variable, then prints and returns the sum. If you're unfamiliar with the concept, a function is a set of reusable instructions that a program uses.

**JavaScript**

Developers often use JavaScript to build web and server applications. The function shown here takes two arguments, calculates the sum of the arguments, and displays the sum using the built-in method `console.log`. You'll see that the argument to `console.log` uses JavaScript's convenient string concatenation to add a static string to a variable called `sum`.

```javascript
function addNumbers(a, b) {
  let sum = a + b;
  console.log("The sum is: " + sum);
  return sum;
}
```

**C**

```c
#include <stdio.h>

int addNumbers(int a, int b) {
  int sum = a + b;
  printf("The sum is: %d\n", sum);
  return sum;
}
```

You can see that the C code is more verbose and requires the inclusion of a header file (`stdio.h`) to use the `printf` function. The `printf` function is used to print the sum to the console, and the `%d` format specifier is used to indicate that the `sum` variable should be printed as an integer.

These are just two simple examples of source code, but they illustrate the basic concepts of programming. As you learn more about programming, you'll encounter many different types of source code, each with its own unique syntax and purpose.

**Conclusion**

Source code is the foundation of all software, and understanding it is essential for anyone who wants to work with computers. Whether you're a programmer, a designer, or simply a curious user, learning about source code can help you better understand the world around you.
开发人员经常使用 C 语言来编写系统软件（运行其他软件的平台）和嵌入式系统。此 C 函数执行与上面 JavaScript 函数相同的操作。但是，它使用 C 标准库函数 `printf` 输出总和。`printf` 语句中的 `%d` 是整数总和的占位符，展示了 C 针对输出的特定于类型的格式。

乍一看，这两个函数的语法非常相似，但当你观察细微之处时，你会发现这两种语言的不同之处。

**什么是源代码工具？**
编码工具帮助开发人员创建、管理、分析和改进代码质量，同时帮助他们更有效地工作。许多自动化工具可以检测代码中的问题，这些问题会导致错误、安全漏洞和代码异味。借助这些工具，[开发人员可以从他们的代码中获得最大的价值](https://thenewstack.io/arming-developers-with-the-power-of-clean-code/)。

以下是最常见的编码工具类型：

* **集成开发环境 (IDE)**，例如 VS Code、Visual Studio 和 IntelliJ，对于帮助[开发人员进行软件开发](https://thenewstack.io/10-pitfalls-to-keep-in-mind-with-ai-software-development/) 至关重要。IDE 包括一个专门的文本编辑器，它会在您键入时注释代码，识别代码中的语法或其他问题。它们还与代码库和构建管道集成，以在您开发时管理版本控制。
* **DevOps CI/CD 工具**，例如 GitHub、GitLab、BitBucket 和 Azure DevOps，包括代码库，这些代码库将您的代码存储在一个单一的事实来源中，以便开发团队成员可以轻松访问和共享。此外，存储库跟踪源代码中的更改，因此您可以管理不同的版本并撤消更改。分支和合并功能存在，因此开发人员可以在开发时同时处理代码，而无需担心相互覆盖工作或破坏稳定代码。DevOps 工具包括构建过程的自动化，以便可以快速轻松地发布更改。
* **静态代码分析器**在开发人员工作流程中无缝运行，以检测代码中的问题，这些问题会导致错误、漏洞和技术债务，而无需构建和执行应用程序。这些分析器允许开发人员在应用程序经过测试并发布到生产环境之前，在开发过程的最早阶段捕获编码错误。其他好处包括帮助执行编码标准和最佳实践，减少手动代码审查，并教育开发人员如何正确编码，这有助于提高他们的技能。

源代码工具不仅仅检测问题。它们有助于使开发人员变得更好并提高他们的工作质量，从而导致企业重视的更可靠、更安全的软件。像 [SonarQube、SonarCloud 和 SonarLint](https://www.sonarsource.com/lp/products/all/?utm_medium=referral&utm_source=newstack&utm_campaign=ss-sonar-products24&utm_content=media-tns-sourcecode-240718-&utm_term=&s_category=Organic&s_source=External%20Referral&s_origin=newstack) 这样的工具和解决方案可以提高代码质量，并帮助开发人员从他们最重要的资产中获得最大的价值：源代码。

**最后的想法**
源代码质量可以决定对我们日常生活和工作至关重要的应用程序和系统的成功或失败。作为一名开发人员，您不仅要了解编码概念，还要确保您使用正确的开发和测试工具。通过集成这些基本组件，您将有效地生产高质量的工作，确保您的成功。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等等。
](https://youtube.com/thenewstack?sub_confirmation=1)