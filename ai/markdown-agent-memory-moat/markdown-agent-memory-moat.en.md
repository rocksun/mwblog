In April, Andrej Karpathy published a GitHub gist file called “[LLM Wiki,”](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) a brief text document designed to help one build a personal knowledge base using LLMs. It’s based on the premise that an AI agent will keep what it knows as linked Markdown files it can read and rewrite, because a language model does not get bored maintaining cross-references and can touch fifteen files in a single pass. It was only a few thousand words with no product attached.

Two months later, Google turned that instinct into a published standard called the [Open Knowledge Format](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing). The OKF packages organizational knowledge, metrics, tables, and runbooks as plain Markdown that any agent can read without a proprietary account. Google is careful to call it `v0.1` — a starting point rather than a finished standard.

[Garry Tan](https://www.ycombinator.com/people/garry-tan), the Y Combinator president, got there first in a different lane. His [gstack](https://github.com/garrytan/gstack), an MIT-licensed Claude Code setup that crossed 66,000 GitHub stars within weeks, comprises 23 specialist roles, each a Markdown file. No runtime; no code; just prose that runs across ten different coding agents.

## Markdown has become the substrate agents read and write

Three approaches, three different needs, one common solution. Karpathy sought agent memory, Google aimed for enterprise context in BigQuery agents, and Tan wanted a way to summon an engineering team from a terminal. All three turned to the same basic resource: a folder of Markdown files versioned in git.

Developers had already established this practice. [CLAUDE.md](https://code.claude.com/docs/en/memory#claude-md-files) and [AGENTS.md](https://agents.md/) are present in millions of repositories as the initial files an agent loads. OKF and gstack are the evolved forms of this convention – one focused on what the agent knows, the other on how it behaves.

This is the Git and JSON playbook tied to the agent’s knowledge. The formats that survived are the ones you could start using without changing anything. You can simply cat the file, clone the repo, and any tool you already use can parse it. MCP remains important as the interface an agent connects to. Markdown is becoming the format that carries the content.

## The lock-in moved from the model to the files

The significant factor to observe here is the competitive advantage, not technical specifics. For two years, the belief was that owning the best model meant controlling the developer.

This perspective is now shifting. Replacing Claude with GLM or Codex, gstack continues to operate because the core intelligence evolved, but the documentation did not.

> The moat is shifting from the model to the Markdown a team owns and accumulates over time.

The moat is shifting from the model to the Markdown a team owns and accumulates over time. A company’s OKF bundle, including its runbooks, metric definitions, and architecture decisions, is, by design, portable across clouds, models, and frameworks.

That kind of portability is the reason vendor-neutral formats exist and why Google’s OKF deserves a closer look.

> If no one develops consumers for it, it remains just a good idea that Google released on a slow Friday.

The area where I am most likely mistaken is durability. Declaring Markdown standards is easy, but making them reliable is difficult. OKF is merely a 0.1 draft with a reference implementation, not a full ecosystem. If no one develops consumers for it, it remains just a good idea that Google released on a slow Friday.

The direction remains determined by three separate bets targeting the same file format within a single quarter. Your next agent is likely to interpret its context from a Markdown folder, and the creator of that folder now possesses an advantage that the model vendor cannot easily replicate.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)