You open Claude Code or Cursor, describe your tables, and in seconds the AI hands you a Postgres schema that looks… fine. It runs. Your tests pass. You ship.

What you don’t see are the quiet little disasters tucked inside: money for prices, a BRIN index on random data, SERIAL and UUID mixed like a cocktail, timestamp without time zone because some tutorial said it was “easier”.

Fast-forward six months. You’re debugging currency-conversion bugs, chasing timezone ghosts, rewriting migrations, and adding the index that should have existed since day one. The code the AI agent wrote worked; it just wasn’t good. It was copying whatever examples it scraped from the entire internet.

And that’s the problem. It learned SQL from everywhere: Postgres, MySQL, SQLite, SQL Server, Oracle, random tutorials, and a decade of Stack Overflow answers. In all that noise, the nuances of idiomatic, high-quality Postgresget buried under the good, the bad, and the MySQL.

So we built something to fix that.

## Giving AI the Postgres Judgment It’s Missing

pg-aiguide gives AI coding agents the Postgres-specific judgment they’re missing.It does this with three things working together:

1. **AI-optimized “skills”**— curated, opinionated Postgres best practices that Claude Code and other agents can apply automatically.
2. **Semantic search across official documentation** — version-aware retrieval for Postgres 15–18.
3. **Extension ecosystem docs**, starting with TimescaleDB and expanding quickly

You can connect it to any AI coding agent via our public **Model Context Protocol (MCP) server** or with the **Claude Code plugin** built to take advantage of Claude’s native skill support. No accounts. No usage limits. Completely free.

The goal is simple:**Make AI write correct, production-ready Postgres by default.**

You shouldn’t have to paste docs, correct outputs, or rely on prompt hacks. The AI should just generate better SQL the first time.

💡

****Try it now**** 

You can start using pg-aiguide in less than a minute. It works with Claude Code, Codex, Cursor, Gemini CLI, Visual Studio, VS Code, Windsurf, and any other MCP compatible editors. See our

[quickstart guide](https://github.com/timescale/pg-aiguide/tree/main?tab=readme-ov-file#-quickstart)

for installation instructions.

## Why Database Code Quality Is So Important

AI adoption among Postgres developers has exploded: jumping from 37% to 55% in a single year according to the [2024 State of Postgres](https://www.tigerdata.com/state-of-postgres/2024) survey. But as LLMs get more general, the training data has become broad instead of specialized and the LLMs become *less* precise.

This creates a surprising problem: A study by METR recently found that experienced developers using AI actually took **19 percent longer** to complete tasks. Not because the AI failed, but because the output was almost right—the kind of subtle mistakes that take the longest to spot, debug, and unwind.

With databases, “almost right” compounds quickly.

Schemas codify decisions that are painful to change later. Indexing mistakes hide until your tables grow. Datatype choices that take an hour to fix in development can take days of migrations and careful planning in production.

You can refactor application code. You can’t refactor state without consequences.

pg-aiguide stops these mistakes at the source, before they get baked into production.

## Generic vs. Guided SQL

Here’s what happens when you ask a coding assistant to design a simple bookstore schema.

### Without pg-aiguide

```
CREATE TABLE customers (
    customer_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE INDEX idx_customers_email ON customers(email);

CREATE TABLE authors (
    author_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    biography TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

```

Copy

This schema works, but has classic issues:

* mixed identity strategies
* arbitrary `VARCHAR` limits
* case-sensitive email uniqueness
* timestamp defaults that behave inconsistently across systems

### With pg-aiguide enabled

```
CREATE TABLE authors (
  author_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name TEXT NOT NULL,
  bio TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX ON authors (name);

CREATE TABLE users (
  user_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  email TEXT NOT NULL UNIQUE,
  password_hash TEXT NOT NULL,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  phone TEXT,
  is_active BOOLEAN NOT NULL DEFAULT true,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE UNIQUE INDEX ON users (LOWER(email));
CREATE INDEX ON users (created_at);
```

Copy

This version uses:

* consistent identity columns (`BIGINT GENERATED ALWAYS AS IDENTITY`)
* `TEXT` instead of unnecessary `VARCHAR`
* correct timestamp handling (`timestamptz + now()`)
* case-insensitive uniqueness enforced properly

Behind the scenes, the AI used the [design\_postgres\_table skill](https://github.com/timescale/pg-aiguide/blob/main/skills/design-postgres-tables/SKILL.md) either through the [view\_skill](https://github.com/timescale/pg-aiguide/blob/main/API.md#view_skill) MCP tool or [Claude’s native skills framework](https://www.claude.com/blog/skills). In both cases, the agent automatically discovered and applied the Postgres-optimized guidance without human intervention.

You didn’t have to prompt differently.

You didn’t have to paste in docs.

**pg-aiguide automatically shifts AI from “SQL that works” to “SQL you’d actually want in production.”**

## The Skills Are the Secret Sauce

If you want AI to generate high-quality SQL, it is not enough to let it search the manual. A manual tells you what you can do, not what you should do. Skills fill that gap. They give the model judgment, not just facts.

Our skills are not trying to reteach the LLM syntax or capabilities. Instead they give the model the context it needs to make better choices. Here is an excerpt from a real skill.

```
## Postgres "Gotchas"

- **FK indexes**: Postgres **does not** auto-index FK columns. Add them.
- **No silent coercions**: length/precision overflows error out (no truncation). 
  Example: inserting 999 into `NUMERIC(2,0)` fails with error, unlike some 
  databases that silently truncate or round.
- **Heap storage**: no clustered PK by default (unlike SQL Server/MySQL InnoDB); 
  row order on disk is insertion order unless explicitly clustered.
```

Copy

These are the kinds of details you only know once you have lived in Postgres for a while. They trip up LLMs for the same reason they trip up developers who are new (and not so new) to the database. Yet these details are exactly what allow the model to produce better SQL.

In our evaluations (currently human-vibes-driven, soon LLM-judged), schema quality improves consistently when we compare a system with just semantic search to one that includes both semantic search and skills:

* more appropriate data types
* correct timestamp semantics
* stronger indexing strategies
* fewer migration pitfalls
* fewer long-term performance surprises

This is what “AI coding tools actually understanding Postgres” looks like.

## The Tools We Provide The LLM

pg-aiguide provides two core capabilities that map cleanly to how AI coding tools operate.

### 1. Skills: Complete, Opinionated Postgres Guidance

`view_skill` returns full, AI-optimized best practices.These aren’t tutorials and they aren’t vague prompts. They’re machine-targeted, dense, token-efficient guidance that the AI can reliably use.

For example:

* prefer `BIGINT GENERATED ALWAYS AS IDENTITY`
* don’t use `money`
* don’t use `timestamp` without timezone
* index your foreign keys
* expect errors on precision overflows

Skills don’t need to be chunked—they are written so that each skill fits in context as a single complete unit.

Claude Code even supports skills natively, so the MCP server’s `view_skill` tool is disabled automatically when running as a plugin.

### 2. Semantic Search: Version-Aware Vector Retrieval Across Docs

The MCP tools `semantic_search_postgres_docs` and `semantic_search_tiger_docs` allow the AI to pull in the **correct** documentation for the Postgres version you’re targeting.

This matters because Postgres versions evolve meaningfully:

* Postgres 15: `UNIQUE NULLS NOT DISTINCT`
* Postgres 16: major changes to parallel query behavior
* Postgres 17: COPY error-handling improvements

Without version awareness, an AI can (and does) hallucinate features or syntax that will break your actual environment.

All of this knowledge of Postgres is chunked, embedded, and stored in Postgres itself.

We scrape official HTML docs, preserve header context, attach source URLs, and use character-bounded chunking with H1→H2→H3 breadcrumbs so each piece retains meaning of how it fits into the broader puzzle.

## Help Us Build the World’s Best Postgres Guide for AI

Postgres has 35 years of engineering, craft, and hard-won lessons behind it. No single team can capture all of that. The community built the patterns, extensions, and production wisdom that make Postgres what it is. AI coding tools should reflect that depth, not spit out generic SQL lifted from outdated tutorials and old Stack Overflow posts.

pg-aiguide is our first step toward making Postgres the best database to use with AI coding assistants on purpose, not by accident. We are expanding the skill library with richer indexing guidance, full-text search skills, and documentation for essential extensions like PostGIS and pgvector. We are also adding keyword BM25 search to pair with semantic search for more accurate retrieval. **But we need your help.**

### How You Can Contribute

You can make an immediate impact:

* add documentation for your Postgres extension
* contribute new skills that encode real, battle-tested expertise
* help evaluate, refine, and stress-test existing skills
* request features or report issues
* improve semantic search chunking or propose new areas to index
* share deep knowledge on partitioning, replication, security, or performance tuning

Skills matter most. They turn years of experience into guidance the AI can use instantly. Our schema-design skill went through multiple iterations before it felt right, and we learned a ton in the process. We would love to partner with you to build skills in your area of expertise.

pg-aiguide is fully open source at github.com/timescale/pg-aiguide.

**Help us teach AI to write Postgres like an expert.**