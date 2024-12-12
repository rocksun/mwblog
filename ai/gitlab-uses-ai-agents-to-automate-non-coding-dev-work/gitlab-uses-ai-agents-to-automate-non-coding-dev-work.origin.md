# GitLab Uses AI Agents To Automate Non-Coding Dev Work
![Featued image for: GitLab Uses AI Agents To Automate Non-Coding Dev Work](https://cdn.thenewstack.io/media/2024/12/0cefaa67-ai-assistants-1024x631.jpg)
Most AI offerings target helping the developer code — but [GitLab](https://about.gitlab.com/) is taking a different approach with its artificial intelligence agents, using them to automate everything that supports the code base, such as documentation, merge requests, security and compliance tasks.

Last week at AWS re:Invent, GitLab and [Amazon Web Services announced the integration of GitLab’s AI-powered assistant, GitLab Duo, with ](https://aws.amazon.com/?utm_content=inline+mention)[Amazon Q,](https://thenewstack.io/amazon-q-a-genai-to-understand-aws-and-your-business-docs/) an AI assistant developed for enterprise use. This will allow developers to use Amazon Q autonomous agents.

The integration is now available in preview to GitLab Ultimate tier customers on self-managed subscriptions.

The New Stack spoke with [Emilio Salvador](https://thenewstack.io/author/emilio-salvador/), GitLab’s vice president of strategy and developer relations, about what this means for developers, development teams, and the software life cycle.

“It’s part of the GitLab UI, so you invoke the agents within the tools you use on a daily basis,” Salvador said. “Our goal here is to meet developers where they are and make the entire developer experience as seamless as possible.”

## A 360 Degree Software Development Life Cycle
Traditionally, software development has been a linear journey. AI agents will change that, Salvador said.

“You start with planning, and once your app is deployed, you’re done, right?” he said. “When there’s a problem, someone says, ‘Oh, there’s a problem,’ and everyone basically also tries to figure that out, and takes forever to find out where the problem came from.”

The process is reaction-based, but AI can change that. Salvador sees two things happening as AI agents are integrated into the process.

First, the software development loop is closing. Developers will have information from applications that are running in the cloud from systems that monitor the applications, detect problems, and connect the problems back to the developer.

“It’s a 360 [degree] software development life cycle when planning and deploying happens all the time and much faster than it happened before,” he said.

Second, there will be not just one AI agent but an ecosystem of AI agents that help developers in many different tasks across different languages, business segments and industries.

“What I see is that there’s going to be [a] gazillion small agents that will talk to each other and will be specialized to the tasks at hand,” he said.

## AI From the GitLab UI
Developers can type their requirements on a GitLab issue and invoke the Q agent through a Quick Actions, which are text-based shortcuts that allow developers to perform common actions directly within comments or descriptions of issues, merge requests, and epics. The agent then creates an entire project with a code base.

It can do 80% of the work for developers, Salvador added. However, unlike code assistants, which focus on code creation, AI agents handle many tasks that take developers away from coding.

“Basically, what it’s going to help developers [do] is focus on the things that matter most — solving business problems, working on business logic, and removing from the equation all those mundane tasks that developers don’t like to do,” Salvador said.

The tasks that Q AI agents can assist with are:

- Creating a project, including the files and headers for the project;
- Generating unit tests for new merge requests;
- Enforcing consistent quality assurance practices across teams;
- Providing security, compliance and code quality reviews; and
- Modernizing Java code.
## Modernizing Code
While it’s only available for Java at this time, the AI can take Java 8 or Java 11 code and with a click bring it up to Java 17. It can scale to thousands of lines of code, he said.

“It’s a 360 software development life cycle when planning and deploying happens all the time and much faster than it happened before.”

— Emilio Salvador, GitLab vp of strategy and developer relations
“That’s all that work in the background, no humans involved; [it] grants all the tests, grants all the pipelines, and if the agent encounters a problem, then [it] basically requests feedback from the user,” he said. “Things that in the past used to take weeks, if not months, now can be done in minutes or hours.”

There are plans to expand that functionality. Indeed, AWS announced last week that its [AI agents can now migrate .Net code to Linux](https://thenewstack.io/aws-launches-new-ai-agents-to-simplify-legacy-migrations/), a capability that Salvador said will eventually become available as part of the [GitLab integration](https://about.gitlab.com/blog/2024/12/03/gitlab-duo-with-amazon-q-devsecops-meets-agentic-ai/).

## The Development Team
“Development is a team sport, right?” Salvador said. “Eventually, if you happen to have the ball, using a sports analogy, is that there are other players that eventually you need to work with, because no single developer completes the entire process by himself or herself.”

The AI doesn’t just help developers: It helps the communication across different teams, he added. It “understands” when something happens and knows the right person to reach out to, he said. He compared it to a super assistant that’s able to see across the development life cycle.

“Let’s say, for example, that I’m developing code, I finish my code, I commit the code, and then eventually there’s a problem with code quality or security or whatever. Then all of a sudden, that is detected by one of these agents,” he said. “When there’s a problem, the agent knows who to reach out to in order to get work fixed.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)