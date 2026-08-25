<!--
title: Anthropic的Playground对阵OpenAI：发布一周的新工具为何能击败六年老将？
cover: https://cdn.thenewstack.io/media/2026/08/1467d3c7-lei-hwang-df6pl3gehrg-unsplash-scaled.jpg
summary: 本文对比测试了Anthropic新推出的Playground与OpenAI的同类工具。测试发现，尽管Anthropic的新工具删减了部分功能，但其在代码导出便捷性和错误提示清晰度上表现更佳，证明了极简工具在实际开发场景中同样具有强大的实用价值。
-->

本文对比测试了Anthropic新推出的Playground与OpenAI的同类工具。测试发现，尽管Anthropic的新工具删减了部分功能，但其在代码导出便捷性和错误提示清晰度上表现更佳，证明了极简工具在实际开发场景中同样具有强大的实用价值。

> 译自：[Anthropic's Playground vs. OpenAI's: The week-old tool beat the six-year incumbent](https://thenewstack.io/anthropic-openai-playground-comparison/)
> 
> 作者：Jessica Wachtel

8月18日，Anthropic对其开发者控制台中的提示词测试工具Workbench进行了更名，替换为Playground。然而，Anthropic所做的不仅仅是更改工具名称。

Anthropic还删除了已保存提示词、版本历史、评估（evals）和团队共享等功能。新工具是无状态的，这意味着它不会记住任何内容，也不会在Anthropic的服务器上存储任何数据。（如果您在Workbench中有任何存储内容，请务必在9月1日前导出旧的Workbench数据。）

Playground对Anthropic来说[可能很新](https://support.claude.com/en/articles/8606378-how-do-i-use-the-playground)，但我们在OpenAI那里已经见过它了。OpenAI的Playground是最早的AI工具之一。它自GPT-3时代就已存在。它于2020年6月推出，比ChatGPT诞生早了整整两年半。

值得注意的是，就在Anthropic推出其更精简的Workbench替代品的那一周，OpenAI宣布将于11月30日关闭其已保存提示词（Prompts）和评估（Evals）平台。两家公司得出了相同的结论：提示词应该存在于代码中，而不是网页控制台中。

> 两家公司得出了相同的结论：提示词应该存在于代码中，而不是网页控制台中。

我想看看较新的Playground在与OpenAI长期使用的Playground对阵时表现如何。Anthropic是推出了一款相当的工具，还是仅仅为了跟上他们“持续发布”的目标而匆忙添加了一个低质量的产品？我将两者都进行了测试以找出答案。

## 测试过程

Playground是开发者在将指令放入实际代码之前测试和优化模型指令的地方。你编写指令、运行它们、观察它们失败、修复它们，然后重复此过程。

在每个工具中，我构建了同一个小程序：一个PR审查机器人。它读取代码变更的片段并以严格的机器可读格式报告：变更的风险程度、触及的文件、单行摘要以及测试是否已更改。两个工具收到了相同的指令和代码变更。

接下来，每方进行两项测试：

* 构建机器人，运行它，然后使用导出功能将其转换为实际代码，并确认代码可以在我的笔记本电脑上运行。
* 强制失败，即现实世界中请求中断的方式，并查看工具是否解释了出了什么问题。

我会在本文底部添加提示词和差异（diff），以防有人想自己运行这些测试。

关于我的测试有两个简短说明：

* Anthropic和OpenAI的playground都不在订阅计划范围内。你需要添加积分才能使用它们。我的Anthropic账户里已经有18美元多，我在OpenAI账户里充值了10美元。
* 我没有测试的一点是Anthropic删减的OpenAI功能，比如已保存提示词、版本历史和评估，因为OpenAI即将在11月淘汰它们。

### 测试一：构建并发布

首先，我测试了Anthropic。我粘贴了我的指令和代码变更，点击运行，第一次尝试就得到了正确答案。机器人读取了差异并返回了我要求的完全内容：低风险评级、触及的三个文件、变更的单行摘要，以及对测试已修改的确认，所有内容均为有效的JSON。模型是claude-sonnet-5。这是默认设置，我没有更改它。响应仅用了1.9秒，使用了102个token，花费0.0029美元。

导出功能的效果比我预期的要好。一个开关可以将整个内容转换为Python代码，且我的指令已经包含在内。我复制了它并在我的终端中运行，它完成了与浏览器版本相同的工作：将差异发送给Claude并打印出JSON审查结果。我不需要对Playground的输出进行任何修改就能让它工作；它按原样运行。

然后我将注意力转向了老牌选手OpenAI。OpenAI的Playground现在被称为Chat，但它用于提示词测试的目的相同。该页面比Anthropic的页面有更多的控件：用于推理和详细程度的设置，以及一个为你编写提示词的按钮。我在测试前注意到的另一件事是，我的积分不足以将模型切换为GPT-5.4-mini。每当我试图更改模型时，我都会被提示添加更多积分才能切换（我充值了10美元）。

结果也如预期：在6.2秒内第一次尝试就得到了正确答案，并且具备Anthropic没有的功能，例如颜色编码格式和模型推理过程视图。测试使用了约2.9k个token，但没有列出成本。我想它太便宜了，以至于对我的10美元没有任何影响。

> OpenAI没有导出我的机器人。它导出了我对话的记录、我的指令、模型之前的回答，甚至是它私有的推理过程（作为一个加密文本块）。

导出功能是OpenAI表现不佳的地方。生成的Python代码运行没有报错，但什么也没打印出来。当我打开文件时，我看到了原因。OpenAI没有导出我的机器人。它导出了我对话的记录、我的指令、模型之前的回答，甚至是它私有的推理过程（作为一个加密文本块）。导出的文件包含了整个来回对话，包括模型的答案。运行它会将所有这些再次发送给模型，包括问题和答案。从模型的角度来看，工作已经完成，所以它没有返回任何新内容。

为了获得一个有效的机器人，我必须在浏览器中删除旧的响应，再次导出，并自己添加一行打印代码。

第一轮测试由Anthropic胜出，因为其复制/粘贴无需修改即可成功。

### 测试二：强制失败

我用每个开发者最终都会遇到的错误测试了两个Playground。你限制模型回答的长度，因为上限控制成本。答案达到上限，在句中被切断，任何期望得到完整答案的程序都会停止工作。我通过限制token配额实现了这一点。

Anthropic准确地在预期的位置截断了答案，就在它下方是一句简单的话。“达到最大token限制 — 请在模型设置中提高‘最大token’以获取更多。”没有任何不清楚的地方。

我无法在OpenAI上运行此测试，因为我找不到限制设置。我浏览了新Chat界面中的每个设置面板、溢出菜单，甚至是旧的API模式（它位于一个警告弹窗后，列出了切换后将失去的功能）。控制此故障的设置在我能找到的任何地方都没有暴露。这并不意味着它不存在，但确实意味着存在潜在的UX问题。这意味着开发者无法使用该工具来了解他们在生产环境中会遇到的最常见故障之一。

第二轮，还是Anthropic胜出。我能运行的测试总是胜过我找不到的设置。

> 新的Playground被简化了，但剩下的部分以你想要的方式工作。

## 我的想法是什么？

我只能根据我今天测试的内容进行评价。这些测试告诉我，Anthropic是一个更好的工具，原因有二：

* 我喜欢完美的复制/粘贴，无需任何编辑。
* 它提供了对token花费的更多控制，我认为这很重要，因为某些迹象表明这些AI成本很快就会变得非常高昂。

所以，不，Anthropic不仅仅是在走过场。新的Playground被简化了，但剩下的部分以你想要的方式工作。

**这是我使用的提示词：**

*你是一个PR审查机器人。你接收一个git diff。请仅以这种确切的JSON格式响应：{“risk”: “low” | “medium” | “high”, “files_touched”: [“path1”, “path2”], “summary”: “一句总结”, “tests_modified”: true | false} 不要输出除JSON以外的任何内容。*

Diff:

*diff –git a/rich/text.py b/rich/text.py*

*index 8a2f3c1..d94b7e2 100644*

*— a/rich/text.py*

*+++ b/rich/text.py*

*@@ -589,6 +589,28 @@ class Text(JupyterMixin):*

*if whitespace_count:*

*self.right_crop(whitespace_count)*

*+    def lstrip(self) -> None:*

*+        “””去除文本开头的空白。”””*

*+        text = self.plain*

*+        whitespace_count = len(text) – len(text.lstrip())*

*+        if whitespace_count:*

*+            self.left_crop(whitespace_count)*

*+*

*+    def strip(self) -> None:*

*+        “””去除文本两端的空白。”””*

*+        self.lstrip()*

*+        self.rstrip()*

*+*

*def set_length(self, new_length: int) -> None:*

*“””设置文本的新长度，需要剪裁或填充。”””*

*length = len(self)*

*diff –git a/rich/table.py b/rich/table.py*

*index 1c8e9a4..f2d1b83 100644*

*— a/rich/table.py*

*+++ b/rich/table.py*

*@@ -412,9 +412,7 @@ class Table(JupyterMixin):*

*def _measure_column(self, console, options, column):*

*–        # 遍历所有单元格以查找宽度*

*–        widths = []*

*–        for cell in self._get_cells(console, column):*

*–            widths.append(console.measure(cell.renderable).maximum)*

*+        widths = [*

*+            console.measure(cell.renderable).maximum*

*+            for cell in self._get_cells(console, column)*

*+        ]*

*return max(widths) if widths else 0*

*diff –git a/tests/test_text.py b/tests/test_text.py*

*index 3e4f2a1..9c8d7b5 100644*

*— a/tests/test_text.py*

*+++ b/tests/test_text.py*

*@@ -201,6 +201,24 @@ def test_rstrip():*

*test = Text(“Hello, World!    “)*

*test.rstrip()*

*assert str(test) == “Hello, World!”*

*+def test_lstrip():*

*+    test = Text(”    Hello, World!”)*

*+    test.lstrip()*

*+    assert str(test) == “Hello, World!”*

*+*

*+def test_strip():*

*+    test = Text(”    Hello, World!    “)*

*+    test.strip()*

*+    assert str(test) == “”*

*+*

*+def test_strip_all_whitespace():*

*+    test = Text(”     “)*

*+    test.strip()*

*+    assert str(test) == “”*