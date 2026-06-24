As AI models now take over the core processes of writing code, the conversation has shifted to how effectively [we can use AI itself to review](https://thenewstack.io/future-of-code-reviews/) the codebases currently being created. If the consensus here suggests we should move the human checkpoint upstream, the question of just exactly where human developers should be working now comes to the fore.

It’s a pain point that surfaces in teams where a mandatory peer review now risks serving mostly as a rubber stamp. A pull request sits in a peer review channel for a couple of days before another developer, who arguably has very little context for what the software engineer did in the first place, finally becomes available… only to say, “Let’s gamble. Try merging.”

> “We must realize that it’s time to clean up ‘human slop’ i.e. a class of error that humans make far more often than AI does. For these types of mistakes, an AI reviewer is much more reliable than a tired human.”   
> —Avital Tamir, groundcover.

## The pros outweigh the cons, I guess

In most developer shops, this scenario still plays out; perhaps because there’s some level of infinite optimism that says the pros outweigh the cons, perhaps also because it creates a sense of standardization and order in the software team.

It’s a question that’s been nagging [Avital Tamir](https://www.linkedin.com/in/avital-tamir-5356a1407/) for some time in his capacity as a software engineer at [groundcover](https://www.groundcover.com/about), a cloud-native observability platform company.

Calling for a change in the way software teams handle the code review process at large, Tamir tells *The New Stack* that he’s not suggesting we turn over to all-out cowboy-coding chaos – he’s simply making the case that the way we’ve been doing code reviews for the past two decades needs to change with the times.

“There’s a lot of discourse about AI slop like hallucinations, misunderstood context and confident wrongness, and those are real concerns,” Tamir says. “But we must also realize that it’s time to clean up ‘human slop,’ i.e., a class of error that humans make far more often than AI does. For these types of mistakes, an AI reviewer is much more reliable than a tired human.”

## A working example of human sloppiness

The kind of human slop Tamir describes may be a familiar scene for many developers. Once a feature is complete, the programmer opens a pull request. Then it sits, marinating for a while. The developer pings their colleagues on Slack. Nothing happens on the first day, but after 48 hours, someone comments with a nitty-gritty niggle about variable naming or a question already answered in the code.

The developer fixes these nuisance factors, primarily because arguing takes longer than just fixing an inconsequential element of the code structure. After that, finally, an [LGTM](https://miro.medium.com/v2/resize:fit:1200/1*Kdlt69ZHH3rctVRIhkH_wA.png) (“looks good to me”) arrives.

“What did that accomplish?” asks Tamir. “A feature that could have shipped Tuesday ships Friday. Your competitor ships on Tuesday, finds the real bug on Wednesday, and fixes it on Thursday. Meanwhile, you’ve spent two days in review limbo, optimizing for plausible deniability instead of iteration speed.”

He asks us to consider what that review time is actually catching.

“The bugs that really hurt, like race conditions, data edge cases, or failure modes under load, are rarely spotted by someone reading code in isolation without full system context,” Tamir clarifies. “The feedback that does come through tends to be stylistic such as: ‘[use early returns](https://dev.to/eddiegoldman/early-return-vs-classic-if-else-a-universal-pattern-for-writing-cleaner-code-1083)’, ‘extract a function’ and so on… things that good static analysis should have caught automatically.”

If we multiply this process across dozens of engineers, multiple pull reviews per week, and multi-reviewer policies, it’s not unreasonable to argue that the compounding cost becomes substantial, ultimately manifesting as lost shipped features and learning cycles.

> “Self-review isn’t no review. It is a process designed to place review responsibilities more directly in the hands of the software engineer with the most context, and that’s typically going to be the original author, obviously. Using an AI-augmented review process.”

## The case for rigorous self-review

Tools such as [CodeRabbit](https://thenewstack.io/coderabbits-ai-code-reviews-now-live-free-in-vs-code-cursor/) allow developers to codify a team’s stylistic conventions as rules (“use early returns,” “prefer composition over inheritance,” “keep functions under 50 lines”) and apply them consistently to every pull request. Also in this space, we find [Claude Code Review](https://thenewstack.io/anthropic-launches-a-multi-agent-code-review-tool-for-claude-code/), a new multi-agent tool designed to identify software bugs before a human reviewer even sets eyes on the code; [Qodo](https://thenewstack.io/qodo-now-lets-developers-create-their-own-coding-agents/) with its agentic software code development and review functions; and [Greptile](https://www.greptile.com/?utm_source=google&utm_medium=cpc&utm_campaign=greptile-branded&utm_term=greptile&utm_content=182547601187&gad_source=1&gad_campaignid=22546549656&gbraid=0AAAAA-YPtJkqOxXuHkrNXuODgtythYvQa&gclid=CjwKCAjw6MPRBhBTEiwAd-7Mr0RHhg3a914UNnIplt8_NYOIJa4SmYJ94ZTxs4NWOsJ1UoU8sprx-xoCl7oQAvD_BwE) for AI code review services, among others.

“With these types of resources at our disposal, I ask again: if AI is writing and reviewing the code, and a human with full context of the requirements has already verified the behavior, what gap does the asynchronous human approver fill when we should be championing rigorous self-review?” argues Tamir.

> “The uncomfortable truth is that a lot of code review is just theater. It creates the appearance of rigor without reliably delivering it.”

But, he cautions, self-review isn’t no review. It is a process designed to place review responsibilities more directly in the hands of the software engineer with the most context, and that’s typically going to be the original author, obviously. Using an AI-augmented review process, Tamir describes his typical flow as follows:

* Work closely with the AI through every edit to read each change, steer it when needed, and understand what shifted and why.
* Run a full test suite on the code, and verify that “coverage” (i.e., all lines of code that exist do in fact execute in the test) is meaningful, not just present.
* Manually verify the behavior end-to-end before opening a pull request for the code written thus far.
* Open the pull request and let the AI review tool run. Loop its comments back to the coding AI, decide which to act on and which to dismiss, and iterate.
* Merge, then monitor. Check error rates and metrics. Own the outcome.

“That process is more rigorous than waiting 48 hours for an LGTM,”  Tamir says. “Plus, it puts accountability exactly with the person who understands the problem. The uncomfortable truth is that much code review is just theater. It creates the appearance of rigor without reliably delivering it.”

## It’s a question of trust

Given the presence of these kinds of AI-code review tools today and the propositions being made here, we may ultimately get down to questioning the fabric of software engineering team structure and the management approach that oversees it.

This brings trust into the picture. Tamir suggests that if leadership doesn’t trust software engineers to review their own work responsibly, “that’s a hiring problem, not a process problem” in real terms.

“Trust in high-performing teams is built through outcomes: shipping features that work, owning failures and fixing them fast, proactively sharing knowledge, and including colleagues in decisions. Those behaviors create a track record that a peer review approval queue does not,” he concludes.

Teams considering embracing some or all of these techniques may want to start with a low-risk internal software tool, or perhaps a greenfield service or a non-customer-facing system. In concert with this approach (and while the team measures its success, deployment frequency, rollback rate, etc.), they can reserve synchronous human collaboration for higher-stakes decisions.

This way, team collaboration might really start to matter and make a difference, and we could shift from LGTM to looks really good to me.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)