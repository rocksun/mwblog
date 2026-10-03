**AI coding agents trying to work around a limitation** in GitHub’s command-line tool ended up publishing more than 13,000 internal images to public repositories, according to an incident report Glow Labs released this week. The company calls the incident PixelLeak.

Developers at more than 300 organizations were affected, including one of the world’s largest tech companies, a frontier AI lab, a major enterprise software vendor, and a Fortune 500 travel company, along with teams in cloud, healthcare, fintech, and government, and the exposed images are spread across more than 900 repositories.

None of it came from an attack, [Glow Labs](https://www.glow.io/blogs/how-ai-agents-exposed-developer-screenshots-from-leading-tech-companies) says the agents were completing tasks their developers had assigned them.

> None of it came from an attack, the agents were completing tasks their developers had assigned them.

The trigger was one of the most routine steps in frontend work. A developer finishes a UI change and asks the agent to attach before-and-after screenshots to the pull request, but GitHub’s [image attachment feature](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/attaching-files) was built for people working in the web interface, while coding agents operate through the text-based CLI, and GitHub’s CLI didn’t get an image attachment option until version 2.99.0 on September 1. When the agent couldn’t attach the images that way, it looked for another route to make them visible to reviewers.

Glow reproduced the behavior in its lab by asking an agent running Anthropic’s Claude Opus 5 in Claude Code to change the header color on a private Minesweeper project. The agent created a new public repository and pinned the screenshots to a commit there so reviewers could see them from the private pull request.

“GitHub cannot render images from a private repo in a PR description — its image proxy fetches anonymously, so anything committed here (branch, release asset, whatever) shows up broken for reviewers,” the agent reasoned.

“The only way to satisfy both ‘reviewers see the images’ and ‘nothing but index.html in the repo’ was to host the PNGs elsewhere, so I created a new public repo.” Glow says that reasoning was representative of what it found at many of the affected organizations.

> “The only way to satisfy both ‘reviewers see the images’ and ‘nothing but index.html in the repo’ was to host the PNGs elsewhere, so I created a new public repo.”

## What the screenshots exposed

The exposed material went well beyond interface tweaks. At a manufacturer with more than 100,000 employees, an agent working on an internal billing screen published screenshots to a public repository under the developer’s personal GitHub account. Those images included billing records from a utility company involved in the fix.

Because the repository lived under the employee’s personal GitHub account rather than the company’s organization, the security team never spotted it, and the images were still public when Glow made contact.

> Because the repository lived under the employee’s personal GitHub account rather than the company’s organization, the security team never spotted it, and the images were still public when Glow made contact.

## Why scanners missed the leaks

That case reflects a broader pattern, with Glow finding that 93% of the images were stored in repositories under employees’ personal usernames, putting them outside the reach of scans focused on company GitHub organizations.

Even where the images were visible, the tools teams rely on to catch leaks, such as secret scanners and static analysis, analyze code and text rather than image content, allowing screenshots of internal consoles to pass through undetected.

Roughly a third of affected organizations had developers using gitshot, an unvetted open-source tool for publishing screenshots during code review, and at several large companies, agents discovered the tool and used it on their own.

Glow found more than 100 public accounts exposing internal work through `_gitshot` tags, including development work from a frontier AI lab and, at one financial services firm, an internal treasury and settlement console, a withdrawal screen naming an institutional client and two screen recordings of its money-movement console.

Coding agents can [install tools and packages without anyone on the team vetting them first](https://thenewstack.io/aikido-ai-agents-security/), and gitshot shows what can happen when one of those tools gives an agent a path around existing controls.

## How one workaround spread

The incident became systemic once the workaround became a reusable instruction. At one software vendor, [agents serving multiple engineers began publishing review screenshots publicly](https://www.glow.io/blogs/how-ai-agents-exposed-developer-screenshots-from-leading-tech-companies) in early July, and within a week more than a dozen of them had encoded the approach as a skill applied to every development ticket.

Running that skill, the agents uploaded more than a thousand screenshots and screen recordings of the company’s product, along with written summaries of features that were weeks or months from release.

Agent skills have already become a [supply chain risk in their own right](https://thenewstack.io/ai-agent-skills-security/), and this case shows that a skill doesn’t need to be malicious to spread risk across an engineering team when a mistaken one propagates just as efficiently. Glow began notifying affected organizations on September 9, 2026, and believes others are also affected.

For teams running coding agents, triage comes first. Glow recommends starting with everyone who commits to your private repositories, including former employees, and reviewing their personal accounts; then checking releases and gists in addition to file listings, since images attached to a release can make the file view look empty. Remove anything that turns up everywhere it exists, and rotate any credentials or other secrets legible in the images.

> Remove anything that turns up everywhere it exists, and rotate any credentials or other secrets legible in the images.

After triage, the focus shifts to the agents and tools developers are actually using. Glow recommends removing tools like gitshot that haven’t gone through a security review, keeping git tooling up to date and requiring approval before an agent takes potentially risky actions.

Teams should also review the shared rules and instruction files their agents load, since that’s how a one-off workaround can become something agents repeat automatically.

## Runtime controls for coding agents

The control Glow says actually stops this behavior operates at runtime. Glow, which actually sells endpoint runtime protection, recommends a pre-execution hook that blocks or holds for approval any attempt to create a new public repository, push to a personal account instead of the company’s organization, push to a gist, or switch a repository from private to public.

These gates work best when they [sit outside the agent and evaluate the action itself](https://thenewstack.io/ai-coding-agent-security/), regardless of whether it came from careful reasoning or an injected prompt. An agent that cannot create a public repository has no way to improvise this particular escape.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)