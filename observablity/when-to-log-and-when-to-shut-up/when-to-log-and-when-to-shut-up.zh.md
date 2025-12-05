说实话：大多数日志都只是噪音。

| |
| --- |
| `[INFO] Starting process … probably.` `[DEBUG] Made it to line 42 — still alive.` `[TRACE] Function entered. Leaving soon.` `[INFO] User clicked a button. Which one? No idea.` `[WARN] Everything’s fine, just felt like warning you.` `[DEBUG] Variable x = 7. Might change. Might not.` `[INFO] Operation completed successfully (we think).` `[TRACE] Loop iteration #12 of infinite sadness.` `[DEBUG] Placeholder for meaningful message.` `[INFO] Shutting down gracefully … except when not.` |

作为开发者，我们常常像撒纸屑一样散布日志——每个函数入口、每个变量、每次心跳。很快，数TB毫无意义的日志行堆积如山，塞满了无人问津的仪表盘。

我们花费数百万美元给可观测性供应商，仅仅是为了存储我们的垃圾。每条无用的日志行都消耗计算资源、磁盘空间和金钱。无目的的[日志记录](https://thenewstack.io/how-to-evaluate-logging-frameworks-10-questions/)不是[可观测性](https://thenewstack.io/introduction-to-observability/)，而是制造垃圾。

即使是现代可观测性平台，[通过列式存储大幅提高压缩率](https://clickhouse.com/blog/log-compression-170x)，也没有理由记录所有内容。这仍然会将根本原因分析变成大海捞针的问题，稀释了你真正需要的信号——而且你还要为此支付更多费用。

我们需要有选择性。记录那些有助于我们理解系统、调试实际问题或解释业务影响的内容——其他的一切都不要记录。

## 日志行的哲学

每一行日志都是一种选择，而不是一种条件反射。如果它不能帮助你在凌晨3点追踪一个bug，那就删除它。日志记录不是写日记；保持其简洁、清晰且真正有用。

在你点击 `logger.info` 之前，停下来问问自己：我真的会grep这条日志吗？

如果不会，那就删除它。日志不是叙述；它们是证据。它们的存在是为了告诉你系统在出错时在想什么。

日志不应被降级到可观测性链的末端。它们不仅是确认的显微镜，更是发现的地图。有时，获取洞察最快的方法是探索原始文本——grep、过滤并遵循直觉。

日志能激发好奇心——它们揭示了指标可能掩盖的细微之处，以及跟踪（traces）无法表达的上下文。不要将它们视为最后的手段，而应将其视为一个活生生的真相来源，从一开始就可供探索。

## 无上下文，便如未发生

没有输入、ID或状态的“发生错误”毫无意义。添加足够的上下文来重构那一刻——请求ID、用户ID、输入参数、操作名称。如今，借助OpenTelemetry，你可以免费获得跟踪（trace）和跨度（span）ID。使用它们。通过跟踪ID连接到跟踪（甚至指标）的日志，比独立的文本行有无限的价值。

日志不是一个独立的支柱；它们是你根本原因分析的最后一章。你根据指标发出警报，通过跟踪进行调查，然后深入日志查看实际发生了什么。当你的日志通过跟踪和跨度ID链接起来时，它们就不再是噪音，而变成了证据——范围紧密、有上下文，并直接与单个请求的路径相关联。这才是带有目的的可观测性，而不是一堵文本墙。

## 结构良好，而非自由文本

自由文本日志记录已经过时了。结构化日志，无论是JSON、CSV还是键值对，不仅更容易查询；它们更是分析的基础。一旦日志具有结构，模式就会浮现：

*   这个错误上周开始激增。
*   这主要发生在事件X之后。
*   此警告与此特定部署相关联。

日志记录的未来不是阅读一行，而是看到成千上万行中的模式。

[![Structured logging makes charting easy and efficient](https://cdn.thenewstack.io/media/2025/12/057dadf0-image1.png)](https://cdn.thenewstack.io/media/2025/12/057dadf0-image1.png)

结构化日志使图表绘制变得简单高效。

虽然许多可观测性平台提供读取时模式（schema on read），但这种灵活性是有代价的。每个查询都迫使系统逐行扫描和解析原始文本，以推断出本应存在的结构。这些查询计算成本高昂、速度较慢，并且用户编写起来也更困难。

预结构化日志彻底扭转了这种低效率。当你的数据已经有形时，你可以利用[列式存储和原生聚合](https://clickhouse.com/blog/breaking-free-from-rising-observability-costs-with-open-cost-efficient-architectures)——在几毫秒而非几分钟内查询、可视化和关联事件。

## 知道何时测量，而不仅仅是何时记录日志

并非所有[事件都属于日志流](https://thenewstack.io/understanding-log-events-why-context-is-key/)。有些事情值得拥有结构和时间——这正是跨度（span）和指标的作用。如果你正在测量延迟、用户流或分布式因果关系，则应发出一个跨度。跨度捕获跨服务的持续时间、上下文和关系，并告诉你为什么某个东西变慢或损坏，而日志只能喊出它发生了。

同样的逻辑也适用于指标，将重复的日志转换为你可以高效地发出警报和聚合的真实信号。如果你发现自己每秒记录数百次相同的消息，你不是在可观测，而是在浪费存储空间。测量一次，总结一次，让你的指标和跟踪来完成繁重的工作。

## 日志级别是给人看的，不是给机器看的

日志记录不是个人的调试日记；它是供你未来的队友共享的工件。每一行都应该帮助别人理解发生了什么，而无需猜测你的意思。为下一次事件编写日志，而不是为你当前的心情。你的日志讲述了你的系统的故事。让它成为值得阅读的故事，例如：

*   **ERROR：** 呼叫人类。出问题了。
*   **WARN：** 意料之外但可承受。稍后调查。
*   **INFO：** 值得了解的常规系统行为。
*   **DEBUG/TRACE：** 临时的开发者洞察——应很少离开你的笔记本电脑。

要深思熟虑。除非确实需要采取行动，否则不要将某事标记为错误。过度使用ERROR会麻痹你的警报，并使团队习惯于忽略重要的事情。每个日志级别都应该传达意图：现在需要修复什么，需要关注什么，以及可以忽略什么。

话虽如此，跟踪日志记录也有其用武之地。例如，在ClickHouse Cloud的幕后，我们[广泛地进行跟踪日志记录，以帮助我们的工程师诊断性能问题](https://clickhouse.com/blog/scaling-observability-beyond-100pb-wide-events-replacing-otel)，并大规模支持客户。这是一个有意的例外——在运营一个为数千个实时工作负载提供服务的分布式数据库时是必要的。然而，对于大多数应用程序而言，这种程度的冗长不是可观测性；它只是噪音。

## 帮助你少记录、更智能记录日志的工具

存在丰富的SDK和强大的过滤器，所以你不必“记录所有内容”。使用它们。

现代[OpenTelemetry Collector SDK](https://opentelemetry.io/docs/specs/otel/logs/sdk/?utm_source=chatgpt.com) 允许你规定要记录什么：你可以对代码进行插装，以便只创建有意义的日志行，并可以在摄取或收集时过滤或丢弃其他所有内容。

例如：

```
import logging
from opentelemetry.sdk._logs import LoggerProvider, LogRecord
from opentelemetry.sdk._logs.export import ConsoleLogExporter, SimpleLogRecordProcessor

# Configure OpenTelemetry logger provider
logger_provider = LoggerProvider()
logger_provider.add_log_record_processor(SimpleLogRecordProcessor(ConsoleLogExporter()))

# Get a logger from OpenTelemetry
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logger_provider.get_logger(__name__)._handlers[0]) # Simplified for demo

# Log only important events
user_id = "user123"
request_id = "req_abc"

if error_condition:
    logger.error(f"Failed to process request for user {user_id}. Request ID: {request_id}",
                 extra={"user_id": user_id, "request_id": request_id, "error_code": 500})
elif important_event:
    logger.info(f"User {user_id} successfully completed action. Request ID: {request_id}",
                extra={"user_id": user_id, "request_id": request_id, "action": "checkout"})
else:
    # Avoid logging verbose debug messages in production unless strictly necessary
    logger.debug("This is a verbose debug message that we usually filter out.")
```

如果管理员发现用户生成了无意义的日志，他们可以在管道中或通过强制执行最小日志策略来积极过滤这些日志。如果你使用的是专有平台，这些平台也提供了类似的过滤或摄取控制工具，即使它们没有公开宣传。

## 有目的地记录日志，否则就不要记录

可观测性不是关于数量，而是关于清晰度。每一行日志都应该通过解释指标和跟踪无法表达的内容来赢得其位置。无目的的日志记录只会烧钱并埋葬洞察。

要深思熟虑。使用结构。添加上下文。知道何时测量，何时跟踪，以及何时保持沉默。现代工具使自律比以往任何时候都更容易，但这种自律仍然必须来自你自己。

归根结底，出色的日志记录不是关于捕获发生的一切，而是关于捕获重要的内容。