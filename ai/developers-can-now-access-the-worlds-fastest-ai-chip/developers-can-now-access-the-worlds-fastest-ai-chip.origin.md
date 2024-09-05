# Developers Can Now Access the World’s Fastest AI Chip
![Featued image for: Developers Can Now Access the World’s Fastest AI Chip](https://cdn.thenewstack.io/media/2024/08/df525111-getty-images-hch5fqzxshc-unsplash-1024x683.jpg)
AI computing is still at the dial-up level. Getting an answer from an LLM can be slow. But now Cerebras — a chip maker — has launched an AI cloud service that it claims is 10 to 20 times faster than regular cloud providers.

The service, called [Cerebras Inference](https://inference.cerebras.ai/), provides access to the world’s largest and fastest AI chip, which handily outperforms a single or group of Nvidia GPUs cobbled together.

Cerebras’ WSE-3 AI chip size is about 46,225mm², which is 56 times larger than Nvidia’s H100 GPU. Cerebras has put together these mega-AI chips in its data centers.

The company is also welcoming developers to build AI applications on it with free API keys, though there’s very limited customization available. The available models on the service include Llama 3.1 and its 8 billion and 70 billion parameter variants.

Upcoming models include Llama 3.1 with 405 billion parameters, Mistral’s Large 2 with 123 billion parameters, which was [announced](https://mistral.ai/news/mistral-large-2407/) a month ago, and Cohere’s [Command R](https://cohere.com/command).

## Behind the Numbers
The response time on Cerebras chips for Llama 3.1 with 8 billion parameters is 1,842 tokens per second, according to independent benchmarks on [Artificial Analysis](https://artificialanalysis.ai/models/llama-3-1-instruct-8b/providers).

On the same LLM, the output speed of Microsoft Azure is 51.5 tokens per second, and Amazon is 92.2. That makes Cerebras 20 times faster than the major cloud providers.

“Most of our users are inference application developers who just want to build on top of the stack of an open source model.”

– Andy Hock, Cerebras Systems
The numbers vary with larger context sizes and LLM size, which have demanding memory and data requirements.

Developers have control over the frontend of the development, but can’t do much with the backend in customizing models or controlling hardware.

“Most of our users are […] inference application developers who just want to build on top of the stack [of an] open source model,” said Andy Hock, vice president of product management at Cerebras Systems, in an interview with The New Stack.

**What Devs Need to Know**
The Cerebras-compatible models themselves are written in standard Pytorch.

Developers will get a free API key, and can easily move chatbot or other AI applications to Cerebras’ inferencing cloud service.

For example, developers can change a line code by swapping out the API key and pointing from OpenAI to Cerebras’ cloud service. That’s by changing just a line or two of code.

Cerebras users can build RAG or customized models with personalized data.

“They’re therefore just waiting and ready for your inbound API call to throw data at those weights on the wafer and generate the answer back,” Hock said.

“If they want to run something that’s not Llama 8B, not Llama 70B… they can work with us to build it and deploy it,” Hock said.

Customers can build RAG or customized models with personalized data. That will require the installation of Ollama and creation of a vector database locally. An example using Pinecone and Docker is outlined [here](https://github.com/Cerebras/inference-examples/tree/main/rag-pinecone-docker), and Weaviate and Hugging Face are outlined [here](https://rag-weaviate-cerebras.streamlit.app/). You can view [other examples](https://inference-docs.cerebras.ai/examples) and, also, the Cerebras Inference platform is [compatible](https://inference-docs.cerebras.ai/openai) with OpenAI client libraries.

The company is discussing “easy buttons” and customization capabilities, executives said. But the first thing was to get the service up and running so that developers get access to the chips, Hock said.

“We’re going to learn a lot about the market for this new breed of performance over the next 60 days. We have some really exciting partnerships and application projects coming,” he added.

**Pricing**
Cerebras’s inference isn’t cheap when compared to cloud providers. But as with CPUs and GPUs, you have to pay for performance.

The good news: the API is free.

A free tier of Llama 3.1-8b — with the 1,800 tokens per second speed — has a daily token limit of 1 million, and 30 requests per minute. The paid tier has 10 cents per 1 million tokens in input or output, with unlimited requests.

The free tier of Llama 3.1-70B — with 450 tokens per second speed — has a daily token limit of 1 million, and 30 requests. The paid tier has 60 cents per minute per 1 million tokens in input or output.

Cerebras also has an enterprise model for those who want to run customized models.

Google and OpenAI have recently been raising prices for customers using APIs to access LLMs — that upset customers who were using Google AI tools to build applications. Similarly, the price of Cerebras inferencing may go up as it comes out of the experimental phase. Cerebras’ chips are expensive to manufacture, and it’ll need to recoup money to build up its cloud infrastructure.

**Scope**
Cerebras’ AI speed opens the door to agents (or agentic) modeling, in which a single prompt is spread out and sent out to many different models. Those models review it, analyze it, and produce results, which are spread into other models, and then aggregated back.

“We have partners building applications that chain our LLM with multiple other models.”

– Hock
“We have partners building applications that chain our LLM with multiple other models. For example, doing speech-to-text conversion before sending text to our LLM inference, then outputting to a text-to-speech model,” Hock said.

Developers can do that on Cerebras cloud once many more models become available.

“You have full flexibility as a developer to effectively string our LLM inference into a multimodal workflow,” Hock said.

There’s no easy-button capability yet to do that. Developers will have to customize scripts to different models for such workflows.

**Under the Hood**
There’s a reason Cerebras is able to pull off such significant speed upgrades.

The chip is 57 times larger than a single Nvidia GPU. In production, individual Nvidia’s H100 GPUs are cut off a big wafer. Instead, Cerebras has put its entire chip on a wafer.

“What we are putting together is impossible to achieve on GPUs.”

– Andrew Feldman, Cerebras CEO
The sheer size and wafer engineering of the 4-trillion-transistor chip give it the performance benefits. Cerebras claims it is 10x faster than the H100 chips in Nvidia’s DGX servers.

“What we are putting together is impossible to achieve on GPUs,” Cerebras CEO Andrew Feldman said during a press conference.

Existing AI installations involve a complex network of interconnected GPUs with independent memory units working in tandem. The distance between processors and integrated memory creates a bottleneck, which leads to slowdowns.

Cerebras has instead put its SRAM memory inside the mega chip, which solves the bandwidth problem.

“Speed converts to quality, more powerful and more relevant answers,” Feldman said.

The results are from a 16-bit data type, which requires speed but generates more accurate answers. Many cloud providers are quantizing down 8-bit or 4-bit data types, which sacrifices quality for speed.

## Cerebras vs. Nvidia
Cerebras may have better hardware, but it isn’t Nvidia, which has its GPUs in some of the most powerful generative AI systems.

OpenAI and Microsoft have built their own hardware, and Google’s AI system relies on TPUs. Nvidia will ship its next generation of Blackwell at the end of this year. Most proprietary and open source large language models are already tuned to run on the GPUs.

Cerebras doesn’t have a software ecosystem, which is built around open source AI models such as Llama and Mistral. Developers will be key in helping the company’s inferencing service succeed, and it has Discord and Slack channels for developers.

That said, Cerebras’ chip is doing well in the high-performance computing and AI training space. It is also working with G42, which is the largest Middle Eastern data center provider, to establish AI data centers in the US.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)