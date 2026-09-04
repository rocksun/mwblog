**我一直对公司的产品策略感到好奇**，当他们接连发布产品，并宣称新产品“好得多”从而进行降价竞争时。

[GLM-5.3](https://thenewstack.io/glm-5-3-post-training-coding/) 和 [GLM-5.3-Flash](https://thenewstack.io/glm-5-3-flash-chinese-chips/) 就是很好的例子。Z.AI 于 8 月 26 日发布了 GLM-5.3-Flash，并打出了[大胆的营销口号](https://docs.z.ai/guides/vlm/glm-5.3-flash)：以“极低的成本”提供更强的智能，并且服务速度提高了 3 倍。其架构相比本月初发布的旗舰机型 GLM-5.3，将注意力计算量减少了 3 倍。

在 [OpenRouter](https://thenewstack.io/stripe-acquires-openrouter-tokens/) 上，Flash 的输入 token 价格为每百万 0.075 美元，输出 token 为 0.25 美元。而 GLM-5.3 分别为 1.188 美元和 4.18 美元，后者价格贵了近 16 倍。看起来确实更便宜，但我们的测试将对此进行验证，因为最终还是要看 token 的使用量。

如果它消耗更多的 token，那么我们必须将较低的成本归因于定价策略的调整，这意味着如果 Z.AI 改变其定价结构（即结束我们目前所享受的免费增值模式），它最终可能会变得更贵。

为了查明真相，我针对三个任务和 27 个问题对每个模型进行了测试，以确定哪个模型更好，以及 GLM-5.3-Flash 是否在市场上占有一席之地。

## 测试

我针对用户在实际工作中会用到的主题对两个模型进行了测试：

* **编程** – 编写一个 Python 日期解析函数的规范，包含严格的边界情况：多种输入格式、两位数年份、无效日期必须返回 None。我的评分标准是，在任何模型看到规范之前，先运行我编写并验证过的包含 12 个用例的隐藏测试集来测试它们生成的代码。
* **推理** – 一个排班难题，根据七条相互关联的规则将五个人安排到五个会议时段。我预先暴力破解了所有 120 种可能的排班表，以确认唯一存在的解。
* **信息提取** – 一份包含 10 个分散事实的供应商谈判邮件往来，其中包含一个陷阱：8% 的折扣适用于修订后的 92 个席位价格，而不是最初的报价。

我在测试章节中包含了所有提示词，以便任何人都可以自行复现。

## 测试 1：日期解析器

提示词：

```
"Write a Python function parse_event_date(s) that converts a date string to ISO format YYYY-MM-DD. Supported input formats: Month D, YYYY (e.g., March 5, 2026), D Month YYYY, US-style MM/DD/YYYY or M/D/YY, and ISO YYYY-MM-DD. Month names may be full or 3-letter abbreviations, in any letter case. Two-digit years always mean 2000-2099. Ignore leading and trailing whitespace. Return None for dates that don't exist on the calendar, strings missing a year, and anything unparseable. Use only the Python standard library."
```

这是最难的测试，但产生的数据最奇怪。两个模型生成的代码都通过了所有 12 个隐藏测试，包括那些陷阱。例如，2 月 30 日被正确拒绝；“12/31/99”被正确解读为 2099 年，没有年份的日期被正确返回 None。

但达到同样的结果所花费的代价大不相同。GLM-5.3-Flash 花费了 455.8 秒，其中大部分时间用于生成 38,677 个 token（这消耗了大量的 token）进行推理，最后才得出 60 行的功能代码。GLM-5.3 花费了 174.7 秒和 14,801 个 token，得出了几乎完全相同的方案。Flash 的账单依然更低，为 0.019 美元，而 GLM-5.3 为 0.065 美元，这是因为其每 token 的单价实在低太多了。

> “‘预算型’模型的低价掩盖了它为了得到相同答案而付出更多努力的事实。”

如果 Flash 按旗舰级的费率收费，其 38,677 个 token 的思考过程将花费 0.16 美元，是旗舰模型 0.065 美元账单的 2.5 倍。这种“预算型”模型的低价，掩盖了它为了得到相同答案而付出更多努力的事实。

## 测试 2：排班难题

提示词：

```
"Five consultants (Ana, Ben, Carla, Dev, Elena) each get exactly one meeting slot: 9am, 10am, 11am, 1pm, 2pm. Rules: 1. Ana is not in the first slot and not in the last slot. 2. Ben's slot is earlier than Carla's. 3. Dev's slot is immediately after Ana's. 4. Elena's slot is not adjacent to Ben's. 5. Carla is not at 11am. 6. Ben is not at 9am. 7. Elena is not at 2pm. Exactly one schedule satisfies all seven rules. State the final schedule."
```

两个模型都给出了唯一的有效排班表，五个人的安排都准确无误。GLM-5.3 在答案中展示了清晰的逐项排除过程，用时 18.9 秒，消耗 1,804 个输出 token。Flash 用时 33.5 秒，消耗 1,003 个输出 token，直接给出了结果，没有展示推导过程。有些人可能喜欢看过程，但我不需要。我更喜欢简短、直击要点的回答（这在 AI 中有时很难做到）。

> 在简单的工作中，预算模型确实名副其实（如果你是在控制成本，而不是时间）。

这是本次测试中对两者来说最便宜的一项：Flash 为 0.0003 美元，旗舰版为 0.008 美元。token 的计算在这里发生了反转。旗舰模型生成的 token 比 Flash 多 80%，即使 Flash 按旗舰费率收费，这个答案也只需 0.004 美元，大约是旗舰账单的一半。在简单的工作中，预算模型确实名副其实（如果你是在控制成本，而不是时间）。

## 测试 3：供应商邮件

提示词：

```
“A three-email vendor renewal thread (full text in my test kit), with the instruction to extract vendor, renewal date, seat counts, costs, discount, deadline, contract number, and proposed call time into JSON."
```

邮件往来中的陷阱隐藏在数学题中。8% 的折扣适用于 73,600 美元（修订后的 92 个席位报价），而不是最初的 68,000 美元（85 个席位报价）。两个模型都避开了陷阱并返回了准确答案。它们都正确提取了全部 10 个字段，并返回了正确的最终价格 67,712 美元。

这是预算模型在速度和成本上获胜的首个测试。用时 7.7 秒对 14.8 秒，输出 token 为 435 对 327。这表明 Flash 的速度并不总是很慢。在简单的工作中，它表现得像一个预算模型应有的样子。交给它难活，它的推理阶段就会膨胀。

## 结果

| 指标 | GLM-5.3-Flash | GLM-5.3 |
| --- | --- | --- |
| **准确率** | 27/27 | 27/27 |
| **总 token 数** | 41050 | 17867 |
| **总成本** | $0.0198 | $0.0757 |
| **平均响应时间** | 165.7s | 69.5s |

我对这两个模型进行了编码任务、逻辑难题和数据提取任务的测试，每个任务 27 分，以衡量预算模型放弃了多少准确度。结果它没有放弃任何准确度；两者得分均为 27/27。

Flash 的速度不是必然的。它取决于工作的难度。在三个任务中最难的编码任务中，Flash 花费了 7.6 分钟并产生了 38,677 个输出 token，才得出旗舰模型在 3 分钟内用 14,801 个 token 达到的答案。在难度中等的难题上，两者用时相差无几。在简单的提取工作中，Flash 是更快的模型。Z.AI 的效率宣传应该加上一个前提：请将 Flash 用于最简单的任务，因为它虽然能处理困难工作，但效率远低于旗舰版。

## 我的看法

我带着测量廉价模型会损失多少准确性的想法进行了测试。结果它没有损失任何准确性。在复杂的编码规范、逻辑难题和细节繁多的信息提取中，两个模型同样准确。

它们的区别在于最适合的场景。选择取决于模型在做什么。Flash 在提取任务中更快，但在排班难题中较慢，尽管两次运行都在几秒钟内完成。

> 困难的工作最终取决于你是想花时间还是花钱。

困难的工作最终取决于你是想花时间还是花钱。Flash 以大约总成本的四分之一得到了相同的答案，但完成编码任务的时间却花了两倍多。而且不要太执着于成本计算。Flash 在处理困难工作时会消耗更多的 token，因此它的优势取决于当前的每 token 价格，而提供商随时可能更改这些价格。

#### 更多来自 *The New Stack* 的 Z.ai 相关内容：