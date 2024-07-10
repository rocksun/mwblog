# What Devs Really Want in an Internal Developer Portal
![Featued image for: What Devs Really Want in an Internal Developer Portal](https://cdn.thenewstack.io/media/2024/07/38b5734c-devs-want-internal-developer-portal-1024x576.jpg)
Measuring developer productivity has become a [controversial subject](https://leaddev.com/process/what-mckinsey-got-wrong-about-developer-productivity). Some think developers should be [measured](https://thenewstack.io/agile-devops-platform-engineering-confusion-stalls-devs/) on how many lines of code they can write, how quickly they can ship a new feature and how swiftly they can find a fix for a bug. Others think these metrics only tell engineering leaders one part of the story, and developer experience — how a developer feels about their work — is equally important.

Developer experience is a broad term covering onboarding; relationships with managers, peers and other groups; technologies, processes, policies and approvals; software velocity and quality; and more. It’s becoming an area of focus for engineering leaders because of research indicating that [better developer experience leads to better developer productivity.](https://github.blog/2024-01-23-good-devex-increases-productivity/)

One of the core drivers behind the adoption of [internal developer portals](https://www.getport.io/glossary/internal-developer-portals) is improving [developer experience](https://www.getport.io/glossary/developer-experience). It comes from the recognition that, if during the software development lifecycle (SDLC), the developer finds it difficult to discover information, needs to wait for [DevOps](https://thenewstack.io/devops/) or site reliability engineering (SRE) to scaffold a service or can’t find other services or APIs, the developer experience won’t be good.

## Measuring Developer Experience with Surveys
It’s important to measure developer experience because, if the SLDC process is slow, unproductive and full of diversions and missing data, how can developers be productive? Also, without this data, how can engineering leaders improve the developer experience and productivity?

Implementing developer experience surveys before implementing a portal helps you measure developer experience broadly and make informed decisions about what to include in the portal. By knowing how developers feel, you can better gauge what they need and create a change management process and roadmap.

A survey can also help you envision what your initial portal minimum viable product ([MVP](https://www.getport.io/blog/internal-developer-portal-how-do-i-get-started)) will look like and what features each sprint will focus on. Many engineering leaders are using developer experience surveys to generate insights that help them decide what to work on next in the portal and demonstrate the results of prioritizing or implementing a new feature.

Here’s our rundown of everything you need to know about creating, implementing and using a developer experience survey.

## Prepare the Survey
### What Is the Endgame?
Begin by asking what you want from your survey. Alongside improving developer experience by exploiting the portal’s features, you may want to learn about:

- Improving developer onboarding.
- Increasing speed to ship quality code.
- Eliminating bottlenecks in the SDLC.
- Reducing mean time to repair, resolve, recover or respond (
[MTTR](https://thenewstack.io/why-are-we-so-bad-at-mean-time-to-repair-mttr/)). - Reducing burnout.
Focus on questions that will help you take action on specific areas. Use the survey to discover pain points you may have not considered and to evaluate how well you’re addressing them.

For example, if you think you can eliminate bottlenecks in the SDLC by helping the team find answers or solutions to problems more quickly, [you can ask](https://survey.stackoverflow.co/2023/#professional-developers-developer-experience):

*On an average day, how much time do you typically spend searching for answers or solutions to problems you encounter at work? (Include time spent searching on your own, asking a colleague or waiting for a response.)*
Include multiple-choice answers ranging from 15 minutes a day to over 120 minutes a day.

### Who Should You Survey?
This may be as simple as “all our developers,” but perhaps your survey can be adapted to other personas in the organization. Developers’ day-to-day work overlaps with DevOps, SREs and others, and these personas can also [benefit](https://www.getport.io/blog/how-can-different-user-personas-get-the-best-out-of-an-internal-developer-portal) from an internal developer portal. The different personas have different levels of tech knowledge and use different technologies and features. For example, managers may need a quick way to assess standards compliance, while developers may need self-service.

One of our customers began their portal scoping exercise by surveying their cloud native developers, as this was the organization’s new focus. And [LinkedIn](https://getdx.com/blog/analyzing-developer-survey-data-linkedin/) surveys all its developers but breaks the resulting data down into developer personas to evaluate the results.

### How Much Time Should It Take?
You want to find the right balance between engagement and productivity. The survey shouldn’t take longer than 15 minutes to complete; this is likely to provide a good data sample without taking too much time.

One of our customers conducts weekly surveys that cover developer experience and other topics using a specialized developer experience platform. The team is required to complete it, and engagement exceeds 90%. However, annual or [quarterly surveys](https://thenewstack.io/developer-productivity-metrics-drive-continuous-improvement/) are more common.

[Abi Noda](https://www.linkedin.com/in/abinoda/), CEO of DX, explained at Port’s recent Portal Talks event that you have to be able to sustain [80% to 90% participation rates](https://www.youtube.com/watch?v=vYyB75vlH_E&t=23s) for self-reported data to be credible.
Making the survey anonymous enables developers to answer questions honestly without being concerned about repercussions. Even with an anonymous survey, the respondent can be inferred on smaller teams or with specific roles or personas. This may lead to developers answering how they think they “ought to,” rather than truthfully. One way to work around this is to save each answer independently and not in a thread. Even if the survey is anonymous, you can’t assume the results tell the whole truth, so keep that in mind when looking at the data.

To increase participation rates, Noda says the survey design and experience must be high-quality, relevant and useful to engineering organizations, executives *and* the developers and teams. It’s important to communicate results and organizational learnings from the survey.

**Main takeaway: **Frame the survey as an exercise that is aimed at helping your developers — not testing or catching them out.
## Create the Survey
### What Survey Tool Should You Use?
You can choose a platform designed specifically for developer surveys such as DX or Culture Amp, or a more general tool like SurveyMonkey, [Google](https://cloud.google.com/?utm_content=inline+mention) Forms or Qualtrics.

### What Should You Avoid?
Two intrinsically linked things to avoid are leading questions and validating assumptions.

**Validating assumptions:**Often, engineering leaders are tempted to ask questions in a way that they hope validates their own assumptions. This isn’t helpful. Not only is the question neither fair nor balanced, it may lead to you to work on an area that isn’t a big developer pain point. This may create resentment and distrust and undermine future surveys and engagement.**Leading questions:**Asking leading questions may not yield the response you’re looking for. For example, if you ask your team to rate statements like “[task X] provides a bad experience,” you may get mixed responses. For one thing, it is a leading question they may not agree with nor have an opinion about, and also the framing and format of the question isn’t suitable. Instead, ask more open questions like “rate [task X] from 1–10, where 10 is a good experience.”
**Main takeaway: **Use formats that lend themselves to better answers; rankings or ratings are a good way to go.
### What Topics Should You Ask About?
#### Importance of Tasks
To avoid confirming your own assumptions, ask developers how important a specific issue is to them, then ask how satisfied they are with it. For example:

- How important is the speed your team ships code to your developer experience?
- How happy are you with the speed with which your team ships quality code?
#### Pain Points
Port’s DevEx survey template ([email us for a free copy](mailto:%20info@getport.io)) tries to find out developers’ biggest [pain points](https://thenewstack.io/boost-developer-productivity-by-reducing-their-paper-cuts/), so you can help ease friction by using the portal’s features. Questions might include:

- Rank from 1 to 5 how much
**time is spent on specific tasks**in a typical week, including reviewing pull requests (PRs), writing new features, managing incidents, solving bugs, doing ops-related tasks, refactoring code and meetings. - Rank the
**top blockers of day-to-day work**, such as waiting for pull requests (PRs) to be reviewed for DevOps to resolve requests, finding owners of services/APIs or waiting for other people to provide knowledge, permissions or access. - Estimate how much
**time developer onboarding takes**.
- Rank 26 of the
**biggest pains developers experience**during work planning, development, shipping and managing production, including Jira tickets management, scaffolding a new service to toggle feature flags, or understanding and troubleshooting outages.
Open-ended questions help identify issues you haven’t already considered, particularly when many developers share the same complaint.

Rerun pain-point surveys after you begin using the portal and implementing features. This tells you if your changes made a noticeable difference.

#### Features
You might want to ask which [ self-service capabilities](https://www.getport.io/product/self-service) developers would find most useful. Offer a list of potential new features and ask developers to rank their top, second and third priority. This helps you prioritize which self-service action to put in place.

Use this same format to ask what types of **monitoring or management features **developers are most interested in. And you can use the same format for other portal capabilities.

## Get Feedback About the Portal
After developers have been using the portal, change your survey to get feedback on it. For example, if you want to know about the software release experience after the portal’s implementation, you can ask developers to rank from 1 (very easy) to 10 (extremely confusing/difficult) things like:

- The current portal layout is easy to navigate.
- Releasing an app to production is confusing.
- I can easily find all my team’s deployments and releases.
- If a deployment (develop), promotion (stage) or release (production) fails, I am able to quickly identify where it failed.
Other questions might include:

- What is the average time you wait to receive assistance from the engineering team to resolve a deployment or release problem during business hours?
- If there’s one thing you’d change or add to the portal or in the deployment/release process, what would it be?
Use the feedback to make improvements to the portal, then rerun the survey to see if the improvements improved developer experience.

## Evaluate Satisfaction and Well-Being
Developer experience goes beyond the themes, pain points and features above. If you want to know [how developers actually feel](https://thenewstack.io/how-intercom-ships-industry-leading-developer-experience/), ask questions like:

- How productive do you feel? (1 is not productive at all; 10 is very productive.)
- How satisfied are you with your ability to be productive? (1 is not satisfied at all; 10 is very satisfied.)
- What are you most stressed about on a day-to-day basis? (Include options, rankings and open fields.)
- What is the one thing you would change about your experience?
Make sure to provide one or two open-ended questions for each topic or theme. Asking respondents to share longer, better or alternative explanations provides a better understanding of the situation.

Answers to these questions and the actions you take in response can help you retain staff, improve work conditions and improve collaboration and communication. DX offers a [survey template](https://getdx.com/guide/devex-survey-template/) that you can download.

## Act on the Survey Results
Asking questions is just the first step in using a survey to improve developer experience. The next step is to use the results to make changes that address the biggest pain points and barriers to productivity and satisfaction. I’ll talk more about that in part 2 of this series.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)