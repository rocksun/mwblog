Meet AUTOSEL, a Linux maintainer that helps keep the kernel stable.

AUTOSEL is a script, one that uses a Large Language Model (LLM) to complete its task.

It does a thankless job, one loathed by all kernel maintainers, that of backporting patches.

Backporting patches is a “very tedious and frustrating process” that “doesn’t scale,” said NVIDIA Distinguished Software Engineer [Sasha Levin](https://www.linkedin.com/in/sasha-levin-9861662/), in a [talk](https://ossna2025.sched.com/event/1zffD/ai-for-kernel-engineers-sasha-levin-nvidia) at the [Open Source Summit.](https://ossna2025.sched.com/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) The [presentation](https://lwn.net/Articles/1026558/) focused on how AI is starting to be used in the Linux kernel community to help keep up with the Herculean tasks of maintaining the Linux kernel.

It may not be writing exciting new features for the open source operating system kernel yet, but AI has excelled in tasks that are mind-numbingly repetitive yet still necessary. In other words, AI is already making the lives of Linux kernel developers easier, said Levin, who helps maintain the Linux Kernel Stable and LTS trees.

## Patch Inspection

As the world’s single largest open source project, the Linux kernel gets updated and upgraded … a lot.

The pace has remained constant: As many as 10,000 new patches have landed in the mainline kernel over a 10-week period.

Stable and Long-Term Support (LTS) kernel maintainers usually review around 100 patches per day, every day, including weekends and holidays.

Only a few, about 5-10, turn out to be suitable for backporting.

Levin’s [**AUTOSEL**](https://git.sr.ht/~sashal/autosel), written in Rust, takes a first pass at incoming commits, looking for similarities across submitted commits and past backporting decisions, and suggesting only those to human committers to seem to be worthy of closer review.

AUTOSEL is built from multiple LLMs, with each LLM used for a particular strength, as well as for cross-validation to reduce errors and hallucinations.

For each commit, the tool creates mathematical representations (or “embeddings”) of the text that preserve semantic meaning for every commit in the kernel’s history, making them easily comparable.

For human maintainers, the tools cuts down the number of commits that humans have to review. It even explains its reasoning in an email.

## Know Your Tools

Like any other tool, the value of an LLM corresponds to how well it is understood by it user.

You can think of [Large Language Models](https://thenewstack.io/how-to-generate-ai-from-a-database-bruce-momjian/) as the next generation of compilers, providing developers with a jump in productivity, Levin said. They act like “massive state machines,” though what is unusual about them is that they perform state transitions in a probabilistic, rather than deterministic, manner.

They are good at matching patterns given a huge number of parameters and an input provided by a user. A “temperature” parameter controls how probabilistic the LLM is, or how liberally it interprets its material.

## Other Uses

And like any other technology, LLMs are first being tested in minor tasks.

LLMs excel at “small, well-defined tasks.” Levin said.

One such use is code generation and refactoring. Tightly-defined bug fixes, or converting code to other forms, such as standard APIs, are good tasks.

For the 6.15 kernel release, Levin had an LLM write a patch to convert the open-coded hash table implementation to a standard API.

Linux kernel 6.16 included `git-resolve`. This tool resolves incomplete or incorrect commit IDs, a [nagging issue](https://lwn.net/Articles/1001526/) for core developers, though not one that occurs often enough to spend a lot of time manually writing a tool to figure out which commit an incomplete SHA-1 is actually connected to.

It took Levin all of 20 minutes to work with the LLM to create the tool.

It would take an engineer about half a day to create such a tool, making it not worth the effort given the relative rarity of the issue it addressed. Plus the LLM did a lot of extra credit: It created a set of self-tests and even documentation, which a human engineer would have done begrudgingly if at all.

There’s no end of clean-up tasks that could be done with the kernel, Levin said. An LLM could help non-native English speakers write descriptive commit messages.

## CVE Classification

Another tedious chore is classifying security vulnerabilities ([CVEs](https://thenewstack.io/vulnerability-management-best-practices-for-patching-cves/)), a task that the Linux kernel community took on in 2024.

The work involves inspecting commits to see if they address security issues.

Originally, a set of “hacky Bash scripts” was written to help.

LLMs were used to replace the scripts with a set of far more refined tools written in Rust, which included a full set of testing tools and documentation.

Using AUTOSEL as a launching point, a CVE classifier uses LLMs to identify commits that address security issues, and then goes on to check the vulnerability hasn’t already addressed in a previous patch. This is an overwhelming task for humans, given the 40 million lines of code that make up the [Linux kernel](https://thenewstack.io/learning-linux-start-here/).

LLMs can understand the semantic meaning of the commits, which provides for a far more comprehensive matching capability. A [Retrieval Augmented Generation](https://thenewstack.io/navigating-the-nuances-of-graphrag-vs-rag/) (RAG) cycle pulls in the kernel’s development history and documentation (e.g., Git repositories) to minimize hallucinations.

The LLMs effectively act as AI agents, Levin noted. They can run [git commands](https://thenewstack.io/how-to-make-git-a-developers-bff/), such as [`git blame`](https://git-scm.com/docs/git-blame), directly against the code repository to learn from the history of the kernel development itself.

In summary, AI has thus far helped Linux scale its maintenance efforts, while enhancing consistency and reducing manual labor for tedious tasks.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 25 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)