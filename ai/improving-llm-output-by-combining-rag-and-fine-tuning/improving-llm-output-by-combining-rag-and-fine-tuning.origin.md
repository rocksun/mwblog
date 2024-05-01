# Improving LLM Output by Combining RAG and Fine-Tuning
![Featued image for: Improving LLM Output by Combining RAG and Fine-Tuning](https://cdn.thenewstack.io/media/2024/04/e3e72775-llm-finetuning-rag-1024x576.jpeg)
[Large language models (LLM)](https://thenewstack.io/7-guiding-principles-for-working-with-llms/) and conversational AI have great potential to make applications easier to use, particularly for new users. They can answer questions about the product, copilot the platform, summarize data and do much more to help users get up to speed quickly.
While there is tremendous excitement about the use of LLM, there is also a lot of skepticism about whether this tech is “enterprise-ready.” Specifically, the tech industry wants to know how to best customize these tools for specific use cases and domain-specific knowledge. Trying to use off-the-shelf LLM models or ChatGPT can result in random answers and hallucinations since they do not have product-specific domain knowledge. This could cause enterprise customers to lose trust or worse, lead them to make bad decisions based on incorrect suggestions.
At
[Conviva](https://www.conviva.com/), we were excited to use LLMs to simplify how customers use our product. For background, Conviva provides quality experience monitoring for many of the leading media and entertainment companies around the world. Customers interact with our interactive drill-down systems to get real-time insights into their users’ quality of experience. Traditionally, new users had to refer to our product documentation or engage with customer service specialists to answer “semantic” questions; e.g., How is a specific [quality of experience (QoE) metric](https://thenewstack.io/why-observability-cant-measure-what-really-matters/) defined? What does a specific client-side attribute or /dimension mean? What is a good range of values for a specific QoE metric?
In the summer of 2023, we decided to build and operationalize a conversational Q&A solution called Conviva PromptAI. This conversational copilot is being used by over 100 users at more than 20 enterprise-grade customers daily.
In designing Conviva PromptAI, we had three key top-level questions to answer:
- Should we host our own LLM or use APIs for third-party services?
- What language model should we use?
- How do we best teach the LLM our domain? Fine-tuning?
[Retrieval-augmented generation (RAG)](https://thenewstack.io/retrieval-augmented-generation-for-llms/)? Something else?
We’re sharing our experience and learnings in the hope it can be more broadly useful to other enterprises embarking on a similar journey.
## Host or Use an API?
Our first question was whether to use an
[open source LLM](https://thenewstack.io/large-language-models-open-source-llms-in-2023/) model or a cloud service solution like OpenAI. In general, OpenAI’s model (GPT-4) has higher accuracy than its open source counterparts. However, the open source models provide greater control over hyperparameters, the ability to fine-tune and better ways of combining different models together easily.
Our core product has a lot of things that require specially-made models and configurations. We also want to continue our investment in the LLM technology, which requires a high level of control and flexibility. These factors led us to choose the open source path and host our own models instead of using third-party services.
## What’s the Right Language Model?
After deciding to leverage an open source LLM, the next hurdle was selecting the ideal model to meet our needs. When our project kicked off last year, we settled on Llama2 70B. At that time, Llama2 stood out as the most robust open source LLM available, as it offered the broad general performance we require. We specifically chose the 70B variant over its smaller counterparts, the 7B and 13B models, as it provided more comprehensive and detailed explanations tailored to our context.
When deciding which LLM is best for your use case, comparing benchmark scores such as
[MMLU](https://github.com/hendrycks/test) or [HellaSwag](https://rowanzellers.com/hellaswag/) can help. Since we selected Llama2, the landscape has evolved with the introduction of other open LLMs, such as Mixtral 8x7B, DBRX and Grok-1.5. We are currently evaluating these alternatives, but at this time we don’t believe there is significant value to switching, given the more serious challenges in domain adaptation.
## Fine-Tuning, RAG or Both?
There are three natural options for teaching the LLM the contextual domain knowledge required to guide its answers:
[Prompt engineering](https://roadmap.sh/prompt-engineering)
- Retrieval-augmented generation (RAG)
[Fine-tuning](https://thenewstack.io/what-is-a-large-language-model/)
As our goal is to help customers, letting users perform prompt engineering is not an option: Since users may not even know how to phrase the prompts, we cannot expect prompt engineering to deliver the desired user experience! Therefore, RAG and fine-tuning were our only options.
To understand the differences, think about training an LLM as a student preparing for an exam. RAG is like taking an open book exam. The LLM can access the relevant information using any retrieval mechanism, such as web browsing or database queries. Fine-tuning is like taking a closed-book exam. The LLM needs to memorize new knowledge during the fine-tuning process, and it answers questions based on its memory.
The table below summarizes the pros and cons of these two canonical approaches.
|
RAG |
Fine-tuning
|
Effort required to curate training set |Zero
|Very high
|
Accuracy |Limited by performance of retrieval
|Not very good at handling detailed information, may hallucinate
|
Freshness of data |Easy
|Expensive to retrain and maintain freshness
RAG is easy to start with and can work with out-of-the-box pretrained models.
If a user asks “What is the definition of buffering ratio?” information about other metrics would not be helpful for answering it. RAG converts a user question into an embedding and then searches the prepopulated vector database to find documents “similar to” the user’s question. Then these documents are provided as part of the context inside the LLM prompt to answer the user’s question.
However, RAG still has limitations with providing correct answers. This is especially true when a user’s question doesn’t directly relate to the content in the documentation.
Consider a situation where a user asks for the top five metrics they should monitor. In practice, each metric might have specific documentation, but there may not be a single document that ranks the metrics directly. Therefore, the retrieval process struggles to use similarity scores effectively to identify the correct metrics to answer the question.
RAG is not well-suited for questions that require examining nearly all available documents to find an answer. It operates under the assumption that only a few documents are needed to respond to any given question.
![Comparison of RAG and fine-tuning](https://cdn.thenewstack.io/media/2024/04/c4baa5b7-rag-finetuning-comparison-1024x757.png)
Comparison of RAG and fine-tuning: RAG (left) fails to retrieve the proper documents to answer the question. However, fine-tuning (right) can help extract knowledge from all documents to answer the question.
Fine-tuning is better at extracting knowledge from all available documents to answer a question. However, we’ve found that fine-tuning is not without its own set of problems. In some cases, fine-tuning is not as accurate as RAG when handling very detailed information. While this can be attributed to our training dataset, it is a practical problem to create the right training dataset to overcome only with fine-tuning. Second, fine-tuning is weak on refreshing information based on the latest available content. Last but not least, fine-tuning is very resource intensive. It is essentially a training process and thus requires non-trivial amounts of machine resources. This could become a blocker for companies that do not have enough GPUs. The process also takes a long time and requires a lot of trials and errors.
## Our Approach: Combining Fine-Tuning With RAG
Our experiments made us realize that, on their own, fine-tuning and RAG are not sufficient. To get the best of both worlds, we adopted a hybrid approach that merges fine-tuning with RAG.
This table summarizes the pros and cons of the three approaches.
|
RAG |
Fine-tuning |
Our approach
|
Effort required to curate training set |Zero
|Very high
|RAG + synthesizing data for fine-tuning
|
Accuracy |Limited by performance of retrieval
|Not very good at handling detailed information, may hallucinate
|Use fine-tuning to increase retrieval accuracy
|
Freshness of data |Easy
|Expensive to retrain and maintain freshness
|Use RAG for the latest information
The high-level idea behind our approach is improving the retrieval process through a fine-tuned model. As mentioned earlier, one of the challenges for fine-tuning is creating a training dataset. However, once we prepare the documents for RAG, we can directly use them for fine-tuning. We also synthesize more data by leveraging the LLM to rephrase the existing document.
The figure below shows the overall workflow of merging RAG and the fine-tuning model. For a given user question, the fine-tuned LLM generates an initial answer speculatively. Then this response is used to get related documents. Finally, the LLM creates an answer that combines retrieved documents and the original user question. Adding the fine-tuned model makes a huge improvement in the accuracy of retrieval and the quality of the final answer.
![Merged RAG and fine-tuning workflow](https://cdn.thenewstack.io/media/2024/04/5d90f3ed-merged-rag-finetuning-model-1024x84.png)
Merged RAG and fine-tuning workflow.
As we rolled out the system, we also implemented a simple user score mechanism to collect data on satisfaction with responses from internal experts and our customers. With the merged approach, we saw significantly improved results in our internal user testing that gave us confidence about its higher quality.
## Conclusions
PromptAI has significantly enhanced the value we provide our customers. Instead of navigating through extensive documentation, our users can now directly inquire about their needs and concentrate on resolving issues with the assistance of PromptAI.
The proof, as they say, is in the pudding, and the ultimate validation is the feedback we have received. As one customer said, “
*I don’t have time to look through dashboards during a live event — I need to ask someone a question about why something is happening and trust that it’s right. This is the direction that I’d like to see this going in.”*
This innovation is possible thanks to recent innovations in LLMs and the availability of high-fidelity open source models. While our experience suggests there is some “lift” required to make it use-case-ready and adapt it to domain knowledge, the ROI is well worth it.
We hope by sharing our key learning and design choices, we can inspire and help other enterprises embarking on a similar journey to leverage the power of LLMs.
[Vyas Sekar](https://thenewstack.io/author/vyas-sekar/) also contributed to this article. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)