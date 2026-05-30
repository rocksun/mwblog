**Last week at Google I/O**, the company announced the beginning of the end for Gemini CLI — that is, for everyone save enterprise users and those with API keys. Starting June 18, many users will lose access to Gemini CLI, Gemini Code Assist IDE extensions, and Gemini Code Assist for GitHub.

Instead, developers can shift to Antigravity CLI, a closed-source platform that lacks features and is already frustrating some developers with usage limits.

## But why?

In its [announcement blog post](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/), Google says Antigravity CLI comes in response to the community’s shifting needs: “Listening to your feedback made one thing clear: we can serve you best by pouring our energy into a single product built for today’s multi-agent reality.”

That product, Antigravity CLI, is a “premier agent-first development platform” that includes a server-side harness and a new terminal experience. Google says Antigravity will still enable users to get quick answers, scaffold and build new projects, and provision cloud infrastructure, but it’ll be snappier. Plus, Antigravity can orchestrate multiple agents in the background for complex tasks and make sure improvements to the core agent are universally applied, thanks to a new unified architecture.

But going by the first waves of feedback from Gemini CLI users, it appears many think they’re getting the short end of the stick.

## It has fewer features, at least for now

“There won’t be 1:1 feature parity right out of the gate,” says Google. What it doesn’t say is when, or if, that parity will ever come.

> “There won’t be 1:1 feature parity right out of the gate.”

In the meantime, developers can use what Google dubs Gemini’s “most critical features” via Antigravity plugins: Agent Skills, Hooks, Subagents, and Extensions.

## It’s not open source

Unlike Gemini, Antigravity isn’t open source. While the [Gemini GitHub page](https://github.com/google-gemini/gemini-cli) is dense with code and a list of hundreds of contributors, [Antigravity’s](https://github.com/google-antigravity/antigravity-cli) is bare in comparison.

Developers do not seem enthused. As one [Redditor](https://www.reddit.com/r/GeminiCLI/comments/1thweon/comment/omq0tt5/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) notes: “I don’t see any indication that Antigravity cli will be open source, I had all kinds of custom layers on top of gemini cli that I will be sad to lose. And I am quite anxious about usage limits.”

## It may be effectively more expensive

Other developers aren’t merely anxious about usage limits; they’re already running into issues. The [GeminiCLI Reddit thread](https://www.reddit.com/r/GeminiCLI/) is full of frustrated comments from Antigravity users saying the new platform makes them hit usage limits faster, which may effectively render the new platform more expensive than was Gemini.

“I can tell you quota is VERY LOW with Antigravity CLI, just tried do design a couple of screens in kotlin, and run out of tokens,” says one Redditor. Another adds, “even with pro I got the usage limit in just 6 to 7 prompts, this is insane, earlier I used to make whole projects with gemini cli with only 13% quota reached.”

Still more chime in with reports of their own debacles, one questioning whether Antigravity was even ready for a rollout, “Something’s wrong with the limits; they’re catastrophically low even with a subscription. The documentation is very poor. They shouldn’t have released it in this state.”

The trouble with usage limits seems to be the common story, and it may end up pushing some users to jump ship. “if they don’t refresh every day I will cancel my google sub and use codex or claude code. The pro tier is a joke if Cli quota is gone,” writes another Redditor.

“Just switched to antigravity cli but going back to gemini cli while I can, my tokens went crazy fast,” says one more.

But the window to switch back is closing fast.

## Everyone’s out of luck, except enterprise users and those with API keys

On June 18, Google AI Pro, Ultra, and free users will lose access to Gemini CLI, Gemini Code Assist IDE extensions, and Gemini Code Assist for GitHub — but enterprise users and those with API keys are safe.

For users with paid Gemini and Gemini Enterprise Agent Platform API keys, Gemini CLI will still be accessible. Similarly, for those using Gemini CLI or IDE extensions via a Gemini Code Assist Standard or Enterprise license and for those using Gemini Code Assist for GitHub via Google Cloud, access will be unchanged.

## Is this the way things are now?

“[N]ot a long time ago I was eager for some AI-related news, cause I expected some new breakthroughs. Now every announcement is [basically] ‘we’re making AI more expensive,’” laments a Redditor.

> “Now every announcement is [basically] ‘we’re making AI more expensive.'”

If they’re sour about so many fellow Redditors saying they’re hitting usage limits faster with Antigravity than they did with Gemini, this user may be similarly sullen about [Anthropic splitting billing and pushing Agent SDK into separate credit pools](https://thenewstack.io/anthropic-agent-sdk-credits/?utm_source=chatgpt.com) and [GitHub moving Copilot to usage-based billing](https://thenewstack.io/github-copilot-usage-billing/?utm_source=chatgpt.com), other moves in the growing trend of climbing AI costs.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)