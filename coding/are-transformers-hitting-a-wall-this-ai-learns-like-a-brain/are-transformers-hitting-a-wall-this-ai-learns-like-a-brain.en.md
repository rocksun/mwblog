The team from [Pathway](https://pathway.com/) believes that the transformer architecture developed eight years ago has reached its limits, which no amount of computing can overcome. Nor is there the power available to sustain itself. Further, there’s a lack of temporal reasoning and continual learning.

And so, as discussed in [a research paper Pathway published in September](https://arxiv.org/abs/2509.26507) and our interview at [AWS re:Invent](https://reinvent.awsevents.com/on-demand), the company is building a post-transformer-era frontier model built on neuronal dynamics with dragons in mind — a Dragon Hatchling architecture, inspired by the 20-watt human brain.

“You have neurons that are connected to each other and that talk to each other,” said Pathway CEO [Zuzanna Stamirowska](https://www.linkedin.com/in/stamirowska/). “And once there is a new bit of information that comes into the system —and it may keep on flowing over time, just like for humans — the neurons that are interested fire up, and those who are connected may fire up together with them.”

Neurons firing together integrate Hebbian learning — the concept that “neurons that fire together wire together.” And that small bit of information? Pathway calls it sparse activation; it’s key to understanding the company’s approach. According to the research paper I cited previously, it means about 5% of neural connections fire in the Dragon Hatchling model. The remaining 95% remain silent.

## The Dominance and Limitations of Transformer Architecture

Transformer architecture powers large language models from [GPT](https://thenewstack.io/gpt-5-a-choose-your-own-adventure-for-frontend-developers/) to [Claude](https://thenewstack.io/anthropics-new-claude-opus-4-5-reclaims-the-coding-crown-from-gemini-3/) with [attention mechanisms.](https://thenewstack.io/introduction-to-llms/) These allow the model to weigh the importance of different words in a sentence or document, helping process and manage context and relationships between words.

Transformer technology has achieved so much, affecting the way we live and work. It’s just that its power consumption is unsustainable, and its performance shows diminishing improvement.

Consider the way a transformer learns during training. It sees patterns thousands or millions of times, using [gradient descent](https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent). The process requires repetition after repetition until the system grasps what a small child, or any human, learns with just one experience.

“How many times did you need to taste soap as a kid?” Stamirowska asked. “Once, maybe twice at most. But for a transformer model to taste soap, it literally [needs] thousands or millions of times for it to change the weights in the model so that it could say, ‘Oh, this is [how] soap tastes.'”

## The Problem with Temporal Blindness in Transformers

Current architectures have limits that scaling does not solve, Stamirowska said.

There’s the issue of temporal blindness. “By definition, transformers don’t have the notion of time,” she said. “They don’t see sequences of events that would normally lead us to conclusions that, OK, something is good, something is bad.”

For instance, in training models, a massive amount of data is collected, and then the data undergoes a process similar to a blender before being trained.

Here’s where it gets tricky. The training is done in parallel. All temporal data gets removed. There is no sequencing, only parallelism. All tokens are viewed simultaneously, not in order of time. The goal: maximize throughput. The downside: The concept of time becomes a dimension that the model doesn’t consider, for the sake of speed.

“For any application involving temporal reasoning — from market prediction to system monitoring — this is a fundamental handicap,” Stamirowska said.

## How Memory and Continual Learning Challenge LLMs

Then, there’s the memory problem. Continual learning is not supported the way humans learn. Do you know that a hot stove may burn you? Why? My biological system tells me so.

“LLM transformers won’t be able to incorporate memory and time. Like, kind of learn and kind of generalize over time. They want to do it.”

And it is all so terribly inefficient.

A transformer model learns by gradient descent. Every learning is gradual. It may take 10,000 documents to learn something that a child understands by learning something just once.

Pathway’s approach uses memory in context with neuroscience. It’s a different form of learning compared to transformer models.

“If two neurons fired up, the connection between them will become stronger, right?” Stamirowska said. “And these connections are, in fact, the memory of the system.”

Temporal structure gets preserved instead of discarded. The result is a system that resembles a brain, known as a post-transformer architecture, which operates on GPU scale and, as Stamirowska said, performs “at the level of transformers, actually.”

## Introducing Pathway’s Dragon Hatchling Architecture

Pathway has a team with an established AI pedigree. CTO [Jan Chorowski](https://www.linkedin.com/in/janchorowski/) worked with [Geoffrey Hinton](https://www.cs.toronto.edu/~hinton/), a Nobel Prize winner. Chorowski, one of the first to apply attention to speech recognition, conducted research that dovetailed with the emergence of attention mechanisms and the subsequent development of this field.

[Adrian Kosowski](https://www.linkedin.com/in/kosowski/) leads Pathway’s research and development. Kosowski is a quantum physicist, computer scientist and mathematician with expertise in complex systems.

Stamirowska worked at the Institute of Complex Systems in Paris, applying particle dynamics to forecasting problems, which aligns with the approach they have pursued with their learning mechanisms.

Pathway has built a stream processing framework with more than 100,000 stars on GitHub. Organizations like WhatsApp and NATO use the AI platform, according to Stamirowska.

Dragons serve as the model names for Pathway. The company calls its architecture Dragon Hatchlings because dragons need a nest. Pathway’s Dragon nest has all the connectors for the “hatchlings.”

The nest for the hatchlings is powered by [Pathway’s Live Data Framework](https://github.com/pathwaycom/pathway), a Python ETL (extract, transform, load) framework for stream processing, real-time analytics, large language model (LLM) pipelines and retrieval-augmented generation (RAG).  It’s an incremental data processing engine using [Apache Spark](https://thenewstack.io/is-apache-spark-too-costly-an-aws-engineer-tells-his-story/) that can handle low-latency streaming with the same Python API, Stamirowska said.

Data scientists can code in Python, which gets translated into Rust on an incremental data processing engine, no matter the pace at which data streams into the system.

It’s comparable to [Apache Flink](https://thenewstack.io/building-real-enterprise-ai-agents-with-apache-flink/), she said, but is more like Apache Spark on steroids. And it’s how their platform will gain acceptance in enterprise environments.

The nest is ready. Now it’s time for the Dragons to hatch.

The Dragon Hatchling architecture includes the memory as part of the model. In contrast, a transformer architecture separates the memory.  The whole model does not get scoured, only the applicable neural connectors. And it doesn’t forget: For instance, add a spreadsheet and the model will remember it.

Pathway’s architecture reflects innovations with in-memory architectures that have emerged over the past decade. [Victor Szczerba](https://www.linkedin.com/in/victorszczerba/), now on the Pathway team, led the go-to-market for [SAP](https://www.sap.com/index.html?utm_content=inline+mention) HANA, the in-memory database.

“The state is actually built into the platform … it’s built into the map of learning itself, because it’s kept on the synaptic kind of connections,” Stamirowska said. “So it’s really, like, as a transformer had memory by definition. Intrinsically, this is what we have.”

## A Data-Efficient Approach Inspired by Neuroscience

There are other concepts that Stamirowska addressed in our interview, about how traditional transformers use a lot of energy by constantly firing millions and billions of parameters.

Pathway handles it a bit differently. It relies on neural connections, which allow for efficiencies with its in-memory capabilities.

“So when you fire up the kind of connections and neurons that you need,  you don’t fire up always huge matrices, dense matrices,” she said. “You may have, potentially, a pretty large model, because you can store quite a lot in the structure, but you use only a very tiny portion.”

Pathway’s approach evolves the thinking about AI’s progress beyond its transformer roots.

In sum, the Pathway approach is data-efficient. It provides temporal reasoning and uses minimal energy (think neurons firing vs. data center megawatts). The model is the memory. And it can interpret based on the connections it makes for particular concepts.

The trade-offs? There are plenty. First, transformers do have an advantage, with their eight-year history.  Much could be written about the infrastructure, models and tooling ecosystem. In contrast, the Dragon Hatchling technology is a different type of architecture compared to transformer-based systems.

## The Future of AI Beyond the Transformer Era

Transfomers may be wasteful, but pattern matching has a successful track record. And only until recently has the conversation started to shift to topics of more than just transformers.

Is there an appetite for change? Some signs are there. As Stamirowska said, “It was very difficult to say for an AI researcher that he or she is not working on transformers  … It really wasn’t popular until maybe two months ago.”

At this point, it becomes more of a philosophical question. What’s the future of AI if transformer-based approaches that are really not sustainable?

The transformer era has brought considerable advancements, but it has also created a roaring blaze that can never be satisfied. Perhaps we really do need to be riding dragons, high above the molten landscape.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/13c3d9d6-cropped-0fe18b69-ef774ac85213a6506cf973dc6380cd57.jpeg)

Alex Williams is founder and publisher of The New Stack. He's a longtime technology journalist who did stints at TechCrunch, SiliconAngle and what is now known as ReadWrite. Alex has been a journalist since the late 1980s, starting at the...

Read more from Alex Williams](https://thenewstack.io/author/alex/)