# Why Upstage Builds Small Language Models
![Featued image for: Why Upstage Builds Small Language Models](https://cdn.thenewstack.io/media/2025/01/19e82884-lucy-park-upstage-2-1024x576.png)
LAS VEGAS — [Upstage](https://www.upstage.ai/) is a South Korean enterprise AI company that builds [small language models](https://thenewstack.io/small-language-models-vs-llms-what-theyll-mean-for-businesses-in-2025/) (SLMs)to help companies solve document processing problems. It originated as a company using optical character recognition (OCR) to scan documents for large corporations in South Korea.

When [ChatGPT](https://thenewstack.io/openai-launches-new-chatgpt-interface-designed-for-coding/) emerged, customers started asking Upstage about [large language models (LLMs)](https://thenewstack.io/llm/). Upstage had provided 95% accuracy using its OCR capability, but customers wanted 100% accuracy. So, the Upstate team began looking at models that would fit the requirements for getting better accuracy. The LLMs serve a general purpose, but the smaller models were more applicable to the narrow focus that document processing requires.

There’s not much attention paid to SLMs, but their capabilities have uses that include providing company-specific or even country-specific LLMs.

“Customers wanted a language model that was fit for their own use,” said [Lucy Park](https://www.linkedin.com/in/echojuliett/), co-founder and chief product officer, in an interview at [AWS](https://aws.amazon.com/?utm_content=inline+mention)[ re:Invent](https://reinvent.awsevents.com/on-demand/). “So that’s one of the reasons we started out to build small language models. And so here we are working on document processing engines and large language models.”‘

## Model Merging to Create SLMs
Upstage, an [AWS Generative AI Accelerator](https://aws-startup-lofts.com/amer/program/accelerators/generative-ai) participant uses open source models, allowing running on a single GPU. Its flagship model, Solar, compares to other small models that also run on a single GPU, including Llama 3.81 B, Mistral Small Instruct 2409, and [Hugging Face’s](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/) ExaOne3.0 7.8B Instruct.

Park said Upstage merges two copies of a small LLM into a large LLM. For instance, it would integrate a 7 billion parameter model into a 10 billion parameter mode. “If we have a 14 billion model, we explode that into a 22 billion model,” she said. “So that’s what we have been doing recently.”

Model merging, a technique for combining LLMs has gained acceptance in the AI community. Implementation includes such practices as weight averaging, a method that merges the parameters of multiple separate models with different capabilities. Model merging allows data scientists “to build a universal model without needing access to the original training data or expensive computation,” according to a[ paper published in August by researchers ](https://arxiv.org/html/2408.07666v1)from Nanyang Technological University, Northeastern University and Sun Yat-sen University.

Park said Upstage has found increases in its benchmarks using a combined model approach. According to the Upstage site, Solar Pro is a small language model that shows a 64% improvement in Eastern Asia language mastery compared to Solar Pro preview.

The improvements in SLMs for languages reflect their growing popularity. SLMs train smaller data sets, making them flexible for domain-centered approaches like Upstage’s.

Park said the large language models focus on general intelligence. The small language models also provide a narrower focus.

For example, Upside built a specific model for the Thai language. With Thai, it’s similar to[ GPT 4](https://thenewstack.io/gpt-4o-and-sql-how-well-can-an-llm-alter-its-own-schema/), the[ OpenAI](https://thenewstack.io/openai-launches-new-chatgpt-interface-designed-for-coding/) model.

SLMs also cost a lot less to develop. Hypothetically, Park said, imagine an SLM that costs $10 to build. An LLM that is 10 times bigger may cost $100.

Customers will pursue three options to deploy the models, she said. If they are deploying on-premise models, they can use the Upstage console, which provides APIs through the AWS marketplace. For example, the Solar Pro model is now available on the Amazon Bedrock Marketplace.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)