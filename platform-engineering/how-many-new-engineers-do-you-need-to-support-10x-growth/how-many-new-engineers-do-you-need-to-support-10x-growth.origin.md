# How Many New Engineers Do You Need To Support 10x Growth?
![Featued image for: How Many New Engineers Do You Need To Support 10x Growth?](https://cdn.thenewstack.io/media/2024/05/0e4b22fd-hiring-new-engineers-growth-1024x576.jpg)
“We’d like to be able to service 10 times as many users or customers, but we don’t necessarily want to have 10 times the number of engineers.”
That’s how
[Andrew Keogh](https://www.linkedin.com/in/andrew-keogh-ie/), director of product development operations at [Workhuman](https://www.workhuman.com/), a social peer-to-peer employee recognition platform, kicked off his conversation with The New Stack.
Workhuman has really grown in popularity over the last couple years, Keogh said, but now technology and processes need to be able to scale along with it. The company currently has more than 7 million users, but is focused on scaling significantly by 2030.
So how does a SaaS company with more than a $2 billion valuation prepare to deliver on its goal of making work more human? How can it be sure its technology can scale without overscaling its tech team? By focusing on developer experience and by embracing a
[platform engineering](https://thenewstack.io/platform-engineering/) strategy.
## A Shared Responsibility to All Customers
Around three years ago, Workhuman began investing in platform capabilities. The platform team looked to invest in cross-functional initiatives, including new shared services and disaggregating monolithic applications.
These transformations, Keogh said, are beginning to bear fruit.
“It’s understanding the bounded context in which we operate from a domain perspective,” he explained. “We’re determined to keep things moving forward into this constant scaling of our feature set.”
Their technology team is now divided into an architecture group, a platform group, an infrastructure group and product engineering, with about 100 engineers working on common services, tech modernization and scaling projects for the 200 engineers on the value-stream aligned product teams.
“We’ve set up ourselves to have a set of core responsibilities, but there’s [also] a shared responsibility to our users and customers,” Keogh said.
He and the team of five are setting up a strategy for a stronger developer experience with a focus on developer productivity.
“Not so much in measuring lines of code or anything archaic like that, but in terms of ensuring that there are as few blockers as possible,” he clarified, “and that [developers] are able to deliver their best work as frictionless as possible.”
All in addition to adopting a strategy to make sure everything — the people, processes and technology — can readily scale alongside the business.
## Metrics Will Vary
When Keogh joined Workhuman in 2020, the company was already tracking the core four
[DORA metrics](https://thenewstack.io/google-says-you-might-be-doing-dora-metrics-wrong/) — deployment frequency, lead time for changes, change failure rate and failed delivery recovery time. Even in attempting to collect this data, it became apparent that Workhuman engineering was releasing software in a number of different ways across a number of independent applications.
Part of his role has evolved into making sure that teams have an accurate view of where they are, compared both to their past results and to other teams, as well as enabling teams to identify what improvements they can make.
“By empowering our engineers, we enable them to remove the blockers that they have locally.”
— Andrew Keogh, Workhuman
DORA results vary heavily by team — and that’s OK, Keogh added. For example, the mobile app team simply cannot release daily because its deployment frequency is externally controlled by the major app stores.
Each team has its own set of practices, he said, as they resist the Scaled Agile Framework (SAFe) and other more top-down, guardrailed paths to scaling.
“We encourage our teams to find and use their own way of working, so each team will have its own local flavor. It’s about giving them the metrics and the tools to be able to understand where their issues are, and the flexibility they need to work at their own pace and style to resolve it,” Keogh said.
“By empowering our engineers, we enable them to remove the blockers that they have locally.”
Workhuman is investing heavily in platform engineering and creating paved roads or
[golden paths](https://thenewstack.io/how-to-pave-golden-paths-that-actually-go-somewhere/) — the smoothest ways to get things to production.
“What sort of investments do we need to make to enable us to be able to operate at that scale, in terms of technology, in terms of our people?” Keogh said. “We’ve made strides, but we’re probably at the beginning of that journey. We’re really beginning to accelerate into it now.”
## Does Generative AI Accelerate Developer Productivity?
Workhuman is exploring how
[generative AI](https://thenewstack.io/ai/) (GenAI) and especially code generators like GitHub Copilot can enable Workhuman engineers to [unlock developer productivity](https://thenewstack.io/how-google-unlocks-and-measures-developer-productivity/). Currently, 10% of its engineers are trialing coding assistants to find where and if [GenAI enhances the software development life cycle](https://thenewstack.io/how-generative-ai-can-increase-developer-productivity-now/).
“We’re looking where the opportunities are for us, and then will double down on investments,” as Workhuman looks to accelerate AI adoption throughout 2024. In order to do this, Keogh continued, “we’ll be measuring ourselves against a number of metrics to see that we are actually seeing some benefit from the tools, both quantitative and qualitative.”
Workhuman is focused on innovation utilizing AI, which Keogh believes will allow the engineering team to “deliver higher levels of value more frequently to our customers.”
The platform team has established a baseline, especially for cycle time and deployment frequency, that they are measuring. It sends out in-the-moment surveys using DX’s real-time intelligence product,
[PlatformX](https://getdx.com/products/platformx/), to participating engineers to measure GenAI adoption and impact. For example, they can answer questions like:
- How useful do you find this GenAI tool?
- What’s the level of difficulty in adopting it?
- How is it impacting your ability to do your job?
- Has this tool made your life easier or not?
“We are listening to engineers from a range of teams with different roles to understand their needs,” Keogh said. By experimenting, they’ll know which tools are useful — or not — for each type of engineer or use case. Perhaps, for example, code generation isn’t particularly useful for a QA engineer, but it can effectively reduce toil for unit test creation.
“It’s not only to understand if we got some ROI, but also where we should lean into first. So, as the technology [GenAI] matures, we’re taking advantage of the initial use cases and then, over time, we can look to extend.”
Workhuman is providing
[AI guidelines](https://thenewstack.io/tech-works-when-should-engineers-use-generative-ai/) on personally identifiable information (PII), as well as a lot of guidance around the validity of suggestions and considering the [security of the underlying libraries](https://thenewstack.io/ai-llms-and-security-how-to-deal-with-the-new-threats/).
“Data is critical. Security is critical,” Keogh emphasized, “But we are also focused on deploying this tech responsibly.”
## Actionable Developer Feedback
“Receiving feedback and acting on it is a priority for us, therefore, we have a lot of listening posts,” Keogh said about how Workhuman collects actionable developer feedback.
This is a combination of local team health checks and a quarterly developer survey from
[DX’s DevEx 360 product](https://getdx.com/products/devex360/), which Workhuman started piloting about 18 months ago, he said, “to look into how properly to measure developer experience and find ways in which we can help boost developer productivity.”
“People don’t suffer survey fatigue as long as they can see actions being taken.”
— Andrew Keogh, Workhuman
“What I love about DX is that it’s able to show what’s local to a team [and] can be fixed locally. Then also surface more systemic issues for cross-team initiatives to start to address,” Keogh said. “We’re getting different stratifications of feedback, which is not something we had before.”
Before DX, he said, the platform team was trying to deliver services in a one-size-fits-all fashion, without necessarily understanding the nuances in different application teams. With this “deeper, richer dataset,” he said they can take different approaches, including helping engineering managers discover how to help their teams and uncovering patterns shared by a few teams.
So far, Workhuman boasts more than 95% participation in the quarterly DX developer surveys, “so we can see that people really see the value in participating and then the changes that get made as a result.”
The engineering organization also compares itself against DX’s industry benchmark data, which highlights how the top 10% of organizations score within the developer insights platform.
## Common Barriers to Productivity
One thing they’ve uncovered is that, as the company has grown, so too has its number of meetings — a known trigger of context switching, which is a known barrier to productivity.
Workhuman is strategizing about how to be intentional about planning meetings and who needs to attend.
This is an effort to be more respectful of interruptions to focus time across the organization. Workhuman has already witnessed an improvement between the first survey and the most recent, in April.
DX has also surfaced (and made investments in) improving documentation to increase platform adoption. The platform team has adopted the
[Diátaxis](https://diataxis.fr/) systemic approach to technical documentation, which focuses on creating four types of docs: tutorials, how-to guides, explanations and reference information.
GenAI’s ability to discover and interrogate Workhuman’s tech stack should help even more, he explained, compared to relying on memory of why things were chosen for what purpose. “Clear ownership leads to documentation [and] leads to good maintenance practices.”
## The Risk of Survey Fatigue
Workhuman also uses its own
[employee Moodtracker survey](https://press.workhuman.com/press-releases/workhuman-launches-moodtracker/) for cross-organizational feedback. Moodtracker is a freely available tool that asks questions about team health and employee engagement.
“Sometimes we can get concerned about the sheer number of surveys that we have, but I think we need to really consistently ask for feedback,” he said. “People don’t suffer survey fatigue as long as they can see actions being taken.”
A multiplicity of surveys could be a natural effect of being an employee feedback company. “Making work more human is at the core of everything we do,” Keogh said. As an employee recognition platform, he continued, “The levels of collaboration and willingness to assist each other are off the charts here in a way I haven’t observed in other companies that I’ve worked for.”
Of course, the secret to avoiding survey fatigue is making sure your engineers know that you’re actually doing something in response to the results. The platform team is also leveraging Slack and demos to amplify what’s worked for particular teams.
“We’re learning from teams and each other,” Keogh said. “It’s enabled us to have multiple experiments running and, when things work, we’re able to share those learnings and improve.”
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)