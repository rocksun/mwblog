# The Python Linter Ruff Is a Win for Open Source — and Rust
![Featued image for: The Python Linter Ruff Is a Win for Open Source — and Rust](https://cdn.thenewstack.io/media/2024/07/3806fa61-ruff-1024x683.jpg)
Astral Software [describes its mission](https://astral.sh/about) as “high-performance developer tools for the Python ecosystem, starting with Ruff, an extremely fast Python linter, written in Rust.”

And the same page also includes this statement of a larger mission from Astral founder, [Charlie Marsh](https://www.linkedin.com/in/marshcharles/). “To me, the response to Ruff is itself evidence of an opportunity: to make the Python ecosystem more productive by building high-performance developer tools.”

One thing’s certain: it’s been a whirlwind journey. Last October Marsh noted in [a blog post](https://astral.sh/blog/the-ruff-formatter) that “A little over a year ago, I made the first commit to Ruff, an extremely fast Python linter, written in Rust. Since then, Ruff has grown to millions of downloads per week with support for hundreds of lint rules, serving as a drop-in replacement for dozens of tools like Flake8, isort, and pyupgrade.”

It’s been a fast success, and Ruff offers a good example of taking inspiration from other parts of the programming world, and then thinking about what it is that developers really want.

And along the way, Charlie Marsh has also learned a lot about life in the fast lane of open source development…

## An Open Source Journey
That October blog post was announcing the launch of Ruff’s Python formatter — their first non-linter tool — stressing that a unified tool chain is their ultimate north star. But the formatter’s release was also a milestone: the first tool built [collaboratively by a team](https://thenewstack.io/distributed-teams-distributed-applications-collaboration-in-a-cloud-native-world/). “The first draft of the Ruff linter was written by me, in a cave,” Marsh joked. (Adding “We’ve now grown to a core team of five, with over 290 contributors.”)

In a very short time, Ruff has become a true open source success story. In [April of 2023](https://astral.sh/blog/announcing-astral-the-company-behind-ruff) Marsh called Ruff “my first experience as an open source maintainer at scale, and it’s been an intentional goal of mine to create a project and an environment that’s welcoming to both new and existing contributors.”

And in a [recent interview on the Software Engineering Daily podcast](https://softwareengineeringdaily.com/2024/06/12/ruff-and-next-generation-python-tooling-with-charlie-marsh/), Marsh said Ruff has now built “a strong and sustainable contributor base. You’ve actually had a lot of contributors who it’s their first-time writing

[Rust](https://thenewstack.io/rustlangs-semantic-versioning-still-breaks-too-many-apps/), and they see Ruff as an interesting entry point for them.”

There’s a conscious effort to make it a welcoming community, Marsh added. “So, you know, trying to have good contributor documentation, being willing and able to mentor people who come in and write Rust for the first time, and give them feedback, and kind of coaching them through it. Those are all things that we try to do.”

After graduating from Princeton, Marsh admits he was “more of a consumer of open source than a maintainer.” So the experience of launching Ruff became “a crash course in what it’s like to be a maintainer,” he said on the podcast.

Though it started with a handful of users, the user base has grown so dramatically that “everything we ship gets feedback and gets tested within five minutes.”

Marsh laughed and admitted that he preferred the earlier stage, which was more fun — since he’s learned that building software is harder when you have to maintain compatibility for your user base. “It’s like, with great power comes great responsibility.”

But he also described this mature stage as “very rewarding” — and he appreciates the constant feedback from users.

Issues are good. Issues means people are using it.

— Charlie Marsh (@charliermarsh)

[May 31, 2024]
“It’s part of what makes open source, I think, really fun… You have this direct relationship with users that just doesn’t really exist in the same way in a lot of other categories of software.”

## Origin Story
Marsh founded Astral in October of 2022, after four and a half years as a software engineer at Spring Discovery, a company with a machine learning-based platform of tools for clinical research. Before that Marsh was a [senior software engineer](https://thenewstack.io/what-it-takes-to-become-a-senior-engineer/) at Khan Academy, where he worked on their iOS and Android apps, he said during the podcast — plus a Python-based web app, and a web frontend which used “a lot of React.

“I’ve kind of inadvertently spent my career jumping between programming ecosystems,” Marsh told JetBrains [in 2023](https://blog.jetbrains.com/pycharm/2023/02/ruff-python-linter-interview-with-charlie-marsh/), adding that “Moving between these ecosystems has really influenced how I think about tooling. I see something that the web does well, and I want to bring it to Python, or vice versa. Ruff is based on many of those observations…”

For example, the web ecosystem obviousy had more non-JavaScript tooling. And on the podcast, Marsh said he also knew Python had really good tie-ins with Rust, “a very good ecosystem of tooling that enables Rust-Python bridging in different ways.”

One thing led to another, and five months after Ruff’s launch, it had been adopted as the primary linter for top Python projects including Pandas, FastAPI, Apache Airflow, according to a [blog post by Marsh](https://notes.crmarsh.com/ruff-the-first-200-releases). (The post notes that Ruff’s first version supported 20 lint rules, but five months later it [supported 376](https://github.com/charliermarsh/ruff#supported-rules). Plus, it had also added an official VS Code extension, and an official Language Server Protocol…)

And by April of 2023, Astral Software was announcing plans “to continue building high-performance developer tools for the Python ecosystem” — with [$4 million in seed funding](https://astral.sh/blog/announcing-astral-the-company-behind-ruff) raised from investors like Accel, Caffeinated Capital, and even Docker founder Solomon Hykes. “In short, we’re going to take the ideas behind Ruff to their extreme by (1) expanding Ruff itself and (2) building more Ruff-like things.” (The business plan was “build and sell services on top of our tools” while “the tools themselves will remain free and open-source.”)

By then Ruff had already reached over 1 million downloads a month, with Marsh [blogging](https://astral.sh/blog/announcing-astral-the-company-behind-ruff) that major companies like [Microsoft](https://news.microsoft.com/?utm_content=inline+mention), [Amazon](https://aws.amazon.com/?utm_content=inline+mention), Netflix, Mozilla, and Hugging Face had adopted Ruff. “Many established projects and companies now rely on Ruff to write code every day.

“I view that as both my greatest source of motivation and my most significant responsibility. Thank you for your trust. I won’t let you down.”

## Performance — and More
Astral continues expanding its line of free tools. In February, the company [announced uv](https://astral.sh/blog/uv), described as “an extremely fast Python package installer and resolver, written in Rust, and designed as a drop-in replacement for pip and pip-tools workflows.”

Announcing uv: an extremely fast Python package installer and resolver, written in Rust.

uv is designed as a drop-in alternative to pip, pip-tools, and virtualenv.

With a warm cache, uv installs are near-instant. Here, it’s > 75x faster than pip and pip-tools.

[pic.twitter.com/wrvaudUn6i]— Charlie Marsh (@charliermarsh)

[February 15, 2024]
And of course, Astral continues to update Ruff. As of [May 22nd](https://astral.sh/blog/announcing-astral-the-company-behind-ruff), Ruff ships with the beta version of a new built-in Language Server (written in Rust) offering the same features as their older [ruff-lsp](https://pypi.org/project/ruff-lsp/0.0.9/) implementation.

But when asked on the podcast for Ruff’s selling points, Marsh had a ready answer. “The flagship feature is performance. The second is simplicity.” But a third feature is what he calls “adoptability”. “We just had a really strong focus on making it easy to adopt… [F]rom the start, we basically mapped our rules back to existing other linters, so that when people migrate they should see effectively the same sets of violations. That’s been a really helpful thing, because people moving from project to project — they already recognize the rules. They’re already familiar with them. Their projects are probably already in compliance with them.”

Marsh noted that Python had a lot of different tools, and “sort of by accident… we ended up consolidating a lot of tooling into one.” So while their main goal was performance, Marsh thinks that’s been “one of the most impactful things for users… [W]hen people migrate to Ruff, they’re often replacing, like 20 or 30 tools with one.”

And in addition, “a lot of our rules ship with auto-fixes… We’ll do code transformations to try and fix them automatically.”

## Future Features
During the interview, Marsh also noted that the tool “is just very much in flux,” while they’re developing it “pretty aggressively.” And then he gave some clues about Ruff’s future. Marsh said he’s “quite interested” in someday supporting the ability to let users customize the linter’s rules and to see Ruff doing type inference and analysis and inference, across files. Being able to work across files “matters a lot for language servers,” Marsh pointed out later calling it something “we’re going to be thinking about over the course of the next year, basically… growing Ruff into something that can deal with analysis across multiple files, that can do really smart type inference in Python, that can support really good in-editor experiences.”

Marsh was asked an interesting question: how will linting change in the next 5 to 10 years — especially with AI enhancements coming to many dev tools. And he had an interesting response — that things like static analysis tools become even more important if machines are generating code. “If people are generating more code, I think the value of tools that are consistent, and explainable, and reliable, actually potentially goes up. Like, if you have a bunch of *generated* code, the idea of having a linter to enforce consistency and style and correctness, I think is actually more important, potentially than it is today.”

Marsh has seen “interesting explorations” of [Large Language Model](https://thenewstack.io/why-large-language-models-wont-replace-human-coders/)-powered linters, where plain-text descriptions or examples input by users are then applied to an entire codebase.

Marsh even built a prototype once — before concluding that “in my experience, most people actually don’t want to be writing their own lint rules. That’s actually a lot of the value of a linter, I think…

“You’re putting together a curated and opinionated set of rules… Most people don’t want to sit down and develop their own taxonomy of rules — even if it was made very easy to do so.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)