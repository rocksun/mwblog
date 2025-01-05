# Top Problems Developers Need You To Fix Now
![Featued image for: Top Problems Developers Need You To Fix Now](https://cdn.thenewstack.io/media/2024/12/6dec8a87-fix-api-problems-1024x576.jpg)
Many software developers started tinkering with code as kids and kept doing it until they turned it into a career. The thrill of making a function that works or successfully troubleshooting a tricky bug isn’t age-restricted — it feels good to be productive.

At the same time, a surprisingly high number of developers experience [burnout](https://thenewstack.io/the-developer-crisis-mental-health-burnout-and-retention/) at work. It’s a significant problem in many organizations, and the [costs](https://thenewstack.io/the-hidden-costs-of-chasing-five-nines-in-availability/) can be exceptionally high for development teams.

Why are developers getting burned out if they enjoy their line of work? The catch is that developers spend as little as [10% of their day writing code](https://www.software.com/reports/code-time-report). The tech industry has been wrestling with this problem for years. In 2009, Paul Graham, a founder of Y Combinator, called for tech management to be more aware of the “[maker’s schedule](https://www.paulgraham.com/makersschedule.html)” and reduce the overhead of manager-driven disruptions.

If anything, makers’ schedules are even more fragmented now than 15 years ago as complications like globalization, [containerization](https://thenewstack.io/year-in-review-containers-get-smaller-faster-more-secure/) and [threat actors](https://thenewstack.io/developers-are-key-to-stopping-rising-api-security-threat/) proliferate. Companies have tried to compensate by investing in workplace culture, project management tools and products that promise a better developer experience, but those efforts haven’t paid off. Rates of burnout among tech employees have increased from [around 57% in 2018](https://www.forbes.com/sites/laurencebradford/2018/06/19/why-we-need-to-talk-about-burnout-in-the-tech-industry/) to [as high as 71% in 2024](https://www.cio.com/article/657960/burnout-an-it-epidemic-in-the-making.html).

It’s time to take a different approach and get to the root of the problem. If developers are frustrated and burned out, we should talk to *them* about improving their working conditions. Below, I’ll walk through some common challenges and show you how to take a developer-focused approach to solving them.

## What Do Developers Want To Change?
In the debate over whether to focus on developer productivity or developer experience, a key point is often overlooked: When people are happier, they do more and better work. If teams want to improve their productivity, they should start by understanding what’s holding back individual developers.

We spoke with experienced developers and engineering leaders at API World recently and asked them [a simple question](https://www.youtube.com/watch?v=bazRLYt_Cb8&t=2s): “What were your API pain points in 2024?”

The answers echo what we’ve been hearing for years and will be familiar to anyone who’s worked in the industry. The people we spoke to had different problems on their minds, but they tended to fall into five categories: streamlining data access, better collaboration, improving security, building consistency and discovery, and getting support for API program investments.

Each of these is a productivity blocker for developers — an aspect of their jobs that takes crucial time and attention away from coding. These widespread problems add disproportionately to developers’ cognitive loads, increasing burnout and driving down productivity and satisfaction.

### Streamlining Data Access
APIs make more data available to more users than ever before. However, the available data might not be what people actually need; sometimes, it’s in an unworkable format or from a blocked geographical region. Beyond the issue of access, duplicate data and inconsistent formats and protocols often take up far too much of API teams’ time.

We spoke to [Adam Malone](https://www.linkedin.com/in/adamdmalone), director of worldwide solutions engineering at [Hasura](https://hasura.io/?utm_content=inline+mention), about [improving data management](https://www.getambassador.io/blog/5-api-development-tips-from-engineers-at-api-world). His suggestions fall into three areas:

**Understand your data pipeline**: The team that designs your data models needs to know how data will be consumed, produced and used. Is your data traceable? Mutable? How are you validating data at different stages? What’s a data object’s life cycle and lifespan? It’s not enough to produce data that meets one specification; large, complex organizations need APIs that can handle large, complex data throughout their life cycle.**Increase and improve data modeling**: Data management is a concern during development and in production. The knowledge you gain from taking a deeper look at your data pipeline should inform how you model data during the early stages of your API life cycle. Knowing how your data will be used can help you choose appropriate data structures, design suitable indexing strategies and optimize for read and write operations. Data models can help you maintain data integrity and performance in future iterations.**Secure your data**: Data security and compliance are more important than ever. Hacking methods are increasingly sophisticated, and the stakes have only gone up. Proper security, including encryption, authentication, authorization and data validation, is crucial for the long-term viability of your API programs.
This brings us to the next big blocker for API teams.

### Addressing Security With Fewer Headaches
Over 40% of API World attendees cited security concerns as their top frustration (based on a survey the Ambassador team conducted during the conference). The issue is evergreen: [API security](https://roadmap.sh/best-practices/api-security) is never done, because the threat environment is always changing. You’ll soon pay the price if you neglect security. By this point, most people in the tech industry accept that reality.

Frustration builds — as it often does — when security measures are inconsistent, time-consuming and complicated. As a result, users start circumventing security practices. Some violations are minor, like password reuse. Others are more serious, like sharing admin credentials. Others will completely sabotage your network security and data integrity, like salespeople using actual customer data in demonstrations.

These problems aren’t caused by bad actors — they happen because security policies are so cumbersome they get in the way of people doing their jobs.

The [best security policies](https://www.getambassador.io/courses/apisec-api-gateway-security-best-practices) are those you can implement consistently across your organization and that employees follow because they involve simple, practical routines. For API programs, this often means using [an API gateway](https://www.getambassador.io/products/edge-stack/api-gateway/security-authentication).

Authenticating to an API gateway grants access to many valuable resources with a single login. The logic of the login process is straightforward and short, so there’s no temptation for employees to circumvent it. It also makes user activity traceable and credentials easier to revoke if needed.

### Collaborating Better
API developers know they need to collaborate. It’s almost intrinsic to APIs as a technology — the “I” stands for interface. You need communication from the start if you’re building an interface that works for people on both sides.

But just because collaboration is necessary doesn’t mean it’s easy. The proliferation of tools in many API-driven organizations can get in the way of human communication. People need to talk to people, not just to tools, and an [API development platform](https://www.getambassador.io/blog/platform-engineering-solution-common-devops-challenges) should make that more manageable by breaking down silos and simplifying toolchains.

While [API documentation](https://www.getambassador.io/blog/api-documentation-done-right-technical-guide) is certainly part of the solution, the priority should be making collaboration less painful. One area where you might find room for improvement is shortening the feedback cycle for developers working on new features.

When developers spend more of their time in the [inner development loop](https://www.getambassador.io/blog/boost-developer-velocity-optimizing-feedback-loops), they’re more productive and can integrate new ideas faster. In turn, they can share challenges and ideas with users sooner, enabling them to work together more effectively.

Containerization has been a boon for external stakeholders, but it significantly slows down individual developers. The best container-based development environments let developers access ephemeral environments with little overhead, allowing them to stay in the inner dev loop longer.

Look for an API management tool that offers easy access to [shareable mock servers](https://www.getambassador.io/docs/blackbird/latest/guides/mocks) and full [IDE integration](https://www.getambassador.io/docs/blackbird/latest/guides/code). This helps developers build and test API endpoints in a production-like environment without relying on lengthy build processes. Improvements like this significantly lessen the cognitive load on devs, so they can focus more deeply on their most critical work.

### Building More Consistency and Discovery
Another challenge we heard from engineering leaders was delivering consistent code across a portfolio of APIs. Ensuring consistency within a single API is essential if you want your code to work smoothly, but most organizations use and produce dozens of APIs across their applications, making consistency more challenging and important.

Consistent API functionality and data models matter:

**Inconsistent code is virtually always less secure**: How can you know that you’re following best practices when your APIs have different auth protocols?**Inconsistent APIs = developer toil**: Gaining access to APIs is often a frustrating starting point for many developers when faced with a lack of a consistent and accessible API catalog.**Users are more successful when they can predict how an API will work**: No one wants to read and internalize documentation on every API they use. Developers tend to generalize from a few endpoints and methods to other APIs — you need to ensure that won’t backfire.**Efficient collaboration from design through production**: Did developers build what they said they’d make at the start? Is the data delivered meeting user expectations? Are your data formats consistent across all read/write operations?**Planning future updates and versioning**: To understand what changes users can tolerate without introducing a new version, you must know precisely what you deliver throughout your current APIs. Inconsistency makes that problematic.**Discovery is more manageable when people know what they’re looking for**: Software support teams for Microsoft Excel used to field thousands of feature requests for features that were already available. The problem was discoverability: Excel was incredibly feature-rich, but the menus and toolbars had been growing continuously — not to mention chaotically — and no one could find what they needed. The same happens with large API portfolios; inconsistency only worsens the problem.**Observability gets easier when APIs are easily compared**: If you want to compare the performance and usage patterns of different APIs or endpoints, remember the principle of scientific control. If your APIs are inconsistent, you can’t make meaningful comparisons, and you can’t apply the hard-won wisdom from one resource to another. If you control formats and enforce governance, you’ll find it much easier to understand the differences.
Your [APIs need protocols and standards](https://www.getambassador.io/blog/four-ps-platform-engineering), and your teams need tools to facilitate governance and compliance. A well-engineered platform includes automated tools like [boilerplate code generation](https://www.getambassador.io/blog/reduce-boilerplate-time) to do some of the heavy lifting.

Again, you want your developers to focus on innovation and iterating on their code. Look for ways to reduce the burden of rote work and manual checks, and you’ll eliminate much of the drudgery and fatigue in developers’ days.

## Making the Case for API Program Investments
A common factor leading to developer burnout is a sense that their work isn’t valued. If leaders aren’t confident in advocating for the value of APIs, their teams experience the downstream effects. However, if leaders are effective advocates, developers benefit from seeing the impact of their work and feel like a valued part of the organization.

Fortunately, it’s not hard to find reasons to like APIs from a business standpoint. Some will be unique to your organization. You need to fully understand the use cases for your APIs and be able to explain how you’re addressing those needs.

The benefits can be broader, too:

#### APIs Create New Value From Existing Data
By decomposing data into smaller, purpose-built units and offering it on a self-service basis, APIs make data useful to more people. APIs also let users control their costs, which helps you attract a broader, more sustainable customer base.

#### Building APIs Can Be Fast
Building APIs on a developer-friendly platform can be [even faster](https://www.getambassador.io/blog/blackbird-accelerate-api-dev-hackathon). Developers can quickly iterate on new ideas, allowing them to test new features and business models with little overhead.

#### APIs Give You Control Over How You Use AI — and How You Don’t
Everyone needs to plan for adapting their processes and products for AI. While specialized AI-based tools deliver much value, AI-based products are still pretty questionable.

Your [API development teams](https://roadmap.sh/api-design) can use AI to increase productivity at multiple stages in their workflow without compromising the integrity of your API products. This is [more cost-effective](https://www.getambassador.io/blog/5-api-development-tips-from-engineers-at-api-world) than large-scale AI product launches and a good way to familiarize yourself with AI’s possibilities and limitations.

Documenting your API process improvements is key to making the case for your API programs. We focus on individual developer experience because developers are more productive in the [inner dev loop](https://thenewstack.io/api-world-4-api-development-tips-to-drive-business-impact/) of coding, building and testing. They’re also happier, which pays off in the long run with better business continuity and reduced employee onboarding costs over time.

Engineering leaders need to speak up: API teams are contributing tremendous value to their organizations and could do even more with tools and processes that effectively address their biggest frustrations.

## Narrow Your Focus To Build a Broader Solution
The list of challenges above is sizable. Tackling them might feel daunting, especially if you’re trying to face them one at a time. Fortunately, you don’t have to.

Product management approaches to APIs are exhausting and counterproductive; doing too much at once leads to wasted effort and resources. API development benefits from a holistic approach that can reduce friction, improve developer productivity, and alleviate stress and cognitive load. Teams must look beyond one-off solutions to rethink the API management paradigm.

Counterintuitively, the answer is to try to do less — and as a result, you’ll get more done. At Ambassador, we encourage API teams to shift their focus away from API product management to a more concrete, relevant unit of work: [the endpoint](https://nordicapis.com/managing-up-the-endpoint-lifecycle-matters-more/).

API as a Product isn’t a bad concept, but its true focus is API consumers. It’s just not a good way to manage developer workflows. The internal dev loop needs an internally focused management approach, which means refocusing on the unique work that API developers do — which is to write and debug code, one endpoint at a time.

If you want to take a slightly broader approach than endpoint management, [platform engineering](https://www.getambassador.io/blog/platform-engineering-main-goal-supporting-developer-experience) is an approach to DevOps and tooling that starts from a similar idea. A lot of DevOps and developer tool programs are designed around the needs of site reliability engineers (SREs). SREs do invaluable work, but they’re externally focused and work to ensure consistent service delivery to customers. Platform engineering shifts the focus back to the daily workflow of the engineers who build your APIs.

Endpoint management and platform engineering pay off for a few reasons. They lessen the cognitive load on developers by reducing non-coding workloads. They let teams follow the “maker’s schedule” more closely, providing extended blocks of focused work. And they reduce unnecessary friction with tools shaped around fixing the self-reported frustrations of actual developers.

Meeting the unique needs of dev teams can pay for itself, especially when the tools you choose are lean, purpose-built and developer-friendly. This single approach can prevent and address many of the most common developer complaints, improving developer experience *and* productivity.

## Pave a Better Path Forward
API development will never be pain-free, but identifying the biggest day-to-day obstacles can help teams move in the right direction. When you change processes and tools on your API teams, the goal should be to reduce developer toil: Put control in developers’ hands so they can tackle the friction that most affects them.

If you can help your developers make this shift, you’ll see a big payoff. They will write more and better code and experience less burnout. Give developers access to the tools that make them more productive. They’ll build more powerful APIs and be much happier doing it.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)