**With an eye on the huge downstream pressure** that AI code tools are putting on software engineering teams, [GitLab](https://about.gitlab.com/assessments/devops-modernization-assessment/?utm_medium=cpc&utm_source=google&utm_campaign=eg_emea_dmp_x_x_en_gitlab_search_br_core_emea&utm_content=modernization-devops&_bt=799134064298&_bk=gitlab&_bm=e&_bn=g&_bg=75294586319&gad_source=1&gad_campaignid=2062237857&gbraid=0AAAAADcJCbc76EU4m0mAHvvwnnqG_W5m3&gclid=CjwKCAjw3ejRBhAdEiwADkqPn1C7H4Sg3hCgHTj04p-T5ZBJXctz3mWXwAZmWPFZGUmSZPXRB9ibjRoCb-AQAvD_BwE) released its [AI Accountability Report](https://about.gitlab.com/resources/ai-accountability-survey-2026/) on Tuesday to assess which direction the “industry conversation” is moving in.

The narrative now appears to have shifted from how quickly teams can generate code to whether they can actually control what they ship.

The Harris Poll for GitLab surveyed 1,528 developers and technology buyers across six countries. Some 91% of organizations have two or more AI coding tools in active use, and 78% report that developers are writing and committing code faster since adopting AI tools. But speed is outpacing control, with 43% of respondents reporting they cannot reliably distinguish AI-generated code from human-written code in their own codebase.

[Manav Khurana](https://www.linkedin.com/in/mkhurana/), chief product and marketing officer at GitLab, tells *The New Stack* that his organization’s study sheds light on a [governance gap](https://thenewstack.io/five-pillars-ai-governance/) opening up due to the sheer volume of code now being produced.

## The AI code review bottleneck

“AI has shifted the bottleneck from writing code to reviewing it — 85% of our survey respondents confirmed this,” Khurana says. “Developers have an increased load of validating code they didn’t write and may not fully understand. The gains from writing code faster are washed away by the lag in days-long review cycles.”

He reminds us that, while the speed of software coding has increased, cutting code is only one part of the [software development lifecycle](https://thenewstack.io/ai-agents-are-finally-starting-to-revolutionize-the-software-development-lifecycle/) (SDLC): Before coding comes requirements; throughout coding comes review, security, testing, and deployment; and after coding comes enhancements, integrations and maintenance.

Khurana thinks that the fix here is to use an agentic infrastructure that makes the rest of the software delivery process move at the same pace as agentic coding. That means machine scale execution, context across the full lifecycle, governance built into the flow, and orchestration across all layers.

> “A developer reviewing an agent-generated merge request can see who invoked the agent and what issue it was tied to. What they often can’t see without pulling from multiple systems is what security findings it touched, what policy governed it, and whether the risk it introduced was ever resolved.” – Manav Khurana,

Next, we come to the toolchain problem.

“Only 28% of organizations say their SDLC tools are fully integrated with shared data and workflows,” highlights Khurana. “A developer reviewing an agent-generated merge request can see who invoked the agent and what issue it was tied to. What they often can’t see without pulling from multiple systems is what security findings it touched, what policy governed it, and whether the risk it introduced was ever resolved.”

The GitLab mantra states that when governance is built into the platform, code reviews are automatic, based on the team and company’s policies. All agent actions are tied to an identity, logged against a policy, and surfaced in the review flow automatically.

“The goal is to make the governance layer invisible to the developer so reviewers can focus on the decisions that require human judgment,” suggests Khurana.

## What exactly is GitHub doing?

In terms of providing for machine-scale agentic execution, a new Git backend and interface have been developed, which the organization claims will “sustain millions of agent sessions reliably” and with blazing fast speed. In the company’s own testing processes, it has recorded seeing up to 50x faster wall clock time and up to 1000x less network traffic compared to the current generation of Git.

“We have also engineered for context,” clarifies Khurana. “[GitLab Orbit](https://about.gitlab.com/blog/introducing-gitlab-orbit/) [introduced on June 10 this year] provides agents with a context graph connecting code, pipelines, work items, security findings, and production signals. In our testing, we’re seeing agents work up to 11x faster, require 4.5x fewer tokens, and have 45x fewer hallucinations. More notably, agents can now answer questions they previously couldn’t because they can get all the context they need with a single graph call.”

There’s also additional governance and orchestration developments on the table to ensure agent actions are automatically coordinated across the SDLC according to the policies that teams define.

## Ask yourself three questions about AI code

Crucially, the GitLab report defined AI accountability as the organizational and technical capability to answer three questions about any line of AI-generated code:

* Where did this code come from?
* What was it meant to do?
* Who is responsible for it once it’s in production?

GitLab has said that most organizations cannot answer those questions today.

As a result of not knowing the who, what and where of executing AI code (presumably with the why and when factors being implied also here), Khurana says that escalating costs are usually a clear signal that the governance gap is widening. He explains that agents consuming tokens inefficiently against infrastructure that wasn’t built for them is a sign that the context and governance layers are missing.

“Most organizations have pursued agentic software engineering by adding AI coding tools on top of the infrastructure they already have, and the problems are showing up quickly,” insists Khurana. “This is where GitLab’s approach differs. GitLab is building the agentic infrastructure that other tools do not address – from execution at machine scale to context, governance, and orchestration across the software lifecycle. A coding assistant makes one developer faster – [what we are doing] what makes the whole system move at machine speed without losing control of it.”

Other measures from the GitLab study here provide the following pair of heavily weighted percentages. A total of 91% are likely to invest in AI code governance tools in the next 12 months; 98% have already allocated or expect to allocate budget. Additionally, 85% agree that the next phase of AI in software will focus less on generating code and more on governing it

## What should (junior) developers think next?

Khurana points to what he calls “a maturation” in how enterprises are thinking about AI, which, if they get it right, moves AI code functions from being a productivity tool to a foundational capability that can scale.

That maturation has an impact at the senior level for engineering project management, but it also has ramifications for junior developers just embarking upon their careers.

“One of the skills that matters most now is judgment,” Khurana concludes. “Junior developers who invest in understanding systems deeply, not just syntax, and can trace code back through pipelines, security findings, and production signals, are the ones who make agentic engineering work.”

We know that agents can generate code faster than any developer. But, currently, what they cannot do is evaluate whether that code is right for the system and the requirements it needs to meet.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)