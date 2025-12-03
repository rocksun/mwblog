If 89% of business leaders think their customers are satisfied with their conversational AI experiences, while only 59% of consumers are, we’re facing a wide gap between AI perception and reality.

Even with widespread leadership backing, 98% of organizations anticipate changing their conversational AI strategy within the next year, with 58% planning to fully replace their conversational AI solution, according to a new Twilio report, [“Inside the Conversational AI Revolution.”](https://www.twilio.com/en-us/report/Inside-the-Conversational-AI-Revolution)

You could say these results, from a global survey of 457 business leaders and 4,800 consumers across 15 countries, are just part of [growing pains](https://thenewstack.io/4-reasons-agentic-ai-is-failing/). After all, customer satisfaction with AI-backed chatbots increased 30% over the last quarter, according to the Twilio survey, signaling that, like most AI solutions, conversational AI is on an improvement curve.

Some of this customer dissatisfaction can be blamed on persistent data silos — as well as on the disconnect between subject matter experts, like customer support representatives, and the knowledge bases the responses are trained on. It also could be that the built or bought conversational AI tool is too broad, à la [ChatGPT-4.0](https://thenewstack.io/we-used-gpt4-during-a-hackathon-heres-what-we-learned/). It’s likely a mix of all these hurdles.

Whatever the reason, you’re likely rethinking your conversational AI plan for 2026. The New Stack talked to [Andy O’Dower](https://www.linkedin.com/in/odower/), vice president of product management at Twilio, a cloud communications company, about what these results mean for the near future of your conversational AI strategy.

## Prioritize Focused and Discrete Use Cases

At this stage, there is no one-size-fits-all chatbot.

“If I just give a generic chatbot a generic question, I’m going to get a generic response,” O’Dower said.

Of course, when chatbots were first launched, that’s all the data they had to work with, most likely whatever Open AI was trained on. Now organizations are adding more and more internal sets, entering what he calls the whack-a-mole stage: “We’re never going to use a generic [AI agent](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) that’s going to handle any inquiry that anyone could ever have about our business.”

This is all too broad, too fast, he said. It’s better, instead, to nail down the first “discrete, focused,” often most frequently asked questions, he said, to find measurable success and then to expand from there. This can be as simple as customers or patients having difficulty logging into your website or app.

If a customer contacts their bank’s customer support saying they have a weird charge on their bank or credit card, “the AI should, in theory, know the place where you want to go,” O’Dower said, based on “the regular charges. And then algorithms go into that — where you buy, what e-commerce sites you use or not, purchase prices and everything that goes into that.”

Instead of a customer support rep manually scanning PDFs, the AI should be able to — based on different data sources, including that customer’s purchasing history — pinpoint which purchase is the outlier. Then, an AI agent might be able to suggest next steps of how to contest the expense, or it knows when to escalate the matter to a human right away.

> “You want to be thinking about these AI agents, not just as a specific replacement of my inbound customer support 800 number. They’re starting to think about this AI agent over time becoming a representation of my entire business.”
>
> **— Andy O’Dower, Twilio**

This is in part because, over time, more data sources are being integrated into the chatbot’s conversational AI.

O’Dower calls it a customer support pyramid. If an organization has 1,000 support calls, about half will be regular use cases that an AI agent or even simpler automation can answer — like “Did this ship?”— replying with not just the expected arrival date but the shipping info and link to third-party tracking. It can also make excuses or refunds when shipments go wrong. Quick responses to these, without humans in the loop, maintain a higher level of overall customer satisfaction.

Then, farther up the pyramid, as customer requests become less frequent yet more complex, a human agent can become what O’Dower calls a “super agent,” backed by an internal conversational AI interface that allows for quicker discovery and resolution.

A good conversational overlay on top of correct data can significantly decrease the response time for service representatives.

Giving AI access to internal data and having a healthy data ecosystem are two of the capabilities that [Google’s](https://cloud.google.com/?utm_content=inline+mention) [2025 “DORA” report found](https://thenewstack.io/ai-has-won-googles-dora-study-shows-universal-dev-adoption/) can amplify the impact of AI adoption.

Again, this demands a modular approach, so “you’re not just opening the floodgates of too much data going into an AI agent,” he said. Instead, “identify who these customers and consumers are.”

Develop a habit of asking the AI agent what it’s told a consumer, making sure it’s not sharing any personally identifying information.

## Adopt a Flexible and Modular AI Strategy

But the near future of conversational AI is flexible.

“The technologies are getting better and better,” O’Dower said. “You as an engineer need to think about this from a modular standpoint” in the face of AI’s continued improvement. “If you’re adding more and more modular data sources that could enrich the 360-degree view of who a customer is, and then you can match that with a better and better language model, then you should get better and better results on the other side.”

With everything so new, as I argue in [The New Stack’s new AI enterprise strategy playbook](https://bit.ly/AI-Enterprise-Playbook), it’s essential to maintain flexibility, avoiding vendor lock-in at all cost.

“I could be pitched on a full, out-of-the-box, total solution that does it all for me,” said O’Dower. “That solution might be wed to one existing language model under the hood, or it might be able to only pull from data sources that it has prebuilt integrations with.”

This demand for flexibility is in part because you can’t really know which data sources and services will work with your customers until your conversational AI is in production — and you see how often “HUMAN PLEASE” is yelled at your bot.

“If I send this out to customers, and I still get X amount of people right away saying that this didn’t solve their problem, I need to escalate to human,” he continued. This is a red flag that your training data is off. With an all-in-one solution, you have to go back to the vendor, requesting more external and internal data sources to train on, which slows progress.

Remember: While AI is starting to trigger notable increases in productivity, it is all highly experimental. Different data sources may make an AI agent more successful or not, especially if it has access to different backend services, like a return-a-product service, a billing reminder service or an appointment scheduling service. But if you go for a so-called full-service solution right now, it’s unlikely to have everything you need built in — because you can’t yet predict your needs, or your customers’ behavior.

This is why more than half of organizations surveyed in this year’s Twilio report plan to change their conversational AI provider in the next year.

“Don’t go from one boxed-in solution to another boxed-in solution,” O’Dower said. “Those language models are going to continue to get better and better and better. You’re going to find more and better data sources that maybe you already have internally that you could plug into this.”

## Learn To Measure Conversational AI Success

Only [63% of “AI mature” organizations](https://www.gartner.com/en/newsroom/press-releases/2025-06-30-gartner-survey-finds-forty-five-percent-of-organizations-with-high-artificial-intelligence-maturity-keep-artificial-intelligence-projects-operational-for-at-least-three-years) — those with AI initiatives remaining in production for three or more years — measure the success of their AI strategy at all, according to a June report by Gartner. You must consider if your chatbot is all talk and no action.

Success for conversational AI, O’Dower said, is defined by when its users say it’s working — and when you can prove that it’s working for your business. We all remember early on when a prompt injection had someone trying to buy a Chevy for $1. A “one agent to rule them all” model risks something like this happening again. Instead, you need a fleet of conversational AI agents working together, each specialized in and trained on handling a discrete request.

“We need to talk to our AI agent policy expert that knows what we can and can’t do, that then puts in guardrails to any type of [large language model](https://thenewstack.io/introduction-to-llms/) [LLM] that says that’s completely out of policy,” O’Dower said. “That AI agent knows all the policies through and through better than a human agent would know out of the gate.”

Within these guardrails, he said, an AI agent might be able to create a reasonable benefit, like generating a coupon for a free oil change, not selling a car for a buck.

“What we saw in the early days start to happen was to deploy an OpenAI LLM, and just plop it on the website, and let it talk to anybody about any topic,” O’Dower said, “versus a much more discrete, focused, modular strategy where you know you’re gonna change and evolve this.”

A lot of success relies on proper leadership around AI strategy. This means, he said, “From the top down, not saying ‘AI everything.'”

Instead, O’Dower said, it means “saying, ‘If we are to be successful in automating and giving a much better customer experience, we are going to force teams to work together.'”

This can be a dedicated team that has brought together representatives from other teams, he said, including bringing folks “from legal, from data, privacy and security, from customer service, from marketing, from go-to-market teams, the engineering and product teams together, to be able to say, ‘we are going after this use case, and we are going to make an amazing experience with conversational AI, and you will be mapped to this initiative.’”

## Use Modular Data for a Holistic Customer View

We know that [data is what’s holding most organizations back](https://thenewstack.io/your-top-2026-priority-prepare-your-data-for-ai/) from systemic, cross-organizational AI success. In fact, the MIT Project NANDA’s [“State of AI in Business 2025”](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf) report, released in July, discovered that 95% of AI pilots fall flat due to persistent data silos.

Carving out modular data sources, O’Dower said, also support the cultivation of a 360-degree view of the customer.

“Not just one big block of data — that doesn’t make sense because you need to match up these data points,” across different departments, O’Dower said.

Instead, he added, a cross-organizational data strategy must consider, “How does that interact with what our policies are and what our marketing and promotions are? The better that data is structured, the far better results you’re going to get on the other side, when you match it up with an AI agent.”

This modularity — in contrast to a one-size-fits-all AI customer support solution — also allows your conversational AI stack to connect with different services, from payment solutions to appointment scheduling bots.

Soon, he predicted, the customer experience will become more flexible, including intuitive conversational AI that works via voice when you’re driving or via text when you’re on do not disturb or work mode. These advances will also see more customers supported in more spoken languages.

If 58% of organizations intend to replace their conversational AI solution completely in 2026, as Twilio reported, that’s a sign that you need flexibility in response to this still-emerging space. And it means you’re more likely than not to make a chatbot change next year, too.

It’s also time to start thinking strategically about your conversational AI. As O’Dower said, think “about these AI agents not as just a specific replacement of my inbound customer support 800 number. They’re starting to think about this AI agent over time becoming a representation of my entire business.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/220bf6cf-jriggins-2025-600x600.jpeg)

Jennifer Riggins is a tech storyteller and journalist, event and panel host. She bridges the gap between business, culture and technology, with her work grounded in the developer experience. She has been a working writer since 2003, and is based...

Read more from Jennifer Riggins](https://thenewstack.io/author/jennifer-riggins/)