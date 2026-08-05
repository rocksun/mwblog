**DeepSeek has launched DeepSeek-V4-Flash-0731**, delivering a significant boost in agent performance without changing the model’s core architecture.

Following an announcement last week, the company made the update available as a public beta through DeepSeek’s API, and the [open weights were published on Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731) under the MIT license later the same day.

Although the model itself hasn’t changed, DeepSeek says additional post-training is responsible for the performance gains, showing that meaningful improvements don’t always require a larger model.

DeepSeek’s decision to release the production-ready weights under a permissive license gives organizations much more control over how they deploy and customize the model.

> Although the model itself hasn’t changed, DeepSeek says additional post-training is responsible for the performance gains, showing that meaningful improvements don’t always require a larger model.

## Same architecture, better results

DeepSeek says V4-Flash-0731 uses the same architecture as the preview release, with 284 billion total parameters and 13 billion activated parameters per token.

This is much smaller than V4-Pro, which has 1.6 trillion total parameters and 49 billion activated parameters. For companies running agents at scale, the activated-parameter gap translates directly into inference cost — [though model price alone doesn’t tell the full story](https://thenewstack.io/agentic-ai-token-costs/).

> Even though it is still the smaller model, DeepSeek says the updated Flash version now beats the earlier V4-Pro preview on several agent-focused benchmarks.

Even though it is still the smaller model, DeepSeek says the updated Flash version now beats the earlier V4-Pro preview on several agent-focused benchmarks.

The company reported 82.7 on Terminal-Bench 2.1, 54.4 on DeepSWE, and 70.3 on Toolathlon-Verified.

## Benchmark claims under scrutiny

Early independent testing by [Artificial Analysis](https://artificialanalysis.ai/articles/deepseek-v4-flash-0731-scores-50-on-the-artificial-analysis-intelligence-index-10-points-above-previous-deepseek-v4-flash) found a lower Terminal-Bench 2.1 score of 79%, which suggests that DeepSeek’s reported numbers may not always match independent results.

DeepSeek also shared results from several internal tests, though they have not yet been independently verified. If those results hold up, they add to growing evidence that companies can get more performance out of existing models through post-training instead of simply making them larger.

## Open weights, full control

The MIT license means organizations aren’t limited to using DeepSeek through its hosted API. The release adds to a trend towards open-weight models closing the gap with [proprietary alternatives](https://thenewstack.io/open-weight-models-frontier-costs/). That flexibility is paired with support for tools many developers already use. V4-Flash now supports the Responses API for building AI agents and multi-step workflows, and DeepSeek has published instructions for integrating the model into [Codex-based development workflows](https://api-docs.deepseek.com/updates/).

## Familiar APIs, lower switching costs

For teams already using OpenAI-style APIs, that lowers the barrier to trying another model because they can evaluate it without making major changes to their existing setup.

The [V4 technical report](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731) also covers inference improvements, like speculative decoding with DeepSeek’s [DSpark framework](https://www.techtimes.com/articles/319236/20260628/deepseek-releases-dspark-speculative-decoding-makes-v4-85-percent-faster.htm), which are designed to make serving more efficient. When combined with self-hosted deployments, these features give infrastructure teams more ways to adjust performance for their own production needs.

This release reflects that companies are now finding new ways to improve model effectiveness without making models larger, and they’re competing on how those models are delivered. While many AI vendors focus on hosted APIs, DeepSeek continues to publish downloadable weights that organizations can run on their own infrastructure. Support for familiar API formats also makes it easier for teams to test open-weight models without revamping present workflows.

> Companies are finding new ways to improve model effectiveness without making models larger, and they’re increasingly competing on how those models are delivered.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)