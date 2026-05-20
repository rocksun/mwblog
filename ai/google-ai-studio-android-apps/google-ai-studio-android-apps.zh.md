Apple 可能并不[看好氛围编程](https://www.theinformation.com/articles/apple-cracks-vibe-coding-apps)，但谷歌正在全力投入。周二，谷歌[宣布](https://android-developers.googleblog.com/2026/05/build-android-apps-google-ai-studio.html)任何人现在都可以使用 [Google AI Studio](https://aistudio.google.com/apps?features=build_android_app) 仅通过几个提示词来构建基于 Kotlin 的原生 Android 应用。为了测试结果，用户可以将应用安装在自己的设备上并与他人分享进行测试，或者将其导入 Android Studio 以完善细节并为更广泛的发布做好准备。

正如谷歌在公告中所指出的，AI 已经让构建基于 Web 的应用程序变得几乎易如反掌（尽管在生产环境中运行它们是另一个问题）。然而，由于每个人都在 *localhost:3001* 上的浏览器中运行他们的 MVP，移动端开发在某种程度上被边缘化了。虽然谷歌已经在 Android Studio 中支持 Gemini 进行移动应用的氛围编程（并且从今天开始，也几乎支持任何流行的 LLM），但对于许多非开发人员来说，在那里起步无疑是一个障碍。

> “现在，你可以兼得两者的优点：基于提示词界面的便捷性与 Android SDK 的强大功能相结合，全都在你的浏览器中完成，无需安装。”

“现在，你可以兼得两者的优点：基于提示词界面的便捷性与 Android SDK 的强大功能相结合，全都在你的浏览器中完成，无需安装，”谷歌写道。

该公司指出，在 AI Studio（谷歌用于测试新模型和原型设计的 Web 工具）中构建 Android 应用所使用的技术，与在 Android Studio 中使用 Gemini 构建应用的技术相同。这些应用将使用 Kotlin 编写，并采用谷歌的 Jetpack Compose，这是目前构建 Android 应用的标准。

> 这真正实现的是……能够使用移动设备上的所有功能，包括内置传感器、GPS、蓝牙和 NFC。

不过，这真正实现的是能够使用移动设备上的所有功能，包括内置传感器、GPS、蓝牙和 NFC。谷歌的示例展示了这在 Pixel Watch（毕竟它们也是 Android 设备）上如何运作：构建一个模仿小型飞机上的航空电子面板，利用来自 GPS、陀螺仪和其他传感器的数据——尽管谷歌的提示词要求显示空速指示器，但这是手表永远无法获知的（不过地速对于此用途也足够了）。

当然，谷歌还指出，你可以将 Gemini 集成到应用中，为其带来 AI 能力。

AI Studio 现在带有一个内置的 Android 模拟器用于预览应用，但真正的测试是它在实际设备上的运行情况。为此，用户只需将他们的 Android 手机插入运行 AI Studio 的机器，集成的 Android Debug Bridge (ADB) 就会接管工作。

为了在 Android Studio 中继续构建应用，谷歌将允许开发人员将代码下载为 zip 文件。

这里特别有趣的是，谷歌还建立了一个与 Google Play Console 的直接连接，因此用户可以直接将应用上传到 Google Play 进行测试和分享。一个注意事项是你需要一个 [Google Play 开发者账号](https://play.google.com/console/u/0/signup)，这需要支付 25 美元的一次性注册费。“AI Studio 将自动创建你的应用记录，打包 bundle，并将其上传到 Google Play 管理中心内部测试轨道。”

很快，你还将能够直接从 AI Studio 与朋友和家人分享这个应用。

路线图中还包括与 Firebase 的集成，Firebase 是谷歌的后端平台，用于为移动应用添加数据库、身份验证等功能。