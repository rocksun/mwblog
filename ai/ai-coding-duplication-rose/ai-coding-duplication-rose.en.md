**Since they arrived on the scene**, a great swathe of the software industry has pinned its hopes on AI tools, whether that’s early chat interfaces or modern agentic swarms. But the tone has shifted over the past few weeks, with HR software provider Rippling adding an anti-tokenmaxxing [AI spend console](https://www.rippling.com/blog/introducing-ai-spend-console) to give CFOs and CTOs visibility into spend, and IBM Vice Chairman Gary Cohn saying [last week](https://finance.yahoo.com/sectors/technology/articles/companies-struggle-measure-ais-roi-171020855.html) that the ROI has “not been nearly as high as people might think.” As the northern hemisphere feels the Fall cooldown, it seems that Winter is coming for AI tool budgets.

As organizations balance the books, teams will start feeling pressure on their Claude Code and Cursor budgets. That means they may face harder usage limits where returns are unclear, or budgets that can’t sustain the usage levels.

For organizations that have figured out [how to measure AI impact](https://thenewstack.io/how-to-measure-ais-organizational-impact/), there’s a growing realization that generating code volume at pace doesn’t guarantee movement in the metrics that matter. If you count lines of code, the number of pull requests, or even the number of features delivered, you’ll see no clear relationship to value. Not every line of code or feature matters equally to the business or its customers. This distribution is galaxy-wide.

Even at the output level, many organizations haven’t worked out how to turn siloed gains into end-to-end improvements. Gains in coding speed transfer to new tasks introduced by AI or get absorbed by downstream changes. If you haven’t worked out the inherent properties of value streams before you bought AI, you’ll be getting painful lessons when you try to track your ROI.

If the only problem were translating the cost of AI tools into end-to-end value, it would be serious enough. But something far worse is happening.

## Productivity in terms of output

Let’s look at the data, which GitClear collected and analyzed for the [Maintainability Gap report](https://www.gitclear.com/the_ai_code_quality_maintainability_gap). The report, published in June, covers 623 million analyzed changes from 2023 to 2026. This is a substantial dataset, with millions of change operations included across three and a half years. As teams rapidly adopt AI developer environments and tools such as [Cursor and Claude Code](https://thenewstack.io/ai-coding-tool-stack/), GitClear’s code-change-operation database allows them to detect and classify code duplication, hotspots, and signals of good or poor code factoring.

Heavy AI users gained 25% on their own prior velocity, far from the claims of 10x increases. The same report shows those heavy users out-producing non-AI users by 4 to 10x, which sounds like the opposite finding until you look at who they are. Teams that outperformed their peers in output were doing so before AI tooling arrived. And remember, there’s no guarantee this output will accrue to the value stream, or provide meaningful value to the organization or its customers.

The first part of the ROI calculation is to determine whether these increases are worth the cost. For many organizations, I would be surprised if they were.

Perhaps because much of the discussion of AI tools has focused on speed, other factors have received little attention. The software industry may have found a different kind of value if it had focused on the tools as a forklift truck, rather than a racing car, because the straight-line speed doesn’t seem so impressive. Yet they can perform heavy lifts that are tricky for us mere humans, like large-scale changes across a codebase, such as replacing an unmaintained library with a replacement.

For those who pass this first gate, we can look at the next factor.

## Productivity in terms of code quality

The shift to AI has brought about a giant behavioral change in the software industry. For several decades, the importance of code maintainability has been emphasized repeatedly. More than half the programming books on my shelf focus on architecture, code design, coupling, and cleanliness. The idea of refactoring, supported by automated tests, appears across many of these books.

Yet the signals GitClear is getting from the data are a complete reversal: a return to the code-and-fix era of software development. Across the dataset, block duplication rose 81% over 2023, from 40.3 to 73.0 per million changed lines. Those multiple expressions of the same concept drift apart and create whack-a-mole bugs. Moved code, the signature of refactoring, fell from 21% of changed lines in 2022 to 3.8% in 2026, which means code is becoming harder to understand, and that will hit maintainers with or without AI.

![](https://cdn.thenewstack.io/media/2026/09/da120fb8-image-1.png)

Chart showing a dramatic drop over four years in refactoring changes and a steep rise in duplication over the same time period.  
  
Source: [GitClear](https://www.gitclear.com/the_ai_code_quality_maintainability_gap)

When you make these changes, you get away with it initially because you’re early in the maintenance cost curve. Over time, however, the rising costs will become unbearable. Rework rates will rise, stealing time from new feature development. Seemingly minor issues will take far too long to pinpoint and resolve, with many simply becoming part of how it works because the fix is economically unviable. The accumulation of tightly coupled, incomprehensible code units will reach the point where the software stops being valuable.

We’ve been trying to validate the claims of 10x boosts with AI coding assistants. The data shows the opposite. Before AI, developers chose refactoring over copy-and-paste about two to one. Now they’re roughly five times likelier to copy and paste.

## Technical practices are the mission, not a side quest

When I’ve presented at conferences and user groups on what great software delivery looks like, I mention, among other things, test automation and refactoring. In the Q&A that follows, this question will inevitably come up in one form or another: “How do I get permission from my boss to do these things?”

Developers are whipped hard for fast progress, so they are trained to avoid what they see as *the side quest*. If they need to increase output, they streamline coding tasks, leaving no time to write tests or improve the code’s design, which would delay the feature. Inevitably, this makes all feature development vastly slower over time.

The premise of lightweight software delivery processes is that they rely on technical practices that control the cost of maintaining software over time. The wisdom is that working more deliberately today lets us maintain the pace of change indefinitely. If we skip these practices, change becomes increasingly slow and expensive.

![](https://cdn.thenewstack.io/media/2026/09/da120fb8-image.png)

Chart showing a traditional software project with costs rising superlinearly over time and an XP project with cost growth subdued.”  
Based on figures in Extreme Programming Explained (Beck, 1999)

Those technical practices, like test automation and refactoring, aren’t side quests; they are the work. Technical discipline is a fundamental requirement of commercial software delivery, and these practices stopped being optional some time ago.

When asked for techniques to convince managers to allow these practices, I’m confused. I’ve never asked for permission to do what is right for me, the software, its users, and the organization. No compromise can be reached, because omitting technical practices harms everyone involved.

This “side quest” thinking was unresolved in many organizations, and adding AI into the mix has made things far worse. When teams are given AI tools, they come with the expectation of a big return. When teams are, in reality, seeing a 25% increase in their rate of change against an industry misperception of some 10x boost, they will feel even more pressure to deliver.

Under these dysfunctional circumstances, it’s no wonder those who treat good practice as a side quest are skipping crucial steps.

## Real high performance is well known

High-performing teams have worked out that a set of software delivery practices is no longer optional. They worked it out because they were scaling long before the new tools arrived.

For software that matters, that people depend on, and that still needs to exist in a year, in five years, and beyond, we’ve moved from the pick-and-mix of the past, and there’s a new bar for professional software delivery.

There is a glimmer of hope here. The teams doing well with AI are the same teams that outpaced the industry before AI. They maintain rigorous technical disciplines, monitor code health indicators, and prioritize the craft of keeping code maintainable for the long haul.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/10/e54f7c3f-cropped-fc6cbbe0-steve-fenton-600x600.jpg)

Steve Fenton is an Octonaut at Octopus Deploy, a DORA community guide and a eight-time Microsoft MVP with more than two decades of experience in software delivery. He has written books on TypeScript (Apress, InfoQ), Octopus Deploy, and web operations....

Read more from Steve Fenton](https://thenewstack.io/author/steve-fenton/)