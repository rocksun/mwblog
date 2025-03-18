
<!--
title: Roo Code快速入门
cover: 
summary:
-->

前一段时间试用了 [WindSurf](https://windsurf.ai) 和 [Trae](https://trae.ai)，充分体验了指挥式编程的乐趣。[WindSurf](https://windsurf.ai) 看起来更加的完善，但是当我想要大展拳脚时，免费的额度已经用完了。于是想便转向 Trae，正好我有个 AWS 上部署资源的任务，于是就用 Trae 帮我来编写 Pulumi 代码。效果不错，虽然不时有一些小错误，但是比我自己写要快太多了，这个后面可以详细讲讲。不过，对于很多程序员来讲，追求的是更自由地做事方式，于是我决定开始尝试 [Roo Code](https://marketplace.visualstudio.com/items?itemName=rooveterinaryinc.roo-cline)。

## 安装

打开 VSCode，按下 Ctrl+Shift+X ，在搜索框输入 Roo Code，看到 Roo Code，点击 Install 即可。

安装完成后，VSCode 的左侧边栏就会出现一个小火箭图标，点击就看到了  Roo Code 的界面。此时，会要求你配置一个 Provider。

## 配置一个 provider

也就是配置一个大预言模型的 API。Roo Code 是推荐 Claude 3.7 Sonnet，但对于我来说，虽然 Claude 非常的棒，我还是想先试试免费的，你还是我们的 Gemini。

到 [Gemini AI Studio](https://ai.google.dev/) 注册一个账号，创建一个 API key ，然后到 Roo Code 的配置界面录入，然后选择 gemini-2.0.flash-001 作为模型。点击 Save 保存。

当然，使用 Gemini 还有个障碍还是网络，需要让 VSCode 走代理。很遗憾，Roo Code 应该是不支持通过环境变量或 VSCode 配置设置代理，所以我设置了个 VPN 代理。

## 第一个尝试

我想，这个 Roo Code 应该可以帮助我编写这篇文章，这也是我目前使用 VSCode 最多的地方，于是在 Roo Code 的聊天界面，选择 Code 模式，然后输入：

```
帮我把文章中出现的工具加上链接
...
```

然后我的 Markdown 文件中的：

```
前一段时间试用了 WindSurf 和 Trae
```

就变成了

```
前一段时间试用了 [WindSurf](https://windsurf.ai) 和 [Trae](https://trae.ai)
...
```

很不错，给的链接很准确。

## 进一步优化

