Before an AI coding agent writes a single line of code, it has already spent tokens. For example, on source files, ticket descriptions, build logs, quality findings, and dependency alerts. Most of what you pay for isn’t the pull request; it’s everything the agent read to get there.

Teams often focus their cost controls on model choice, prompt length, and request limits. Those are worthwhile levers, but a less visible one sits in the interfaces between agents and developer tools: the format of the data returned to the model.

> “Token costs are shaped not only by what coding agents read, but also by how development tools package that information.”

When a tool returns a long list of similarly shaped records, sending verbose JSON can make the agent pay repeatedly for field names, quotation marks, and structural syntax. The content is useful; much of the representation is not. For [agentic development workflows](https://thenewstack.io/what-agentic-workflows-mean-to-microservices-developers/), the output format is an engineering decision, not a cosmetic one.

This does not mean every integration should abandon JSON. JSON remains a broadly supported interchange format and can be the more compact choice for nested or irregular data. The practical question is narrower: when a model needs to consume a large, uniform collection, can the tool return the same information in a representation designed for that shape?

## Why structure becomes part of the token bill

Consider an issue list. Each entry may include an identifier, rule, severity, file, line number, message, status, and estimated remediation effort. In conventional JSON, those labels appear for every record:

```

{
  "key": "AZ1002fQ9x",
  "severity": "BLOCKER",
  "component": "src/main/java/com/acme/UserRepo.java",
  "line": 29,
  "status": "OPEN"
}

```

That is readable and useful for many systems. But an agent inspecting 25, 100 or 500 findings does not need to be told the meaning of severity or component hundreds of times. Repeating those labels consumes context that could instead hold more relevant evidence, instructions or source code.

Token-Oriented Object Notation (TOON) is one approach to this problem. It keeps a schema-like header for a uniform array and then sends each record as a row. The field names appear once, while the values remain intact. It is a lossless encoding of the JSON data model for the data shapes it targets.

> “A regular structure gives a model an explicit set of fields to expect, which can make review and validation more predictable.”

The result is not merely smaller text. A regular structure gives a model an explicit set of fields to expect, which can make review and validation more predictable. The agent receives the same findings, but with less repeated scaffolding around them.

## Measure a real workflow, not a synthetic promise

The useful unit of analysis is a team’s actual tool output and actual model. Character counts are a helpful first signal, but [tokenization differs across models](https://thenewstack.io/agent-harness-token-costs/). Rather than assume a universal percentage, capture a representative response, run it through the tokenizer or format utility relevant to the workflow, and compare it with the current default.

For example, the Sonar CLI can return an issue list as JSON or TOON:

```

# Default JSON output
sonar list issues -p my-org_my-app --severities BLOCKER,CRITICAL --format json > issues.json

# Evaluate the same data with the TOON CLI
npx @toon-format/cli issues.json --stats

# Return compact, lossless output directly to an agent
sonar list issues -p my-org_my-app --severities BLOCKER,CRITICAL --format toon

```

The first command preserves a baseline. The second reports the savings for the actual payload. The third applies the alternative only where the consumer is an agent.

I saw this myself when generating a representative 25-issue comparison: TOON used 49% fewer characters than pretty-printed JSON and 33% fewer than minified JSON. The [TOON project’s published benchmarks](https://github.com/toon-format/toon) also report lower token usage for uniform tabular datasets, alongside comparable retrieval accuracy in its test set. Those results should be treated as directional evidence, not a substitute for measuring a production payload with the model a team has selected.

## Use the format that fits the reader

A durable rule is to choose the format based on the consumer and the shape of the data:

* Use a table when a person needs to scan a short result in a terminal.
* Use standard JSON when a script, API client or deeply nested payload benefits from its familiar structure.
* Consider a compact, schema-first representation such as TOON when an LLM is reading many records with the same fields.

The last case matters because coding agents increasingly call tools in loops. An agent may list findings, inspect affected files, make a change, run an analysis, and list the remaining findings. A modest reduction in one response compounds when the same workflow runs across repositories and iterations.

> “A cheaper context that causes a weaker decision is not a cost improvement.”

Still, compactness is not the only requirement. The format must preserve the fields the agent needs to make a sound decision. It must be accepted by the toolchain. And it should be validated against the tasks that matter: identifying the highest-priority finding, locating the affected code, and determining whether remediation is complete. A cheaper context that causes a weaker decision is not a cost improvement.

## Treat tool responses as part of agent design

The broader lesson is that agent cost is partly a context-design problem. Teams can [reduce unnecessary context](https://thenewstack.io/how-to-reduce-mcp-token-bloat/) in several complementary ways: retrieve only relevant files, return tool results at the right level of detail, and avoid repeatedly transmitting structural overhead. None of these changes requires reducing the quality bar for code or security findings.

Start with the highest-volume structured call in an agent workflow. Measure the baseline. Change one format setting. Then assess token consumption, response quality, and task completion together.

That approach is intentionally modest. It avoids a platform rewrite and makes the trade-off visible. As AI-assisted development increasingly becomes a routine part of engineering work, disciplined choices about what agents see, and how they see it, will be as important as the models they use.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/08/5659f85b-cropped-e00a390f-prasenjit-sarkar-scaled-1-600x600.jpeg)

Prasenjit A. Sarkar is product and solutions marketing manager at Sonar. With over 20 years of experience in the technology industry, he is a seasoned technology and product leader who is passionate about building and scaling innovative AI products. He...

Read more from Prasenjit A. Sarkar](https://thenewstack.io/author/prasenjit-a-sarkar/)