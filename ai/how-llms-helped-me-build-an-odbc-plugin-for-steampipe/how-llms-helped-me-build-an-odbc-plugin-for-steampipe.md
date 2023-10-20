<!--
# LLM如何助我打造Steampipe的ODBC插件
https://cdn.thenewstack.io/media/2023/09/4eac67bf-steampipe-1024x684.jpg
Image via Pexels
 -->

Jon Udell运用ChatGPT、Cody以及GitHub Copilot来协助他为Steampipe开发ODBC插件，后者是一个可扩展的SQL接口，用以连接云API。

译自 [How LLMs Helped Me Build an ODBC Plugin for Steampipe](https://thenewstack.io/how-llms-helped-me-build-an-odbc-plugin-for-steampipe/) 。

我在LLM时代来临前已经为我的前两款Steampipe插件([Hypothesis](https://hub.steampipe.io/plugins/turbot/hypothesis)和[Mastodon](https://hub.steampipe.io/plugins/turbot/mastodon))编写了代码，因此非常渴望能与我的助手团队一起开发下一个项目：用于ODBC(开放数据库连接)的插件。

Steampipe从表面上是将API映射到数据库表。当你执行`select * from aws_sns_topic`时，Steampipe实际调用的是AWS ListTopics API。许多Steampipe插件就是这样工作的：一个表对应一个特定的API调用。

但是，有些插件工作方式更为通用。Net插件中的[net_http_request表](https://hub.steampipe.io/plugins/turbot/net)将Steampipe变成了HTTP客户端。[exec插件](https://hub.steampipe.io/plugins/turbot/exec)为shell命令创造了SQL接口，[Terraform](https://hub.steampipe.io/plugins/turbot/terraform)插件对基础设施即代码配置文件也做了同样的工作。通过扩大什么才算API的定义，Steampipe不断拓展它对各种形式结构化数据的支持。

数据库也提供了一种API。Steampipe的数据库插件不能使用固定模式，而必须动态发现模式。当插件SDK增加对动态模式的支持时，[CSV](https://hub.steampipe.io/plugins/turbot/csv)插件第一个使用了这个特性。因此，它成为启发ODBC插件的一个来源，后者会为任何具有ODBC驱动的数据库创建SQL接口。

Jose Reyes的[Postgres插件](https://github.com/jreyesr/steampipe-plugin-postgres)是另一个灵感来源(清楚起见，这只是他对Steampipe的[深入研究](https://jreyesr.github.io/tags/steampipe/)的一小部分)。Postgres插件使Steampipe可以查询远程Postgres表。

## 这些例子你看到了吗？请为ODBC做类似的工作。

这是我的梦想。嘿，问问又不会受伤，对吧？但这对我的团队来说不是很好的使用方式。我无法让ChatGPT、Sourcegraph Cody或GitHub Copilot从例子中推断出任何接近工作插件的东西。相反，像往常一样，我们将任务分解成可管理的块。像往常一样，这样效果很好。

这里有一个小例子，说明了它提供的有用帮助。该插件需要一个配置文件来定义ODBC数据源和表名。这些定义使用HCL编写。通过团队的反复讨论，我设计了一种格式，可以与Steampipe的配置模式一起使用。

```hcl
connection "odbc" {
    plugin = "odbc"
 
    data_sources = [
      "SQLite:foo",
      "PostgreSQL:jose"
    ]
}
```

给定这一点，LLM然后就可以编写插件配置所需的样板代码了。这些小事积少成多。

## 障碍及其解决方案

ODBC是进入数据源宇宙的大门。首先，你要在Linux上安装类似[unixODBC](https://www.unixodbc.org/)的驱动程序管理器，然后添加可以连接SQLite或Postgres的驱动程序，或者连接那些甚至不是数据库的源(它们是进入其他数据源宇宙的门户)。[CData](https://www.cdata.com/drivers/)提供了广泛的ODBC驱动程序，其中一些与Steampipe插件重叠，而其他则没有。这听起来是测试插件的一个有趣第一步，因此我安装了CData的RSS和Slack驱动程序，并着手让插件发现它们的模式。

但是，当我试图在插件的初始化阶段调用ODBC驱动程序时，没有任何作用；日志中还出现了关于底层操作系统信号处理的不祥信息。这是我无法调试的问题——是Steampipe？CData？unixODBC？还是三者的组合？但如果可能的话，我仍想取得进展。因此，我尝试了几种解决方案：使用互斥锁保护插件对ODBC驱动程序的调用，调整时序，以及最终有效的在初始化后运行模式发现并将模式缓存到文件系统。ChatGPT说这“有点投机取巧”。但我能够快速迭代这些选择的能力，在其帮助下，起到了决定性作用。

## 模式发现

Steampipe插件使用Go编写，它们高度依赖Go生态系统中的数据源SDK。ODBC插件的最佳选择是github.com/alexbrainman/odbc。它工作良好，支持一些内省，但最通用的方法似乎也是最笨的：选择一行数据，捕获列名，并试图推断它们的类型。LLM(主要是ChatGPT)很快就实现了这种策略。

我们确实讨论了它的缺陷。例如，如果示例的第一行包含空值怎么办？这不是一个致命的缺陷，这意味着该列将始终是一个字符串类型，Steampipe查询作者将不得不编写`where number::int > 1`而不是`where number > 1`，这还不算太糟。我们还一致认为，如果插件存活并成熟，那么投入一种方式让插件用户提供提示以激活特定于数据库的发现机制可能是值得的。但与此同时，笨方法已经足够用了，可以继续推进。

## 实现SQL到SQL的下推

这是一个查询来找到[分配给你的未关闭问题](https://hub.steampipe.io/plugins/turbot/github/tables/github_my_issue#list-all-of-the-open-issues-assigned-to-you)。

```sql
select
  repository_full_name，
  number
  title
from
  github_my_issue
where
  state = 'OPEN';
```  

如果GitHub插件不实现下推，Steampipe会将查询映射到GitHub API来列出所有你的问题，并返回包含所有问题的表。然后Steampipe的Postgres引擎会将WHERE条件应用到结果过滤，只保留打开的问题。

当然，你更希望在可能的情况下将此类过滤下推到API中。因此，这里实际发生的是插件将`state`定义为可选的键列(也称为限定词或“qual”)。当查询包含`where state = 'OPEN'`时，插件会调整API调用以包含该过滤条件。

当插件的API是SQL时，同样的想法也适用。你可以在[这里](https://github.com/jreyesr/steampipe-plugin-postgres/blob/ef30b9f32aa91fdba6862c9ca0a39632814ba6b1/postgres/utils.go#L134)的Postgres插件中看到。[表定义](https://github.com/jreyesr/steampipe-plugin-postgres/blob/ef30b9f32aa91fdba6862c9ca0a39632814ba6b1/postgres/table_code_postgres.go#L13)的List函数将在每个发现的模式中将所有列设置为可选的键列，以便在Steampipe的WHERE子句中提及它们中的任何一个或全部，并下推到远程Postgres处理的WHERE子句中。

ODBC插件也是如此。仅从这个查询中你无法看出来。

```sql
select
  name，
  number，
  _metadata
from
  odbc.sqlite_foo
where
  number = 1
```

```
+------+--------+-------------------------------------------+
| name | number | _metadata                                 |
+------+--------+-------------------------------------------+
| jon  | 1      | {"connection_name":"odbc","dsn":"sqlite"} |
+------+--------+-------------------------------------------+
```

但是在内部，因为插件实现了下推，其调试日志显示WHERE过滤器是由SQLite处理的，而不是由Steampipe处理。

ChatGPT在第一次试验中没有做对。尽管Postgres插件提供了清晰的例子，但它提供的部分解决方案正确地调整了传递给SQLite的SQL，却忽略了定义可选键列这一点。这很容易修复，最终我们一起实现了这个功能，比我自己工作轻松许多。

## 测试策略

我请团队讨论测试插件的方式，整体反馈都相当不错。Copilot为`getSchemas`函数提出了合理的测试，但在解决了幻觉后，仍有问题让它运行。日志记录很麻烦，模拟数据库连接也是。

在LLM的帮助下解决这些问题要比其他情况容易得多。太容易了，事实上我迷失了方向。学习与插件SDK的日志记录机制交互的细节以及使用模拟连接ODBC驱动程序的方法很有趣。随着快速迭代解决方案的能力，我取得了快速进展。但是随着测试代码变得越来越复杂，这似乎需要过多努力才能获得较少的回报。

因此，我决定切换到端到端测试策略：用示例数据填充各种ODBC源，并针对它们运行Steampipe查询。我发现LLM在生成测试数据方面表现优秀。在这种情况下，首先是编写独立程序来填充SQLite数据库。三个助手都轻松完成了这件事，但ChatGPT的版本最有趣。鉴于我们对第一行采样策略的讨论，它“知道”第一行应该包含空值。

## 事后总结：复查和解释

最后，我邀请团队回顾代码并解释工作原理。ChatGPT在此过程中积累了充足的上下文，做得很出色。由于Cody和Copilot没有那么多参与，上下文较少，我认为这是一次有用的测试。LLM帮助你面向不熟悉的代码的能力是一个关键优势。

Cody和Copilot都提供了有用的解释。鉴于两者都可以查看本地仓库中的代码，我对Copilot幻想出的文件名和函数名感到惊讶，而Cody说对了。

![](https://cdn.thenewstack.io/media/2023/09/ba05f452-odbc-explain-cody-copilot.png)

然后我要求Cody和Copilot评估模式发现策略。我已经与ChatGPT进行了广泛讨论，并认为明显的缺陷——对第一行采样的风险可能会对某些列找到空值——对首个版本的插件来说是一个可以接受的风险，该插件可能会在以后用特定于数据库的逻辑进行增强。

![](https://cdn.thenewstack.io/media/2023/09/87134aff-odbc-weaknesses-1024x621.png)

Cody对关键缺陷的更完整和连贯的回应证实了这一点，而Copilot较短的回答则忽略了这点。

总的来说，我发现请LLM回顾代码和文字都很有帮助。当[橡皮鸭回话](https://blog.jonudell.net/2023/05/24/when-the-rubber-duck-talks-back/)时，反馈可能有用也可能无用，不准确。但无论哪种方式，这种互动都可以促使你以不同的视角思考你正在做的事情。这感觉上具有内在价值。
