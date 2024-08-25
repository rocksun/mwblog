# Use Small Language Models To Deploy AI on a Budget
![Featued image for: Use Small Language Models To Deploy AI on a Budget](https://cdn.thenewstack.io/media/2024/08/5415ea9f-abc-3523453_1280-1024x682.jpg)
AI is upending the tech industry. The talk of [artificial general intelligence](https://thenewstack.io/ai/) (AGI) and its ability to replace humans is ubiquitous. Whether the future is in a decade or a year, many teams need help making the most of AI.

Only a handful of companies maintain the LLMs we know — GPT, Claude, Bard, LaMDA, LLaMA, etc. — because the resources required for training are prohibitively expensive. [LLMs](https://thenewstack.io/how-llms-guide-us-to-a-happy-path-for-configuration-and-coding/) are trained on [enormous data sets](https://thenewstack.io/how-to-scale-rag-and-build-more-accurate-llms/).

These models are just the start. They offer an incredible platform to build a more effective and tailored solution: small language models (SLMs) trained on your specific data.

**What Makes an SLM Small?**
In short — the number of parameters. To understand the value of an SLM to real-world applications, you have to appreciate the verbosity of an LLM. OpenAI’s GPT-3 has 175B parameters, and Meta’s Llama 3.1 has a version with 405B parameters. But what does that mean?

LLMs consume, interpret, and generate human language using the transformer model to tokenize and analyze data utilizing parameters. If you’ve done any reading, you’ll likely see that “token” and “parameter” are used interchangeably, but they’re different.

Tokens are discrete units of data to LLMs. In the example below, each word is ingested by the LLM as a token. Depending on the model, tokens can be words, phrases, characters, etc. Tokens allow the LLM to break apart data and evaluate it efficiently. For example, an LLM may interpret the word “cats” the same as “cat” to standardize the information.

Simply put, parameters are the rules — the weights and biases — that the LLM uses to evaluate data. Parameters allow the LLM to emphasize particular words more to establish context and meaning. The parameters also link words; in the example below, “future” and “it’s” refer to the same thing.

You’re probably asking yourself, “Are more parameters better?” Well, like all things in tech, it depends. If you have to hang a painting on your wall, is every tool in Home Depot better than a hammer and a nail?

LLMs are incredible feats of technology, and their ability to compute vast amounts of information better and faster is improving daily. However, the cost and time required to train and fine-tune an LLM are out of the question for most companies. They’re just too big. Most businesses don’t need an all-in-one tool but a specific tool for a particular task.

This is where SLMs shine.

**Training the Model on Your Data**
Whereas LLMs must be trained using significant cloud resources, training SLMs uses proprietary data and is compute-efficient and cost-effective.

Imagine you’re a government contractor who responds to requests for proposals (RFPs) to secure contracts. Typically, you’ll have a team review those RFPs, manually collect the appropriate information required to respond, answer detailed questions about how your company will fulfill the needs of the contract, and write a full proposal, including the job roles required and the corresponding government codes for those jobs.

The RFPs are never published publicly, meaning an LLM can’t be trained on them, and the hundreds, if not thousands, of proposals your company has written are proprietary.

Imagine if you could train an SLM on all your proprietary data and have the SLM generate detailed proposals on your behalf. Can you imagine how much time your team would save? You can do this by starting with a foundation model, like [Llama 3.1](https://llama.meta.com/docs/get-started/), and fine-tuning the SLM on the previous RFPs and corresponding proposals. You can also use a tool like [Arcee.AI](http://arcee.ai).

In either case, and to get the most from your SLM, you’ll want to accomplish four key steps: 1/ continual pre-training, 2/ alignment, 3/ model merging, 4/ retrieval augmented generation (RAG), and 5/ continuous adaptation.

**Understanding the Steps of Training an SLM**
Imagine our small language model is Dominique, a sophomore in high school. Pre-training is everything Dominique learned in all the years prior — math, science, language arts, sports, art — everything. Model merging is when I paired Dominique, who excels in math, with Asma, who excels in science and had them learn and test together for the rest of the year. Despite being particularly good in one topic, they’ll be exceptional in two topics.

Regarding alignment and fine-tuning, instruction-tuning (the first part of alignment) can be described as the lessons Dominique is taught her sophomore year. The critique phase (the second part of alignment) is the feedback given to Dominique on her homework. RAG is like giving Dominique an open-book test; she can look up relevant information to help her get a better grade. Finally, continuous adaptation updates Dominique’s knowledge as information changes (e.g., Pluto is no longer a planet), so she has the latest, most up-to-date information.

**Implementing Your Model**
In the government contractor’s example, they want to build an SLM to write proposals. The developers would take a smaller open source model, like Llama in one of its smaller versions (70B or 8B parameters), and train it using the proprietary data of their previous proposals, previous RFPs, and any other relevant text data.

That model can then be merged using an open source tool — either a more generic model that specializes in language or another domain-specific model. For example, if they had a model that specialized in creating proposals for the Army (using specific jargon and terms) and another model that specialized in writing proposals for building rockets, they could be merged to write highly specialized and accurate proposals for building Army rockets. Remember that models can only be merged if they share the same architecture and size.

From there, they’d want to align that freshly merged model to ensure it’s delivering the desired results. That includes providing examples of what is expected and interacting with the model to test whether it’s generating the desired type of content.

Although tools like Arcee.AI can get the same results without RAG, if you’re building from scratch, you can use an RAG layer to allow it to accurately retrieve specific information and generate more accurate text or have real-time data retrieval. For example, government job codes would be an excellent piece of data to keep at the RAG layer.

Finally, just like humans, an SLM is ever-evolving and ever-learning. Once deployed, models can be updated as business data and demands change. Depending on the frequency of your new data, plan to retrain your models every six to 12 months.

**Making the Most of AI**
LLMs only take you so far and provide no real market differentiator. After all, you’re using the same data as everyone else — generic information gathered from (usually open source) data.

SLMs are a much more cost-effective approach, allowing companies to adapt models to their proprietary data in secure environments. Not to mention that SLMs are kinder to the planet by using significantly fewer compute resources and are much greener in energy. The level of responsiveness and adaptability offered by SLMs is unmatched by current generative AI technology. It provides the ultimate path to use generative AI to improve your business.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)