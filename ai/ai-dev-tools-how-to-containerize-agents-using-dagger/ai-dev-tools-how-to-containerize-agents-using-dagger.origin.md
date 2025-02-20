# AI Dev Tools: How To Containerize Agents Using Dagger
![Featued image for: AI Dev Tools: How To Containerize Agents Using Dagger](https://cdn.thenewstack.io/media/2025/02/f8b4d45f-agents-1024x667.jpg)
We’ll need to standardize the process of building [AI agents](https://thenewstack.io/ai-agents/), so why not look to the [container ecosystem](https://thenewstack.io/introduction-to-containers/) for inspiration?

This was the takeaway from a talk by [Docker](https://www.docker.com/?utm_content=inline+mention) creator and CEO of Dagger, [Solomon Hykes](https://www.linkedin.com/in/solomonhykes/), who spoke at Sourcegraph’s [AI Tools Night meetup](https://lu.ma/aidevfeb), held last week at the San Francisco Cloudflare headquarters.

“There should be a software ecosystem where we could reuse each other’s stuff,” Hykes said. “We propose Dagger as an ecosystem.”

[Dagger](https://dagger.io/blog/public-launch-announcement) is an [open source engine runtime](https://thenewstack.io/solomon-hykes-dagger-brings-the-promise-of-docker-to-ci-cd/) for software builds. Contributing DevOps engineers have [created](https://docs.dagger.io/quickstart/) thousands of modules, or [dags](https://dagger.io/blog/introducing-the-daggerverse), for [their own container build processes](https://dagger.dev/dev-guide/).
Dagger builds an immutable container chock full of specialized logic, and the design can easily be applied to building large language model-based agents, Hykes argued.

“All these startups selling you fancy infrastructure … well, basically, that is open source now,” he said.

And to demonstrate how easily containers make things go, Hykes built a simple AI agent, and in turn, built a [cURL clone](https://thenewstack.io/you-too-could-have-made-curl-daniel-stenberg-at-fosdem/), using only three function calls.

## We’ve Seen This Movie Before
The Docker container [was successful](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/) in no small part because it tamed the rapidly growing complexity of building web applications, Hykes recalled. Break the app into reusable components and containerize them for easy replication. Docker [brought](https://thenewstack.io/docker-at-10-3-things-we-got-right-3-things-we-got-wrong/) reusability and scalability.

“I propose we do the same thing for agents,” Hykes suggested. “Put those brains in a jar, then have some control over what they connect to.”

Adding the ability for external system calls into [LLMs](https://thenewstack.io/in-2025-llms-will-be-the-secret-sauce-in-software-development/) has been a [major groundbreaker](https://thenewstack.io/ai-agents-are-about-to-blow-up-the-business-process-layer/), and has quickly become an essential element to [building an AI agent](https://www.anthropic.com/research/building-effective-agents). They provide the protocol for an LLM to call an additional function if needed to complete a task.

As the number of agents proliferate, and the tasks they execute grow more complex, managing these agents will soon be become unwieldy.

## Dags All The Way Down
LLMs work just like a good immutable software build system, Hykes observed. They are bounded to an immutable state. You add data to the context window, and a function is executed.

Dagger has a new predicate called LLM, which is basically an empty state with [GPT-4o](https://openai.com/index/hello-gpt-4o/) loaded in (though it can use other models).

With either the Dagger shell or programmatically, you then can chain multiple operations together. The first of which could be, say, an initial prompt.

The entire Dagger API is a set of objects, each with its own set of function calls, schema and state. So, within the Dagger Shell, you can create a container object:

1 |
LLM | with-container (Container | from alpine | with-new-file yay.txt 'my favorite language is PHP') |
Executing the above example of creating a container object, Hykes added a file, yay.txt, to prove the veracity of his live demo.
In addition to creating the container, the command also connects it to the LLM itself, he noted.

From there, you can chain together multiple objects.

When the “build” is run, an [OpenTelemetry](https://thenewstack.io/how-to-make-sense-of-ios-user-activity-with-opentelemetry/) instrumentation can list all the steps it had taken, including how the LLM recovered from all the various errors (such as calling the wrong installation package) that the LLM will need to go through to complete its goals (which is also great for accountability).

Hykes also showed how, on first pass, the command to create the container had installed PHP into the container itself, so it would be available for subsequent use.

Chilling!

## cURL Clone in Three Functions
The bare minimum for an LLM workspace, Hykes advised, would at least be a container and a state, functions for reading and writing files, and a build function (ideally with no arguments).

Hykes wrote a dag with all these things, called [toy-workspace](https://daggerverse.dev/mod/github.com/shykes/melvin/toy-workspace@efce73bff57b24f54fcdfc387fb987dd99146f05).

In the demo, he installed toy-workspace into an LLM container. He added a rudimentary prompt for the LLM:

*You are an expert Go programmer.**You have access to a workspace.**Use the read, write and build tools to complete the following assignment:*
The user command is assigned to an @assignment variable.

He then had some final instructions:

*DO NOT USE CONTAINER TOOL.**Don’t build until your code builds.**The function is looped.*
Showing off his demo chops, Hykes then ran this very program, adding only the instruction, “Write me a cURL clone.” A minute later, he had a working cURL clone running.

“This is the magic of agent development,” Hykes said.

## Agent Debugging
[YK Sugi](https://www.linkedin.com/in/ykdojo/), the Sourcegraph senior AI developer advocate who organized the meetup, appreciated Dagger’s approach, especially for the debugging.
“As someone who’s built agents myself, I know that building AI agents can be a challenge,” he wrote in a LinkedIn message.

“Your errors could be coming from the LLM API that you’re using or whatever setup you have for your LLM,” he wrote. They could be rate-limiting issues or the syntax not matching the current version that’s available. It can be a pain to find the source of the issue.

“With agents, you might have a specific issue with the path that it’s trying to follow or maybe the syntax of the tool usage not being correct from the LLM output. Even if the LLM behaves the way you want it to, you might have problems with the backend services.”

Dagger’s ability to examine all of the logs, not just the ones from the LLM, but also from the ones from the backend services, could be a great help in this regard.

“It seems to make not just debugging simpler, but also development in general, so that it’s easier to develop a more reliable system,” he wrote.

The [entire evening](https://lu.ma/sourcegraph) of [Sourcegraph](https://sourcegraph.com/about)‘s AI Dev Tools Night [can be found here](https://www.youtube.com/watch?v=1HA9h1MnUy0).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)