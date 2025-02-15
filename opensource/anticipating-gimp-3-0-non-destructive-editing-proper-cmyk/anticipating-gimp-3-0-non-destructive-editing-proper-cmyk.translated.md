# 期待GIMP 3.0：非破坏性编辑，完善的CMYK支持

![期待GIMP 3.0：非破坏性编辑，完善的CMYK支持](https://cdn.thenewstack.io/media/2024/12/65513765-gimp-1024x715.jpg)

我记不清从什么时候开始使用[GIMP](https://www.gimp.org/)了。对于那些不知道的人来说，GIMP代表GNU图像处理项目，它是Photoshop的开源替代品。

GIMP功能强大，拥有创建和编辑令人惊叹的图像所需的所有工具。多年来，我一直使用GIMP为我和许多其他人创建书籍封面，以及创建/编辑屏幕截图和其他图像相关任务。

GIMP的开发速度往往比较慢。例如，GIMP 2.0是在[20年前发布的](https://thenewstack.io/qa-cockroach-labs-spencer-kimball-on-distributing-sql/)。用计算机的年龄来衡量，GIMP 2.0的发布仿佛发生在恐龙时代。

经过这么多年，3.0版本即将到来，它包含一些早就应该出现的非常不错的功能。

让我们来看看一些应该让任何GIMP用户都期待这个即将发布的版本的功能。

## 非破坏性编辑

如果GIMP 3.0只增加一个新功能，那么非破坏性编辑将是我最想要的功能。非破坏性编辑使得可以编辑图像而不会永久更改原始图像。

想想看。您可以打开一个图像，对其进行大量更改，并立即恢复到原始状态。不再需要一次撤消一个更改，并希望编辑历史记录能够追溯到足够远。相反，非破坏性编辑不会从原始图像中删除任何数据，因此它始终存在且不会降级。

我有很多情况下需要恢复到原始状态，但是我已经进行了如此多的更改，以至于历史记录无法追溯到最初。如果我正在处理复杂的图像，那可能是一个大问题。

非破坏性编辑在图层效果窗口中控制，您会在其中看到一个小小的fx图标。单击该图标以查看所有已更改的图层效果（图1）。

<br>

图1：我的一个书籍封面，如GIMP 3.0中所示，使用了非破坏性编辑。

## 额外的图层功能

对于那些依赖图层的人（比如我），GIMP 3.0添加了新的图层功能，例如自动扩展图层（GIMP会根据最新的更改自动调整图层的尺寸）。还有一个新的图层吸附选项，可以更容易地更精确地对齐图层。如果您曾经需要逐像素对齐图层，您就会明白为什么这个功能很重要。

## 改进的字体处理

如果您查看我电脑上的GIMP，会发现安装了数百种字体。到目前为止，GIMP在字体方面并不是最好的。我多次遇到这种情况；在处理书籍封面时，字体往往无法正确渲染，会出现伪影和/或位图。

值得庆幸的是，在GIMP 3.0中，字体处理已完全重做，因此[字体](https://thenewstack.io/what-developers-need-to-know-about-fonts-and-typography/)方面的问题会少得多。

## 插件

GIMP依赖于插件来扩展其功能集。如果您想要效果，很可能需要添加插件。许多插件都已针对3.0版本进行了更新和调整。例如，GEGL（通用图形库）的插件包括GEGL样式（图2），其中包含几种新的效果，例如非破坏性描边、内发光和斜面。

<br>

图2：GEGL样式的新增内容。

## CMYK支持……终于来了！

GIMP 3.0终于获得了[CMYK支持](https://www.digital-print-solutions.com/cmyk-colors)。不要太兴奋，因为它不是完整的CMYK色彩空间。即便如此，GIMP 3.0也会提供更好的开箱即用的CMYK支持，因此您可以更好地准备打印作品。如果您不确定CMYK是什么，它是一种色彩模型，也称为四色印刷，用于彩色印刷。如果没有CMYK支持，在GIMP中生成的图像并不总是能以准确的色彩打印。

在3.0版本中，用户可以导入CMYK颜色配置文件进行“专色校样”，这意味着可以在RGB色彩空间中工作，但可以在CMYK配置文件中查看图像。对于任何使用GIMP创建打印图像的人来说，这都是非常重要的。

## 没有改变的内容

这可能会让一些用户失望，也可能不会，但GIMP的UI几乎没有变化。如果您喜欢GIMP界面，这会让您松一口气。如果您讨厌GIMP界面，很可能您已经从这个开源图像编辑器转向了其他工具。无论哪种方式，界面上唯一大的变化是一个新的启动画面。我一直都很喜欢GIMP的UI，但是很多用户并不认同这种观点，因此根本不改变UI似乎是一个错失的机会……尤其是在20年之后。

在大多数情况下，GIMP 3.0感觉非常像GIMP 2.0。

## 何时发布？
目前，GIMP 3.0 尚未公布官方发布日期，但预计很快就会发布。我相当有信心会在2025年第一季度看到它发布。如果您迫不及待想在Linux上试用GIMP 3.0，以下是如何操作。

### 在Ubuntu上

如果您使用的是基于Ubuntu的发行版，请使用以下命令添加所需的资源库：

```bash
sudo add-apt-repository ppa:ubuntuhandbook1/gimp-3
```

之后，使用以下命令更新apt：

```bash
sudo apt-get update
```

最后，使用以下命令安装GIMP 3.0：

```bash
sudo apt-get install gimp libgegl-0.4-0t64 gir1.2-gegl-0.4 gir1.2-gimp-3.0 gir1.2-babl-0.1 -y
```

### 使用Flatpak

如果您选择的Linux发行版（例如Fedora）使用Flatpak，您可以使用以下命令安装GIMP 3.0：

```bash
flatpak install --user https://flathub.org/beta-repo/appstream/org.gimp.GIMP.flatpakref
```

注销并重新登录，您将在桌面菜单中看到GIMP 3.0图标。

要随时了解GIMP的最新信息，请务必查看官方的GIMP新闻页面。

[技术发展日新月异，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)