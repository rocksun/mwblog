In 2020, Shopify made a bet that resonated across the developer world by writing mobile code once in React Native instead of duplicating every feature in Swift and Kotlin.

On Thursday, the company [said it’s going back](https://shopify.engineering/back-to-native).

You read that correctly; the company is ditching cross-platform mobile apps for full native development, and it’s leaning heavily on AI agents to do the heavy lifting. Its consumer app, Shop, took just 12 weeks to go from proof of concept to a fully native production release. Next up is the far more grueling merchant app, a 300-plus screen beast that relies heavily on deep iOS platform integration.

What’s interesting is that Shopify doesn’t consider its React Native bet a mistake, because the framework did exactly what the company needed it to do for many years. Not to mention, there was no obvious sign Shopify was preparing to walk away from any of this either; as recently as [January 2025](https://shopify.engineering/five-years-of-react-native-at-shopify), the company was still talking publicly about its future with React Native.

## Agents replaced cross-platform tradeoffs

But the coding agents got a lot better and by late 2025, Shopify found that an agent could look at how a feature worked on iOS and build the Android version, or do the same thing in reverse. Engineers could also work on platforms they didn’t know particularly well because the agent could handle more of the platform-specific work.

“LLMs changed one of the core assumptions behind our 2020 decision,” wrote Mustafa Ali, Shopify’s director of engineering.

> “LLMs changed one of the core assumptions behind our 2020 decision,”

## The Rewrite Economics Keep Changing

Shopify isn’t the only company throwing agents at this kind of problem. Bun creator and current Anthropic technical team member, [Jarred Sumner](https://www.linkedin.com/in/jarred-sumner-a8772425/) used 64 parallel Claude Fable 5 instances to [port the JavaScript runtime from Zig to Rust](https://bun.sh/blog/rewriting-bun-in-rust) — roughly a million lines of code in 11 days, at an estimated API cost of $165,000. Sumner reported the existing test suite passed across all six supported platforms before the merge.

A year ago, that would have taken a small team multiple quarters but today it’s an 11-day sprint supervised by one person.

> A year ago, that would have taken a small team multiple quarters but today it’s an 11-day sprint supervised by one person.

Keep in mind, those productivity gains aren’t evenly distributed. As *The New Stack* [recently reported](https://thenewstack.io/openai-agent-research-bottleneck/), AI agents can create more work elsewhere in an engineering organization even as they make some development tasks much faster. But they are also changing the amount of work involved in decisions that used to be difficult and expensive to undo.

In May, developer [Simon Willison](https://www.linkedin.com/in/simonwillison/) [wrote](https://simonwillison.net/2026/May/14/not-so-locked-in/) about meeting an engineer whose company had used coding agents to combine its old iPhone and Android apps into a single React Native app. Willison asked why they would bother consolidating when agents were making separate codebases easier to maintain, but the engineer wasn’t worried about getting locked in. React Native did what the company needed, and if that changed later, they could always move back to native. Shopify is now doing the exact same thing, but with a much bigger app and a lot more on the line.

## Zero-shot prompting produced junk

Shopify first tried giving an LLM the existing React Native code and asking it to rewrite it natively. The results weren’t good. Ali describes the output as slop, but adding more steps didn’t solve the problem.

Even when the team had the model write specs and task files before touching the code, it still produced too much code that engineers wouldn’t want to maintain.

## Helix breaks migrations into pieces

Enter Helix, Shopify’s internal system for managing the agents doing the rewrite. It takes the migration screen by screen, breaking each one into smaller chunks rather than trying to recreate everything at once. Shopify compares the result with the existing app as it goes, while separate agents look for problems in the code before a human signs off. The system also keeps that review feedback around, so problems caught earlier can inform what happens next.

It’s also hard not to connect that approach to what happened [when Shopify’s CEO publicly threatened to ban Claude Code](https://thenewstack.io/shopify-claude-code-agentsmd/) over engineers shipping agent-generated code without enough review. Helix takes a similarly cautious approach by assuming the agent’s output needs to prove itself before anyone relies on it.

## Codebases built for agents

The migration exposed another problem. Agents can change code in seconds, but testing it in a mobile simulator can take twice as long.

Shopify worked around that by separating business logic from the UI and letting agents interact with the app through a CLI running on a desktop. Some checks that once took minutes now happen in milliseconds, while the same interface can control a simulator when needed.

[Most codebases weren’t built with AI agents in mind](https://thenewstack.io/go-language-ai-agents/). Shopify is starting to build around them, and says it will judge the native apps partly by how much work agents can eventually handle on their own.

> Some checks that once took minutes now happen in milliseconds, while the same interface can control a simulator when needed.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)