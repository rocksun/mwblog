[Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) (AWS) is [launching](https://aws.amazon.com/blogs/opensource/introducing-strands-labs-get-hands-on-today-with-state-of-the-art-experimental-approaches-to-agentic-development/) [a dedicated GitHub organization](https://github.com/strands-labs) for its most experimental agentic AI work.

On Monday, the company launched Strands Labs, where teams across Amazon will publish frontier projects that aren’t quite ready for inclusion into the production-ready version of the company’s Strands Agents SDK.

The initial release includes two projects: AI Functions, which generates code at runtime from natural-language specifications, and Strands Robots, which connects large language models to physical hardware via vision-language-action (VLA) models.

## Why a separate org?

The Strands Agents SDK, which AWS first open-sourced in May 2025, has been downloaded 14 million times, according to Clare Liguori, a Senior Principal Engineer at AWS who leads work on both Strands and the Kiro AI coding assistant. The SDK now ships in Python and TypeScript, and AWS uses it internally for production workloads.

That traction is precisely why Liguori’s team felt it needed a boundary between the stable SDK releases and more experimental work. “We want to make sure that the SDK continues to focus on that production-ready solution,” Liguori tells *The New Stack*.

> “We want to make sure that the SDK continues to focus on that production-ready solution… [Strands Labs] gives both Amazon’s internal teams and the wider Strands community a place to iterate…”

Strands Labs gives both Amazon’s internal teams and the wider Strands community a place to iterate on ideas where “the interfaces might change a lot,” she adds, without destabilizing the core SDK’s API surface.

So while all Strands Labs projects will ship with documentation, functional code, and basic tests, users should expect breaking changes.

Even before the launch of Strands Labs, AWS had already pushed some experiments into the Strands SDK, but, as Liguori acknowledges, today those would likely have gone into Strands Labs first. One of those was an experiment in steering the agent, for example.

## AI Functions: Prompts instead of code

For developers, the most interesting of these two current experiments is likely AI Functions. This lets developers define what a Python function should do in natural language, along with preconditions and postconditions that act as guardrails. At runtime, a coding agent then generates the implementation.

Since the agents aren’t always perfect, the built-in deterministic guardrails should ensure that if the output isn’t correct, the agent self-corrects and tries again.

Liguori uses the example of a receipt parser. Receipts vary wildly in format, making deterministic code brittle. With AI Functions, a developer specifies that the function must return a vendor name, a total price, and line items, and the agent handles the edge cases.

What’s important here is that from the program’s perspective, this looks like any other function. “It’s not this separate thing that’s an agent,” Liguori says. “It’s a normal function” embedded in otherwise deterministic logic.

`@ai_function(  
code_execution_mode="local",  
code_executor_additional_imports=["pandas.*"],  
)  
def fuzzy_merge_products(invoice: DataFrame) -> DataFrame:  
"""  
Find product names that denote different versions of the same product, normalize them  
by removing version suffixes and unifying spelling variants, update the product names  
with the normalized names, and return a DataFrame with the same structure  
(same columns and rows).  
"""`  
 `# Load a JSON (the agent has to inspect the JSON to understand how to map it to a DataFrame)  
df = import_invoice('data/invoice.json')  
print("Invoice total:", df['price'].sum())`

`# Load a SQLite database. The agent will dynamically check the schema and generate  
# the necessary queries to read it and convert it to the desired format)  
df = import_invoice('data/invoice.sqlite3')  
# Merge revisions of the same product  
df = fuzzy_merge_products(df)`

Longer term, the team sees AI Functions as a path toward a feedback loop: run an agentic function millions of times in production, observe which code paths emerge, and eventually collapse the results back into deterministic code that no longer needs a model call.

One thing the Strands team has always stressed is its belief that the models will only get better, so the agent framework should get out of the way as much as possible. In many ways, AI Functions is a push in that direction, too, with its focus on models’ ability to write code as needed.

## Robots reasoning in the cloud

Strands Robots tackles a very different problem. It pairs lightweight, low-latency VLA models running on local hardware with frontier LLMs in the cloud. Frontier models, after all, are too computationally intensive to run directly on a robotic arm. But for the robot to work efficiently, you need to bring latency down as much as possible.

AWS is partnering with Nvidia and Hugging Face on the project, and the team is also releasing a simulated environment so developers can iterate without a physical robot on their desk.

Liguori says the team has been running proof-of-concept work with AWS customers, and she noted that Amazon itself, obviously, runs a very large fleet of warehouse robots. But she also sees applications for in-vehicle AI, for example, and other edge scenarios that need both domain-specific local inference and the kind of long-horizon planning that modern LLMs can offer.

## Agent frameworks everywhere

AWS is obviously not the only hyperscaler investing heavily in agent frameworks ([and there are reasons for that](https://thenewstack.io/agent-framework-container-wars/)). Google’s [open-source Agent Development Kit](https://google.github.io/adk-docs/), announced at Cloud Next 2025, targets multi-agent orchestration. Microsoft’s [Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?pivots=programming-language-csharp), one of the few agentic frameworks to support .NET, recently [reached](https://devblogs.microsoft.com/foundry/microsoft-agent-framework-reaches-release-candidate/) its Release Candidate status. And startups like CrewAI, LangGraph, and others are already major players in this field, with personal agents also taking off thanks to the hype around [OpenClaw](https://thenewstack.io/deno-sandbox-security-secrets/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)