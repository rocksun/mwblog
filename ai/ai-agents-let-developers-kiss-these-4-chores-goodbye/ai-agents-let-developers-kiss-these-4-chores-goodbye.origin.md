# AI Agents Let Developers Kiss These 4 Chores Goodbye
![Featued image for: AI Agents Let Developers Kiss These 4 Chores Goodbye](https://cdn.thenewstack.io/media/2025/05/c00d132d-ai_programming_buddy-1024x579.jpg)
The developer focus on AI has been very tactical, the CEO of [All Hands AI](https://www.all-hands.dev/), [Robert Brennan](https://www.linkedin.com/in/robert-a-brennan/), told developers at the [Infobip Shift Conference](https://shift.infobip.com/), hosted earlier this month in Miami. All Hands AI creates open source [AI agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) for use in software development.

Tactical deployment means AI is primarily performing auto-complete in an IDE, he said.

“You’re in your IDE, you’re actively working on a problem, and the AI is basically — wherever your cursor is pointed — it’s predicting the next few lines of code as an autocomplete,” he said.

It’s super-useful, he admitted — but AI can do more to become a coder’s best friend, he explained during his presentation of how he uses AI in programming.

All Hands AI created [OpenHands](https://github.com/All-Hands-AI/OpenHands), an MIT-licensed, large language model-powered software development agent that can write code, run commands, browse the web, and even solve GitHub issues.

More recently, this month All Hands announced a collaboration with [Mistral](https://thenewstack.io/gemma-google-takes-on-small-open-models-llama-2-and-mistral/) AI, which led to the release of an open source model for [coding agents called Devstral](https://www.all-hands.dev/blog/devstral-a-new-state-of-the-art-open-model-for-coding-agents).

“Software Engineers, it’s very clear at this point that how we were working two years ago is not how we’re working today,” Brennan said. “And how we’re going to be working two years from now is going to look very, very different. We think it’s really important that the software engineering community have a say in what that change looks like, that we have a say in what our jobs look like two years from now.”

Brennan believes an open source approach will unlock those valuable future AI use cases for software development.

“You’re giving one or two lines of English to an agent saying, please refactor this file, please add a unit test, please fix the merge conflicts on this PR; and the agent goes off and works for 5, 10, 15 minutes on its own, without needing supervision, then [it] comes back to you with an answer,” he said. “In the meantime, you can be focused on a different coding task. You can be talking to your teammates on Slack. You can be goofing off on Reddit.”

## Breaking Down AI Agents: Agentic Loops
But before developers can get to living that particular dream, there’s work to be done.

At their core, AI agents run on agentic loops, Brennan explained. That’s basically a cycle between a [large language model](https://thenewstack.io/7-guiding-principles-for-working-with-llms/) — which provides the “brains” or “engine” for the AI — and the external world, where the agent acts.

“The basic loop is we ask the LLM, ‘What’s the next action you can take?’” he said.

That action may be browsing a web page to find documentation, running a command, or reading and editing a file. Once the LLM returns the work, the software developer feeds that back into the LLM for the next step of the loop. Basically, the developer keeps turning that loop until finally the LLM says it’s finished the tasks, he said.

“Digging into these actions a little bit more, there’s a lot of interesting stuff that happens under the hood to allow software development agents to really do the job well,” he said.

In the early days of code editing, the naive implementation was to stick the entire file that it wanted to edit into the LLM and get back an entirely new version of the file, he explained. That meant using more tokens, which made it expensive, slow and error-prone. The agent might replace all the tabs and spaces, or forget lines.

“Now there’s much more sophisticated strategies to do diff-based file editing or a string ‘find and replace’ — modern agentic frameworks have a much more sophisticated solution for file editing,” he said.

“With OpenHands, we’ve taken the decision that, by default, the agent is always running in a sandbox. It’s got a Docker runtime, where it has its own file system and has its own terminal. ”

— Robert Brennan, CEO of All Hands AI
A lot of agentic tooling will run locally on your laptop, he said. It’s also running inside your terminal, which he acknowledged can be a little bit scary. That’s why permissioning becomes very important in using AI agents, he said.

Usually, AI agents run with some kind of confirmation mode — when the agent says it wants to run a command, a developer has to hit the Y button before it can proceed one step further. That can be a little tedious because it’s reverting back to tactical mode, he added.

OpenHands found a workaround that will even protect you from it running the `/rmrf`
Linux command that forcefully and recursively deletes files and directories.

“With OpenHands, we’ve taken the decision that, by default, the agent is always running in a sandbox,” he said. “It’s got a Docker runtime, where it has its own file system and has its own terminal, even if it tries to run /rmrf, it’s not going to screw up your file system, and that allows the agent to be much more autonomous and run unsupervised.”

That leads to considerations such as what sorts of credentials should an AI agent be given access.

“Do you want to give it API keys?” He asked. “Maybe you want it to be able to read from an S3 bucket, but you don’t want it to just be able to take down your production Kubernetes cluster.”

## AI Microagents
He also shared a bit about microagents, which are one way to break down larger AI tasks into smaller tasks that can be given to specialized microagents to solve autonomously.

The practical challenge for enterprises lies in making microagents reliable, secure and tailored to specific workflows. Tooling is still evolving, but a few Brennan specifically mentioned were [Cursor Rules](https://docs.cursor.com/context/rules), available in the AI-powered code editor, or a clon.md file, which is a markdown file containing specific instructions or policies used within an AI or Machine Learning context, specifically within the [mlem.ai framework](https://github.com/iterative/mlem.ai/blob/main/content/docs/command-reference/clone.md).

## Developer Use Cases for AI Agents
Brennan highlighted some of his favorite use cases for AI agents and microagents:

**1. Resolve Merge Conflicts**
“This is my least favorite thing to do as a developer,” he said. “I’ve got a PR that’s been approved, the tests are passing, it’s ready to go but then somebody else edits the same file that I’ve edited and Git can’t automatically resolve the merge.” This requires that he sort through the old code and the new code to try to get it merged.

“It’s a very rote task, not a lot of creativity involved, and it’s something that AI does exceptionally well,” he said. “So now anytime there’s a merge conflict, I just ask the AI to do it for me.”

As a result, he hasn’t actively manually resolved merge conflicts in months.

**2. Address PR Feedback**
“Somebody else has already given a very clear description of what they want,” he said.

In doing so, they’ve basically written the prompt for you. He advises the AI to fix it and immediately addresses their feedback. “I’ve also asked it to fix the merge conflicts simultaneously,” he said.

**3. Infrastructure Changes**
AI can deal well with infrastructure changes, he added. Helm is a popular package manager for Kubernetes.

“This is another one of my favorite tasks, because I hate working with TerraForm and Helm usually involves some like, weird, esoteric change that needs to be made to go hunting around the documentation for some Helm chart, etc.,” he said. “Again, one that the agent tends to do very well.”

He uses OpenHands to fix memory problems because the AI is great at following all the best practices around building databases and migrations, he said.

**4. Testing**
Brennan also uses OpenHands AO to fix failing tests and expand test coverage.

“This is really great because there’s a very clear definition of done: Tests are failing,” he said. “The AI can basically just iterate, changing the code or changing the tests, until it gets to a point where it can run that command and it passes with exit code, zero.”

It can also expand tests if there’s an area of your code base that’s completely uncovered by tests, he added.

“This is just a very easy, quick win for working with agentic AI […] it can just iterate until the tests are passing,” he said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)