[Godot Engine](https://godotengine.org/), the open-source alternative to game engines such as Unity, is rewriting its [contribution policy](https://contributing.godotengine.org/en/latest/pull_requests/pull_request_guidelines.html) to bar most AI-generated code from its repositories.

The move follows months of internal discussion at the [Godot Foundation](https://godot.foundation/), the non-profit that stewards the project, and comes as maintainers say they can no longer keep pace with a growing backlog of pull requests, many of them AI-authored.

However, the Foundation also notes that the strain isn’t just about managing a deluge of AI-generated slop — it’s about what reviewing a pull request is supposed to accomplish. Reviewing code, its argument goes, has always been a slog, but it also served as a way of training future maintainers, and that no longer holds once the contributor on the other end is a machine rather than a person.

> “AI contributions have the added pain of being demoralizing.”

As the Foundation puts it, “AI contributions have the added pain of being demoralizing,” given that feedback left on a pull request doesn’t change how a model behaves next time, and the Foundation says it can’t trust heavy AI users to understand their own code well enough to act on that feedback themselves.

“Reviewing PRs is already tedious work, but it is rewarding because reviewers generally feel that their efforts are contributing to educating a new contributor — who may become a future maintainer/reviewer),” the Foundation [writes](https://godotengine.org/article/contribution-policy-2026/). “If your feedback on PRs is just being absorbed by a machine and not going towards mentoring a potential future maintainer, it becomes much harder to justify spending your free time on PR review.”

> “Reviewing PRs is already tedious work, but it is rewarding because reviewers generally feel that their efforts are contributing to educating a new contributor.”

## Closing the gap

Autonomous AI agents and “vibe-coded” pull requests already trigger an automatic ban from Godot’s GitHub repository, according to the Foundation, though it isn’t currently written into Godot’s published contribution guidelines. This new update, which is currently still a work-in-progress, will go further: it closes that gap by prohibiting AI from generating any substantial piece of code, whether the request comes from a bot or a human pasting in AI output — even if the human then reviews and discloses it.

Contributors can still use AI for narrow, low-stakes tasks such as code completion, regex, or find-and-replace, provided they disclose it in the pull request. AI-generated text in discussions with maintainers is also off-limits, aside from machine translation of human-written text.

Notably, new contributors, defined as anyone with three or fewer merged pull requests, must now get explicit sign-off before submitting new features or large refactors.

## ‘Contributor poker’

Godot’s mentorship argument isn’t entirely new to the open source realm. Back in April, [systems programming language Zig](https://thenewstack.io/introduction-to-zig-a-potential-heir-to-c/) adopted a [similar zero-tolerance policy](https://kristoff.it/blog/contributor-poker-and-ai/) for AI-assisted contributions, with Zig Software Foundation VP of Community [Loris Cro](https://kristoff.it/) arguing that the entire point of reviewing a pull request is to invest in the person submitting it, not just the code itself. He calls this dynamic “contributor poker,” writing that “in contributor poker, you bet on the contributor, not on the contents of their first PR” — an idea he borrows from the poker maxim “you play the person, not the cards.”

An AI-generated pull request breaks that calculation entirely, Cro argues, since a maintainer’s review time does nothing to build a future contributor if there’s no person on the other end learning from it.

Other projects, including the terminal emulator [Ghostty](https://github.com/ghostty-org/ghostty/pull/10412) and the C library [curl](https://daniel.haxx.se/blog/2025/07/14/death-by-a-thousand-slops/), have restricted or shut down parts of their contribution pipelines over the same underlying problem, with reasoning that has focused more on review burden and false bug reports than on mentorship specifically.

## The talent pipeline

Godot and Zig’s policies sit alongside broader concern about AI’s effect on the junior talent pipeline in software, and the underlying worry is much the same, just playing out at a different point. The corporate version of that worry is about entry-level jobs disappearing because AI now does tasks once assigned to junior developers.

As *The New Stack* [reported in April](https://thenewstack.io/agentic-ai-junior-developer-crisis/), Microsoft’s Mark Russinovich and Scott Hanselman [warned](https://cacm.acm.org/opinion/redefining-the-software-engineering-profession-for-ai/) that once companies lean on senior engineers paired with AI tools instead of hiring junior developers, “the profession’s talent pipeline collapses, and organizations face a future without the next generation of experienced engineers.”

> “We need to take steps to reduce the burden on maintainers while ensuring we still have a pipeline to mentor new contributors to become future maintainers.”

The open-source version of that same problem shows up even without anyone being shut out of a job. Junior contributors are still present and still willing to submit code — but if that code was written by AI rather than by them, the maintainer’s feedback still has nowhere to land, and the informal pipeline that turns a first-time contributor into a future maintainer stops functioning just as it would if the contributor had never shown up at all.

The Godot Foundation said it expects to keep revisiting the policy as AI tools change, describing its current approach as “conservative”.

“We need to take steps to reduce the burden on maintainers while ensuring we still have a pipeline to mentor new contributors to become future maintainers,” the Foundation says.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)