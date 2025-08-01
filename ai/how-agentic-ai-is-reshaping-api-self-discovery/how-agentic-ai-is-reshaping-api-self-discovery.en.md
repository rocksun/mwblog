Generative AI (GenAI) is already transforming how we interface with APIs, and the spotlight is shifting to the next leap in AI evolution: agentic AI.

[Agentic AI](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) refers to intelligent systems that can reason, plan and act autonomously. These agents can interpret user goals, discover tools ([APIs](https://thenewstack.io/introduction-to-api-management/)), reason about when and how to use them and then execute workflows. This can change how APIs are consumed, documented and exposed.

Agentic AI can fundamentally change API consumption by enabling natural language-driven, autonomous API discovery and execution.

## API Consumption Challenges Agentic AI Addresses

APIs must be discoverable, descriptive and context-aware for AI agents to work correctly. Here are some of the issues that may occur otherwise and potential solutions.

### 1. Ambiguity in Intent Mapping

Most users don’t speak in structured API schemas. They express what they want in natural language:

*“Place an order for two iPhone 16s for customer John.”*

Traditional API integrations require explicit knowledge of which endpoint to call, which parameters are needed and what format is required. This can lead to friction, errors and slow integration development.

Agentic AI uses structured metadata to solve this by grounding natural language intent into executable function calls. It can parse the user’s request, search for relevant tools and generate the correct API invocation.

**Example**

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | { |
|  | "function": "createOrder", |
|  | "parameters": { |
|  | "customer\_name": "John", |
|  | "product": "iPhone 16", |
|  | "quantity": 2 |
|  | } |
|  | } |

The agent maps the intent to the correct function based on a *semantic match* to the tool’s description and schema.

### 2. Lack of Structured, Self-Describing APIs

Most APIs were built for human developers: swagger specs, Markdown docs and examples. However, AI agents need *machine-readable schemas* to reason about capabilities, input requirements and constraints.

Agentic AI works when APIs expose the following in a structured format:

* Function name and description
* Input parameters with types and constraints
* Authentication requirements
* Output schema
* Errors and limits

**Example Tool Schema**

This structure enables agents to:

* Validate inputs before execution.
* Build dynamic user interfaces (UIs).
* Choose tools based on context and task type.

### 3. Inconsistent Tool Invocation and Planning

In traditional workflows, APIs are manually stitched into automation logic. With agentic AI, *planning and execution are dynamic*. The agent:

* Reads the tool catalog.
* Matches the current user’s goal to the most relevant tool.
* Fills in parameters from context or prompts.
* Authenticates security.
* Executes the tool and observes outcomes.

**Example**

User prompt: *“Log a ticket for user 1234 saying their shipment didn’t arrive.”*

**Agent Invocation**

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | { |
|  | "function": "createSupportTicket", |
|  | "parameters": { |
|  | "customer\_id": "1234", |
|  | "issue": "Shipment not received" |
|  | } |
|  | } |

### 4. Choosing the Right Tool from Similar Options

APIs often have overlapping functionality:

* `getWeatherToday` vs. `getWeatherForecast`
* `searchFlights` vs. `recommendFlights`

Agents use **semantic similarity** to select the right tool. However, excessive similarity can confuse the agent.

**Solution**

* Use detailed, disambiguated descriptions.
* Include capabilities or intent tags.
* Score tool relevance based on embedding similarity plus historical success rate.

**Example Catalog With Capabilities**

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | { |
|  | "name": "searchFlights", |
|  | "description": "Find direct and connecting flights between cities", |
|  | "capabilities": ["search", "flight", "date", "filter"] |
|  | } |

By matching user input to capabilities, agents can disambiguate and select more accurately.

## How Structured Metadata Enables Dynamic Agent Behavior

Structured tool schemas help agents in the following ways:

`description`: Intent grounding; maps prompt to tool usage.  
`parameters`: Input validation, UI generation, prompt slot filling.  
`auth`: Execution occurs only with valid credentials.  
`capabilities:` Enable multistep planning and chaining of compatible tools.  
`rate limits`: Let agent reason about retry policies or tool availability.

This metadata is the foundation for **declarative, self-discoverable APIs,** consumable by agents without manual programming.

**Example: End-To-End Planning by an Agent**

User prompt: *“Translate ‘Good morning’ to Spanish and send it as a message to Carlos.”*

Tools in the catalog:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | [ |
|  | { |
|  | "name": "translateText", |
|  | "description": "Translate text between languages", |
|  | "parameters": { |
|  | "text": "string", |
|  | "target\_language": "string" |
|  | } |
|  | }, |
|  | { |
|  | "name": "sendMessage", |
|  | "description": "Send a message to a contact", |
|  | "parameters": { |
|  | "recipient": "string", |
|  | "message": "string" |
|  | } |
|  | } |
|  | ] |

**Agent Reasoning**

1. Detect task requires translation → `translateText`.
2. Store output → use as input to `sendMessage`.
3. Construct a plan:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | [ |
|  | { |
|  | "function": "translateText", |
|  | "parameters": { |
|  | "text": "Good morning", |
|  | "target\_language": "es" |
|  | } |
|  | }, |
|  | { |
|  | "function": "sendMessage", |
|  | "parameters": { |
|  | "recipient": "Carlos", |
|  | "message": "Buenos días" |
|  | } |
|  | } |
|  | ] |

Let’s explore tool calling with and without [large language models (LLMs)](https://thenewstack.io/introduction-to-llms) involved.

Here’s an example `HTTP GET` endpoint from the OpenAPI spec to retrieve details about a specific order based on the `orderNumber`:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | paths: |
|  | /{orderNumber}: |
|  | get: |
|  | summary: Retrieve the details of your order. |
|  | parameters: |
|  | - name: orderNumber |
|  | in: path |
|  | description: >- |
|  | Order number to lookup - you should find this in your confirmation |
|  | e-mail |
|  | required: true |
|  | schema: |
|  | type: string |
|  | responses: |
|  | '200': |
|  | description: Order found successfully |

Here’s an example [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) server snippet from the above specification that returns details about a specific order based on the `orderNumber`:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | @mcp.tool(description= "Retrieve the details of your order.") |
|  | def OrdernumberGet(orderNumber:str): |
|  | manufactured\_params = {} |
|  | for param in ['orderNumber']: |
|  | if locals()[param] is not None: |
|  | manufactured\_params[param] = locals()[param] |
|  | try: |
|  | response = requests.get(f'{base\_url}/{orderNumber}', headers=headers, params=manufactured\_params, verify=False).json() |
|  | except Exception as e: |
|  | response = {"error": str(e)} |
|  | return response |

Here’s a code snippet for an MCP client discovering the tools:

This example shows an MCP calling an MCP server without involving an LLM.

[![MCP calling MCP server without using an LLM](https://cdn.thenewstack.io/media/2025/07/6abbcb00-no-llm-1.png)](https://cdn.thenewstack.io/media/2025/07/6abbcb00-no-llm-1.png)

Source: IBM.

And here’s an agent calling with a user request that uses an LLM:

User request: “*Get order details for order number 1.”*

[![Agent is using LLM, Claude Desktop](https://cdn.thenewstack.io/media/2025/07/db1f8e24-claude-order-details.png)](https://cdn.thenewstack.io/media/2025/07/db1f8e24-claude-order-details.png)

Source: IBM.

Add another order API to the MCP server. This time, make the description a bit more specific.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | @mcp.tool(description= "Returns Order Details given an order number.") |
|  | def GetOrdernumber(orderNumber:str): |
|  | manufactured\_params = {} |
|  | for param in ['orderNumber']: |
|  | if locals()[param] is not None: |
|  | manufactured\_params[param] = locals()[param] |
|  | try: |
|  | response = {"response": str("The shipment status is NOT Shipped yet")} |
|  | except Exception as e: |
|  | response = {"error": str(e)} |
|  | return response |

The MCP client now detects two endpoints:

[![MCP detects two endpoints](https://cdn.thenewstack.io/media/2025/07/bc776aeb-mcp-two-endpoints-1.png)](https://cdn.thenewstack.io/media/2025/07/bc776aeb-mcp-two-endpoints-1.png)

Source: IBM.

This time, for the same user request, the agent uses the new, updated API:

User request: “*Get order details for order number 1.”*

[![Using the new API](https://cdn.thenewstack.io/media/2025/07/910b0e53-using-new-api.png)](https://cdn.thenewstack.io/media/2025/07/910b0e53-using-new-api.png)

Source: IBM.

## **Conclusion**

The metadata influences how agents pick an API over the other. Tweaking the metadata can have undesired consequences.

Agentic AI is rapidly redefining the way APIs are consumed:

* APIs must be self-describing, machine-readable and intent-grounded.
* Tool catalogs must expose metadata such as schema, parameters, capabilities and constraints.
* Agents can dynamically reason, plan and invoke APIs — unlocking fast, smart and more autonomous integrations.

As we move into the age of AI-native development, designing for agent-first consumption is not optional — it’s the foundation for intelligent automation and adaptive workflows in hybrid environments, and protocols like MCP play a crucial role in this evolution.

*IBM is working to bring autonomy, intelligence and collaboration to enterprise integration. [Learn more](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.426619851;dc_trk_aid=618928292;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1) about [IBM webMethods Hybrid Integration](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.426621492;dc_trk_aid=619117818;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1).*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/07/ca6ec632-nazrulislam.jpg)

Nazrul serves as the Chief Architect for AI, IBM Integration Platform, where he strategically guides innovation and architectural excellence across the organization's AI-driven initiatives. In his current role, Nazrul is pivotal in steering the strategic direction and innovation of the...

Read more from Nazrul Islam](https://thenewstack.io/author/nazrul-islam/)