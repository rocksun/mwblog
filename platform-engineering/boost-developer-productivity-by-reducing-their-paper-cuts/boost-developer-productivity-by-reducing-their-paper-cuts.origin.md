# Boost Developer Productivity by Reducing Their ‘Paper Cuts’
![Featued image for: Boost Developer Productivity by Reducing Their ‘Paper Cuts’](https://cdn.thenewstack.io/media/2024/05/ac0f76ed-joyful123-1024x576.jpg)
We’ve all had a paper cut. They are small but leave an inordinate impact. And they often disrupt our ability to type and deliver work.
A poor developer experience is death by a thousand paper cuts. That’s why
[Jason Kennedy](https://www.linkedin.com/in/jasonhkennedy/) and his engineering experience team at [One Medical](https://www.onemedical.com/) are looking to remove the sources of each little pain in the cut.
The company operates primary-care clinics and has adopted a technology-powered approach to health care — grounded in a belief that developer experience affects patient experience. This has the company applying an almost meditative approach to both user experiences, one grounded in observation, inquiry and empathy.
One Medical focuses on
[developer joy](https://thenewstack.io/measure-developer-joy-not-developer-productivity-atlassian-says/), assuming that [developer productivity](https://thenewstack.io/how-google-unlocks-and-measures-developer-productivity/) will be the end effect.
## From Engineering Efficiency to Engineering Experience
When One Medical’s DevEx team formed in mid-2022, it was originally called engineering efficiency but soon went through a rebrand to focus on the whole engineering experience.
In October 2022, Kennedy joined the company as senior engineering manager and team lead, in part because the team was already established, signaling that there was cross-company buy-in already.
“Someone internally had already done some of the legwork and convinced the org that this team was needed,” which he said was something missing at other businesses he’d worked at before.
The EE team, as they call themselves, focuses on creating an efficient and
[joyful development experience](https://thenewstack.io/how-intercom-ships-industry-leading-developer-experience/) for One Medical engineers. More recently, the team is expanding its scope to include the whole software development life cycle, irrespective of what engineers are working on. This has them expanding beyond local development on the monolith into service creation, testing, data engineering and maintenance.
With this broader focus in mind, Kennedy’s team has expanded from four to eight engineers, including some quality engineers who were already doing platform work — all set to serve One Medical’s 150 full-time engineers. As almost “platform engineers of quality,” these new additions are responsible for working on maintaining the test frameworks, developing an overall companywide testing strategy and improving the engineering experience across several platforms.
## Gemba: Understanding Developer Pain Points
About 18 months ago, One Medical kicked off its DevEx journey with a survey of the whole engineering organization, looking to identify the most impactful areas to work on.
“We really want to know what’s going on, and not just guess what we think should be better,” Kennedy said. “We really want to ask engineers what’s going wrong. It’s really driven by what the engineers are seeing. They know where the biggest problems are.”
One Medical follows the lean management practice of Gemba. Japanese for “actual place,” this involves observing the reality of the work in action. When permitted, the whole staff, including leadership, is encouraged to shadow clinical operations. This grounds everyone, Kennedy said, in the purpose of “what we are doing — we’re giving care to patients and we’re improving outcomes, and our work is informed by making that better.”
Similarly, the engineering experience team kicked off with and continues to shadow engineers, asking questions about the painful paper cuts developers work with every day. This tightens
[developer feedback loops](https://newsletter.getdx.com/p/measuring-developer-productivity) and builds empathy around the developer experience.
All engineer walks are done virtually.
## Look Out for Paper Cuts, Big and Small
Beyond continued Gemba walks, in early 2023, the engineering experience team introduced a weekly Slack poll, which included the request, “Tell us what impacted your productivity this week.”
Several answers were given, like issues with local development, testing and database environments, as well as custom, fill-in-the-blank options. These weekly polls kept the pulse on the developer experience, and then, monthly, Kennedy’s team would aggregate this information to see how things are trending.
They also ran a quarterly
[Net Promoter Score Survey (NPS)](https://medium.com/a-technical-leaders-toolbox/the-developer-nps-why-are-you-not-measuring-this-cdf942703aa8).
On a quarterly basis Kennedy’s team takes everything under consideration to see which important concerns float to the top.
Last year the survey revealed that the data in their testing environments was not a small cut but a major pain. In response, the One Medical engineering experience team created scripts and processes where teams could reset their testing environment in under half an hour.
“We got rid of the need for them to really dig and debug and go figure out, ‘OK what’s actually broken in this environment?’ before I actually do my testing,” Kennedy said.
Now developers can reindex the database and testing environment completely. “That’s probably one of the more intense ‘break glass’ options. We’ve got a couple other options, [but this is a] shorter turnaround.”
His team also looks for
[quick wins](https://thenewstack.io/at-platformcon-for-realtor-com-success-is-driven-by-stories/). An early one included developers complaining about having to log into Amazon Web Services every time they had to start up the monolith. It turned out there was something in the startup of the server that was triggering something seemingly unrelated in AWS that would unnecessarily require a re-login. His team spent a couple days building a way to skip this extra step for a big DevEx win.
## How To Collect Developer Feedback
For much of 2023, the developer survey process was fully manual.
“We began to ask ourselves, ‘How do we want to improve this feedback mechanism? Do we as a team want to put effort into building out our own surveys, really investing in an internal way of getting this feedback? Or do we want to go buy something off the shelf that we know that we can just operate?’”
For Kennedy’s team and their objective of increasing developer joy and efficiency to then improve patient outcomes, building their own developer feedback platform was simply not a priority. They adopted the
[DX developer insights platform](https://getdx.com/).
At the time of our interview, the One Medical engineering experience team had just completed its second “snapshot,” which is a survey run across an entire engineering organization. Each snapshot is very thorough, he said, but takes just five to six minutes for developers to complete. His team then gets a “breadth and depth of information.”
## Sometimes a Monolith Cannot Stand Alone
Developer experience is a sociotechnical endeavor, so what are some of the technical changes Kennedy’s team is working on in response to developer feedback?
From the start, they knew that developers were spending a lot of time on local development tasks, so these DevEx engineers worked on the experience of those working on One Medical’s cloud-based, Ruby on Rails monolith. They revamped the local development and scripting and adopted GitHub’s Codespaces to create a one-click cloud development environment.
With a monolithic architecture, Kennedy observed, it’s difficult to establish a sense of ownership at the team level, which makes changes and service creation harder, so his team is looking to reduce reliance on the monolith as “a way to create an environment where a team can operate a lot more autonomously,” Kennedy said. “They can make decisions and operate as quickly or as slowly as they want without running into really old code that nobody knows anything about.”
This move doesn’t just look to increase developer joy, but infrastructure engineer joy as well.
The team has begun laying down
[golden paths](https://thenewstack.io/how-to-pave-golden-paths-that-actually-go-somewhere/), including the approved, easier paved road to create a new service, but not a required one. Similarly, developers are still welcome to set up and maintain a full local environment, but they are encouraged to go down Codespaces’ path of least resistance.
## What One Medical Doesn’t Measure (Sort of)
So far, 2024’s obsession with
[developer productivity](https://thenewstack.io/a-guide-to-measuring-developer-productivity/) hasn’t hit One Medical. Not directly anyway. Back when they used the weekly Slack poll, they tried to make time estimations via the question: How much time are you losing to local development maintenance?
“If you translate that into developer costs and the costs of the cloud development environments, then you get an environment in a minute and require no ongoing maintenance.”
Kennedy said that this translated to them being “able to show this is how much it’s costing developers to do all this maintenance, and this is how much it costs for them to have basically no maintenance at all.”
The team has since shifted away from that weekly poll to a combination of continued Gemba practice and the results from the DX platform, as well as follow-up interviews: “Hey, your team was really good at this metric — let’s talk about what you’re doing well,” and “hey, your team identified this as something that you need some help with. Let’s dig into where you might have some specific problems.”
Before Q2 of 2022, One Medical didn’t have a developer productivity team, although there was an infrastructure team, a site reliability engineering team and occasionally a platform team. But even though this focus on DevEx is relatively new, there has been top-down buy-in from the start. Kennedy said of the company’s leadership, “They recognize the importance of developers having a good experience and how much that contributes to certainly the overall employee well-being, but also we’re going to have a better product if engineers feel better about working on things.”
## Developer Productivity Is a Result, Not an Objective
Since it’s a long-proven assumption that
[happy developers are productive developers](https://www.sciencedirect.com/science/article/pii/S0164121218300323) (and vice versa), the One Medical engineering experience team doesn’t feel obliged to define and measure developer productivity.
Of course, developer onboarding experience matters, and new engineers can now spin up their environment on Day 1 and commit stuff on Day 21. As Kennedy’s team has access to far more metrics in DX, it’s looking at things like ease of release and time for deep work, like developers rating interruption frequency and length. One Medical also looks to limit recurring meetings and even practices No Meeting Tuesdays.
“We as the engineering experience team probably can’t affect that super directly on an org level. But what I can do is bring these results to our manager group.” For his own teammates, every quarter Kennedy asks them to look at recurring meetings and ask: Is this meeting still needed? Is this the right time to have this meeting? If the response is that the meeting isn’t needed, he promises that it’s not going to show up again.
Q2 sees a focus on continuous deployment to help reduce the amount of time developers have to wait for their code to reach production.
“Because I know, when I was a developer, what brought me joy is getting stuff done quickly and getting onto the next thing and getting that feedback hit of ‘Cool, my stuff is working, let’s deploy to production.’ Then I’ll move on to the next one.”
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)