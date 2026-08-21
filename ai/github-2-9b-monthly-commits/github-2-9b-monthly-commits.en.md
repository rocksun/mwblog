Per month, GitHub now sees 2.9 billion commits, 130 million merged pull requests, and 24 million new repos. Back in April, GitHub already had a hard time handling ‘only’ 1.4 billion commits.

To a large degree, that’s thanks to how popular coding agents have become and how quickly software development is changing. But it’s also no secret that GitHub, despite [its efforts to move to a more modern architecture](https://thenewstack.io/github-will-prioritize-migrating-to-azure-over-feature-development/), simply hasn’t been able to scale fast enough to meet this demand.

> “We have made progress, but these incidents make clear that we must accelerate this work.” — GitHub CTO Vlad Fedorov.

## Why GitHub went down on August 17

The new data comes from a [postmortem of its August 17 outage](https://github.blog/news-insights/company-news/the-august-17-outage-and-the-work-ahead/), which lasted almost eight hours. That was GitHub’s second major outage in August alone.

As GitHub CTO Vlad Fedorov notes in the postmortem, “We have made progress, but these incidents make clear that we must accelerate this work.”

![](https://cdn.thenewstack.io/media/2026/08/8cf84602-blog-post-aug-17-outage-1.png-1024x576.webp)

Credit: GitHub.

He stresses that the outage was due to scaling issues, not any code changes. GitHub’s infrastructure ran out of capacity, and those issues cascaded into this outage.

“Our investigation found that the outage began when traffic reached a new peak, and a critical infrastructure component in our Central US data center failed to scale with it,” he explains. “The resulting capacity pressure spread through our systems, causing authentication failures and disrupting multiple GitHub services.”

![](https://cdn.thenewstack.io/media/2026/08/c43f4ad8-blog-post-aug-17-outage-gitfetch.png-1024x576.webp)

Credit: GitHub.

## 3M new CPU cores and GitHub still can’t keep up

It’s worth noting that this is not because GitHub isn’t scaling its infrastructure. Fedorov used the post to disclose that 58% of GitHub’s platform load is now served by Azure. That’s up from 12% in May. Half of all Git operations are now served by Azure, too.

The team added 3 million CPU cores this year, as well as 120 petabytes of high-speed storage, Fedorov writes.

As for GitHub’s own data center, that’s maxed out now. “We installed as much hardware as available power allowed in our existing data centers while accelerating our migration to Azure,” Fedorov says.

He also acknowledges that GitHub is facing other challenges as well.

“As the pace and complexity of change increased, our existing operational practices did not keep up. We have redirected teams and resources toward availability and invested in stronger testing, safer rollouts, better observability, and more effective alerting. We have made progress, but this work is not complete,” he writes. “In addition, we are also isolating critical systems and removing shared dependencies between them. This work is designed to reduce the likelihood of an outage and limit its impact when one occurs.”

For now, to avoid the issues that triggered the recent outages, GitHub is making a few concrete changes: it’s applying consistent retry limits and budgets, and tweaking timeouts across service-to-service interactions “to prevent retry storms and cascading load,” as Fedorov writes.

## A creaking GitHub is an opportunity for others

GitHub is central to the developer ecosystem — and especially the open source ecosystem. Its recent issues, however, have created an opening for others to launch competing products.

That includes [Entire](https://thenewstack.io/entire-git-for-agents/), the startup founded by GitHub’s former CEO Thomas Dohmke, which is betting on a distributed system to better handle agent-driven development workloads. With [Origin](https://thenewstack.io/cursor-origin-github-alternative/), Cursor, too, is getting into this game.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)