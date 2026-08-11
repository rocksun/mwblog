**In the early days of Claude Code**, it felt like you either had to approve everything the coding agent did — which was incredibly annoying — or give it free rein, which was incredibly dangerous.

Earlier this year, Anthropic introduced [auto mode](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode), which uses a separate classifier model to allow Claude to decide when something is so dangerous that human intervention is needed.

Starting August 14, that will [become the new default](https://claude.com/blog/auto-mode-default-in-claude-code) for Pro, Max, and Team users (it remains opt-in for Enterprise users and on the Claude API and cloud platforms for now, with a default rollout there planned within the next month), because, as it turns out, humans don’t do so well when constantly prompted for permissions.

## The 97% problem

Indeed, as Anthropic’s own research shows, they currently approve 97% of permission prompts.

“While most prompts are likely for safe, routine commands, an approval rate that high suggests many users are clicking through reflexively rather than reviewing each command,” Anthropic notes.

![](https://cdn.thenewstack.io/media/2026/08/54ffa374-hpi2quja8aaun3e-1024x631.jpeg)

*Credit: Anthropic*

Working with more than 1,000 testers, the team also found that humans only caught 13.6% of dangerous commands, while Claude Code in auto mode caught 89%.

The longer the sessions continued, the worse the human testers performed. After 50 prompts, the testers only found 5% of dangerous commands (though it’s unclear if Anthropic provided them with coffee during those long sessions).

> As it turns out, humans don’t do so well when constantly prompted for permissions: After 50 prompts, the testers only found 5% of dangerous commands.

Anthropic argues that seeing fewer permission prompts means users will spend more time actually reading and evaluating the ones that do come through.

In practice, when the classifier flags a command, auto mode blocks it instead of asking for permission. Claude will then typically look for a safer way to accomplish the same task, or come back to the user for explicit approval.

There’s a fallback, too: After three consecutive blocks, or twenty in a single session, auto mode hands control back to the user and reverts to manual approvals.

As Anthropic also [notes](https://x.com/ClaudeDevs/status/2085794863786958988), with agents now often working for much longer periods, auto mode makes it far easier to run these multi-hour tasks without having to spend hours doing nothing but [botsitting](https://www.businessinsider.com/botsitting-ai-hidden-human-labor-at-work-2026-6).

## Auto mode on hard

Ahead of this launch, Anthropic also spent time hardening auto mode.

The most consequential of these changes are the hard denies. Anthropic says the classifier is designed to never approve data exfiltration, like sending code or secrets to an external destination. To run an action like that, a developer would have to switch out of auto mode or run the command themselves.

Organizations can also add their own hard deny rules for actions they never want allowed, even when a user asks for them.

> The classifier now also carries explicit rules for how secrets and confidential data can be accessed and shared.

The classifier now also carries explicit rules for how secrets and confidential data can be accessed and shared, and it checks whether the destination of a git push or pull request is public, private, or trusted before the action runs. The same push, after all, can be routine or an exfiltration depending on where it lands.

In addition, the classifier now sees a repository’s git status before destructive commands like git reset –hard, so auto mode knows what uncommitted work is about to be discarded, and an API-side probe screens content Claude pulls from web pages, files, and tool outputs for prompt injection attempts, adding a warning to Claude’s context when something looks off.

To pressure-test this work, Anthropic ran a two-week red-teaming pilot with Apollo Research, which injected synthetic attacks into real workflows. Before the hardening, the classifier missed 12% of these attacks; afterward, that number dropped to 7% on a held-out test set.

## Auto mode vs. prompt injections

Anthropic is also taking this chance to compare itself with its biggest competitor, OpenAI. Of course, the company wouldn’t do this if the results weren’t good, but Anthropic did commission a third party to test how well auto mode fared in preventing prompt injection attacks.

Trajectory Labs found that with Anthropic’s models in auto mode, not a single one of the 720 attacks it tried got through (and even with permissions fully bypassed, Claude Sonnet, Fable, and Opus 5 only let through 0.09% of attacks).

OpenAI’s GPT-5.6 Sol in Codex let 19% of all attacks through in full access mode and just under 6% in its auto-review mode.

![](https://cdn.thenewstack.io/media/2026/08/4674a74b-6a75fafde538ce42b19d5742_image3-2-1024x666.png)

Credit: Anthropic.

Still, Anthropic itself notes that auto mode is a classifier, not a guarantee — it reduces risk, it doesn’t eliminate it. For high-stakes changes to production infrastructure, the company still recommends keeping a human in the loop.

## Bonus: Claude Code sessions can now DM each other

In addition to this permissions update, Anthropic also on Friday announced that if you run parallel Claude Code sessions, they can now talk to each other. That’s especially useful if you have multiple sessions that are working on related problems and they need to tell each other about changes to the code they are working on.

“Instead of having to re-explain yourself in another session, you can now tell Claude to do it. It sends a summary (not your history or files), and the other session picks it up mid-task,” Anthropic [explains](https://x.com/ClaudeDevs/status/2085817074816070014) on X.


[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)