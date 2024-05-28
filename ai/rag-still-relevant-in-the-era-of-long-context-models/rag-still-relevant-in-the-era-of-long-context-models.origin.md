# RAG: Still Relevant in the Era of Long Context Models
![Featued image for: RAG: Still Relevant in the Era of Long Context Models](https://cdn.thenewstack.io/media/2024/05/1b558d74-color-3498348_1280-1024x577.jpg)
Google recently released
[Gemini 1.5 Pro](https://gemini.google.com/app), a [large language model ](https://thenewstack.io/do-enormous-llm-context-windows-spell-the-end-of-rag/)boasting a mammoth one million token context window. This sparked a buzz in the AI community, with some dubbing it the “RAG killer.”
Before we rush to write eulogies for retrieval-augmented generation (RAG), let’s take a deep breath and analyze the situation from an enterprise perspective. Extremely long context windows may get data science teams to a working pipeline faster, but does a deployment speed advantage justify an application that costs many times as much to run in production?
Probably not.
Enterprises need applications that achieve high performance in a small footprint. That means choosing and customizing a right-sized foundation model along with the entire supporting
*LLM system* ecosystem around it. Highly customized RAG systems simply provide better value for high-throughput tasks.
But these technologies can co-exist. While RAG will remain a staple of production applications, Gemini 1.5 Pro and similar models will help enterprise data science teams experiment and iterate faster.
## RAG’s Obvious Advantage: More Tokens = Higher Cost
Injecting more context into large language model (LLM) prompts means paying for more processing power — whether that’s directly with per-token charges through an API, or indirectly through the cost of computational resources. Data scientists and developers, therefore, must carefully consider how much context is the right amount for each task.
In a way, this is a nice problem to have. Early LLM-backed applications typically used the entire context window and struggled to optimize what context to fit into it. As context sizes increased from 1,000 tokens to 16,000 tokens and now one million tokens, development pressure has shifted from prioritizing the most important documents to deciding where performance gains no longer justify the price of additional text.
No matter how an enterprise pays for its
[LLM usage](https://thenewstack.io/clean-data-trusted-model-ensure-good-data-hygiene-for-your-llms/), more tokens mean higher operating costs. Very few tasks require a million tokens of context.
## RAG’s Modularity Advantage
The modular architecture of RAG-based applications offers valuable flexibility. Gemini, like most LLMs, is a black box. It undoubtedly works well on some topics and tasks and less well on others. If an enterprise data science team built an application that used Gemini 1.5’s entire context window, they would have a difficult time replacing Gemini with another model — at least until a comparable competitor reaches the market.
That’s not true with RAG-based applications. RAG-based LLM systems allow data science teams to swap out and
[ customize each component](https://thenewstack.io/red-hat-podman-lab-gets-developers-started-on-genai/) to their specific needs.
Snorkel AI recently worked on a RAG-based project with a banking customer. The customer needed the system to accurately answer questions about contracts. The project started with off-the-shelf components (GPT-4 as the LLM with LlamaIndex for RAG) and scored 25% accuracy — quite far from deployment benchmarks.
In their first sprint, our engineers added components to the application to intelligently chunk and tag source documents. The off-the-shelf version of the application struggled to identify which texts contained dates. Our team added a lightweight helper model that explicitly tagged document chunks predicted to contain date information. They also optimized the prompt template and fine-tuned the embedding model on the domain-specific data. In just three weeks, they improved system accuracy to 79%.
Later work pushed the accuracy to 89%, but they achieved their first 54-point gain without modifying the off-the-shelf LLM at all. That’s the power of RAG’s modularity.
## Better Data Development Builds Better LLM Systems
Our engineers’ 64-point accuracy gain would have been impossible without top-quality data development guided by our client’s subject matter expert.
To train the date-tagging model, we needed examples of passages that did and did not mention dates. Our engineers didn’t immediately know what kind of subtle date references to expect, but the subject matter expert did. The SME identified a small number of passages with oblique or subtle date references, and wrote a brief explanation for why they tagged it.
When it comes to production use cases, RAG will win out. Its modularity, multiple points of customizability and comparative cost-effectiveness make it the better choice for enterprise AI.
Our engineers then encoded the SME’s explanations as labeling functions in the Snorkel Flow AI data development platform. The platform quickly labeled a large number of documents, and our engineers then checked the accuracy of their labeling functions against the SME’s ground truth. This allowed them to identify shortcomings and iterate until they produced a high-quality dataset capable of training a high-accuracy helper model.
In the end, our client’s SME spent more time verifying the accuracy of the model than they did labeling data.
While this kind of data development is technically possible with non-programmatic approaches, it’s neither efficient nor practical.
## Where Gemini 1.5’s Million-Token Context Window Fits in
While I would not recommend any enterprise to build a production LLM system that uses Gemini 1.5 pro’s full-context window, Google’s noteworthy achievement has a place in
[enterprise AI development](https://thenewstack.io/devs-get-ai-pixie-dust-at-google-i-o-but-no-search-updates/).
Long context models will accelerate simpler and preproduction use cases. That’s a lot of enterprise AI today! Gemini and others will let data science teams complete proof-of-concept applications faster than they can now. Once they’ve proven the concept, they can move on to building a robust, modular and highly customized RAG-based application.
## Customized RAG > Long Contexts in Production Applications
Gemini 1.5 represents a significant technical achievement. I applaud the researchers and engineers at Google for what they’ve done. Gemini and other long context models will hold an important place in enterprise AI. Allowing data science teams to handle challenging one-off questions and finish rough drafts of applications faster will yield real business value.
But, when it comes to production use cases, RAG will win out. Its modularity, multiple points of customizability and comparative cost-effectiveness make it the better choice for enterprise AI.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)