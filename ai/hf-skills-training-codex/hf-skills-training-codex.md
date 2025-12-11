<!--
title: Codex 正式开源 AI 模型
cover: https://huggingface.co/blog/assets/hf-skills-training/thumbnail-codex.png
summary: Codex开源AI模型，集成Hugging Face Skills，实现模型微调、评估、报告生成及部署。自动化端到端机器学习实验，减少人工干预。
-->

Codex开源AI模型，集成Hugging Face Skills，实现模型微调、评估、报告生成及部署。自动化端到端机器学习实验，减少人工干预。

> 译自：[Codex is Open Sourcing AI models](https://huggingface.co/blog/hf-skills-training-codex)
> 
> 作者：ben burtenshaw, shaun smith

在我们让 [Claude Code](https://huggingface.co/blog/hf-skills-training) 训练开源模型的工作基础上，我们现在正让 [Codex](https://developers.openai.com/codex/) 走得更远。我们让 Codex 访问了 [Hugging Face Skills](https://github.com/huggingface/skills) 仓库，该仓库包含用于机器学习和 AI 任务（如模型训练或评估）的技能。借助 HF 技能，一个编码智能体可以：

*   对语言模型进行微调并应用强化学习对齐
*   审查、解释并根据 Trackio 的实时训练指标采取行动
*   评估检查点并根据评估结果采取行动
*   从实验中创建报告
*   使用 GGUF 导出模型并进行量化以进行本地部署
*   将模型发布到 Hub

本教程将深入探讨其工作原理以及如何自行使用。那么，让我们开始吧。

> Codex 使用 `AGENTS.md` 文件来完成专门任务，而 Claude Code 使用“技能”。幸运的是，“HF-skills”兼容这两种方法，并可与 Claude Code、Codex 或 Gemini CLI 等主流编码智能体配合使用。

借助 `HF-skills`，你可以告诉 Codex 如下内容：

```
Fine-tune Qwen3-0.6B on the dataset open-r1/codeforces-cots

```

Codex 将会：

1.  验证你的数据集格式
2.  选择合适的硬件（对于 0.6B 模型选择 t4-small）
3.  使用并更新带有 Trackio 监控的训练脚本
4.  将作业提交到 Hugging Face Jobs
5.  报告作业 ID 和估计成本
6.  在你询问时检查进度
7.  如果出现问题，帮助你调试

当你在做其他事情时，模型会在 Hugging Face GPU 上进行训练。完成后，你微调过的模型将出现在 Hub 上，随时可用。

这不是一个玩具演示。该扩展支持生产中使用的相同训练方法：监督微调、直接偏好优化和具有可验证奖励的强化学习。你可以训练 0.5B 到 7B 参数的模型，将它们转换为 GGUF 进行本地部署，并运行结合不同技术的多阶段管道。

## 目标：端到端机器学习实验

我们在 Claude Code 教程中探讨了这种单一提示方法。然而，我们现在可以更进一步，让 OpenAI Codex 进行端到端机器学习实验。例如，Codex 应该能够监控进度、评估模型并维护最新的训练报告。这将使工程师能够将实验委派给 Codex，并以更少干预的方式审查报告。它还将允许 Codex 根据训练报告和评估结果自行做出更多决策。

那么，让我们开始吧！

## 设置和安装

开始之前，你需要：

### 安装 Codex

Codex 是 OpenAI 的 AI 编码智能体，包含在 ChatGPT Plus、Pro、Business、Edu 和 Enterprise 计划中。Codex 将 AI 协助直接引入你的开发工作流程。

请参阅 [Codex 文档](https://developers.openai.com/codex/) 以获取安装和设置说明。

### 安装 Hugging Face 技能

Hugging Face Skills 仓库包含一个 `AGENTS.md` 文件，Codex 会自动检测并使用它。

克隆仓库：

```
git clone https://github.com/huggingface/skills.git
cd skills

```

Codex 将自动检测仓库中的 `AGENTS.md` 文件并加载技能。你可以通过以下方式验证指令是否已加载：

```
codex --ask-for-approval never "Summarize the current instructions."

```

请参阅 [Codex AGENTS 指南](https://developers.openai.com/codex/) 以获取更多详细信息。

### 连接到 Hugging Face

使用 `hf auth login` 命令和来自 [hf.co/settings/tokens](https://huggingface.co/settings/tokens) 的写入访问令牌向 Hugging Face 进行身份验证：

Codex 支持 [MCP（模型上下文协议）](https://developers.openai.com/codex/) 服务器。你可以配置 Hugging Face MCP 服务器以获得额外的 Hub 集成功能。你可以通过将以下内容添加到你的 `~/.codex/config.toml` 文件中，将 Hugging Face MCP 服务器添加到你的 Codex 配置中：

```
[mcp_servers.huggingface]
command = "npx"
args = ["-y", "mcp-remote", "https://huggingface.co/mcp?login"]

```

在 [设置](https://huggingface.co/settings/mcp) 页面中配置 Hugging Face MCP 服务器以使用 Jobs 等相关 MCP 服务器。

然后启动 Codex，你将被引导至 Hugging Face MCP 身份验证页面。

## 你的第一个 AI 实验

让我们来看一个完整的例子。我们将使用 [open-r1/codeforces-cots](https://huggingface.co/datasets/open-r1/codeforces-cots) 数据集和 [openai\_humaneval](https://huggingface.co/datasets/openai/openai_humaneval) 基准，微调一个小型模型以提高代码解决能力。

> `open-r1/codeforces-cots` 数据集是一个包含 codeforces 问题和解决方案的数据集。它是用于指令微调模型以解决硬编码问题的好数据集。

### 指示 Codex 进行端到端微调实验

在你的项目目录中启动 Codex。然后给它一个简单明确的指令：

```
Start a new fine-tuning experiment to improve code solving abilities on using SFT. 
- Maintain a report for the experiment. 
- Evaluate models with the openai_humaneval benchmark
- Use the open-r1/codeforces-cots dataset

```

> 你会注意到，我们比 Claude Code 教程中的单一提示方法更进一步。我们在指令中添加了更多细节，也为实验添加了更多步骤。
>
> 为什么不尝试自己通过更多开放式问题来迭代这个实验，比如“哪个模型最适合代码解决能力？”或“哪个数据集最适合代码解决能力？”

Codex 会分析你的请求并准备训练配置。对于一个演示数据集上的 0.6B 模型，它会选择 `t4-small`——足以满足该模型大小的 GPU，也是可用的最便宜选项。Codex 将在 `training_reports/<model>-<dataset>-<method>.md` 处启动一个新报告，其内容类似于下面的示例。随着实验的进行，Codex 将使用最新信息和每次运行报告来更新该报告。

训练报告示例

```
# Base Model & Dataset
[Base Model](https://huggingface.co/Qwen/Qwen3-0.6B)  
[Dataset](https://huggingface.co/datasets/open-r1/codeforces-cots)

---

# `sft-a10g` - `TBD` - `In Progress`

## Training Parameters
| Parameter | Value |
|-----------|-------|
| Method | SFT (TRL) |
| Model | `Qwen/Qwen3-0.6B` |
| Dataset | `open-r1/codeforces-cots` (train, 5% eval split) |
| Max Length | 2048 |
| Epochs | 1 (extend to 3 after first check) |
| Per-Device Batch Size | 1 |
| Grad Accum Steps | 8 |
| Effective Batch | 8 |
| Learning Rate | 5e-5 |
| Weight Decay | 0.01 |
| Warmup Ratio | 0.03 |
| Eval Strategy | steps (500) |
| Save Strategy | steps (500), `hub_strategy=every_save`, limit=2 |
| Precision | bf16 |
| Gradient Checkpointing | true |
| Packing | false |
| Hub Model | `burtenshaw/qwen3-codeforces-cots-sft` |
| Hardware | a10g-small |
| Timeout | 2h |
| Trackio | project `qwen3-codeforces-cots`, run `sft-a10g` |

## Run Status
In Progress (queued to submit)

## Run Logs
Pending submission (job link will be added)

## Trackio Logs
Pending (will link after job starts)

## Run Evaluations
Pending (lighteval `openai_humaneval` for base + checkpoints)

---

# Experiment Evaluations
| Run Title | Benchmark | Score | Evaluation Job Link | Model Link |
|-----------|-----------|-------|---------------------|------------|
| `sft-a10g` - `TBD` - `In Progress` | HumanEval pass@1 | TBD | TBD | [burtenshaw/qwen3-codeforces-cots-sft](https://huggingface.co/burtenshaw/qwen3-codeforces-cots-sft)

```

### 更新训练报告

随着实验的进行，Codex 将使用最新信息和每次运行报告来更新该报告。你可以在 `training_reports/<model>-<dataset>-<method>.md` 文件中查看报告。

例如，当实验进行中时，Codex 会将报告标题更新为 `sft-a10g` - `TBD` - `In Progress`。

```
# `base-humaneval-a10g` - `2025-12-09 13:47:47 UTC` - `进行中`

```

它可以链接到运行日志和 Trackio 日志。

```
## Run Logs

[Run Logs](https://huggingface.co/jobs/burtenshaw/6938272ec67c9f186cfe1ae3)

## Trackio Logs

[Trackio Logs](https://burtenshaw-trackio.hf.space/?project=qwen3-codeforces-sft&metrics=train/loss&runs=sft-qwen3-codeforces-20251209-175806&sidebar=hidden&navbar=hidden)

```

它将在一个组合表格中更新评估结果。

```
# Experiment Evaluations

| Run Title | Benchmark | Score | Evaluation Job Link | Model Link |
|-----------|-----------|-------|---------------------|------------|
| `base-humaneval-a10g` - `2025-12-09 13:47:47 UTC` - `Completed` | HumanEval pass@1 | 0.304 | [Logs](https://huggingface.co/jobs/burtenshaw/69382863c67c9f186cfe1ae7) | [Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) |
| `qwen3-0.6b-lora-v1` - `2025-12-09 13:47:47 UTC` - `In Progress` | HumanEval pass@1 | TBD | TBD | [burtenshaw/qwen3-codeforces-cots-sft](https://huggingface.co/burtenshaw/qwen3-codeforces-cots-sft)

```

### 数据集验证

数据集格式和处理是训练失败最常见的原因，通常需要在训练脚本中完成大量工作。Codex 可以在作业开始前验证数据集，并为 TRL 定义配置或单独处理数据集。

在大多数情况下，Codex 会在训练前验证数据集，但你始终可以在提交作业前检查数据集验证。

```
Check if open-r1/codeforces-cots works for SFT training.

```

Codex 在 CPU 上进行快速检查（耗费几分钱），并报告：

```
Dataset validation for my-org/conversation-data:

SFT: ✓ READY
  Found 'messages' column with conversation format

DPO: ✗ INCOMPATIBLE
  Missing 'chosen' and 'rejected' columns
```

如果你的数据集需要转换，Codex 可以在训练前对数据集进行预处理。

```
Preprocess the dataset open-r1/codeforces-cots to use 'good_response' and 'bad_response' instead of 'chosen' and 'rejected'.

```

Codex 将预处理数据集并使用新配置更新训练脚本。

### 提交前审查

在 Codex 提交任何内容之前，你将看到配置：

```
I'll fine-tune Qwen/Qwen3-0.6B on open-r1/codeforces-cots using SFT.

Configuration:
- Hardware: t4-small (~$0.75/hour)
- Estimated time: ~20 minutes
- Estimated cost: ~$0.30
- Output: username/qwen-codeforces-cots-sft

The model will be pushed to Hub automatically. Should I submit?
```

这是你调整任何内容的机会。更改输出仓库名称，选择不同的硬件，或要求 Codex 修改训练参数。一旦你批准，作业就会提交。

例如，你可以要求 Codex 尝试一次测试运行：

```
Do a quick test run on 100 examples.

```

### 使用训练报告跟踪进度

提交后，你可以使用训练报告跟踪进度，并获取运行日志和 Trackio 日志的链接。你还可以告诉 Codex 获取日志、总结进度并更新训练报告。随着 Codex 运行作业，它将使用最新信息更新训练报告。

Codex 响应示例

```
─ Worked for 10m 38s ─────────────────────────────────────────────────────────────────────────────────────────────────────────

• Training and eval jobs are live. Key details:

  - SFT launched on open-r1/codeforces-cots (solutions_py_decontaminated, 98/2 split) with LoRA on Qwen/Qwen3-0.6B, a10g-
    large, bf16, max_steps=1000, batch=1, grad_accum=8, lr=2e-5, save/eval every 200 steps, hub push burtenshaw/qwen3-
    codeforces-cots-sft. Job: https://huggingface.co/jobs/burtenshaw/6938272ec67c9f186cfe1ae3 (Trackio project codeforces-
    cots-sft, run qwen3-0.6b-lora-v1).
  - Baseline lighteval (HumanEval) on the base model queued on a10g-large. Job: https://huggingface.co/jobs/
  - Experiment report updated with current runs and links: training_reports/qwen3-codeforces-cots-sft.md.

  To evaluate the fine-tuned checkpoints once the SFT job pushes to the hub, reuse the same lighteval script:
  hf jobs uv run --flavor a10g-large --timeout 1h --secrets HF_TOKEN -e MODEL_ID=burtenshaw/qwen3-codeforces-cots-sft -e
  RESULTS_ORG=burtenshaw -d /tmp/lighteval_humaneval.py
  (or swap MODEL_ID for a specific checkpoint path). This will log to the same results directory on the hub.

  1. Monitor the two running jobs; I can fetch logs or metrics on request.
  2. After a checkpoint lands, trigger the lighteval run above to compare against the baseline; then we can fill in pass@1 in the report.
```

Trackio 将通过运行评估作业并选择最佳检查点来为你监控训练和评估分数。如果你想知道训练作业的状态，你可以要求 Codex 获取日志并在表格中总结进度。

```
Are models outperforming the base model?
```

```
| Model | Benchmark | Score | Evaluation Job Link | Model Link |
|-----------|-----------|-------|---------------------|------------|
| `qwen3-0.6b-lora-v1` - `2025-12-09 13:47:47 UTC` - `Completed` | HumanEval pass@1 | 0.342 | [Logs](<link to training job>) | [burtenshaw/qwen3-codeforces-cots-sft](https://huggingface.co/burtenshaw/qwen3-codeforces-cots-sft)
| `base-humaneval-a10g` - `2025-12-09 13:47:47 UTC` - `Completed` | HumanEval pass@1 | 0.306 | [Logs](<link to evaluation job>) | [Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B)

```

你还可以实时监控训练损失。

![Sweep 测试的 Trackio 仪表板示例](https://huggingface.co/datasets/hf-skills/images/resolve/main/codex-sft-codeforces.png)

*Codex 获取日志并总结进度。*

点击 [此处](https://burtenshaw-trackio.hf.space/?project=qwen3-codeforces-sft&metrics=train/loss&runs=sft-qwen3-codeforces-20251209-175806&sidebar=hidden&navbar=hidden) 查看包含一些已完成运行的 Trackio 仪表板示例。

### 使用你的模型

训练完成后，你的模型将位于 Hub 上：

```
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("burtenshaw/qwen3-codeforces-cots-sft")
tokenizer = AutoTokenizer.from_pretrained("burtenshaw/qwen3-codeforces-cots-sft")

```

Transformers 作为标准库非常出色，我们可以轻松地将训练好的模型转换为 GGUF 以进行本地部署。这是因为训练技能包含将模型转换为 GGUF 的指令和支持脚本。

```
Convert my fine-tuned model to GGUF with Q4_K_M quantization.
Push to username/my-model-gguf.

```

Codex 随后转换为 GGUF，应用量化，并推送到 Hub。如果训练了 LoRA 适配器，它会将 LoRA 适配器合并到基础模型中。

然后在本地使用它：

```
llama-server -hf <username>/<model-name>:<quantization>


llama-server -hf unsloth/Qwen3-1.7B-GGUF:Q4_K_M
```

### 硬件与成本

Codex 根据你的模型大小选择硬件，但了解权衡有助于你做出更好的决策。你可以使用 [硬件指南](https://github.com/huggingface/skills/blob/main/hf-llm-trainer/skills/model-trainer/references/hardware_guide.md) 查看硬件选项和成本，但 Codex 会为你完成此操作并选择最佳选项。

对于 **1B 参数以下的小型模型**，`t4-small` 效果很好。这些模型训练速度快——预计一次完整运行费用为 $1-2。这非常适合教育或实验性运行。

对于 **小型模型 (1-3B)**，升级到 `t4-medium` 或 `a10g-small`。训练需要几个小时，费用为 $5-15。

对于 **中型模型 (3-7B)**，你需要使用 LoRA 的 `a10g-large` 或 `a100-large`。完全微调不适合，但 LoRA 使它们非常可训练。生产预算为 $15-40。

对于 **大型模型 (7B+)**，此 HF 技能作业尚不适用于此规模。但请继续关注，我们正在努力！

## 下一步

我们已经展示了 Codex 可以处理模型微调的整个生命周期：验证数据、选择硬件、生成脚本、提交作业、监控进度和转换输出。

可以尝试以下事项：

*   在自己的数据集上微调模型
*   尝试更大规模的实验，使用更多模型和数据集，并让智能体为你创建报告。
*   使用 GRPO 在数学或代码上训练推理模型，并让智能体为你创建报告。

该 [扩展是开源的](https://hf-learn.short.gy/gh-hf-skills)。你可以对其进行扩展，根据你的工作流程进行自定义，或者将其用作其他训练场景的起点。