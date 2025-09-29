A [2025 Atlassian report](https://www.atlassian.com/blog/developer/developer-experience-report-2025) found that 50% of developers surveyed lose more than 10 hours a week to overhead work that’s not development. But [Jouke Visser](https://www.linkedin.com/in/joukevisser/) said on the frontend, the situation may be even worse — because the ecosystem grew so fast.

Platform engineering can help, according to Visser, who is a platform engineering ambassador for the [frontend](https://roadmap.sh/frontend). He is also the founder and chief architect at FrontenderZ, a specialist consultancy dedicated to helping large enterprises design, build and scale internal [frontend development](https://thenewstack.io/introduction-to-frontend-development) platforms. We asked Visser why the [frontend is ignored in platform engineering](https://platformengineering.org/blog/your-platform-has-a-frontend-blind-spot) efforts.

“Last June, when I was in London for the platform engineering conference, I walked up to [Kaspar von Grünberg](https://www.linkedin.com/in/kvgruenberg/?originalSubdomain=de) [an early pioneer in platform engineering] and asked him that very same question,” Visser told The New Stack. “And he said, ‘Looks like we don’t have many people speaking about it — why don’t you join [our ambassador program](https://platformengineering.org/ambassador-program)?’”

## Platform Engineering for the Frontend

The frontend has been ignored in platform engineering for too long, Visser said. He has worked in the field since 2017, when he acquired the title of solution architect for the frontend platform.

“I started doing research — well, that was very short because there was just nothing out there,” he said. “I really had to reinvent the wheel myself.”

Other organizations were working on similar initiatives, but not necessarily calling it platform engineering. They approached it more as a developer experience or developer enablement issue, he said. Their efforts were disorganized compared to the platform engineering on the backend, he said.

That led to a situation where the frontend is often behind on its dependencies, he added.

“It’s usually we’re behind on React two versions or we have an incompatible update that we want to roll out, or we change the architecture and we have no idea how to reach that team that is hardly ever working on any frontend stuff and get them aligned,” he said. “There’s so much overhead in that space, at least when I compare it to backend development.”

The backend is very API contract-based, he added, whereas with the frontend, the only thing you can be sure of is that the audience isn’t going to come together in a single browser window.

“How do you manage all that complexity?” he said. “Hopefully everything is just compatible and working well together and also looking good, right?”

## Creating a Platform for the Frontend

At the time, Visser was working for a company with a big mono repo that involved 160 teams working on just a couple of applications, with one platform team basically preparing all of the lifecycle management on any dependencies.

Basically, the team set up a six-week cycle leading up to a release where they would do all kinds of updates, including breaking changes. They then closed the PRs for an hour and merged the branch. At that time, everyone had to rebase.

If a test proved something didn’t work and was too complex to upgrade, they would pull it so they could do the build and work on the fix over the next six-week cycle.

> “All of these things, they’re interconnected, and I think if you have a take a step back and take a holistic approach to to the entire ecosystem that your developers need to work with, that really helps and establishes a good developer experience, also.”  
> **– Jouke Visser, frontend platform engineering ambassador**

“Instead of everyone in all of those 160 teams doing their own part on their own updates, it was one team spending, on average, a third of their time overall, scripting these kinds of changes,” he said. “That’s was just taking care of 160 teams, not having to worry about any upgrades anymore.”

Inevitably, there were the teams who were behind, who didn’t test until before the release, but the platform engineering team took a stance: This is the rhythm and there’s no waiting for one or two teams who aren’t ready.

“That strictness led to compliance,” he said.

The discipline was born out of a situation that happened when he first became a [platform engineer](https://thenewstack.io/tips-for-building-a-platform-engineering-discipline-that-lasts/).

“We were horribly behind on AngularJS and there was just no way we could organize an on-step upgrade without basically spending six months on aligning and coordination between different teams,” he said. “The bank was not happy with us, being behind so far, that became a number one priority: Always be up to date with all of your third-party dependencies and have a full compliance check on all the security issues that were reported with any of the dependencies.”

That lead to the insight that dependencies needed to be organized and organized at scale.

“How do you do that? By centralizing that responsibility, but still with the collaboration of the product teams,” Visser said.

It was a slow process, he acknowledged, that required a few years before it became really ingrained in the organization. But now that company is ahead of other organizations, he added.

## Get Started With Frontend Platform Engineering

The first step in any [platform engineering effort](https://thenewstack.io/platform-engineering/platform-engineering-what-is-it-and-who-does-it/) is to get buy-in from developers by ensuring the platform will bring value to their jobs by solving something for them, he said.

“Let’s face it, we’re engineers; the most stubborn people that there are, and I consider myself part of them,” Visser said. “If you know how to solve a problem, if you are used to a tool, you’re not necessarily willing to change that because someone else tells you to.”

To get buy-in, which in turn will lead to adoption of the platform, start by interviewing and surveying the developers the platform will serve, he suggested. Ask them what they need and want from the platform.

> “It’s about the problem that they’re facing and how they want to work in their developer flow. If you can make that happen, the conversation is not so much about the actual technology that you’re using.”  
> **– Jouke Visser**

“If I build a platform and I standardize on using Yarn, and rest of the world is using PNPM, and I’m telling them ‘Because I say so, you have to change from PNPM to Yarn,’ and they say ‘We’re going back in time’ — that’s not a conversation you want to have when you are implementing your platform,” he said. “That’s a discussion you need to have upfront [while] making sure that you’re building the right thing.”

Platform engineering isn’t just about tooling or technology, he added.

“It’s about the problem that they’re facing and how they want to work in their developer flow,” he said. “If you can make that happen, the conversation is not so much about the actual technology that you’re using.”

Second, a development shop would ideally identify what’s causing developers the most time. That will identify the pain point for a platform engineer.

“Solve it well in a productized version in a fashion that’s repeatable and automated, then we really help the organization with that specific pain point,” he said. “That builds trust in [the idea that] if they do it like this for this other aspect that we’re struggling with, then we can slowly but surely build out a platform.”

## Frontend Platform Engineering Requires a Holistic Approach

Platform engineering should also [take a holistic approach](https://thenewstack.io/port-platform-engineering-can-be-the-first-step-in-system-automation/), he added.

“It’s not just about the dependencies, because if you talk about the dependencies, then that automatically has a reflection on what you build yourself and how you build it yourself,” he said. “In order to have the flexibility to be able to switch between frameworks, for example, or to support multiple frameworks, if that’s your thing, have some core functionality in a framework-agnostic way, in core libraries that you can reuse in multiple frameworks.”

Doing that will have a consequence for the way you build your software, he added.

“All of these things, they’re interconnected, and I think if you have to take a step back and take a holistic approach to the entire ecosystem that your developers need to work with, that really helps and establishes a good developer experience, also,” Visser said.

Although Visser has some dissenting views about the issue of technical debt — he’s not sure it’s something you fight against so much as something that should be considered in the way developers work with their own code — he said that platform engineering can help with technical debt if the platform team implements the right guardrails, he said.

“That’s where I learned my biggest lesson from failure, I would say, because we didn’t have any proper architectural guardrails in place. We hardly had any linting rules in place,” he said. “When, within six months, at least 50 teams on-boarded on that platform, they all had their own specific way of doing things and in terms of standardization, we weren’t prepared for that.”

This taught him that a platform engineer should at least have a baseline of style guide and architectural rules — just a base set of rules in place — to which every developer has to adhere.

“That makes it so much easier to maintain later on,” he added.

Ideally, frontend [platform engineering](https://thenewstack.io/ebooks/platform-engineering/platform-engineering-what-you-need-to-know-now/) will provide a set of building blocks that developers need — like a design system or customer authentication.

“If you have all of that standardized, it’s so much easier to just build something,” he said.

*For more on how to get started, Visser’s company FrontenderZ offers a free download, [The Architect’s Guide to Frontend Platform Engineering](https://www.frontenderz.io/download-the-architects-guide-to-frontend-platform-engineering). You can also read more about [platform engineering on The New Stack](https://thenewstack.io/platform-engineering/).*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)