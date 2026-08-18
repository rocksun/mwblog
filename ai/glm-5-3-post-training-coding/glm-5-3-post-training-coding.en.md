Z.ai released GLM-5.3 on Friday, a coding and agent model built from the same base model as GLM-5.2. Developers can already use GLM-5.3 through Z.ai’s GLM Coding Plan with Claude Code, Cline, OpenCode and Codex. Direct API access is still listed as “coming soon,” because Z.ai plans to release the model weights after two weeks of hardening and safety testing.

## Post-training did the heavy lifting

Z.ai significantly expanded post-training for GLM-5.3, exposing the model to tenfold more long-horizon task environments while broadening its access to developer tools and engineering workflows.

Some training tasks simulated the full software lifecycle — from identifying bugs and drafting fixes to writing code, running tests and shipping results. [According to Z.ai](https://docs.z.ai/guides/llm/glm-5), single tasks matched the workload of a senior engineer over several days.

> Z.ai concentrated compute on the specific environments the model actually works in.

This makes GLM-5.3 a compelling case study for post-training compute scaling. Z.ai concentrated compute on the specific environments the model actually works in. They are not alone in testing that hypothesis — [DeepSeek recently proved a smaller model could outperform its flagship counterpart](https://thenewstack.io/deepseek-v4-flash-open-weights/) simply by optimizing post-training rather than inflating parameter counts.

## Benchmarks jump, caveats remain

Z.ai claims GLM-5.3 delivers a 50% performance boost over GLM-5.2 on its internal Code Bench, though [self-reported vendor numbers](https://z.ai/blog/glm-5.3) warrant the usual skepticism until the community tests the released weights. On public evaluations, however, the model posts dramatic gains in agentic coding. GLM-5.3 surged to 28.3 on Terminal-Bench 3.0 (up from 4.6), lifted its DeepSWE v1.1 score from 46.2 to 66.9 and edged up from 23.8 to 28.5 on Agents’ Last Exam. That 66.9 on DeepSWE lands right alongside Google’s [Gemini 3.7 Flash (65%)](https://thenewstack.io/gemini-3-7-flash-agents/), though variations in testing harnesses mean head-to-head comparisons should be taken with a grain of salt.

## Longer context comes with several effort levels

With a 1-million-token context window and a 128,000-token completion ceiling, GLM-5.3 accommodates massive codebases. Developers on Claude Code can configure the larger window via the glm-5.3[1m] model tag and a matching 1M-token compaction window.

Reasoning effort is configurable across low, high, and max levels (max enabled by default). Although recommended for non-trivial engineering tasks, max reasoning introduces noticeable latency and token overhead. Teams must evaluate if the downstream accuracy justifies the added compute cost. Z.ai asserts the model optimizes the trade-off between latency, token efficiency, and correctness, but official per-token API pricing has not yet been published.

> While convenient for developers who just want the latest model under the hood, it creates a blind spot for teams trying to run clean A/B comparisons against previous versions on the same plan.

This absence reflects ongoing market recalibration around agent economics. Between [OpenAI’s aggressive price drops](https://thenewstack.io/gpt-5-6-api-price-cuts/) and [Microsoft introducing token caps](https://thenewstack.io/microsoft-copilot-token-budgets/) to mitigate runaway autonomous agents, pricing long-horizon agentic compute remains a moving target. On Z.ai’s Coding Plan, usage is metered via credits: GLM-5.3 carries higher baseline multipliers for input, cached-input, and output tokens compared to GLM-4.7, offset by a 50% off-peak discount.

There is one migration wrinkle worth keeping in mind. According to Z.ai’s documentation, Coding Plan calls to GLM-5.2 or GLM-5.1 are automatically redirected to GLM-5.3. While convenient for developers who just want the latest model under the hood, it creates a blind spot for teams trying to run clean A/B comparisons against previous versions on the same plan. Just be sure to double-check the actual model ID returned by their agent.

## Security gains taper at exploitation

Z.ai is positioning cybersecurity as an emerging strength for GLM-5.3. The model scored 84.5% on CyberGym, up from 77.2% for GLM-5.2. Z.ai reports that this narrowly exceeded Mythos 5 at 83.8% and GPT-5.6 Sol at 83.6%.

GLM-5.3 did not perform as well when it had to exploit the vulnerabilities it found. Its ExploitBench score more than doubled from 24.4% to 54.4%, but it still trailed Mythos 5 at 78% and GPT-5.6 Sol at 76.5%. The results follow a pattern seen across frontier AI labs: [OpenAI recently built a model specifically for cybersecurity work](https://thenewstack.io/openai-gpt56-cyber-daybreak/) and [delayed the release of another over concerns about what its offensive capabilities could do in the wild](https://thenewstack.io/openai-astra-cybersecurity-delay/).

Z.ai acknowledges that the model is currently stronger at the earlier stages of the exploitation chain, including reviewing source code and verifying vulnerabilities, than at completing deeper offensive security tasks. But take those high white-box review scores with a grain of salt. As you know, reliably crafting an exploit, proving real-world reachability in production, or patching the flaw without triggering downstream regressions is an entirely different challenge altogether.

> Reliably crafting an exploit, proving real-world reachability in production, or patching the flaw without triggering downstream regressions is an entirely different challenge altogether.

## **Weights arrive in two weeks**

GLM-5.3 can already be selected in the GLM Coding Plan through Anthropic-compatible and OpenAI-compatible endpoints. Users can connect it to Claude Code, Codex, or another agent that supports custom model configuration. [Z.ai’s model-switching guide](https://docs.z.ai/devpack/latest-model) provides the required endpoints and settings.

The more consequential release is scheduled for two weeks from now. Once the weights are available, developers will be able to test whether the benchmark improvements carry over to local deployments, different inference stacks, and repositories that were not selected by Z.ai. That wait is familiar — [Moonshot released Kimi K3’s weights under similar conditions](https://thenewstack.io/kimi-k3-open-weights/), and the gap between “open weights announced” and “weights you can actually run” has become a recurring pattern in the open-model space.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)