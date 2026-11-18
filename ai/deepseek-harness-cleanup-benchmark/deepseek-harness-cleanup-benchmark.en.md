![Cleaning up](https://cdn.thenewstack.io/media/2026/11/ca5aed9f-handrush-supply-i8sfnhlttdo-unsplash-1024x724.jpg)

DeepSeek’s open-source coding agent is losing points on a major benchmark for a habit developers usually treat as good practice: cleaning up after itself.

The problem surfaced when Hugging Face harness optimization researcher [Joël Niklaus](https://www.linkedin.com/in/joelniklaus/) added [DeepSeek Harness](https://huggingface.co/spaces/joelniklaus/harness-leaderboard) to his coding-agent leaderboard, which compares ten harnesses running the same underlying models.

DeepSeek Harness is statistically tied for first across the board’s five scored evaluations, yet on Terminal-Bench alone it drops to sixth, because one built-in behavior caused it to fail tasks that competing agents completed.

> DeepSeek Harness is statistically tied for first across the board’s five scored evaluations, yet on Terminal-Bench alone it drops to sixth…

“One habit explains much of that gap,” [Niklaus writes on X](https://x.com/joelniklaus/status/2120540528886603949), referring to the agent’s weaker Terminal-Bench performance.

## A tidy habit backfires

DeepSeek Harness shuts down background processes when a task finishes, which is a problem for three Terminal-Bench tasks that need those processes to keep running.

Niklaus found that DeepSeek Harness passed just two of 36 attempts using DeepSeek-V4.1-Flash and GLM-5.3-Flash, while OpenCode, Pi, and Nous Research’s Hermes Agent passed all 36 on those same tasks.

> DeepSeek Harness passed just two of 36 attempts … while OpenCode, Pi and Nous Research’s Hermes Agent passed all 36 on those same tasks.

That behavior knocked between 1.5 and 1.7 percentage points off DeepSeek Harness’s scores. On DeepSeek-V4.1-Flash at high reasoning effort, it was enough to account for more than the entire 1.3-point gap between DeepSeek Harness and the leader.

The [leaderboard’s changelog](https://huggingface.co/spaces/joelniklaus/harness-leaderboard/blob/main/CHANGELOG.md) confirms that the shutdown behavior belongs to DeepSeek Harness itself and the results were left unchanged.

DeepSeek’s [engineering documentation](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/jobs/jobs-local/README.md) describes its local job registry as a deliberately short-lived component. “Choose it when jobs should live in the harness process and die with it,” it states. Jobs that need to survive restarts or run across processes require a different backend.

## Same model, different results

Niklaus launched his [Harness Leaderboard](https://huggingface.co/spaces/joelniklaus/harness-leaderboard) on November 5 after running 28,849 trials across its original nine harnesses using three open models, DeepSeek-V4.1-Flash, GLM-5.3-Flash and Flint.

He kept the model, provider, and reasoning effort constant while swapping harnesses, and the differences were substantial. Mini-swe-agent, a relatively simple bash-based agent, completed 51.4% of tasks compared with 27.3% for OpenClaw, although several other harnesses were statistically tied with the leader.

Costs varied just as dramatically. Pi achieved a 49.4% solve rate at $0.29 per solved task, while OpenCode cost $3.35 per solved task in the initial evaluation. Hugging Face co-founder [Thomas Wolf](https://www.linkedin.com/in/thom-wolf/) sums up the findings [on X](https://x.com/Thom_Wolf/status/2118863053001531676) as “same open model, different harness => very different results.”

*The New Stack* contacted DeepSeek for comment on the findings but had not received a response by publication time.

## Orchestration isn’t a guarantee

Y Combinator President and CEO [Garry Tan](https://www.linkedin.com/in/garrytan/) has been running [separate evaluations](https://github.com/garrytan/g-harness-evals) using Claude Opus 5.5 and GPT-6.1 Sol.

“[Harnesses differed more on cost than on how often they solved tasks](https://github.com/garrytan/g-harness-evals?tab=readme-ov-file#what-we-found),” the researchers write. On multi-user tasks, OpenClaw running Opus 5.5 cost roughly twice as much per solved task as the other Opus harnesses, largely because it repeatedly sent context with each request.

The project also tested Tan’s gstack workflow skills. In 46 sessions, Opus 5.5 read the instructions but never followed the prescribed steps, and the attempts cost roughly twice as much.

The researchers note that the tasks were relatively easy, so it’s unclear whether following the instructions would have improved the results. The results make a case for testing the harness just as carefully as the model.

> The results make a case for testing the harness just as carefully as the model.

The post [DeepSeek’s coding agent is too tidy for its own good — and benchmarks are punishing it](https://thenewstack.io/deepseek-harness-cleanup-benchmark/) appeared first on [The New Stack](https://thenewstack.io).