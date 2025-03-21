# A Hugging Face Project Is Uncovering DeepSeek-R1’s Secrets
![Featued image for: A Hugging Face Project Is Uncovering DeepSeek-R1’s Secrets](https://cdn.thenewstack.io/media/2025/03/609ba3c6-solen-feyissa-ipskq4kllkg-unsplashb-1024x576.jpg)
[DeepSeek-R1](https://www.deepseek.com/)’s release was a huge wake-up call for the AI world, according to [Jeff Boudier](https://www.linkedin.com/in/jeffboudier/), who leads product and growth at [Hugging Face](https://huggingface.co/).
“The wake-up call was that, in order to get the best possible AI, you don’t need to rely on closed models from OpenAI, Anthropic, Google, etc.,” Boudier said. “You can access an open model here from DeepSeek with similar capabilities, coming from a research lab that was previously not very much known.”

[Hugging Face](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/) is a company that serves as a repository hub and community for [open source](https://thenewstack.io/making-good-on-the-promise-of-open-source-ai/) [large language models (LLMs](https://thenewstack.io/what-is-an-llm-token-beginner-friendly-guide-for-developers/)). It very quickly saw the impact of DeepSeek-R1, which is [hosted on the platform](https://huggingface.co/deepseek-ai/DeepSeek-R1).
“What was interesting is that it was not just a big announcement for sort of the general public, it also created a flurry of activity within the AI community, and we saw that directly on Hugging Face,” Boudier told The New Stack. “The [R1 release today](https://huggingface.co/deepseek-ai/DeepSeek-R1) — that’s over 10 million downloads on Hugging Face and that’s just the last 30 days.”

## How DeepSeek Changed AI
[DeepSeek creates very efficient models that run](https://thenewstack.io/how-to-run-deepseek-models-locally-on-a-windows-copilot-pc/) on less powerful hardware. That’s unusual in AI, so much so that when its R1 model was released in January, [it triggered a stock dive](https://finance.yahoo.com/news/nvidia-stock-plummets-loses-record-589-billion-as-deepseek-prompts-questions-over-ai-spending-135105824.html) for [NVIDIA](https://thenewstack.io/after-deepseek-nvidia-puts-its-focus-on-inference-at-gtc/), which manufactures the graphics processing units (GPUs) upon which other AI systems rely.
DeepSeek also used multiple [neural networks instead of relying on a single “generalist” model](https://thenewstack.io/who-needs-neural-networks-the-generative-prowess-of-state-transition-models/). Plus, it was inexpensive to train at just $5.5 million compared to other generation AI models, “thanks to architectural changes like [Multi-Token Prediction (MTP)](https://arxiv.org/abs/2502.09419), [Multi-Head Latent Attention (MLA)](https://arxiv.org/abs/2502.07864) and a LOT (seriously, a lot) of hardware optimization,” [Hugging Face researchers wrote in a blog post](https://huggingface.co/blog/open-r1).

The [DeepSeek organization on Hugging Face](https://huggingface.co/deepseek-ai) is also the most followed organization on the site, with more than 45,000 followers. That’s more than Google, Microsoft or other large AI players. There are now thousands of DeepSeek model derivatives available on the hub, he added.

It also changed the game for those organizations that want to use AI. Now, organizations can download the open source DeepSeek, released under the [MIT license](https://opensource.org/license/mit), and host it on premises.

“If you’re an enterprise, you don’t need to send your customer data to an API anymore, like that of OpenAI or others,” Boudier said. “You can actually host everything in-house. And it’s also MIT-licensed, so you can use it for whatever commercial purpose. That’s really, really powerful.”

## The Open-R1 Project
DeepSeek didn’t just release its open source R1 and R1-Zero models — the Chinese company released a [technical report](https://github.com/deepseek-ai/DeepSeek-R1/blob/main/DeepSeek_R1.pdf) that was “very generous in terms of the knowledge they shared and how they were able to create R1 and R1-Zero models using reinforcement learning techniques and some of these tricks,” Boudier explained.

The techniques described in the technical report were implemented within Hugging Face libraries, so they can be used by research labs around the world, he added. That included techniques such as [Generative Reasoning and Planning Optimization (GRPO)](https://thenewstack.io/deep-dive-into-deepseek-r1-how-it-works-and-what-it-can-do/), which enables the AI to think through completing more complex tasks and then improve over time.

But there were some missing pieces in DeepSeek’s research, Boudier said.

“The technical report did not explain or describe the [training data](https://thenewstack.io/dealing-with-distributed-data-when-training-ai-models/) that was used to train and align the R1 model,” he said. “It did not describe the distillation process.”

Specifically, a Hugging Face research team noted, the report left questions about:

- Data collection, such as how the reasoning-specific datasets were curated.
- Model training. “No training code was released by DeepSeek, so it is unknown which hyperparameters work best and how they differ across different model families and scales,” the researchers said.
- Scaling laws. “What are the compute and data trade-offs in training reasoning models?” Hugging Face researchers asked.
These questions lead to the creation of the [Open-R1 project](https://huggingface.co/open-r1), an initiative that is systematically reconstructing DeepSeek-R1’s data and training pipeline, validating its claims, and “pushing the boundaries of open reasoning models,” the researchers wrote.

“By building Open-R1, we aim to provide transparency on how reinforcement learning can enhance reasoning, share reproducible insights with the open source community, and create a foundation for future models to leverage these techniques,” they stated.

The Hugging Face researchers outlined their “plan of attack” for Open-R1:

- Replicate the R1-Distill models by distilling a high-quality reasoning dataset from DeepSeek-R1.
- Replicate the pure RL pipeline that DeepSeek used to create R1-Zero. This will involve curating new, large-scale data sets for math, reasoning, and code.
- Show they can go from base model → SFT → RL via multi-stage training.
Reproducing the DeepSeek-R1 pipeline allows the research labs to go through the exact same process that DeepSeek went through when they created DeepSeek-R1 and DeepSeek-R1-Zero, which were reasoning models distilled from the foundation model, DeepSeek-V3.

## Open-R1’s Purpose
Open-R1 isn’t designed to create new models per se — it’s more about creating and freely publishing artifacts.

One of the missing pieces in DeepSeek’s published research was how to go from a large, pre-trained model that has general knowledge and has been trained on trillions and trillions of tokens to a model that’s very good at a particular domain.

The key was creating reasoning traces that are produced by inferencing this “very capable model” on a [specific domain](https://thenewstack.io/domain-specific-ai-aiseras-answer-to-enterprise-needs/) and questions, Boudier said. Reasoning traces refer to a record or log of the steps an AI system takes to arrive at a conclusion or decision. Think of it as recording the AI’s “thought process.”

“You can actually host everything in-house. And it’s also MIT-licensed, so you can use it for whatever commercial purpose. That’s really, really powerful.”

— Jeff Boudier, head of product and growth at Hugging Face
In the case of DeepSeek-R1 and R1-Zero, the reasoning is on a specific domain, rather than, say, the whole internet.

“You can take a model and then teach it through distillation to be really, really good at this particular type of tasks” through reasoning traces, Boudier explained.

That’s what the [Hugging Face team released in its second update](https://huggingface.co/blog/open-r1/update-2) — a mathematical reasoning traces dataset called [Open-R1-Math-220k](https://huggingface.co/datasets/open-r1/OpenR1-Math-220k) that has more than 200,000 reasoning traces for complex mathematical questions.

“The synthetic datasets will allow everybody to fine-tune existing or new LLMs into reasoning models by simply fine-tuning on them,” the team said of the math datasets. “The training recipes involving RL [reinforcement learning] will serve as a starting point for anybody to [build similar models from scratch and will allow researchers](https://thenewstack.io/agentic-ai-tools-for-building-and-managing-agentic-systems/) to build even more advanced methods on top.”

There’s a lot of potential in exploring other areas, including code but also scientific fields such as medicine, “where reasoning models could have a significant impact,” they stated.

## The Latest Release
The [Open-R1 project just released its third update](https://huggingface.co/blog/open-r1/update-3), which Boudier called the “most exciting update to date.”

It includes a code programming data set with more than 100,000 events programming reasoning traces obtained from DeepSeek R1. This dataset can be used to train new models to better understand the nuances of code, enabling the AI model to explain the reasoning behind the code. From it, the team built the [OlympicCoder 7-billion](https://huggingface.co/open-r1/OlympicCoder-7B) and [32-billion parameter models](https://huggingface.co/open-r1/OlympicCoder-32B).

“What’s really exciting is that by applying the distillation pipeline that they recreated from the R1 paper and from the R1 release, they were able to create these really, really powerful models,” Boudier said. “To give you a sense, the 32-billion model outperforms [Claude Sonnet](https://thenewstack.io/making-the-fediverse-more-accessible-with-claude-3-7-sonnet/), which is the [Anthropic](https://thenewstack.io/model-context-protocol-bridges-llms-to-the-apps-they-need/) state-of-the-art model for advanced programming challenges.”

The team also released a new [IOI benchmark](https://github.com/huggingface/ioi) — based on the annual competitive programming competition, the International Olympiads of Informatics — to have a new way to measure a model’s ability to tackle more challenging programming problems.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)