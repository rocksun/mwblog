Anthropic has extended its enhanced access to Claude Fable 5 for all paid subscribers through July 19, marking the third extension in five weeks. The company announced the move Sunday evening, just hours before the previous deadline expired.

The decision comes amid growing speculation about Anthropic’s next major model release after an unreleased model dubbed “Claude Honeycomb EAP” briefly appeared inside Cursor earlier this week, fueling community theories that Opus 5 could arrive before the end of the month.

## Fable 5 free access extended

Subscribers on Pro, Max, Team, and qualifying Enterprise plans can continue using Fable 5 for up to 50% of their weekly usage allowance at no additional cost through July 19 at 11:59:59 p.m. Pacific. Anthropic also extended the temporary 50% increase to Claude Code’s weekly rate limits through the same date.

Once the promotion ends, Fable 5 usage will be billed at $10 per million input tokens and $50 per million output tokens, matching Anthropic’s priciest tier.

## Users demand usage resets

As Anthropic extends the promotional period once again without resetting users’ Fable 5 allowances, users are growing frustrated. In Reddit threads, subscribers say another week of availability offers little benefit if they’ve already exhausted their included usage.

Many contrasted Anthropic’s approach with OpenAI’s, which has occasionally reset usage caps following service disruptions or unexpected demand, arguing that a reset would give them a better opportunity to test the model during each extension. Some users said the lack of a reset is pushing them to try competing models instead.

## Still no permanent return

After the U.S. Commerce Department lifted the restrictions on June 30, Anthropic restored access to Fable 5 on July 1, extending the free period through July 7 while introducing a 50% weekly usage cap. Hours before that deadline expired, the company pushed the offer to July 12. Then, on Sunday night, it did it again, extending free access through July 19.

The repeated extensions have become a story of their own. Anthropic launched Claude Fable 5 on June 9, initially offering free access through June 22. That plan was disrupted just three days later when an export-control directive forced Anthropic to disable both Fable 5 and Mythos 5 worldwide on June 12.

Claude Code lead engineer Thariq has said Anthropic intends to bring Fable 5 back as a standard subscription benefit once the company has enough compute capacity. However, Anthropic has not provided a timeline, and after five weeks of rolling extensions, the model still falls back to prepaid usage credits once the temporary offer expires.

## Honeycomb EAP briefly surfaces

There are also signs Anthropic may have another model waiting in the wings. On July 8, developer @chetaslua spotted a previously unknown model called Claude Honeycomb EAP inside Cursor’s model picker.

The listing disappeared within hours, but screenshots shared by the developer spread across X, Hacker News, and developer forums.

The images appeared to show Honeycomb routing certain sensitive prompts to Claude Opus 4.8 rather than handling them directly. Anthropic has neither confirmed nor denied the leak, and the model does not appear in the company’s public API or documentation.

The early access model was described as an Anthropic research model with per-turn controls, safety fallbacks, a one-million-token context window, and an “extra high effort” reasoning mode. Only two prompts were reportedly run before it was removed.

What caught developers’ attention was its safety behavior. According to the leaked listing, sensitive prompts were routed to Claude Opus 4.8 rather than handled directly. Anthropic has already documented a similar fallback mechanism for Fable 5, in which certain cybersecurity requests are automatically routed to Opus 4.8. If Honeycomb routes down to Opus 4.8, many developers believe it suggests the unreleased model sits above it in capability.

## Honeycomb’s competitive stakes are high

That theory gained traction because Honeycomb’s leaked specifications closely mirror the published Fable 5 architecture, including adaptive thinking, a one-million-token context window, and Opus 4.8 safety fallbacks. Several developers now speculate Honeycomb EAP is an early preview of Claude Opus 5, with a possible launch before the end of July.

While Fable 5 still holds the strongest published results on repository-scale coding benchmarks such as SWE-bench Pro, rivals including OpenAI’s GPT-5.6 Sol and xAI’s Grok 4.5 are now targeting the same high-end developer market at a fraction of the price.

That puts pressure on Anthropic. If Honeycomb ultimately becomes Claude Opus 5, it will need to deliver a meaningful performance advantage — or a more competitive pricing strategy — to justify Fable 5’s premium cost.

> Honeycomb will need to deliver a meaningful performance advantage — or a more competitive pricing strategy — to justify Fable 5’s premium cost.

When the current promotion expires on July 19, Fable 5 usage will switch to Anthropic’s prepaid credit system. At $10 per million input tokens and $50 per million output tokens, it’s the company’s most expensive generally available model. By comparison, Claude Opus 4.8 costs $25 per million output tokens.

There are ways to lower those costs. Prompt caching reduces the price of cached input tokens by 90%, while Anthropic’s Batch API cuts both input and output pricing in half for jobs that don’t need immediate responses. For scheduled or offline workloads, that effectively brings Fable 5’s pricing in line with Opus 4.8.

The highest costs show up in long-running agentic workflows. Fable 5 was built for tasks such as extended coding sessions, large-scale document analysis, and multi-step research, with a one-million-token context window and up to [128,000 output tokens](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5#:~:text=up%20to%20128k%20output%20tokens%20per%20request.). Those workloads can generate large volumes of output, causing costs to add up much faster than with shorter chatbot-style conversations.

For users who don’t need those capabilities, Claude Sonnet 5 is a far less expensive alternative. Anthropic’s current default model costs $2 per million input tokens and $10 per million output tokens through Aug. 31, 2026, before increasing to $3 and $15, respectively. While it lacks Fable 5’s one-million-token context window and maximum output size, it delivers strong performance for most daily coding and reasoning tasks.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)