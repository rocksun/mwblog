我一直不喜欢“提示工程(prompt engineering)”这个词，它总让我想起用一种花哨的方式来谈论施魔法。现在，这个词已经过时了，“上下文工程(context engineering)”正流行。我们都意识到管理AI代理在其上下文窗口中持有的内容至关重要。

工程化上下文可能意味着不同的事情。我将在这里重点介绍为[XMLUI](https://docs.xmlui.org)升级[MCP服务器](https://github.com/xmlui-org/xmlui-mcp)如何提高其管理代理上下文的能力（披露：我是XMLUI项目的顾问；另请参阅[The New Stack的报道](https://thenewstack.io/make-react-components-with-xmlui-a-visual-basic-for-the-ai-era/)）。

## 使用 xmlui-mcp

*xmlui-mcp*与文档、源代码和示例一起工作。这是一个用于Claude或Cursor等代理的典型配置。

```
"xmlui": {
    "command": "/Users/jonudell/xmlui-mcp/xmlui-mcp",
    "args": [
    "/Users/jonudell/xmlui",
    "/Users/jonudell",
    "xmlui-invoice,xmlui-mastodon"
    ]
},
```

这段代码意味着：

* 启动 xmlui-mcp 二进制文件
* 使用 /Users/jonudell/xmlui 作为 XMLUI 仓库克隆的位置
* 使用 /Users/jonudell 作为示例的根目录
* 在 xmlui-invoice 和 xmlui-mastodon 子文件夹中查找示例

这运作得很好。我从XMLUI开发人员那里听到了关于成功的一次性结果，并且对这个反馈感到高兴：

“我让MCP服务器运行着，刷新了页面，突然之间就有了我所要求的可用UI。我生活在未来。”

真棒！

## 提高期望

尽管受到了鼓励，但我并不满意。当您使用代理和*xmlui-mcp*的组合时，您应该始终被引导到正确的解决方案，该解决方案由源代码、文档、操作指南或工作示例引用支持。如果没有出现解决方案？那是文档中的错误（我们可以修复）或缺少的功能（我们可以添加）。您*绝不*应该被引导到一个没有锚定到事实依据的不正确解决方案。而这种情况经常发生。

我添加了一个名为`xmlui_rules`的提示，其中包含诸如“不要发明任何xmlui语法，只使用你可以在文档和示例应用程序中找到示例的结构，并且始终引用你的来源”之类的指导。现在，我可以简单地说“记住规则”而不是将规则粘贴到聊天中，但我不得不重复这一点。*xmlui-mcp*如何才能在管理上下文和重申规则方面发挥更积极的作用？

首先，xmlui-mcp搜索工具需要变得更擅长模糊搜索。与我的[助手团队](https://thenewstack.io/7-guiding-principles-for-working-with-llms/)（在本例中为ChatGPT、Claude和Cursor）合作，我们提出了一个分阶段的方法：首先查找精确的搜索字符串，然后采取一种宽松的方法，省略常见的停用词，然后采取一种部分匹配的方法，该方法仅需要查询词的子集匹配（例如，找到仅包含四个查询词中的两个的文档，而不是要求所有四个都匹配）。第一个版本使用了一种优先考虑精确度而不是召回率的算法。这似乎太严格了，但是当我提高召回率时，结果被不相关的命中淹没了。如果系统可以帮助代理编排工具和搜索策略的组合，那么这一层中保守的精确度方法并不是一个破坏交易的因素，结果证明。

为了具体说明这一点，请考虑以下测试查询：“How do I create a row of equal width components?”（如何创建一行等宽的组件？）

这是我希望代理找到并报告的URL：[Make a set of equal-width cards](https://docs.xmlui.org/howto/make-a-set-of-equal-width-cards)（制作一组等宽卡片）。该查询对于该结果来说并不完美，但是Cursor达到了我想要的目的地。

[![](https://jonudell.info/newstack/equal-width-components.png)](https://jonudell.info/newstack/equal-width-components.png)

它是如何到达那里的？我要求它解释。

1. 初始搜索策略
我首先搜索“row equal width components layout”，但没有得到匹配。然后我尝试了更具体的术语：
mcp\_xmlui\_xmlui\_search with “HStack row layout components” – 找到了通用的HStack信息
2. 关键发现
在“width 100% equal”的搜索结果中，我找到了这个特定的匹配：
mcp\_xmlui\_xmlui\_search with “width 100% equal” – 这是找到操作指南的关键搜索
文件名本身包含“equal-width-cards”，这正是我需要的！
3. 我如何将等宽组件连接到等宽卡片
这种连接不是一个飞跃，而是搜索结果中的直接匹配。当我搜索“width 100% equal”时，搜索引擎找到了：
– 文件名：make-a-set-of-equal-width-cards.md
– 标题：“Make a set of equal-width cards”
– 操作指南列表：Make a set of equal-width cards，在操作指南索引中
– 搜索过程
4. 这是确切的顺序：
– 首次搜索：“row equal width components layout” → 没有结果
– 第二次搜索：“HStack row layout components” → 找到通用的HStack信息
– 第三次搜索：“width 100% equal” → 找到了操作指南！
第三次搜索是一个突破，因为它找到了专门解决您所要求的操作指南。5. 为什么这行得通
搜索成功是因为：
– 操作指南文件名包含“equal-width-cards”
– 搜索词“equal”与文件名中的“equal-width”匹配
– 搜索词“width”与关于宽度大小的内容匹配
– 操作指南专门介绍了如何创建一行等宽的组件

要了解这是如何工作的，请查看Cursor从*xmlui-mcp*收到的一个响应：

```
Query: "width 100% equal"  (stages=3, hits=50, confidence=high)
Facets: components=12 files (36 matches)  examples=0 files (0 matches)
  howtos=2  source=6 files (12 matches)

docs/public/pages/layout.md:395: When you use a `HStack` child with percentage width, the effective width is calculated from the stack's viewport width.
docs/content/components/IFrame.md:45:       width="100%"
...
xmlui/src/components/AppHeader/AppHeader.module.scss:127:       width: 100%;
xmlui/src/components/AutoComplete/AutoComplete.module.scss:42:     width: 100%;

---
JSON:
{
  "query_plan": [
    {
      "stage": "exact",
      "query": "width 100% equal",
      "hits": 1
    },
    {
      "stage": "relaxed",
      "query": "width 100% equal",
      "hits": 1
    },
    {
      "stage": "partial",
      "query": "width 100% equal",
      "hits": 109
    }
  ],
  "sections": {
    "components": [
      {
        "type": "components",
        "path": "docs/content/components/IFrame.md",
        "line": 45,
        "snippet": "      width=\"100%\" "
      },
      ...
      {
        "type": "components",
        "path": "docs/public/pages/tutorial-09.md",
        "line": 146,
        "snippet": "    \u003cTable width=\"100%\" data=\"{[$props.details]}\"\u003e"
      }
    ],
    "examples": [],
    "howtos": [
      {
        "type": "howtos",
        "path": "docs/public/pages/howto/make-a-set-of-equal-width-cards.md",
        "line": 0,
        "snippet": "[filename match]"
      },
      {
        "type": "howtos",
        "path": "docs/public/pages/howto/make-a-set-of-equal-width-cards.md",
        "line": 1,
        "snippet": "# Make a set of equal-width cards"
      }
    ],
    "source": [
      {
        "type": "source",
        "path": "xmlui/src/components/Accordion/Accordion.module.scss",
        "line": 19,
        "snippet": "    width: 100%;"
      },
      ...
      {
        "type": "source",
        "path": "xmlui/src/components/App/App.module.scss",
        "line": 165,
        "snippet": "          width: calc(100% + (2 * var(--scrollbar-width)));"
      },
  },
  "facets": {
    "components": {
      "files": 12,
      "matches": 36
    },
    "examples": {
      "files": 0,
      "matches": 0
    },
    "howtos": {
      "files": 1,
      "matches": 2
    },
    "source": {
      "files": 6,
      "matches": 12
    }
  },
  "confidence": "high",
  "agent_guidance": {
    "rule_reminders": [
      "🚨 BEFORE RESPONDING: Ask yourself 'Am I about to provide code without a documented working example?' If yes, STOP and acknowledge the limitation instead",
      "🚨 PRIORITY ORDER: 1) Check for documented working examples 2) IF NONE FOUND: Explicitly state this and provide no code 3) ONLY THEN: Provide general documentation URLs (if any exist)",
      "🚨 MANDATORY ACKNOWLEDGMENT: When no documented examples are found, you MUST start your response with: 'I am following the guidance by not providing code examples because no documented working examples were found.'",
      "🔍 SEARCH STRATEGY: Use xmlui_examples and xmlui_search_howto first, then fall back to xmlui_search",
      "📚 PREFER: Examples and howtos over general component documentation",
      "🔄 FALLBACK: If no examples/howtos found, then search general documentation",
      "🔗 MANDATORY: Always include documentation or example URLs in your response",
      "🔗 MANDATORY: Always include documentation URLs in your response - see documentation_urls",
      "📍 REQUIRED: Cite specific sources with clickable links from the search results",
      "✅ VERIFY: You must include at least one URL from documentation_urls in your response",
      "❌ Do not invent syntax - only use documented constructs",
      "📝 Always cite your sources when providing code examples",
      "🔗 Provide specific URLs to documentation sources (see documentation_urls)",
      "📍 Reference file paths and line numbers when available",
      "⚠️ Preview and discuss limitations before providing code"
    ],
    "suggested_approach": "Limited examples found. Cross-reference component documentation with any available examples. Always provide URLs to documentation sources.",
    "url_base": "https://docs.xmlui.org",
    "documentation_urls": [
      {
        "title": "Layout",
        "url": "https://docs.xmlui.org/layout",
        "type": "components"
      },
      ...
      {
        "title": "Make A Set Of Equal Width Cards",
        "url": "https://docs.xmlui.org/howto/make-a-set-of-equal-width-cards",
        "type": "howtos"
      },
      ...
      {
        "title": "Accordion.module",
        "url": "https://docs.xmlui.org#xmlui/src/components/Accordion/Accordion.module.scss:19",
        "type": "source"
      },
    ]
  }
}
```

这些响应以前是未加区分的文件名和代码片段列表。现在，它们描述了结果如何落在不同的存储桶中，这些存储桶表明应该选择哪个工具进行后续搜索。此外，他们还用关于将答案锚定到他们可以引用的文档的指导来敲打代理。

为了万无一失，我还将此添加到Claude和Cursor的基本用户提示中：

Obey the guidance you receive from the xmlui-mcp server.（遵守您从xmlui-mcp服务器收到的指导。）

I will disbelieve any answer for which you cannot cite an URL to documentation or a working example.（我不会相信您无法引用文档或工作示例的URL的任何答案。）

If you don’t find an URL, say so.（如果您找不到URL，请说明。）

If you do find one, cite it.（如果您找到一个，请引用它。）

## 诚实地承认失败

我们不应该只测试快乐路径。这是一个应该失败的查询：“How do I right-align a cell in a table?”（如何在表格中右对齐单元格？）目前还没有办法做到这一点！与原始*xmlui-mcp*一起工作的代理给出了各种无稽之谈的答案。这是Cursor使用新版本的响应方式。

[![](https://jonudell.info/newstack/right-align-cell-in-table.png)](https://jonudell.info/newstack/right-align-cell-in-table.png)

这更像样了。展示你的研究发现了什么，但如果不存在确定的答案，就不要假装有。当您无法引用证据时，请说明。

## 使用可测试的文档进行上下文工程(Context Engineering)

在[上一期](https://thenewstack.io/mcp-is-rss-for-ai-more-use-cases-for-model-context-protocol/)（以及[更早的一篇文章](https://thenewstack.io/code-in-context-how-ai-can-help-improve-our-documentation/)）中，我建议文档现在可以进行测试。如果有一种正确的方法来做某事，那么与AI代理一起工作的XMLUI开发人员应该能够找到它。未能找到正确的解决方案应该指向文档中的一个漏洞，我们可以通过添加一个说明推荐模式的工作示例来弥补该漏洞。然后，我们可以进行测试以验证以前失败的搜索现在以我们期望的方式成功。

> 我们编写文档的方式都不会优先考虑LLM。可访问性原则“路缘坡道使每个人都受益”也适用于此处。

现在您听到的一件事是：“我们不再为人们写作，我们正在为机器写作，以便他们可以帮助人们。” 我不这样认为。我们编写文档的方式都不会优先考虑LLM。可访问性原则“路缘坡道使每个人都受益”也适用于此处。周到的命名和仔细的选择分层——这些都是使所有读者受益的编辑最佳实践。然而，真正优先考虑LLM的是MCP服务器，该服务器以最适合代理处理的方式向代理提供文档。

它正在成为一种伙伴关系，其中对代理友好的文档帮助我们与代理一起创建更多更好的对代理友好的文档，而具有文档意识的MCP服务器帮助我们与代理一起以文档知情的方式生成软件。代理甚至可以帮助我们调整MCP服务器对代理的有用性。那是这项练习中最令人愉快的部分：与代理一起迭代MCP服务器，使用它，内省他们的工具选择和搜索策略，并将学习内容反馈到MCP服务器的下一个迭代中。

尽管自主LLM本质上是不可靠的，但是在不可靠的层之上构建可靠层存在悠久的软件传统。这也适用于此处。我们无法保证在使用XMLUI MCP服务器从文档、来源、操作指南和示例中提取模式的代理的帮助下构建XMLUI应用程序时，您永远不会被误导。但是现在，您和您的AI团队更有可能锚定到事实依据。在这一点上，我会将上下文工程(context engineering)定义为实现这一目标所需的任何措施。