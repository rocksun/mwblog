Unless your business was born out of a university machine learning (ML) department or conceived in the last three years, you’re not likely an “AI native organization.” But that doesn’t mean you can’t embrace [AI native development](https://thenewstack.io/what-is-an-ai-native-developer/).

As we enter 2026, organizations need to ride the dramatic sociotechnical shift of AI and steer change management in a new direction. Traditional [DevOps](https://thenewstack.io/introduction-to-devops/) is no longer enough, but its engineering best practices are more necessary than ever. [Platform engineering](https://thenewstack.io/platform-engineering/) becomes table stakes as it helps deliver MLOps, merging AI into continuous delivery pipelines with security guardrails and gates. And deep technical experience is deemphasized in lieu of “softer” core skills like the ability to respond to change, learn and collaborate.

In this time of constant flux, here are some evergreen AI-first strategies for your tech talent and training today.

## Applying DevOps Fundamentals in the Age of AI

With AI, more code than ever is produced — with fewer humans in the loop. But if [writing code was never the bottleneck](https://leaddev.com/velocity/writing-code-was-never-the-bottleneck), that means delivery speed relies on honing all the other bits on the path to production. Much of the success with AI comes from having engineering best practices down — with one important change.

“In addition to the traditional DevOps, you need to add more things to account for what’s important for AI,” said [Tiago Miyaoka](https://www.linkedin.com/in/tiago-yuzo-miyaoka/), head of data and AI practice at [Andela](https://andela.com/?utm_content=inline+mention) tech talent marketplace.

DevOps practices trend deterministically, following the same cycle until there’s a major change. [Generative AI](https://thenewstack.io/ebooks/generative-ai/ai-for-the-enterprise-the-playbook-for-developing-and-scaling-your-ai-strategy/) and [AI agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) are more probabilistic and not always straightforward, he continued, with results changing over time. [MLOps and AIOps](https://thenewstack.io/ai-operations/) account for this change.

“If you think about DevOps and PlatformOps, it’s a deterministic output — it has to work, and you have to detect if it’s not working,” said [Jake Hoffner](https://www.linkedin.com/in/jakehoffner/), senior director of product and engineering at Andela. But, with generative AI, “these are probabilistic outputs that the system is creating. How do you deterministically determine that something is probabilistically producing a good output?”

Software engineers need to learn from their data science colleagues about scoring and sampling a high percentage of what is being produced. They also need to learn when to go the probabilistic route when flexibility is fine and when to remain deterministic when reliability and consistency are non-negotiables.

If something must have the same output each time, you can’t use generative AI to produce any part of that in a runtime system, Hoffner emphasized.

“If you want AI to produce deterministic output, have it write the code that produces the output at runtime, don’t rely on the AI’s output itself at runtime,” he said. “One or more humans should always review the code first.”

Embedding DevOps best practices — automated [CI/CD](https://thenewstack.io/introduction-to-ci-cd/) pipelines and guardrails, monitoring and observability, continuous delivery with rollbacks — is crucial at scale. Adding to this, the [DevOps principles](https://thenewstack.io/devops/ "DevOps principles") of small batches of code and shorter feedback cycles make both humans and AI agents more successful.

## The Role of Platform Engineering in Enabling AIOps

All of this is enabled by paved pathways with guardrails put up by platform engineering teams. An [internal developer platform](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/ "internal developer platform") makes it easy to do the right thing, whether that’s for engineers of all experience levels, swarms of AI agents or, increasingly, an orchestration of the two.

The recently released [2025 DORA report](https://dora.dev/research/2025/) concurs, recommending seven capabilities that, paired with AI, lead to the best outcomes:

* A [clear and well-communicated policy](https://thenewstack.io/how-to-create-the-generative-ai-policy-you-needed-yesterday/) of when and where to use AI
* Healthy data ecosystems
* AI-accessible internal data
* Strong version control practices and rollbacks in place
* Working in small batches
* User-centric focus
* Quality internal platforms

Perhaps the most ignored of these is maintaining a user-centric focus. So many opaque top-down AI mandates have led to “AI for AI’s sake.” As [Shahzia Holtom](https://www.linkedin.com/in/shahzia-holtom-phd-ba978210/), senior director of technical excellence at [Microsoft](https://news.microsoft.com/?utm_content=inline+mention), recommended, “Do the hard thing first [and] really focus on the users’ perspective.”

Miyaoka and the folks at Andela define AIOps as AI engineering, or using AI to develop new AI apps and systems. This relies on AI architecture, like a vector database to store knowledge bases or documents that the AI will consult in your AI application. This includes the [Model Context Protocol](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) (MCP) and the internal developer platform that enable API-based extensibility on top.

“You have all components in the cloud that are all connected in this architecture. And for agentic AI usually you have multiple, like maybe tens or dozens of AI agents that are connected on a very complex pipeline,” Miyaoka said. Especially for AIOps, “you need to have all of that very carefully monitored, making sure that everything’s running properly. Because, if one of those things breaks, then your whole application breaks, and then if your application goes down, you lose money.”

This includes making sure your data scientists, software engineers and platform engineers continuously monitor for model drift and performance to see if the live results are as expected. This demands a creative, exploratory mindset to figure out the cause of any changes.

AI engineering should also be paired with more customer-facing roles to help identify changes to customer behavior or outdated knowledge bases.

## Why You Should Hire for Potential, Not Technical Skills

Most organizations are still hiring people for very skills-focused roles.

But with everything changing so fast, any technology or programming language choice could be altered, eliminated or replaced by AI at any time. And for this newest, shiniest technology, it’s impossible — despite requirements in many job ads — to have several years of experience.

“At Andela, we’re putting a deeper emphasis on soft skills because that’s something that’s always been important,” Hoffner said, but that has “been skipped over by a lot of assessment providers.”

As LLMs are approaching doctorate-level knowledge, he observed, engineers’ decision-making skills become more important. Talent assessment needs to evolve in response.

“Given that it’s so early, I think companies should be looking for people who are constantly looking to [adapt a workflow](https://thenewstack.io/how-atlassian-is-driving-the-ai-agent-assisted-workflow/),” he said. “You’re looking for people who are more willing to be adaptable and more willing to apply and test out different techniques and see what works. Because at this point, nothing’s locked in.”

> It’s better to hire for capacity for change than years with a certain programming language, and then supplement with skills training programs.

With AI-generated resumes feeding into AI-driven applicant-tracking systems, it’s increasingly challenging to validate experience via traditional recruitment paths.

“It’s really hard to differentiate who is really an AI-fluent engineer … ready to go on their first day,” Miyaoka said. Given that AI in the software development life cycle is only about three years old, it is unreasonable to demand much experience with AI engineering.

Andela has found that DevOps best practices and the ability to spot mistakes in AI-generated code can be more valuable than years of hands-on experience with AI.

It’s better to hire for capacity for change than years with a certain programming language, and then supplement with skills training programs.

The better “assessment is identifying not just the raw skill but aptitudes that are more core and less applicable to any certain skill — more foundational,” Hoffner continued. He also recommends assessments to identify “people that are more willing to be early adopters, who are more willing to be flexible in how they utilize these tools and rethink everything they’ve known to this point, because it’s all changing.”

It’s not just at the individual workflow level either. The shift from DevOps to AIOps, Miyaoka added, means that teams have to adopt their existing stack to the AI era, too. This isn’t going to demand just hiring from the outside, but rather upskilling from within.

Senior engineers should be actively mentoring putting security and guardrails in place. Embracing a PlatformOps approach with monitoring and rollbacks makes it much safer to fail, learn and try again.

## Adopting AI Native Ways of Working

“You should not just have AI generate something and ship it off to production,” said [Nathen Harvey](https://www.linkedin.com/in/nathen/), DORA lead at [Google Cloud](https://cloud.google.com/?utm_content=inline+mention). “There has to be other steps and validation along the way.”

More than ever, we need a human in the loop interacting with AI. And we need fast learners who can collaborate across departments. So far, the greatest impact of AI is on individual productivity, which is why there’s been very little “AI wow” at the team, department and organizational levels.

“AI’s primary role in software delivery is that of an amplifier. And the greatest returns on AI investment come from a strategic focus on the underlying organizational systems,” Harvey said. “Without this foundation, AI creates localized pockets of productivity that lead to downstream chaos.”

This is why a recent [MIT study found](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf) that 95% organizations got zero return on investment from AI pilots. The study blamed a lack of contextual learning and experimentation stuck inside data silos.

> Centralized AI experimentation and implementation is the only way to answer what business information you need to make decisions at scale.

DORA 2025 prescribed ways to design for these new AI native ways of working in a way that breaks down this compartmentalization:

* **AI native delivery pipelines** with continuous analysis, dynamic test generation and predictive risk assessment.
* **AI native data systems** in which AI helps maintain its own environment by organizing, cleaning and analyzing data.
* **AI native security** with proactive thread detection and [automated incident response for low-stakes incidents](https://thenewstack.io/stop-chasing-low-stakes-incidents-let-ai-do-it/).
* **AI native collaboration** via [agentic workflows](https://thenewstack.io/how-atlassian-is-driving-the-ai-agent-assisted-workflow/).

AI should augment the work we are doing today, the DORA team argues, including removing friction in existing workflows and adding value-stream mapping — ideally across more than the individual team or developer experience.

“What business problem are you trying to solve?” asked [Lee Fulmer](https://www.linkedin.com/in/leefulmer/), senior advisor at McKinsey and Company. “I don’t believe in having a separate AI strategy. Don’t even have a separate technology or data strategy — they’re embedded in our business strategy.”

Here again, platform engineering arises as a success pattern because it creates a single pane of glass that connects engineering and data science to business goals in a way that the business side can understand its tech investment.

“AI is a business and a human transformation, not a technological transformation,” Fulmer continued. “Sure technical prowess is important, but an AI-first strategy will only work when grounded in the people and processes — the why and how for your business.”

Centralized AI experimentation and implementation is the only way to answer what business information you need to make decisions at scale.

## You’re Not Late. You’re Right on Time.

“Learning a little bit about AI can be formidable,” [Hannah Foxwell](https://www.linkedin.com/in/hannah-foxwell/), founder of [AI for the Rest of Us](https://aifortherestofus.live/), explained.

“The future isn’t going to be handed to us by someone else. We are going to figure out what to do with this amazing new technology and we’re going to do it by working together.”

> The organizations that are looking to AI to cut back on headcount are the first ones to lose face and value in this first stage of AI.

Indeed, the aptitude in greatest demand right now is being open to change. As [Mustafa Suleyman](https://www.linkedin.com/in/mustafa-suleyman/), CEO of Microsoft AI, posted on X this past June:

“Biggest career accelerator in the next decade: get really, really good at learning.

* + Figure out your learning style.
  + Use AI to convert material into that format/style (podcasts, quizzes, etc.)
  + Apply knowledge.
  + Repeat.

Learn fast, grow fast.”

The organizations that are looking to AI to cut back on headcount are the first ones to lose face and value in this first stage of AI. This breaks the trust and psychological safety needed to experiment and innovate in times of great change.

“The form of intelligence that makes the most difference now is LQ: the ability to learn,” said [Claudia Harris](https://www.linkedin.com/in/claudia-harris-obe-71793374/), CEO of Makers. She ardently argues that no one is behind in AI because we must focus on the human side of AI adoption.

At the AI for the Rest of Us conference in October, Harris said that a superpower is “being able to understand that you’re not stupid: ‘It’s just me. I need to persevere, even when it feels bad, I get less return to my input than I’m used to.’ There’s a lot of work involved in learning, and it’s messy.”

This means, she continued, becoming not the expert in a certain technology, but in the fundamentals of research, analysis, creation, coding and communication. Start with focusing on the boring use cases.

Whether someone is a new hire or a current employee, the team at Andela is creating a continuous loop of assessment and training around problem-solving, collaboration and writing code.

No matter what role or how many years of experience you have, being open to experiment and learn will be the most hireable skill in 2026 and beyond.

*[Upskill your internal teams on the latest AI skills](https://andela.com/discover/ai-native-talent?utm_medium=content&utm_source=TNS&utm_campaign=navy-tansy).*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/220bf6cf-jriggins-2025-600x600.jpeg)

Jennifer Riggins is a tech storyteller and journalist, event and panel host. She bridges the gap between business, culture and technology, with her work grounded in the developer experience. She has been a working writer since 2003, and is based...

Read more from Jennifer Riggins](https://thenewstack.io/author/jennifer-riggins/)