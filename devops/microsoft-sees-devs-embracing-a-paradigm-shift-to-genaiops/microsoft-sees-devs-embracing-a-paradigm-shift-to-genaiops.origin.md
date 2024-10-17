# Microsoft Sees Devs Embracing a ‘Paradigm Shift’ to GenAIOps
![Featued image for: Microsoft Sees Devs Embracing a ‘Paradigm Shift’ to GenAIOps](https://cdn.thenewstack.io/media/2024/10/a92e2bdd-the-blowup-pguirt0m-m0-unsplash-1-1024x703.jpg)
Organizations and developers continue to try to keep up with the unprecedented rate of innovation around [generative AI (GenAI)](https://thenewstack.io/generative-ai-in-2023-genai-tools-became-table-stakes/) as they look to make the emerging technology work for them.

The rapid enterprise adoption of GenAI after OpenAI first introduced its ChatGPT chatbot almost two years ago led to the need to bend the technology to the will of business through the fining tuning of AI models and use of [retrieval-augmented generation](https://thenewstack.io/writer-coms-graph-based-rag-alternative-to-vector-retrieval/) (RAG), a process that allows organizations to augment the training of [large language models (LLMs)](https://thenewstack.io/llm/) with their corporate data so that the AI that comes out is more accurate and more specific to their needs.

Likewise, there has been a steady evolution of the tools and processes for managing, scaling, and operationalizing AI models. [MLOps for machine learning environments](https://thenewstack.io/kitops-is-the-open-source-tool-that-turns-devops-pipelines-into-mlops-pipelines/) evolved into LLMOps to address the rise of large language models.

Now comes GenAIOps, which has been on the scene for months and promises to become the go-to process for developing, testing, and deploying GenAI solutions. In a recent blog post, [Yina Arenas](https://www.linkedin.com/in/yinaa/), vice president of product for Microsoft’s AI core platform, called the move from [MLOps and LLMOps to GenAIOps a “paradigm shift”](https://techcommunity.microsoft.com/t5/ai-ai-platform-blog/the-future-of-ai-the-paradigm-shifts-in-generative-ai-operations/ba-p/4254216) that better encompasses what the technology has become.

“GenAIOps extends beyond LLMOps to address the full spectrum of generative AI operations, including [small language models (SLMs)](https://thenewstack.io/the-rise-of-small-language-models/) and multimodal models,” Arenas wrote, noting that it comprises everything from practices and tools to foundational models and frameworks. “This shift moves from merely managing large models to ensuring continuous development, deployment, monitoring, and governance of generative AI applications.”

She lays out the operational challenges organizations face when deploying and scaling GenAI, from the quality and quantity of the data being fed into models to performance, efficiency, cost, security, and compliance.

## Finding the Right GenAI Model
Another hurdle is navigating a complex landscape of GenAI models to find the right ones that not only address performance needs but also integrate well with an enterprise’s existing infrastructure. [Nick Patience](https://www.linkedin.com/in/nickpatience/), the AI lead for analyst firm [The Futurum Group](https://futurumgroup.com/), called finding the right model a daunting task, adding that “there are thousands to choose from, both commercially licensed and open source, and the open source model landscape is proliferating at a rapid pace.”

“One of the key differences with GenAI compared to classic machine learning is that in almost all cases, the GenAI model was not built by the developers’ organization; rather it licensed it or accessed it via an API or downloaded it from an open source repository such as [Hugging Face](https://huggingface.co/),” Patience told The New Stack. “That puts a greater importance on choosing the right models for the task. Contrast that with narrower predictive models using classic machine learning which were usually built and trained using the organization’s own data.”

Many LLMs are massive in size and GenAIOps will bring a more orderly process to collecting, curating, cleaning, and creating proper data sets and the proper measured creation of models with specific checkpoints, [Andy Thurai](https://www.linkedin.com/in/andythurai/), principal analyst at [Constellation Research](https://www.constellationr.com/), told The New Stack.

“Otherwise, it will lead to chaos for many reasons,” Thurai said. “This can also lead to huge infrastructure costs if the models are not trained properly. So far, many developers use random techniques and procedures to create ML models or even LLMs. These defined processes, technologies, and procedures bring some order to the creation, deployment, and maintenance of those models.”

## A Transformation Is Underway
Arenas’ blog is the opening salvo in what will be a series that will go deep into [Microsoft’s GenAIOps framework](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/concept-llmops-maturity?view=azureml-api-2), but she makes clear that GenAI will transform how organizations operate and the roles within them.

“Data teams will become AI insight orchestrators, while IT operations evolve into AI infrastructure specialists,” she wrote. “Software developers will routinely incorporate AI components, and business analysts will translate AI capabilities into strategic advantages. Legal teams will also incorporate AI governance, and executives will drive AI-first strategies.”

Responsible innovation of the technology will be key and lead to instituting AI ethics boards and centers of excellence, something Futurum’s Patience is also seeing. AI governance will become part of GenAIOps, he said, with less of a focus on performance and more on its impact on users in terms of such issues as bias, ethics, and privacy.

There is also the issue of security. GenAI creates what he called novel security risks because developers can control the inputs and have even less control over puts than what they have with more narrow traditional predictive models.

“Then there are broader data-related challenges posed by the use of techniques such as fine-tuning and retrieval-augmented generation,” Patience said. “GenAIOps needs to be able to handle this as well.”

## The Direction Is Clear
GenAIOps comes as businesses continue to adopt the technology. A report by Bain Capital in June said that [nine in 10 businesses have deployed](https://www.bain.com/about/media-center/press-releases/2024/generative-ai-virtually-ubiquitous-in-global-business-as-the-technology-spreads-at-a-near-unprecedented-rate--bain--company-proprietary-survey/#:~:text=Bain's%20latest%20proprietary%20cross%2Dindustry,rapidly%20across%20all%20use%20cases.) or are piloting GenAI technology and that in about 75% of cases, it met or exceeded expectations.

“GenAI is now virtually ubiquitous in global businesses, with major companies having strongly prioritized commitments to it and AI deployments having spread at a near unprecedented pace for adoption of a new technology that is still accelerating,” the report’s authors wrote.

According to market research firm Statista, the global GenAI market is expected to reach more than $36 billion this year and hit [$356 billion by 2030](https://www.statista.com/outlook/tmo/artificial-intelligence/generative-ai/worldwide), growing an average of 46.47% a year during that time.

Patience said he expects businesses and developers will likewise grow their embrace of GenAIOps.

“I see GenAIOps becoming a key part of the overall application development process as AI is increasingly integrated into it,” he said. “The distinction between GenAIOps and MLOps will blur and even possibly disappear as developers seek a common set of tools to deal with AI models, whether they are traditional deterministic ones or probabilistic ones.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)