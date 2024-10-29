# The Future of APIs: Lessons in Security, Composability, AI
![Featued image for: The Future of APIs: Lessons in Security, Composability, AI](https://cdn.thenewstack.io/media/2024/10/442f1059-apis1-1024x572.png)
[berCheck](https://www.shutterstock.com/g/2313542454534543)on Shutterstock
The [API economy ](https://nordicapis.com/how-the-api-economy-is-changing-in-2024/)has arrived, and so have the challenges that come with it. [APIs are now everywhere](https://thenewstack.io/api-management/), embedded in everything, such as mobile apps and IoT devices, and the expectations around what they can do are soaring. Yet, the tools and platforms meant to tame this mess often fall short.

I had the pleasure of attending the recent [Nordic APIs Platform Summit ](https://nordicapis.com/events/platform-summit-2024/)in Stockholm, Sweden, earlier this month, and it was clear that while the benefits of APIs are undeniable, the associated pains are very real. I wanted to share a few of my key takeaways in the hopes that our collective focus will lead to solutions.

## 1. Let’s Not Throw the Baby Out With the Ocean Boilers
Now, I’m coming from the perspective of a VP of engineering at a tech startup where our new focus lies primarily on the development side of the API world. But during my time at the conference, it was clear that the industry is awash with promises of “one size fits all” monolithic API management solutions. In the past two years, many have pushed their offerings as “ocean boilers*,”* claiming to [solve everything](https://thenewstack.io/api-management-is-a-commodity-whats-next/) in one fell swoop.

You can probably guess what’s coming next, because we all know the ocean cannot be boiled. The resulting tension between what’s being promised and what is actually being delivered is palpable. Developers are becoming increasingly vocal about the gap between these promises and reality. But that doesn’t mean we should throw all of these efforts out; what we need is a shift in mindset. We’re on the brink of a new frontier that demands something different, something nuanced.

This new mindset, which came through at Platform Summit is a move toward APIOps and leveraging composable platforms that don’t aim to do everything. Instead, these platforms should focus on doing key things right.

A swing from specialized to monolithic tools seems to happen every few years, but this time it comes with a developer-centric twist. Companies can select (aka developers can adopt) best-of-breed tools for key functions that have the flexibility and composability to integrate into that optimal platform experience, providing the process and visibility required by enterprises today without the adoption battles. This requires a much more developer-centric[ approach to API development and platform strategy.](https://www.forbes.com/councils/forbestechcouncil/2024/02/29/creating-your-api-solution-wishlist-with-developers-in-mind/)

Developer platforms serve as the backbone of the platform engineering paradigm, and they are not just about providing tools and services; they are about motivating and empowering developers to produce their best work.

## 2. We’re Still Talking About Developer Experience
This brings me to my next takeaway from the conference. Amid the chaos of APIs proliferating at every turn, one thing is clear: [Developer experience (DX)](https://thenewstack.io/improving-developer-experience-drives-profitability/) is still important. The best tools in this space aren’t just about flashy features. They’re about enabling developers to do the work they want and need to do without slowing down the process. And this need for a [good experience is not lost on developers](https://thenewstack.io/can-ai-truly-transform-the-developer-experience/).

To translate that tangibly — things like API versioning and life-cycle management need to be baked in from Day 1, not bolted on later. Consistent practices of thorough testing and security must be easy and accessible, not cumbersome or confusing. And documentation, often neglected, needs to be a first-class citizen from the get-go.

Developers want solutions that simplify their daily challenges, not complicate them. The best tools are the ones that help developers iterate more easily and quickly through their development loops without [insulting their intelligence (which is quite an art when you think about it](https://thenewstack.io/zen-and-the-art-and-science-of-api-development/)). The takeaway is simple: Tools that actually deliver on DX will win the day.

![Inner and outer development loops.](https://cdn.thenewstack.io/media/2024/10/a1ec96d7-image1.png)
Image 1

At the heart of the developer experience are the inner and outer development loops. The inner dev loop is the cycle of activities a developer performs locally while working on a feature or bug fix. By contrast, the outer dev loop encompasses the broader development life cycle. The key to increasing developer velocity lies in optimizing their development loops.

We must find ways to minimize the “tax” imposed by the various steps in the development workflow, particularly complicated in today’s microservices and cloud native environments. The right combination of platform approach and developer experience can do this.

Some of the tools mentioned at the conference that offer solutions for a better developer experience were:

- Tools like
[Specmatic](https://specmatic.io/)offer a way to test for conformance, compatibility, and drift at design time, tackling problems early. - Languages like
[TypeSpec](https://typespec.io/)elevate API documentation to first-class status, making it easier for developers to maintain consistency and clarity. - Of course, I’d be remiss not to mention tools like
[Blackbird](http://getblackbird.io)as invaluable in optimizing the[inner and outer developer loops.](https://thenewstack.io/optimize-your-inner-dev-loop-to-increase-developer-velocity/)
These were just a few of the tools that provide that composability I mentioned earlier and fit into your existing workflow rather than forcing you to adapt to theirs.

## 3. There’s Low-Hanging Fruit: We Must Get Security Right
While the challenges are significant, there are still opportunities for quick wins if you’re looking in the right places. After listening to all the sessions, it’s evident that good security practices stand out among the most accessible opportunities for improvement, no matter where you are stuck in the API life cycle. Tried-and-tested [patterns for avoiding common authentication and authorization pitfalls ](https://auth0.com/blog/five-common-authentication-and-authorization-mistakes-to-avoid-in-your-saas-application/)can greatly reduce security risks. Additionally, regularly performing vulnerability assessments and applying encryption to sensitive data both in transit and at rest can further protect APIs from potential exploits.

And of course, we can’t forget the popular[ zero trust](https://www.getambassador.io/blog/the-importance-of-zero-trust) approach that’s rooted in the principle of treating users, systems and network traffic as fundamentally untrusted even though they are within the security perimeter established by a firewall. Or, many are seeking to shift [security left](https://snyk.io/learn/shift-left-security/) to ensure it’s more of a priority earlier on in the SDLC.

Whatever you’re doing to ensure security is a priority, getting it right is one of the lowest-hanging fruits developers can grasp, and many of us are still failing. And with the rise in breaches and attackers ([400% increase](https://salt.security/blog/latest-state-of-api-security-report-400-increase-in-attackers-and-more) in the last six months alone, according to Salt Security), we can no longer afford to ignore beefing up our security measures.

## 4. The Future Is Artificial and Insecure
AI was, unsurprisingly, the elephant in every room at the summit, as it’s been at every conference, panel and article subject for the past year. As much as the industry is talking about APIs, AI is influencing everything, from how we build APIs to how our consumers interact with them. The challenge for API designers isn’t just about how to use AI, but also about creating APIs and platforms that can adapt to how others are using AI in their systems.

Of course, with more [APIs come more sprawl](https://www.infoworld.com/article/3529600/how-do-you-govern-a-sprawling-disparate-api-portfolio.html) and more drift, factors that greatly expand the surface for security attacks. As developers and businesses alike try to navigate this expanding complexity, the question of who and what to trust becomes more pressing. The unfortunate answer is simple: nobody and nothing. [Zero trust architectures](https://www.getambassador.io/resources/kubecrash) and rigorous validation practices are becoming more relevant.

The good news is that solutions to combating that sprawl are increasingly abundant. Whether you call it “governance,” “standardization” or “having a platform strategy,” these solutions will only become more important to the API economy as APIs proliferate and our need for composable, flexible microservice architectures increases.

In the end, it was a great chance to connect with other API-minded colleagues and technology leaders at the summit. The new frontier is a promising one as long as you’re armed with the right [tools](http://getblackbird.io), [approaches](https://www.forbes.com/councils/forbestechcouncil/2024/05/30/rethinking-api-management-should-you-unbundle-or-is-there-a-better-approach/) and [mindset](https://www.forbes.com/councils/forbestechcouncil/2024/02/29/creating-your-api-solution-wishlist-with-developers-in-mind/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)