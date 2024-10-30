# DORA 2024: AI and Platform Engineering Fall Short
![Featued image for: DORA 2024: AI and Platform Engineering Fall Short](https://cdn.thenewstack.io/media/2024/10/e04ef5ea-dora-2024-ai-and-platform-engineering-fall-short-2-1024x576.jpg)
While both AI and platform engineering might make developers feel more productive and satisfied at work, they may be contributing to the creation of slower, more unstable software, according to the latest annual report from [DORA research team.](https://cloud.google.com/?utm_content=inline+mention)

In its 10th year, the[ “2024 Accelerate State of DevOps](https://dora.dev/research/2024/dora-report/),” more commonly known as the[ DORA report](https://thenewstack.io/google-says-you-might-be-doing-dora-metrics-wrong/), continues to explore how teams are getting better at delivering and operating software, in an effort to improve organizational performance and well-being.

In addition to the usual metrics, this year’s report dove into three increasingly interrelated trending topics:

[AI](https://thenewstack.io/ai/)and its impact in the workplace.[Platform engineering](https://thenewstack.io/platform-engineering/).[Developer experience](https://thenewstack.io/how-to-improve-and-measure-devex-in-your-organization/)(DevEx).
The New Stack sat down with[ Nathen Harvey](https://www.linkedin.com/in/nathen/), DORA team lead at Google Cloud, to talk about some highlights from the report, which aggregated the responses of nearly 3,000 tech workers. Google’s DevOps Research and Assessment (DORA) team has a lot to say about the state of[ DevOps](https://thenewstack.io/devops/) in 2024, and Harvey shared his thoughts about why AI and platform engineering might be producing unexpected side effects.

“What we see is that engineers or teams that are taking on more AI capabilities and using more AI tend to have better time in flow; they’re seeing higher levels of individual productivity,” Harvey told The New Stack.

“What we aren’t seeing, though, is some of that productivity and time and flow having good downstream effects when it comes to being able to deliver software fast and safe. In fact, when we see teams increasing their adoption of AI, it’s actually detrimental to their software delivery performance metrics.”

## AI: Still Not Reaching Its Potential
DORA is typically synonymous with[ four software performance metrics](https://thenewstack.io/googles-formula-for-elite-devops-performance/). Two of them, deployment frequency and change lead time, measure throughput, while the other two, change fail rate and failed deployment recovery time, measure stability. Consistently over the last 10 years, the companies that excel at one, excel at all four — while scoring poorly on one means it’s likely your organization is scoring poorly across all four.

Beyond those famous four, DORA covers a sociotechnical range of ways that software teams and engineering organizations can understand and measure the outcomes of their software delivery practices. It then includes advice for how each team can interpret and act on that data.

The 2024 DORA research asked[ more than 100 survey questions](https://dora.dev/research/2024/questions/) about seven key accomplishments and outcomes:

- Reducing burnout.
- Flow.
- Job satisfaction.
- Organizational performance.
- Product performance.
- Productivity.
- Team performance.
“When it comes to delivering software, we have to think about what technical practices we have in place, what processes,” Harvey said. “And, most fundamentally, what’s the culture of your organization?”

With this in mind, each year DORA does a deep dive into at least one big trend that could be influencing your scores. A decade ago, it was the impact of cloud computing. It’s no surprise that DORA 2024 concentrates first and foremost on the impact of AI on software development.

What might be surprising — at least to engineering leadership that is betting whole DevEx budgets on AI — is that results are still mixed.

Most notably, this year’s DORA report found that an increase in AI adoption reduces delivery stability by 7.2% and delivery throughput by 1.5%.

There are measurable benefits of AI on the software development life cycle — including a 3.4% increase in code quality and a 3.1% increase in code review speed. But right now those benefits aren’t flowing all the way through to delivery.

“It’s definitely not an even tradeoff. And the data can’t really tell us why,” Harvey said. “You aren’t seeing those AI impacts flow all the way through.”

## Can Human Devs Maintain AI-Generated Code?
Because each organization is unique, the DORA report offers the data, the trends and subsequent hypotheses that the researchers would love for teams to test in their organizations.

“We know that delivering software is very complex, and we suspect that potentially what AI is doing is helping with the early parts of the development process,” Harvey said, like documentation and code reviews, “but not solving for the later parts. An ability to change something up front without counteracting or being able to digest that change later downstream can have some negative impacts.”

So much of the current focus on[ generative AI is on code generation](https://thenewstack.io/whats-wrong-with-generative-ai-driven-development-right-now/), which is towards the start of the software development life cycle. It’s also the thing that developers say they[ want to spend more time doing](https://www.microsoft.com/en-us/research/uploads/prod/2019/04/devtime-preprint-TSE19.pdf?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform), not something they wish to automate.

“Generating code has rarely, if ever, been the bottleneck in how to get code out to users,” Harvey said. “One hypothesis is that we're just using AI much too early in the process, and there are opportunities for us to use it later, like feedback through automated testing.”

Full test automation coverage is something that development teams typically fail to achieve, which becomes more urgent when more code is being created with the assistance of AI.

New research from Germany’s International University of Applied Sciences found that code generated by AI, while being highly executable, is[ less understandable and maintainable](https://www.mdpi.com/1999-4893/17/2/62) for human coders.

Even if this year’s DORA report saw a 25% increase in AI adoption driving a small increase in perceived code quality, more code being created inevitably contributes to more technical debt and less documentation — which are the top causes of lost productivity, according to the developers that responded to the[ “2024 Atlassian-DX State of DevEx Survey](https://www.atlassian.com/software/compass/resources/state-of-developer-2024?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform).”

The DORA team presents another theory: Since AI has us creating more code than ever, we could be forgetting some of the software delivery life cycle best practices in our speed to production.

“We know from our decade of research, the way to improve software delivery performance is to ship smaller changes,” Harvey said. “AI helps me write more code than I could have in the past, right? So maybe, as an industry, as a team, we're forgetting smaller batches are better because the AI helps us generate larger batches. But larger batches are harder to get feedback on.”

This makes whole swaths of code slower to get through the approval process, and, when it does, it’s putting less stable code into production.

In the qualitative one-to-one interviews that DORA ran for the first time this year, it was revealed that developers don’t really know why their organizations are spending so much on AI.

“It felt like FOMO: My organization is leaning heavily into AI because everyone else is and they're afraid that if we don't do the AI, we're going to get left behind,” Harvey said, feeding back what his colleague[ Kevin Storer](https://www.linkedin.com/in/kevin-m-storer-ph-d-420550216/) heard repeatedly.

This was echoed at the individual level, where everyone said they are using AI mainly because everyone else is using AI.

## How Do Your Developers Feel About AI?
The vast majority of developers think[ AI tools will be more integrated into their workflow](https://survey.stackoverflow.co/2024/ai) of writing, testing and documenting code in 2025. In fact, most of them are already relying on AI tools for a number of common development tasks, according to the report.

Therefore, it’s important to consider where AI is working and where it’s not.

It could also be, aligning with previous[ reports on developer experience](https://thenewstack.io/why-do-developers-lose-1-day-a-week-to-inefficiencies/), that organizations are investing in the wrong AI software development use cases.

The aforementioned Atlassian-DX DevEx Survey found that leaders believe that AI is the most effective way to[ improve developer productivity](https://thenewstack.io/boost-developer-productivity-by-reducing-their-paper-cuts/) and satisfaction — while a whopping two-thirds of developers have yet to see any significant[ AI productivity gains](https://thenewstack.io/how-to-boost-developer-productivity-with-generative-ai/).

Even the so-called AI wins boasted in this year’s DORA report, Harvey said, could just be developers perceiving their code and docs are better with AI but maybe they aren’t.

DORA isn’t integrating with companies’ codebases, he explained. It’s also not asking directly: Since you’ve started using AI, has your code quality improved? Instead, it’s asking questions like:

- How much AI are you using?
- What’s your flow like?
- In the last six months, how satisfied or dissatisfied have you been with the quality of code underlying your primary service or application?
The data team then looks for patterns between these seemingly separate concepts.

The tech industry is likely at the bottom of a J curve, Harvey said, as companies are still figuring out when and where in the software delivery life cycle to use AI. This is also only the beginning of DORA’s attempt to measure the impact of AI, so only time will tell if a climb in productivity, throughput and stability is coming soon.

## Recommendations for Using AI in Development
What we do know is that not everyone is all-in on AI. More than a third of respondents reported little to no trust in AI-generated code.

The 2024 report also offers five recommendations in order to[ foster developer trust in AI](https://dora.dev/research/2024/trust-in-ai/):

- Establish and communicate a generative AI usage policy.
- Invest in faster feedback drivers, like code reviews and automated testing.
- Encourage developers to use GenAI on coding languages they know best, as they’ll feel more confident to spot weaknesses.
- Encourage GenAI usage, but don’t force it.
- Help developers to envision a future role working with AI — not it taking their jobs.
“As an industry, we haven’t found the Goldilocks of trust with AI,” Harvey said, somewhere between trusting an AI-generated code review by default and not trusting AI at all because we’re afraid it’s stealing our jobs.

“That position in the middle is going to always be changing, and we're always going to be trying to find the right balance of what's the right level of trust to have. It could be that we're putting too much trust in AI during the code review process, and that's speeding up our code reviews, and it's leading to lower stability.”

## Some Measurable AI Wins
In the meantime, the DORA report offered some good news for AI users.

A 25% increase in AI adoption is associated with a 7.5% increase in documentation quality, according to the researchers’ estimates. This follows the 2023 DORA Report, which found that quality internal documentation has an almost 13-fold impact on organizational performance.

This is a smart early application of GenAI because [large language models (LLMs)](https://thenewstack.io/llm/) are really good at explaining complex topics. But it’s not the only win.

“What we see is that engineers or teams that are taking on more AI capabilities and using more AI tend to have better time in flow; they're seeing higher levels of individual productivity,” Harvey said.

“What we aren't seeing, though, is some of that productivity and time and flow having good downstream effects when it comes to being able to deliver software fast and safe. In fact, when we see teams increasing their adoption of AI, it's actually detrimental to their software delivery performance metrics.”

The report found that AI has a “substantial and beneficial impact” on flow, productivity and job satisfaction. If a tech worker increases their AI adoption by 25%, that translates to a 2.1% increase in productivity. That 2% at an enterprise scale is significant.

Particularly, the report stated that “AI’s ability to synthesize disparate sources of information and give a highly personalized response in a single location” increases flow while decreasing context switching.

By definition, that means AI is already[ improving developer experience](https://thenewstack.io/can-devex-metrics-drive-developer-productivity/).

## Tighter Feedback Loops Improve Performance
Doubling down on last year, DORA 2024 has re-confirmed that user-centricity remains essential. The tighter the feedback loops, the more likely you are to build what your users actually want to use.

“The reason we want fast software delivery is because we don't really have that tight connection to our users,” Harvey said. “We don't have a nice tight loop [for] every feature or every change that we ship. It's a little bit of an experiment. We need to understand how our user is going to react to that.”

“So the faster we can ship, we can close that feedback loop faster, and that improves our user centricity. But also just actually thinking about who the user is and having conversations around that helps drive things.”

The 2023 DORA report found that a greater user centricity led to a staggering 40% increase in organizational performance.

This year’s report found that organizations that prioritize the end user experience not only produce higher quality products, but these organizations’ developers are more productive, more satisfied and less likely to experience burnout.

## Platform Engineering: a Mixed Impact on DevEx
The three deep-dive pillars of this year’s DORA — AI, platform engineering and developer experience — have something in common: a focus on developers as end users. Specifically, success with platform engineering hinges on a[ Platform as a Product](https://thenewstack.io/platform-engineering-demands-a-product-mindset/) focus, where you work for tighter feedback loops with your internal developer customers.

This year’s report is the first to try to quantify the impact of an[ internal developer platform](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/):

- IDP users had 8% higher levels of individual productivity.
- IDP users had 10% higher levels of team performance.
- An organization's software delivery and operations performance increases 6% when using an IDP.
- An IDP’s focus on self-service supports developer independence, which significantly improves productivity at both the individual and team levels.
In addition, having a dedicated platform engineering team increases productivity at the software development team level by 6%.

But again, similar to AI, an increased focus on platform engineering does not help the organization’s core DORA metrics:

- Throughput decreased by 8%.
- Change stability decreased by 14%.
The DORA team hypothesized that throughput could be decreased because an IDP can actually increase the number of handoffs between systems and teams. But the report predicts that while throughout is down, the ability to get work done is likely up overall.

The report’s authors suggest that the shocking increase in instability could be because platforms enable teams to experiment and deliver changes faster, which results in a higher rate of change failure and rework. However, they also posit that it’s a sign that a platform isn’t aiding in quality or that teams aren’t onboarded and using the full platform capabilities, like automated testing.

Whatever the cause, this change instability as a result of a platform correlates to an increase in[ developer burnout](https://thenewstack.io/tech-works-how-to-identify-and-address-burnout-on-your-team/). And it also could be a sign of overall burnout in the platform engineering team. The report considers that change instability and burnout are predictors for a platform engineering initiative, when an internal developer platform is seen as a fix to these problems.

AI and platform engineering are perhaps the two most important trends that are affecting developer experience. And yet both are sitting in[ Gartner’s trough of disillusionment](https://www.gartner.com/en/research/methodologies/gartner-hype-cycle), where experiments typically fail.

“We aren't seeing them improve software delivery performance yet,” Harvey said. “We aren't seeing them lead to better outcomes when it comes to organizational performance yet. It's up to us as an industry to make sure that we're taking these signals that we're getting from DORA and applying them and using those to help change what we do.”

“That's why DORA’s mission is to help teams get better at getting better. It's a journey of continuous improvement.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)