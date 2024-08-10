# 5 Lessons For Building a Platform as a Product
![Featued image for: 5 Lessons For Building a Platform as a Product](https://cdn.thenewstack.io/media/2024/08/b965a04e-calendar-1763587_1280-1024x748.png)
In 20 years of working in platform engineering and 10 years of building [Platforms as a Product](https://thenewstack.io/platform-as-a-product-in-4-steps/), here are five critical lessons for creating a successful Platform as a Product.

As someone who has been working on [platform engineering](https://thenewstack.io/platform-engineering-is-for-everyone/) for two decades, explicitly building platforms as products, I’ve built platforms for some of the world’s most recognizable brands and founded companies that have gone on to be acquired by much larger organizations. Along the way, I’ve made a lot of mistakes and had a few successes.

I aimed to share my most important learning in a recent PlatformCon talk, “[20 Years’ Platform Engineering, 10 Years’ Platform as a Product, 5 Lessons Learned.](https://www.youtube.com/watch?v=D5KVXPyuvd4)” I wanted to expand upon several topics in this article.

Let’s dive into the five lessons that I regard as [hard-won takeaways](https://www.infoq.com/presentations/project-success/) (because things can and do go wrong!) from my Platform as a Product experience:

- Employ a “product mindset.”
- Find the right abstractions for your organization.
- Democratize your platform.
- Everywhere is brownfield, and everything is complex.
- Day one is easy; day two thousand is hard.
## Employ a Product Mindset for Building a Platform
What does “[product mindset](https://thenewstack.io/platform-engineering-demands-a-product-mindset/)” mean when building a platform? In a [white paper on platforms as products, which I wrote with Joe Fitzgerald](https://wearemomentum.ai/whitepapers/2017-platform-as-a-product-whitepaper.pdf), we define thinking about the “productization” of the platform that can reshape how we think of building platforms:

“Your platform is not an off-the-shelf piece of software; it is an evolving set of reusable services, integrated with your existing systems, that creates valuable outcomes for your business. The platform’s capabilities should change in response to the needs of its users — your app developers — among whom it is a recognizable internal brand. In other words, your platform should be treated as a product.”

If you don’t build from a product mindset, the platform will become project-orientated. It will likely be restricted to a specific start and end date with a release and certain features, operating much like most short-term projects. Like most off-the-shelf software releases, it goes out into the world, and we hope for the best. Then, we repeat this project-focused process. This incremental approach to platform building isn’t aligned with the definition given above and leaves essential opportunities on the table because sound platform engineering is *more than just engineering*.

The user is central to building great platforms. What do users want, and what will they use? The platform evolves based on this use and the feedback we actively seek from our user base. Like most things, it should respond to changing development or business needs and use patterns to deliver value.

A mix of feasibility from an engineering perspective, viability from a product management perspective, and desirability from a design and usability perspective underpins what we mean by “successful product.” This means that while platform engineering is necessary, it isn’t sufficient on its own because a successful platform product requires product management and design skills.

### Key Takeaways
Bringing real and ongoing value to the Platform as a Product demands understanding its users, first and foremost, and keeping the following in mind:

- Platform engineering is just one part — product and design are also essential.
- Collaborate with users and get firsthand experience of what they are doing with the platform; use X-as-a-service to ensure scalability.
- Capture user metrics and respond to feedback to continuously adapt to user needs and inject ongoing innovation.
## Find the Right Abstractions for Your Organization
Talk to any CTO; they will tell you that their application teams spend too much time on non-development tasks. A 2019 ** survey published in The New Stack reported that developers spend less than a third of their time writing or improving code**. My own informal chats with CTOs reveal that upwards of an estimated 80% of application teams’ time is spent on non-value-delivering toil. That is, developers are building their own internal platforms, focusing on operational workloads, and performing any number of other non-creative tasks.

CTOs and developers alike want to reduce this burden. Platform engineering can help — if an organization invests in finding the right abstractions for their business. That’s a big *if *because there’s no one-size-fits-all platform, which is one potential roadblock.

One common approach has been a classic bad DevOps “you write it, you run it” mentality in which individual teams decide to build their platform only to discover that multiple other internal teams have also invested in creating their platforms. Leaving aside the organizational communication silos that let this happen, this is wasteful, inefficient, and fails to take advantage of the power of platform engineering.

### How To Determine the Right Abstractions
What are the “right abstractions”? An excellent place to start is to ask what key attributes we need from a platform to make it worthwhile and valuable. How will it provide the organization with maximum efficiency, security, and productivity? Achieving this demands looking at what is **expected of the teams** in the organization but **unique to the business. **If something is not unique to the industry, buying something off the shelf probably makes more sense, or getting an existing cloud service to serve the need rather than trying to build it yourself.

One way to decide on the right abstractions is to understand the wrong ones. Forcing everyone down a prescriptive “golden path” that aims to show exactly how things should be done creates friction and resistance. The “dictatorial approach” is a common conflict because differing opinions and experiences clash with the “here is how everything will work” approach. Whether it’s CI/CD, the exact framework in use, staging, and production, or other tools, it’s important to **create (de-)composable abstractions to ensure people are more productive and have some flexibility**. Having options in the form of high-level abstractions helps provide some guideposts that won’t turn into an electric fence.

### Key Takeaways
The right abstractions will be unique to an organization and its needs, meaning:

- Finding what is expected of your teams but unique to your business
- A promised “golden path” without flexibility reduces productivity and creates friction
- Don’t dictate to application teams; they will have opinions about how things work. You should try to make their lives easier, but cooperatively, without overruling their experience.
## Democratize Your Platform
Delivering meaningful, productive, and valuable software in an enterprise often involves many stakeholders. Give these people an early “in” or face struggle(s) in getting value into production and delivering value for the organization’s customers.

Many people throughout the process are empowered to say “no” to anything you are trying to do — for various reasons. Democratizing the platform from the get-go helps include these stakeholders and brings their value to the platform early. Time-to-value is a significant consideration for enterprises when making technology investments, and in some organizations, complexity, compliance, and governance (among other things) slow value delivery way down.

An example of the power of democratizing the platform: an insurance company that had six-month to two-year deployment cycles could reduce the time to value by folding all ship-code-to-production activity into a single platform and automating it, seeing their deployment cycles slashed and being able to deploy multiple times a day.

### Key Takeaways
Getting the right stakeholders involved and bringing them and their value to the table makes a big difference in the platform you end up with. Some keys to this democratization process:

- Create a self-service API for your platform with different interfaces to access it
- Help other teams (identity, CI/CD, database) contribute their value to that platform
- Enable teams like security, networking, and other enablement bring what they offer, e.g., subsystem teams gain value from enablement teams, etc.
## Everywhere Is a Brownfield, and Everything Is Complex
The world is not a pristine, green space, and this applies to organizations with a lot of legacy stuff. Yes, [everything is brownfield](https://www.youtube.com/watch?v=b-F1VL4YMbE&list=PLSfU1pZbhFb5we22kkNCzvll64tk_csMM&index=5) and complex, and even the most valuable solutions cannot replace everything or be used everywhere.

As a real-world example, I talked to a CTO at one of the world’s top banks, who explained that he loved what Cloud Foundry could do but wondered what would work for the other 99% of workloads he had responsibility for. Essentially, it’s essential — and sometimes even critical — to think about what needs to get done and what can be done with what you already have. If you’re small or have fundamental apps, using something like Heroku, Netlify, or another platform as a service will make perfect sense. However, complexity is inevitable for other organizations facing layers of scalability, compliance, and governance issues, as well as myriad long-living heritage applications that don’t conform to the new platforms and services being introduced.

Most enterprises are brownfield, almost unimaginably complex, and challenging to work with. This reality informs the honest way we must **think about our platforms and how and whether they can adapt to that landscape rather than trying to dictate to it.**

Underneath that, in most organizations, there is only [one infrastructure layer](https://www.syntasso.io/post/platform-engineering-orchestrating-applications-platforms-and-infrastructure). It’s impossible to say, “Everything’s on Kubernetes.” Instead, it’s likelier to see Terraform, Pulumi, cloud APIs, and infrastructure as code tools like Chef, Puppet, lots of scripting, some declarative and some imperative stuff, and so on. And the platform will have to work with all of this if it will provide real value to the organization. When building a platform, enabling people to bring their value in an X as a Service mentality is essential. You need a straightforward, consistent API in front of the value people have been bringing over time. This API needs to be there for both old and new resources if the platform will deliver actual value inside the organization.

### Key Takeaways
Be prepared for complexity and legacy. Some critical considerations for tackling this reality include:

- Adapt, don’t dictate.
- Understanding and planning for a platform will require working with a lot of brownfield stuff.
- Deliver a straightforward, consistent API for both old and new resources
## Day One Is Easy; Day Two Thousand Is Hard
On day one, it’s easy to create something from scratch. On day 2,000, it’s much harder to maintain what was built on day one. Even with careful planning, a lot happens in an organization over time — people leave and take a lot of institutional knowledge with them; layers are built on layers, and what exists on day 2,000 is a different beast from day one.

How do you work against this? Some challenges, as noted, are impossible to foresee, but **organizing and standardizing** into a manageable structure is step one. Taking control of what we need to manage into a structured setup to understand where they are, which versions they are, and what software is installed there can be done with an X-as-a-service mentality, thinking about standardizing what you offer as a service. Standardizing and caring for an as-a-service offering rather than sharing a code base (a ticking time bomb) helps ensure that users are coming along on the journey rather than taking on their maintenance nightmares.

### Key Takeaways
Day 2,000 can be easier than it seems. Consider the ways to make sure your platform serves your users from day one to day 2,000:

- Organise and standardise
- Consider that it’s easy to build applications but much more challenging to maintain
- Sharing code is a maintenance nightmare; deliver things as a service (manage the fleet, take everyone on the journey, keep them updated and secure)
### Keep the 5 Lessons Alive
Whatever part of the platform engineering journey an organization finds itself in, these five lessons can come in handy in evaluating and designing a platform for the future:

- Product mindset: Make your platform a product
- Find the right abstractions: Make your platform a product that works for you
- Democratize your platform: Make your platform more robust by taking on as much value from stakeholders early on and gaining easier buy-in along the way.
- Everywhere is brownfield, everything is complex: Make your platform adaptable to the existing complexities of the legacy enterprise and its infrastructure and systems.
- Day one is easy; day 2000 is hard: Organise and standardize aspects of your platform as much as possible to ensure ease of use and maintenance from day one to day 2,000 and beyond.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)