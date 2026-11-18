![DuckDB is entering a new era following AWS’s acquisition of DuckLabs and the release of DuckDB 2.0.0, its biggest feature update to date. In this episode of The New Stack Podcast, Gábor Szárnyas, developer advocate at DuckLabs, discusses how the high-performance analytical database is evolving to support AI agents, faster queries, and more flexible data processing.](https://cdn.thenewstack.io/media/2026/11/90305fd8-thumbnail-23-1024x576.png)

DuckDB has always been the database you don’t have to set up: Import it into your code and start querying. DuckDB 2.0 was released in October, and it can now run as a server that other machines can connect to. DuckLabs’ [Gábor Szárnyas](https://www.linkedin.com/in/szarnyasg/) calls this the headline feature of the release.

The team decided to make this latest upgrade a major release since that feature, along with a new storage format and a new SQL parser, marks a big shift in how DuckDB works. On *The New Stack* podcast, [Szárnyas](https://www.linkedin.com/in/szarnyasg/) explains what changed, what early users are teaching the team ahead of the 2.0.1 bug-fix release, and how to plan a production upgrade.

VIDEO

Codenamed Cinnamon Teal, DuckDB 2.0 is the analytical database’s biggest feature release to date, more than two years after 1.0.0.

We met with Szárnyas, head of developer relations at DuckLabs, at the company’s Amsterdam headquarters. DuckDB 2.0 can run as a server and query data faster.

“The other features are an extensible SQL parser, which was experimental earlier this year, but now is something that we turn on by default. That ideally doesn’t break anything, but it might,” Szárnyas says. “We also wanted to signify this with the release and the whole approach to doing more of a networked operation, shipping the [Quack remote protocol](https://duckdb.org/quack/) as a first-class citizen in DuckDB.”

Database files created with DuckDB 2.0 can’t be opened by earlier versions, though 2.0 can still read and write existing database files, which stay readable by older versions. For production systems, Szárnyas repeats a common rule of thumb in the database world: “you should never migrate to a .0 release in production.” Depending on a team’s risk tolerance, he says, 2.0.1 or 2.0.2 is the version to move production to. The team is working on 2.0.1 now, focused on bug fixes, small performance tweaks and user feedback.

DuckDB 2.0.0 already includes dedicated [Agent Mode](https://duckdb.org/docs/2.0/clients/cli/agent_mode), which makes it easier for AI coding agents to interpret errors and correct their own SQL queries, helping them get better results faster without wasting tokens.

> “The AI doesn’t really care. The large language models don’t mind if a text is formatted badly or the punctuation isn’t perfect.”

“For AI agents, we just print simple Markdown tables in compact mode with no spacing. The AI doesn’t really care. The large language models don’t mind if a text is formatted badly or the punctuation isn’t perfect,” Szárnyas says, which lets DuckDB “compress these tables down to maybe 60, 70% of their original size. It is just as legible for the agent.”

Agent Mode comes with no hidden truncation, machine-readable errors structured in JSON, and guardrails against runaway queries, and it works with coding agents such as Claude Code, Codex, and Cursor.

Following Amazon’s announcement to acquire DuckLabs in August, AWS [shared how it uses the in-process analytical engine internally](https://aws.amazon.com/blogs/big-data/aws-and-ducklabs-building-the-future-of-analytics-together/), including to query in S3 Tables. Mai-Lan Tomsen Bukovec, AWS’s technology VP, says AWS has processed more than 2.5 billion queries using its custom Quick query engine with DuckDB integrations and optimizations. She writes that DuckDB has helped Amazon Quick reduce average query latency by 30%.

DuckDB is also set to become the universal SQL dialect of AWS Storage and Analytics. In its Q3 earnings call in October, Amazon CEO Andy Jassy remarked that this will simplify data processing with “a modern analytics engine that is fast, simple to use and ubiquitous, and where customers will be able to write SQL queries once and then execute using any AWS analytics service.” This includes zero migration or portability costs between query engines, which Jassy said will also help AI agents query data efficiently.

The post [DuckDB 2.0 goes client-server and adds an Agent Mode for coding agents](https://thenewstack.io/duckdb-storage-compatibility-agents/) appeared first on [The New Stack](https://thenewstack.io).