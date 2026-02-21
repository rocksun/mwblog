[OpenClaw](https://openclaw.ai/), [NanoClaw](https://nanoclaw.net/), and the various other personal AI agents that are all the hype right now can quickly burn through millions of AI tokens. What has made them affordable is that even the most basic plans at a flat rate of $20/month from Anthropic or OpenAI allow you to use their coding agents with relatively generous token limits, all without using a pay-as-you-go API key.

However, Anthropic recently [updated its Claude Code documentation](https://code.claude.com/docs/en/legal-and-compliance#authentication-and-credential-use) to note that using the OAuth token from those accounts in “any other product, tool, or service, would be against its terms of service.” This is, however, exactly how NanoClaw, for example, runs its onboarding flow.

The update also notes that developers who are building “products or services that interact with Claude’s capabilities” should use API keys. “Anthropic does not permit third-party developers to offer Claude.ai login or to route requests through Free, Pro, or Max plan credentials on behalf of their users,” the document now reads.

Understandably, this created quite a stir in the Claude community on [Reddit](https://www.reddit.com/r/ClaudeCode/comments/1r88vbs/claude_code_policy_clear_up_from_anthropic/), [X/Twitter](https://x.com/robzolkos/status/2024125323755884919) and other forums. The [Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview), which powers all of this, enables people to use not just these new personal agents but also various coding tools. Indeed, the Agent SDK is designed to let users build AI agents with Claude Code at its core.

And while it’s understandable that Anthropic doesn’t want developers to essentially hack the system and build services that depend entirely on the Pro and Max plans without paying for the API, this move seemed to discourage many personal use cases and much of the experimentation that is currently pushing the entire industry forward.

But fret not, Anthropic argues that all of this is simply a misunderstanding.

*The New Stack* asked Anthropic’s PR team for clarification and was pointed to a [post on X](https://x.com/trq212/status/2024212378402095389), where Thariq Shihipar, who works on Claude Code at Anthropic, writes the following: “Apologies, this was a docs clean up we rolled out that’s caused some confusion. Nothing is changing about how you can use the Agent SDK and MAX subscriptions!”

In addition, he later clarified that Anthropic wants to encourage experimentation, but “if you’re building a business on top of the Agent SDK, you should use an API key instead.”

When we asked the company for a bit more qualification (and whether users should worry that Anthropic will cancel their accounts if they use OpenClaw, for example, we received the following statement, which echoes Shihipar’s language: “Nothing changes around how customers have been using their account and Anthropic will not be canceling accounts. The update was a clarification of existing language in our docs to make it consistent across pages.”

![](https://cdn.thenewstack.io/media/2026/02/9592537d-screenshot-2026-02-18-at-1.48.13-pm.png)

It doesn’t help that Anthropic asked Peter Steinberger, the founder of Clawdbot, to change the his project’s name. Hence why “Claudebot” is now called OpenClaw. That was likely a legal necessity, but the process didn’t endear Anthropic to the community. Steinberger has now joined OpenAI. A few weeks ago, Anthropic also [banned developer tools like OpenCode](https://gist.github.com/R44VC0RP/bd391f6a23185c0fed6c6b5fb2bac50e) from using its OAuth system.

To many users, it has also long felt like these subscriptions, no matter the provider, were subsidized by those who use the more expensive API. It’s perhaps no surprise that many users expect we’ll soon come to the end of this “too-good-to-be-true” era of AI services, and that many saw this policy update as a sign of things to come.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)