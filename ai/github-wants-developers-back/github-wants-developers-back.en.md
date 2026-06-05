For much of the past year, GitHub has not been the stable utility developers had long gotten used to. [Outages](https://www.githubstatus.com/history), hitting everything from search to GitHub Actions and the CI/CD pipelines that depend on it, have become too regular an occurrence. The company has logged hundreds of incidents over the past 12 months and has had to apologize in public.

*The New Stack* sat down with GitHub Chief Operating Officer [Kyle Daigle](https://www.linkedin.com/in/kyledaigle/) (who is now also the CMO of Developer at Microsoft) to talk about why all of this is happening and what GitHub is doing to fix this.

## Why planning for 100% growth wasn’t enough

![](https://cdn.thenewstack.io/media/2026/06/30168453-1712319381689.jpg)

Kyle Daigle

One thing the company has been quite open about is that it is facing unprecedented growth in this era of agentic coding — and one that goes well beyond what even a hyper-growth cloud company usually experiences.

To address this hyper growth, as Daigle put it, it’s now “all hands on deck” for GitHub.

“It’s not just about the normal scaling solution in the cloud era of let’s get a bigger machine or let’s do more machines,” Daigle tells *The New Stack*. “It’s now making sure that we can scale at 30 or 40 times over the course of the next year, rather than just a very impressive 100 percent year-over-year historically.”

GitHub assumed, Daigle says, going from 50 percent growth to 200 percent growth would be a surprise. “It turns out that that was the easy number and we need to go even more,” Daigle says. The engineering team at GitHub is now looking to get the system to a place where it can handle 30 times the commits, pull requests, and issues it processes today.

> “It’s not just about the normal scaling solution in the cloud era of let’s get a bigger machine or let’s do more machines.”   
> —GitHub COO Kyle Daigle

There is maybe a bit of irony in this, given that GitHub itself helped kick off much of this era with the launch of Copilot in 2021. This, in many ways, evangelized AI code generation among developers and trained them to lean on it. Now, GitHub is buckling under the load. In all of 2025, the service processed 1 billion commits. Now it processes 1.4 billion a month. Daigle says agents alone are now creating more than 17 million pull requests a month.

## What “all hands on deck” actually means

GitHub has been moving from its own data center to [Microsoft’s Azure cloud](https://thenewstack.io/github-will-prioritize-migrating-to-azure-over-feature-development/) to meet this demand, but Daigle notes that this isn’t just about adding capacity.

“What we’ve been really focused on is not only scaling in the normal ways of continuing to get more CPUs and doing the sort of normal horizontal and vertical scaling, but more importantly, really digging into the underlying systems, and updating them, or rebuilding them, or improving those hidden systems that do the core work,” Daigle says.

Much of the early work focused on relieving pressure on the database, as GitHub Chief Technology Officer Vlad Fedorov pointed out in a blog post earlier this year. GitHub addressed MySQL contention, moved webhooks entirely off MySQL, and redesigned its session cache and authentication flows to reduce database load.

For GitHub Actions specifically, Daigle says the way jobs are dispatched to runners had to be rewritten. The broader architectural goal is to isolate critical services like Actions and Git from everything else, so that a struggling subsystem doesn’t take others down with it. GitHub is also moving performance-sensitive code out of its Ruby monolith and into Go.

“Most of that low-hanging fruit, we’ve conquered,” Daigle says, though he admits the gains are hard to point to. “It’s the catch-22 of improving availability,” he says. “When you’re up, there’s not an easy way of saying, look, we made this improvement.”

GitHub is leaning on Microsoft for help, too. “It’s very much all hands on deck at GitHub,” Daigle says. “We’re getting more support than ever, with experienced engineers to come help us scale quickly.” Much of that reinforcement comes from Microsoft, including engineers who have scaled systems at this magnitude before.

“Our number one priority is having a platform that is up, that you can trust, and that’s reliable for the world’s developers,” Daigle says, “and now the world’s agents.”

## Why GitHub keeps shipping new features anyway

One question worth asking is, if availability is the priority, why is GitHub still rolling out a new Copilot app at its Build conference and other features?

Not every surface carries the same risk, Daigle argues. The CLI and the new Copilot app iterate outside the blast radius of hosted GitHub, so they can move quickly without touching the systems under repair. The backend work is “focused on stability and resilience,” and it occasionally unlocks features as a byproduct of rebuilding the underlying architecture.

“If I release a CLI piece of functionality, it doesn’t have the same stability and resilience characteristics as [github.com](https://github.com),” Daigle says.

That won’t matter much when the underlying infrastructure is down, of course, but Daigle seems hopeful that this phase of GitHub’s history will soon be over.

“Hopefully each month is a little bit better than the month prior,” Daigle says, “with all the urgency that we can put against it.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)