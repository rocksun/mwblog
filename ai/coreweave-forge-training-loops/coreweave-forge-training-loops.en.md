![Abstract glowing digital light threads and data particles sweeping across a black background, representing AI training loops.](https://cdn.thenewstack.io/media/2026/11/7a22998e-paris-bilal-gld2k8ozalu-unsplash-1024x768.jpg)

Production traffic shows failures that benchmarks or pre-deployment evaluations can’t fully reveal. It tells you which edge cases matter and what users need. Turning that signal into the next model version requires an upfront decision: does the model need to change, or is the problem in retrieval, context, prompts, tools, or serving?

Changing weights won’t fix a failure elsewhere in the system. When the model is the right place to intervene, [production evidence can improve](https://thenewstack.io/ai-agent-evaluation-loop/) both quality and economics. A smaller model might reproduce a more expensive model’s behavior; better examples might improve consistency; an outcome-based reward might suit the task. [Refining a capable model](https://thenewstack.io/is-fine-tuning-or-prompt-engineering-the-right-approach-for-ai/) can also avoid another migration to a new model generation.

## Choose a technique from the failure mode

Model distillation fits when a stronger model already produces the desired behavior and you want a smaller, more economical model to reproduce it. [Supervised fine-tuning (SFT)](https://www.coreweave.com/products/coreweave-forge/serverless-sft?utm_source=coreweave.com&utm_medium=site) fits when high-quality examples can teach more consistent behavior. [Reinforcement learning (RL)](https://www.coreweave.com/products/coreweave-forge/serverless-rl?utm_source=coreweave.com&utm_medium=site) fits when you can reliably evaluate an outcome but cannot readily specify the ideal response in advance.

> “Changing weights won’t fix a failure elsewhere in the system. When the model is the right place to intervene, production evidence can improve both quality and economics.”

You may use all three approaches over a model’s lifecycle. Choose from the evidence in your workload, even when that means using a technique that takes more setup.

Production traces have to become training data. [Post-training](https://docs.coreweave.com/products/post-training?utm_source=coreweave.com&utm_medium=site) needs [compute and orchestration](https://www.coreweave.com/solutions/ai-model-training?utm_source=coreweave.com&utm_medium=site), and the resulting model has to be evaluated and returned to [inference](https://www.coreweave.com/solutions/ai-inference?utm_source=coreweave.com&utm_medium=site). That is the work of closing [the loop](https://www.coreweave.com/blog/the-ai-loop-launch-day-is-day-one?utm_source=coreweave.com&utm_medium=site). In RL, inference generates rollouts during training, and new weights must return to serving throughout the run.

At [Fully Connected 2026](https://www.coreweave.com/fully-connected-2026?utm_source=coreweave.com&utm_medium=site), we introduced [CoreWeave Model Distillation](https://www.coreweave.com/products/coreweave-forge/model-distillation?utm_source=coreweave.com&utm_medium=site), [CoreWeave RL Rollouts](https://docs.coreweave.com/products/inference/rl-rollouts?utm_source=coreweave.com&utm_medium=site) on CoreWeave Inference, and a programmable training API. These workflows connect in [CoreWeave Forge](https://www.coreweave.com/products/coreweave-forge?utm_source=coreweave.com&utm_medium=site). The programmable API is in limited preview, with an official launch planned for later in 2026.

## Keep the data fresh when the base model stays

CoreWeave Model Distillation provides a managed workflow. [CoreWeave Agent Lens](https://www.coreweave.com/products/coreweave-forge/agent-lens?utm_source=coreweave.com&utm_medium=site) captures inference traffic as the application runs. The workflow turns it into training data, relabels weak outputs, tests base models and hyperparameters, deploys candidates to [Serverless Inference](https://www.coreweave.com/products/coreweave-forge/serverless-inference?utm_source=coreweave.com&utm_medium=site), and compares them with the production model.

If the model already has the capabilities your task needs, fresh production data can improve its fit without changing the serving profile you know. Compare the new version against the model already running before you move traffic.

[Method](https://methodfi.com/?utm_source=coreweave.com&utm_medium=site) used this workflow to revisit a model it had already deployed. In 2024, it used OpenPipe to train Llama 3.1 8B to navigate bank interactive voice response (IVR) systems, using GPT-4o outputs. In August 2026, Method brought in fresh production data, relabeled it with GPT-5.6 Sol, and trained another version. The candidate won 57.5% of head-to-head evaluations against the deployed version.

The base model had not changed. Fresh production data and Model Distillation in Forge made another iteration possible sooner. The 57.5% result is the share of head-to-head evaluations the new version won.

## Control the training recipe in Python

For teams that want to design their own learning process, the programmable training API for Serverless Training separates training logic from infrastructure operations. You write a Python loop; CoreWeave manages the compute and underlying training infrastructure.

Here’s one way to combine RL updates with periodic supervised updates on verified demonstrations. The example creates a learner and serving adapter, uses an Adam optimizer with a learning rate of 1e-5, and publishes updated weights to the sampler after each step.

```

Python
learner = await training.create_learner(model=model, lora=lora)
sampler = await serving.create_adapter(name="sampler")
optimizer = AdamConfig(learning_rate=1e-5)

for step in range(num_steps):
    trajectories = await run_agent(sampler, tasks)
    update = learner.batch()
    update.forward_backward(
        build_rl_batch(trajectories), loss="importance_sampling"
    )
    update.optim_step(optimizer=optimizer)

    if (step + 1) % sft_interval == 0:
        update.forward_backward(next_demo_batch(), loss="cross_entropy")
        update.optim_step(optimizer=optimizer)

    update.publish_weights(to=sampler)
    await update.result()

await (await learner.save_state("final")).result()
await learner.close()

```

The rollout and batch helpers are illustrative. Your agent logic, reward calculations, and data preparation belong in those helpers. The loop uses importance-sampling loss for RL and cross-entropy loss for demonstrations, then waits for the update result. It saves the final learner state and closes the learner.

You choose how often demonstrations enter the loop, how rewards are calculated, and how the recipe evolves. SFT, RL, and distillation share the training primitives, while the platform runs the distributed systems underneath.

[Willow](https://willowvoice.com/?utm_source=coreweave.com&utm_medium=site) began with supervised learning, then added RL scorers to reduce filler words, improve readability, and remove self-corrected phrases. The scorers were combined into a reward function. Lawrence Liu, Willow’s chief technology officer and co-founder, reported better text styling, emoji handling, and responsiveness to commands than in the deployed model.

## Remove checkpoint reload delays from RL

[RL serving](https://www.coreweave.com/solutions/reinforcement-learning?utm_source=coreweave.com&utm_medium=site) needs enough rollout generation, alignment with the policy being trained, and timely weight updates. The trainer, reward logic, and environment can stay where they are while CoreWeave Inference handles this part of the loop.

[CoreWeave RL Rollouts](https://docs.coreweave.com/products/inference/rl-rollouts?_gl=1*130xxj6*_gcl_au*MTMzMTYxMjc2My4xNzg5NDkwMDE3Li0uLS4xNzkyMTU5MDIyLjMxMzA2MzQxMS4xNzkyMTU5MDIzLjE3OTIxNTkwMjI.*_ga*MTc4NDk5MDM5NC4xNzkwODc1MzU0*_ga_XKNHS53VYL*czE3OTI3MDQxOTAkbzM0JGcxJHQxNzkyNzA1NjE1JGozNyRsMCRoMjIzMzMxMQ..) is built on [Nvidia](https://www.nvidia.com/en-us/?utm_source=coreweave.com&utm_medium=site) Dynamo with vLLM support. When the trainer writes a checkpoint, the service hot-loads it into a live deployment while preserving in-flight requests and endpoint availability. It returns training metadata: token log probabilities (logprobs), token IDs, and expert routing for mixture-of-experts (MoE) models.

> “When the trainer writes a checkpoint, the service hot-loads it into a live deployment while preserving in-flight requests and endpoint availability. Serving uses the trainer’s current policy weights, removing staleness and redeployment delays that would otherwise hold up the next batch of rollouts.”

Checkpoints can be full snapshots or incremental deltas, reducing synchronization after the first upload. Serving uses the trainer’s current policy weights, removing staleness and redeployment delays that would otherwise hold up the [next batch of rollouts](https://thenewstack.io/nebius-agentic-rl-training-bottlenecks/).

## Measure quality and infrastructure separately

We validated the workflow with Nvidia and you.com by post-training Nvidia Nemotron 3.5 Lightning for web search. The run combined SFT and RL with [you.com’s search tools](https://you.com/?utm_source=coreweave.com&utm_medium=site) inside the training loop.

BrowseComp accuracy increased from a 36.97% baseline to 45.45%, a reported 22.94% relative improvement. Average tool calls fell 30.24%. Separately, hot-loading checkpoints into a live deployment was approximately 15 times faster than traditional redeployment cycles.

Better search tooling, post-training refinement, and harness improvements worked together to improve accuracy and reduce tool calls. Hot-loading cut the time spent waiting for checkpoint synchronization. If you’re trying to make a smaller or more efficient model competitive with models an order of magnitude larger, that extra training time matters too.

## Keep the model connected to its experiment

[CoreWeave Forge connects production inference](https://forge.coreweave.com/?utm_source=coreweave.com&utm_medium=site), training, and serving again. Model Distillation supplies a managed path. The programmable API lets researchers control the training loop without managing its infrastructure. RL Rollouts supports teams keeping their own trainer while using CoreWeave for rollout inference.

Models produced by serverless training return as tagged artifacts that can move into Serverless Inference without a separate registry handoff. Experiments remain logged beside them, keeping the run, model, and eventual deployment connected.

> “Choose a failure you can reproduce, use it to guide the training method, and compare the candidate with the model serving users.”

Choose a failure you can reproduce, use it to guide the training method, and compare the candidate with the model serving users. Keep the production examples, evaluation, and resulting artifact together so your team can use them again.

The [CoreWeave Forge blog](https://www.coreweave.com/blog/coreweave-forge-turn-ai-iteration-into-compounding-improvement?utm_source=coreweave.com&utm_medium=site) and [announcement press release](https://www.coreweave.com/news/coreweave-forge-launches-turning-the-ai-loop-production-run-into-a-better-model-and-agent?utm_source=coreweave.com&utm_medium=site) provide context on the capabilities introduced at Fully Connected 2026. CoreWeave also plans further engineering explanations of Model Distillation, the programmable training API, and RL Rollouts.

The post [CoreWeave connects custom training loops to model serving](https://thenewstack.io/coreweave-forge-training-loops/) appeared first on [The New Stack](https://thenewstack.io).