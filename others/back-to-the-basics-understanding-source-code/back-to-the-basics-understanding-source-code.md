
<!--
title: 回归基础：理解源代码
cover: https://cdn.thenewstack.io/media/2024/07/a7636ab3-code.jpg
-->

任何对创建和维护软件感兴趣的人，都应该了解代码的重要性以及编码原则的逻辑和设计模式。

> 译自 [Back to the Basics: Understanding Source Code](https://thenewstack.io/back-to-the-basics-understanding-source-code/)，作者 Robert Curlee。

无论你是在浏览网站、观看电视节目、在你的手机上使用一个程序还是甚至是在你的汽车上打开空调，源代码是所有这些能力背后的驱动力。

开发者使用源代码来描述计算机中电子设备的行为。但编码不再仅仅是程序员的工作。由于计算机几乎是所有现代化设备的核心，编程已经变得更加普遍。对于软件创建和维护的基本原理感兴趣的任何人不仅需要了解代码为何重要，还需要理解编码原理中的逻辑概念和设计模式。

## 什么是源代码？

源代码是编程人员编写的一组逻辑指令，用于创建软件。这些构成算法的指令使用特定编程语言编写，如 JavaScript、HTML、CSS、Python、Java 或 C#。这些指令充当计算机遵循的详细配方，制定执行一系列任务所需的每一项操作。这些任务收集在一个称为程序的文件中，该文件使用人能理解的语言编写。

正如 DNA 承载决定细胞如何生长和运作的指令一样，可以将源代码视为你使用的每件软件的 DNA。代码有助于软件创建、维护和增强。它是我们所有数字工具、应用程序和系统的核心。

## 源代码为什么重要？

无论是计算基本的数学还是运行数十亿笔交易的复杂系统（例如股票交易所），源代码都是我们日常使用的设备和技术中软件的基础。

源代码对于软件维护至关重要，包括修补问题、优化问题，以及以新方式对其进行增强。通过开源项目，软件开发者集合开发应用程序和共享的可重复利用功能库，促进创新并加速技术进步。

编码的一个最关键方面是安全性。识别并解决代码中的漏洞可以防止攻击者利用应用程序。了解代码中哪些构成威胁通常非常困难，也是构建安全稳定应用程序时的一项挑战。

## 源代码的一些常见类型有哪些？

虽然有多种方法对源代码进行分类，但最常见的方法是：

- **开源与专有**：顾名思义，开源代码可供任何人使用或修改。它由社区集体所有，对所有人免费。经常地，开源代码的作者放弃其权利，以便代码可以不受限制地使用。开源运动非常强大，因为它促进了创新，技术进步立即惠及每个人。专有或闭源代码是私有的，只能由所有者使用。拥有专有代码的公司或个人只允许在获得明确许可的情况下对其进行修改或使用。将代码保密是为了保护所有者的知识产权，常常是为了盈利。
- **编译与解释**：代码不仅可以按语言分类，还可以按语言编译成可执行应用程序还是由解释器执行来分类。对于已编译语言，编译器将高级源代码转换为 CPU 可理解的 1 和 0 机器代码指令，并将它们打包到独立应用程序中。然后，计算机可以直接读取和执行该应用程序。另一方面，解释型语言（如 JavaScript）是由解释器在运行时读取并转换为 CPU 指令的。解释型语言允许更大的灵活性并且更容易测试，但与编译后的应用程序相比，性能通常较差。

## 什么是源代码示例？

让我们快速查看一些 JavaScript 和 C 代码示例，了解它们的差异。两个示例都定义一个函数，将两个数字相加到一个变量中，然后打印和返回和。如果你不熟悉这个概念，一个函数是一组可重复的指令，一个程序使用。

**JavaScript**

开发者通常使用 JavaScript 来构建 Web 和服务器应用程序。这里所示的功能采用两个参数，计算参数的总和，并使用内置方法 console.log 显示总和。您会看到 console.log 的参数利用 JavaScript 方便的字符串连接，通过向名为 sum 的变量添加一个静态字符串来实现。

```javascript
function displaySum(a, b) {
    let sum = a + b;
    console.log("The sum is: " + sum);
    return sum;
}
```

**C**

开发人员经常使用 C 语言用于系统软件（运行其他软件的平台）和嵌入式系统。此 C 函数执行与以上 JavaScript 函数相同的操作。但是，它使用 C 标准库函数 printf 输出求和结果。printf 语句中的 %d 是整数求和结果的占位符，演示了 C 对输出进行特定类型格式化的能力。

```c
#include <stdio.h>

int displaySum(int a, int b) {
    int sum = a + b;
    printf("The sum is: %d\n", sum);
    return sum;
}
```

初看之下，这两个函数的语法看起来非常相似，但当你注意的微妙之处越多，你将看到这两种语言有多么不同。

## 什么是源代码工具？

编码工具帮助开发人员创建、管理、分析和改进代码质量，同时帮助他们更有效地工作。许多自动化工具可以检测代码中的问题，这些问题会导致错误、安全漏洞和代码异味。借助这些工具，[开发人员可以从他们的代码中获得最大的价值](https://thenewstack.io/arming-developers-with-the-power-of-clean-code/)。

以下是最常见的编码工具类型：

* **集成开发环境 (IDE)**，例如 VS Code、Visual Studio 和 IntelliJ，对于帮助[开发人员进行软件开发](https://thenewstack.io/10-pitfalls-to-keep-in-mind-with-ai-software-development/) 至关重要。IDE 包括一个专门的文本编辑器，它会在您键入时注释代码，识别代码中的语法或其他问题。它们还与代码库和构建管道集成，以在您开发时管理版本控制。
* **DevOps CI/CD 工具**，例如 GitHub、GitLab、BitBucket 和 Azure DevOps，包括代码库，这些代码库将您的代码存储在一个单一的事实来源中，以便开发团队成员可以轻松访问和共享。此外，存储库跟踪源代码中的更改，因此您可以管理不同的版本并撤消更改。分支和合并功能存在，因此开发人员可以在开发时同时处理代码，而无需担心相互覆盖工作或破坏稳定代码。DevOps 工具包括构建过程的自动化，以便可以快速轻松地发布更改。
* **静态代码分析器**在开发人员工作流程中无缝运行，以检测代码中的问题，这些问题会导致错误、漏洞和技术债务，而无需构建和执行应用程序。这些分析器允许开发人员在应用程序经过测试并发布到生产环境之前，在开发过程的最早阶段捕获编码错误。其他好处包括帮助执行编码标准和最佳实践，减少手动代码审查，并教育开发人员如何正确编码，这有助于提高他们的技能。

源代码工具不仅仅检测问题。它们有助于使开发人员变得更好并提高他们的工作质量，从而导致企业重视的更可靠、更安全的软件。像 [SonarQube、SonarCloud 和 SonarLint](https://www.sonarsource.com/lp/products/all/?utm_medium=referral&utm_source=newstack&utm_campaign=ss-sonar-products24&utm_content=media-tns-sourcecode-240718-&utm_term=&s_category=Organic&s_source=External%20Referral&s_origin=newstack) 这样的工具和解决方案可以提高代码质量，并帮助开发人员从他们最重要的资产中获得最大的价值：源代码。

## 最后的想法

源代码质量可以决定对我们日常生活和工作至关重要的应用程序和系统的成功或失败。作为一名开发人员，您不仅要了解编码概念，还要确保您使用正确的开发和测试工具。通过集成这些基本组件，您将有效地生产高质量的工作，确保您的成功。
