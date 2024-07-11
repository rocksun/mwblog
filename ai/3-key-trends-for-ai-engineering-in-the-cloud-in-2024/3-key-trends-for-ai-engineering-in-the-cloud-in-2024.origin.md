# 3 Key Trends for AI Engineering in the Cloud in 2024
![Featued image for: 3 Key Trends for AI Engineering in the Cloud in 2024](https://cdn.thenewstack.io/media/2024/07/8a745e85-george-c-hsyq2hk91lo-unsplash-1024x576.jpg)
The last 20 years of innovation have given us inflection points where whole new classes of jobs have been created. Think of the rise of the cloud architect and developer after AWS launched in 2006, the mobile developer with the rise of the iPhone and Android, the machine learning engineer when we finally had enough data and compute power to make neural networks work, and then the emergence of the data scientist when those first three trends merged.

“If you wanted to be an AI developer 18 months ago, you had a big hill to climb. […] Now we’re to the point where having an idea and realizing it, you might be able to do that over lunch.”

– Simon Margolis, associate CTO of AI and ML at SADA
Following that path of evolution, we may have now reached another inflection point: the AI engineer. The AI engineer came into vogue in the last couple of years and is on the frontline of using [Large Language Models and associated tooling](https://thenewstack.io/top-5-ai-engineering-trends-of-2023/) to build out generative AI chatbots, agents, and other capabilities.

As foundation models and AI engineering mature, some trends are starting to emerge. We spoke with [Simon Margolis](https://www.linkedin.com/in/smargolis/), associate CTO of AI and ML at [SADA](https://sada.com/), a Google Cloud vendor, about what they are seeing in the current AI engineering landscape and what we might see next.

“It depends on where you are on the kind of overall adoption curve for generative AI,” Margolis said. “You’ve got folks that are still just kicking tires, getting their feet in the water, and then you have folks that were doing generative AI work well before ChatGPT was kind of a household name. Where folks are on that spectrum, I think, has a lot to do with what their major trends are.”

Overall, Margolis identified three key trends for AI engineers halfway through 2024: 1) the ability to build [AI agents](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/) with low or no code or technical knowledge; 2) combining AI modalities such as machine learning and generative AI; 3) using generative AI to help build generative AI agents.

## Building AI Agents Without Code
Two of the major generative AI platforms, Google Cloud and OpenAI, have worked to make it easier for AI engineers to build AI agents without having to fuss too much with the foundation models or vector databases themselves. Both have introduced tools to build agents, with Agent Builder in [Vertex AI](https://thenewstack.io/an-introduction-to-google-vertex-ai-automl-training-and-inference/) at Google Cloud, and [GPTs](https://thenewstack.io/getting-started-with-openais-gpt-builder-and-how-it-uses-rag/) at OpenAI.

“On the early adopter side of things, one of the biggest things we’re seeing a lot of uptick in is the concept of being able to build generative agents without being deeply technical,” Margolis said. “Whereas maybe two years ago, you needed to be really conversant in things like transformers and RAG [[Retrieval Augmented Generation](https://thenewstack.io/freshen-up-llms-with-retrieval-augmented-generation/)], and there was a lot of deeply technical work required.”

Margolis noted that while some fringe players exist in terms of building agents, he has mostly seen just Agent Builder and GPTs out in the wild.

“With things like Agent Builder and GPTs, you don’t need to be an AI engineer to do that.”

The net effect of the ability to build agents with less technical knowledge has been to push the ideation, and some of the execution, of creating agents to line-of-business people instead of relying solely on developers.

“At a high level you’re taking information from some system — a proprietary system, the internet, some combination of them — and you’re using that to inform an AI tool, an agent, or some type of generative assistant,” Margolis said. “It’s the same pattern that we saw maybe a year or two years ago with LangChain, where you have these loops of logic and reasoning and you’re augmenting the output until you get to a point that it’s actually giving you what you want. It’s just become a lot less nuanced.”

“With things like Agent Builder and GPTs, you don’t need to be an AI engineer to do that. You can be a layperson to do that. You can kind of do it using just plain text or ClickOps or something like that. It’s a little bit more predictable, in terms of the solution space.”

## Combining AI Modalities
The idea of combining AI modalities might be of more practical interest to AI engineers. To note, when Margolis is talking about modalities in this sense, he’s talking about the difference between what we might think of as “traditional” machine learning, such as that used in inference and prediction, and the newer modalities of foundation models and generative AI. This is different from the idea of modalities within generative AI, where the input and output is dependent on the media — such as text, audio, video, or translation.

“Whereas you used to see folks that would play either in the generative AI world, or they would play in the more traditional ML world around inference and prediction and stuff like that, you’re starting to see a conflation of those two.”

“This is not a no-code solution, but it’s a relatively low-code solution. I’m not building a model from the ground up. I’m not writing in TensorFlow.”

Margolis notes that this is where we can see the use of generative AI without necessarily building a specific AI agent or chatbot. He uses the example of using AI tools to present data within a healthcare system, where you might have multiple data fields about a patient entered by the nurses or doctors, or administrators, that are written by the generative tool. Then within the same system, there are ML tools with inference engines that might say this is a high-risk patient and so forth.

“A couple years ago, if I wanted to build an application like the [healthcare example], I probably need to enlist some of my ML colleagues who are deeply versed in model creation, and they probably need to build me a propensity model using JAX or TensorFlow,” Margolis said. “They may need to be, literally, getting into the physical GPUs. There’s a lot of ML engineering and data science work that goes into that. Then on the generative side, maybe I can just take that output and I pump it into the context window of my favorite generative model. But those are two really different skill sets.”

Margolis said that tools like Google Cloud’s Vertex suite (SADA is a Google Cloud preferred partner for generative AI) can help bridge the gap between the machine learning tools and the generative AI tools

“Now the same engineer can go and create an AutoML model in Vertex,” Margolis said. “This is not a no-code solution but it’s a relatively low-code solution. I’m not building a model from the ground up. I’m not writing in TensorFlow. I’m not writing in JAX. I’m not dealing with GPUs. I’m not dealing with any virtual or system components.”

For more on combining generative AI with structured data, Margolis recently published an [interesting piece on Medium](https://medium.com/google-cloud/generative-agents-with-structured-data-c4947603f600) on the topic.

## Generative AI To Help Build Generative AI
“The barrier to entry has really dropped, and I think that’s good for everybody.”

We are not quite in a world where computers are autonomously building their own baby computers and writing their own code. However, an interesting development within AI engineering is the use of generative AI to help build more generative AI agents, bots, and applications.

“I think that’s a powerful pattern that’s enabling a lot of people to get involved in the space,” Margolis said.

He likened this trend to the inflection points in the last 10-15 years when developers could begin to easily spin up virtual machines in the cloud circa 2010, or when the barrier to entry to build mobile apps was lowered around 2014.

“I feel like this is the same ‘oh shit’ moment that we had in [the] public cloud when we realized that every student [who’s] just getting started in computer science or systems design back in, you know, 2010, all of a sudden could just go spin up servers and databases,” Margolis said. “If you wanted to be an AI developer 18 months ago, you had a big hill to climb. There was a ton of work required to get to the point where you could actually realize your idea. Now we’re to the point of having an idea and realizing it, you might be able to do that over lunch.”

“The barrier to entry has really dropped, and I think that’s good for everybody.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)