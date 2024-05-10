
<!--
title: 与AI结对：一位高级开发人员构建插件的历程
cover: https://cdn.thenewstack.io/media/2024/05/08083d58-getty-images-hot2zb6x-gk-unsplash.jpg
-->

作者分享了他使用 ChatGPT 学习 Go、浏览 Kolide API 以及构建一个复杂的 Steampipe 插件的经验。

> 译自 [Pairing With AI: A Senior Developer's Journey Building a Plugin](https://thenewstack.io/pairing-with-ai-a-senior-developers-journey-building-a-plugin/)，作者 Jon Udell。

虽然改进[开发人员文档](https://thenewstack.io/code-in-context-how-ai-can-help-improve-our-documentation/)始终有帮助，但许多人（包括我自己）更喜欢在实践中学习。这是我在[七项指导原则](https://thenewstack.io/7-guiding-principles-for-working-with-llms/)中提出的第七项，也是最重要的一项：因为你在面向任务的可教授时刻获取知识，所以学习不是前瞻性的，而是直接且切实的。

> 当经验丰富的开发人员与 LLM 合作时，其机器智能会支持并增强你的智力。

好处对我来说很明显。在 LLM 时代编写 [Steampipe 的 ODBC 插件](https://thenewstack.io/how-llms-helped-me-build-an-odbc-plugin-for-steampipe/) 比我在没有此类帮助的情况下编写插件的体验容易得多。但那公认是一个主观评估，所以我一直在寻找一个机会与另一位插件开发人员比较笔记，当 [James Ramirez](https://www.linkedin.com/in/ramirezj/) 在我们的社区 Slack 中出现并宣布一个新插件用于 [Kolide API](https://hub.steampipe.io/plugins/grendel-consulting/kolide) 时。我邀请他告诉我他构建它的经历，他亲切地带我进行了一次与 ChatGPT 的长时间对话，在此对话中，他熟悉了三个对他来说都是新知识的技术领域：Kolide API、Go 语言和 Steampipe 插件架构。

作为一个额外的挑战：虽然插件开发人员通常为其插件针对的 API 找到合适的 Go SDK，但这里并非如此。因此，有必要为 Kolide API 创建一个 Go 封装，然后将其集成到插件中。

## 测试 ChatGPT 的 Go 能力

James 从一些热身练习开始。首先，为了测试 ChatGPT 的 Go 能力，他提供了一对 Go 函数，他编写了这些函数来调用相关的 API */devices/* 和 */devices/ID*，并要求对它们之间的共享逻辑进行惯用重构。

接下来，他使用简单的可变参数而不是更复杂的 [函数选项模式](https://davidbacisin.com/writing/golang-options-pattern) 探索了函数的可选参数，并确定了简单的方法——使用 *Search* 结构的切片来封装 Kolide 的 [查询参数](https://www.kolide.com/docs/developers/api#search) 的字段/运算符/值样式——就足够了。他要求一个函数将 *Search* 结构的切片序列化为一个 REST URL，然后优化 ChatGPT 提出的版本以创建最终的 [serializeSearches](https://github.com/grendel-consulting/steampipe-plugin-kolide/blob/92614f899c402b28e7bb95ccdabf50b43b1e8762/kolide/client/search.go#L24-L49)，该版本增加了对将友好名称映射到参数的支持并使用字符串构建器。

> AI 处理吹毛求疵，并经常提供可提交的建议。

其中一些优化，包括使用字符串构建器，是由 AI 驱动的机器人 [CodeRabbit](https://coderabbit.ai/) 提出的，它提供了有用的代码审查。他说，这是帮助你和你的团队专注于全局的反馈，因为它处理吹毛求疵，并经常（但并非总是）提供可提交的建议。它还采取更广泛的视角来 [总结拉取请求](https://github.com/grendel-consulting/steampipe-plugin-kolide/pull/60) 并评估已关闭的 PR 是否解决了其关联问题中陈述的目标。

## 映射运算符

他继续探索将 Steampipe 运算符（如 *QualOperatorEqual*）映射到 Kolide 运算符（如 *Equals*）的方法。同样，ChatGPT 提出的方法也变成了一个一次性方案，朝着一个干净简单的方案前进。但正如 James 在我们的采访中证实的那样，由于你无论如何都会迭代一次性版本，所以能够生成合理的迭代而不是通过手工更繁琐地对它们进行编码是有帮助的。在此过程中，他正在学习基本的 Go 惯用语。

**James：**

Go 中有 do-while 循环吗？

**ChatGPT**

没有，但是……

**James：**

Go 中有三元运算符吗？

**ChatGPT**

没有，但是……

**James：**

我如何追加到 *map[string]string*？

**ChatGPT**

像这样……

## 使用反射增强的访问者模式

在理解了基础知识并为 Kolide API 开发了一个 Go 客户端后，James 准备解决插件开发的实际工作：定义从 API 封装返回的 Go 类型映射到控制针对这些表的 SQL 查询的 Steampipe 架构的表。

与所有插件开发者一样，他从一个可以列出资源集的表开始，然后通过过滤和分页对其进行增强。在添加第二个表后，是时候考虑如何抽象出公共模式和行为。最终结果是访问者模式的优雅实现。以下是与表 [kolide_device](https://hub.steampipe.io/plugins/grendel-consulting/kolide/tables/kolide_device) 和 [kolide_issue](https://hub.steampipe.io/plugins/grendel-consulting/kolide/tables/kolide_issue) 相对应的 Steampipe
*List* 函数。

```go
func listDevices(ctx context.Context, d *plugin.QueryData, h *plugin.HydrateData) (interface{}, error) {
	var visitor ListPredicate = func(client *kolide.Client, cursor string, limit int32, searches ...kolide.Search) (interface{}, error) {
		return client.GetDevices(cursor, limit, searches...)
	}

	return listAnything(ctx, d, h, "kolide_device.listDevices", visitor, "Devices")
}


func listAdminUsers(ctx context.Context, d *plugin.QueryData, h *plugin.HydrateData) (interface{}, error) {
	var visitor ListPredicate = func(client *kolide.Client, cursor string, limit int32, searches ...kolide.Search) (interface{}, error) {
		return client.GetAdminUsers(cursor, limit, searches...)
	}

	return listAnything(ctx, d, h, "kolide_admin_user.listAdminUsers", visitor, "AdminUsers")
}
```

以下是所有插件表通用的列表清单函数。

```go
func listAnything(ctx context.Context, d *plugin.QueryData, h *plugin.HydrateData, callee string, visitor ListPredicate, target string) (interface{}, error) {
	// Create a slice to hold search queries
	searches, err := query(ctx, d)
	if err != nil {
		plugin.Logger(ctx).Error(callee, "qualifier_operator_error", err)
		return nil, err
	}

	// Establish connection to Kolide client
	client, err := connect(ctx, d)
	if err != nil {
		plugin.Logger(ctx).Error(callee, "connection_error", err)
		return nil, err
	}

	// Iterate through pagination cursors, with smallest number of pages
	var maxLimit int32 = kolide.MaxPaging
	if d.QueryContext.Limit != nil {
		limit := int32(*d.QueryContext.Limit)
		if limit < maxLimit {
			maxLimit = limit
		}
	}

	cursor := ""

	for {
		// Respect rate limiting
		d.WaitForListRateLimit(ctx)

		res, err := visitor(client, cursor, maxLimit, searches...)
		if err != nil {
			plugin.Logger(ctx).Error(callee, err)
			return nil, err
		}

		// Stream retrieved results
		collection := reflect.ValueOf(res).Elem().FieldByName(target)
		if collection.IsValid() {
			for i := 0; i < collection.Len(); i++ {
				d.StreamListItem(ctx, collection.Index(i).Interface())

				// Context can be cancelled due to manual cancellation or the limit has been hit
				if d.RowsRemaining(ctx) == 0 {
					return nil, nil
				}
			}
		}

		next := reflect.ValueOf(res).Elem().FieldByName("Pagination").FieldByName("NextCursor")
		if next.IsValid() {
			cursor = next.Interface().(string)
		}

		if cursor == "" {
			break
		}
	}

	return nil, nil
}
```

有了此设置，向插件添加新表几乎完全是声明式的：你仅需定义架构及 KeyColumns，以及在 SQL 查询中的 where（或 join）子句与 API 级过滤器之间形成桥梁的相关运算符。然后编写一个微小的 List 函数，该函数定义一个访问器，并将该函数传递到 common listAnything 函数中，该函数封装查询参数编组、连接至 API 客户端、调用 API、将响应解压缩到一个集合中以及迭代集合以将数据项传输到 Steampipe 的外部数据包装器的功能。

James 使用 ChatGPT 来启动访问者模式在 Go 中的惯用实现。这包括学习如何为访问者函数定义一个类型，然后声明一个函数来满足类型。每个表的访问者都封装对 API 客户端的调用，并返回一个接口。所有这些都相当通用，但访问者的响应特定于包装的 API 响应的 Go 类型，这意味着需要为每个表编写一个不同的 List 函数。如何避免这种情况？James 问道：“res 变量上的字段引用需要是可变类型，在执行时指定。你能建议一种方法吗？”

ChatGPT 的建议（他采纳了）是使用反射，以便调用 listAnything（如 listAnything(ctx, d, h, “kolide_device.listDevices”, visitor, “Devices”））可以传递一个名称（"Devices"），使 listAnything 能够以与类型无关的方式访问响应结构的字段，例如，此处的 Devices 字段。

```go
    type DeviceListResponse struct {
      Devices    []Device   `json:"data"`
      Pagination Pagination `json:"pagination"`
    }
```

正因如此，listAnything 终于如其名，成为一个通用的 Steampipe List 函数。该解决方案很少使用反射，并在 API 层和 Steampipe 层中都保留了 Go 的强类型检查。

## LLM 协助真正意味着什么？

它肯定 *不* 意味着 LLM 根据以下提示编写了一个体现复杂设计模式的插件：“我需要一个用于 Kolide API 的 Steampipe 插件，请创建它。”对我来说，以及对 James 来说，它的含义更有趣：“让我们讨论为 Kolide API 编写插件的过程。”这就像与一只橡皮鸭交谈，以便大声思考需求和策略。但 LLM 是 [一只会说话的橡皮鸭](https://blog.jonudell.net/2023/05/24/when-the-rubber-duck-talks-back/)。有时响应直接适用，有时不适用，但无论哪种方式，它们通常可以帮助你获得清晰度。

> 作为一名经验丰富的软件工程师，James 本可以想出办法——但这需要更长的时间。

James 说：“对话要求我对所问的问题非常具体。”虽然他从头开始使用 Go，但他带来了丰富的经验，使他能够快速定位并找出哪些是需要问的正确问题。作为一名经验丰富的软件工程师，James 本可以自己想出所有这些。但这需要更长的时间，而且他将花费大量时间预先阅读文章和文档，而不是通过实践学习。而且可能没有时间！正如我现在从许多其他人那里听到的那样，LLM 提供的加速通常决定了拥有一个想法和能够执行它之间的区别。

James 还提到了我未考虑过的开源角度。在 LLM 之前，他不会以完全公开的方式完成这项工作。“我会一直保密，直到我更有信心，”他说，“但这从一开始就在那里，我很高兴它在那里。”这使得与 Turbot 团队的接触尽早成为可能。

这不是一个自动化故事，而是一个增强故事。当像 James Ramirez 这样的经验丰富的开发人员与 LLM 合作时，其机器智能支持并放大了他的智力。两者协同工作——不仅编写代码，更重要的是，思考架构和设计。
