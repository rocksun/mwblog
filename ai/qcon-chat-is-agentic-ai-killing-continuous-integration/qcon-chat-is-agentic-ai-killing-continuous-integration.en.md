In the age of AI, will we still need [continuous integration](https://thenewstack.io/ci-cd/) (CI) at all?

One panelist in a [QCon AI conference](https://ai.qconferences.com/schedule/newyork2025) panel on AI and engineering asked this, perhaps deliberatively provocative, question: Will AI kill CI?

While many at the event quickly dismissed the notion that AI could go *that* far as to actually eliminate CI, the question resonated in the halls of the conference, held within the scholarly confines of the New York Academy of Medicine in Manhattan’s Upper East Side. It turned out to be one of the most hotly-discussed topics at the event.

And many people agreed that the [software development lifecycle](https://thenewstack.io/toward-a-3-stage-software-development-lifecycle/) will have to change in the era of AI.

[Daniel Doubrovkine](https://code.dblock.org/), who has worked in engineering positions at Shopify, AWS and Artsy.Net and recently took on a VP role at Microsoft, initially floated the question of if AI would kill CI altogether during a panel.

He had recently visited operations at Meta and was surprised how few tests the company actually ran before pushing new code to production, where developers can run many tests locally on their laptops (“[Shift Left](https://thenewstack.io/golden-paths-start-with-a-shift-left/)“) before pushing code.

“I think AI gives us a new opportunity to rethink how we work,” he said, noting it also gives us a chance to get rid of unnecessary tasks that have been built up on the way.

The pull request (PR) is the heart of a CI system, kicking off a whole series of [tests to the software before it is merged into production](https://thenewstack.io/how-ai-revolutionizes-software-testing-and-accelerates-product-releases/).

But “There’s no fundamental law of the universe that says that a PR review or a code review has to happen before the code is deployed,” agreed [Michael Webster](https://www.linkedin.com/in/mikedwebster/), principal engineer for [CI/CD](https://thenewstack.io/ci-cd/) service provider [CircleCI](https://circleci.com/?utm_content=inline+mention), [in his own talk](https://ai.qconferences.com/presentation/newyork2025/ai-works-pull-requests-dont-how-ai-breaking-sdlc-and-what-do-about-it). “There are a lot of compliance tools that say that has to happen, and those are important. But this is not a fundamental fact of software delivery.”

![CI diagram](https://cdn.thenewstack.io/media/2025/01/d539ad56-circleci-webster-pr-workflow-1024x363.png)

It doesn’t have to be this way — CircleCI’s Michael Webster (Google Gemini recreation of Webster’s slide.)

## AI is breaking the software delivery lifecycle

We [think of the development lifecycle](https://thenewstack.io/a-developers-lifecycle-how-i-shifted-my-thinking-and-coding-left/) as a linear series of discrete steps. “You push your code. You build, then you test, then you deploy,” Webster said.

“That model doesn’t hold up with AI,” he said.

Webster’s own QCON talk was about how AI, and agentic systems are changing the [software delivery lifecycle](https://thenewstack.io/ai-has-become-integral-to-the-software-delivery-lifecycle/). [CircleCI](https://circleci.com/?utm_content=inline+mention) is a CI/CD provider, processing over a billion customer jobs annually.

![headshot](https://cdn.thenewstack.io/media/2025/12/a7e6c590-qcon-webster-circleci-300x225.jpg)

CircleCI’s Michael Webster

From what CircleCI is seeing within its own customer base, the software industry is on the cusp of using a lot of headless agents, which can take on long-running tasks on a schedule or be activated via [webhooks](https://thenewstack.io/new-open-source-standard-brings-consistency-to-webhooks/).

Headless agents do well at mechanical translations, once given a solid set of rules to work from. A well-structured repository is key.

One project at CircleCI where agentic agents helped was a project to bring dark mode to CI/CD’s software. The design team specified the attributes required, and the agent did the laborious duty of going through all the user-facing components to make the changes.

“All in all, we’ve seen that this pairing of domain expertise plus AI is a really powerful organization attribute, because it allows more people to contribute,” Webster said.

By Webster’s estimate, through [Google’s GitHub Archive for BigQuery](https://github.com/igrigorik/gharchive.org/blob/master/bigquery/README.md), GitHub is now incurring hundreds of thousands of agent-related activities per week. What are they doing? Pull requests.

But an AI-fueled project can create an immense amount of code, which creates its own bottleneck.

“You have AIs pushing as much code as they are writing,” Webster said. Circle CI is also seeing this behavior with its own customers.

## The problems around pull requests

On average, a code reviewer could be able to inspect 500 lines of code in an hour. When an agentic service can produce 1,500 lines of code every 10 minutes, there is bound to be a traffic jam.

![](https://cdn.thenewstack.io/media/2025/12/31b0b153-qcon-webster-circleci-pr-300x225.jpg)

Presentation at QCon.

Beyond the numbers problem, pull requests are “inefficient generally,” Webster said. By many accounts, the median time that a PR review team can take reviewing code can range from 14 hours down to three, in cases when a single engineer relentlessly pushes one PR through.

Reviewing PRs takes you out of the flow, and the information provided would have been more useful earlier in the development cycle.

Persistent technical debt accumulation is also a problem with this tsunami of PRs.

Headless agents working autonomously can work quickly, but also sloppily. The most recent [DORA survey](https://thenewstack.io/ai-has-won-googles-dora-study-shows-universal-dev-adoption/) reports found the same: increased velocity, but more unstable.

In [one paper](https://arxiv.org/abs/2511.04427), a group of researchers found that adopting an AI service, such as [Cursor](https://thenewstack.io/cursor-2-0-ide-is-now-supercharged-with-ai-and-im-impressed/), can provide a temporary gain in code development, though the project’s velocity will soon be hampered by “static analysis warnings and code complexity.”

And in his own mathematical calculations, Webster estimated that any gains achieved with once AI-generating [code](https://thenewstack.io/ai-code-generations-unexpected-costs-for-dev-teams/) would become useless once AI becomes 75% faster overall than human coders.

“If you’re not able to complement to speed up your delivery,  compared to AI, it’s all going to be washed out by all of the delays in the process,” Webster said.

In other words, “the reality is, even if you did have AI going as fast as you wanted to, you as an organization, and the objective that you’re trying to achieve, couldn’t go faster even if you wanted to.”

There are things that you can do, such as optimizing pipelines, rewriting scripts, paralyzing tests, and better code reviews, which will all help.

![chart](https://cdn.thenewstack.io/media/2025/01/fed223e8-qcon-webster-circleci-pr-2-1024x432.jpg)

Agentic activity on the part of CircleCI customers.

## AI-generated code requires more nimble testing

But perhaps the best answer is to [rethink the testing](https://thenewstack.io/rethinking-testing-in-production/) and validation process to let agents do as much of the work as possible.

“If you have a way to validate the AI, you can let it run as fast as possible,” Webster said.

Develop a set of tests that assert that if the code passes the tests, it should go to production. As others have pointed out, [failure is a data set](https://thenewstack.io/the-key-to-agentic-success-let-unix-bash-lead-the-way/) that AI itself can use to fine-tune its own process.

Thorough [Unit tests](https://thenewstack.io/unit-tests-are-overrated-rethinking-testing-strategies/) are good for this, though are limited in scalability (to about 10x the human-driven workload, Webster estimated).

A better approach is [test impact analysis](https://learn.microsoft.com/en-us/azure/devops/pipelines/test/test-impact-analysis?view=azure-devops) to speed testing, through incremental validation, pruning tests to only what is needed, as highlighted by a dependency graph. CircleCI applied it to its own monolithic user interface application and found that it cut test timing from 30 minutes down to 1.5 minutes.

What this means is we can take an AI agent, have it work as fast as we’re willing to spend money on the tokens, and give it a tool to [run only the test](https://thenewstack.io/stop-running-tests-with-your-ci-cd-tool/) that it needs to run on the changes that it needs,” Webster said.

Such an operation can be easily run from within a container or a laptop.

The principle of selective attention can apply to code review. “Not all code has the same level of risk,” he said. “Here is where you can prune back review to just the changes that matter,” Webster said.

Circle CI has built its own agent, called [Chunk](https://circleci.com/chunk/), for customers to run to streamline their own testing processes.

## Future build systems will be less linear

Future engineers will be worrying less about the code and more about supporting the AI in its relentless pursuit of generating more code, Webster predicted. So tasks like [fixing flaky tests](https://thenewstack.io/how-to-fix-flaky-tests/) will become the first priority, and can be automated as well.

Instead of this linear process, we will need to build systems where all the required tests take place somewhere in the process.

“Instead of having a linear Yes/No, we combine these things into a single gate, where all we do is keep track of what has occurred,” Webster said. If a test passes, the coder should be moved to production. “Everything else besides that is us concerned about other things.”

With AI, “more effort and energy is likely going to be spent in this testing and evaluation, there is less so thinking about the specific designs of low-level details of our services.”

*Full access to these QCon AI talks, and [others](https://thenewstack.io/kepler-openais-internal-agent-platform-for-synthesizing-data/), can now be procured through a [video-only pass](https://ai.qconferences.com/registration/event/newyork2025).*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)