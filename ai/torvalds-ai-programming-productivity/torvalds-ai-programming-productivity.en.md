During his keynote at the recent [Open Source Summit North America](https://events.linuxfoundation.org/open-source-summit-north-america/), Linux and Git creator [Linus Torvalds](https://www.linkedin.com/in/linustorvalds/) did not mince words about those who contend AI will remove the need for human programmers.

Instead of AI “replacing” programming, Torvalds told the audience gathered in Minneapolis that AI boosts productivity in the same way that past technological revolutions did.

Programmers will ultimately use AI to generate the source code, which compilers then turn into machine code. However, to build serious projects intended to last decades, developers must deeply understand the generated code and the system architecture, not just the prompts, he clarified.

“AI is a great new tool, but it’s a tool, and when I see people saying, ‘Hey, 99% of our code is written by AI,’ I literally get angry, because those same people — I can pretty much guarantee — that 100% of their code is written by compilers. But they never say that.”

> “When I see people saying, ‘Hey, 99% of our code is written by AI, I literally get angry”

From the perspective of a long-time open-source maintainer — the first maintainer of Linux, as its creator — Torvalds views AI as a significant, high-productivity tool, similar to the historical shift from machine code to assemblers and compilers.

Torvalds dismissed the idea that AI might one day “replace” programming, arguing instead that it boosts productivity, much like past revolutions in software development. Torvalds emphasized that true software engineering requires, in the immediate future, human understanding of the underlying systems, not just the ability to write AI prompts.

> “I’m 100% convinced that AI is changing programming, but it’s not changing the fun.”

Programmers will ultimately use AI to generate the source code, which compilers then turn into machine code.  “I’m 100% convinced that AI is changing programming, but it’s not changing the fun,” Torvalds said.

As Torvalds mentioned during his keynote, he initially began programming by working with the bare-number machine language in the pre-assembly days. Then assembly languages came into play, and higher-level languages like Fortran, which used compilers, came along. And then, with compilers, productivity actually increased dramatically for basic programming.

AI can increase productivity by a factor of 10, but another way to look at it, according to Torvalds, is that AI-assisted productivity for programming is 10 times less than the productivity gains compilers offer. This assertion is based on Torvalds’ calculation of how compilers have boosted programming by 1,000-fold.

> “People who don’t understand the complexity of systems will also prompt systems and write processes that will fail. So,  I think you do want to understand how it all works.”

“People who know what they’re doing to understand systems will be able to prompt tools to write good code,” Torvalds said. “People who don’t understand the complexity of systems will also prompt systems and write processes that will fail. So,  I think you do want to understand how it all works.”

The immediate dilemma of AI-generated code in open-source projects is the explosion of AI-generated pull requests, often containing bugs that AI tools have found. The people power required to assess and then merge these fixes as commits has been doable for the Linux project for now, thanks to its resources. However, for those thousands of projects that lack resources, many cannot keep up the pace.

“Of all the projects that people maintain that are not the Linux kernel, that maybe is somebody’s head project that they’ve been working on for a decade or more, and they have only one person or three people [to patch bugs and create fixes], they get really burned out,” Torvalds said.

While AI helps identify deep-seated bugs in aging codebases, it also introduces a social burden: “Drive-by” AI bug reports that lack follow-up, causing maintainer burnout, Torvalds said.

Torvalds noted that the Linux project has over 35 years of legacy code and that AI is successfully finding hidden issues. However, it takes extensive time for maintainers to sift through those, Torvalds said.

![](https://cdn.thenewstack.io/media/2026/05/a4f5fd49-screenshot-2026-05-29-at-10.19.38-1024x641.png)

Credit: *The New Stack*

“Sometimes, obviously, AI reports a bug, and when you ask for more information, the person has done that drive-by and doesn’t even answer your question,” Torvalds said. ”So, that’s the real burnout issue.”

Additionally, some tech companies invest in making a name for themselves by using AI to flag bugs for media attention — without providing the necessary code patches. “These companies enjoy spending a lot of money and a lot of tokens on pointing out the above, and strangely, none of these came with a patch, even though all of these were in open source code,” Torvalds asserted. “It’s all very good when AI finds a bug in any source code in the short term, but if AI finds issues that we did not find, it’s going to take us some time to just work through the new issues.”

> “It’s all very good when AI finds a bug in any source code in the short term, but if AI finds issues that we did not find, it’s going to take us some time to just work through the new issues.”

The project maintainers saw a surge in pull requests ahead of the 7.1 release, resulting in more commits during preparation than in any previous release. However, it became apparent that the surge in pull requests was due to AI use rather than increased interest in the new release, as Torvalds initially thought.

Still, as he noted, contributing to the kernel is a good thing with AI, and that very difficult process has been largely supported and, in many cases, augmented with AI tools. As he noted, there was a roughly 20% increase in submissions overall with the current Linux kernel release.

During the Q&A, Torvalds was asked which AI tools the Linux project maintainers use to review pull requests and vulnerability reports, to which he replied, “Sashiko.” However, even with that tool, humans must still maintain and review the implementation or proposed fixes, which still requires a significant amount of manpower across the project.

That said, given the number of layoffs in the tech sector, the actual act of programming itself is changing, but humans, at least in the near- to mid-term, will still require significant expertise and remain in demand.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)