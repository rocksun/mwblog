# Bodhi Linux 提供 Enlightenment 桌面体验

![Bodhi Linux 提供 Enlightenment 桌面体验的特色图片](https://cdn.thenewstack.io/media/2024/12/584b5cf1-bohdihero-1024x783.jpg)

很久以前，我最喜欢的 Linux 桌面是 [Enlightenment](https://www.enlightenment.org/)。它不仅外观独特，而且高度可配置。我记得花了几个小时调整桌面，使其外观和感觉完全符合我的意愿。当我的朋友们看到 Enlightenment 时，他们都想要一个类似的桌面。

如果你想要一个这样的桌面，你必须运行 [Linux](https://thenewstack.io/learning-linux-start-here/)。

在离开 Enlightenment 桌面后，它仍然在我心中占据着特殊的地位，每次看到或使用它时，我都会回到我生命中那个特定的时刻，那时我睁大眼睛，对我在 Linux 桌面上能做的事情印象深刻。

我习惯了 Linux 的灵活性和可靠性，但当我看到任何类似 Enlightenment 桌面的东西时，我仍然忍不住微笑。

[Bodhi Linux](https://www.bodhilinux.com) 就是这种情况。

Bodhi 没有使用 Enlightenment 桌面，而是默认使用 Moksha 桌面，Moksha 基于 Enlightenment。根据 Bodhi 官方网站，Moksha “源自梵文，与 Bodhi 一样，意为‘解放、自由或释放’”。

## Enlightenment

“它是 Enlightenment 17 桌面环境的现代迭代版本。Moksha 引入了多项增强功能，例如许多新功能和两个新模块，集成了来自即将发布的 Enlightenment 版本的错误修复和功能，并消除了 E17 中存在的未完成或故障元素。”

Bodhi Linux 基于 [Ubuntu](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/)，因此您可以获得常用的工具，例如 apt 包管理器。

多年来，我已经多次安装 Bodhi Linux，这个过程与任何 [Linux 发行版](https://thenewstack.io/choosing-a-linux-distribution/) 一样简单。我这次注意到，在安装的早期阶段，下载过程有点停滞，但是一点耐心就能解决问题。下载完成后，安装过程很快完成，我就可以重启并登录了。

## 首先，使用 Bodhi 登录

在我早期使用 Bodhi Linux 的时候，总会有一个“首次使用”欢迎向导，询问一些关于 Moksha 桌面的问题。这种情况不再存在了，我相信这是一个明智的选择。现在 Bodhi 只是将你直接带到桌面上，你就可以开始使用发行版了。

由于我将 Bodhi Linux 作为 [VirtualBox 虚拟机](https://thenewstack.io/deploy-a-virtual-machine-with-oracles-open-source-virtualbox/) 使用，所以我首先要做的是安装 Guest Additions；否则，我无法调整屏幕大小。这并不令人意外，因为 Bodhi 在作为 VirtualBox 虚拟机运行时总是需要这个。

默认桌面具有通常的绿色主题，非常漂亮。当然，Moksha 和 Enlightenment 窗口管理器中都有我最喜欢的功能之一——桌面菜单。

如果您左键单击桌面上任何空白处，将出现一个菜单，您可以在其中访问所有已安装的应用程序和其他条目。我一直觉得这个菜单非常高效，因为我不必总是将光标移动到显示器的左下角。

我在 Moksha 中的下一个最喜欢的功能（也存在于 Enlightenment 和其他一些桌面上）是窗口遮蔽。本质上，窗口遮蔽将应用程序窗口卷到标题栏中，以便您可以更好地组织和访问打开的应用程序（见图 1）。

![图 1：窗口遮蔽是 Moksha 桌面的一个亮点。](./figure1.jpg)

这是多任务处理者的梦想成真。您可以肯定我会抓住任何机会在桌面上使用窗口遮蔽。唯一的问题是 Chromium 浏览器必须配置为“使用系统标题栏和边框”；否则，它是无边框的，遮蔽功能不起作用。

## 预安装的应用程序和 Appcenter

开箱即用，可用的东西不多。有 Leafpad（文本编辑器）、Chromium、Web 浏览器管理器（允许您轻松安装其他浏览器）、PulseAudio 音量控制、Synaptic 包管理器和一些实用程序。

Synaptic 包管理器允许您轻松地从标准存储库安装任何应用程序。它相当老式，但它可以轻松完成工作。

Bodhi Appcenter（见图 2）使用 Chromium 打开一个网站，允许您安装应用程序，例如 LibreOffice。在网站上找到您要安装的应用程序，然后单击关联的“安装”按钮。但是，这时出现了第一个问题。当我尝试从 Appcenter 安装 LibreOffice 时，我收到一个错误，提示它找不到“libreoffice”包。

![图 2：不幸的是，必须通过 Synaptic 安装 LibreOffice。](./figure2.jpg)
其他应用程序在AppCenter中安装得很好，但由于某种原因，LibreOffice失败了。没关系，您可以打开Synaptic，搜索LibreOffice并安装。

## 性能

由于Moksha被认为是一个相当轻量级的桌面，因此它的性能非常好。你会发现Moksha比GNOME、KDE Plasma甚至Cinnamon和MATE都快。启动应用程序，它几乎会立即打开。动画流畅，窗口移动优雅轻松。

我运行了`sudo apt-get dist-upgrade`命令，并对发行版升级的速度印象深刻。五分钟内，所有内容都已升级，我可以重新启动到更新版本的Bodhi。

重新启动后，我很惊喜地发现AppCenter中LibreOffice安装的问题已解决。为此向开发者致敬。更好的是，已经非常出色的性能得到了提升。

我遇到的一个奇怪之处是Bodhi Linux附带的内核。运行`uname -r`命令，我看到安装了内核5.15.0-130。该内核自2021年以来就存在，但支持到2038年，因此它将在很长一段时间内都适用。但是，我猜想，较新的硬件将受益于新的内核。除非您有默认Bodhi内核无法识别的较新硬件，否则我建议坚持使用默认内核，因为它运行良好。

鉴于我对Enlightenment窗口管理器情有独钟，并且之前曾将Bodhi作为我的默认发行版，我可以强烈推荐这款Linux发行版给任何寻找比竞争对手更酷、高度可定制且性能卓越的桌面的人。

如果您对此感兴趣，请立即下载Bodhi Linux的ISO镜像，并将其安装为虚拟机或安装在备用硬件上。您不会后悔的。

[YouTube](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。