Thanks to agentic coding tools like Claude Code, Codex, Cursor, and others, developers are shipping more code than ever. But this also means that more code needs to be reviewed. That’s become a major bottleneck for many teams. To help them, Anthropic on Monday [launched Code Review in Claude Code](https://claude.com/blog/code-review), a new multi-agent system that tries to catch bugs before a human reviewer even sees the code.

Available for Claude Teams and Enterprise users in the Claude Code web interface now, Code Review is a feature that admins can turn on per repository. From then on, it will run in the cloud whenever a pull request is opened for an enabled repository.

Anthropic already offered code review [with Claude Code in GitHub Actions](https://code.claude.com/docs/en/github-actions). But as the company notes, “It’s a more thorough (and more expensive) option than our existing code review GitHub Action, which remains open source and available.”

Cat Wu, the head of product for Claude Code at Anthropic, notes how important some degree of automation for code review has become. “As people adopt Claude Code, we’ve been noticing that people are writing a lot more PRs than they used to,” she says in an interview with *The New Stack*. “What that often means is now the burden is shifted onto the code reviewer because it only takes one engineer, one prompt, to put out a plausible-looking PR. And then the code reviewer needs to spend a bunch of time verifying all the edge cases.”

![](https://cdn.thenewstack.io/media/2026/03/c9ea4b46-screenshot-2026-03-09-at-10.22.36-am-scaled.png)

## A flock of code review agents working in parallel

In practice, Code Review will dispatch a team of agents who work in parallel, each looking for different types of errors. Once done, they’ll leave a comment with their conclusions and, if they find any issues, will also suggest a solution. The agents will not approve any pull requests, though. That’s still the human engineer’s call.

The focus for these agents is on logical errors, and that’s a deliberate choice. Wu tells *The New Stack* the reason is to cut down on false positives.

“A lot of times when a human code reviews, you get the logic errors, but you get a bunch of these styling errors,” she says. “We found that in AI-generated reviews, people really just want the logic errors to start with — and so that’s the core focus here. […] People are very sensitive to false positives, and so if we just focus on logic errors and we just focus on actual bugs in the code, then the false positive rate is low because anytime you know about a bug, you should almost definitely fix it.”

## How Anthropic uses Code Review

Anthropic has been using a similar system internally, and at this point, Wu says, Anthropic’s developers expect to see Code Review comments on their pull requests, “and get a little nervous” when they don’t see it.

Inside Anthropic, the company runs Code Review on almost every pull request now. Before using it, 16 percent of pull requests got substantive review comments, the company says. Now that number is 54 percent. On large pull requests with over 1,000 lines changed, the system will find bugs in 84 percent, with an average of 7.5 issues.

The number of false positives, at least for the agents running on Anthropic’s code base, remains low, with developers marking fewer than 1 percent as incorrect.

![](https://cdn.thenewstack.io/media/2026/03/1a614888-code-review-in-claude-code.gif)

## Slow and steady

Those agents do take their time, though. The average review takes around 20 minutes, Anthropic says, but the time scales with the complexity of the pull request. Simple ones will get what the company calls “a lightweight pass,” while more complex ones will engage more agents and get a deeper read.

As Wu noted, the agents often take the entire code base into account to ensure that a change in one file doesn’t create new bugs because a few files interact with each other in unexpected ways.

“The trade-off that we’ve made for our users is we want this to be extremely intelligent, extremely thorough, but the way to get there right now is to run for a bit longer than other code review tools,” she says. “But what you get is a more robust output. Also, each of the agents doesn’t just look at the code that you’ve changed. It can flexibly traverse the entire code base.”

Code reviews are billed by token usage, and given how deep those agents dig into the code, that can add up. Anthropic says a review generally costs between $15 and $25 on average. Admins can set monthly caps and get an analytics dashboard to track how many pull requests are being reviewed and accepted — and what it all costs.

## Local reviews?

Right now, this tool only runs when a pull request is created, but Wu notes that there “is a ton of demand to run this locally,” within the developer’s inner loop. “I think it is the strongest sign of PMF [product-market fit], because it means that people are actively seeking this out. It’s not like some automation that’s imposed on them. They see the value in it, and they want it to double-check their work,” she says.

Don’t be surprised if Anthropic lets developers run this locally soon as well.

## What about security bugs?

Only a few weeks ago, Anthropic also launched [Claude Code Security](https://www.anthropic.com/news/claude-code-security), which scans an entire codebase for security bugs. Where Code Review focuses on logical errors, Claude Code Security is entirely focused on providing a deep security sweep that runs continuously. If Code Review detects a security issue, it will flag it, “but it’s not as thorough as Claude Code Security,” Wu says.

## Availability

Code Review is now available for admins to turn on for Teams and Enterprise users. If there is demand, Anthropic may extend it to other user tiers as well, Wu says.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)