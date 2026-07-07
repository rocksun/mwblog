With apologies to Gil Scott-Heron and his [timeless 1971 protest song](https://www.youtube.com/watch?v=vwSRqaZGsPw), if anyone thought the AI revolution would not be quantized, they might be wrong. A cultural shift is underway in China, where quantization is indeed driving change.

## Quantization: The compression of AI model weights

[Quantization](https://thenewstack.io/edge-ai-and-model-quantization-for-real-time-analytics/) is the process of compressing AI model weights to a lower numerical precision, making them smaller and cheaper to run. It is a technique that runs in parallel with the provision of open-weight model access, where developers gain public access to a model’s trained parameters, then customize the model and run it locally or on their chosen cloud.

According to [RQR Intelligence](https://renovateqr.com/blog/chinese-ai-models-april-2026), “The massive advantage of the Chinese AI ecosystem is its unwavering commitment to open weights.”

Software engineers are able to use models such as [Qwen](https://thenewstack.io/runpod-ai-infrastructure-reality/), [Xiomei’s MiMo](https://thenewstack.io/coding-agent-endurance-gap/), or [DeepSeek](https://thenewstack.io/deep-dive-into-deepseek-r1-how-it-works-and-what-it-can-do/) V4 Pro and download the weights (the precise numerical values learned during model training), put them through a quantization process, and then run and host them locally on their own machine (or choice of cloud service) to achieve frontier-level intelligence.

> “Chinese frontier models like Z.AI, Qwen, GLM and DeepSeek have become practical tools for software development today. They’re well suited for test generation, refactoring, repo analysis, documentation and first-pass debugging. The caveat is that they still need verification. They’re useful engineering tools, but they’re not autonomous senior engineers” – Gautam Korlam, Sonar.

Principal Engineer at AI code verification and governance company [Sonar](https://www.sonarsource.com/), [Gautam Korlam](https://www.linkedin.com/in/gautamkorlam/), tells *The New Stack* that the biggest advantage of Chinese frontier models is not just another benchmark gain. This is a power play from a different perspective.

“With these Chinese frontier models, developers can inspect them, fine-tune them, run them locally, and integrate them into workflows that are difficult to achieve through API-only deployments. That gives teams more control over cost and intelligence,” Korlam says.

He expands on this, noting that Chinese frontier models like Z.AI, Qwen, GLM, and DeepSeek have become what he views as “practical tools” for software development today.

“They’re well suited for test generation, refactoring, [repo analysis](https://thenewstack.io/phantom-secrets-the-hidden-threat-in-code-repositories/), documentation, and first-pass debugging. The caveat is that they still need verification. They’re useful engineering tools, but they’re not autonomous senior engineers,” Korlam confirms.

The revolution against the proprietary closed-weight AI frontier model companies (Anthropic’s Claude, OpenAI’s GPT-5.5, Google’s Gemini 3 Pro, Meta’s Llama, Mistral, and so on) stems, in part if not wholly, from a strategic response to [US export controls on GPU hardware](https://www.bbc.co.uk/news/articles/cedy6gl99eno).

These constraints have driven Chinese AI labs to innovate by using various coding methodologies. According to [Index.dev](https://www.index.dev/blog/chinese-ai-models), models such as Alibaba Cloud’s Qwen achieve efficiency through the sparse model approach, activating only a subset of parameters during inference.

“Unlike traditional AI models that activate all parameters at once, Qwen3-Max only uses the relevant parts for a given task. This makes it about 30% more efficient on inference, meaning it delivers high performance without burning through computing power,” noted the portal.

> “Things have turned out interesting [with Chinese models at the frontier level], but this is a double-edged sword. It is a blessing for companies and developers. At the same time, it means that the tools can be used by any party – state or private – for defence or offence.” – Piotr Migdał, Quesma.

## Frontier AI is no longer a three-horse race

[Piotr Migdał](https://www.linkedin.com/in/piotrmigdal/), founding engineer at agentic AI evaluation and training company [Quesma](https://quesma.com/) tells *The New Stack* that “things have turned out interesting” with the release of GLM 5.2 by Z.ai, a Chinese model at the frontier level.

He reasons that this development, in particular, means the AI race is “no longer a US-only affair” involving the three usual suspects: OpenAI, Anthropic, and Google. Alongside Z.ai’s GLN, Migdał also points to Qwen 3.6 27B, which he thinks is [the sweet spot for local development](https://quesma.com/blog/qwen-36-is-awesome/) today.

“While the race is and will be fierce, we can expect more Chinese models to be right in the lead,” Migdał says. “GLM 5.2, unlike proprietary models, can be fine-tuned, tweaked to one’s needs to improve its performance on specific tasks, or to remove limitations. This makes it a double-edged sword. It is a blessing for companies and developers, fostering business and open source because there is no longer an API tap controlled by an oligopoly. At the same time, it means that the tools can be used by any party – state or private – for defense or offense.”

With Chinese frontier AI models being widely benchmarked, commented on, and rarely castigated or berated for hallucination across [developer comment boards](https://hn.algolia.com/?q=GLM-5.2), the next inflection point may see a new degree of standardization, transparency, and dare we say commoditization?

## **The specter of model commoditization**

[James McGibney](https://www.linkedin.com/in/james-mcgibney-9059b916/), partner at [OC&C Strategy Consultants](https://www.occstrategy.com/en/), tells *The New Stack* that this is exactly what might be happening.

“Arguably, raw model intelligence is already starting to commoditize, and the emergence of cheaper Chinese open-weight and quantized models will accelerate that shift,” McGibney says.

He thinks that the result of this shift could be enterprises increasingly choosing models on a case-by-case or application-by-application basis.

“If and when this commoditization blossoms, it will further push frontier AI companies — Chinese ones and, for that matter, US ones as well — to move up the stack and so serve to encourage players in this market to monetize the software, workflow integration, governance and implementation layers that make AI reliable and valuable in real business settings.”

Coming full circle then, when Gil Scott Heron told us that the revolution will not be televised, he meant that real change is internal, it won’t be sponsored or commercialized, and that nobody should sit back and be a spectator.

If he were around today (and if he had developed an interest in the growth of Chinese frontier models), he might apply the same scrutiny to the power structures he targeted back in the seventies and then agree that the AI model revolution may well be quantized. Perhaps the only difference (given the presence of software developers) is that this revolution will almost certainly go better with Coke.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)