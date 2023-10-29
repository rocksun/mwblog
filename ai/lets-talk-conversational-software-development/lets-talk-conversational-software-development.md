<!--
# 谈谈对话式软件开发

https://cdn.thenewstack.io/media/2023/10/9d9008b3-antoine-barres-jay5bqvyf5a-unsplash-1024x576.jpg
 -->


利用大语言模型生成代码是改变生活的方式之一，但与它们就软件开发过程进行交谈也同样重要。Jon Udell继续探索大语言模型为程序员带来的价值。

译自 [Let’s Talk: Conversational Software Development](https://thenewstack.io/lets-talk-conversational-software-development/) 。

以下是启动了一次非常成功的人工智能ChatGPT交互的提示。

```
PROMPT:
I’ll give you a test script and the output it is testing, and ask about strategies to improve the test, OK? Here’s the script.

```

```bash
#!/bin/bash

set -eu

list_tickets() {
    local output
    output=$($command $subcommand run list_tickets 2&gt;&amp;1) || {
        echo "Command failed with error: $output"
        exit 1
    }
    echo "$output"
}

output=$(list_tickets)
count=$(echo "$output" | jq -r '.tickets_list | fromjson | length')

# Check if count is greater than 0
if [[ $count -gt 0 ]]; then
    echo "PASS: list_tickets count is greater than 0."
else
    echo "FAIL: list_tickets count is 0 or less."
fi
```

## 一次过路人的见解

该提示是一个有意设置的朴实版本的bash脚本，我设想的脚本。我本来也打算在最初的提示中提供样本输出，但忘记这么做了。回想起来，不提供输出而先让ChatGPT专注于脚本本身可能是一个好主意。它的一些观察包括:

```
RESPONSE:
While you’ve used set -eu to exit on any error or unset variable usage, consider using set -euo pipefail to also capture failures in any part of a pipeline.
```

这是一个很好的关于在编码时[如何从LLM中隐性地获取知识](https://yylives.cc/2023/09/10/learning-while-coding-how-llms-teach-you-implicitly/)的例子。我之前对bash中的严格模式有一些了解，但不完整。因此我们暂停了一会儿来探索这个话题，我加深了知识，并记下考虑使用其他`-o`参数 —— 尤其是 `-x(xtrace)` 和 `-n(noexec)` 用于调试。我们刚刚开始处理手头的实际任务，但这个小小的绕道本身就很有价值。

## 让我们来谈谈JSON

我现在回头提供了样本输出:

```
PROMPT:
“tickets_list”: “[{\”associates_rdb\”:null,\”association_type\”:null,\”cc_email\”:{\”cc_emails\”:[],\”fwd_emails\”:[],\”reply_cc\”:[],\”tkt_cc\”:[]},\”created_at\”:\”2023-10-12T12:15:00+01:00\”,\”custom_field\”:{\”cf_reference_number_2939992\”:null},\”datetime_tc01\”:null,\”datetime_tc02\”:null,\”datetime_tc03\”:null,\”deleted\”:false,\”delta\”:true,\”description\”:\”world\”,\”description_html\”:\”\\u003cdiv\\u003eworld\\u003c/div\\u003e\”,\”dirty\”:0,\”display_id\”:17,\”due_by\”:\”2023-10-16T22:00:00+01:00\”,\”email_config_id\”:153000020300,\”frDueBy\”:\”2023-10-12T22:00:00+01:00\”,\”fr_escalated\”:true,\”group_id\”:null,\”id\”:153002218563,\”int_tc01\”:null,\”int_tc02\”:null,\”int_tc03\”:null,\”int_tc04\”:null,\”int_tc05\”:null,\”internal_agent_id\”:null,\”internal_group_id\”:null,\”isescalated\”:false,\”json_tc01\”:null,\”long_tc01\”:null,\”long_tc02\”:null,\”long_tc03\”:null,\”long_tc04\”:null,\”long_tc05\”:null,\”nr_due_by\”:null,\”nr_escalated\”:false,\”nr_reminded\”:false,\”owner_id\”:null,\”parent_ticket_id\”:null,\”priority\”:1,\”priority_name\”:\”Low\”,\”product_id\”:153000018092,\”requester_id\”:153002362554,\”requester_name\”:\”Jon Udell\”,\”requester_status_name\”:\”Open\”,\”responder_id\”:null,\”responder_name\”:\”No Agent\”,\”sl_escalation_level\”:null,\”sl_manual_dueby\”:null,\”sl_merge_parent_ticket\”:null,\”sl_product_id\”:null,\”sl_skill_id\”:null,\”sl_sla_policy_id\”:null,\”sla_state\”:0,\”source\”:2,\”source_name\”:\”Portal\”,\”spam\”:false,\”st_survey_rating\”:null,\”status\”:2,\”status_name\”:\”Open\”,\”subject\”:\”hello\”,\”ticket_type\”:null,\”to_email\”:null,\”to_emails\”:null,\”trained\”:false,\”updated_at\”:\”2023-10-12T22:05:04+01:00\”,\”urgent\”:false},{\”associates_rdb\”:null,\”association_type\”:null,\”cc_email\”:{\”bcc_emails\”:[],\”cc_emails\”:[],\”fwd_emails\”:[],\”reply_cc\”:[],\”tkt_cc\”:[]},\”created_at\”:\”2023-10-12T04:41:12+01:00\”,\”custom_field\”:{\”cf_reference_number_2939992\”:null},\”datetime_tc01\”:null,\”datetime_tc02\”:null,\”datetime_tc03\”:null,\”deleted\”:false,\”delta\”:true,\”description\”:\”Hello there, Our Report metrics over the last week is at zero and can’t be correct? Are you facing any issues?\”,\”description_html\”:\”Hello there, Our Report metrics over the last week is at zero and can’t be correct? Are you facing any issues?\”,\”dirty\”:0,\”display_id\”:6,\”due_by\”:\”2023-10-16T22:00:00+01:00\”,\”email_config_id\”:153000020300,\”frDueBy\”:\”2023-10-12T22:00:00+01:00\”,\”fr_escalated\”:false,\”group_id\”:153000077019,\”id\”:153002214584,\”int_tc01\”:null,\”int_tc02\”:null,\”int_tc03\”:null,\”int_tc04\”:null,\”int_tc05\”:null,\”internal_agent_id\”:null,\”internal_group_id\”:null,\”isescalated\”:false,\”json_tc01\”:null,\”long_tc01\”:null,\”long_tc02\”:null,\”long_tc03\”:null,\”long_tc04\”:null,\”long_tc05\”:null,\”nr_due_by\”:null,\”nr_escalated\”:false,\”nr_reminded\”:false,\”owner_id\”:null,\”parent_ticket_id\”:null,\”priority\”:1,\”priority_name\”:\”Low\”,\”product_id\”:153000018092,\”requester_id\”:153002465401,\”requester_name\”:\”Adam Doe\”,\”requester_status_name\”:\”Open\”,\”responder_id\”:null,\”responder_name\”:\”No Agent\”,\”sl_escalation_level\”:null,\”sl_manual_dueby\”:null,\”sl_merge_parent_ticket\”:null,\”sl_product_id\”:null,\”sl_skill_id\”:null,\”sl_sla_policy_id\”:null,\”sla_state\”:0,\”source\”:1,\”source_name\”:\”Email\”,\”spam\”:false,\”st_survey_rating\”:null,\”status\”:2,\”status_name\”:\”Open\”,\”subject\”:\”Issues with reports\”,\”ticket_type\”:\”Bug\”,\”to_email\”:null,\”to_emails\”:null,\”trained\”:false,\”updated_at\”:\”2023-10-12T04:41:13+01:00\”,\”urgent\”:false}]”
}
```

在另一个情景下，我可能会花时间优化格式化这个 JSON 输出。但是 LLM —— 像编译器和解释器 —— 不关心这些。更棒的是，它们可以容忍会使传统 JSON 格式化程序死机的语法。如果你把上面的例子粘贴到传统格式器，会遇到两个问题。首先，如果不用花括号包裹就不是有效的 JSON。其次， `tickets_list` 的值不会是 JSON 对象，而是字符串，因为该值是 JSON 的字符串化表示。非常神奇的是，LLM “知道” 你的意图并做出正确反应:

```
RESPONSE:
 
{
          "tickets_list": [
            {
              "associates_rdb": null,
              "association_type": null,
              "cc_email": {
                "cc_emails": [],
                "fwd_emails": [],
                "reply_cc": [],
                "tkt_cc": []
              },
              "created_at": "2023-10-12T12:15:00+01:00",
              "custom_field": {
                "cf_reference_number_2939992": null
              },
            ...
            }
        ]
    }
```

这是非常琐碎的东西，但它是可能影响你的工作流程并浪费最好留给高级功能的认知资源的东西。在这一点上，我还进行了我称之为可解释性测试: LLM是否解释了1) 代码片段需要被花括号包裹，以及2) 嵌套的值需要被解析？以下是结果。

| 工具 | llm 提供者 | 解释需要使用{} | 解释tickets_list需要解析 |
|-|-|-|-|  
| chatgpt | openai | 否 | 是 |
| copilot chat | 开放ai | 否 | 是 |
| claude | anthropic | 否 | 否 |
| cody | anthropic | 否 | 否 |


这引起我的兴趣，因为虽然我知道 Copilot Chat 使用 OpenAI ，Cody 使用 Anthropic，但这不总是明显的。各自的聊天界面增强了提示，使回复不同于从底层 LLM 获得的回复。但在这个例子中，工具似乎与它们各自的界面行为一致。

## 让我们来讨论测试策略

ChatGPT 对 `set -euo pipefail` 的观察只是我们可以探索的多个方向之一，但我把话题引回到了手头的任务上: 完善我在最初提示中包含的测试脚本。该脚本测试的是 Freshdesk 票务系统的输出结果，而天真的测试只是检查我们正在测试的工具是否可以调用 Freshdesk 的 API 并返回多于 0 张票。更好的测试会是什么样的呢？ChatGPT 的建议包括检查优先级和状态是否与预期值匹配、空值或长列表的票务是否被优雅处理，以及所有日期字段是否存在并包含有效日期。

我选择了最后一种方法，ChatGPT 相应地修改了测试脚本。这需要编写一个正则表达式来匹配日期，并在每张票的一组日期字段中循环应用该正则表达式。这感觉太复杂了，所以我要求将范围限制为仅检查一个日期字段: `created_at`。即使这样仍然感觉太复杂，所以我们舍弃了循环，将测试简化为仅检查单张票中的有效日期。之后我们转向了下一个话题。

## 让我们来讨论如何将测试推广到一个测试套件

需要测试的用例有:

- 列出 Freshdesk 票据
- 创建新 Freshdesk 票据
- 删除 Freshdesk 票据
- 检索特定 Freshdesk 票据的详细信息
- 更新 Freshdesk 票据
- 向 Freshdesk 票据添加注释

我很少使用 bash 函数，但我觉得在这里它们可能会很有用，所以当看到一个将 bash 脚本结构化为与六个测试用例对应六个函数的回复时，我很高兴。“看起来不错，”我说，“请给我一个完整的构建如此结构化的版本，并包含第一个测试。”

此时，一个在我身边观看的同事想知道是否对 LLMs 使用“请”和“谢谢”会带来更好的结果。这打败了我！我只是因为感觉很好才这样做。这是一种危险的人格化吗？也许吧。但即使它们是非人类，我也看不出欺负我的助手有任何益处。

然后同一位同事问及另一种从表格驱动测试的替代策略。我们问:

```
PROMPT:
We are wondering if it would be better to have a data structure for these tests instead of a set of loose functions, what do you think are the pros and cons?
```

回应提到了优点(可维护性、重用性、并行执行、一致的日志记录、清晰度)和缺点(额外开销、复杂度、迁移时间、学习曲线)。它以这段总结结束:

```
RESPONSE:
Given that your test suite might grow or change over time, adopting a structured approach earlier can be beneficial. However, it’s essential to weigh the initial time investment against the long-term benefits. If you think your test suite will remain relatively small and static, the current loose function setup might suffice. But if you anticipate growth or frequent changes, the structured approach will pay off in the long run.
```

由于我们处于快速原型设计阶段，还没有准备好对此测试策略进行长期投资，所以我们选择保持松散函数的方式。但我们都觉得花几分钟考虑替代方法是非常有价值的。

## 让我们来讨论持久化票据 ID 的方法

要编写的下一个测试是创建票据的测试。ChatGPT 建议存储票据的 ID 以在其他测试中使用，以测试读取、更新和向票据添加注释的功能。并且它编写了一个将 ID 持久化到文件的函数。这让我感到疑惑，并要求评估在文件和变量之间保存的权衡取舍。这里是对回复的摘要，以表格形式进行了修订(感谢 ChatGPT)。

| 保存于文件 | | 保存于变量 | |
|-|-|-|-|
| 优点 | 缺点 | 优点 | 缺点 |  
| 持久性 | 速度较慢 | 速度快 | 挥发性 |
| 进程间通信 | 复杂度高 | 简单 | 限于单个脚本/进程 |  
| 适合大数据 | 需清理 | 无文件依赖 | 内存限制 |

并补充了这个结论:

```
RESPONSE:
If you’re writing a single script, and the data doesn’t need to persist beyond the script’s execution, a variable might be simpler and faster.
```

我甚至没有考虑基于文件的替代方法。当 ChatGPT 使用那种方法时，它促使我考虑并讨论不同方案的权衡取舍。由于我最终做了与使用 LLM 之前完全一样的事，这次绕路就是无谓的吗？我不这么认为。考虑替代方案总是有价值的。这次绕路花费的时间很少，且虽然它没有改变我最终的做法，但过程感觉很有价值。

在为 get_ticket 函数编写测试时，我们也有过类似的交互。检查获取的票据 ID 是否与我们存储的 ID 匹配就足够了吗？ChatGPT 在效率和彻底性之间划清了界限，列出了进行更彻底检查的选项，并建议对于基本的冒烟测试，优先考虑效率是有意义的。同样，我已经会做更简单的事了，所以这并没有改变任何东西。但尽管我知道我们当然是在进行冒烟测试，大声说出来还是显得很有帮助。

## 让我们来讨论 Bash

这里有一个交互极大地改变了结果。我们向测试套件添加了第三个测试，但只运行了前两个。出了什么问题？调试过程与使用 LLM 之前一样，但 ChatGPT 可以更快地在代码中插入打印语句，因此速度快了很多。在进行几次这种暴力试错法后，我们仍然无法通过第二个测试。

然后我想到问: "关闭 `set -euo pipefail` 会有意义吗?" 当我这样做时，脚本就完整运行了 - 即所有 6 个测试都运行了 - 但第二个测试在本应成功的情况下失败了。随后我恍然大悟。我问: "我们应该从 test_create_ticket 返回 $TICKET_ID 吗？" ChatGPT 提醒我一个我读过但从未遇到过的行为:

```
RESPONSE:
In the context of bash scripts, when you return a number from a function, it’s analogous to an exit code.
```

我的天啊！对了！我们需要该函数设置全局变量为所创建票据的值，但返回零以避免过早退出，同时保持严格模式仍然生效。这是最后的突破；在那之后，一切顺利。

## 当橡皮鸭说话时

我不断回到这一系列文章的第一个主题: 当橡皮鸭说话时。大声思考总是有帮助的。理想情况下，你可以与一个人类伙伴一起这样做。橡皮鸭虽然是个糟糕的替代品，但远胜于一无所有。

与 LLM 对话不像这些选择中的任何一个，这完全是另一回事;我们都在努力弄明白它如何发挥作用。要求 LLM 编写代码，神奇地出现代码？这明显是一个改变生活的事情。与 LLM 就你们合作编写的代码进行交谈？我认为这同样是一个不太明显但同样深刻的改变生活的事情。
