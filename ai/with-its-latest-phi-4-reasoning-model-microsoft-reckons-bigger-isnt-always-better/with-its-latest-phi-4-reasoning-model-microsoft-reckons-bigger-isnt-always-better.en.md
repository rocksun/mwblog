The dominant trend in artificial intelligence of late has been clear: [bigger models](https://thenewstack.io/introduction-to-llms/), more data, more compute. But [the cost](https://thenewstack.io/why-agentic-llm-systems-fail-control-cost-and-reliability/) of training and running those systems keeps rising as companies pour enormous computing resources into ever larger models. It’s this tension that has led researchers at Microsoft to explore a different path: training more compact models on carefully curated reasoning data to see how far they can go.

In a [blog post last week](https://www.microsoft.com/en-us/research/blog/phi-4-reasoning-vision-and-the-lessons-of-training-a-multimodal-reasoning-model/), Microsoft described [Phi-4-Reasoning-Vision-15B](https://huggingface.co/microsoft/Phi-4-reasoning-vision-15B), a multimodal model designed to handle reasoning tasks that involve both text and images. The goal isn’t simply to add visual understanding to a language model; rather, it explores whether compact models trained on high-quality reasoning datasets can compete with much larger systems.

Released with open weights under a permissive MIT license, Phi-4-Reasoning-Vision-15B is available on all the usual platforms, including [Hugging Face](https://huggingface.co/microsoft/Phi-4-vision-reasoning-15B), [GitHub](https://github.com/microsoft/Phi-4-vision), and Microsoft’s [own AI Foundry](https://ai.azure.com/catalog/models/Phi-4-Reasoning-Vision-15B), allowing developers to experiment with the system directly and build on the work. That approach reflects Microsoft Research’s broader effort to encourage external experimentation around the Phi family.

To rewind just a little, Phi models are part of Microsoft’s broader research effort into what the company once referred to as small language models, or SLMs. The series began with [Phi-1](https://huggingface.co/microsoft/phi-1) (around 1.3 billion parameters) and [Phi-2](https://www.microsoft.com/en-us/research/blog/phi-2-the-surprising-power-of-small-language-models/) (2.7 billion parameters), followed by a succession of larger models, including [Phi-3](https://huggingface.co/collections/microsoft/phi-3) and [Phi-4](https://www.microsoft.com/en-us/research/publication/phi-4-technical-report/), each with roughly 14 billion parameters. Parameters are the internal numerical weights learned during training, and are often used as a rough proxy for a model’s size and capability.

Rather than chasing ever-larger parameter counts, Microsoft aimed for comparatively compact models designed for strong reasoning performance without the enormous training runs associated with frontier systems.

It’s also worth noting that Microsoft has seemingly dropped the “small language model” label in its latest research, as the term does not appear in the [technical report](https://www.microsoft.com/en-us/research/blog/phi-4-reasoning-vision-and-the-lessons-of-training-a-multimodal-reasoning-model/) for Phi-4-Vision-Reasoning. At around 15 billion parameters, the model is significantly larger than the earliest Phi systems, which ranged from roughly one to four billion parameters. Yet it remains far smaller than many frontier models developed by rivals, which can run into the hundreds of billions of parameters.

The research emphasis has also shifted toward reasoning and multimodal capabilities rather than model size itself, which may explain why the “small language model” label has been retired for the latest incarnation.

## Teaching smaller models to reason

At its core, the research asks one simple question: how much reasoning ability can be taught to a model without dramatically increasing its size? A key part of that effort is efficiency. Microsoft says the system was built to deliver reasoning capability without requiring the kind of hardware infrastructure typically associated with frontier models.

“Our model is intended to be lightweight enough to run on modest hardware while remaining capable of structured reasoning when it is beneficial,” the researchers note.

The team also emphasises the system’s training efficiency. The model was trained on roughly 200 billion tokens, drawing on earlier Phi-4 reasoning work and the base Phi-4 model. Microsoft says this is far less data than several recent vision-language models — including [Qwen2.5-VL](https://huggingface.co/collections/Qwen/qwen25-vl), [Qwen3-VL](https://huggingface.co/collections/Qwen/qwen3-vl), [Kimi-VL](https://huggingface.co/moonshotai/Kimi-VL-A3B-Thinking), and [Gemma 3](https://deepmind.google/models/gemma/gemma-3/) — which it says were trained on datasets exceeding one trillion tokens.

That efficiency is central to the project’s broader goal of improving the balance between performance and computational cost.

“We can therefore present a compelling option compared to existing models pushing the Pareto-frontier of the tradeoff between accuracy and compute costs,” the researchers write.

Phi-4-Vision-Reasoning-15B tackles that challenge through a training approach focused on structured reasoning tasks. The model was trained on datasets designed to teach step-by-step problem solving, including tasks where it must interpret visual inputs such as tables, screenshots and other structured materials before reaching a conclusion. Some of these examples were generated synthetically, using larger models to produce explanations or solution traces that the smaller system can learn from.

The goal was to produce a model that can follow chains of logic across several steps while also interpreting visual inputs.

The model can also adjust the amount of reasoning it performs depending on the task. Developers can switch between modes that prioritise speed or deeper analysis, allowing the same model to respond quickly in some situations or apply step-by-step reasoning when a problem requires it. [Leon Godwin](https://www.linkedin.com/in/leongodwin/), a principal cloud evangelist for Microsoft in London, said this flexibility allows the system to handle a wider range of workloads without deploying different models.

“The killer feature is three thinking modes — hybrid, think, and nothink — that developers switch at runtime,” Godwin [writes](https://www.linkedin.com/posts/leongodwin_azureai-smalllanguagemodels-activity-7435656545402716160-fMOI/). “Need sub-second GUI element grounding for a computer-use agent? NoThink mode. Need step-by-step mathematical reasoning over a diagram? Think mode. Same model, same deployment.”

That combination is useful because many real-world tasks involve both language and images. Interpreting a visualisation, reviewing a document, or navigating a user interface all require connecting visual perception with reasoning. In real terms, that might include answering questions about charts, analysing screenshots or documents, or generating descriptions of visual content provided alongside a prompt.

However, Microsoft cautions that the model hasn’t been evaluated for high-risk domains such as medical or legal decision-making, or for fully autonomous actions involving financial transactions or other sensitive operations lacking human oversight.

“Developers should consider common limitations of vision-language models as they select use cases, and evaluate and mitigate for accuracy, safety, and fairness before using within a specific downstream use case, particularly for high-risk scenarios,” the [model card warns](https://huggingface.co/microsoft/Phi-4-reasoning-vision-15B).

## Why multimodal reasoning matters

Multimodal AI systems have become a major focus as models move beyond pure text interaction. Many real-world tasks involve both language and visual information — from analysing technical documents and dashboards to navigating software interfaces. By combining visual understanding with structured reasoning, the Phi-4-Vision-Reasoning model interprets visual inputs and applies step-by-step logic to them. Microsoft highlights scenarios such as analysing scientific figures, solving visual math problems, and interpreting diagram-based instructions.

The Phi project also reflects a broader shift in how researchers think about improving AI models. For years, the industry leaned heavily on scaling laws, increasing model size, and training data to improve performance. But that approach comes with hefty compute costs.

Microsoft’s work instead focuses on training strategy: using curated datasets, synthetic reasoning examples, and more targeted training techniques to improve reasoning ability without dramatically increasing model size. One method involves generating step-by-step reasoning traces using larger systems and then training smaller models on those explanations. In effect, large models act as teachers for more compact ones.

Such techniques are becoming more common across AI research. Meanwhile, large frontier models still dominate mindshare, with companies such as OpenAI, Google, and Anthropic continuing to push toward ever larger systems. Experiments like Phi reflect that shift, suggesting that carefully trained models with far fewer parameters may be able to handle many tasks without the enormous compute requirements of frontier systems.

Some researchers argue this approach may be particularly relevant for AI agents, which often need to perform a large number of smaller perception and reasoning tasks rather than rely on a single massive model.

[Elvis Saravia](https://www.linkedin.com/in/omarsar/), an AI researcher and founder of [Dair.ai](http://Dair.ai), said the model illustrates *how* smaller multimodal reasoning systems could play an important role in real-world agent deployments.

“Not every agent task needs a frontier model. Phi-4-reasoning-vision shows what’s possible at 15B parameters,” Saravia [writes](https://www.linkedin.com/posts/omarsar_new-research-from-microsoft-phi-4-reasoning-vision-activity-7435691960193105920-0hbQ?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAAKviRMBcX5r1q4mPiPDFxquTiZC0hbfIYQ). “Smaller reasoning models that handle vision are essential for practical agent deployments.”

Elsewhere, [Andreas von Richter](https://www.linkedin.com/in/avonrichter/), an AI researcher, engineer, and investor, said the most interesting insight in Microsoft’s paper was easy to miss: data quality may be playing a larger role in model performance than architecture alone.

“The biggest performance gains didn’t come from architecture or scale,” von Richter [noted](https://www.linkedin.com/feed/update/urn:li:activity:7435691960193105920?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7435691960193105920%2C7436785692069904384%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287436785692069904384%2Curn%3Ali%3Aactivity%3A7435691960193105920%29). They came from data curation. Systematic filtering, error correction, and synthetic augmentation.”

He also pointed out that the model was trained on roughly 200 billion tokens, compared with about one trillion used for some competing multimodal systems — suggesting a significant efficiency gap driven largely by training data decisions.

Finally, von Richter said the model’s ability to skip reasoning for simpler perception tasks may be particularly important for agent systems, where unnecessary reasoning can add latency and compute costs.

“Most agent pipelines waste compute forcing reasoning on tasks that don’t need it,” he said.

Whether that approach can match the capabilities of the largest models remains to be seen. For now, frontier systems still dominate the most demanding benchmarks. But it highlights a growing debate within the field about whether progress in AI will come from ever-larger models — or [from smarter ways to train](https://thenewstack.io/beyond-shift-left-improving-ai-training-data/)[them](https://thenewstack.io/beyond-shift-left-improving-ai-training-data/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)