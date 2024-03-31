
<!--
title: UI库正在消亡，未来是什么？
cover: https://cdn.thenewstack.io/media/2024/03/83c1de4e-image1a.png
-->

UI 库存在挑战，极大地限制了它们的有效性。让我们探索一个新实体 Bit 组件如何解决这些挑战。

> 译自 [UI Libraries Are Dying: What’s Next?](https://thenewstack.io/ui-libraries-are-dying-whats-next/)，作者 Eden Ella。

UI 库是 UI 组件、样式和实用工具的集合，打包并发布以在应用程序中重复使用。它们有助于维护应用程序内和应用程序之间的连贯性，加快开发速度并使代码更易于维护。

UI 库自有其一系列挑战，极大地限制了它们的有效性。这些挑战源于与代码共享和重用相关的更基本的问题。让我们探讨其中一些挑战，并研究一个新实体，即 [Bit](https://bit.dev/?utm_content=inline+mention) 组件，如何解决这些挑战。

## 什么是 Bit 组件？

[Bit 组件](https://bit.dev/reference/components/the-bit-component)可以被认为是下一代软件包。它的构建设置、[工具](https://bit.dev/docs/getting-started/composing/dev-environments)甚至[版本控制](https://bit.dev/reference/components/version-changes)都封装在组件本身中。Bit 组件托管在 [bit.cloud](https://bit.cloud) 上，按具有不同访问控制的范围分组。这意味着 Bit 组件不绑定到任何 git 存储库。您可以将其[导入](https://bit.dev/reference/workspace/importing-components)（克隆）到您的 [开发环境](https://thenewstack.io/how-to-choose-a-cloud-development-environment/) 中，对其进行修改并将其推回 bit.cloud。

当组件发布时，它们会经历一个[构建过程](https://bit.dev/reference/ci/ripple-ci)，该过程会生成工件。一个重要的工件是组件的软件包。组件可以作为常规 Node 软件包安装，或者如前所述，导入（克隆）到您的项目中，您可以在其中对其进行更新。

例如，要修改组件，我们首先在 bit.cloud 上搜索它：

![](https://cdn.thenewstack.io/media/2024/03/07065669-image2a.png)

我们将运行以下命令将其导入到我们的项目中：

```bash
bit import bitdesign.sparks/actions/button
```

导入的组件现在可用作要修改的源文件和要使用的软件包。Bit 会在每次更改时自动更新软件包。

![](https://cdn.thenewstack.io/media/2024/03/d32c732d-screenshot-2024-03-28-at-9.06.16%E2%80%AFam.png)

一旦我们做出更改，我们就可以创建组件的新版本并将其推回 bit.cloud：

```bash
bit tag --message "use lighter color tokens"
bit export
```

我们的按钮组件现在在 bit.cloud 上提供新版本。我们可以继续维护它，或者我们可以将其从我们的项目中删除，同时只保留软件包以供使用。

![](https://cdn.thenewstack.io/media/2024/03/4a6dc21d-image3a.png)

## 使您的 UI 组件可重用和可移植非常困难

将单个 UI 组件作为软件包共享需要花费太多精力。将组件与项目分离，确保它通用或“足够可重用”，配置其 package.json，记录、设置版本并发布可能很麻烦。

当涉及到表单和全页布局等复杂组件时，这一点更加明显。这些组件通常“隐藏”在存储库中且未共享，迫使其他人从头开始构建它们，这既耗时，又容易出错，而且使代码库更难维护。

正如您将在下一部分中看到的那样，有限的协作也是此问题的一个因素。软件包使用者无法修改和扩展组件以满足新出现的需求，并且通过遵循此迭代过程，您可以使具体组件更通用和可重用。

与此问题密切相关的是创建包含大量组件的“大型库”的常见做法。这是同一问题的另一个症状：将单个组件作为软件包共享并不容易。

![库发布的传统工作流](https://cdn.thenewstack.io/media/2024/03/674bee5c-image4a.png)

*库发布的传统工作流*

## Bit 使得共享单个组件变得简单而轻松

当流程简单时，团队更倾向于[共享组件](https://thenewstack.io/how-to-bridge-the-developer-designer-gap/)，同样，当组件易于查找时，他们也更倾向于重用组件。Bit 使得共享组件变得容易。Bit 组件不需要配置。它们的依赖项会自动检测并智能解析为正确的版本和类型。

![](https://cdn.thenewstack.io/media/2024/03/c5de4ede-image5a.png)

Bit 还会自动生成组件文档，并简化组件预览的渲染。

![](https://cdn.thenewstack.io/media/2024/03/d11e04fd-image6a.png)

如前所述，软件包发布是组件构建管道的一个组成部分。当组件进行版本控制并发布时，其软件包会自动发布到 bit.cloud 的注册表（也可能发布到 [您选择的注册表](https://bit.dev/reference/packages/publishing-components-to-commonjs-registries)），其他用户可以在其中发现并安装它。

![](https://cdn.thenewstack.io/media/2024/03/3c5afca0-image7a.png)

单独打包的组件允许使用者挑选和选择他们需要的组件，并避免无意义的[更新其项目的依赖项](https://thenewstack.io/ai-assisted-dependency-updates-without-breaking-things/)。

![](https://cdn.thenewstack.io/media/2024/03/522a555a-image8.png)

## UI 库限制协作

组件库旨在强制执行 UI/UX 和开发标准的一致性。这是一件好事；但是，如果库不够灵活，无法满足项目的需要，它也可能成为一个挑战。当这种情况发生时，团队被迫绕过库，对其进行分叉并维护自己的版本，或向库维护者建议一个拉取请求 (PR)，并等待其合并和发布。

这通常会导致库采用率低，这违背了最初拥有库的目的。

## Bit 组件促进跨团队协作

由于 Bit 组件是自主的，因此可以在任何地方开发和维护它们。这意味着使用组件的团队也可以对其做出贡献，而无需想出各种解决方法或从一个存储库切换到另一个存储库。

组件可以从任何使用项目立即修改和改进，而维护者可以按照自己的节奏审查和合并更改。

![](https://cdn.thenewstack.io/media/2024/03/53debe66-image9.png)

更改会立即在该项目中生效，并且维护者可以按照自己的节奏进行审查、测试和合并。

## 超越库的未来：完全基于组件的项目

使用 [Bit](https://bit.dev)，传统的独立 UI 库或一般库的概念可能很快就会过时。从“库”到更复杂组件的自然组合可以使用相同的结构和工具来实现，而无需区分“库代码”和“应用程序代码”。

这种向更集成、更灵活的代码重用和包管理方法的转变预示着软件开发的新时代。库和应用程序之间的界限变得模糊，从而导致更高效、更易于维护和协作的开发实践。

随着我们向前发展，重点可能会从使用和贡献独立的 UI 库转向在更动态、相互关联的生态系统中创建和共享 Bit 组件。

这种演变有望使软件开发更具模块化、可扩展性和包容性，为开发人员轻松建立在彼此工作基础上的未来铺平道路，从而带来更快的创新和更强大的应用程序。
