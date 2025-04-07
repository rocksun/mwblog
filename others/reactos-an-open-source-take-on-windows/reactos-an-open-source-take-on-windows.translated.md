# ReactOS，Windows 的开源替代方案

![Featued image for: ReactOS, an Open Source Take on Windows](https://cdn.thenewstack.io/media/2025/03/ece24b22-reactoshero-1-1024x652.jpg)

您是否知道有一个开源操作系统被设计为与 Windows 兼容？

这不是一个旨在看起来和感觉像 Microsoft Windows 的 [Linux 发行版](https://thenewstack.io/choosing-a-linux-distribution/)。实际上，视觉上的相似之处仅止于 Windows 的美学。当然，[任何 Linux 发行版](https://thenewstack.io/check-out-debian-the-mother-of-all-linux-distributions/)都可以预装 Wine，这允许用户安装 Windows 应用程序，但这样的操作系统仍然是 Linux。

在继续之前，我认为我很清楚自己在操作系统领域的立场。我是一个 [核心](https://thenewstack.io/author/jack-wallen/) 的 Linux 用户，并且已经使用了几十年。

话虽如此，仍然有很多人希望继续使用 Windows，但不希望在 Windows 10 支持结束后必须购买新 PC。虽然我更愿意推荐 Linux 发行版（因为它更安全、可靠，并且可以在所有类型的硬件上运行），但我知道有些人甚至拒绝考虑使用 Linux。

这就是 [ReactOS](https://reactos.org/) 的用武之地。这个 Windows 的开源替代方案旨在：

- 创建一个免费的 Microsoft Windows 替代品。
- 确保与现有软件（游戏、生产力应用程序和其他依赖 Windows API 的程序）的兼容性。
- 提供安全改进。

ReactOS 的第一个稳定版本于 2011 年发布。2013 年，发布了一个 Beta 版本，其中包括对 64 位系统和硬件加速的改进支持。最后，在 2020 年，该项目达到了技术 Alpha 里程碑，这意味着该团队在稳定性和性能方面取得了重大进展。

我记得第一次测试 ReactOS（那是它首次发布的时候）。虽然我可以看到操作系统想要做什么，但它几乎无法使用。现在？好吧，只能说最新版本真的让我感到惊讶。

使用 ReactOS 时要记住一件事：不要期望任何即使是略微现代的外观。最新版本看起来非常像旧的 Windows XP UI。

它很丑陋。

另一个需要考虑的问题是，ReactOS 以类似于 Linux 的方式处理软件管理。有一个 ReactOS 应用程序管理器，这是一个应用程序商店，您可以在其中安装所需的应用程序。我甚至尝试下载 Opera 浏览器的安装程序，但默认的 Web 浏览器（名为 Internet Explorer，您准备好了吗）不配合。然后我打开应用程序管理器，找到 Opera，安装了它，并准备就绪。

或者我准备好了吗？

即使安装了最新版本的 Opera，仍然存在问题。然后我去安装 Firefox，却发现可用的版本已经过时了。然后我下载了最新的 Firefox 安装程序（来自 mozilla.org），并开始通过 .exe 安装它。

在双击下载的 .exe 文件并完成安装向导后，我安装了最新版本的 Firefox，并且一切都按预期工作。

接下来，我下载了最新版本的 LibreOffice 的安装程序。在下载过程中，我被警告说我的 Firefox 版本已过时，这很奇怪，但随后它也提到了在受支持的平台上安装。

奇怪。

浏览器仍然在运行，因为它下载了 [LibreOffice 文件](https://thenewstack.io/designing-libreoffice-preparing-images-graphics-editors/)，所以我让它继续。

双击 LibreOffice 安装程序，什么也没发生。

该死。

回到应用程序管理器，我找到了一个 LibreOffice 版本（图 1），但它已经过时了（版本 5.4.7.2）。我不会回到这么过时的版本。再次尝试下载最新版本的 LibreOffice，看看我是否可以运行安装程序。

-
图 1：LibreOffice 已安装在 ReactOS 上。

这也是事情真正开始崩溃的时候。我试图将安装程序文件从“下载”移动到“我的文档”（因为我能够在那里运行 Firefox 安装程序），但这导致文件管理器崩溃。所以，我重新启动了，因为（你知道）Windows 通常需要重新启动才能解决神秘的问题。

重新启动后，我再次尝试安装，结果相同。

这里的教训是，如果您想使用 ReactOS，最好的选择是从应用程序管理器安装应用程序，因为除此之外的任何内容都可能无法安装或运行。

## 为什么要费心使用 ReactOS？
现在，您可能已经举起双手说：“何必呢？” 这是一个合理的问题，除了您是Windows的铁杆用户，并且买不起新机器来替换Windows 10，而且Linux不是您的菜之外，我很难想出一个答案。ReactOS可能已经有近15年的历史了，但它仍然感觉像是一个正在进行中的工作；它有缺陷、运行缓慢，并且不支持大量的应用程序。

最后，我能想象到的唯一理由是，有人想加入ReactOS，那就是[加入开发团队](https://reactos.org/contributing/#paid-jobs)来帮助推动操作系统的发展。我想象如果团队能够消除bug，使安装更多（和更新的）应用程序成为可能，并更新UI，他们将掌握一个改变游戏规则的东西。

如果他们要问我，我会建议升级UI，使其看起来更像最新版本的KDE Plasma。我不知道他们是如何开发操作系统的（或者是否有可能），但是将KDE Plasma移植到ReacOS将会产生巨大的影响，因为他们可以创建一个桌面布局，更像是Windows的现代版本。

就目前而言，感觉就像您正在使用一个运行在Wine之上的完整操作系统。

即便如此，我认为ReactOS是一个重要的项目，因为它展示了需求可以激发什么。需要一个与Windows 1:1兼容的开源操作系统，如果它真的实现，那将通过ReactOS来实现。

我不建议任何人将ReactOS作为日常操作系统使用。但是，如果您想看看能做什么，这是一个很棒的项目。如果团队能找到一些新的开发人员来支持这项事业，它可能会掀起波澜，现在是实现这一目标的理想时机。

[技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，观看我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)