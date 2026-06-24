When Project Valkey released version 9.1 last month, users, contributors and maintainers alike were understandably excited: There were new functionalities and improvements spanning security, observability, performance, and efficiency.

What not everyone knew was that 9.1 had a whole batch of bug fixes performed by an AI agent.

For the uninitiated, [Valkey](https://valkey.io/) is an open source, high-performance, [in-memory data store](https://thenewstack.io/is-a-database-caching-layer-still-necessary/). With a home at the [Linux Foundation](https://thenewstack.io/the-linux-foundation-in-the-age-of-ai/), the [Redis](https://thenewstack.io/redis-is-open-source-again/) alternative supports caching, message broker queues, and complex key-value data structures.

## A stack of bug fixes needed cherry-picking

[Madelyn Olson](https://www.linkedin.com/in/madelyn-olson-valkey/), Valkey project maintainer and principal engineer for [AWS in-memory databases](https://thenewstack.io/diving-into-aws-databases-amazon-rds-and-dynamodb-explained/), tells *The New Stack* that as the team geared up for the [Valkey 9.1 release](https://valkey.io/blog/valkey-9-1-delivers-improvements-in-security-performance-and-more/), their release branch was waiting on a stack of bug fixes that needed cherry-picking.

## Beyond backporting bug fixes

“Instead of relying on manual labor to backport those bug fixes, we deployed an AI agent,” Olson says. “The agent picked up the fixes, applied them, ran the continuous integration pipelines… and seamlessly handled any merge conflicts. That is the exact kind of AI we are interested in at [Valkey](https://thenewstack.io/valkey-a-redis-fork-with-a-future/ "Valkey") — real efficiency and no hype.”

Although there are efficiencies inherent to using a [backport](https://en.wikipedia.org/wiki/Backporting) process (taking a software fix, feature, or security update from a newer version of an application and applying it to an older version), the process can still be complex and laborious in codebases where major changes or modifications are happening.

> “That is the exact kind of AI we are interested in at Valkey — real efficiency and no hype.”

Olsen explains that the team used to “spend hours backporting bugs and security fixes” to older branches to make sure the database continues to perform reliably and securely across versions. This work is critical, but time-intensive for the team, as the branches diverged over time.

The goal (and therefore the validation for embracing the use of an AI code agent) was to give project maintainers their hours back for other project-critical tasks.

“Throughout the 9.1 cycle, we deployed AI to manage backports, conduct code provenance scanning and run verification. By offloading the repetitive, manual work that doesn’t strictly require human judgment, our maintainers were able to focus their energy on core engineering,” explains Olsen.

## Valkey is a “hot” part of data ecosystems

A primary challenge for the Valkey project is managing multiple support branches simultaneously, including [versions 7.2, 8.0, 8.1](https://thenewstack.io/valkey-8-1s-performance-gains-disrupt-in-memory-databases/), 9.0 and now 9.1. Because Valkey is an always-on part of applications for its users, there can be some hesitation to update to the latest major version. Its maintainers describe this as a “healthy worry” that is born out of Valkey being a “hot” part of their ecosystems.

To address this, the project developed a backporting agent designed to automate the maintenance work. This bot works to backport the needed changes, ensuring that backported code passes all relevant continuous integration tests for older versions.

## Humans, still in-the-loop

“The agent workflow proactively identifies test fixes that might need to be backported. Humans are still in the loop, as they are required to perform the final sign-offs before merging, but the tool has allowed our team more time for non-maintenance priorities, saving several hours of testing time per engineer per week,” says Olsen.

> “The Provenance Guard agent runs automatically in the background, notifying maintainers of problematic pull requests and reducing the overall cognitive load on the human review team.”

In addition to this backporting agent, the project has also developed an AI tool to assess and maintain the integrity of the codebase.

Known as Provenance Guard, this agent scans incoming pull requests to verify that no code is inadvertently taken from the unsanctioned codebases and applied to Valkey. The Provenance Guard agent runs automatically in the background, notifying maintainers of problematic pull requests and reducing the overall cognitive load on the human review team.

“Provenance Guard functionality inside our project is both a preliminary and auxiliary check in addition to human-driven code review,” confirms Olsen. “Said differently, the guard is not a last line of defense on our code, far from it. The agent merely offloads an initial scan from a human counterpart, allowing for another set of eyes on a highly deterministic security check.”

Provenance Guard has been successful in catching unintentional copying and its presence is another enhancement to the project’s ongoing security practices.

> “Agents are excellent at routine coding tasks and summarizations, so I would challenge new engineers to ramp up quickly with AI.”

## What agentic debugging means for new developers

With computer science degrees typically taking four years and ChatGPT having been around since it was [launched as a public research preview](https://github.com/jqueryscript/chatgpt-timeline) on November 30, 2022, just three and a half years ago, if agents now handle routine merges seamlessly, what new skills must younger developers master to remain valuable to teams?

“Junior developers, in addition to all the critical coding skills they’ll need to contribute to projects, should also start to tinker with AI on their own,” advises Olsen. “Agents are excellent at routine coding tasks and summarizations, so I would challenge new engineers to ramp up quickly with AI.”

She further states that because agents are “quite good at more basic tasks,” this frees newer joiners to do more systemic thinking about the direction of the project, how a certain feature impacts existing tooling.

“Whether they like it or not, it’s certain that newer engineers will be working alongside agents, so learning how to audit these bot coworkers and coexist will be integral,” Olsen says. “Pragmatism is a core tenet of how AI has been deployed amongst our community, but the results of these initial agents leave our maintainers with real optimism for what’s next.”

## Ready for more agentic code support

Valkey 10.0 is the next stage of the project’s evolution. The next version of Valkey will focus on further improvements to performance, memory efficiency, agentic memory and more.

Looking back at 9.1, Olsen and team say that the hours of labour saved from its agentic tools have allowed them to do more with its community. Everyone is curious about just how much agentic tooling will support the 10.0 launch, not to mention how different coding, debugging and other software engineering agents might look in six months or so.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)