<!--
title: Agent Kit 发布：专为 AI 智能体设计的存储工作流
cover: https://www.tigrisdata.com/blog/assets/images/hero-img-58f7f68426b7bcd6174fba2fa2c01ef8.webp
summary: Tigris 推出 Agent Kit，通过分叉、工作区、检查点和协同四大存储原语，解决了 AI 智能体在处理临时数据、状态回溯和流程触发时的复杂性，极大简化了开发流程。
-->

Tigris 推出 Agent Kit，通过分叉、工作区、检查点和协同四大存储原语，解决了 AI 智能体在处理临时数据、状态回溯和流程触发时的复杂性，极大简化了开发流程。

> 译自：[Introducing Agent Kit: Storage Workflows for AI Agents | Tigris Object Storage](https://www.tigrisdata.com/blog/agent-kit/)
> 
> 作者：David Myriel

**[分叉 (Forks)。](#forks)** 仅需一次函数调用，即可为每个智能体提供同一数据集的独立可写副本，只需支付一份存储账单，且完全没有污染源数据的风险。

**[工作区 (Workspaces)。](#workspaces)** 为智能体提供一个无法逃脱的临时存储桶（scratch bucket），并在其 TTL（生存时间）过期时立即停止计费——即使没人记得去清理。

**[检查点 (Checkpoints)。](#checkpoints)** 锁定存储桶历史中的精确时刻，以便在出现问题时重现智能体当时看到的场景，而无需冻结实时数据。

**[协同 (Coordination)。](#coordination)** 在对象落地的瞬间立即触发流水线的下一阶段，无需轮询循环、定时任务或需要持续运行的粘合服务。

[**`@tigrisdata/agent-kit`**](https://www.npmjs.com/package/@tigrisdata/agent-kit) 是一个全新的 TypeScript SDK，专为 AI 智能体实际需要的存储工作流设计。四个原语——分叉、工作区、检查点、协同——每一个都配有 `teardown`（清理）功能，可清理凭据和存储。没有悬挂密钥，没有半配置状态。

Tigris 已经为你提供了基础原语：存储桶、作用域访问密钥、快照、对象通知。Agent Kit 将它们组合成了每个智能体系统最终都会从头开始构建的四个工作流。

## 对象存储与智能体工作流之间的鸿沟[​](#the-gap-between-object-storage-and-agent-workflows "Direct link to The gap between object storage and agent workflows")

对象存储是有意设计为底层的。存储桶是键（keys）的命名空间。上传对象、获取对象、列出前缀下的键。当你构建 CDN 或备份系统时，这个层面是正确的。但当你构建智能体时，这个层面就不合适了，因为你的需求通常听起来像：

* “给我一份训练集的副本。如果智能体搞乱了，就把它扔掉。”
* “创建一个我可以写入的临时存储桶。24 小时后删除它。”
* “立即标记这个存储桶的状态，以便以后回溯。”
* “当有人完成对 `stage-1/` 的写入时，唤醒我。”

每一个需求对 `@tigrisdata/storage` 和 `@tigrisdata/iam` 来说都是三到五个 API 调用。对于 50 个并行运行的智能体，要保证这些代码不出错需要做大量工作。失败往往发生在平凡之处：忘记的访问密钥、未设置的 TTL、悄悄计费一整年的临时存储桶。

[**Agent Kit 是我们对这一差距的回答。**](https://www.tigrisdata.com/docs/ai/agent-kit/) 四个原语与智能体系统的实际结构相匹配，每个原语都由你已有的底层存储和 IAM API 组合而成。

@tigrisdata/agent-kitForksWorkspacesCheckpointsCoordination@tigrisdata/storage@tigrisdata/iam

## 四个原语[​](#the-four-primitives "Direct link to The four primitives")

每个原语都将几个存储和 IAM 调用组合成一个带有对应清理功能的函数。

### 分叉 (Forks)：为每个智能体提供独立的数据集副本[​](#forks "Direct link to Forks: give every agent its own copy of a dataset")

![船队共同出发——每次分叉都会让智能体带着同一数据集的独立可写副本出发。](https://www.tigrisdata.com/blog/assets/images/sailing-d6eae0f3be05ca29b171b3dde6d3538d.webp)

分叉是存储桶的写时复制（copy-on-write）克隆。创建一个分叉，你就会得到一个新的存储桶，它与源桶共享底层数据，但在任何一方写入的瞬间开始分流。50 个分叉并不需要 50 倍的存储成本。它们的成本仅是一倍的存储量加上分叉产生的新增数据量。

源存储桶需要启用快照功能。对于新桶，请使用 `createWorkspace({ enableSnapshots: true })` 或 `tigris buckets create --enable-snapshots`。检查点也有相同的要求。

手动完成这项工作需要一张源桶快照，并且每个分叉需要两次调用——从快照创建存储桶、铸造作用域访问密钥——以及在完成时的一组撤销并删除调用。对于 50 个智能体，这意味着要对 `@tigrisdata/storage` 和 `@tigrisdata/iam` 进行超过一百次 API 调用，每个调用都有你必须处理的错误路径。Agent Kit 在底层仍然执行这些调用——它只是将它们组合起来，所以你只需编写一个函数，而不是围绕它进行编排：

```
import { createForks, teardownForks } from "@tigrisdata/agent-kit";  
  
const { data: forkSet, error } = await createForks("training-data", 50, {  
  credentials: { role: "Editor" },  
});  
if (error) throw error;  
  
  
await Promise.all(  
  forkSet.forks.map((fork) => {  
      
    if (!fork.credentials) return;  
    return runAgent(fork);  
  })  
);  
  
  
await teardownForks(forkSet);  

```

作用域凭据是头等公民

传递 `credentials: { role: "Editor" }` 或 `"ReadOnly"`，Agent Kit 会为每个分叉铸造一个 IAM 密钥，其作用域仅限于该分叉桶。密钥泄露的影响范围会被限制在一个智能体内，而不是整个数据集。

如果批次中的某个分叉创建失败，`createForks` 会停止并返回已成功的那些分叉以及快照 ID，以便你可以重试或清理部分结果。失败分叉的错误不会直接暴露在返回数据中；如果你需要确切知道是哪一个出错，请对调用进行插桩或直接检查快照。清理（Teardown）是尽力而为的：它会在遇到失败时继续执行，并在单个聚合结果中报告所有错误。智能体系统往往会发生部分失败，而该 API 正是围绕这一点设计的。

### 工作区 (Workspaces)：会自动清理的临时存储桶[​](#workspaces "Direct link to Workspaces: scratch buckets that clean themselves up")

![建立滩头阵地——工作区是一个划定的临时存储桶，智能体在进入下一阶段前会向其中写入内容。](https://www.tigrisdata.com/blog/assets/images/beachhead-6ed495ca6289efa9bc3b53b4c3ab567e.webp)

分叉用于在智能体之间共享初始数据集。工作区则用于需要独立空存储桶的智能体——中间输出、生成的伪像、每个会话的状态。可以将这看作分叉与 `mkdir` 的区别：两者都关乎隔离，但一个从数据集开始，另一个从零开始。

```
import { createWorkspace, teardownWorkspace } from "@tigrisdata/agent-kit";  
  
const { data: workspace, error } = await createWorkspace("agent-session-xyz", {  
  ttl: { days: 1 },   
  enableSnapshots: true,   
  credentials: { role: "Editor" },   
});  
if (error) throw error;  
  
  
  
if (!workspace.credentials) {  
    
}  

```

在底层，这仍然是三个调用——创建存储桶、设置 TTL、铸造凭据——具有三个独立的失败模式。Agent Kit 将它们组合在一起，因此你只需编写一个函数并检查一个结果，而无需亲自编排序列。

TTL 字段物超所值

`ttl` 是手动操作时最容易被遗忘的选项，也是它将一次性的智能体运行变成了缓慢泄露的存储账单。在这里设置它意味着即使你从未执行清理，工作区在一天后也会停止计费。

### 检查点 (Checkpoints)：在风险操作前标记存储桶状态[​](#checkpoints "Direct link to Checkpoints: mark a bucket's state before risky work")

当智能体做出令人惊讶的行为时，你想回答的问题是“智能体读取存储桶时，里面有什么内容？”如果没有检查点，你无法回答这个问题。现在的存储桶包含智能体覆盖的内容，以及此间其他人更改的内容。

检查点是具名快照。在进行风险操作前截取一个，然后继续。如果事情出了差错，将检查点还原到一个新的分叉中进行调查。原始存储桶保持不变：

```
import { checkpoint, restore } from "@tigrisdata/agent-kit";  
  
const { data: ckpt, error: ckptErr } = await checkpoint("training-data", {  
  name: "before-fine-tune",  
});  
if (ckptErr) throw ckptErr;  
  
  
  
const { data: investigation, error: restoreErr } = await restore(  
  "training-data",  
  ckpt.snapshotId,  
  { forkName: "debug-fine-tune-attempt" }  
);  
if (restoreErr) throw restoreErr;  
  

```

还原（Restore）使用与分叉相同的写时复制机制，因此即使是 TB 级的存储桶也是瞬间完成的。你可以将同一个检查点还原到多个分叉中，针对它们运行不同的智能体，并对比结果，而无需支付多份数据副本的费用。

### 协同 (Coordination)：基于对象事件触发下一阶段[​](#coordination "Direct link to Coordination: trigger the next stage on object events")

![拔营起锚，信号发出——智能体流水线的每个阶段在完成写入时都会唤醒下一个阶段。](https://www.tigrisdata.com/blog/assets/images/tent-8526863543d711d9635f25f050935a72.webp)

多智能体系统需要一种让各个阶段互相触发的方法，而无需轮询或运行另一个调度器。Tigris 存储桶在对象发生变化时已经会触发 Webhook，Agent Kit 将其封装为一个类似于智能体流水线阶段的原语：

```
import { setupCoordination, teardownCoordination } from "@tigrisdata/agent-kit";  
  
const { error } = await setupCoordination("pipeline-bucket", {  
  webhookUrl: "https://orchestrator.example.com/hook",  
  filter: 'WHERE `key` REGEXP "^results/"',  
  auth: { token: process.env.WEBHOOK_SECRET },  
});  
if (error) throw error;  

```

当任何智能体向该存储桶的 `results/` 写入时，编排器都会收到一个 POST 请求。无需搭建轮询循环或队列；当前一阶段完成写入时，下一阶段就会运行。

Webhook 交付是至少一次的，并在收到 `5xx` 错误时进行重试。请使你的端点具备幂等性，或者让下一阶段根据对象键进行去重。

## 在一次智能体运行中组合原语[​](#composing-the-primitives-in-one-agent-run "Direct link to Composing the primitives in one agent run")

这些原语被设计为可堆叠的。这是一个多智能体评估运行的示例，它锁定了语料库的已知良好状态，为并行运行进行分叉，并在任何智能体提交报告时唤醒编排器：

```
import {  
  createForks,  
  teardownForks,  
  checkpoint,  
  setupCoordination,  
} from "@tigrisdata/agent-kit";  
  
  
  
const { data: baseline, error: ckptErr } = await checkpoint("training-data", {  
  name: "pre-eval-baseline",  
});  
if (ckptErr) throw ckptErr;  
  
  
const { data: forkSet, error: forkErr } = await createForks(  
  "training-data",  
  5,  
  { credentials: { role: "Editor" } }  
);  
if (forkErr) throw forkErr;  
  
  
await setupCoordination("eval-reports", {  
  webhookUrl: "https://orchestrator.example.com/eval-complete",  
  filter: 'WHERE `key` REGEXP "^reports/"',  
  auth: { token: process.env.WEBHOOK_SECRET },  
});  
  
  
await Promise.all(forkSet.forks.map((fork) => runEvalAgent(fork)));  
  
  
  
await teardownForks(forkSet);  

```

这是大多数多智能体运行最终呈现的形式。这些原语保持与其底层的存储和 IAM 调用紧密关联，因此当某个步骤失败时，你可以推断出实际上哪些资源已配置，哪些没有。如果你的智能体不需要初始数据集，只需要空的临时空间，只需将 `createForks` 替换为 `createWorkspace` 即可——生命周期相同，起点不同。

## 哪个原语适合哪种任务[​](#which-primitive-fits-which-job "Direct link to Which primitive fits which job")

使用此表作为快速决策指南：

| 场景 | 原语 |
| --- | --- |
| N 个智能体需要相同的初始数据集但需要进行不同的写入 | 分叉 (Forks) |
| 一个智能体需要一个带有 TTL 的空临时存储桶 | 工作区 (Workspaces) |
| 在风险操作前标记已知良好的状态 | 检查点 (Checkpoints) |
| 当阶段 A 写入某个前缀时，阶段 B 应该运行 | 协同 (Coordination) |

## Agent Kit 在你的技术栈中处于什么位置[​](#where-agent-kit-fits-in-your-stack "Direct link to Where Agent Kit fits in your stack")

LangGraph 有检查点机制。OpenAI Assistants 有线程和文件搜索。Bedrock Agents 有会话内存。**Agent Kit 位于所有这些工具之下的一层** —— 关注的是存储和凭据，而不是状态机或提示词。你的 LangGraph 检查点持久化图状态；而 Agent Kit 检查点则对该图正在读取的存储桶进行快照。你的 OpenAI Assistant 有一个线程；而 Agent Kit 工作区则是该助手写入伪像的私人临时存储桶。请将 Agent Kit 与你已有的任何框架配合使用，而不是取代它们。

## 存储和 IAM 之上的轻薄层[​](#a-thin-layer-over-storage-and-iam "Direct link to A thin layer over storage and IAM")

Agent Kit 是一些组合工作流，位于你已使用的任何框架之下——LangChain、CrewAI、你自己构建的框架，或是尚未出现的工具。它并不试图取代其中任何一个。

目前整个包的 TypeScript 代码不足 600 行。随着我们添加更多组合工作流，设计原则保持不变：每个函数都返回 `TigrisResponse<T>` —— 一个 `{ data }` 或 `{ error }` 的辨别联合类型，无一例外；每个 `create*` 或 `setup*` 都有对应的 `teardown`；配置同时映射到存储和 IAM。

智能体工具往往有过度抽象的习惯：库隐藏了它们的所作所为，这在一切正常时没问题，直到某些环节出错，你需要确切知道哪些 API 调用以什么顺序运行。Agent Kit 保持与原语的亲近，因此每个函数都映射到一个或两个底层的存储或 IAM 调用，让你在发生故障时能够进行推断。

## 安装 Agent Kit[​](#install-agent-kit "Direct link to Install Agent Kit")

```
npm install @tigrisdata/agent-kit  

```

凭据来自环境变量，与 `@tigrisdata/storage` 和 `@tigrisdata/iam` 共享：

```
TIGRIS_STORAGE_ACCESS_KEY_ID=tid_...  
TIGRIS_STORAGE_SECRET_ACCESS_KEY=tsec_...  

```

或者通过任何函数上的 `config` 参数以内联方式传递它们。完整的 API 参考、各原语指南以及失败模式说明都在 [Agent Kit 文档](https://www.tigrisdata.com/docs/ai/agent-kit/)中。

Agent Kit 发布版本为 `0.1.x`。该 API 目前已可用，但在 1.0 版本之前可能会有所演进——如果需要稳定性，请锁定版本。欢迎在 [GitHub](https://github.com/tigrisdata/storage/issues) 上对这些抽象提供反馈。

源码位于 [`tigrisdata/storage`](https://github.com/tigrisdata/storage) monorepo 下的 `packages/agent-kit`，采用 MIT 许可。如果你想添加原语、修复 Bug 或告诉我们抽象有误，欢迎提交 PR。

**为你的智能体提供符合其真实工作方式的存储原语**

安装 @tigrisdata/agent-kit，用四个函数替换上百个 API 调用的繁琐代码。你在 Tigris 上的前 5 GB 存储是免费的。