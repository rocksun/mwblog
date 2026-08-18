Google has a new Gemini model, and no, it is not Gemini 3.5 Pro. Gemini 3.7 Flash launched Thursday as the company’s new workhorse for coding agents and automated business workflows, just three weeks after Gemini 3.6 Flash became available.

The quick turnaround may cause some version fatigue, but Google says the new model is better at writing code and handling the longer workflows that keep agents on track. Google has paired those improvements with an introductory API price that is half the original cost of Gemini 3.6 Flash, but with a caveat; that price will increase on January 1, 2027.

> Google says Gemini 3.7 Flash is less likely to get stuck when something goes wrong and better at knowing when it needs more information before moving forward.

## Coding benchmarks jump sharply

Google says Gemini 3.7 Flash is less likely to get stuck when something goes wrong and better at knowing when it needs more information before moving forward. The model scored 43.6% on FrontierCode 1.1 Main, up from 34.4% for Gemini 3.6 Flash. Its DeepSWE v1.1 score climbed from 49% to 65.3%. The pattern echoes what happened when [DeepSeek’s smaller model outperformed its own flagship](https://thenewstack.io/deepseek-v4-flash-open-weights/) — leaner models are consistently punching above their weight class. The WebDev Arena score rose more modestly, from 1,538 to 1,588.

But benchmarks cannot show how reliably that will happen inside a company’s own environment. Google seems focused on helping agents work through a codebase without getting stuck. If Gemini 3.7 Flash can recover from a bad first attempt and reach the right result faster, it could save time and tokens even when another model looks cheaper on paper.

## Thinking levels control cost

Gemini 3.7 Flash offers three thinking\_level settings: low, medium and high, with medium used by default.

Low is intended for latency-sensitive work such as incident-response pipelines and real-time chat. Medium balances speed with the reasoning required for coding and agent workflows. High allows the model to spend more time reasoning and using tools when it encounters difficult coding, math, or planning problems.

A routing agent may work fine on low, while one trying to untangle a race condition may need high. The trade-off is cost: the longer Gemini spends thinking and calling tools, the more tokens it uses — what’s arguably more important is [total token consumption across the full agent loop](https://thenewstack.io/agentic-ai-token-costs/).

Gemini 3.7 Flash currently costs $0.75 per million input tokens and $3.75 per million output tokens. Google has applied that rate to Gemini 3.6 Flash as well until December 31. On January 1, 2027, both rates double to $1.50 per million input tokens and $7.50 per million output tokens. Google is not alone in using aggressive pricing to win developer adoption — [OpenAI recently slashed its own API costs amid rising global competition](https://thenewstack.io/gpt-5-6-api-price-cuts/).

The discount gives teams a few months to test Gemini 3.7 Flash at scale, but once the price increases, agents that carry large amounts of context or spend more time reasoning could cost twice as much to run. [The blank-check AI coding era is dead](https://thenewstack.io/microsoft-copilot-token-budgets/), so teams building around today’s price need to plan for that increase at the first of the year.

> The blank-check AI coding era is dead, so teams building around today’s price need to plan for that increase at the first of the year.

## Migration requires real work

Teams coming from Gemini 3.5 Flash, Gemini 3 Flash Preview or Gemini 3.1 Pro have a little more work ahead of them. [Google’s migration guide](https://ai.google.dev/gemini-api/docs/latest-model) says they’ll need to remove temperature, top\_p and top\_k, replace the numeric thinking\_budget with the thinking\_level setting and drop candidate\_count.

Developers must also remove prefilled model turns. Google recommends standardizing multi-turn interactions around the server-side previous\_interaction\_id. Applications that use the generateContent API should ensure that every FunctionResponse includes the corresponding call ID and function name.

The changes are manageable, but engineers should still do tests before trusting its work in production. [Code that passes every test can still break the next AI agent that touches it](https://thenewstack.io/go-language-ai-agents/) — a reminder that test coverage and agent reliability are not the same thing.

## Automation gains remain early

The improvements go beyond coding. Gemini 3.7 Flash scored 34% on GDP.pdf, up from 22%, while its AutomationBench score rose from 17% to 30.4%. Both are meaningful gains, although neither suggests the model can be left to work unchecked.

Teams that have only just moved to Gemini 3.6 Flash do not need to start over. Google has not announced plans to shut it down, giving developers time to decide whether another migration is worth it.

Meanwhile, Gemini 3.5 Pro is still missing. Google promised it for June, later said it was coming “soon” and has since started training Gemini 4. It is a [familiar problem across frontier labs](https://thenewstack.io/opus-5-agentic-coding-cost/): The model developers are waiting for does not always arrive when they need it.

> The model developers are waiting for does not always arrive when they need it.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)