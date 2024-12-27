# AI, Hardware and Open Models: Headed in the Linux Direction
![Featued image for: AI, Hardware and Open Models: Headed in the Linux Direction](https://cdn.thenewstack.io/media/2024/09/38d69a92-does-your-open-source-project-need-foundation-oversight-2-1024x576.jpg)
From the 1960s onwards, IBM’s mainframe systems started the era of proprietary hardware and software, which trickled into the PC era. In the early 1990s, Linux broke that chokehold, emerging as an open source alternative for those tired of proprietary operating systems and hardware.

The AI market is traveling the same path, but the surroundings are different. Open AI models on the rise are shaking up the AI market, breaking a stranglehold of proprietary models running on proprietary hardware.

Cloud providers, including Google and Amazon, are rushing to put open models on their proprietary chips. That’s because consumers of AI models want lower cost and flexibility associated with open AI LLMs. The trend aligns with how Linux grew to now run most of the internet.

“If you want to go fast, go alone. If you want to go far, go together,” said [Fabrizio Del Maffeo](https://www.linkedin.com/in/delmaffeo/), CEO of Axelera, an AI hardware company.

## How Did We Get Here?
The AI era started off much like the PC era, with proprietary Windows software working exclusively on x86 hardware.

The rise of Linux was driven by x86, and “it was Linux plus x86 that became the web stack/LAMP stack,” said [David Kanter](https://www.linkedin.com/in/kanterd/), founder of AI benchmarking organization MLCommons.

“The reality is Linux has truly taken over the proprietary Unixes. Solaris is gone; HP-UX is gone; Tru64 is definitely gone; AIX is still around,” Kanter said.

Open models such as Meta’s Llama and Google’s Gemma are similarly breaking the dominance of proprietary models driving enterprise AI, such as Google’s Gemini and OpenAI’s GPT-4.

Google’s TPU AI chips previously ran only its proprietary Gemini LLM, but the company earlier this year put its homegrown Gemma open model on the chips.

Amazon at Re:Invent made Meta’s Llama 3.1 model with 405 billion parameters available on its homegrown Trainium2 chip.

“Trainium2 is cheaper than comparable Nvidia instances, so taking Llama2 405B and training it against customer proprietary data to create a custom model is a budget-friendly approach,” said [James Sanders](https://www.linkedin.com/in/jamesaltonsanders/), an analyst at TechInsights.

## What Are Open Models?
To be sure, open models and open source AI models aren’t the same. In the world of software, you can modify open source code any way you see fit. There are multiple definitions of what it means to be open in AI.

The Open Source Initiative two months ago [defined open source AI](https://thenewstack.io/the-open-source-ai-definition-is-out/) as “applied to a system, a model, weights and parameters, or other structural elements.” That included all the training data.

Meta’s Llama doesn’t fit the OSI definition, but it is mostly open with some restrictions. Users can use Llama as a pretrained model and finetune it to specific needs. But users can’t access or modify Llama’s pretrained data, as Meta doesn’t want to reveal the sources of data it used to pretrain the model.

Proprietary models like Gemini, Claude and GPT-4 are completely closed.

## Like Linux, Lock in Customers
Cloud providers are following the footsteps of Linux OS providers like Red Hat — wrapping the open source OS with proprietary tech and locking customers into the software stack.

The open AI models are a low-cost way to lure customers to cloud services. Once customers are locked into a cloud service provider, it is hard to leave.

“The motive is to get more customers using their services that surround AI like the compute, data management, security and storage,” said [Patrick Moorhead](https://www.linkedin.com/in/patmoorhead/), principal analyst at Moor Insights and Strategy.

AWS’s Trainium2 hasn’t set the world on fire, so porting Llama to Trainium2 brings more value to its chips. At Re:Invent, AWS also announced its homegrown Nova models, which will run on Trainium.

AWS wants broad coverage of use cases, said [Naveen Rao](https://www.linkedin.com/in/naveen-rao-bba5b01/), vice president of artificial intelligence at Databricks. Rao sold his company, MosaicML, to Databricks in 2023 for $1.3 billion.

“Supporting more models increases the relevance for a piece of hardware, so that’s likely the main reason. And it’s not a huge lift for them,” Rao said.

## The Open Edge
Open source and open models are advantageous for cloud-captive AI accelerators.

“The ideal state is to provide a familiar environment with minimal friction at a lower cost,” Sanders said.

Open models also allow creation of open source model derivatives, smaller and optimized, which can better fit industry-specific requirements.

“Adding open models to the catalog allows them to increase customer bases and monetize the services,” Del Maffeo said.

Groq, Sambanova, Cerebras and other small hardware providers are also providing open models as a service at very low token cost.

## The Linus of Open AI Models
It can be notoriously difficult to load open AI models on Google’s TPU and AWS’s Trainium. Open models need specialized forks for custom chips.

Open models are typically built on frameworks and toolchains such as PyTorch, JAX or TensorFlow. Developers use the framework’s built-in tools and APIs to measure the performance and fix it with techniques that include optimizations for the architecture and chips.

By comparison, Nvidia’s GPUs are generic AI accelerators that can run just any PC or AI application.

HuggingFace is driving open source AI growth on proprietary hardware. It provides hundreds of open models that have proven similar accuracy and performance to more power-hungry models.

AWS is [partnering](https://aws.amazon.com/ai/hugging-face/) with Hugging Face to train and deploy models on Trainium.

“Now that the market is accelerating, it’s natural to see Amazon opening access on its infrastructure to any other open source model,” Del Maffeo said.

HuggingFace in July announced AI models were [available](https://huggingface.co/blog/tpu-inference-endpoints-spaces) for deployment on Google Cloud TPUs.

“With more concerns around the increasing power consumption, cooling requirements and cost to train large models, innovations from the community that help alleviate these challenges are welcomed,” Del Maffeo said.

More developers are also gaining experience in machine-learning development, and the community capability can cover the needs of a large part of the AI market.

## Changing Definition
Enterprises already use a mix of open and closed source models.

“As of now, the architecture of all models is largely the same,” Rao said.

From a hardware perspective, the difference between open and closed models is much more about the data and training regimen than it is about the architecture of the model, he said.

“You could argue that all models that run on hardware are open source or derivatives of open source architectures. That might change in the future with this whole inference time-scaling idea like [GPT-4o1](https://openai.com/index/introducing-openai-o1-preview/),” Rao said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)