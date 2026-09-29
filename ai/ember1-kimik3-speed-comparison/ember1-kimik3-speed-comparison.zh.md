**Fireworks Research 推出了 Ember-1**，于 9 月 23 日作为研究预览版发布。它基于 Moonshot 的[开源权重模型](https://thenewstack.io/open-weight-models-frontier-costs/) [Kimi K3](https://thenewstack.io/kimi-k3-open-weight-coding/) 构建，声称在消耗大约少 40% 的 Token 的情况下，达到了与 Kimi K3 相当的质量。Fireworks 表示，它“学会了在保留关键思考的同时，裁剪不必要的推理”。推理 Token 作为输出计费，因此思考较少的模型成本应该更低。

不过，这里有个问题。在 [OpenRouter](https://thenewstack.io/openrouter-us-region-routing/) 上，Ember 的成本为每百万输入 Token 3 美元，每百万输出 Token 15 美元。Fireworks 对 Kimi K3 的收费相同，但其他提供商销售 Kimi 的价格低至每百万输入 Token 1 美元，每百万输出 Token 9 美元。

我通过 OpenRouter 在 Fireworks 上运行了这两个模型，因此两者的计费都是 3 美元和 15 美元，我还计算了 Kimi 在较低价格下的成本。

如果一个模型不准确，它有多便宜也无济于事。我想知道 Ember 较短的思考过程是否经得起考验。如果它裁剪了实际需要的推理，那么在最困难的问题上，准确率应该最先下滑。因此，我构建了难度逐渐增加的测试，每个测试运行五次，这是我最近的测试中一直在增加的相同一致性检查。

## 测试

我通过 OpenRouter 使用相同的提示词和默认的推理设置调用了这两个模型。为了使速度比较保持公平，我都将它们路由到 Fireworks。每个模型每个测试运行五次，我将推理 Token 与其余输出分开记录。

* **逻辑谜题** – 三个规模递增的谜题，分别有 4、5 和 7 名工程师，每个谜题有一个解决方案。更大的谜题需要更长的推理链，因此减少思考应该最先受到影响。
* **部署调度** – 12 个有依赖关系的微服务，每个团队一次部署一个，并有两个黑窗口期。模型必须找到最快的可能发布方案：17 小时。
* **概率问题** – 关于重试系统的五个问题，其服务器在健康和降级之间切换，外加一个熔断器。每个答案都是一个精确的分数，我通过 200 万次请求的模拟进行了核对。

在任何模型看到答案之前，我都用两种独立的方法确认了每个答案。我在本文末尾附上了提示词，供任何想在自己的系统上复制这些测试的人使用。

### 逻辑谜题

两个模型在所有五次运行中都解出了全部三个谜题。

Ember 平均消耗 13,630 个推理 Token，耗时 3 分 46 秒，每次运行花费 0.27 美元。Kimi 平均消耗 16,679 个推理 Token，耗时 12 分 26 秒，花费 0.34 美元。这意味着 Ember 的推理 Token 减少了 18%。尽管未包含在营销宣传中，但 Ember 比 Kimi 快得多。Kimi 最慢的一次运行耗时近 20 分钟。

### 部署调度

两个模型每次都找到了 17 小时的调度方案，并且每个调度都通过了我的检查器。

Ember 平均消耗 6,543 个推理 Token，耗时 1 分 29 秒，花费 0.10 美元。Kimi 平均消耗 7,792 个推理 Token，耗时 4 分 46 秒，花费 0.13 美元. 这意味着推理 Token 减少了 16%，速度明显更快。

### 概率问题

这个测试产生了唯一的失误。Kimi 在每次运行中都正确回答了所有五个问题。Ember 有四次全部答对。在第五次时，它在第一个问题上犯了一个小的算术失误，得出 0.94619 而不是 0.94629，并且该错误延续到了另外两个答案中。

它还节省了最多的成本。它平均消耗 6,242 个推理 Token，耗时 1 分 47 秒，花费 0.13 美元。Kimi 平均消耗 9,682 个推理 Token，耗时 6 分 48 秒，花费 0.19 美元。这是 Ember 接近其宣传的减少 40% Token 的营销声明的第一次。再一次，Ember 的速度明显更快。

## 结果

|  |  |  |
| --- | --- | --- |
| **测试（每次 5 次运行）** | **Ember-1** | **Kimi K3** |
| 逻辑谜题 | 5/5 完美，3:46，13,630 推理 / 17,766 总输出，$0.27 | 5/5 完美，12:26，16,679 推理 / 22,553 总输出，$0.34 |
| 部署调度 | 5/5 完美，1:29，6,543 推理 / 6,822 总输出，$0.10 | 5/5 完美，4:46，7,792 推理 / 8,365 总输出，$0.13 |
| 概率问题 | 4/5 完美，1:47，6,242 推理 / 8,365 总输出，$0.13 | 5/5 完美，6:48，9,682 推理 / 12,381 总输出，$0.19 |
| 完美运行次数 | 15 次中的 14 次 | 15 次中的 15 次 |
| 总成本，均在 Fireworks 上（$3/$15） | $2.48 | $3.26 |
| 总成本，Kimi 按最低价格（$1/$9） | $2.48（无更便宜的提供商） | $1.96 |

Kimi K3 在 15 次运行中获得了 15 次完美运行，而 Ember-1 是 14 次。Ember-1 的唯一失误是概率测试中的算术失误；在我看来，这似乎并不太重要，因为它是 15 次中的 1 次。

我在测试期间注意到的一点未包含在营销宣传中，即 Ember-1 完成每组测试的速度比 Kimi K3 快 3.4 倍。至于减少推理 Token 的使用，Ember-1 的推理 Token 使用量减少了 23%。这有助于降低成本。总计花费为 2.48 美元，而 Kimi K3 在 Fireworks 上花费为 3.26 美元，这使其便宜了 24%。

需要注意的是，Kimi K3 的成本取决于提供商。在其列出的最低价格（每百万输入 Token 1 美元，每百万输出 Token 9 美元）下，相同的运行只需花费 1.96 美元，低于 Ember-1。

### 我怎么看？

Ember-1 的准确率与 Kimi K3 大致相当，并且使用的推理 Token 少得多。Ember-1 在此测试中的较低成本并不那么重要，因为想要使用 Kimi K3 的用户可以在 OpenRouter 上路由到更便宜的提供商，这会使价格降到 Ember-1 以下。

关于 Kimi K3，我知道的一件事是它很慢。又便宜又慢。不过，我的速度数据来自 Fireworks 的标准端点，我没有测试更便宜的提供商。如果你有时间并且想花更少的钱，Kimi K3 赢了。如果你想以快得多的速度获得与 Kimi K3 几乎相同的结果，请使用 Ember-1。

**提示词**

每个提示词都以固定的答案格式结尾，以便可以进行自动评分。

**逻辑谜题**

*解决以下三个逻辑谜题。每个谜题恰好有一个解。*

*PUZZLE SMALL: 4 engineers (Ava, Bo, Cleo, Dev) each own exactly one server. Each server has a rack position (1, 2, 3, 4, numbered left to right), an operating system (Debian, Alpine, Fedora, Ubuntu), a role (cache, queue, proxy, db). No two servers share any of these values.*

*Clues:*

*If the server in rack 3 runs Fedora, then the Debian server is in rack 3.*

*The server in rack 1 is Dev’s.*

*Exactly one of these is true: the server in rack 4 runs Ubuntu, or the Alpine server is not Bo’s.*

*Cleo is the proxy.*

*The db server is Dev’s.*

*Ava runs Alpine.*

*The queue server is not Ava’s.*

*Bo is in rack 3.*

*Bo and the Ubuntu server are in neighboring racks.*

*PUZZLE MEDIUM: 5 engineers (Ava, Bo, Cleo, Dev, Eun) each own exactly one server. Each server has a rack position (1, 2, 3, 4, 5, numbered left to right), an operating system (Debian, Alpine, Fedora, Ubuntu, Arch), a role (cache, queue, proxy, db, build), a replication data center (Oslo, Lima, Pune, Accra, Perth). No two servers share any of these values.*

*Clues:*

*Cleo is the db.*

*Exactly one of these is true: the cache server runs Arch, or the server replicated to Perth is the proxy.*

*The server in rack 5 runs Fedora.*

*Exactly one of these is true: the server in rack 2 is not the proxy, or Cleo runs Debian.*

*Exactly one of these is true: the server replicated to Pune is the db, or Dev is in rack 3.*

*The server in rack 1 is the db.*

*The proxy server is in rack 5.*

*The server in rack 4 runs Ubuntu.*

*The cache server and the server replicated to Pune are in neighboring racks.*

*Ava is the cache.*

*The server replicated to Accra is the queue.*

*The server replicated to Lima is not in rack 3.*

*Eun runs Alpine.*

*The queue server is not in rack 2.*

*The Fedora server is not Dev’s.*

*The server in rack 2 is not replicated to Lima.*

*PUZZLE LARGE: 7 engineers (Ava, Bo, Cleo, Dev, Eun, Finn, Gia) each own exactly one server. Each server has a rack position (1, 2, 3, 4, 5, 6, 7, numbered left to right), an operating system (Debian, Alpine, Fedora, Ubuntu, Arch, Rocky, NixOS), a role (cache, queue, proxy, db, build, metrics, auth), a replication data center (Oslo, Lima, Pune, Accra, Perth, Quito, Riga). No two servers share any of these values.*

*Clues:*

*The build server is Cleo’s.*

*The proxy server does not run Fedora.*

*The server replicated to Quito is Finn’s.*

*The server in rack 6 is replicated to Lima.*

*The Alpine server is exactly 4 racks to the right of the auth server.*

*The server replicated to Oslo is Dev’s.*

*The Debian server is replicated to Quito.*

*The server replicated to Accra is not the build.*

*The Rocky server is exactly 1 rack to the right of Gia.*

*Exactly one of these is true: the Ubuntu server and the server replicated to Pune are in neighboring racks, or the server replicated to Oslo runs Fedora.*

*The server replicated to Oslo does not run Fedora.*

*Ava runs Rocky.*

*Exactly one of these is true: the proxy server is somewhere to the left of the server replicated to Riga, or the Debian server is in rack 7.*

*The auth server and Bo are in neighboring racks.*

*The metrics server is Gia’s.*

*The Fedora server is somewhere to the left of the server replicated to Pune.*

*Exactly one of these is true: the server replicated to Accra is in rack 2, or Finn is the queue.*

*If the Debian server is Finn’s, then the server in rack 7 does not run Rocky.*

*The NixOS server is not replicated to Perth.*

*The server in rack 7 is replicated to Accra.*

*The server replicated to Pune is the db.*

*At the end of your response, give each solution as a block, one line per engineer, in the order the engineers are listed in that puzzle:*

*SMALL:*

*<name> | <rack> | <os> | <role>*

*MEDIUM:*

*<name> | <rack> | <os> | <role> | <dc>*

*LARGE:*

*<name> | <rack> | <os> | <role> | <dc>*

---

**部署调度**

*You are planning a production rollout of 12 services. Time is measured in whole hours from hour 0.*

*Services (owning team, deploy duration in hours):*

*auth: team A, 3 hours*

*billing: team B, 4 hours*

*catalog: team C, 2 hours*

*search: team C, 3 hours*

*cart: team B, 2 hours*

*checkout: team B, 3 hours*

*payments: team A, 4 hours*

*notify: team C, 2 hours*

*ledger: team A, 2 hours*

*gateway: team A, 3 hours*

*reports: team B, 3 hours*

*inventory: team C, 4 hours*

*Rules:*

*Dependencies. A service may start deploying only after every service it depends on has finished deploying:*

*gateway depends on auth*

*payments depends on auth*

*search depends on catalog*

*cart depends on catalog*

*cart depends on inventory*

*checkout depends on cart*

*checkout depends on payments*

*ledger depends on billing*

*ledger depends on payments*

*notify depends on checkout*

*reports depends on ledger*

*gateway depends on search*

*notify depends on gateway*

*Each team can deploy only one of its services at a time.*

*Different teams can deploy at the same time.*

*Blackout windows. No deploy may be in progress at any time during hours 9 to 11 or hours 17 to 19. A deploy may end exactly at hour 9 or 17, and may start exactly at hour 11 or 19. A deploy cannot pause and resume.*

*Each deploy runs from its start hour for its full duration without interruption.*

*What is the earliest hour by which all 12 services can be finished? Give a schedule that achieves it.*

*At the end of your response, give your answer in exactly this format:*

*MAKESPAN: <hour>*

*<service>: <start hour>*

*(one line per service, all 12 services)*

---

**概率问题**

*A client calls a payment API and retries on failure.*

*The server is in one of two states on each attempt, Healthy or Degraded.*

*On the first attempt, the server is Healthy with probability 4/5 and Degraded with probability 1/5.*

*Between consecutive attempts, the state changes like this: from Healthy, it stays Healthy with probability 3/4 and becomes Degraded with probability 1/4. From Degraded, it stays Degraded with probability 2/3 and becomes Healthy with probability 1/3.*

*An attempt succeeds with probability 9/10 if the server is Healthy and 2/5 if it is Degraded, independently of everything else given the state.*

*The client makes at most 4 attempts and stops as soon as one succeeds.*

*Circuit breaker: if two consecutive attempts both hit a Degraded server and both fail, the client stops immediately and makes no more attempts.*

*Answer these questions with exact fractions in lowest terms:*

*Q1. What is the probability that the request eventually succeeds?*

*Q2. What is the expected number of attempts the client makes?*

*Q3. Given that the request succeeds, what is the probability that it succeeded on exactly the second attempt?*

*Q4. What is the probability that the circuit breaker ends the request early, before the client has used all 4 attempts?*

*Q5. Given that the request succeeds, what is the probability that the first attempt failed?*

*At the end of your response, give exactly five lines in this format:*

*Q1: <fraction>*

*Q2: <fraction>*

*Q3: <fraction>*

*Q4: <fraction>*

*Q5: <fraction>*