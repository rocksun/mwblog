# OpenAI Releases New Models Trained for Developers
![Featued image for: OpenAI Releases New Models Trained for Developers](https://cdn.thenewstack.io/media/2025/04/4b2023c3-newopenaimodels_frontend-1024x579.jpg)
[OpenAI](https://thenewstack.io/introduction-to-the-openai-agents-sdk-and-responses-api/) released a new series of GPT models in April that focus on developer AI needs, including improvements to [frontend development](https://roadmap.sh/frontend) and coding in general, and the ability to follow instructions and long contexts.
“We’re excited to announce GPT-4.1, which is a family of models in the API that were trained just for developers,” said OpenAI chief product officer [Kevin Weil](https://www.linkedin.com/in/kevinweil/) during an April 14 livestream about the news. “They even meet or beat GPT-4.5 in a bunch of key ways. And for the first time, they have long context.”

The livestream can be viewed at the bottom of the company’s [post announcing the GPT-4.1 models](https://openai.com/index/gpt-4-1/).

The GPT-4.1 models best GPT‑4o at a variety of coding tasks, including agentically solving coding tasks, frontend coding, making fewer extraneous edits, following diff formats reliably and ensuring consistent tool usage, the company wrote.

On April 16, the AI company also launched [two new reasoning models](https://openai.com/index/introducing-o3-and-o4-mini/):

- OpenAI o3, which offers “strong performance in coding, math, science, and visual understanding.”
- OpenAI o4-mini, which is a smaller, faster model that delivers results — especially in math, coding and visual tasks — at lower cost, the company stated.
The reasoning models are the OpenAI first models that can [“think” with images](https://openai.com/index/thinking-with-images/), according to the company. That basically means they don’t just “see” an image, but can integrate visual information directly from the image into their reasoning chain. For instance, developers could upload whiteboard images to the models, and they could interpret the information rather than just seeing a whiteboard with scribbles.

The OpenAI o3 and o4 models can also independently use all ChatGPT tools, including web browsing, Python, image understanding and image generation to solve complex multistep problems more effectively and independently.

The reasoning models are available today to ChatGPT Plus, Pr, and Team users (o3, o4-mini, o4-mini-high), replacing the o1, o3-mini and o3-mini-high models. o3-pro will follow in a few weeks, but for now, Pro users still have access to o1-pro.

Finally, the AI company also launched [Codex CLI](https://github.com/openai/codex) on April 16. Codex CLI is a lightweight, open source [coding agent that can run locally in a developer’s](https://thenewstack.io/ai-coding-agents-level-up-from-helpers-to-team-players/) terminal.

## When To Use Which GPT-4.1 Models
The GPT-4.1 models are only available through OpenAI’s API platform and not in the public [ChatGPT](https://thenewstack.io/what-chatgpt-and-claude-can-see-on-your-screen/). That said, many of the improvements in following instructions, coding and intelligence have been gradually incorporated into the latest version of GPT-4o.

As for the new models, [Michelle Pokrass](https://www.linkedin.com/in/mpokrass/), who works on OpenAI’s post-training technical team, suggested during the livestream when to use which model.

“When deciding when to use them, we recommend starting with 4.1. It’s our powerhouse for these three dimensions: coding, instruction following and long context,” Pokrass said. “But if you need something a little faster, for maybe a slightly simpler use case, I’d recommend 4.1 mini.”

She added that the nano model — OpenAI’s first — is “an absolute workhorse” for tasks such as auto-complete, classification or extracting information from long documents.

## What GPT-4.1 Offers Developers
For frontend developers, the GPT-4.1 models offer improvements to frontend coding, according to the company’s post.

“GPT‑4.1 also substantially improves upon GPT‑4o in frontend coding, and is capable of creating web apps that are more functional and aesthetically pleasing,” the post stated. “In our head-to-head comparisons, paid human graders preferred GPT‑4.1’s websites over GPT‑4o’s 80% of the time.”

The models boast a larger context window, supporting up to 1 million tokens of context. OpenAI also said the GPT-4.1 can better use that context due to its improved long-context comprehension.

“While benchmarks provide valuable insights, we trained these models with a focus on real-world utility,” the post stated. “Close collaboration and partnership with the developer community enabled us to optimize these models for the tasks that matter most to their applications.”

That’s made the models more reliable. Add to that longer context comprehension of the GPT-4.1 models, and the result is that the models became more effective than previous generations at powering AI agents or systems that automate tasks.

“We trained GPT‑4.1 to reliably attend to information across the full 1 million context length,” the blog post said. “We’ve also trained it to be far more reliable than GPT‑4o at noticing relevant text, and ignoring distractors across long and short context lengths. Long-context understanding is a critical capability for applications across legal, coding, customer support and many other domains.”

The GPT-4.1 model is also more reliable at code diffs across a range of formats, which will be important to API developers who want to edit large files, the post noted.

“We’ve specifically trained GPT‑4.1 to follow diff formats more reliably, which allows developers to save both cost and latency by only having the model output changed lines, rather than rewriting an entire file,” the post stated.

A big draw, though, might be that the GPT-4.1 models promise better performance at a lower cost point.

It’s worth noting that these models have a “refreshed knowledge cutoff of June 2024,” the company stated.

The GPT-4.1 models outperform GPT-4o and GPT-4o mini across the board, “with major gains in coding and instruction following,” the company said in a blog post about the announcement.

“When combined with primitives like the [Responses API](https://platform.openai.com/docs/api-reference/responses),” the post noted, “developers can now build agents that are more useful and reliable at real-world software engineering, extracting insights from large documents, resolving customer requests with minimal hand-holding, and other complex tasks.”

## Evaluating the GPT-4.1 Models
To create the GPT-4.1 models, the OpenAI team created an internal eval for the models that drew on common developer concerns, such as assessing the models’ ability to:

- Use a specific format such as
[XML](https://thenewstack.io/vintage-computer-festival-2017-giant-floppy-disks-json-vanquished-xml/),[YAML](https://thenewstack.io/with-yamlscript-yaml-becomes-a-proper-programming-language/)or[Markdown.](https://thenewstack.io/introduction-to-markwhen-a-markdown-timeline-tool-for-devs/) - Follow ordered instructions.
- Understand negative instructions that specify what behavior the model should avoid.
- Train the model to say “I don’t know” if requested information isn’t available.
The blog post also includes details about the new models’ benchmarks

## OpenAI’s First Nano Model
OpenAI also released its first nano model, GPT-4.1 mini.

“It matches or exceeds GPT‑4o in intelligence evals while reducing latency by nearly half and reducing cost by 83%,” the company’s post stated. ”For tasks that demand low latency, GPT‑4.1 nano is our fastest and cheapest model available.”

The post went on to say that the new nano model offers “exceptional performance at a small size with its 1 million token context window, and scores 80.1% on MMLU, 50.3% on GPQA and 9.8% on Aider polyglot coding — even higher than GPT‑4o mini.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)