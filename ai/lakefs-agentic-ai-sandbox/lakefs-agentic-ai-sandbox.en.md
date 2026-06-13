**Beneath the chatbots and copilots, there’s a quiet revolution happening** in the data services space**.** From pure-play database vendors to data integration wranglers and onward to the cloud hyperscalers, the focus has shifted.

Now in the spotlight is the question of how to automate data governance for agentic AI workloads, and for good reason: Traditional manual data stewardship doesn’t scale in a world where agents are becoming increasingly autonomous (and powerful).

Aiming to cut a swath in this marketplace is data control plane company [lakeFS](https://lakefs.io/). The organization announced its lakeFS for Agentic AI service on Wednesday, and it appears to be designed to bring governed, reproducible data access to autonomous and [headless agentic](https://thenewstack.io/why-headless-browsers-are-a-key-technology-for-ai-agents/) workloads (those that execute decisions below the user interface level) that run at enterprise scale.

## The manual model breaks

[Einat Orr](https://www.linkedin.com/in/einatorr/), CEO and co-founder of lakeFS, tells *The New Stack* that manual data stewardship was built for human-paced, human-reviewed workflows, i.e., someone looking at a change before it is committed.

“When dozens or hundreds of agents are making changes simultaneously, faster than any person can review, the manual model breaks,” Orr says. “This is because with a human analyst, a bad write to production is usually one mistake, caught by another human before it spreads far. An agent is different — it acts automatically, in parallel, at machine speed, and it doesn’t pause to second-guess itself. And because so much agent activity is unsupervised, you often find out after the damage is done.”

She explains that attempts to identify and roll back incorrect or corrupted production data across a wide set of data modalities, such as images, documents, metadata, and structured data, are almost impossible to pull off. Impossible, that is, unless the team has the data infrastructure in place to isolate and track such changes automatically.

While some of the more disastrous outcomes stay inside an organizaton’s perimeter (or are swept beneath the communications radar), Orr explains that real world consequences of bad agentic data writes are manifold.

“Insurance claims get inappropriately denied or approved, sensor data from machines gets misinterpreted, an incorrect medical diagnosis is made, or customer service bots provide incorrect answers to customers,” Orr says. “The cost of an individual action may be manageable, but agents performing these actions hundreds or thousands of times can have an exponentially larger impact.”

> “As agents are let loose on enterprise data at a massive scale, any agent that reads or writes to production data without isolation or a reproducible trail is a liability, no matter how good the model is,”   
> —Einat Orr, lakeFS CEO.

## Bad agents acting in the real world

Examples of this happening include the July 2025 [Replit AI coding agent incident](https://x.com/jasonlk/status/1946069562723897802), which deleted a live production database during an explicit code freeze, wiping records for more than 1,200 executives and around 1,200 companies. To tidy up its handiwork, the agent then fabricated thousands of fake records and initially claimed the deletion couldn’t be rolled back.

Also in July 2025, [Google’s Gemini CLI agent misread](https://incidentdatabase.ai/cite/1178/) a single failed command, acted on a version of the file system that existed only in its own interpretation of the scenario, and permanently destroyed a user’s project files. The Gemini agent is [widely reported to have said](https://developers.slashdot.org/story/25/07/26/0642239/google-gemini-deletes-users-files-then-just-admits-i-have-failed-you-completely-and-catastrophically) of its actions: “I have failed you completely and catastrophically. My review of the commands confirms my gross incompetence.”

“The pattern in both is the same: An autonomous agent took a destructive action that no one authorized, and the lack of isolation and a reliable rollback path turned a single mistake into permanent loss,” Orr says.

A doctor of mathematics with a track record in hardcore software engineering, the bottom line for Orr is clear: “As agents are let loose on enterprise data at a massive scale, any agent that reads or writes to production data without isolation or a reproducible trail is a liability, no matter how good the model is,” she said.

> “…any agent that reads or writes to production data without isolation or a reproducible trail is a liability…”

[Gartner expects 40 percent](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025) of enterprise applications to have task-specific agents embedded by the end of 2026, up from less than 5 percent a year earlier. [IDC projects](https://www.idc.com/resource-center/blog/agent-adoption-the-it-industrys-next-great-inflection-point/) that agent use at the largest enterprises will grow tenfold by 2027, with the API and data calls those agents make growing a thousandfold.  
That’s the scale production data has to withstand, and it’s what lakeFS is built to govern.

## Agents sent to play in an isolated data sandbox

To address these issues, lakeFS for Agentic AI gives every agent its own isolated data sandbox with a “zero-copy” branch of relevant data, so the agent can access the dataset it needs via references, snapshots, or copy-on-write techniques.

This means any changes the agent wishes to make must be validated and merged in accordance with the policy guidelines defined by the system architecture. In turn, this produces a unified audit trail across every agent action.

When running, lakeFS for Agentic AI is powered by its data version control architecture, which provides zero-copy data sandboxing. This enables isolation so that agent mistakes are automatically isolated and never corrupt production data. Every agent run is tied to an exact, immutable version of the data. Past actions can be recreated, debugged, audited, or extended using the same inputs.

Production data is gated by policy. Merges into production happen only after pre-merge validations pass. Every change can carry an agent identity, a run ID, and an execution context. The result is a unified audit trail instead of evidence scattered across orchestrators, model providers, and cloud logs.

## Agents confined by branch-scoped credentials

Where agents are permitted to read and write through standard file operations. lakeFS provides file-level data access with branch-scoped credentials. These can be described as strictly cryptographically bounded, ephemeral access tokens that confine an agent to a specific branch of data or code, so that the agent operates only within its own workspace. This whole mechanism keeps each agent’s working set narrow and avoids context bloat.

“With lakeFS Mount, a branch, or even a subset of a branch, can be mounted as a local directory inside the sandbox or virtual machine where the agent is running,” Orr confirms. “From the agent’s perspective, it’s just reading and writing to files and folders.” She further clarifies and notes that no LLM tokens are spent learning the lakeFS API. The agent works with a familiar filesystem interface, and lakeFS handles the versioning underneath.

Developers also have a couple of options for injecting custom validation logic. CEO Orr explains that software engineers can use webhooks or Lua scripts, both of which allow users to define behavior and rules that must be met before a merge can proceed.

“Beyond automated checks, lakeFS also supports pull requests, which bring a human into the loop. In agentic workflows, this gives you a way to review and approve what an agent is proposing before it reaches production,” she clarifies.

## Who else builds “Git for data” services?

Clearly, other vendors and projects exist in the data versioning market.

[Apache Iceberg](https://iceberg.apache.org/docs/latest/branching/#:~:text=For%20more%20sophisticated%20snapshot%20lifecycle,and%20tag%20level%20retention%20policies.) has functions for branching and tagging data. [HPE acquired Pachyderm](https://www.hpe.com/us/en/newsroom/press-release/2023/01/hewlett-packard-enterprise-acquires-pachyderm-to-expand-ai-at-scale-capabilities-with-reproducible-ai.html) back in 2023 for its data versioning and pipelines technologies, which serve MLOps teams.

Originally developed by Dremio, [Project Nessie](https://projectnessie.org/) is now an open-source data catalog and version control system for data lakes. Data Version Control (DVC) is an open-source data version control infrastructure designed for complex AI operations and big data environments, but now we’ve come full circle as lakeFS [acquired the project](https://lakefs.io/media-mentions/lakefs-acquires-dvc-uniting-data-version-control-pioneers/) in late 2025.

In the search for governance automation for agentic AI workloads, lakeFS appears to offer a comprehensive, cohesive set of tools and functions. In the “Git for data” marketplace, a variety of options exist, but lakeFS hasn’t explicitly positioned itself as a carte blanche replacement for similar or related tools.

One thing is certain: The questions of who is feeding what data to which agentic function, when, where, and why are becoming an increasingly pressing issue if we want AI to work correctly.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)