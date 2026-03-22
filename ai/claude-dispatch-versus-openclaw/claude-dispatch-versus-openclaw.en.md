It is sometimes difficult to capture just how popular OpenClaw is around the world. Then there are reports like one in *Forbes* recently.

“On a Friday afternoon in March, nearly 1,000 people lined upoutside Tencent’s headquarters in Shenzhen to get a piece of software installed on their laptops,” an article in [*Forbes*](https://fortune.com/2026/03/14/openclaw-china-ai-agent-boom-open-source-lobster-craze-minimax-qwen/) reads, citing a Reuters report as its source.

Why would engineers from a $650 billion Chinese company deploy an open-source AI agent built by an Austrian onto random people’s laptops? But it seems many Chinese AI startups are all trying to “raise a lobster” with government encouragement.

I looked at [NanoClaw](https://thenewstack.io/nanoclaw-containerized-ai-agents/) two weeks ago, which is a much safer version of its bigger crustacean brother, but it was never going to be long before a company as quick-witted as Anthropic got into a craze originating from its own work.

The basic three foundations of OpenClaw we’ve now seen in multiple places: An LLM agent, with access to a local drive, controlled via mobile messaging. Like bankruptcy, the audience for this caught on gradually, then suddenly. The user can now do real work, with AI, via the software they are already totally familiar with. That is the offer that others are trying to measure up to.

I want to quickly mirror one of [Azeem Azhar](https://www.linkedin.com/in/azhar/)’s points — that while Apple has done nothing notable in the AI software space, their hardware is well-suited for running agentic (i.e., actual computing) tasks. Their family of Apple Silicon chips, replacing Intel chips, is well-suited for local on-device inference. This is why the Mac Mini, a computer that a whole generation has probably never heard of, is selling out in stores.

OpenClaws vital weakness (lack of secure boundaries and guardrails) is also its strength – you can try anything, and it might just work. Naturally, no company that could be sued would follow this inflammable route.

The first stab at the mobile communication piece from Anthropic was [Claude Remote Control](https://code.claude.com/docs/en/remote-control), which dropped last month. This worked with Claude Code and [Simon Willison](https://simonwillison.net/2026/Feb/25/claude-code-remote-control/) described it as “janky.”

## Enter Claude Dispatch for Cowork

But now there is [Claude Dispatch for Cowork](https://support.claude.com/en/articles/13947068-assign-tasks-to-claude-from-anywhere-in-cowork). You already get two pieces of the trifecta with Cowork — AI agents working with your local drive, without having to grok MCP.

If you have a Pro plan, you can try this research preview.

First, make sure your Claude Desktop is up to date. If you remember, you can start [Cowork](https://thenewstack.io/how-claude-cowork-helps-developers-spread-the-ai-knowledge/) from a tab within it.

Looking at my Desktop Apps File menu, I can immediately see I need an update

![](https://cdn.thenewstack.io/media/2026/03/4a243a62-image.png)

And after updating, when I restart Claude Desktop, I see this:

![](https://cdn.thenewstack.io/media/2026/03/2d5aa649-image-1-1024x430.png)

So by hitting Dispatch, we see the steps needed are quite straightforward:

![](https://cdn.thenewstack.io/media/2026/03/4524a5a8-image-2-845x1024.png)

The new piece is that we also need an app for the phone. Now, I wouldn’t say this is dropping the ball, yet this isn’t like using WhatsApp. We need to install a new app just to talk to Claude. However, it is of course far safer and likely the correct first move for Anthropic. I didn’t have the Claude app (because I absolutely didn’t need it), but I installed it on my Android to complete the chain.

The final setup tells us quite a bit about what is going on

![](https://cdn.thenewstack.io/media/2026/03/b5a74737-image-3-821x1024.png)

(I am not entirely sure of what “Claude in Chrome” is, but it appeared to be another beta plugin. You may have seen my article on [WebMCP](https://thenewstack.io/webmcp-chrome-ai-agents/) this week.)

Instead of starting a new session for each task, you have a single persistent thread with Claude Dispatch. This thread doesn’t reset – Claude retains context from previous tasks, so you can pick up where you left off – on laptop or phone. In fact, it is quite hard to restart even if you want to.

After logging in and fiddling with my phone, I saw the link to the Dispatch thread, and we were off.

I thought I’d try to find a passport scan — which is actually something suggested in the Claude Cowork hints. I started on my laptop to check things out first:

![](https://cdn.thenewstack.io/media/2026/03/a56d3982-image-4-1024x523.png)

I needed to talk to Google Drive. Although Claude didn’t know it could do this, fortunately, the web did – I just had to add a connector:

![](https://cdn.thenewstack.io/media/2026/03/1d3409fd-image-5-1024x493.png)

I realised it had access to the Drive on the web, not the actual folder, which was odd. However, I gave it access and carried on.

As expected, it worked like a walkie-talkie — with any requests typed on my phone getting “dispatched” onto the laptop:

![](https://cdn.thenewstack.io/media/2026/03/1d0fca00-image-6-1024x444.png)

Unfortunately, after multiple permission requests, it just gave up on the query and died.

I was going to keep trying, maybe by telling it about a specific folder, but I realised I wouldn’t know whether the problem was with Cowork or Dispatch, and I would be missing the point. I could clearly see that the remote control aspect was working fine. And yet I’m not sure whether this advances the case for putting down OpenClaw and waiting for Anthropic to pick up the slack.

## Raising a lobster

I’m wondering whether this approach — while a good start — will leave Anthropic too far behind OpenClaw. Even if this becomes less fiddly, a single continuous thread controlled by an app to give you a walkie-talkie is just more Anthropic-specific machinery. And users aren’t asking for a walkie-talkie to a session — they just want to find that passport scan.

It feels like a bit more work is needed to find the right framing that keeps things secure while remaining flexible enough to compress the distance between curiosity and adoption.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)