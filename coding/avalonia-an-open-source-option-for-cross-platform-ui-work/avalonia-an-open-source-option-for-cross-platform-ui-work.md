
<!--
title: Avalonia：一个开源的跨平台UI选项
cover: https://cdn.thenewstack.io/media/2025/01/05f20762-ahmet-kurt-nvaovwz7-s8-unsplashb.jpg
-->

Avalonia 是一个用于跨平台 UI 开发的开源框架。它通常用于构建可在各种设备上运行的 .NET 应用程序。

> 译自 [Avalonia: An Open Source Option for Cross-Platform UI Work](https://thenewstack.io/avalonia-an-open-source-option-for-cross-platform-ui-work/)，作者 David Eastman。

.NET 的问题一直是微软对非 Windows 系统的支持有些迟缓。要找到一个使用 C# 但可以在 MacBook 上运行的 UI 库比预想的要难。一个解决方案是 [Avalonia](https://avaloniaui.net/)，它可以帮助你“使用 .NET 为每个设备构建应用程序”——它确实填补了开源跨平台框架的空白。此外，研究它还可以磨练你的框架设计技能。

## 开始

让我们[开始使用 Avalonia](https://docs.avaloniaui.net/docs/get-started/test-drive/introduction) 来编写一些简单的代码，同时了解一下它的架构。我假设你已经安装了 Visual Studio Code 和 .NET。我在之前的[文章](https://thenewstack.io/duck-db-query-processing-is-king/)中介绍过如何使用 VS Code；它的灵活性使其非常适合用于不同的项目（Avalonia 本身实际上推荐使用 JetBrains 的 .NET IDE，Rider）。

我们将在命令行中使用 dotnet，这将加快创建简单项目的效率。首先，我们安装 Avalonia 模板：

![](https://cdn.thenewstack.io/media/2025/01/ab1ebe20-image-1024x270.png)

在一个新的项目目录中，我们使用 MVVM 模板，该模板也适用于 MacOS：

![](https://cdn.thenewstack.io/media/2025/01/a9243a92-image-1-1024x316.png)

然后像往常一样，我们在文件夹中打开 Visual Studio Code：

![](https://cdn.thenewstack.io/media/2025/01/b6f4547f-image-2.png)

搜索 Avalonia 扩展。你肯定想要第一个：

![](https://cdn.thenewstack.io/media/2025/01/c9b5074e-image-3.png)

如果我们选择 Program.cs 文件并点击箭头“运行与此文件关联的程序”，Avalonia 将立即构建一个窗口：

![](https://cdn.thenewstack.io/media/2025/01/31b9dbc9-image-4-1024x465.png)

很好。现在让我们看看基础知识，然后做一些更有趣的事情。

如果你熟悉**Windows Presentation Foundation**(或 WPF，我乐意假设你对此一无所知)，那么你一定见过**可扩展应用程序标记语言**(XAML)，而 Avalonia 使用它自己的品牌“axaml”文件扩展名。你还会注意到它附加了 C# 扩展名来标记“代码隐藏”文件。所有这些都有效，即使有点混乱。是的，它是 XML。

值得庆幸的是，有一些有趣的文件。窗口在“MainWindow.axaml”中定义，你可以看到定义的标题：

![](https://cdn.thenewstack.io/media/2025/01/221d551a-image-5-1024x356.png)

唯一其他有趣的是 TextBlock 定义：

```xml
<TextBlock Text="{Binding Greeting}" HorizontalAlignment="Center" VerticalAlignment="Center"/>
```

除了像我们看到的那样将自身定位在屏幕中央之外，它还向我们介绍了数据绑定，这可能比它应该的要棘手一些。显然，我们将发现术语 Greeting 与一个变量绑定，但在哪里？

如果我们查看一个样板文件“App.axaml.cs”，我们会看到一个名为**DataContext**的东西，它在启动时被设置：

```csharp
...desktop.MainWindow = new MainWindow { DataContext = new MainWindowViewModel(), };...
```

这表明当框架开始绑定时，它将使用这个新的模型类。如果我们查看“MainWindowViewModel.cs”，我们会发现大致是我们所期望的：

```csharp
namespace avaloniaui.ViewModels;
public partial class MainWindowViewModel : ViewModelBase {
    public string Greeting { get; } = "Welcome to Avalonia!";
}
```

因此，TextBlock 已绑定到类变量。IDE 主要在构建后帮助协商这一点。

所以让我们来看一些困难的部分，并了解一些 UI。我将构建一个列表框，允许你选择一个简单的类别项并用示例填充另一个列表。因此，我们将看到一些 UI 设计并处理一些事件。

回到 MainWindow.axaml 文件，我们将单独的 TextBlock 替换为此：

```xml
<StackPanel Orientation="Horizontal">
  <TextBlock Text="{Binding Greeting}" FontSize="20" FontWeight="Bold" Margin="20 10"/>
  <StackPanel Margin="20 25">
    <TextBlock Margin="0 5" Background="LightBlue" DockPanel.Dock="Top">Choose a category</TextBlock>
    <ListBox x:Name="category" SelectionChanged="CategoryChanged" Margin="1" SelectionMode="Single,AlwaysSelected">
      <ListBox.ItemTemplate>
        <DataTemplate>
          <TextBlock Text="{Binding}"/>
        </DataTemplate>
      </ListBox.ItemTemplate>
    </ListBox>
  </StackPanel>
  <StackPanel Margin="20 25">
    <TextBlock Margin="0 5" Background="LightBlue" DockPanel.Dock="Top">Examples</TextBlock>
    <ListBox x:Name="resultlist">
      <ListBox.ItemTemplate>
        <DataTemplate>
          <TextBlock Text="{Binding}"/>
        </DataTemplate>
      </ListBox.ItemTemplate>
    </ListBox>
  </StackPanel>
</StackPanel>
```

就是这样。仅查看标签，你可以看到我们使用**StackPanel**作为整体容器，内部有两个 StackPanel——因为我们将外部 StackPanel 定义为水平方向，所以内部 StackPanel 将并排放置。我们在两个堆栈中定义一个 ListBox。一个行为差异是第一个的 SelectionMode 强制始终选择某些内容。

从数据角度来看，我们把第一个列表框命名为“category”，第二个命名为“resultlist”，这在后面会用到。你可以看到每个堆栈中的TextBlock都有一个绑定。所以我们会把我们自己的字符串放在里面。当然，现在我们还没有数据。

事件方面，我们在第一个堆栈中检测“SelectionChanged”。我们需要对此做出响应。事实上，如果我们尝试运行它，Avalonia 会提示我们“无法为 SelectionChanged 属性找到合适的 setter 或 adder”。

所以让我们尝试修复事件。在`MainWindow`类中，我们添加以下方法：

```csharp
using System;
...
public void CategoryChanged(object source, SelectionChangedEventArgs args) {
    if (source is ListBox listBox) {
        Console.WriteLine($"Category changed to {listBox.SelectedItem}");
    }
}
```

现在我们可以再次运行框架，甚至可以看到 Stack 列的文本标题。

![](https://cdn.thenewstack.io/media/2025/01/21bf4528-image-6-1024x204.png)

让我们尝试添加一些数据。我们实际上可以直接在`MainWindow`类中操作。我们将添加一些数据，并用它来填充第一个ListBox，并将其作为`ItemSource`用于category ListBox：

```csharp
using System.Collections.Generic;
...
private Dictionary<string, List<string>> catgeoryDict = new Dictionary<string, List<string>>() {
    {"Trees", new List<string>(){"Larch", "Oak", "Pine", "Willow"}},
    {"Birds", new List<string>(){"Eagle", "Hawk", "Owl", "Raven"}},
    {"Mammals", new List<string>(){ "Bear", "Deer", "Fox", "Wolf"}},
    {"Snakes", new List<string>(){"Cobra", "Python", "Rattlesnake", "Viper"}},
    {"Insects", new List<string>(){"Ant", "Bee", "Fly", "Wasp"}}
};

public MainWindow(){
    InitializeComponent();
    category.ItemsSource = new List<string>(catgeoryDict.Keys);
}
```

这给了我们一个不错的 category ListBox。所以我们完成了一半。

![](https://cdn.thenewstack.io/media/2025/01/562b5b31-image-7-1024x524.png)

现在，我们只需要在用户点击选择时响应类别更改，通过从我们的数据中填充正确的列表来显示示例。我们只需在事件响应方法中添加一行：

```csharp
public void CategoryChanged(object source, SelectionChangedEventArgs args){
    if (source is ListBox listBox) {
        Console.WriteLine($"Category changed to {listBox.SelectedItem}");
        resultlist.ItemsSource = catgeoryDict[(string)listBox.SelectedItem].ToList();
    }
}
```

由于 SelectedItem 在我们的例子中是一个字符串，我们可以直接将其用作 category 字典的索引来查找示例。现在我们完成了。我们可以选择任何类别并将结果放入下一个列表框：

![](https://cdn.thenewstack.io/media/2025/01/025e67a5-image-8-1024x475.png)

## 结论

这并不太痛苦，但任何进一步的操作都需要我们正确使用 ViewModel。我尝试使用 DataGrid，这是一个更强大的组件来显示数据，但这要棘手得多。

为简洁起见，即使对于这个简单的例子，也有很多东西没有解释——这感觉像是来自其他地方相当多的设计包袱。尽管如此，它仍然成功地实现了其作为跨平台 UI 工作的开源选项的目的。
