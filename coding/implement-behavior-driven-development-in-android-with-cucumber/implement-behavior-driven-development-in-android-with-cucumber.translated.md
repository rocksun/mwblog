# 使用 Cucumber 在 Android 中实现行为驱动开发

![Implement Behavior-Driven Development in Android With Cucumber 的特色图片](https://cdn.thenewstack.io/media/2024/11/2d34c959-android-cucumber-bdd-1024x576.jpg)

软件开发涉及流程和人员。人员包括技术和非技术利益相关者，但由于流程主要是技术性的，因此它会在技术和非技术利益相关者之间造成很大的差距。

弥合这一差距需要一种协作方法，该方法使用自然语言来鼓励技术和非技术利益相关者之间的沟通和协作。这正是 [行为驱动开发 (BDD)](https://thenewstack.io/two-ways-to-get-started-with-behavior-driven-design-bdd/) 的目标：在开发人员、测试人员和业务利益相关者之间达成理解。

作为一名软件工程师，我一直在使用最流行的工具之一 [Cucumber](https://cucumber.io/) 来实现 BDD。Cucumber 通过协作执行规范来帮助业务和技术团队协作。BDD 规范还兼作自动化测试。使用 Gherkin 框架，这些规范是协作编写的，[使团队](https://thenewstack.io/entrepreneurship-for-engineers-why-team-alignment-matters/) 与系统的实时文档保持一致。

在本文中，我将解释将 Cucumber 测试集成到 [Android 应用程序](https://roadmap.sh/android) 中的五个简单步骤。

## 为什么将 Cucumber 用于 UI 测试

- 它支持各种 [编程语言](https://thenewstack.io/programming-languages/)，包括所有 Java 虚拟机 (JVM) 语言。
- 它与 Espresso 框架无缝集成，用于用户界面 (UI) 测试。
- 它使任何人都可以使用任何口语编写所需行为的纯文本描述，并使用这些描述运行自动化测试。它的纯语言解析器 Gherkin 促进了这一点，因为它以客户、利益相关者、经理、开发人员、质量保证 (QA) 测试人员等可以理解的清晰且合乎逻辑的语言指定了预期的软件行为。
- 它提供了有关应用程序的出色文档。
- 它可以使用 BDD 运行自动验收测试。

## 使用 Cucumber 设置 Android Studio 进行测试

让我们深入了解如何使用 Cucumber Tests 设置 Android Studio。

### 先决条件

在开始之前，请确保已安装 [Android Studio](https://developer.android.com/studio) 集成开发环境 (IDE)。

您还可以考虑从 Android Studio 市场安装以下插件：

- **: 此 Finanteq 插件支持使用 Kotlin 编写的步骤定义的 Cucumber。它允许直接从 IDE 运行 Cucumber 场景作为 Android** [Cucumber for Kotlin and Android](https://plugins.jetbrains.com/plugin/22107-cucumber-for-kotlin-and-android) [已编制的测试](https://developer.android.com/training/testing/instrumented-tests)。
- **: 这些插件增加了对 Cucumber 测试工具使用的 Gherkin 语言的支持，并为步骤定义提供编码帮助。** [Gherkin](https://plugins.jetbrains.com/plugin/9164-gherkin)和 [Cucumber for Java](https://plugins.jetbrains.com/plugin/7212-cucumber-for-java)由 JetBrains 提供

### 1. 创建带有依赖项的 Android Studio 项目

在 IDE 中创建一个新的 Android Studio 项目，或使用现有项目。接下来，添加 Cucumber 依赖项。

在 app 级模块中
build.gradle 文件中，添加以下依赖项：

### 2. 创建您的 Instrumentation Runner

在
app/src/androidTest/java/com/your/app/ 中，创建一个名为
CucumberTestInstrumentation.java 的自定义 Instrumentation Runner。将此类添加到
build.gradle 中的
android >
defaultConfig 下：

您已成功为 Cucumber 设置 Android Studio，因此现在可以继续进行激动人心的部分。

**3. **Given、When、And 和 Then

Gherkin 是一种特定于领域的语言，它使用非技术术语逐步描述功能的实现。它使用关键字
Given、
When、
And 和
Then 来解释步骤。这些步骤可以用任何人类语言编写，例如英语、阿拉伯语或卢奥语。

以下是我将在此项目中使用的用英语编写的 Gherkin 特性场景示例：

在
app/src/androidTest/assets 中创建一个
assets 目录，并添加一个名为
features 的文件夹。您将在其中添加包含用英语编写的上述步骤定义的功能文件。

添加一个名为
login.feature 的新
.feature 文件，并添加上述功能步骤。

### 4. 使用 Espresso 框架实现场景步骤

在
app/src/androidTest/java/com/your/app/ 中，创建一个名为
LoginSteps 的 Kotlin 类。您将在其中编写测试来实现
login.feature 中的步骤。

以下是步骤实现的代码片段：

### 5. 提供 Cucumber 选项
[运行测试](https://thenewstack.io/who-should-run-tests-on-the-future-of-qa/)时，您必须提供包含步骤定义的包，并将它们粘贴到步骤中。

在
`app/src/androidTest/java/com/your/app` 中，创建一个名为
`test` 的文件夹，并添加一个新的 Kotlin 类。

最后，您可以运行测试，但首先，确认您的项目结构如下所示：

## 运行测试

要运行测试：

- 打开
  **编辑配置**。
- 单击
  左面板上的 **+**，然后选择
  Android 仪器化测试。
- 编写名称以匹配功能的名称，以便于记忆。在这种情况下，即
  客户登录的能力。然后单击
  **运行**或 **确定**以稍后从 IDE 工具栏运行或调试它。

以下是上述实现的结果。

## 结论

弥合技术和非技术利益相关者之间的差距对于有效的软件开发至关重要。行为驱动开发促进了自然语言中的协作和沟通。

Cucumber 等工具可帮助使用可执行规范作为自动化测试来实现 BDD，从而使团队能够创建清晰、共享的文档。将 Cucumber 集成到您的 Android 应用程序开发中可以增强团队协调并简化开发。

有关更多见解，请访问我的
[Hechio BDD](https://github.com/Hechio/HechioBDD) 参考项目或 [cucumber/cucumber-android](https://github.com/cucumber/cucumber-android) 项目，该项目为 Cucumber-JVM 提供 Android 支持。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)