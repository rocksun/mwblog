OpenAI launched [GPT-5.6](https://thenewstack.io/openai-gpt-56-live/) last week and folded Codex into a unified ChatGPT desktop app. Since then, the company has been running flat out.

Early Tuesday, [Tibo Sottiaux](https://www.linkedin.com/in/thibault-sottiaux-27195366/), engineering lead for Codex at OpenAI, mused on X that combined active users of Codex and ChatGPT Work might hit 8 million. The trajectory has been impressive, especially as the use of Anthropic Claude has grown so much in 2026. Codex had fewer than 1 million weekly active users in February but hit 5 million by early June. Then GPT-5.6 launched on July 9, and the numbers accelerated sharply — 6 million by July 12, 7 million roughly 24 hours later, and 8 million by Sunday.

That’s a growth curve most enterprise SaaS products never see in a lifetime, let alone in five months.

## What broke at launch

OpenAI [merged the standalone Codex app into the ChatGPT desktop app](https://thenewstack.io/openai-codex-work-atlas/), launched ChatGPT Work as a new agentic mode for knowledge workers, and began sunsetting the Atlas browser — all in a single day.

According to the company, demand surged almost immediately, with traffic roughly doubling OpenAI’s previous peak within 48 hours. The sudden influx exposed several scaling issues. In a [detailed thread](https://x.com/thsottiaux/status/2076495156757577895?) published on July 12, Sottiaux outlined the team’s response, which included optimizing inference to increase capacity by about 10% per subscriber, reducing the context window from 372,000 to 272,000 tokens after the larger limit created unintended billing issues, rolling back experimental reasoning-effort settings (internally known as “juice” values), and patching overly aggressive multi-agent behavior at the highest reasoning levels.

OpenAI also temporarily removed the five-hour usage cap for Plus, Business, and Pro subscribers — a move that amounts to the most generous access the product has offered since launch.

Community reactions were split between those who read the context window rollback as a stealth downgrade and those who credited Sottiaux for explaining the operational trade-offs publicly. [OpenAI CEO Sam Altman weighed in](https://x.com/sama/status/2076780425280954658) with what amounted to a positioning statement against competitors who, in his framing, treat users with contempt.

## Competitors respond to the surge

Within hours of OpenAI announcing its 7 million user milestone, Anthropic [extended its Claude Fable 5 promotional pricing through July 19](https://thenewstack.io/fable-5-honeycomb-opus/) and bumped Claude Code’s weekly usage limits by 50%. Whether one caused the other is unknowable, but the overlap gives us plenty to speculate about.

Since Thursday, GPT-5.6 Sol has risen to second on Arena’s agent leaderboard after 7,800 real-world agentic sessions, and many developers now see OpenAI as the leader in AI coding again.

## Cost per task matters

Developers judge systems by the cost of completing a task. Cognition, for example, [reported](https://x.com/cognition/status/2076714965344342382) that its Devin Fusion product, powered by Fable 5, can be cheaper per completed task than Anthropic’s pricier Opus 4.8 because better delegation reduces unnecessary work. In 81% of Fable-led runs, the lead model never edits code. The takeaway is that a more expensive model can still lower overall costs if it avoids wasted work.

> In 81% of Fable-led runs, the lead model never edits code.

## The harness is becoming the product

OpenAI’s decision to merge Codex, ChatGPT Work, and its built-in browser into a single desktop app reflects that shift. The same is true of its plugin architecture, which connects the app to Slack, Google Drive, SharePoint, CRMs, and calendars. OpenAI is turning it into a workspace that sits atop the tools people already use.

Anthropic has moved in a similar direction with Claude Cowork, which developed after the company saw users already using Claude Code for far more than software development.

## Usage caps remain the bottleneck

Right now, the problem remains the usage cap. Even with the five-hour limit lifted, Codex and ChatGPT Work are forced to share a single weekly pool. If you run a heavy Sol Ultra session with multi-agent orchestration, you’ll burn through that allowance incredibly fast. (Sottiaux is aware of the headache and says a fix is in the works).

In the broader race, OpenAI has the sheer gravity of 900 million weekly users and killer benchmark scores. Anthropic still holds a massive amount of developer goodwill thanks to premium code quality and enterprise-friendly pricing. And for the DIY crowd, open-source stacks running GLM 5.2 or Kimi K2.7 look better than ever if you want to trade a little speed for data control. Coding agents and knowledge work are multiplying fast, and we haven’t even hit the weekend yet.

> Coding agents for coding and knowledge work are multiplying fast, and we haven’t even hit the weekend yet.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)