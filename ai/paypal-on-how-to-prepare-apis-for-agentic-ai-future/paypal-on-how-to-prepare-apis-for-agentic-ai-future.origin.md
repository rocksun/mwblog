# PayPal on How To Prepare APIs for Agentic AI Future
![Featued image for: PayPal on How To Prepare APIs for Agentic AI Future](https://cdn.thenewstack.io/media/2025/06/a8890dbb-paypallogo-1024x576.jpg)
Photo by Mariia Shalabaieva on Unsplash.

PayPal predicts that within five years, 20% to 30% of its customers will start their shopping through AI agents and AI tools. It’s preparing for this eventuality by creating a [Model Context Protocol (MCP) server](https://thenewstack.io/mcp-is-rss-for-ai-more-use-cases-for-model-context-protocol/) that exposes [PayPal’s existing APIs](https://thenewstack.io/api-governance-using-patterns-from-paypal-netflix-and-more/) in a way that’s easy for AI to understand.

“We’re probably a little ways away from the day when agents are completely automated and buying things at scale and sending to you without any interaction, but we’re much closer than people think,” said [Brenden Lane](https://www.linkedin.com/in/brendenlane/), PayPal’s senior director of developer product. “PayPal is trying to be the infrastructure layer for agented commerce.”

PayPal used Postman’s new [Agentic AI Builder with MCP Integration](https://learning.postman.com/docs/postman-ai-agent-builder/ai-tool-builder/overview/), which allows developers to take [API collections](https://thenewstack.io/introduction-to-api-management/) and turn then into callable agent tools using MCP. The MCP server will be the way developers access the tools that PayPal will provide for agentic AI commerce, Lane explained. (For a look at why MCP is needed in addition to APIs, check out engineer [Frank Fiegel](https://github.com/punkpeye)’s explanation of [how MCP differs from APIs](https://glama.ai/blog/2025-06-06-mcp-vs-api).)

One of the pieces that PayPal is interested in owning for agentic AI transactions is identification.

“We think that providing things like identity information, just validating that I am who I say am, could be something that’s very, very valuable going forward,” Lane told The New Stack.

PayPal’s MCP server enables AI agents to initiate and manage payment processing via PayPal. It provides access to transaction history, account information and information about payment disputes or claims. It also interacts with PayPal’s invoicing or subscription management features.

[PayPal’s MCP server](https://www.postman.com/paypal/paypal-public-api-workspace/collection/6830d951bcd2d577d7632320) is available through Postman’s new [curated network of MCP servers](https://www.postman.com/explore/mcp-servers), which was announced last week at Post/Con 2025 in Las Angeles.
An MCP server is really just enriched data on top of APIs, Lane explained.

“One of the big benefits that Postman is providing is really helping people who might have APIs today bring them into this AI world,” he said. “One of the great things about AI is that agents, or the AI tools, can actually start to compose these different tools and services together through the MCP server and basically make it [super easy to build](https://thenewstack.io/tutorial-build-a-simple-mcp-server-with-claude-desktop/) a lot of experiences that we didn’t have before.”

## Managing the User Interface
Lane said PayPal was “pleasantly surprised” when it learned how much of the experience transfers from the traditional API world to the new AI agentic world. But a few things become important when developing for AI, he added.

“There are differences in experience that we recommend developers think through and handle. A classic example in our case is that when somebody wants to buy something, that’s real money moving — that’s something we want to be cautious about,” he said.

In today’s world, that means multi-factor authentication. That same level of verification is needed with AI, but it might look different because there are lots of other types of interactions now enabled, such as chat prompts, he said.

In fact, AI can support multiple modalities, which means your content can be delivered in a different format than you planned. For instance, content could be summarized and read to someone instead of being viewed visually.

However, that may create problems for businesses. Not all clients or agents will have a robust visual experience yet, but a product catalog may rely primarily on pictures, Lane said.

“As a business, you might want to think about are there different ways I can make pictures available to people? Or, if it’s not pictures, some other way to tell and show people what am I getting if I go buy this thing,” he said. “One advantage of MCP servers and AI is that it does suddenly make your information and experiences potentially available across a lot of different types of user interface.”

It may be that frontend developers have to block off certain types of interface options if it can’t be supported well, he added.

## Leveling Up APIs for AI
Lane’s colleague, PayPal Lead Producer Manager [Rebecca Hauck](https://www.linkedin.com/in/rebecca-hauck/), presented what PayPal had learned about [API design](https://roadmap.sh/api-design) for AI during a Post/Con session. Essentially, it means API development must “level up” to be a good AI citizen, she said.

“We usually strive for clean docs, logical endpoints and maybe some sample code, but AI doesn’t read docs the way we do, so we need to recognize AI’s role, perspective and ability,” he said. “AI needs structure and context in the API itself to understand how to use it properly. So this is where we need to evolve to step up to the next level.”

She added that developers have to recognize that AI is not just a tool, but a new form of API consumer.

“That means rethinking the [way we design APIs](https://thenewstack.io/how-radical-api-design-changed-the-way-we-access-databases/) so they can be interpreted and used reliably by machines as well as people,” Hauck said. “Simply put, it means creating APIs that are clear, easy to use and work well for humans and AI systems, so they can easily understand each other and work smoothly.”

That translates into a few specific requirements. First, it’s important that APIs and the supporting documents are unambiguous, because — unlike humans — the AI will not ‘tinker’ to figure out what a document meant if it’s unclear.

The API and the documentation have to be predictable and transparent, she said.

“APIs should do what they say,” she said. “[AI agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) rely on consistency. If behavior changes unexpectedly, they’re lost. Strong schema design remains paramount to achieving this.”

It’s very important, then, to adhere to formats such as [OpenAPI](https://thenewstack.io/openapi-initiative-new-standards-and-a-peek-at-the-roadmap/) and [JSON](https://thenewstack.io/how-we-built-the-new-json-api-for-cassandra-and-astra-db/), she added.

“The API schema is more like a contract,” she said. “It’s like a cheat sheet for AI. It tells them what to expect, how to behave and what the boundaries are.”

In addition to explaining what the API can do — which is typically covered in documentation — developers should go a step further and explain why the API does what it does and when it should be used. Tell the AI what the endpoint is for, what the goal is, and when it should be used, she advised.

“We might think that an endpoint is super intuitive, but if AI can’t figure it out, or what it does or how to call it, it’s dead,” Hauck said. “The goal isn’t to choose one audience over the other. It’s to design in a way that supports the entire population of API consumers and citizens.”

[Metadata](https://thenewstack.io/use-ai-to-improve-your-organizations-metadata/) also becomes more important.
“Metadata in a structured format provides extra context that lets agents do more than just poke around blindly,” Hauck said. “It’s like labeling everything in your toolbox so even a robot could figure out what to use and when.”

MCP addresses many of these issues, she added. It provides an additional [semantic layer](https://thenewstack.io/demystifying-the-metrics-store-and-semantic-layer/) that acts as an addendum to your API contract, specifically for [large language models](https://thenewstack.io/7-guiding-principles-for-working-with-llms/) (LLM). It adds other capabilities that are not accessible through your APIs, she said.

Finally, don’t forget about practical [issues such as security](https://thenewstack.io/shadow-zombie-and-misconfigured-apis-are-a-security-issue/), she said.

Postman provides a sort of sandbox for organizations to test that APIs are designed for both developers and humans, she said.

“Postman is no longer just for human devs, testing endpoints,” she told the Post/Con audience. “We can also use it to design and simulate how LLM-based agents might interact with our APIs.”

Developers should test how well the APIs work for both developers and agents by creating sample calls and simulations that show how both a developer and an agent would “walk” through a workflow, she suggested.

While APIs have traditionally been focused on [developer experience](https://thenewstack.io/api-governance-and-developer-experience-in-a-developer-portal/), they now have to focus on agent experience, she stressed.

“That’s all about designing APIs that machine agents like LLMs and autonomous tools can understand without getting confused or stuck,” she said. “This means things like rich metadata, consistent patterns, clear naming, [and] structured responses that both people and agents can work with.”

*Postman paid travel and accommodations for Loraine Lawson to cover Post/Con.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)