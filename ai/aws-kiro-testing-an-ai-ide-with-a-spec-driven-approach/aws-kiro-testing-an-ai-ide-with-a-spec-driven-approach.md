
<!--
title: AWS Kiro：用规格驱动方法测试 AI IDE
cover: https://cdn.thenewstack.io/media/2025/09/09235ce3-tandem-x-visuals-fzooxr2auvi-unsplashb.jpg
summary: 本文介绍了AWS发布的Kiro，它侧重于编写规范而非提示，旨在将开发分解为用户故事、技术设计和可跟踪的任务。文章详细描述了Kiro的工作流程，包括需求生成、设计阶段和任务执行，并提出了对UI和团队协作的改进建议。总的来说，作者认为Kiro的方法强大，AWS值得称赞。
-->

本文介绍了AWS发布的Kiro，它侧重于编写规范而非提示，旨在将开发分解为用户故事、技术设计和可跟踪的任务。文章详细描述了Kiro的工作流程，包括需求生成、设计阶段和任务执行，并提出了对UI和团队协作的改进建议。总的来说，作者认为Kiro的方法强大，AWS值得称赞。

> 译自：[AWS Kiro: Testing an AI IDE with a Spec-Driven Approach](https://thenewstack.io/aws-kiro-testing-an-ai-ide-with-a-spec-driven-approach/)
> 
> 作者：David Eastman

7月，[Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention)发布了 Kiro，这是其对 Windsurf 和 Cursor 的回应 —— 但侧重于编写规范而非提示。然而，我发现，在一大批开发者涌入查看后，对它的访问受到了限制。几周前我才从等待列表中出来，所以现在是时候深入了解一下了。

通过 [Google](https://cloud.google.com/?utm_content=inline+mention) 登录后，您应该在 Kiro 应用程序上看到这个屏幕：

[![](https://cdn.thenewstack.io/media/2025/09/875b3758-image-1024x921.png)](https://cdn.thenewstack.io/media/2025/09/875b3758-image-1024x921.png)

所以输入您的代码，您应该就能进入了。

显然，至少有 [六个主要的 IDE 产品](https://visualstudiomagazine.com/articles/2025/07/21/forked-again-awss-kiro-latest-ai-assistant-based-on-vs-code.aspx) 是基于 Visual Code 的分支；我知道 [Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/) 和 [Windsurf](https://thenewstack.io/windsurf-an-agentic-ide-that-thinks-and-codes-with-you/)。现在还有 Kiro。

Kiro 被放置在您的路径中，因此您可以从 shell 运行它。它打开后看起来（毫不奇怪）与 Visual Code 相似：

[![](https://cdn.thenewstack.io/media/2025/09/d076719d-image-1-1024x766.png)](https://cdn.thenewstack.io/media/2025/09/d076719d-image-1-1024x766.png)

如您所见，它设置为 Claude Sonnet 4。我将忽略“氛围 (Vibe)”选项，直接切换到“规范 (Spec)”设计路径。

## 什么是规范开发？

Kiro 的规范驱动工作流将开发分解为三个不同的阶段：**生成具有详细验收标准的用户故事**，**创建技术设计**，以及将工作分解为一系列**可跟踪的实现任务**。

这些工件应该是具有功能性业务用例的可组合文档，并且是 Kiro 世界中的一等公民。显然，这比仅仅用大型语言模型玩扑克骰子要正式得多。大多数遵循敏捷的团队应该对这个提议的过程没有问题，即使您的实际工作流程有所不同。

我将在我最近测试过的其他一些 [agentic 编码产品](https://thenewstack.io/developer-walk-through-of-auggie-cli-an-agentic-terminal-app/) 上测试 Kiro 的同一个 Rails 项目。它是我简单的游戏开发 MVC 应用程序，可以帮助我设计对话。

## 从氛围 (Vibe) 到规范 (Spec)

将我的代码库作为文件夹加载后，我可以通过描述我希望它处理的项目来启动 Kiro。在这种情况下，我需要一个单独的实用程序，它只链接到我系统中的一个现有模型：

[![](https://cdn.thenewstack.io/media/2025/09/b5b5c1b1-image-2.png)](https://cdn.thenewstack.io/media/2025/09/b5b5c1b1-image-2.png)

对于我的项目，我希望用户能够对“每日格言 (Thought for the Day)”执行 CRUD 操作（创建、读取、更新、删除），这只是一些文本和与现有角色声音相关联的图像。

在查看项目并隔离出一个相关模型后，提示又回来了：

[![](https://cdn.thenewstack.io/media/2025/09/5ecee2c1-image-3-600x1024.png)](https://cdn.thenewstack.io/media/2025/09/5ecee2c1-image-3-600x1024.png)

让我们看一下第一个文档 requirements.md：

[![](https://cdn.thenewstack.io/media/2025/09/26709886-image-4-1024x279.png)](https://cdn.thenewstack.io/media/2025/09/26709886-image-4-1024x279.png)

这是对常规 CRUD 操作的一个很好的介绍。它假设这些想法是鼓舞人心的，这在游戏的上下文中部分是正确的。它还理解它应该遵循约定，就像所有 Rails 应用程序一样。

让我们向下滚动到第一个用户故事：

[![](https://cdn.thenewstack.io/media/2025/09/8cdd2a17-image-5-1024x586.png)](https://cdn.thenewstack.io/media/2025/09/8cdd2a17-image-5-1024x586.png)

“管理员”的角色不太正确，但这里的相关含义是“可以创建内容”。Kiro 捕捉到了“声音关联”标准，这是与现有声音 MVC 模型的重要连接。它还发现需要文本条目，而不需要图像。这是正确的 —— 作者在创建文本时可能无法访问图像。

总共有六个需求/验收集，涵盖了其他 CRUD 任务和视图。

最后一个面向开发人员的角色，所以我知道它会正确使用 Rails：

[![](https://cdn.thenewstack.io/media/2025/09/05bda1dc-image-6-1024x487.png)](https://cdn.thenewstack.io/media/2025/09/05bda1dc-image-6-1024x487.png)

JSON 端点很重要，因为这就是我将结果数据移动到主游戏中的方式。简而言之，它涵盖了所有基础 —— 主要是在没有任何干预的情况下。

## 设计阶段

[![](https://cdn.thenewstack.io/media/2025/09/64677c1e-image-7.png)](https://cdn.thenewstack.io/media/2025/09/64677c1e-image-7.png)

完成后，我们将被邀请继续前进。

现在 Kiro 查看控制器并查看其他 MVC 模型的代码，因此它知道如何进行。由于我的项目是一个 Rails 应用程序，因此约定已经很强大：

[![](https://cdn.thenewstack.io/media/2025/09/3d3259eb-image-8-1024x772.png)](https://cdn.thenewstack.io/media/2025/09/3d3259eb-image-8-1024x772.png)

从敏捷的角度来看，这通常是开发人员的领域知识，但它是以架构师可以理解的术语编写的。因此，它介于我所说的“用户故事”和“任务”之间。我喜欢它发现了视图中的 Bootstrap 样式。

大约有 170 行设计，所以我只会展示另一个部分。它再次捕获了属性中 Voice 和我的现有模型之间的关系，以及使用 ActiveRecord 获得的自动生成的东西：

[![](https://cdn.thenewstack.io/media/2025/09/4fd11ee2-image-9-1024x315.png)](https://cdn.thenewstack.io/media/2025/09/4fd11ee2-image-9-1024x315.png)

其中包含测试，但由于这是一个不断发展的工具，我会在我们开始任务之前要求从设计中删除测试：

[![](https://cdn.thenewstack.io/media/2025/09/ebdbaa90-image-10.png)](https://cdn.thenewstack.io/media/2025/09/ebdbaa90-image-10.png)

## 开始执行任务

现在我们准备好进入实施阶段：

[![](https://cdn.thenewstack.io/media/2025/09/ba68ae3d-image-11.png)](https://cdn.thenewstack.io/media/2025/09/ba68ae3d-image-11.png)

任务列表的编写既面向 LLM，也面向开发人员：

[![](https://cdn.thenewstack.io/media/2025/09/9af3b7c3-image-12-1024x639.png)](https://cdn.thenewstack.io/media/2025/09/9af3b7c3-image-12-1024x639.png)

但是，所有任务看起来都是正确的 —— 如您所见，它们与需求相关联。尤其关注影响现有模型的任务，如任务三；但它只是想建立额外的关系，这应该只是 voice.rb 模型文件中的一行。

有一些小的“开始任务”按钮，因此很明显，如果团队希望自己完成任务，他们可以使用这些按钮。有些测试任务感觉更适合人类：

[![](https://cdn.thenewstack.io/media/2025/09/91856d91-image-13.png)](https://cdn.thenewstack.io/media/2025/09/91856d91-image-13.png)

然而，这突出了一点重要之处。Kiro 是希望人类团队来完成这些任务，还是希望用户依靠 LLM 来生成代码？

目前，设计倾向于后者，这符合市场预期。但它也标志着前者将如何运作。

## 最终确定

[![](https://cdn.thenewstack.io/media/2025/09/2cb730bd-image-14.png)](https://cdn.thenewstack.io/media/2025/09/2cb730bd-image-14.png)

我不太确定这个阶段的真正用途是什么，但我被建议去按顺序启动任务。

我不会太深入地研究运行任务的结果，因为我们在这里是为了查看规范 —— 我们知道 LLM 可以轻松处理 Rails 模型。但让我们来看一个。第一个任务从迁移文件开始：

[![](https://cdn.thenewstack.io/media/2025/09/b982c14c-image-15.png)](https://cdn.thenewstack.io/media/2025/09/b982c14c-image-15.png)

由于这是 Rails，它有一种定义的方式来生成迁移文件（模型的数据库世界描述），所以我可以查看对于提供的小框来说太长的命令：

`rails generate migration CreateThoughtsForTheDay text:text voice_id:integer image_id:string`

从技术上讲，voice\_id 应该是一个引用，即使它是一个整数。但我会接受这个命令。按照现在的惯例，LLM 会查看它所做的事情并对其进行增强：

[![](https://cdn.thenewstack.io/media/2025/09/8f3a18a7-image-16.png)](https://cdn.thenewstack.io/media/2025/09/8f3a18a7-image-16.png)

生成的迁移仍然没有直接提及引用，但我们现在正在进入与您的 LLM 伴侣进行通常的实现争论的世界。现在是退出游戏的好时机：

```
class CreateThoughtsForTheDay &lt; ActiveRecord::Migration[8.0]
  def change
    create_table :thoughts_for_the_day do |t|
      t.text :text, null: false
      t.integer :voice_id
      t.string :image_id

      t.timestamps
    end

    add_index :thoughts_for_the_day, :voice_id
    add_foreign_key :thoughts_for_the_day, :voices
  end
end
```

## 结论

Kiro 的目标是开发团队，他们可以使用工件来批准或更改工具之外的设计。这是一种不同于“氛围编程 (vibe coding)”的方法，后者始终锁定在环境内部。

我认为工作流程可能需要简化。目前，我可以更改现有需求，整个树都会更新。我担心用户钩子（我没有介绍）引起的依赖循环可能会失控。或者，更准确地说，它在压力下可能会变得脆弱。但现在还处于早期阶段。

目前缺乏 UI 的“块状感” —— 有大量的文本，较少的图标和包含图形。这最初是正确的，因为共享的 markdown 文档是产生的“货币”。

由于它们侵入了团队的工作流程，因此必然需要进行更多用户体验工作，以了解团队真正需要什么，以及他们将接受什么。我感觉团队中的工件维护需要单独的工具。

但总的来说，我认为 Kiro 显示的方法很强大。AWS 应该因支持这款雄心勃勃的产品发布而受到赞扬。它绝对不仅仅有一线希望。