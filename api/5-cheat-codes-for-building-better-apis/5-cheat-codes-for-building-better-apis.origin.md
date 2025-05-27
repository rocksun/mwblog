# 5 ‘Cheat Codes’ for Building Better APIs
![Featued image for: 5 ‘Cheat Codes’ for Building Better APIs](https://cdn.thenewstack.io/media/2025/05/9c3e61d2-matthew-voget-apis-2-1024x576.jpg)
A staggering amount of Internet traffic — in the 70-80% range, depending on whose data you believe — comes from API calls.

But while 85% of developers report building or maintaining RESTful APIs, only about 50% of devs surveyed say they use [OpenAPI specs](https://thenewstack.io/openapi-initiative-new-standards-and-a-peek-at-the-roadmap/), [according to 2023 data](https://www.getambassador.io/blog/conquer-api-rainbow-road-level-dev-cheat-codes) from Postman, the API platform company.

What does this mean? A lot of red flags, according to [Matthew Voget](https://www.linkedin.com/in/matthew-voget-47a225a1/), vice president of engineers at [Ambassador](https://www.getambassador.io/?utm_content=inline+mention).

“We’ve got too many APIs and not enough specs,” Voget said in a presentation this past Thursday at [APIDays New York](https://www.apidays.global/new-york/).

Add to this situation the emergence of the [Model Context Protocol (MCP)](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/), an open source standard that aims to streamline how AI models and APIs interact. The analyst firm Gartner, he noted, has “reported that 80% of enterprise AI agent frameworks are going to be using an MCP side style of service discovery by 2028.

“So add that kind of third layer into this, what do you get?” Voget asked. “You have a lot of APIs, a lot of traffic on the internet done through APIs, and potentially a lot of AI agents using these APIs.”

With [a flood of AI agents using these APIs](https://thenewstack.io/its-time-to-start-preparing-apis-for-the-ai-agent-era/) that lack standardized specs, an “even bigger red flag” is raised, Voget said. “How do you know what type of data is being accessed by these AI agents, if you don’t have high-quality API specs to tell you how that interaction behaves?”

The current situation comes down to two main challenges, he said: a lack of API specs and insufficient development loops. To help developers overcome these obstacles, Voget offered the APIDays audience five “cheat codes” for building better APIs in the AI agents era.

## Missing Specs, Development Loops
Building APIs without OpenAPI specs can hold organizations back from taking full advantage of [AI agents ](https://thenewstack.io/ai-agents/)and related innovations, Voget suggested.

“I’ve already seen half a dozen companies out here saying that they’ll convert your open API specs into MCP servers,” he said. “You can’t do that unless you have an open API spec.”

And those missing API specs, Voget said, can present other, more potentially hazardous vulnerabilities than simply missing out on the latest and greatest. “You might run into bugs due to untested code or unvalidated APIs. You might have integration issues between your APIs.”

Security gaps are also a big concern in such cases, he said. “You might not know that an API is protected or not protected if you don’t have it described in the spec and poor [developer experience]. This is not only true for humans interacting with your APIs, but also for AI agents.”

Development loops — the process through which APIs go when being developed — can also present challenges, Voget said.

He presented a model for software development with “outer” and “inner” loops. “The inner loop you can think of is something a developer is going to have to do multiple times a day, when maybe building out a new API or building a feature,” Voget said. “They’ll write code, they’ll build that, they’ll test their code locally. Typically, they’ll debug and then finally commit.

“And then that will enter the outer loop, where they’ll do things like run a CI workflow, do integration testing, and deploy, eventually, to production. And so if you think about it, the inner loop ought to be really fast, because developers are going to execute this multiple times. They’re going to do quick validation, especially if they’re using AI code generation tools.”

But this model for software development requires trade-offs that have an impact on developer productivity, he added: speed versus quality, autonomy versus skills.

“Sometimes it’s tough to find that unicorn developer who can do it all,” he said. As a result, “We often kind of silo these teams. We’ve got the DevOps or platform team, and then we’ve got our dev feature teams, but those siloed teams can lead to inefficiencies, especially when a developer needs to deploy something to a hosted environment or a remote environment to test something out.”

## Cheat Codes for APIs
To help overcome the challenges of missing specs and inefficient development loops, Voget offered five “cheat codes” for building better APIs.

### 1. Use AI-Driven Specs.
Use AI for what AI is good at: following rules.

“I don’t fully trust AI yet to write all of my code and expect that code to be bug-free,” Voget said. However, “Where I would trust AI-generated content more is following a rigid structure like the Open API specification and say, ‘Hey, use pattern matching and fill in the gaps that I have in this spec,’ or ‘Produce this spec for me based off of scanning my code files and get me to that specification.’”

### 2. Base Your Mocks off API Specs.
If AI enables developers to create higher-quality API specs faster, Voget said, they should also be able to spin up mock instances of those API specs quicker, too.

”Mock servers are really useful for powering parallel development,” he said. “Maybe you’ve got a frontend team who’s working on the UI and a backend team who’s working on an API. They can work in parallel if they have a really high-quality mock that describes that interface. And so I like basing these mocks off of specs, versus rolling out bespoke implementations of mock servers, because those are tough to maintain.”

### 3. Embrace Workflow Testing.
“We have, especially with microservices, a bunch of APIs that do specialized things or have a few endpoints,” Voget said. “And we can set up these contract tests to test the units of our API. But what’s really cool is that open API has an [Arazzo specification](https://spec.openapis.org/arazzo/latest.html) … Arazzo specs are really great because they can test a workflow of API calls.”

The Arazzo spec can help to carry out a functional test of the API’s workflow, he said. For instance, “let’s say that I have an API to retrieve a user profile, but first I need to authenticate to get an auth token. So that’s an API call. And then, maybe I have to get the list of users. So that’s another API call. And then I can finally get the user profile by ID, which is a third API call.”

The Arazzo specification, Voget said, “can describe that whole interaction, which is really, really powerful. If we arrive at Arazzo specs, we can set up these end-to-end tests and integration tests based on these specifications.”

### 4. Develop Locally, but Test Remotely.
The first three cheat codes, Voget said, are aimed at solving the challenge of missing or inadequate specs. The last two tackle development loop/developer productivity challenges.

The upshot of cheat code No. 4: You say something works on your machine? Prove it.

“How can we move testing from our outer dev loop into our inner dev loop, where it’s fast?” Voget asked. “What we can do is set up this concept of a remote, shared development environment.”

Some developers may have already set up ephemeral test environments in their CI workflow, he said, “where you might be coding on something, and you submit a pull request, and then we spin up some remote environment to do your testing in.”

But Voget thinks “we can shift that even farther to the left, and already have a development environment set up such that you would only need to make changes to your API code and only run and test your API while testing with remote resources, like your UI or other dependencies. Mock services can really help out with this too, especially if you’re hosting shared mock instances.”

By setting up a shared, remote development environment, he said, a team can alleviate “the burden of running your entire app locally.”

The keyword, Voget suggested, is “shared”: “No more running everything on local hosts where only you can access it. Have these shared, curable URLs that you can give your team to say, ‘Hey, test out my local changes,’ or ‘Test out my changes that I’m pushing up to this shared development environment,’ ahead of me even committing code or pushing it into the CI loop.”

### 5. Use Production-Like Development Environments.
“If we are setting up this shared remote development environment, the great thing about that is, we can make that as close to production as we want to,” Voget said. “It’s remote. It’s most likely going to be built in the same kind of infrastructure and architecture as our production environment.”

A staging or pre-prod environment that closely mimics a production environment is the ideal, he noted; so why not create a dev environment that also mimics a prod environment?

The production-quality dev environment should include the production API gateway, along with “all the microservices and all the dependencies that we need to run our full application,” Voget said. “We can get that really high-quality testing before we’ve even committed our code.”

Cheat code No. 5, he said, helps solve the trade-off API builders — and devs in general — face, between quality and speed. “We can actually have both,” he said. “We can have a quick dev loop, inner dev loop, and also have a high-quality test environment to test our changes out of it.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)