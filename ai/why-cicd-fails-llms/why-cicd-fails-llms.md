<!--
title: 为何传统CI/CD无法应对LLM（以及我们为此构建的发布门禁）
cover: https://cdn.thenewstack.io/media/2026/07/b731a254-and-machines-4aqekfdyurg-unsplash.jpg
summary: 文章探讨了传统CI/CD在LLM应用中的局限性，并提出了针对LLM管道的发布门禁方案，涵盖基准评估、漂移检测、影子验证及成本/延迟控制，以防止AI生产中的静默退化。
-->

文章探讨了传统CI/CD在LLM应用中的局限性，并提出了针对LLM管道的发布门禁方案，涵盖基准评估、漂移检测、影子验证及成本/延迟控制，以防止AI生产中的静默退化。

> 译自：[Why traditional CI/CD fails for LLMs (and the release gates we built to fix it)](https://thenewstack.io/why-cicd-fails-llms/)
> 
> 作者：Freddy Daniel Alvarez Pinto

这篇文章解释了为什么传统的 CI/CD 门禁对于生产级人工智能系统来说是不够的。我分享了一种针对 LLM 管道的实用发布门禁方法，该方法使用了基准评估、漂移检测、影子验证以及成本/延迟护栏。重点在于预防：基于生产基础设施的平台工程实战经验，在 AI 回归问题到达用户之前将其捕获。

我曾在周五下午部署了一个更新后的 RAG 管道。所有的评估都通过了，相似度得分看起来也很棒，但到了周一早上，系统却在自信地推荐过时的定价数据，原因在于嵌入模型发生了足够的漂移，从而偏向于选择陈旧的数据块而不是最新的数据块。没有触发警报，没有测试失败，仪表板显示为绿色，但输出结果是一堆垃圾。

那一刻，我不再信任“绿色”作为发布信号。我们遇到的不是部署问题，而是发布门禁问题。传统的 CI/CD 是为确定性软件构建的。LLM 是概率性的。我们的门禁也必须如此。

## 为什么传统 CI/CD 在 LLM 管道中会失效

在正常的软件交付中，门禁非常简单：单元测试通过、集成测试通过、安全检查通过，然后部署。它是二元的。构建结果要么是绿色，要么是红色。当你交付的东西是“行为”时，这种模式就会失效。

> “传统的 CI/CD 是为确定性软件构建的。LLM 是概率性的。我们的门禁也必须如此。”

一个生产级人工智能系统今天在相关性上的得分可能是 0.82，明天可能是 0.79，下周可能是 0.74。由于没有任何单次运行会跨越你的失败阈值，即使你的用户已经体验到了更差的回答，也不会有人收到警报。

我在管理生产基础设施、OpenStack 私有云、数据库迁移、CI/CD 管道和任务关键型系统方面拥有超过 20 年的经验。在传统的 DevOps 中，我们了解到，如果一台服务器报告 99.9% 的正常运行时间，但却丢弃了 0.1% 的金融交易，那么它是不健康的。它掩盖了一个 Bug。LLM 评估也是一样的道理。总体得分掩盖了局部失败。

第一种失败模式是评估漂移：得分逐渐退化，但从未严重到足以触发硬阈值。第二种是分布偏移：真实用户提出的问题简短、混乱且奇怪，而你干净的评估数据集从未预料到这些情况。第三种是上下文污染：你检索到的文档发生了变化，但你的测试仍然在问昨天的问题。

传统的 CI/CD 门禁会问：“测试通过了吗？”LLM 发布门禁会问：“行为是否保持在可接受的范围内？”正常的部署门禁比较的是预期输出与实际输出。[AI CI/CD 门禁](https://thenewstack.io/coding-agents-cicd-fix/)则将候选行为与历史行为、生产行为以及成本、延迟和风险进行对比。传统门禁在异常情况下快速失败。LLM 发布门禁则在漂移情况下谨慎失败。

> “传统门禁在异常情况下快速失败。LLM 发布门禁则在漂移情况下谨慎失败。”

这种区别很重要，因为生产级 AI 系统倾向于“腐烂”而不是“爆炸”。

我构建了 `llm-eval-drift-release-gates-AGENT`，因为我想要一个将 AI 发布视为基础设施发布的门禁：可度量、可重复，且尽可能枯燥。枯燥是被低估的品质。它能让工程师睡个好觉。

## LLM 发布门禁的构成

第一个门禁是基准评估套件。它在候选管道上运行一个固定的数据集，并对相关性、忠实度、安全性、依据性以及任何你关心的特定领域检查进行评分。重点不是为了证明模型是完美的。重点是在回归问题变成客户投诉之前捕获它们。

以下是我使用的模式中一个简化的 Python 结构：

```python
from enum import StrEnum
from pydantic import BaseModel, Field

class GateStatus(StrEnum):
    PASS = "pass"
    WARN = "warn"
    BLOCK = "block"

class EvalResult(BaseModel):
    run_id: str
    status: GateStatus
    scores: dict[str, float] = Field(default_factory=dict)
    drift_detected: bool = False
    reason: str | None = None
```

使用 StrEnum 可以保持枚举为字符串原生类型，而不依赖多重继承。这在发布工具中很重要，因为状态值经常被记录、序列化、在 CI 中进行比较或传递到仪表板中。

这可以捕获明显的失败，如相关性崩溃、忠实度下降、不安全输出或格式错误的评估结果。如果评估彻底失败，管道会立即阻断；如果触发警告，则应要求人工审批。我不喜欢静默警告；它们只是穿着体面外衣的未来事故。

第二个门禁是评估漂移检测。固定的阈值是不够的。如果相关性从 0.91 降至 0.86，你的 0.80 阈值会告诉你一切正常。但你的用户可能并不这么认为。

因此，我将当前得分与最近部署的滚动基准进行对比：

```python
def detect_score_drift(
    current: dict[str, float],
    baseline: dict[str, float],
    max_drop_pct: float = 5.0,
) -> tuple[bool, list[str]]:
    failures: list[str] = []
    for metric, base_value in baseline.items():
        current_value = current.get(metric)
        if current_value is None:
            failures.append(f"Missing metric in current run: {metric}")
            continue
        drop_pct = ((base_value - current_value) / base_value) * 100
        if drop_pct > max_drop_pct:
            failures.append(f"{metric} dropped {drop_pct:.2f}%")
    return bool(failures), failures
```

评估套件在周四晚上 11 点检测到了 6% 的相关性下降。如果没有它，这个下降到周一就会影响到 200 个用户。门禁不需要知道业务背景。它不需要。它只需要知道候选版本比上一个已知的良好版本差。

第三个门禁是影子流量验证。在完全发布之前，我会将一小部分真实流量路由到候选管道。用户仍然会获得生产级别的答案，但系统会记录候选版本的输出以进行比较。

这就是应用于 AI 的金丝雀部署。我在基础设施发布中使用了相同的模式，包括我 `eks-canary-deployment-pipeline` 仓库背后的思想。不同之处在于，对于 LLM，你比较的不只是 HTTP 200 状态码。你比较的是回答质量、检索到的上下文、延迟，以及候选版本是否出于可疑原因与生产版本不一致。

判别模型（Judge model）很有用，但我不会让它成为唯一的权威。它产生一个信号。发布策略决定是否通过。

第四个门禁是成本和延迟。一个得分完美但成本高出 3 倍的模型不是一个有效的发布。增加两秒延迟的 RAG 管道也没有准备好。这种思考也塑造了我的 `enterprise-rag-guardrails-costops` 工作。

```python
def enforce_runtime_budget(
    total_tokens: int,
    latency_ms: int,
    max_tokens: int = 8000,
    max_latency_ms: int = 2500,
) -> None:
    if total_tokens > max_tokens:
        raise RuntimeError(f"token budget exceeded: {total_tokens}")
    if latency_ms > max_latency_ms:
        raise RuntimeError(f"latency budget exceeded: {latency_ms}ms")
```

当这些门禁失败时，系统会阻断发布或将其路由至人工审批。我已经学会了在部署期间不要与延迟“讨价还价”。它总是会在后续阶段胜出。

这四个门禁并不能让 LLM 部署变得完美。它们只是让发布带有“绿色徽章”的垃圾产品变得更难了。

## 将其接入你现有的 CI/CD

发布门禁不应该是一个独立的科研项目。如果你的平台团队已经在使用 [GitHub Actions](https://thenewstack.io/github-agentic-workflows-overview/) 或 GitLab CI，那么 LLM 部署管道应该适应现有的工作流。

这种模式刻意保持枯燥：

```yaml
pipeline:
  - build
  - unit-tests
  - eval-baseline
  - drift-check
  - shadow-validate
  - cost-guard
  - deploy
  - post-deploy-monitor
```

这就是我从我的 devsecops-pipeline-github-actions 工作中扩展出来的形状。构建应用程序。运行确定性测试。运行基准评估套件。与滚动基准进行比较。针对影子流量进行验证。检查成本和延迟预算。仅在所有门禁都通过时才部署。

这就是 MLOps 护栏对平台工程师变得有用的地方。你不需要一套独立的部署哲学。你只需要在你团队已经信任的管道中增加一套额外的检查。

这是一个可以从 CI 调用的 Python 入口点示例。重要的细节是，当需要的报告缺失或格式错误时，它会优雅地失败，因为原始堆栈跟踪不是一种发布策略。

```python
import json
import sys
from pathlib import Path

def load_scores(path: str) -> dict[str, float]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    return {key: float(value) for key, value in payload.items()}

current = load_scores("reports/current_eval.json")
baseline = load_scores("reports/baseline_eval.json")
drifted, reasons = detect_score_drift(current, baseline, max_drop_pct=5.0)

if drifted:
    print("LLM release gate blocked:", "; ".join(reasons))
    sys.exit(1)

print("LLM release gate passed")
```

最好的发布门禁是你的团队真正会使用的那个。如果配置它需要 ML 博士学位，那它就不是门禁，而是一堵墙。

我正在攻读云计算安全博士学位，我甚至不想让部署过程变成每周五都要写的论文。门禁应该足够简单，可以在 CI 中运行；足够严格，可以阻断错误的发布；且足够灵活，以避免成为办公室的摆设。

最后这一点我学到的时间比我想承认的要长。

## 我做错了什么，以及我会如何改进

我的第一个版本极其严格。每次部署都被阻断。评估套件会抱怨措辞上的小变动、无害的格式差异以及处于边缘的得分下降。团队开始完全绕过门禁。这是我的错。

一个阻断一切的门禁比没有门禁还要糟糕。至少在没有门禁的情况下，人们知道他们是在冒风险。而在一个糟糕的门禁下，他们学会了无视这个系统。

> “一个阻断一切的门禁比没有门禁还要糟糕。在一个糟糕的门禁下，他们学会了无视这个系统。”

我的第二个错误是仅使用合成查询进行评估。它们很干净、完整且礼貌。真实用户并非如此。真实用户会输入三个词、拼错产品名称、粘贴片段，并期望系统理解他们从未提供过的上下文。

评估结果看起来很棒，但生产环境却并非如此。

我的第三个错误是没有对评估数据集进行版本控制。当我添加新的边缘情况时，我失去了将旧版本与新基准进行比较的能力。现在，我像版本化 Terraform 状态一样版本化评估集：小心翼翼，带有备份，并带有一点点偏执。

从玻利维亚的科恰班巴构建这个系统也影响了设计。我没有无限的云额度来消耗在巨大的评估运行上。这迫使我优化采样，缓存判别模型调用，并将快速 PR 检查与更繁重的每晚检查分离开来。

限制催生了更好的工程设计。很烦人，但这是事实。

## 交付信心，而不仅仅是代码

在传统软件中，我们交付代码并验证行为。在 AI 中，我们交付行为并验证对齐。发布门禁是我们跨越这一鸿沟的方式。

LLM 发布门禁不会消除生产级 AI 系统的不确定性。什么都不会。但它们为平台团队提供了一种实用的方式，可以在用户发现之前捕获评估漂移、分布偏移、上下文污染、成本激增和延迟回归。

这对于 [Agentic 工作流的可靠性](https://thenewstack.io/avoiding-the-ai-agent-reliability-tax-a-developers-guide/)至关重要。这对于 AI CI/CD 至关重要。这至关重要，因为“所有测试通过”已经不再足够了。

我构建了 llm-eval-drift-release-gates-AGENT，因为我厌倦了绿色管道对我撒谎。该仓库是一个开源、离线优先的参考实现，用于这种发布门禁模式。它被刻意设计得足够小，以便在你的 CI/CD 环境中进行检查、运行、破坏和强化。

仓库：<https://github.com/fdaniel-alvarez-dev/llm-eval-drift-release-gates-AGENT>

Fork 它，破坏它，改进它。最糟糕的发布门禁就是你从未构建过的那一个。