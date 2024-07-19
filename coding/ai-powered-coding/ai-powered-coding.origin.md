I am by no means a skilled coder, but thanks to a free program called [SWE-agent, I was](https://github.com/princeton-nlp/SWE-agent) just able to debug and fix a gnarly problem involving a misnamed file within different code repositories on the software-hosting site GitHub.

I pointed SWE-agent at an issue on GitHub and watched as it went through the code and reasoned about what might be wrong. It correctly determined that the root cause of the bug was a line that pointed to the wrong location for a file, then navigated through the project, located the file, and amended the code so that everything ran properly. It’s the kind of thing that an inexperienced developer (such as myself) might spend hours trying to debug.

Many coders already use [artificial intelligence](https://www.wired.com/tag/artificial-intelligence/) to write software more quickly. GitHub Copilot was the [first integrated developer environment to harness AI](https://www.wired.com/story/openai-copilot-autocomplete-for-code/), but lots of IDEs will now automatically complete chunks of code when a developer starts typing. You can also ask AI questions about code or have it offer suggestions on how to improve what you’re working on.

Last summer, John Yang and Carlos Jimenez, two Princeton PhD students, began discussing what it would take for AI to become a real-world software engineer. This led them and others at Princeton to come up with [SWE-bench](https://www.swebench.com/), a set of benchmarks for testing AI tools across a range of coding tasks. After releasing the benchmark in October, the team developed its own tool—SWE-agent—to master these tasks.

SWE-agent (“SWE” is shorthand for “software engineering”) is one of a number of considerably more powerful AI coding programs that go beyond just writing lines of code and act as so-called software agents, harnessing the tools needed to wrangle, debug, and organize software. The startup Devin went viral with [a video demo](https://www.youtube.com/watch?v=fjHtjT7GO1c) of one such tool in March.

Ofir Press, a member of the Princeton team, says that SWE-bench could help OpenAI test the performance and reliability of software agents. “It’s just my opinion, but I think they will release a software agent very soon,” Press says.

OpenAI declined to comment, but another source with knowledge of the company’s activities, who asked not to be named, told WIRED that “OpenAI is definitely working on coding agents.”

Just as GitHub Copilot showed that [large language models can write code and boost programmers’ productivity](https://www.wired.com/story/openai-copilot-autocomplete-for-code/), tools like SWE-agent may prove that AI agents can work reliably, starting with building and maintaining code.

A number of companies are testing agents for software development. At the top of the SWE-bench leaderboard, which measures the score of different coding agents across a variety of tasks, is one from [Factory AI](https://www.factory.ai/), a startup, followed by [AutoCodeRover](https://autocoderover.dev/), an open source entry from a team at the National University of Singapore.

Big players are also wading in. A software-writing tool called [Amazon Q](https://aws.amazon.com/q/) is another top performer on SWE-bench. “Software development is a lot more than just typing,” says Deepak Singh, vice president of software development at Amazon Web Services.

He adds that AWS has used the agent to translate entire software stacks from one programming language to another one. “It’s like having a really smart engineer sitting next to you, writing and building an application with you,” Singh says. “I think that’s pretty transformative.”

A team at OpenAI recently helped the Princeton crew improve a benchmark for measuring the reliability and efficacy of tools like SWE-agent, suggesting that the company might also be honing agents for writing code or doing other tasks on a computer.

Singh says that a number of customers are already building complex backend applications using Q. My own experiments with SWE-bench suggest that anyone who codes will soon want to use agents to enhance their programming prowess, or risk being left behind.

- The Big StoryPriscila, Queen of the Rideshare MafiaBy Lauren Smiley
- ScienceEverything You See Is a Computational Process, If You Know How to LookBy Lance Fortnow
- SecurityHackers Claim to Have Leaked 1.1 TB of Disney Slack MessagesBy Lily Hay Newman
- GearThe Paris Olympics Will Show Us the Future of Sports on TVBy Boone Ashworth