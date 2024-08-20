# Be an AI Power User: Success Strategies in the AI Landscape
![Featued image for: Be an AI Power User: Success Strategies in the AI Landscape](https://cdn.thenewstack.io/media/2024/08/c22ed3d7-chatbot-1024x576.jpg)
If you’ve been following along with my [previous article on the current state of large language models](https://thenewstack.io/the-current-state-of-llms-riding-the-sigmoid-curve/), you might wonder, “OK, so where do we go from here?” Well, buckle up because we’re about to dive into how you can become an AI power user in this evolving landscape.

As I explained previously, [LLMs](https://www.datastax.com/guides/what-is-a-large-language-model?utm_medium=byline&utm_source=thenewstack&utm_campaign=enterprise&utm_content=power-user) are starting to level out in capabilities and quality. They also represent a new competency in application development that is evolving and maturing in real time. Being curious and learning today will keep you from waking up in a few years and finding out you’re the COBOL programmer on the team.

## What Exactly Is an AI Power User?
First things first: Let’s define what we mean by an “AI power user.” It’s not about who can use the biggest model or throw the most compute at a problem. An AI power user can effectively leverage AI tools while understanding their limitations and optimal use cases. It’s about working smarter, not just harder. Yes, this means learning how to work with prompts, which causes eye rolls in some circles.

Before you get judgy, recall when you learned that `SELECT * FROM x WHERE y=0`
was a ridiculous incantation to type when getting data. Right. Let’s move on.

## The Golden Rule: Minimize LLM Usage
Now, here’s something that might surprise you: The key to being an AI power user is often about using LLMs less, not more. I know it sounds counterintuitive, but hear me out. When you start using something like ChatGPT, the typical pattern is to dump loads of data into the prompt and hope for the best. Unless you are condensing text, it’s just an expensive way to learn that LLMs have limits.

LLMs are powerful, but they’re also resource-intensive and can be [unpredictable](https://arxiv.org/abs/2304.00612). Those two features should signal to any engineer that we have a boundary problem — a minimum and a maximum. The most effective AI [applications often use LLMs judiciously](https://thenewstack.io/how-llms-are-transforming-enterprise-applications/) as part of a larger system rather than the entire solution. Think of LLMs as the spice in your AI recipe — a little goes a long way, but too much can overpower everything else.

The goal is to find the “Goldilocks Zone” of LLM usage for your use case: not too much, not too little — just the right amount. And here’s the kicker: You want to be ready to slide that window as capabilities and costs change over time.

AI is still a fast-moving technology. Using the Moore’s Law strategy, application developers have thought of horizon windows where more CPU power is available. Game developers learned to make this a feature with a literal slider to bump up as capabilities improved. When the next breakthrough and step-up in functionality occurs, will you have to rewrite? Or will you be able to just move the slider to the right to offer your users more?

## Understanding LLM Limitations: No More Magical Thinking
To become a true AI power user, you need to understand the limitations of LLMs. I’ve worked with users who thought they could replace entire job roles or complex analytic jobs with an LLM. That’s what I call “magical thinking,” and it’s the fastest way to end up with a failed AI project. It happens with every new technology and happens before we establish a common understanding of boundaries.

LLMs are not magic boxes that can solve any problem you throw at them. They have specific strengths and weaknesses; understanding them is crucial to using LLMs effectively. So let’s consider the boundaries and what, as an AI power user, you need to do to work with the technology we have today, in the Goldilocks Zone.

## Effective Strategies for LLM Usage
Given the current state and trajectory of LLMs, how can we use them effectively? Here are some strategies that power users employ:

**Human-in-the-loop approaches:**Don’t try to automate everything and go completely hands-off. Sometimes, the most effective use of an LLM is to augment[human decision-making rather than replaceit entirely](https://thenewstack.io/ai-is-best-supporting-human-decision-making-not-replacing-it/). The human-in-the-loop could even be your end user. There is a lot of power in contextual follow-up with some further clarification.**LLM tool calling:**Instead of relying on the LLM to generate information, use it to call the right tools or APIs. This can dramatically improve accuracy and reliability. For example, if a user asks, “What did I buy last week?” The LLM can issue a tool call to query a database and then convert the response to something more human than a result set. “You bought Lego set X! That looks like fun.”**Agent frameworks:**These can help manage complex workflows involving multiple LLM calls and other processes. An interesting feature with some of the early agents available now is acting as the feedback mechanism. Agents can do that in some cases when a human can see a response and ask again. If a database query tool call returns an empty result, the agent can rethink the follow-up. I’ve seen this in action and see this as something that will improve more over time.**Focus on data quality:**The old adage “garbage in, garbage out” is even more true with LLMs. High-quality, clean data is crucial for effective AI applications. Where that clean data can make the most difference is in[retrieval-augmented generation (RAG)](https://www.datastax.com/guides/what-is-retrieval-augmented-generation?utm_medium=byline&utm_source=thenewstack&utm_campaign=enterprise&utm_content=power-user). If you avoid using LLMs for knowledge and focus on communication, the data retrieved needs to be precise. In the retail example, good descriptions without a lot of codes or extra boilerplate will improve responses.
## The Rise of Small, Focused Models
Here’s another trend power users are latching onto: small, focused models. While the headlines might be all about the latest 175-billion-parameter behemoth, many practical applications are finding success with much smaller, more specialized models. Smaller models are having their moment and asking some interesting questions. Do LLMs need to have both reasons and knowledge or can we separate those two things?

Take Apple’s approach, for example. It’s shipping small, focused models that will run on a mobile device to perform specific tasks. Or look at Salesforce’s “Tiny Giant” project. These smaller models can often perform specific tasks just as well as (or better than) larger, general-purpose models, and they do it with far less computational overhead. They are focused on the reasoning aspects of LLM action. Instead of knowing all the words to a song from “Hamilton,” they can determine you are talking about music and activate the right service.

## Becoming the ‘AI Adult’ in the Room
As an AI power user, you’ll often find yourself in the role of the “AI adult” in the room. This means having the confidence to say no to bad ideas and guiding others away from magical thinking. It’s about having a conservative, actionable point of view on [building AI applications](https://thenewstack.io/surmounting-the-challenge-of-building-web3-applications/). It does not mean that you can or should act like the know-it-all.

Remember, most users are just trying to figure this out. You can help steer projects toward success and avoid costly pitfalls by providing clear, practical guidance. Listening and understanding should first lead to helping others be successful. When you hear about a project to eliminate all customer service representatives, you can help guide the project into something that will actually ship.

## Practical Steps for AI Implementation
So, how do you put all this into practice? Here are some concrete steps:

**Start small:**Look for simple enhancements to existing applications rather than trying to rebuild everything from scratch. Your mantra should be, “How can I make my users some percent more productive?”**Focus on your data:**Clean, high-quality data is the foundation of any successful AI project.**Explore augmentation techniques:**RAG, tool calling and agent frameworks are all built to put you in the driver’s seat and minimize reliance on LLMs.
## Your First AI Project: Build a Chatbot
Now, here’s the most important piece of advice I can give you: If you want to become an AI power user, start by building and deploying a chatbot into production. Chatbots might seem a bit “Hello World” at this point, but trust me on this. I added the deployment to the production part because that’s where the real learning happens. Building a chatbot will teach you crucial lessons about:

- Managing conversations and context
- Integrating external data sources
- Handling edge cases and unexpected inputs
- Balancing model capabilities with other components
Plus, it’s a project you can start right now with minimal resources. Outside of production, it’s the perfect [sandbox](https://www.langflow.org/) for experimenting with different techniques and understanding how LLMs work in practice. In production, it adds value following the sliding scale of LLM use.

## Wrapping Up
Becoming an AI power user isn’t about using the biggest models or the latest buzzword technologies. It’s about understanding the landscape, using tools judiciously and always keeping an eye on practical, valuable applications, just like every other engineering practice.

Remember the key points:

- Minimize LLM usage — find that Goldilocks Zone!
- Understand and respect the limitations of AI
- Focus on data quality and targeted use of AI capabilities
- Start small and practical — build that chatbot!
As we ride the sigmoid curve of AI development, the real winners won’t be those who can use the most AI, but those who can use AI most effectively. So go forth, confidently ship your chatbot and start your journey to becoming an AI power user. The future is waiting, and it needs more AI adults in the room.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)