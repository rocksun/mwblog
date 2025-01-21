# More AI, More Problems for Software Developers in 2025
![Featued image for: More AI, More Problems for Software Developers in 2025](https://cdn.thenewstack.io/media/2025/01/444289ce-steve-johnson-bjwdjszsqz4-unsplashb-1024x576.jpg)
[Generative AI](https://thenewstack.io/ai/) has more code being created than ever. But despite the popularity of [platform engineering](https://thenewstack.io/platform-engineering/), a developer crisis is brewing, as uncovered by Harness’s the [State of Software Delivery 2025](https://www.harness.io/state-of-software-delivery), which summed up the experience shared by 250 engineering leaders and 250 software developers.
“Generating more code is awesome,” said [Martin Reynolds](https://www.linkedin.com/in/martinreynolds/), field CTO at Harness, as developers are predominantly feeling more productive with [AI coding assistants](https://thenewstack.io/how-generative-ai-coding-assistants-increase-developer-velocity/).

“But that generates more of everything else that happens after the code — and there’s a lot down that line. From security testing, to unit testing, the overall governance, the amount of deployments that happen, the number of dependencies that get pulled in.”

The majority of developers interviewed have problems with at least half of all deployments aided by AI coding assistants. The report found that 67% of developers spend more time debugging AI-generated code, while 68% spend more time resolving security vulnerabilities. While AI speeds up code writing towards the start of the [software development lifecycle](https://thenewstack.io/software-development/), more code means a greater demand for code reviews, security validation and quality assurance. This demand is so far nowhere near being met.

Add to this, when [AI adoption increases, delivery stability and throughput decreases](https://thenewstack.io/dora-2024-ai-and-platform-engineering-fall-short/).

Despite all these downsides, AI adoption is continuing to rise in [software delivery in 2025](https://thenewstack.io/developer-productivity-in-2025-more-ai-but-mixed-results/). Here’s what organizations can do to stop AI-generated code from turning into a totally toil-ridden disaster.

**Will AI Hurt or Heal Developer Burnout?**
Developers, the report found, are spending more time debugging than ever. That doesn’t necessarily mean that AI-generated code is innately more buggy.

However, using AI to generate code can leave users — especially more junior developers — without the context the code was written with and who it was written for, making it harder to figure out what’s gone wrong.

“The risk is generally higher for junior developers. Senior developers tend to have a much better awareness and quicker understanding of the code that’s generated,” Reynolds observed. “Junior developers are under a lot of pressure to get the job done. They want to move fast, and they don’t necessarily have that contextual awareness of the code change.”

Without quality and governance controls — like security scans and dependency checks, and unit, systems and integration testing — deployed throughout the software development lifecycle, he warned, the wrong thing is often merged.

“A lot of organizations struggled with that without GenAI software, and then, when you generate more code, it just exacerbates that problem,” Reynolds said.

Interestingly, [GenAI can be really useful](https://thenewstack.io/whats-wrong-with-generative-ai-driven-development-right-now/) at explaining code, particularly to junior developers.

“Why not make it part of the process that actually, when AI code is generated, it also generates documentation about how that code works, right?” he suggested.

Indeed, generative AI is very good at explaining complex concepts. In fact, the [2024 DORA report](https://thenewstack.io/dora-2024-ai-and-platform-engineering-fall-short/) found that the biggest generative AI win was a significant increase in documentation quality. Docs help reduce cognitive load. Putting a chatbot overlay over the docs or integrating it within the codebase — like Github’s Copilot does — further reduces context switching.

While more AI-generated code increases demand for code reviews, the most recent DORA report also found that a 25% increase in AI adoption increased code review speed by 3.5%. This could be through simply more nudges or by leveraging AI to identify the right person to review the first time or to more evenly distribute the code review load.

But docs and code reviews are only a small part of the complex software development lifecycle, which, the Harness report found, still sees developers spending at least 30% of their time on manual, repetitive tasks. That toil is costly.

With more AI-generated code, the burden on the developer increases. Now, again according to the Harness report, 88% of developers work more than the expected 40 hours a week, with half of all interviewed acknowledging that this overtime contributes to an unhealthy work-life balance.

Organizations need to be considering AI’s effect not only on the software development lifecycle but the lifecycle of the software developer too.

**Are Orgs Prepared for Shadow AI?**
Shadow IT has developers looking to engineer their way out of a problem by adopting — and often even paying for — tools that aren’t among those officially approved by their employers. Shadow AI is an extension that sees, the report found, 52% of developers using AI tools that aren’t provided by or explicitly approved by IT.

It’s not like developers are behaving insubordinately. The reality is, three years into widespread adoption of generative AI, most organizations still don’t have [GenAI policies](https://leaddev.com/software-quality/ai-governance-policy-engineering-managers-needed-yesterday).

Survey respondents uncovered serious gaps in the review of AI-generated code:

- 60% stated they do not evaluate the effectiveness of AI coding tools.
- 60% stated they do not have processes for assessing code for vulnerabilities or errors.
- 58% of organizations interviewed did not have outlined specific use cases where AI is and is not approved as safe to use.
- 43% of organizations do not dictate what code can or cannot be input into AI tooling.
- 42% of organizations do not have a list of preferred or denied tools.
Since engineering is inherently a science, you can’t improve what you don’t measure. While 83% of developers responded that they believe software development has become more efficient since the introduction of AI tools, these perceived [developer productivity gains](https://thenewstack.io/how-to-boost-developer-productivity-with-generative-ai/) remain unproven.

What’s more concerning is that organizations didn’t have all the controls and automated testing in place before this explosion of AI-generated code. This worry increases in regulated environments, where uptime can directly affect lives.

“It comes back to having policies in place [and] doing the security scans, that are making sure they’re not introducing risky vulnerabilities into their software because of the dependencies, that’s checking the quality of the code in terms of security,” Reynolds said. “Tools exist. Making sure that they are always run against your code is absolutely key.”

Organizations must also consider the risk of public AI tools being trained on personally identifiable information, proprietary code, trade secrets or more, and create and codify GenAI policies with automatic rollbacks in response.

These policies must also be updated frequently, but with notice, alerting developers when they will be applied — and, ideally, *why*. Version control is also important.

This need for a GenAI policy will become more urgent as generative AI tooling adoption and applications increase. In 2025, engineering leaders are planning to implement AI in the following places:

- Continuous integration and delivery (CI/CD) – 50%.
- Performance optimization – 48%.
- Security and compliance – 42%.
- Code cost optimization – 40%.
- Code generation (most used already) – 39%.
- QA/testing – 28%.
- Error remediation – 26%.
Harness aims to put governance policies in place — with [Open Policy Agent](https://www.harness.io/blog/harness-policy-as-code) to codify them — so there are no exceptions.

**Will Generative AI Kill Your Job?**
Popular headlines of late seem convinced that GenAI is ready to replace junior developer and QA jobs. And 90% of Harness’s survey respondents echoed this concern.

First, that result is concerning because engineering leaders were half of those responding to the survey, meaning a majority may have nefarious goals for GenAI. Add to that, spend on [generative AI is expected to increase](https://www.gartner.com/en/newsroom/press-releases/2024-10-23-gartner-forecasts-worldwide-it-spending-to-grow-nine-point-three-percent-in-2025) by another 10% in 2025.

But looking to rely so heavily on AI-generated code already — especially without those checks in place — is rash.

“Saying ‘reduce the need for junior developers’ or ‘I don’t need junior developers because I have AI’ — where are all your senior developers going to come from in the future?” Reynolds asked, calling this a short-sighted solution. “Am I going to rely on other companies to make junior developers?”

AI replacing QA seems particularly unrealistic. Right now, AI-generated code demands a human in the loop, especially at companies that don’t have policy checks in place.

“I think generative AI can reduce the burden on QA,” he said, mentioning how Harness has automatic test generation. “But that doesn’t take away the need for humans to make sure they’re using the right tests in the right areas, to point the software at the right part of the system.”

As AI tools become more ingrained into the day-to-day developer experience, the Harness report predicts that the role of developers will continue to evolve — and likely expand to include even more. Rather than displacement, the report says the role’s remit must continue expand to include AI prompt engineering, output validation and capabilities integration, among other things, which organizations also have to help upskill their staff in. All with clearly established boundaries and training.

As Reynolds put it, a successful future with AI-generated code all about innovation within guardrails.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)