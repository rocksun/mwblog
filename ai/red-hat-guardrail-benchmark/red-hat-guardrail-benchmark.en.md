**Guardrail selection has typically meant choosing between a purpose-built classifier** and an LLM acting as a judge. Decision models such as TypeSafe AI’s Jev have added a third option, promising the flexibility of zero-shot policies without the cost of open-ended generation.

TypeSafe launched Jev in mid-September with performance claims based on evaluations it designed and ran itself. Red Hat’s AI Safety team has now [put all three approaches through the same benchmarks](https://developers.redhat.com/articles/2026/10/02/benchmarking-ai-decision-models-against-traditional-guardrails). It tested nine guardrail configurations on prompt injection and content safety, running each through NVIDIA’s open source [NeMo Guardrails](https://thenewstack.io/nvidia-launches-ai-guardrails-llm-turtles-all-the-way-down/) toolkit. And the first result was actually pretty close.

[Qwen3.6-35B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B-FP8), used as an LLM judge, topped that test with 89.31% accuracy. Red Hat’s [DeBERTa-based prompt-injection classifier](https://huggingface.co/RedHatAI/deberta-v3-base-prompt-injection-v2), which has roughly 200 million parameters, finished second at 89.01%. Qwen3.6-35B is a mixture-of-experts model with about 3 billion parameters active per token; however, the 175x figure overstates the difference in inference compute.

The latency results separated the two far more clearly. Red Hat’s main results table puts DeBERTa at a median of 54.1 milliseconds, compared with 312.5 milliseconds for Qwen and 348.1 milliseconds for Jev, which reached 86.35% accuracy. On prompt injection, the small classifier matched the largest model in the test almost point for point while returning its decision in a fraction of the time.

> On prompt injection, the small classifier matched the largest model in the test almost point for point while returning its decision in a fraction of the time.

The content-safety benchmark reversed the leaderboard order. Jev led at 86.20%, followed by DiffusionGemma, an open source Jev-style model [served through vLLM](https://developers.redhat.com/articles/2026/09/28/run-decision-model-vllm-and-red-hat-ai), at 85.53% and Qwen at 85.47%. Red Hat’s 125-million-parameter [Granite Guardian classifier](https://huggingface.co/RedHatAI/granite-guardian-hap-125m) finished sixth at 80.27%, about six points behind Jev, though it remained the fastest option with a 33.2-millisecond median.

Red Hat plans to ship both classifiers as the default guardrail configurations in OpenShift AI 3.6, which gives the company a stake in how they compare. Its authors acknowledged that the content-safety result also points to a need for better small predictive models in that category.

## Where decision models pull ahead

Decision models are pitched as a way to keep an LLM’s flexibility for classification without paying to generate tokens the application never uses. Jev takes the application’s state and a set of typed questions, then returns typed answers, such as a probability between 0 and 1.

The content-safety benchmark is where that approach paid off. Red Hat’s policy covered prejudice, violence, profanity, illegal activity, sexual content, and pretexts such as role play, a much broader mix of risks than prompt injection, and both Jev and DiffusionGemma beat the purpose-built Granite classifier on it by more than five points.

Red Hat stopped short of endorsing decision models as a replacement for LLM judges. Qwen posted lower median latency than Jev on both benchmarks in Red Hat’s setup. NVIDIA’s 4-billion-parameter [Nemotron-3.5-Content-Safety](https://huggingface.co/nvidia/Nemotron-3.5-Content-Safety), running Red Hat’s custom policy, trailed Jev on content safety by 1.13 percentage points while responding faster.

> The open source alternatives also weaken the case for Jev in particular.

The open source alternatives also weaken the case for Jev in particular. DiffusionGemma came within 0.67 percentage points of Jev on content safety and beat it on prompt injection, 87.72% to 86.35%. [Laya](https://huggingface.co/convaiinnovations/laya), an open source decision model with about 421 million parameters that Red Hat ran on a laptop CPU, posted 85.44% on prompt injection, though its results on content-safety were heavily dependent on the way the policy was written.

## Prompts still shape accuracy

Nemotron’s prompt-injection accuracy jumped from 69.37% to 84.84% when Red Hat replaced NVIDIA’s default risk definitions with its own. Laya swung even further on content safety, scoring 57.87% under Red Hat’s original policy and 75.20% after the team tuned a policy specifically for it. That same tuned policy lowered Jev’s content-safety accuracy from 86.20% to 82.53%.

A policy that recovered nearly 18 points for one decision model cost another 3.67 points on the same benchmark. That makes any single position on the leaderboard hard to take at face value. Red Hat noted that its original risk definitions were adapted from prompts that had worked well for LLM judges and may not suit zero-shot classifiers. SkipLabs founder Julien Verlaguet told *The New Stack* earlier this year that [many AI guardrail claims amount to better prompting](https://thenewstack.io/skiplabs-ai-guardrails-skipper/), and Red Hat’s numbers suggest the prompt still does much of the work for decision models.

## Latency depends on deployment

Red Hat’s latency figures measure more than inference speed. The team ran its pretrained classifiers, Laya and BART-large-mnli, on a MacBook Pro M1 CPU. Qwen, Nemotron, Shieldstral and DiffusionGemma ran through vLLM on GPU nodes with 96 GB of VRAM in a U.S. East Red Hat OpenShift Service on AWS cluster, and Jev was called through TypeSafe’s API. Because the benchmark ran from the United Kingdom, every hosted model absorbed a transatlantic network hop that Red Hat estimates added at least 56 milliseconds per request.

Subtracting that estimate from Qwen’s median still leaves roughly 256 milliseconds, several times DeBERTa’s result. DeBERTa got there on a laptop CPU while the larger models had dedicated GPUs, so the classifier’s speed advantage holds up after accounting for the network.

For a guardrail in an application’s request path, every millisecond adds to the delay the user feels, whether it comes from inference or the network. Teams already [running guardrails as a separate hop ahead of inference](https://thenewstack.io/how-to-put-guardrails-around-containerized-llms-on-kubernetes/) also have to account for where that guardrail runs. Remote GPUs or a third-party API add cost and failure points that a classifier running on commodity CPUs avoids.

## Choosing a guardrail model

Red Hat’s results show where the tradeoff starts to shift. A small task-specific classifier remains the stronger default for a well-defined risk with plenty of labeled training data. A zero-shot decision model or LLM judge earns its overhead on broader policies where no strong classifier exists, which matches the conclusion Red Hat’s authors reached.

> A zero-shot decision model or LLM judge earns its overhead on broader policies where no strong classifier exists, which matches the conclusion Red Hat’s authors reached.

The benchmark also undercuts the idea that decision models have already become the new default for guardrails. Jev competed with both classifiers and LLM judges without consistently beating either.

Red Hat tested only English-language datasets, so the accuracy results may not carry over to multilingual guardrails.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)