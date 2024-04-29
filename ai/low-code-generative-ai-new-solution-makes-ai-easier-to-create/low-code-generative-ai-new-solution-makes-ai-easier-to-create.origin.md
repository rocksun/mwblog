# Low-Code Generative AI: New Solution Makes AI Easier to Create
![Featued image for: Low-Code Generative AI: New Solution Makes AI Easier to Create](https://cdn.thenewstack.io/media/2024/04/b7eccb84-mariia-shalabaieva-jryya3w2uxk-unsplash-1024x576.jpg)
Not all generative AI is a chatbot nor does it need to be.
[Generative AI](https://thenewstack.io/how-generative-ai-coding-assistants-increase-developer-velocity/) is about so much more, said [Rodrigo Coutinho](https://www.linkedin.com/in/sousacoutinho/), AI product manager at the [low-code development platform OutSystems](https://www.outsystems.com/).
The company recently launched a new offering called
[AI Agent Builder](https://www.outsystems.com/ai/) that simplifies the development of AI agents for organizational use. The agents are a collection of model connections, configurations and promptings, he explained.
“The idea behind an AI agent is to give the ability of people that are using low code to access GenAI technologies, and so you can think of it kind of as a configuration, where you establish what model you want to use,” Coutinho told The New Stack. “The cool thing is not only does this allow for you to use the agent in the
[low-code environment](https://thenewstack.io/what-a-low-code-platform-offers-frontend-developers/), so instead of having to think of all these things, you simply have the visual element that does all this functionality, but it also allows us to give a playground for people to try out the agent.”
The agents still require some
[prompt engineering](https://thenewstack.io/developer-tips-in-ai-prompt-engineering/), but the out-of-the-box interface allows developers and others to try out the agent, tweak it and make it their own, he said.
## Three Agents Available Out-of-the-Box
OutSystems offers three AI agents: One that can handle call summarization, one that handles ticket deflection, and a private chat agent.
Call summarization simply summarizes long calls, so that (for example) salespeople can upload a full summarization into their sales application or other notes. Ticket deflection means that if someone asks a question that might normally require a support ticket, the agent can provide an answer based on the documentation provided to it. It can also be connected to something like Zendesk to move ahead with submitting the ticket. The user interface element is also provided out of the box with the AI agent, he added.
The private chat allows organizations to embrace
[ChatGPT](https://thenewstack.io/improving-chatgpts-ability-to-understand-ambiguous-prompts/)-like functionalities without worrying about potential data usage issues and other compliance-related issues that generative AI chatbots raise. All the AI agents are designed to guarantee privacy and limit other organizational risks associated with public GPTs.
“The whole architecture was made thinking about [it] being used in our systems, in the sense that we provide a local element that exposes the agent and that’s very easy to call,” he said. “If you want to use the agent from a third-party application or do an integration, it’s rather simple in the sense that you can create an OutSystem application, where you just expose it as a REST API.”
## Simplifying AI Development
While developers tend to associate
[low-code with citizen developers](https://thenewstack.io/pro-coders-key-to-stopping-citizen-developer-security-breach/), the AI agents also simplify development efforts for programmers, Coutinho said.
“It’s very easy for anyone to, with a few configurations, create an agent that’s really useful and there’s something that impacts the business,” he said. “Also, because after the configuration, you have the playground, so you can tweak and iterate over the agent that you did until you’re happy with the results.”
The agents can be used and reused in any application, he added.
“You can have multiple interfaces using the same agent,” he said. “We could have an interface closer to a chatbot or something closer to a forum and all of this is one visual element. It’s very easy then to reuse that throughout the organization.”
Currently, developers can choose from
[Azure OpenAI](https://thenewstack.io/generative-ai-cloud-services-aws-azure-or-google-cloud/) or [AWS](https://aws.amazon.com/?utm_content=inline+mention) [Bedrock](https://thenewstack.io/aws-goes-deep-on-ai-chip-power-and-cost-savings/) foundation models, then integrate them with organizational knowledge sources, and input natural language instructions for use inside applications. OutSystems also built-in guardrails to control access and performance monitoring, including security support.
“We want to make sure that the user model ensures privacy and security on data access and so by giving developers an agent, as opposed of giving direct access to these models, you ensure they use the right one,” he said.
The same applies to
[data](https://thenewstack.io/integrating-real-time-and-historical-data-enhances-decision-making/), he added. When developers configure the agent, the platform ensures that the [data doesn’t contain sensitive](https://thenewstack.io/qa-how-verticalchange-secures-sensitive-data-using-open-source-tools/) data that an organization would not want exposed, he said. It also monitors things like token usage so users are aware of the costs of each model and how much information each model provides, he added.
“An agent also has data associated so it’s very easy to control what type of data and what do you want to provide the agent to use to give the responses to the customers,” he said. “Even if it’s not going to the model, you also want to be careful with the data that goes to the customers. You don’t want private
[data to leak](https://thenewstack.io/why-unsuspecting-data-leaks-are-a-key-to-rampant-blockchain-hacks/) out.”
It also can simplify
[combatting hallucinations](https://thenewstack.io/3-ways-to-stop-llm-hallucinations/) by simplifying connecting to another model and having it check a model’s answers for possible hallucinations.
“The cool
[thing about having these agents available in low code](https://thenewstack.io/adopting-low-code-for-developers-5-things-to-consider/) is that it’s very easy to orchestrate these things,” Coutinho said.
For example, OutSystems set up its own translation of its forums from English to Japanese. The first thing that was required was ensuring that the English was correct, he said, because the company has a lot of non-native speakers who “are very creative in their use of English, myself included,” Coutinho said.
“So the first thing you need to do is ask AI to take this English sentence and make it good and then translate it to Japanese,” he explained. “Using low code, this is very easy to use because you just have a couple of visual elements, you connect everything and you have a visual way to understand what is going on. The same applies to checking out hallucinations. You can call the model and then have another agent that validates if it is within the standards that you would expect.”
## Creative AI Use Cases
OutSystems does plan to add additional LLM models in the future, including models to handle images and video.
“We want to expand also with more examples, both on the agent side to help people create better products and on the sample website to give inspiration,” he said. “We are aware there are a lot of businesses that know that GenAI can help them be more productive and more effective, but they need a bit of inspiration to understand exactly what’s possible. We’ll keep growing AI Agent builder to provide those examples.”
Beyond the predictable use cases, customers have used the agents to help employees be more productive with falling-out timesheets, Coutinho said. Employees describe what they have been doing during the week and the AI allows them to quickly fill in their time sheets.
Customers are also using the private chat function to extract information from text-based inputs, such as a name or email information. Then that information can be used to create in structured datasets, he said.
One company is using the agents to extract information from all the job applications, CVs and resumes they receive from a job posting, he added.
“I’m very curious to see what people will do with it,” he said. “Our customers have a lot of imagination. I’m really looking forward to see the kind of original ideas come out of this”
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)