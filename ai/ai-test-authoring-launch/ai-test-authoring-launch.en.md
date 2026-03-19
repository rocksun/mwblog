AI code-generation tools have compressed software development cycles, but testing hasn’t kept up. [Sauce Labs](https://saucelabs.com/) thinks it has found an answer.

To ensure that testing doesn’t become a bottleneck, Sauce Labs this week [launched](https://saucelabs.com/company/news/sauce-labs-AI-for-authoring-news-release) AI for Test Authoring, built around what it calls “intent-driven testing.”

Instead of writing test scripts that specify every click, browser, and operating system, as has been the norm for a while, engineers or product managers can use this new tool to describe what an application is supposed to do, either in natural language, through a Jira spec, or even from a Figma design. The platform then generates executable test suites that are not tied to any one framework and runs them on Sauce’s cloud platform across virtual and real devices.

## Why testing became a bottleneck

[Prince Kohli](https://www.linkedin.com/in/princekohli/), who joined Sauce Labs as CEO about a year ago from Automation Anywhere, has a pretty straightforward diagnosis for why testing has been a bit neglected: Nobody wanted to work on this problem.

> “It is not sexy. Most engineering heads, therefore, tended to punt it and deprioritize.”

“It is not sexy,” Kohli tells *The New Stack*. “Most engineering heads, therefore, tended to punt it and deprioritize.”

The result was two decades of drift. “Twenty years ago, it was a lack of interest. Fifteen years ago, when manual QA started becoming more automated, it got into its own journey of do you send it offshore with cheaper people, or do you start automating?” Kohli says. “That’s been the last 20 years of testing, and it’s not a happy place to be.”

The shift from manual to automated testing was progress, but Kohli argues it stopped short of fundamentally rethinking what a test could be.

## The velocity-quality gap

It’s only now, with code generation speeding up thanks to AI, that this question has come to the forefront again. Shipping the code to production — not writing it — is now the bottleneck.

“You can accelerate code writing with AI, but you can’t really ship the code until you know that it works well,” Kohli says. “And you can’t use OLD techniques when code writing is becoming so fast, and the quality of that code is actually becoming lower, simply because human verification is not actually keeping up. You need to reimagine testing.”

Code Labs’ own research shows that 89 percent of CIOs identify test authoring speed as the primary bottleneck in AI-driven delivery of automated coverage. For complex user journeys, automated test coverage rarely exceeds 35 percent, while teams spend 40 percent of their time maintaining tests and scripts.

![](https://cdn.thenewstack.io/media/2026/03/bcd41e92-safta-conceptual-b.png)

## Intent-driven testing

Intent-driven testing is meant to change this by removing much of the day-to-day toil for writing and maintaining scripts. In a way, that’s pretty much what AI coding has done for handling routing code changes, for example. It’s a different way of thinking about tests, Kohli argues. “You don’t say, ‘When someone clicks on X, Y should happen,’’ he says. “You say, ‘I’m building an e-commerce app. I want to add five T-shirts, check out via PayPal, and ship to my home in California.’ That’s a happy path.”

Sauce Labs’ service takes that description and dynamically generates test suites across browsers, operating systems, and device types. Because the specification never mentions a specific framework or OS, the resulting tests aren’t tied to one either.

> “We remove most of the heavy lifting, but we’re not trying to take ownership away.”

“We remove most of the heavy lifting, but we’re not trying to take ownership away,” Kohli says. “You would have spent three days writing this. It’s done now in three minutes, but this is still your code.”

The argument for this approach, Kohle says, is durability. Traditional test quickly scripts break when a front-end element changes. Tests defined by intent don’t carry that dependency, Sauce Labs believes. When a new version ships, the intent doesn’t change, so the tool can regenerate the tests.

And that’s an important point to highlight. The test itself is still written in code and can be edited and adjusted just like before.

![](https://cdn.thenewstack.io/media/2026/03/42b15bd7-safta-feature-steps-d.png)

Credit: Sauce Labs.

## The data moat

Sauce Labs’ competitive case comes down to data: 8.7 billion test runs accumulated across its customer base.

“We’re not giving a prompt. We’re giving RAG data,” Kohli says. “We know from history what the right places to test are. If you’re writing an e-commerce app, we know where the flaky parts usually are.”

The company claims 41 percent faster root-cause analysis than general-purpose LLMs and counts 80 percent of the world’s top 10 financial institutions as customers. In regulated industries like pharma, where some companies must retain 30 years of test data, Kohli says compliance knowledge is something a general-purpose coding tool lacks.

Sauce is only one of many companies exploring the use of LLMs to automate testing. Companies like Applitools and Mabl have been building toward AI-assisted testing for years, and newer entrants like QA Wolf and Momentic are also pushing into the testing space.

To some degree, the larger question may actually be whether test authoring stays a standalone product at all. If the coding tools (and the LLMs that back them) keep getting better, they may eventually be able to build and run these tests as part of their process, too.

Kohli’s counter is that a general-purpose model can generate test code, but doesn’t know where an e-commerce checkout typically breaks or what regulatory retention rules look like at a pharma company. That knowledge, he says, is Sauce Labs’ moat.

Sauce AI for Test Authoring is generally available today, priced per developer rather than by token consumption. In part, that’s because Kohli doesn’t believe that consumption-based pricing will work in the enterprise. Procurement groups, after all, don’t like to approve products where the final cost is unknown.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)