# Generative UI for Devs: More Than AI-Assisted Design
![Featued image for: Generative UI for Devs: More Than AI-Assisted Design](https://cdn.thenewstack.io/media/2025/04/43cc88d4-founders_thesys-c1-2-1024x576.jpg)
[Generative AI](https://thenewstack.io/how-generative-ai-is-reshaping-the-sdlc/) is being used to create designs, but a new AI-driven approach called [generative user interface](https://docs.thesys.dev/guides/genui) (GenUI) goes beyond static design, allowing [web developers](https://roadmap.sh/roadmaps?g=Web+Development) to leverage AI and data for more personalized applications and analytics displays.
The New Stack spoke with [Rabi Shanker Guha](https://www.linkedin.com/in/rabisg/), co-founder and CEO of [Thesys](https://www.thesys.dev/), about what generative UI means for development. The company specializes in AI-driven interfaces and created [Canvas](https://www.thesys.dev/products/canvas), a design tool for conversational AI products. Several tools and platforms offer AI-assisted features for UI generation or code generation for UI components, such as [GitHub Copilot](https://thenewstack.io/github-copilot-and-open-source-a-love-story-that-wont-end-well/), [Amazon](https://aws.amazon.com/?utm_content=inline+mention) [CodeWhisperer](https://thenewstack.io/decoding-amazons-generative-ai-strategy/) and [Vercel’s v0](https://v0.dev/).

On Monday, Thesys launched a new offering called [C1](https://docs.thesys.dev/guides/solutions/chat) that it says is the first API built to deliver GenUI capabilities.

Generative UI gives developers a way to create dynamically generated graphic user interfaces that adapt to user inputs, context and preferences for a more personalized experience, said Guha.

“This is very different from [AI-assisted design ](https://thenewstack.io/figma-redesign-shows-how-ai-can-transform-apps-adds-dev-support/)… which basically takes a prompt and converts it to a design. But this is like having a developer assistant do the work for you,” Guha said. “It can interpret intent. It can interpret data. It can interpret … for example, your geolocation [and] time of the day, and then present an ideal user interface to you in real time.”

Generative AI excels at intent. You can ask AI to help you buy a watch and explicitly feed it information about yourself — your country, your age, your gender, what you’d like in a watch — and it will generate recommendations.

C1, he said, takes this concept of intent and creates an interface from it. It combines the usability design of modern apps with the intelligence quotient of AI — all leveraged via an API.

“The C1 API bridges that gap,” Guha said. “And now all the AI agents of the world or the AI power interfaces of the world can have the same goodness of a rich visual UI.”

## A New Design/Frontend Dev Workflow
Currently, designers tend to work in Figma or a similar design tools, then hand off the design to a developer, who codes it. That can lead to translation headaches.

Guha doesn’t see C1 as a tool for designers, but said it could lead to a world where designers and developers co-exist within the same solution.

“C1 by Thesys is an attempt by us to bridge that gap and bring all that intelligence of AI and [[large language models](https://thenewstack.io/llms-can-now-trace-their-outputs-to-specific-training-data/)] with the goodness of traditional UX,” Guha said. “We can condense this entire thing into more of an LLM-driven development model.”

C1’s software development kit (SDK) can be integrated into a web page or applications with [three lines of React code](https://docs.thesys.dev/guides/setup), allowing developers to then start playing around with the outputs via prompting.

One example the company used to demonstrate its capabilities is a display of the “Harry Potter” movies’ cast. A developer might have created that as a list, but a designer might recommend a carousel. Rather than having to code that, a developer can go back to C1 and tell it to display the cast in a carousel.

“Next time your user asks that,” he said, “now it’s a carousel.”

![A carousel of the Harry Potter cast made by Thesys C1.](https://cdn.thenewstack.io/media/2025/04/c95e6517-harrypotter_c1_use.jpg)
A carousel of the “Harry Potter” movies’ cast made by Thesys C1.

## C1’s Generative UI Solution
C1 works as a drop-in replacement for an LLM API. For instance, if a frontend developer is leveraging [OpenAI’s API](https://thenewstack.io/introduction-to-the-openai-agents-sdk-and-responses-api/), the developers can switch out the OpenAI API, changing the URL from the OpenAI library to the Thesys URL to start designing in real time with prompts.

C1 has two parts, Guha said. There’s the API itself, which is designed to be OpenAI compatible. That means developers can continue to use their favorite tools, such as [Model Context Protocol (MCP) servers](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) and existing memory integrations, instead of learning new tools or solutions.

There is also a Thesys frontend SDK that can integrate with a developer’s existing [React](https://thenewstack.io/how-to-build-a-carbon-aware-website-using-react-and-next-js/) code base, he added. Thesys’ solution is compatible with anything above React 18.

Thesys, he clarified, does not stream React. It streams a representation of the UI, and using the SDK, converts to React on the consumer side.

C1 uses [Crayon](https://github.com/thesysdev/crayon), an MIT-licensed, UI toolkit for building AI agents. It was created by Thesys and the core is a React-based library that abstracts away the state management and backend integration. It is lightweight and can be integrated with any HTTP server including [LangChain](https://thenewstack.io/benchmark-llm-application-performance-with-langchain/), [CrewAI](https://thenewstack.io/how-crewai-enables-ai-agents-as-collaborative-team-members/) or a simple FastAPI server serving a LLM-driven agent, according to the documentation. It’s designed to integrate seamlessly with C1 but it has no dependencies on Thesys.

The C1 documentation shows that the GenUI tool is leveraging the [Anthropic](https://thenewstack.io/deno-2-0-angular-updates-anthropic-for-devs-and-more/) LLM [Claude Sonnet 3.5](https://www.anthropic.com/news/claude-3-5-sonnet). The company plans to expand the LLM offerings so that developers can choose which model they deploy with C1.

There is a [playground for developers](https://chat.thesys.dev/) to explore C1.

## Popular Use Cases: Analytics and Forms
C1 isn’t designed to create simple landing pages.

“If you’re building, for example, a landing page for your portfolio, C1 by Thesys isn’t really going to help you much,” Guha said. “But if you’re thinking of reimagining your CRM software with AI, this is where C1 by Thesys really shines.”

Its real power is in using data, he said: “People can use us for almost anything they are building an AI interface for, but if you talk about our experiences, so far, we have seen the biggest win with analytics-specific use cases. Analytics are one of those places where AI has an obvious edge over you having to learn [Power BI](https://thenewstack.io/power-bi-gets-low-code-datamart-feature/), for example, or you having to learn how to build a Salesforce dashboard.”

One Thesys customers is using C1 for [sales data](https://thenewstack.io/salesforce-officially-launches-einstein-ai-based-data-cloud/) specifically. The customer had already created a solution that brought in data from a Software as a Service solution and other sources, then it built a layer with OpenAI on top of it that could understand queries and return an output. Users could ask how many customers are in the pipeline this month, and it would fetch all that data, crunch it and produce the results in text.

“They were already building this, but they had a hard time figuring out how to visualize this data, how to present it in a natural, intuitive way,” he said. “You have this response in text, but text is probably not the best way of representing this data. Sometimes a chart might be a more natural way of representing this data.”

The company replaced its OpenAI endpoint with the Thesys API. Now the customer can ask a variety of questions, such as “How many people are using our product right now?” or “How many customers did we lose?”

“It generates a live React component on the frontend, with buttons and forms and all the elements,” Guha said.

Another company came to Thesys with an edtech product with a text-based quiz: Basically, it asked a question and users had to type in the response to a text field. C1 was able to turn the quiz into a form with multiple-choice questions and buttons.

“Let’s say you are building an AI version of a very simple quiz. So you have used Open AI, and you said to Open AI, ‘Give me 10 questions, and for each of these 10 questions, give me four options, and then role-play a quiz,’” Guha said. “We are basically built on top of existing LLMs, so we understand all that context.”

It also understands data, he added. So it will generate a UI representation of the output, giving the developer those 10 questions but rendering it as a form with multiple choice, button options.

“Those are the biggest use cases we are seeing,” Guha said. “But the sky is the limit on what you can do with it.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)