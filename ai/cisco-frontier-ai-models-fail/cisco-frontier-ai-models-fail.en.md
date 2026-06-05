The safety benchmarks enterprise buyers rely on to evaluate AI models are measuring the wrong thing.

That’s the finding from recent [Cisco](https://thenewstack.io/cisco-is-using-ebpf-to-rethink-firewalls-vulnerability-mitigation/) research pairing single-turn and multi-turn evaluations across 15 closed frontier models from [OpenAI](https://thenewstack.io/openai-launches-gpt-5-5-calling-it-a-new-class-of-intelligence/), [Anthropic](https://thenewstack.io/anthropic-agent-sdk-confusion/), [Google](https://thenewstack.io/is-ai-the-ultimate-version-of-google-as-larry-page-wanted/), [Amazon](https://thenewstack.io/amazon-ai-assisted-errors/), and [xAI](https://x.ai/).

Every model failed a non-trivial share of multi-turn attacks, and the success rates of those attacks ranged from 7.89% to 88.30% across the cohort — a wider spread than the single-turn range of 2.19% to 64.91%.

Single-turn is a one-and-done interaction. Multi-turn is a continuous back-and-forth dialogue.

“Multi-turn evaluation matters for one primary reason: it is where attackers operate,” the report states. “Real adversaries iterate, reframe refusals, decompose tasks across turns, adopt personas, and escalate gradually.”

## Single-turn scores don’t tell the story

The most consequential finding isn’t the raw numbers; it’s that single-turn performance is a poor predictor of multi-turn resilience. Cross-regime deltas swung as high as 55 percentage points in both directions.

[Gemini 3 Pro](https://thenewstack.io/google-launches-gemini-3-pro/) moved from 18.10% single-turn attack success rate (ASR) to 73.35% under iterative attack — a fourfold increase. [OpenAI’s GPT-5.4](https://thenewstack.io/openai-gpt-5-4-ai-jobs-report-anthropic-dow-supply-chain-risk/), which posted a strong-looking 2.74% single-turn ASR, reached 24.68% under multi-turn pressure, a ninefold jump. [Grok 4.1 Fast](https://x.ai/news/grok-4-1-fast) in its non-reasoning configuration hit 88.30% multi-turn ASR despite a 34.15% single-turn baseline.

The [Anthropic Claude](https://thenewstack.io/anthropic-launches-claude-opus-4-and-sonnet-4/) family performed best overall in multi-turn conditions, with ASRs ranging from 11.16% to 16.20% under iterative attack — still elevated from single-turn baselines of 2.19% to 3.64%, but well below most of the cohort, the report shows.

[Amazon’s Nova](https://thenewstack.io/aws-updates-its-nova-models-to-compete-with-google-anthropic-and-openai/) variants produced the most counterintuitive result. All three moved in the opposite direction from most models: high single-turn failure rates but lower multi-turn ASR. Nova 2 Lite posted a 34% single-turn ASR yet achieved the lowest multi-turn ASR in the cohort at 7.89% — the clearest case of single-turn brittleness that doesn’t translate into iterative exposure.

## One configuration flag, 45 points of difference

Perhaps the most operationally significant finding involves Grok 4.1 Fast. When tested under identical conditions, enabling reasoning mode dropped multi-turn ASR from 88.30% to 43.47% — a 44.83 percentage-point swing due to a single configuration change.

Cisco says this kind of configuration-driven safety variation isn’t captured by any public benchmark or model card it’s aware of and argues that AI providers should disclose safety-relevant effects of deployment-time settings alongside capability benchmarks.

## Where failures concentrate

Not all attack strategies are equally effective, and not all models fail the same way, the report indicates. Cisco decomposed multi-turn outcomes across five attack strategy families. Within each, the spread between the most- and least-exposed models ranged from 79 to 89 percentage points, meaning aggregate scores can hide per-strategy vulnerabilities.

On the single-turn side, failures concentrated in a small set of procedures. Imposter AI attacks led at 37.50% weighted ASR — more than 14 percentage points above the tenth-ranked procedure. Soft Paraphrase and System Prompts followed. On the content side, Hate Speech, Profanity, and Specialized Advice dominated.

## What enterprises should do

Cisco translates its findings into three practical recommendations:

* First, AI providers should publish attack success rates, broken down by strategy family, with every model release.
* Second, enterprise deployment gates should include regression tests for the highest-risk procedures and content types, with a 3-percentage-point threshold that triggers review.
* Third, any model with more than a 15-percentage-point gap between single-turn and multi-turn ASR should require manual review before deployment — a rule that would have flagged eight of the 15 models in this cohort.

One important caveat: Cisco tested base models *without* system prompts, content filters, or custom orchestration, and real enterprise deployments typically include those controls, which could shift outcomes in either direction.

The broader message is that “Safety remains a continuous, regime-dependent property rather than a binary certification,” the report concludes, “even for frontier models from leading providers.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)