# Russ Cox’s Next Act: AI-Powered Help Agents for Open Source Projects
![Featued image for: Russ Cox’s Next Act: AI-Powered Help Agents for Open Source Projects](https://cdn.thenewstack.io/media/2024/09/8ffa6c69-github-profile-for-go-tech-lead-russ-cox-and-for-the-gaby-help-bot-he-created-1024x638.jpg)
Russ Cox’s next act looks like his last act, at least until his ChatBot replacement takes over.

When Cox [stepped down](https://thenewstack.io/russ-cox-steps-down-as-tech-lead-of-go-programming-language/) as the [Go language](https://thenewstack.io/how-golang-evolves-without-breaking-programs/)‘s [tech lead](https://thenewstack.io/what-made-golang-so-popular-the-languages-creators-look-back/) in September, “I am not leaving the Go project…” he emphasized in his [Aug. 1 announcement](https://groups.google.com/g/golang-dev/c/0OqBkS2RzWw).

But besides discussing designs, answering questions, advocating for Go, and filing issues “from time to time” — and “working on a few potential new standard libraries”— Cox will also be shifting focus to an interesting new Go-related project that he started up in June. And Cox’s larger goal is to help all open source maintainers with a tooling architecture that can “automate various mundane things that a machine can do reasonably well…”

“Maintainer toil is not unique to the Go project,” the [home page](https://pkg.go.dev/golang.org/x/oscar/internal/gaby) asserts points out, “so we are aiming to build an architecture that any software project can reuse and extend, building their own agents customized to their project’s needs.”

## May I Help You?
A [README file](https://github.com/golang/oscar/blob/master/README.md) on GitHub describes the code underlying the project as “an open-source contributor agent architecture” for “creating automated help, or ‘agents,’ for open-source maintenance.” They’ve named it OSCAR — an acronym standing for (O)pen (S)ource (C)ontributor (A)gent a(R)chitecture.

“Serving as a project search engine is still not the best use of the maintainer’s time,” notes Oscar’s README file. But an automated agent could always be standing by to instantly “surface related project context” from past issue reports (as well as pull requests/change lists, documentation, and forum discussions).

The README file acknowledges that the project “is very much an experiment.” But it notes that a first prototype of the contributor-helping agent has already performed “many” successful interactions for issues submitted for the Go programming language.

On June 7, Cox [announced the surprise launch of a first prototype agent](https://github.com/golang/go/discussions/67901#discussion-6793082) named Gaby — powered by Google’s Gemini LLM. Its first mission? Automatically adding a hyperlink when an issue mentions a specific changelist number. (Which led to Cox’s first change to Gaby — telling it to ignore pull requests and to focus only on editing *Issues*.)

The same day Cox taught Gaby to rewrite any Google-internal URLs that appeared in submitted issues, swapping in their public counterparts. And within a few days, more feature requests began appearing in the discussion…

![Screenshot of reactions to Gaby bot launch announcement on June 7 2024](https://cdn.thenewstack.io/media/2024/08/31a9193b-screenshot-of-reactions-to-gaby-bot-launch-announcement-on-june-7-2024.png)
Cox’s announcement of Gaby’s launch drew enthusiastic reactions – including 133 upvotes.

But Gaby’s biggest impact seems to be in automatically posting what it’s identified as “Similar Issues” when a new issue is submitted — “a list of at most ten highly related links that add context to the report.” (Cox’s June 7 announcement notes that Gaby only posts “if it finds any that are similar enough. If not, it will stay quiet.”) But he also noted that on Gaby’s first day of operation, its “similar” links had indeed correctly identified when duplicate Issues were being filed.

Gaby’s documentation notes that the agent’s responses proved to be “incredibly helpful.” One grateful contributor even began their [response](https://github.com/golang/go/issues/68196#issuecomment-2191837536) to Gaby with the words: “Good bot :)”

Within ten weeks, Gaby had [commented on nearly 600 different Go issues](https://github.com/golang/go/issues?page=9&q=is%3Aissue+is%3Aopen+commenter%3Agabyhelp) — 370 closed and another 216 open.

And soon Go’s issues had a new label available: “[gabywins](https://github.com/golang/go/issues?q=label%3Agabywins+is%3Aclosed)“.

## LLMs … or Not
“Posting about related issues is a limited form of analysis,” acknowledges the documentation for Oscar, “but we plan to add other kinds of semantic analysis, such as determining that an issue is primarily about performance and should have a ‘performance’ label added.

“We also plan to explore whether it is possible to analyze reports well enough to identify whether more information is needed to make the report useful.” Someday the agent could even recreate the bug in a sandbox to see which releases it affects — “and even use *git bisect* to identify the commit that introduced the bug.”

What else lies in the future? Possible “stretch goals” include labeling issues automatically or contacting maintainers for crucial changelists. (And there have already been some preliminary experiments with Gemini to see how it performs “selecting from and invoking available tools to satisfy natural language requests made by a maintainer”.)

“Another stretch goal might be to identify when an issue needs more information and ask for that information.” Although [Gaby’s documentation](https://pkg.go.dev/rsc.io/gaby) acknowledges bluntly that “There is no guarantee that today’s [Large Language Models] work well enough to build a useful version of that.” The final paragraphs of the documentation even raise the possibility of Gaby one day holding “interactive conversations”.

“Overall, we believe that there are a few good ideas for ways that LLM-based bots can help make project maintainers’ jobs easier and less monotonous, and they are waiting to be found.”

“There are also many bad ideas, and they must be filtered out. Understanding the difference will take significant care, thought, and experimentation. We have work to do.”

“Some aspects of the work may involve AI/LLMs; some will not.”

The project wryly notes that it also hopes to identify what LLMs “should not be used for.” But more importantly, “The guiding principle is to create something that helps maintainers and that maintainers like, which means to use LLMs when they make sense and help but not when they don’t.” So, for example, it stresses that its goal for the LLMs isn’t to have them replace programmers. “After all, writing code is the fun part of writing software.”

Instead, it envisions the possibility of LLMs becoming “a small (but critical!)” part of the interaction — “to focus on the not-fun parts, like processing incoming issues, matching questions to existing documentation, and so on…”

Oscar’s documentation even looks ahead to the day Gaby can be hosted on other platforms (like Google’s Cloud Run) so it can be integrated with GitHub’s event-based notification service webhooks. Gaby uses GitHub’s REST API to download the state of the issue tracker for source material (and it also uses project documentation), notes Oscar’s README file. “But the architecture makes it easy to add additional sources.”

## Charting a Path
In his Aug. 1 announcement, Cox shared his understanding of his role after 12 years as the tech lead for Go: “serving all of you, and trying to create the right conditions for all of you to do your best work.”

And he seems to be continuing that work in other ways — and not just for Go developers. Cox’s announcement added a hope that the Oscar-related work “will uncover ways to help open source maintainers that will be adopted by other projects, just like some of Go’s best ideas have been adopted by other projects.”

For now, the Oscar architecture “is being developed under the auspices of the Go project,” according to its README file. “At some point in the future it may (or may not) be spun out into a separate project…”

There was something poignant when Cox, speaking in general terms, wrote in his announcement that “my goals for Oscar are to build something useful,” but also to “learn something new” — and, to “chart a path for other projects.” Cox had added that “These are the same broad goals I’ve always had for our work on Go, so in that sense Oscar feels like a natural continuation.”

And by August 15, Cox had already made 13 commits to Oscar.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)