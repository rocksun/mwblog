**At its annual Universe ’26 conference in San Francisco this week,** GitHub took to the [question of the platform’s stability](https://thenewstack.io/github-2-9b-monthly-commits/) head-on.

The code-hosting company spent a significant part of the event’s keynote to talk about the investments it is making. That includes [adding 4 million cores and 160 petabytes of storage](https://thenewstack.io/github-7-4b-commits-september/), along with a full rearchitecting of its backend infrastructure.

But at a press conference and in interviews with *The New Stack* after the keynote, the leadership team of [Jay Parikh](https://www.linkedin.com/in/jayparikh), the executive VP of CoreAI at Microsoft who now leads GitHub, and GitHub COO [Kyle Daigle](https://www.linkedin.com/in/kyledaigle/) also answered questions about what GitHub’s role is in this changing developer landscape — and how they feel about some of the [competition that is now popping up](https://thenewstack.io/cursor-origin-github-alternative/) in response to these changes.

It’s a timely question, since former GitHub CEO Thomas Dohmke launched a [GitHub alternative](https://thenewstack.io/entire-trails-agentic-code-review/) just a few days before GitHub’s conference.

When asked about [Entire, Dohmke’s startup](https://thenewstack.io/thomas-dohmke-interview-entire/), at the press conference — and Microsoft’s M12 investment arm funding of Entire — Daigle diplomatically noted that Microsoft often invests in tools “that compete not only with GitHub but with the entirety of the Microsoft product estate. And that’s a good thing. That’s not a bad thing.”

Daigle noted that GitHub operates at a global scale, serves more than 225 million developers, and keeps iterating to better serve them.

> “I don’t think the world needs a new GitHub.”  
> —GitHub COO Kyle Daigle

“I don’t think the world needs a new GitHub,” he said. “They might need different tools. That’s great, but what they need is [GitHub] to evolve for the agentic era, which is what we’re doing.

“The stats for the Git layer that we showed today kind of speak for themselves.”

![](https://cdn.thenewstack.io/media/2026/10/1973762f-img_5949-edit-1024x768.jpg)





*Credit: The New Stack*

Daigle stressed to *The New Stack* the role GitHub plays in the overall software development ecosystem — spanning individual developers, large open source projects, and Fortune 100 enterprises.

Daigle argued that the conversation about new Git forges, or version control forges more broadly, focuses too narrowly on companies and the economic use of those platforms. “I think that loses a core component of the problem,” he told *The New Stack*.

“We’ve never been the only Git host. We’ve never been the only SCM host,” Daigle said, pointing to Perforce and other options companies have relied on for years. What sets GitHub apart, he argued, is hosting all developers together at scale, rather than focusing only on enterprises or only on open source. “I don’t see folks trying to go solve that problem. They’re trying to solve a part of the problem,” he said. “There are places where they’re very opinionated and doing it in a unique way. I think that’s always been true.”

Daigle’s argument, at its core, is that it is much easier to build tools that focus on the enterprise. At least for now, that is where Entire and most other Git forges have their focus.

More sharply, Daigle said this moment “feels similar to the end of the zero interest rate era,” when “there were a lot of really talented, interesting developer tools, but they were just incredibly narrow.” He added: “Luckily, a lot of those folks ended up joining GitHub — and doing some really great work.”

> “GitHub may not think there needs to be a new GitHub, but developers clearly do.”   
> —Entire CEO Thomas Dohmke

## Entire’s reaction

When asked by *The New Stack* to comment on Daigle’s assessment that the world doesn’t need a new GitHub, Dohmke provided the following statement: “GitHub may not think there needs to be a new GitHub, but developers clearly do. Do we really want to put the future of software development and open source into the hands of a single big tech company? We are building [Entire](https://thenewstack.io/entire-trails-agentic-code-review/) so the new home of the community is open source, scalable, and resident in many regions around the world.”

## Platforms versus products

With new competition for users debuting in the form of Dohmke’s Entire platform, Parikh emphasized the importance of GitHub’s user community and the platform it offers at Wednesday’s press conference: “With how fast the world is changing around how we build and the lifecycle of software, the power of the community, I think, is more important than it’s ever been in terms of what we’re creating, how we’re sharing, how we’re learning together.”

Parikh made a similar point in a later interview with *The New Stack*, drawing a distinction between individual development tools and the platform that supports them when asked about the competitive landscape GitHub now faces.

“GitHub and Microsoft have always been platform companies,” he said. “So much of what’s out there are products, and yes, we have products, and we have platforms.”

For Parikh, that means offering a complete development workflow while also letting developers choose which pieces they use. Or as Daigle put it, “we’ll give you the full flow, or we’ll give you the primitives, which I think is what most companies want. Everyone’s interested in what is the one way to do this, but nobody wants to buy the only way. They want to have the optionality and the choice.”

## Where agents break things

Supporting those varied workflows ended up forcing GitHub to reconsider some of the assumptions the team had made about which services were most likely to fail.

“The places that have failed are not the places we would have expected to fail historically, because agents act in such a different way than a human being,” Daigle said. “Some services that were scaling perfectly, and we thought were good to go for quite some time, had a surprising failure.”

![](https://cdn.thenewstack.io/media/2026/10/91c580ab-img_5947-1024x768.jpg)





*Credit: The New Stack*

Those failures began emerging in early summer, prompting GitHub to look beyond adding capacity as the main solution.

“It’s not just increasing the number of cores, the overall horizontal scaling, but looking at core services that need to be completely rewritten because the behavior pattern is so incredibly different,” Daigle said.

Parikh, whose experience includes scaling infrastructure at Facebook and Akamai, said the current growth rate makes incremental improvements pointless.

“You have to take a full systems look at it,” he said. “Getting five or 10% here or there, it lasts you two weeks or a week now.”

What makes all of this harder is that GitHub has to make those changes while keeping the service running and compatible with existing workflows. And in the meantime, the traffic patterns are changing, too, Parikh said.

“The traffic patterns are also not static right now … We optimized CPU, and now all of a sudden the bottleneck is going to move somewhere, and then you’re like, ‘Oh, I thought it would show up here, but it showed up here.’ Right now, the good news is you do these in staged rollouts. You test these things, and then you adjust,” he said.

One substantial architectural change the team has committed to is separating compute from storage in GitHub’s Git infrastructure. This now allows the company to more easily scale each according to demand.

“Depending on what that traffic is, time of day, who’s using it and what type of product offering sits on top of it, you can scale these things independently and optimize for how that compute workload changes and how that storage workload changes,” Parikh said at the press conference.

[Moving from GitHub’s own data centers to Azure](https://thenewstack.io/github-will-prioritize-migrating-to-azure-over-feature-development/) also provides more capacity, geographic flexibility and redundancy, Parikh said, which the existing facilities could not offer. But he also stressed that the work remains unfinished and includes additional changes to harden and scale GitHub Actions, for example.

“We can’t add the capacity. We don’t have the scale in those fixed data centers that GitHub has operated on, and so moving into cloud infrastructure that gives us flexibility and scale and location and redundancy and network and all that is much better for us,” Parikh told *The New Stack*.

## Keeping free repos free

Interestingly, these architecture changes also affect the economics of hosting all open-source code and free repositories on GitHub.

Daigle said that separating compute and storage should reduce the cost of storing Git repositories, helping GitHub maintain access as developers and their agents create more work.

Daigle said GitHub has a responsibility to its community. Suddenly limiting developers to a handful of private repositories “breaks the whole contract of what GitHub is,” he said.

Daigle said anyone writing code, whether they’ve done it for years or are just starting, should have a home on GitHub. “A repo should not be hidden out on your laptop, or [be] an HTML file shared between friends,” he said. “We have a place for that.”

He did, however, distinguish that commitment from the cost of supplying AI models. GitHub cannot give everyone unlimited free tokens, he said, and has had to decide [where to subsidize access](https://thenewstack.io/github-copilot-usage-billing/).

## Rethinking Git and verification

Beyond GitHub’s own infrastructure, Daigle also sees room to change Git itself. He wants the company to work with the community on its underpinnings and sees a role for something like “a porcelain layer on top of Git,” which he described as a higher-level interface that simplifies access to the underlying system.

Daigle said GitHub needs to “assert our role in the community” and work with established and new players alike to rethink some of Git’s underpinnings. “They kind of didn’t make sense before the agent change,” he said, “and now they really, really don’t make sense.”

At the same time, though, Daigle remains cautious about whether this agentic era needs an entirely different version control system.

“I want to know we need to move before we move,” he said. “I don’t think we’re done with [Git] yet. I just think we do need to lean in more.”

“You actually need to review it, you need to push it into production, you need to run other workflows, you need to do AI scanning for security issues,” Parikh said at the press conference.

> Daigle expects verification — reviewing, testing, and deciding whether software should reach production — to become the next bottleneck.

Daigle expects verification — reviewing, testing, and deciding whether software should reach production — to become the next bottleneck. He argued that even unlimited CPUs wouldn’t make running every build after every agent commit desirable.

“If I have 5 or 10 agents running at a single time, I don’t actually want or need all those builds for the sake of the agent,” he said. “And that requires a change in behavior for the agents or the humans involved.”

Among the possibilities he raised were signing locally executed builds and submitting them with an agent’s work, selecting a smaller set of relevant tests, and exploring proof-driven development. The right combination of tests, evaluations and live verification will depend on the application.

“If you’re an automaker, you’re not going to say, ‘Well, I’ll let my agent check if the brake caliper was engaged or not,’” he said.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)