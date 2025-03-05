# Why AI Agents Suck So Bad
![Featued image for: Why AI Agents Suck So Bad](https://cdn.thenewstack.io/media/2025/03/c8db6817-rodion-kutsaiev-l2jpoyf82ne-unsplash-1024x585.jpg)
Let me set the stage.

The other day I realized my DJI LIDAR was on the fritz. I depend on that small bit of tech to add autofocus and auto-follow to my cinema camera. Without that feature, I’d have a harder time getting some of the shots I need.

The thing is maybe a year or so old, but I had no idea if it was still under warranty. Either way, it had to be repaired.

![DJI Lidar (B&H)](https://cdn.thenewstack.io/media/2025/03/e42527db-dji_cp_rn_00000359_01_focus_pro_lidar_1712652359_1816801-300x300.jpg)
This is a DJI Lidar (B&H)

So, I hopped onto the DJI site and headed to support, where I assumed I’d be greeted by an AI agent.

Yup.

I hopped onto the agent and typed something akin to “My LIDAR will no longer autofocus.” The AI agent’s response was no help, so I followed up with a question. Again, the [AI agent](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) failed me, so I took another approach and asked a question, “How do I return my LIDAR for repair?”

The agent couldn’t help me.

After 30 minutes of trying, I decided a real human was necessary. Roughly 60 minutes after that, I had a return label for my LIDAR and could pack it up.

Given how so many enterprise businesses are relying on AI agents for just about everything, this should not have been the case. That conversation with the AI agent should have been simple, maybe something like this:

*Me: My LIDAR no longer autofocuses.*
*AI Agent: Can you give me the serial number so I can better assist you?*
*Me: Certainly. <types serial number>*
*AI Agent: Thank you. One moment, please. <moment passes> Your device is still under warranty. Type your email address and I will send a return label and we’ll place a priority on the process.*
*Me: Thank you.*
*AI Agent: Is there anything else I can help you with?*
*Me: No. Thank you.*
*AI Agent: Have a good day and remember to check your email for the label.*
That’s how the exchange *should* have gone; but alas, it did not and I spent far too much time arranging for the return and repair of the item.

As it stands, the only side of the coin enjoying the efficiency is the business. Every instance I’ve had trying to resolve an issue with an AI agent has been very similar to what I experienced when trying to get my LIDAR returned, so it’s not DJI’s fault.

The problem is with AI itself.

## AI Is Supposed To Make Everything More Efficient.
I’ve actually built a [chatbot](https://thenewstack.io/what-we-learned-from-building-a-chatbot/) before and understand how they work. AI agents are very similar in both how they are constructed and how they are supposed to interact with users.

The thing is, most AI agents are based on [Retrieval Augmented Generation](https://thenewstack.io/how-to-add-rag-to-ai-agents-for-contextual-understanding/) (RAG) models, which happen to be inexpensive and ineffective. Such RAG-based systems are employed around the world and this is a problem. Why? Because companies are using those systems to help with the very complex task of handling customer support.

Think about that for a second.

Many large companies might not feel this way but customer support is an insanely complicated process. Every user has different problems, a different level of understanding of what they are using or trying to do, speaks different languages, and is at very different levels of frustration.

When RAG-based systems are employed for this purpose, they can’t handle the nuances of communication and are often incapable of handling the problem.

Why is this? RAG-based AI isn’t the same as an AI system like [Mistral](https://mistral.ai/about), [Ollama](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/), or [ChatGPT](https://thenewstack.io/how-to-build-web-components-using-chatgpt/) in that it doesn’t have language processing, reasoning, or the ability to make decisions. You’ll know when you’re using a RAG-based system because the interaction is far from human. The only way RAG-based AI agents work is if you know the right questions to ask. Ask something off-topic or complex and you’ll immediately understand what I mean, as the agent will either not know how to reply, will repeat itself, or reset (which I’ve experienced on several occasions).

RAG-based systems are used in healthcare, legal advisory services, real estate agents, e-commerce assistants, enterprise retrieval-based chatbots, meeting notes and summary generators, appointment booking and scheduling, data analysis agents, and more.

## How Can the Problem Be Resolved?
You might have used[ Google’s Gemini Live](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/) and experienced a full-blown conversation with AI. I’ve used it and it’s impressive. I also regularly use Ollama via Msty for research and am rarely let down. Now, imagine if a company used something like Gemini Live as a support agent. Things would get done with a level of accuracy and expediency like never before.

The problem is that most companies aren’t going to want to spend the money on a transformative AI agent. What is a transformative AI agent? I’m glad you asked.

A transformative AI agent has the following qualities:

- Autonomy
- Learning and adaptability
- Decision-making
- Task execution
- Collaboration
These types of agents are what is considered the “third wave” of AI development (after predictive and generative AI) and could easily revolutionize many industries.

However, companies need to be willing to spend the money to make them work and that’s not going to be cheap or easy. Consider this: a company could create a transformative AI agent and make it available to businesses everywhere. Once a business decides to adopt that agent, they have to train it specifically for their needs (for products, services, etc.).

That training will require the business to have plenty of documentation for both their products and processes. On top of that, to really make these agents effective, they have to be integrated with other systems within the business (for things like ticket submission); otherwise, they won’t be very effective.

Just for fun, I asked Gemini this question:

Why are AI agents so bad at handling support?

The response from Gemini was telling:

While AI agents have made significant progress, they still struggle with nuance, adaptability, data biases, and customer trust. Overcoming these limitations requires ongoing research, better data, improved algorithms, and a more human-centered approach to AI implementation in customer support. The key is to see AI as a tool to augment human agents, not replace them entirely. The best customer support experiences will likely be those that seamlessly blend the strengths of both AI and human intelligence.

Gemini hit the nail on the head with its response, especially the part where AI is a tool to augment human agents, not replace them entirely. Until companies understand that RAG-based agents are not capable of replacing humans for support, customers and clients are going to continue having frustrating experiences and might even turn on a favorite brand because support is so bad.

This problem is real and I don’t see it going away any time soon.

Why? Simple. I asked the [Perplexity](https://thenewstack.io/more-than-an-openai-wrapper-perplexity-pivots-to-open-source/) AI-driven search engine the following question:

How much would it cost for a company to deploy a transformative AI agent?

The answer should tell you why:

*The cost of deploying a transformative AI agent for a company can vary significantly based on the complexity and scope of the project. As of 2025, here’s an overview of the potential costs:*
*For small-scale or basic AI agent development, companies can expect to spend between $50,000 to $80,0001.**Medium-scale AI agent development typically ranges from $80,000 to $150,0001.**Large-scale or advanced AI agent development can cost $150,000 or more.**For highly specialized, intelligent agents with advanced features like deep learning, real-time decision-making, and continuous learning, costs can exceed $300,000.*
So, anywhere from $50,000 to $300,000 dollars to deploy a transformative AI agent. That’s a big chunk of change, especially compared to a RAG-based system, which (according to Perplexity) can start at $7,000 and increase as complexity is added.

In the end, RAG-based AI agents are far cheaper than transformative AI, so you can bet that’s where most businesses are going to land. Until they finally open their pockets a bit deeper for the transformative option, most customers and clients are going to come away less than pleased.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)