# It’s Time To Start Preparing APIs for the AI Agent Era
![Featued image for: It’s Time To Start Preparing APIs for the AI Agent Era](https://cdn.thenewstack.io/media/2025/01/786d3304-fahim-muntashir-14joixmsoqa-unsplash-1024x683.jpg)
[Fahim Muntashir](https://unsplash.com/@f12r?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/a-man-using-a-laptop-computer-on-a-wooden-table-14JOIxmsOqA?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
The software engineering world has always designed APIs with human developers in mind, who have predictable and consistent usage patterns. But a distinct new kind of API consumer is rapidly emerging: the AI agent.

Unlike human developers, AI agents behave like a thread. They are task-based bots spun up to achieve a specific goal. Completing their task might require them to form API connections on-demand, query an API, and close the connection. With agentic AI, integrations are no longer static and immutable concepts. Distinct, short-lived [integrations will become](https://thenewstack.io/ai-has-become-integral-to-the-software-delivery-lifecycle/) the norm. And with AI agents becoming the norm within dozens of coding assistant tools and platforms, the question is no longer ‘if’ but ‘when’ API design approaches will change along with them.

**How AI Agents Will Change API and Application Development **
### Limitless API Calls
Let’s use a flight booking application as an opportunity to examine how AI agents are already changing application development:

flowchart TD
subgraph Traditional[“Traditional Integration”]
A1[User Enters Search Criteria] –> B1[App Validates Input Format]
B1 –> C1[App Maps Fields to API Schema]
C1 –> D1[Make Airline API Call]
D1 –> E1[Parse Response]
E1 –> F1{Flight Available?}
F1 –>|Yes| G1[Display Results]
F1 –>|No| H1[Show Error]
G1 –> I1[User Selects Flight]
I1 –> J1[New API Call for Booking]
J1 –> K1[Handle Response]
end

subgraph AI[“AI-Agent Integration”]
A2[User Types Natural Request] –> B2[AI Parses Intent]
B2 –> C2{Request Type?}
C2 –>|Search| D2[Extract Search Parameters]
C2 –>|Modify| E2[Understand Modification]
C2 –>|Question| F2[Handle Query]
D2 & E2 –> G2[AI Makes API Call]
G2 –> H2[Process Response]
H2 –> I2[Generate Natural Reply]
I2 –> J2[User Responds]
J2 –> B2
F2 –> I2
end

Here, the difference in API usage boils down to deterministic vs. non-deterministic. The traditional app gathers input from the user and makes a single API call to surface the results. Usually, a single action by the user corresponds to a single API call.

Compare that to an AI agent application, which theoretically has no limit on the number of calls it can make from a single user request. It will continue to iterate and make several or even dozens of calls until it has satisfied the user’s request. If the result is unsatisfactory, the user can also re-prompt the agent.

**Granular Security for AI Agents**
On the security side, connection patterns and authentication flows will transform. In the short term, AI-based apps should increase the number of instances where an application requests access to a 3p API on behalf of a user. In the long term, the dynamic nature of AI agents might produce more sophisticated approaches to security.

For example, imagine an AI agent that needs to access your calendar to book a flight. Rather than requesting blanket calendar edit access, it might receive a temporary “micro-scope,” allowing it to check availability for dates relevant to travel planning. These micro-scopes would expire once the task is complete, minimizing the security surface area. As a model for LLMs, OAuth will likely die in a year.

**Managing Context Across APIs**
Traditional APIs treat each request as isolated, but AI agents consider the bigger picture when maintaining conversation context across many calls.

As AI agents increasingly need to coordinate between multiple services to complete tasks, the real [challenge is managing context across different APIs](https://thenewstack.io/rest-vs-graphql-solving-api-challenges-in-modern-data-transfers/). Where will that context live? And who needs to know about it? Currently, that context lives with the LLM, which picks and chooses the pieces it needs to share when sending an API request. But it isn’t hard to imagine a future with standardized “context blocks,” such that context can be shared and accessed across several API providers.

**How You Can Prepare for AI Agents Today**
AI agents are in their early days, and things will change significantly in the next 6 months. Let’s look at what you can do today to prepare your API for AI agents.

**Maintain Your OpenAPI Spec**
AI agents don’t care about how pretty your API documentation is. They only care that your OpenAPI spec is correct, descriptive, and up to date. They care about what data your API takes and what data it outputs. That’s it.

If you’re unfamiliar with OpenAPI,[ it’s a standard to describe REST APIs](https://886132a5.streaklinks.com/CPdoc00YmJqhv9T9EwVgiZiS/https%3A%2F%2Fwww.speakeasy.com%2Fopenapi%23openapi-overview). If you have a REST API, there’s a good chance that you have an OpenAPI spec lying around. Whether that spec is correct and up to date is another question entirely.

If you’ve been putting off updating your specs, AI agents are a significant reason to perform a proper cleanup. Most of the major AI agent frameworks (Langchain, LangGraph, Crew AI, etc.) use OpenAPI as the medium for enabling LLMs to interface with your API. If your spec is inaccurate or vague, you’re undermining other developers trying to build on top of your API with AI.

**Pay Attention to MCP**
In November, Anthropic announced the[ Model Context Protocol](https://886132a5.streaklinks.com/CPdoc00Vlcoc7HUQrwvDlSTY/https%3A%2F%2Fmodelcontextprotocol.io%2F) (MCP), an attempt to improve on the current system of using OpenAPI. While today’s APIs require unique implementations for each AI assistant or agent that wants to access them, MCP proposes a single server-client architecture that provides a simple JSON schema for [APIs accessible to your LLMs](https://thenewstack.io/accessing-perplexity-online-llms-programmatically-via-api/).

For API builders, this signals a potential shift away from building AI-specific endpoints or features and toward exposing their data through standardized MCP servers that any AI system could consume.

This could dramatically simplify how APIs handle AI integrations and make their data more accessible to the growing AI tools and agents ecosystem.

Whether the MCP will be broadly adopted or become specific to Anthropic is unclear. However, as one of the largest LLM providers in the market, you should consider building an MCP server regardless of broader adoption. To make your API available, you must create a pared-back SDK that adheres to the principles outlined in the standard.

The AI agent era of API design and consumption will introduce new challenges for developers and new opportunities. For example, API discovery among human developers remains an unsolved challenge today, and AI agents could either [solve or exacerbate this problem](https://thenewstack.io/the-future-of-sql-conversational-hands-on-problem-solving/).

But regardless of how the software integration industry ultimately adapts to the agents, developers must start laying the groundwork to prepare for them today.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)