# The New Shadow IT: LLMs in the Wild
A few months ago, a platform engineer at a mid-sized fintech wired OpenAI into a Terraform pipeline. He didn’t try to hide it. He just wanted to tag cloud resources automatically, and the LLM handled it better and faster than anything the team had built internally. But when security caught wind of it? Audit panic. Risk review. Retroactive approvals. Sound familiar?

LLMs now represent the new shadow IT. They’re slipping into environments faster than most orgs can track.

Shadow AI means developers integrate [large language models](https://thenewstack.io/what-is-a-large-language-model/) (LLMs) or GenAI systems into production workflows without approval. They test [prompts on live customer data](https://thenewstack.io/with-leftoverlocals-gpus-can-leak-llm-prompt-data/), call OpenAI from rogue scripts, and spin up fine-tuned models on GPU clusters without informing security or governance. While [developers may not intend to introduce risk](https://thenewstack.io/are-your-development-practices-introducing-api-security-risks/), these actions entirely bypass visibility, controls, and policy.

Why does this keep happening? Because [devs don’t need permission to install a Python](https://thenewstack.io/why-every-python-dev-needs-virtual-environments-now/) package. Because using an API key is easier than submitting a Jira ticket. Because the AI works. And that’s the part no one wants to say: these tools are often more helpful than the sanctioned alternatives.

We’ve seen LLMs used to auto-tag infrastructure, classify alerts, generate compliance doc stubs, and spin up internal search tools on top of knowledge bases. We’ve also seen them quietly embedded into CI/CD workflows, buried inside scripts no one else reviews. Sometimes, they even make it into production pipelines without anyone flagging the dependencies. These aren’t hypothetical edge cases — they happen at every company we talk to.

Shadow AI isn’t just a developer cutting corners. It’s a signal. It tells you where your tooling is too slow, too rigid, or just plain missing. But you lose trust if you ignore it — or worse, try to clamp down without offering alternatives. You push that activity deeper underground. And eventually, you pay for it with a breach, an audit failure, or a support nightmare when no one knows how that prompt pipeline works.

The risks are real. Developers can leak PII or proprietary logic by sending prompts to external APIs. They can create model sprawl — zombie workflows no one owns or maintains. They can introduce invisible dependencies that silently drift between environments. And they do it with zero logging, no review process, and no audit trail.

Some orgs are starting to catch up. They’ve built detection rules that flag outbound traffic to OpenAI or Anthropic. They scan for model APIs in [source code or suspicious runtime](https://thenewstack.io/new-open-source-runtime-for-web-developers-uses-p2p/) behavior. They look at telemetry patterns and trace anomalies that resemble prompt usage. Sometimes, they even bake LLM observability into cloud security tools or EDR platforms. It’s early, but it’s starting to happen.

The most mature teams go beyond point detections. They map where AI workloads run, what they do, and how they interact with sensitive systems and data. They build visibility not just into when a model runs, but who built it, where it lives, and whether it aligns with policy. This is how you move from whack-a-mole reaction to sustainable governance. If you can see where AI is being used, you can manage it, guide it, and bring it into the fold without killing innovation.

Still, detection alone doesn’t solve the problem. If your only move is to shut things down, you’ll alienate the developers trying to solve real problems. A more brilliant strategy offers guardrails, not roadblocks. Provide secure, internal gateways to approved models. Spin up sandboxes with observability built in. Give teams a way to experiment with AI that doesn’t leave them exposed — or invisible.

You’ll still need policy. You’ll still need oversight. But if you create reasonable defaults, people will use them. If you lead with control, they’ll route around you.

LLMs are already part of your stack, whether you planned for them or not. They’re embedded in scripts, pipelines, and workflows across your org. You can’t stop developers from using LLMs. But you can ensure you’re not the last one to find out.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)