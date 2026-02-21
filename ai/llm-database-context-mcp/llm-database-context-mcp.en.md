LLMs are [accelerating work across engineering disciplines](https://clickhouse.com/blog/agent-facing-analytics), from generating React components and building backend APIs to noodling with SQL. But we all know LLMs make mistakes, and the nature of those mistakes varies dramatically across domains. Using LLMs with databases is deceptively error-prone.

When an LLM generates a React component, errors tend to surface quickly. The code either fails to compile or renders something visibly wrong: a button in the wrong place, a modal that won’t close, or a layout that breaks on mobile. You look at the screen, and something is obviously off.

You don’t really get that with databases. When an LLM generates a SQL query, it either fails to execute or it runs successfully. And here’s the problem: A query that runs successfully can still be completely wrong. If you’re filtering rows by a condition, how do you verify that every one of the 4,000 returned rows actually matches? If you’re computing an aggregate, how do you validate the final number when you can’t see which rows contributed to it? These are opaque answers that aren’t quick or easy for a human to validate.

> “A query that runs successfully can still be completely wrong. … These are opaque answers that aren’t quick or easy for a human to validate.”

This creates a dangerous failure mode. LLMs are remarkably good at producing syntactically valid queries. They’re far less reliable at producing semantically correct ones.

## The scale of the semantic correctness problem

[Analysis](https://www.usedatabrain.com/blog/llm-sql-evaluation) of 50,000+ production queries showed that most “broken” queries actually execute successfully and return data. A user asks for “revenue by product category” and uses a “revenue” column in the products table, even though it actually exists in the order\_items table. The query runs. Numbers appear. A CFO makes decisions based on metrics that are silently, completely wrong.

Often, LLMs take the first seemingly correct path and fail to explore alternatives, missing the actually correct path entirely. Similar results are seen when [researching](https://clickhouse.com/blog/llm-observability-challenge) whether LLMs can perform root-cause analysis on observability data, which found that LLMs would routinely get stuck with tunnel vision and end up in the wrong place with the wrong answer.

These incorrect assumptions often stem from missing semantic context, which particularly affects work with databases.

## Why LLMs need context for databases

Three characteristics make database work especially susceptible to silent LLM failures.

Firstly, SQL dialects diverge in ways LLMs don’t anticipate. There’s a wealth of knowledge out there about SQL, which you’d think would give LLMs all the training data they’d ever need. But even among humans, SQL is often misunderstood as a uniform, fully standardized language (and, given that LLMs are trained on human output, we only have ourselves to blame for their confusion). While the basics of SQL can often be ported between databases, most databases adapt SQL to create their own dialect. These differences can be subtle, where similar intent is implemented with slightly different syntax, or dramatic, which renders a lot of “general wisdom” useless.

Secondly, the real-world is messy, as are our schemas. Column names like “amount” could mean gross revenue, net revenue, or quantity. Tables named “users” and “customers” might overlap or be completely distinct. There’s probably a bunch of deprecated schemas, tables, and columns floating around that are kept for some legacy use case. LLMs do their best to pattern-match what they see against what they’ve been trained on, but end up making confident guesses that are [frequently wrong](https://arxiv.org/html/2501.09310v1): inventing columns that don’t exist or joining tables on the wrong keys.

Lastly, humans tend to communicate ambiguously, which leads to misinterpretation. Some of this comes from our laziness and from hoping the robot will just work it out for us, while some comes from assuming the listener has the same background and understanding as we do. For example, in some countries, financial years align with calendar years, but not in all. So, when is FY2026 Q1? If you’re a bank in Europe, one billion is a million million, but to a bank in the USA, it’s one-thousand million. LLMs may know that these differences can exist, but how will they know which one applies to you?

They need context!

## There are many ways to provide context

Many of these failures stem from a common setup: using frontier LLMs out of the box with minimal context about your specific environment. The model knows SQL in the abstract but nothing about your schema, your dialect’s quirks, or your business logic.

> “The model knows SQL in the abstract but nothing about your schema, your dialect’s quirks, or your business logic.”

The past year has seen rapid development in methods for giving off-the-shelf LLMs personalised context. At the end of 2024, Anthropic released the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro), which enables standardized connections between LLMs and external tools such as databases. In mid-2025, OpenAI introduced the [AGENTS.md](http://AGENTS.md) convention: a single Markdown file that provides domain-specific context that travels with your codebase. Toward the end of 2025, Anthropic followed up with [Agent Skills](https://agentskills.io/home), which provides modular, on-demand capabilities that agents can invoke when needed.

Each approach offers different capabilities and ways to address the context problem.

MCP servers provide structured tool access that enables your LLMs to interact directly with your database. Rather than asking an LLM to just generate some SQL and give you the text, MCP lets you expose specific capabilities: query execution, schema introspection, and table metadata. There’s a huge breadth of MCP servers that cover just about any database you can imagine, such as [ClickHouse](https://github.com/ClickHouse/mcp-clickhouse), Postgres, and MongoDB. With MCP, the LLM can search for context within the system itself.

AGENTS.md embeds context in a markdown file that you can store in your repository along with your code. You can simply document your schema conventions, business logic, and anything else noteworthy in one file. It has very little overhead, being just a text file, and can be very efficient. However, context bloat is a well-known problem with LLMs, and the downside of AGENTS.md is that the file is always loaded in full. A big file could take up a meaningful chunk of context.

Agent Skills is similar to AGENTS.md, but is modular and allows progressive loading of context. Rather than a single file, knowledge is broken into separate files called Skills. The agent can list the available files to build a lightweight index of its skills and choose to read a skill when it is relevant to the task at hand.

The upside to skills is that unused knowledge doesn’t take up an LLMs limited context window. But it assumes the LLM correctly and consistently knows when to invoke a skill and chooses the right one. Vercel maintains a [marketplace of Agent Skills](https://skills.sh) that includes database-specific skills for databases such as ClickHouse and PostgreSQL.

We don’t need to rely solely on these “LLM-native” answers, either. Databases like ClickHouse, PostgreSQL, and MySQL have supported storing context before LLMs existed, via the [COMMENT syntax](https://clickhouse.com/docs/sql-reference/statements/create/table#comment-clause) on tables and columns. This metadata travels with the schema, meaning it can assist LLMs whether they’re seeing it in a Git repo or by describing entities via MCP. It’s an elegant way to add context that you’ve probably already got.

## So which to choose?

Vercel recently [evaluated](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals) AGENTS.md against agent skills for their own framework documentation, and the results were quite interesting. AGENTS.md achieved a 100% pass rate while skills maxed at 79%. In 56% of test cases, agents never invoked available skills. The documentation existed; the agent could access it, but it never did.

It’s likely that LLMs will improve on their tool-calling abilities, which will make Agent Skills more consistent. But it’s also likely that models will continue to ship with larger and larger context windows. It’s not yet clear whether AGENTS.md or Agent Skills will win and become the de facto answer, or if we’ll pick the one that best suits our situation. Even then, there’s a compelling case to keep semantic context within the database objects themselves.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/11/c15429d3-cropped-aa698fc3-alasdair_brown.jpeg)

Alasdair Brown has spent the past decade designing, building and operating data platforms, from user-facing, real-time analytics for top brands, to some of the world's largest nation state cyber-defense systems. He is an advocate for simple data architectures and often...

Read more from Alasdair Brown](https://thenewstack.io/author/alasdair-brown/)