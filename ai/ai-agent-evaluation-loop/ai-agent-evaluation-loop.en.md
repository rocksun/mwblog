**Your agent is live. The service is healthy. But are its answers getting better?** By connecting production traces, curated data, and evaluations, your team can find failures, choose improvements, and prove the next version works before it reaches users.

A first deployment is still a milestone. Then the hard questions begin: How do we keep outputs accurate and customers happy? What will it cost us? After a few iterations, teams can spend more time maintaining tools and coordinating handoffs than improving the application itself.

## Find the gaps between teams

Consider what happens when the AI engineers who trained a model hand it off to an application or site reliability engineering (SRE) team. The engineers understand what “good” looks like; the production team owns the running service. From there, they may look at different systems.

Application traces land in a dashboard built for uptime. The on-call engineer sees a healthy service, while the research team learns little about answer quality or user sentiment. The evaluation suite drifts as user behavior changes, but no one owns refreshing it. Researchers, AI engineers, and business leads return to separate dashboards for the next release.

> The on-call engineer sees a healthy service, while the research team learns little about answer quality or user sentiment.

Start by asking who can turn a production failure into an evaluation case, and who owns keeping that case current. If the answer requires copying context between teams, that’s where you’re lost in the handoffs..

## Connect the five stages of improvement

The [AI loop](https://www.coreweave.com/blog/the-ai-loop-launch-day-is-day-one?utm_source=coreweave.com&utm_medium=site) follows a familiar cycle: run a model or agent, observe its behavior, curate the signal into data, improve the system, evaluate the result, and repeat. Each stage needs to carry enough context for the next team to act.

**Run**. Choose the model and agent harness — the code and tools around the model — for the workload. Capture the signals you will need to investigate behavior after deployment.

**Observe**. Look beyond availability. Capture traces, metrics, tool usage, and behavioral feedback so you can examine an agent’s decisions and identify where a run went wrong.

**Curate**. Turn production examples into useful datasets and refreshed evaluation suites. Keep human review in the process, and preserve the lineage that explains where an example came from.

> A release should show what improved, rather than rely on a few promising answers.

**Improve**. Match the change to the failure. You might adjust the harness, switch models, or refine behavior through [reinforcement learning](https://www.coreweave.com/solutions/reinforcement-learning?utm_source=coreweave.com&utm_medium=site) (RL), [supervised fine-tuning](https://www.coreweave.com/products/coreweave-forge/serverless-sft?utm_source=coreweave.com&utm_medium=site), or model distillation. Define the quality, latency, or cost outcome you expect.

**Evaluate**. Compare the candidate against repeatable standards before, during, and after deployment. A release should show what improved, rather than rely on a few promising answers.

## Keep the record with the work

These handoffs shaped our approach to [CoreWeave Forge](https://www.coreweave.com/products/coreweave-forge?utm_source=coreweave.com&utm_medium=site), which we announced last week at our [Fully Connected 2026 conference](https://www.coreweave.com/fully-connected-2026). We designed it to connect running, observing, curating, improving, and evaluating in one development environment. [MasterClass](https://www.coreweave.com/news/coreweave-ai-cloud-platform-powers-masterclasss-ai-teaching-agents?utm_source=coreweave.com&utm_medium=site) and Canva are starting to use Forge to complete their AI loop.

The useful test for a connected environment is whether you can trace a deployment back to its model version, evaluation, dataset, and production examples. [CoreWeave Registry](https://coreweave.com/products/coreweave-forge/registry) manages models, agents, and datasets; [Weights & Biases Models](https://www.coreweave.com/products/coreweave-forge/weights-and-biases-models?utm_source=coreweave.com&utm_medium=site) tracks experiments, hyperparameter sweeps, analysis, and automated workflows. Together, those records help teams understand what changed and whether it improved results.

For observation, [CoreWeave Agent Lens](https://www.coreweave.com/products/coreweave-forge/agent-lens?utm_source=coreweave.com&utm_medium=site) traces steps, decisions, and tool calls, with conversation views and technical detail. Monitors score live traffic with human oversight and curation. Our [launch post](https://coreweave.com/blog/coreweave-forge-turn-ai-iteration-into-compounding-improvement) reports Agent Lens improves failure detection by 20% and fixes issues at half the cost; teams should assess those results against their own workloads.

[CoreWeave Notebooks](https://www.coreweave.com/products/coreweave-forge/notebooks?utm_source=coreweave.com&utm_medium=site) provides managed Python notebooks for shared evaluations and custom analytics. [CoreWeave ARIA](https://www.coreweave.com/products/coreweave-forge/aria?utm_source=coreweave.com&utm_medium=site) analyzes runs, proposes experiments, and recommends code changes stored in GitHub. Its integration with Weights & Biases Models supports autoresearch based on detected signals. Keep the evaluation evidence alongside any proposed change so the team can judge the result.

[CoreWeave Sandboxes](https://www.coreweave.com/products/coreweave-forge/sandboxes?utm_source=coreweave.com&utm_medium=site) provides isolated central processing unit (CPU) or graphics processing unit (GPU) environments for agents, tool calls, RL, and evaluations. CoreWeave ARIA and CoreWeave Sandboxes are generally available; Agent Lens, Notebooks, and Model Distillation in preview and part of CoreWeave Training) are new in CoreWeave Forge.

## Choose the improvement your workload needs

Post-Training uses production signals to improve model quality, latency, and cost without requiring a training cluster. [Serverless SFT (supervised fine-tuning)](https://www.coreweave.com/products/coreweave-forge/serverless-sft?utm_source=coreweave.com&utm_medium=site) and [Serverless RL (reinforcement learning)](https://www.coreweave.com/products/coreweave-forge/serverless-rl?utm_source=coreweave.com&utm_medium=site) let teams experiment with their own training recipes.

For a task already proven in production, [Model Distillation](https://www.coreweave.com/products/coreweave-forge/model-distillation?utm_source=coreweave.com&utm_medium=site) trains a smaller, open-weights model on the larger model’s outputs. It then scores the candidate head-to-head against the incumbent. That comparison gives you evidence for deciding whether to move traffic. A smaller model is useful only if it meets the task’s requirements.

## Treat inference as part of the loop

Every stage depends on inference, but workloads need different levels of control. [CoreWeave Inference](https://www.coreweave.com/solutions/ai-inference?utm_source=coreweave.com&utm_medium=site) offers [Serverless Inference](https://www.coreweave.com/products/serverless-inference?utm_source=coreweave.com&utm_medium=site) for accessing open-weights models and [Dedicated Inference](https://www.coreweave.com/products/dedicated-inference?utm_source=coreweave.com&utm_medium=site) for workloads on isolated infrastructure.

With [Serverless Inference](https://www.coreweave.com/solutions/ai-inference?utm_source=coreweave.com&utm_medium=site), CoreWeave manages the infrastructure. With [Dedicated Inference](https://www.coreweave.com/solutions/ai-inference?utm_source=coreweave.com&utm_medium=site), teams control model weights, deployment settings, and GPU resources. Choose based on the workload’s requirements; teams can move between the approaches as those requirements evolve.

[Cline](https://cline.bot/?utm_source=coreweave.com&utm_medium=site) uses open-source models in Serverless Inference for its open-source, open-choice coding agent, which our [launch post](https://coreweave.com/blog/coreweave-forge-turn-ai-iteration-into-compounding-improvement) describes as trusted by more than 11 million developers. [Grammarly](https://www.grammarly.com/?utm_source=coreweave.com&utm_medium=site) uses Dedicated Inference with explicit GPU selection and fully managed operations.

RL adds another requirement. The policy generates rollouts — examples of its behavior — training produces updated weights, and those weights return to serving for the next round. Slow checkpoint loading slows the whole cycle.

Our new [RL rollouts](https://docs.coreweave.com//products/inference/rl-rollouts?utm_source=coreweave.com&utm_medium=site) feature in Dedicated Inference uses the NVIDIA Dynamo foundation to hot-load updated checkpoints with minimal downtime. We partnered with NVIDIA and you.com’s engineering team to post-train NVIDIA Nemotron 3.5 Lightning using RL Rollouts in NeMo gym with you.com’s web search application programming interface (API). Our [launch post](https://coreweave.com/blog/coreweave-forge-turn-ai-iteration-into-compounding-improvement) reports a 15-fold improvement in model reload latency against baseline.

## Keep the loop open to your stack

An improvement loop reaches into the observability platform, data warehouse, and security stack you already use. [The CoreWeave Partner Network](https://www.coreweave.com/coreweave-partner-network?utm_source=coreweave.com&utm_medium=site) includes infrastructure, data services, independent software vendors (ISVs), and models and inference, with solutions tested on CoreWeave under production conditions.

That includes tools agents call. [Exa](https://exa.ai/?utm_source=coreweave.com&utm_medium=site), [Parallel Web Systems](https://parallel.ai/?utm_source=coreweave.com&utm_medium=site), and [You.com](http://you.com/?utm_source=coreweave.com&utm_medium=site) provide a live web search layer through one integration. Search gives an agent access to information beyond its training data; you still need to observe and evaluate its tool calls and resulting answers.

We built [CoreWeave Forge](http://forge.coreweave.com/?utm_source=coreweave.com&utm_medium=site) for teams with workloads on CoreWeave Cloud, other clouds, and private data centers. Improvement data stays portable, with open interfaces between stages, so curated datasets and evaluation suites can remain useful wherever you run.

## Start with one production failure

Pick a failure your team understands. Follow it from trace to curated example, proposed fix, evaluation, and deployment. Record where context disappears and where ownership is unclear. That gives you a concrete starting point for connecting the loop.

To test that workflow, CoreWeave Forge offers a [30-day Pro free trial](https://id.coreweave.com/signup?utm_source=coreweave.com&utm_medium=site) with credits across product lines. For those interested in proving production workloads with direct access to CoreWeave experts and infrastructure, try [CoreWeave ARENA](https://www.coreweave.com/coreweave-arena?utm_source=coreweave.com&utm_medium=site). The goal is to make each deployment feed what you build next, with evidence that the next version improves on the last.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/10/25080c29-cropped-209029e1-67db33f24c8d74c7d3b1e685_team-member_chen-goldberg@2x-600x600.avif)

Chen Goldberg is Executive Vice President of Product and Engineering at CoreWeave, where she leads the teams building the full-stack platform that is reimagining cloud computing in the AI era. Her focus spans the software, tooling, and infrastructure innovations that...

Read more from Chen Goldberg](https://thenewstack.io/author/chen-goldberg/)