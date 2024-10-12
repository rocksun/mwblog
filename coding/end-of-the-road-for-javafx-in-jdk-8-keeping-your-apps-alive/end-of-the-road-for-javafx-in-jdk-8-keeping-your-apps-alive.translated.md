# JDK 8 中 JavaFX 的终结：如何让您的应用程序保持活力

![Featued image for: End of the Road for JavaFX in JDK 8: Keeping Your Apps Alive](https://cdn.thenewstack.io/media/2024/10/d3e01363-gravel-1024x576.jpg)

JavaFX 是一套流行的图形和媒体包，它使开发人员能够设计、创建、测试、调试和部署跨不同平台一致运行的富客户端应用程序。从 JDK 11 开始，JavaFX 不再包含在大多数 OpenJDK 发行版中。您可以从 [OpenJFX 网站](https://openjfx.io/) 单独下载它。[OpenJDK](https://github.com/openjdk/jdk) 和 [OpenJFX](https://github.com/openjdk/jfx) 作为 GitHub 上的开源项目发展，并遵循相同的发布节奏，因此两者都已于上个月发布了 [版本 23](https://thenewstack.io/oracle-unveils-java-23-simplicity-meets-enterprise-power/)。

少数 OpenJDK 发行版仍然提供包含 JavaFX 的构建，确保组合的 OpenJDK 和 OpenJFX 完全兼容。

[Oracle](https://developer.oracle.com/?utm_content=inline+mention) 将于明年 3 月结束对 JDK 8 中 JavaFX 的支持，并将停止提供包含 OpenJFX 的 Java 8 构建，如 [Oracle Java SE 支持路线图](https://www.oracle.com/java/technologies/java-se-support-roadmap.html) 中所述。这意味着从 2025 年 4 月起，如果您使用的是 JavaFX，则需要找到替代发行版，如果您想继续接收 [安全更新](https://thenewstack.io/the-hidden-threats-lurking-in-outdated-java/)。这适用于所有使用 JavaFX 工具构建的具有用户界面的桌面应用程序、服务器端图像处理、汽车和飞机中的信息娱乐应用程序、机顶盒等。

缺乏对 JavaFX 的支持带来了几个风险：

- 您的 CI/CD 构建将失败，因为新的 Oracle JDK 8 版本不再支持 JavaFX。
- 您无法修复这些失败的构建，因为 JavaFX 8 不再作为开源项目维护，并且没有单独的下载可用。
- 如果您决定坚持使用包含 JavaFX 的最新发布的 Oracle Java 8 包，您的系统将容易受到 CVE 的攻击，因为不会发布新的版本或安全补丁。对于该版本的 Java 和 JavaFX 中的错误修复也是如此。

您有哪些选择？

当然，每个问题都有多种解决方案。以下是一些需要考虑的选择：

- 您可以停止升级您的 Java 8 系统，并坚持使用包含 JavaFX 的最新发布的 Oracle Java 8。但是，如前所述，这会使您的组织面临安全攻击和风险。
- 将您的代码升级到更新的 Java 版本并使用免费的 JavaFX 运行时 (17+)。这带来了额外的优势，例如性能提升、新的 Java 功能、API 等等。但是，它也带来了许多功能回归风险，您可能需要更改您的
[应用程序代码并审查和测试您的整个代码库](https://thenewstack.io/how-to-test-how-much-memory-your-java-application-uses/)和运行时环境。
- 最简单的解决方案是切换到另一个提供包含 JavaFX 的 OpenJDK 8 构建的 OpenJDK 发行版。它应该支持包含的组件，包括 WebKit、多媒体等等。因此，您只需更换 OpenJDK 兼容的运行时，即可照常使用您的代码和已编译的应用程序。

## 结论

虽然出于多种原因，建议您将应用程序更新到更新的 Java 版本，但我们理解这并不总是可行，或者投资太大。在这种情况下，其他 OpenJDK 发行版可以帮助您在 Java 8 上运行包含 JavaFX 的系统。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等等。
](https://youtube.com/thenewstack?sub_confirmation=1)