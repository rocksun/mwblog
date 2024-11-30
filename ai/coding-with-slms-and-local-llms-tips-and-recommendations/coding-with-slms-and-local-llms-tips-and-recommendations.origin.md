# Coding With SLMs and Local LLMs: Tips and Recommendations
![Featued image for: Coding With SLMs and Local LLMs: Tips and Recommendations](https://cdn.thenewstack.io/media/2024/11/837bd360-gabriella-clare-marino-egxpsrg02su-unsplashb-1024x576.jpg)
While [the impact of GitHub Copilot](https://thenewstack.io/a-developer-health-check-on-github-copilot-and-ai-assistants/) and other mainstream AI solutions on coding is undeniable, plenty of questions arise around the trend as a whole.

For starters, many developers aren’t too comfortable sharing their code, oftentimes proprietary, with third parties. There’s also the financial part of the equation since API costs can accumulate pretty quickly — especially if you’re using the most advanced models.

Enter *local* language models and their diminutive equivalents, such as small language models. The developer community has been increasingly vocal about their benefits, so let’s see what all the fuss is about. In addition to the concept itself, we’ll cover the best models, their benefits, and how this affects AI-aided development as a whole.

## What Are Locally Hosted LLMs
Locally hosted LLMs are advanced machine learning models that operate entirely within your local environment. These models, [typically boasting billions of parameters](https://datasciencedojo.com/blog/tuning-optimizing-llm-parameters/), offer sophisticated code generation, contextual understanding, and debugging capabilities. Deploying LLMs locally allows developers to circumvent the latency, privacy issues, and subscription costs associated with cloud-hosted solutions.

Running an LLM locally provides fine-grained control over model optimization and customization, which is particularly useful for specialized development environments.

Furthermore, [fine-tuning an LLM on proprietary codebases](https://huggingface.co/learn/cookbook/en/fine_tuning_code_llm_on_single_gpu) enables more context-aware suggestions, which can significantly streamline complex workflows. The ability to maintain sensitive data locally also reduces exposure to privacy risks, making this option attractive for enterprise developers who need compliance with strict data governance policies.

However, running large models requires substantial hardware resources — typically multicore CPUs or GPUs with ample memory — making it a choice better suited for those with robust setups or specific performance needs. The trade-off is a powerful, adaptable tool that can provide deep insight and support in coding scenarios.

### What Are SLMs?
SLMs, or Small Language Models, are more lightweight versions of their LLM counterparts. They are designed with fewer parameters, [optimizing them for speed and efficiency without sacrificing core capabilities](https://www.salesforce.com/blog/small-language-models/) like code completion and simple context handling. They can’t do everything; but what they can do, they do brilliantly.

The smaller architecture of SLMs also makes them highly efficient for tasks where reduced latency and smaller memory footprints are essential. SLMs are [suitable for scenarios such as rapid prototyping](https://dl.acm.org/doi/10.1145/3643795.3648393), embedded systems development, or working on machines with limited computational resources.

The main limitation of SLMs is their reduced ability to capture complex, broad contexts compared to LLMs, which can affect their performance when dealing with intricate projects or extensive codebases.

Nevertheless, they’re considered attractive because experts believe phones will be able to run them efficiently in a matter of months. I’ve seen experiments of SLMs using computer vision [to read bank statements](https://www.docuclipper.com/blog/how-to-read-a-bank-statement/) and submit data to Freshbooks — more use cases like that will emerge.

While Google, Microsoft and Anthropic are focused on giant models distributed as a service, Apple has emerged as a leader in the open source SLM space. Their [OpenELM family is made to be run on mobile devices](https://venturebeat.com/ai/apple-releases-openelm-small-open-source-ai-models-designed-to-run-on-device/), and early feedback suggests they have the ability to complete coding tasks efficiently.

## How to Choose the Best Model for Coding
Selecting [the optimal local LLM or SLM for your development](https://thenewstack.io/llm-chains-are-transforming-ai-development/) needs involves a combination of community insights, empirical benchmarks, and personal testing. Start by exploring community-driven leaderboards, which rank models based on various performance metrics such as speed, accuracy, and parameter efficiency.

These rankings provide a solid foundation for understanding which models are leading the field and how active their respective communities are in contributing to enhancements and optimizations. However, this is still a pretty robust view.

The next step would be to see [how the model performs on more standardized leaderboards](https://arxiv.org/abs/2403.19114) along the lines of:

**HumanEval**: A benchmark comprising 164 programming problems designed to assess the functional correctness of code generated by LLMs. Models are evaluated based on their ability to produce correct and executable code solutions.**MBPP (MultiPL-E)**: An extension of the HumanEval benchmark, MBPP includes problems across multiple[programming languages](https://thenewstack.io/programming-languages/), enabling the evaluation of multilingual code generation capabilities. It assesses models on their proficiency in generating correct code in various programming languages.**BigCodeBench**: A comprehensive benchmark that[evaluates LLMs on code understanding and generation tasks across 43 programming languages](https://arxiv.org/abs/2311.08588)and eight coding tasks. It measures performance from three dimensions: length, difficulty, and efficiency.**LiveCodeBench**: A dynamic[benchmark that continuously collects new coding problems](https://arxiv.org/abs/2403.07974)from platforms like LeetCode, AtCoder, and CodeForces. It evaluates LLMs on code generation, self-repair, code execution, and test output prediction, providing a holistic assessment of coding capabilities.**EvoEval**: A benchmark suite that evolves existing coding problems to create new challenges, assessing the program synthesis abilities of LLMs. It highlights potential overfitting in models and provides insights into their adaptability to novel coding tasks.
Benchmarks are critical, but they are not one-size-fits-all. Public benchmarks can provide a general overview of a model’s performance in standardized tasks, but **the ultimate test is always how a model performs within your specific development environment**.

Running personal benchmarks on tasks typical of your workflows will help identify how well a given model fits your real-world needs — whether that’s generating boilerplate code, debugging legacy applications, or offering context-aware suggestions. Think about what you require from a coding model, and prompt different ones to complete it. Repeat the task on a regular basis and apply it to newly-released models, too.

## Best Local LLMs for Coding
I know the word “best” holds a lot of weight, but keep in mind that every list like this is subjective. Every benchmark, every test and every use case — they’re all different, so a model that works for you might not be ideal for someone else.

### DeepSeek V2.5
DeepSeek V2.5 is an open source model that [integrates the capabilities of DeepSeek-V2-Chat and DeepSeek-Coder-V2-Instruct](https://huggingface.co/deepseek-ai/DeepSeek-V2.5), enhancing both general conversational and coding proficiencies. It supports a context length of up to 128K tokens, facilitating extensive dialogue management and complex data processing. This makes it ideal for larger projects.

In evaluations, DeepSeek V2.5 has demonstrated notable improvements in tasks such as writing and instruction-following, outperforming its predecessors in benchmarks like AlpacaEval 2.0 and ArenaHard. This model is accessible via web platforms and APIs, offering a streamlined, intelligent and efficient user experience.

### Qwen2.5-Coder-32B-Instruct
Qwen2.5-Coder-32B-Instruct is a state-of-the-art open source code model [developed by the Qwen team at Alibaba Cloud](https://www.alibabacloud.com/blog/alibaba-cloud-unveils-new-ai-models-and-revamped-infrastructure-for-ai-computing_601622). It seems to match the coding capabilities of GPT-4o, demonstrating strong and comprehensive coding abilities alongside good general and mathematical skills.

The model [supports a context length of 128K tokens and is proficient in 92 programming languages](https://arxiv.org/abs/2409.12186). It has achieved top performance on multiple code generation benchmarks, including EvalPlus, LiveCodeBench, and BigCodeBench, and performs comparably to GPT-4o in code repair tasks.

I also like this model because it comes in various quantizations, [being made available in 0.5, 1.5, 3, 7, 14 and 32 billion parameters](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct). Hence, even those with lower-specced devices can run it to assist with coding tasks.

### Nxcode-CQ-7B-orpo
Nxcode-CQ-7B-orpo is a local Large Language Model optimized for coding tasks. It offers balanced performance for simple coding scenarios, providing a lightweight solution for developers seeking efficient code generation and understanding capabilities.

Interestingly, it’s not a standalone model — [it’s a fine-tuning of Qwen/CodeQwen1.5-7B on high-ranking data](https://huggingface.co/NTQAI/Nxcode-CQ-7B-orpo) pertaining to coding, as stated by the authors.

In contrast with Qwen2.5 and LLaMa 3, Nxcode-CQ-7B-orpo is designed to handle fundamental coding tasks effectively, making it suitable for projects with less complexity. Hence, it’s the best learning assistant for code-related tasks and basics [related to JavaScript web development](https://thenewstack.io/top-10-javascript-seo-tricks-every-developer-should-know/). I found it lackluster when dealing with more complex Three.js animation, for instance.

### OpenCodeInterpreter-DS-33B
OpenCodeInterpreter-DS-33B is a high-parameter model focusing on advanced code interpretation and dynamic problem-solving, [created by a team of Chinese scientists](https://arxiv.org/abs/2402.14658). It excels in understanding complex code structures and generating sophisticated code solutions.

Unlike Qwen, this model is based on another, mainly on Deepseek-coder-33b-base. It grabbed the community’s attention immediately upon release, [excelling on HumanEval and MBPP](https://huggingface.co/m-a-p/OpenCodeInterpreter-DS-33B).

The model’s large parameter size enables it to manage intricate coding tasks, making it a valuable tool for developers working on complex projects requiring deep code analysis and generation.

### Artigenz-Coder-DS-6.7B
Developed by an Indian team, [Artigenz-Coder-DS-6.7B is tailored for rapid code prototyping](https://huggingface.co/Artigenz/Artigenz-Coder-DS-6.7B), offering efficient code generation capabilities. While it may not match the robustness of larger models, it provides a practical solution for developers needing quick code drafts and prototyping assistance.

Artigenz-Coder-DS-6.7B is suitable for projects where speed and efficiency are prioritized over handling highly complex coding tasks. Its 13GB memory footprint makes it one of the most accessible coding models, being able to easily run on mid-range hardware.

## Downsides of Local LLMs for Coding
More than anything, local models are limited by hardware. With [Nvidia’s top-of-the-line H100 GPU costing up to $40,000](https://sherwood.news/tech/companies-hoarding-nvidia-gpu-chips-meta-tesla/) and tech giants hoarding billions of dollars worth of them, there’s no conceivable way any individual or organization can match this computing power. That’s without even mentioning [the fact these companies employ the foremost AI engineers](https://www.economist.com/business/2024/06/08/the-war-for-ai-talent-is-heating-up) and have a head start over entire countries.

You can still rent GPU time to train or fine-tune LLMs, but even this is prohibitively expensive. For now, the best one can hope for is to save for a home server rack with a couple of 3090s chugging along.

Then, there’s the fact that this data isn’t safe just because it’s on your device. Don’t be surprised to see people [becoming more wary of accessing captive portals](https://www.cloudi-fi.com/blog/what-is-a-captive-portal) when connecting to WiFi networks, as hackers will try to steal local LLM data. Remember, this is still a nascent field and there are still vulnerabilities we aren’t even aware of.

Finally, there’s also the unfortunate fact that Claude 3.5 Sonnet and o1-preview are far ahead of any open source, locally run competition. You can’t beat billions of gigabytes of VRAM [and billions of dollars in R&D funds](https://www.reuters.com/technology/artificial-intelligence/openai-closes-66-billion-funding-haul-valuation-157-billion-with-investment-2024-10-02/). Nevertheless, the goal isn’t to beat that — it’s to provide something open source, free and customizable that devs can use reliably and consistently, right?

## Conclusion
Many consider local LLMs and SLMs the future of coding assistants. Copilot, ChatGPT and Claude might have tens of billions in financial backing, but you’ll always be at the mercy of someone else’s software, restrictions, censorship and, of course, data center issues.

Locally hosted models, on the other hand, are completely private and won’t require sharing code with a third party. Furthermore, you’re not at the mercy of the cloud or the limitations of your API budget.

So, what’s the holdup? Well, these LLMs are not only less impressive from a performance standpoint, but they’re also less intuitive and harder to fine-tune than ready-made, no-code coding assistants like Copilot. Nevertheless, we’re already nearing the performance of mainstream models and the likes of Apple and Meta and focusing their efforts on open source. Exciting times are upon us.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)