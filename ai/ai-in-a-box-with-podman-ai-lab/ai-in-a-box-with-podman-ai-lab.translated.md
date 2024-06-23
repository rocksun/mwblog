### AI-in-a-Box 与 Podman AI Lab

![AI-in-a-Box 与 Podman AI Lab 的特色图片](https://cdn.thenewstack.io/media/2024/06/12c91cf8-podman-playground-1024x678.jpg)

AI 无处不在。你可以向任何一家公司投石问路，你都会发现一家目前正在以某种形式或功能使用 AI 的公司（https://thenewstack.io/pyconus-simon-willison-on-hacking-llms-for-fun-and-profit/）。

大多数 AI 都通过 Microsoft 等公司来体验。对于一些人来说，这很好。对于另一些人来说，与第三方合作使用这种有争议的技术的想法是不可行的。

幸运的是，你始终可以选择在本地运行 LLM（大型语言模型）。这些“AI-in-a-box”工具是快速了解 AI 用法或为你的员工提供 LLM 的好方法。

一种这样的方法是使用 Podman（https://thenewstack.io/use-podman-to-create-and-work-with-virtual-machines/）和 Podman AI Lab（https://thenewstack.io/red-hat-podman-lab-gets-developers-started-on-genai/）。此选项不仅非常易于部署，还允许你选择要使用的 LLM，并且运行得非常好。

我在 AlmaLinux 虚拟机上部署了 Podman AI Lab（https://podman-desktop.io/extensions/ai-lab），惊讶于它的运行效果。与我尝试过的其他 AI-in-a-box 解决方案相比，Podman AI Lab 的功能要好得多，即使资源最少。说到这里，你需要以下最低配置：

- 4 GB 可用内存
- 4 个 vCPU 内核

一旦你拥有这些（以及支持 Podman 的任何 Linux 发行版的运行版本），你就可以启动并运行它了。需要记住的一件事是，你的 AlmaLinux 版本需要安装桌面环境，否则你将无法运行 Podman Desktop（这是必不可少的）。

让我告诉你如何操作。

## 安装 Podman Desktop

你必须做的第一件事是安装 Podman Desktop。最简单的安装方法是使用 Flatpak。AlmaLinux 预装了 Flatpak 并已准备好使用，因此安装 Podman Desktop 只需发出以下命令：

```
sudo flatpak install flathub io.podman_desktop.PodmanDesktop
```

安装完成后，你应该在桌面菜单中找到 Podman Desktop。单击那个坏小子，让我们安装 AI Lab。

## 安装 Podman AI Lab

Podman Desktop 启动并运行后，是时候安装 Podman AI Lab 扩展了。为此，请单击侧边栏中的扩展图标（拼图图标）。在结果窗口（图 1）中，在搜索栏中输入 Podman AI Lab，然后按 Enter。

- 图 1：Podman Desktop 扩展窗口。

当 Podman AI Lab 列表出现时，单击关联的下载按钮（向下箭头）以安装扩展。当扩展显示绿色指示符时，表示已成功安装。你还会看到侧边栏中出现一个新图标，看起来像 Android 头部的顶部。

## 下载 LLM

现在是下载你的第一个大型语言模型的时候了。为此，请单击侧边栏中的 Podman AI Lab 图标，然后单击目录。在这里，你将看到可用 LLM 的列表。选择一个，然后单击关联的下载按钮（图 2）。

- 图 2：你可以找到几个 LLM 可供选择。

根据你选择的 LLM，下载可能需要一些时间。完成后，你就可以继续下一步了。

## 创建服务

现在你已经下载了 LLM，请单击服务按钮。在结果窗口中，单击新建模型服务，然后单击创建服务（图 3）。

- 图 3：使用 Podman AI Lab 创建你的第一个服务。

两件事：

- 如果你下载了多个 LLM，你可以通过单击 LLM 下拉菜单来选择要与此服务关联的 LLM。
- 除非你有充分的理由不这样做，否则我建议使用服务的默认端口。

该服务部署不需要花费太多时间。完成后，你现在可以启动一个游乐场，在那里你可以开始与你的 LLM 交互。

## 创建游乐场

单击模型下的游乐场。在结果窗口中，你可以给游乐场指定一个特定名称，也可以将游乐场名称字段留空，Podman 将分配一个随机名称。确保选择了正确的模型，然后单击创建游乐场。新的游乐场应该几乎立即可用。

## 使用你的新游乐场

当游乐场准备就绪时，你将在窗口底部看到一个提示（图 4）。

- 图 4：你的新 AI Lab 游乐场已准备好接受你的查询。
我快速测试了 Podman AI 实验室，并输入了 Linux 是什么？几乎立即，AI 实验室就给出了一个有效答案（图 5）。

**图 5：我惊讶于 Playground 的响应速度。**

然后我决定尝试一些更复杂的问题，要求实验室解释量子力学。再一次，我惊喜于它生成答案的速度。鉴于这是在虚拟机上运行的，性能非常出色。

这就是它，另一个可以部署和使用的盒子中的 AI。有了足够的能力，你可以部署一个相当强大的 AI 工具，供个人使用（甚至是小企业）。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。