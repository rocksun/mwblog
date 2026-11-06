**Together AI is putting AI coding agents to work on the GPU code** that runs its inference infrastructure, automating performance tuning that used to take engineers days or weeks of manual work.

The company unveiled [Together Compiler](https://www.together.ai/blog/together-compiler-continual-compilation-for-ai-inference) on Wednesday, a system that generates, tests, and improves GPU kernels without an engineer directing each experiment, and Together AI says it can deliver gains overnight. The process runs without a person steering each step, but it doesn’t ship anything on its own.

Asked how much people remain in the loop, Together AI tells *The New Stack*, “The optimization loop is autonomous,” adding that “the final evaluations and deployment process are automatic but must be kicked off by a human, who reviews the changes before deploying to production.”

> “The optimization loop is autonomous. The final evaluations and deployment process … must be kicked off by a human, who reviews the changes before deploying to production.”

## Why GPU kernels fall behind

New AI models arrive so frequently that keeping inference infrastructure optimized has become a challenge. Each model has different requirements, and GPU code tuned for one workload may not perform nearly as well on another.

Together AI says 80% of OpenRouter traffic now comes from models released within the past three months. That leaves engineers constantly adjusting code to keep up; now Together Compiler automates much of that work.

Multiple coding agents run experiments simultaneously, writing and testing GPU kernels while sharing results to help guide the next round of improvements.

## Faster testing, more experiments

The company has also found a way to speed up testing. Instead of restarting an inference engine every time an agent changes the code, Together Compiler keeps the engine running and loads new code. According to Together AI, this cuts initialization time from roughly 467 seconds to just nine seconds.

> Instead of restarting an inference engine every time an agent changes the code, Together Compiler keeps the engine running and loads new code.

## Reading the 252x claim

Together AI says its compiler can run 252 times as many optimization experiments as existing agent-based systems. The company tells *The New Stack* that it used Apple’s RSI Inference Bench harness as its baseline, comparing both systems on the same inference workload and hardware, with only the optimization approach changing.

The 252x figure refers to the number of experiments Together Compiler can run compared with Apple’s system, not how much faster the AI models themselves perform.

The company separately reports inference throughput improvements of up to 2.6x compared with published benchmark configurations. Those gains depend on the model and hardware, and the results haven’t been independently verified.

More experiments give Together Compiler more chances to find improvements. And because each test takes less time, the agents can do overnight what might otherwise take engineers weeks of manual tuning.

## Better performance, same cost

Faster inference doesn’t necessarily mean lower prices. Asked whether the performance gains would translate into customer savings or primarily improve its own infrastructure efficiency, Together AI tells *The New Stack*, “Together Compiler improves Together AI’s infrastructure efficiency. For the same dollar cost, customers will get better performance.”

> “For the same dollar cost, customers will get better performance.”

Developers may get more work out of the same GPUs, but that doesn’t always mean lower [per-token prices](https://thenewstack.io/google-frozen-gemini-chip/). The company tells *The New Stack* that customers will get better performance for the same cost, rather than a price reduction.

Together AI says its compiler is already serving trillions of tokens daily. It’s another sign that [coding agents](https://thenewstack.io/gpt-5-6-codex-user-surge/) are moving beyond writing application code and into GPU performance optimization, with engineers reviewing work that agents can now complete overnight.

[AI Engineer
Step by step guide to becoming an AI Engineer in 2026

Introduction
Working With LLMs
Context Engineering
AI Models
Embeddings & Vector Databases
Embedding Models
RAGs
AI Agents
AI Safety and Ethics
Evaluation & Observabiity](https://roadmap.sh/ai-engineer?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=together-compiler-gpu-optimization)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)