# To Fix Platform Engineering, Build What Users Actually Want
![Featued image for: To Fix Platform Engineering, Build What Users Actually Want](https://cdn.thenewstack.io/media/2025/05/2ddadfb4-platform-engineering-decisions-2-1024x683.png)
I was working with an automotive client whose engineering team had an ambitious goal: build new microservices and an external partner platform — fast. But “fast” was easier said than done.

While the team was excited about shipping features, it was constantly pulled into the weeds of infrastructure decisions. The developers were juggling too many compute options, trying to convince architects of their choices, and struggling with the anxiety of learning yet another tool while still delivering sprint after sprint.

What stood out most was a heated debate between two technical group leads. One was adamant that [AWS](https://aws.amazon.com/?utm_content=inline+mention) ECS with Fargate was the right path: simple, serverless, and easy to manage. The other camp strongly advocated for AWS EKS, paired with the [Kubernetes](https://roadmap.sh/kubernetes) ecosystem: [Prometheus](https://thenewstack.io/creating-a-path-for-prometheus-success/) for observability, [Grafana](https://thenewstack.io/can-grafana-adaptive-metrics-help-slash-observability-costs/) dashboards, [GitOps](https://thenewstack.io/4-core-principles-of-gitops/) workflows — you name it.

Each option had merit. But the debates were endless, decision-making slowed and delivery suffered.

So I quietly made the call: we’d move forward with a managed [Kubernetes](https://thenewstack.io/kubernetes-v1-33-advances-in-ai-security-and-the-enterprise/) platform. I prioritized developer experience, maintainability and future scalability. And we just got on with building.

That moment was a turning point for me — not because of the specific tools we chose, but because it exposed the core issue many teams face today: when platform complexity becomes the blocker instead of the enabler.

One of the biggest challenges organizations face today is the sheer complexity of technology — it’s fragmented, evolving rapidly and constantly shifting. Add to that the acceleration of platform business models, and staying ahead becomes a relentless pursuit.

Five years ago, digital transformation was a choice. Today, it’s a necessity.

This is where [platform engineering](https://thenewstack.io/platform-engineering/) comes in. At its core, platform engineering should serve as an abstraction layer — addressing at least two critical pain points:

- Managing fragmented technology stacks.
- Keeping up with rapid technological change.
By doing so, it empowers businesses to focus on delivering value instead of wrestling with infrastructure. Platform engineering should reduce friction, enable agility and make technology a seamless enabler, not a burden. But how do we know if it’s working?

## Measuring Success: Impact Over Adoption
Success in platform engineering isn’t just about how many teams use the platform — it’s about how effectively it drives outcomes. A successful platform should:

- Accelerate digital transformation, not delay it.
- Deliver a developer experience as seamless as any great external product.
- Provide intuitive, integrated solutions — not merely shift complexity onto developers.
Too often, [“shift-left”](https://thenewstack.io/the-limits-of-shift-left-whats-next-for-developer-security/) is misinterpreted as offloading everything onto engineers. But it’s the responsibility of platform engineers, designers and architects to create systems that are intuitive and allow developers to focus on innovation. If that doesn’t happen, developers disengage — and the platform becomes shelfware.

## Would You Use Netflix Like This?
Imagine signing up for [Netflix](https://thenewstack.io/developer-productivity-engineering-at-netflix/), excited to binge your favorite series. But:

- It takes six months to learn how to use it.
- Navigation changes every time you log in.
- Watching a movie feels entirely different from watching a series.
You’d probably quit. Now apply this to internal developer platforms.

If it takes developers and engineers months to become productive, your platform isn’t helping — it’s hindering. A great platform should be as frictionless and intuitive as a consumer-grade product.

Internal platforms must empower instant productivity. If your platform offers compute, it shouldn’t just be raw power — it should be integrated, easy to adopt, and evolve seamlessly in the background. Let’s not create unnecessary cognitive load. Developers are adapting quickly to generative AI and new tech. The real value lies in solving real, tangible problems — not fictional ones.

This brings us to a deeper look at what’s not working — and why so many efforts fail despite the best intentions.

## Diagnosing Platform Engineering’s Growing Pains
[Platform engineering](https://thenewstack.io/ebooks/platform-engineering/platform-engineering-what-you-need-to-know-now/) is still maturing, and it shows. Many tools and practices are being assembled without fully understanding real-world industry pain points.
Most enterprises are hybrid by nature — legacy systems, siloed processes and complex workflows are the norm. The real challenge isn’t just technological; it’s integrating platform engineering into these messy realities without making it worse.

Today, no single product solves this end-to-end. We’re still lacking a holistic solution that manages internal workflows, governance and hybrid complexity without adding friction.

What’s needed is a shift in mindset — from assembling open source tools to building integrated, adoption-focused, business-aligned platforms. And that shift must be guided by clear trends in tooling and team structure.

## Tools and Trends: What Lies Ahead
Open source remains powerful, but it’s still fragmented. While it has huge potential, the lack of consolidation and standards continues to create integration challenges.

In response, many organizations are leaning into DIY, developer-led platforms. Engineers increasingly want control — over tooling, integration and automation. This trend is here to stay.

Meanwhile, the software opportunity remains wide open. The market is still waiting for a true platform product that balances flexibility with usability. If built right, this could redefine platform engineering.

Of course, tooling is only part of the picture. Equally important is how organizations structure their platform teams.

## Why Business Alignment Matters in Platform Engineering
Internal platforms have impact on external performance. When internal tools are clunky or slow, customer-facing innovation suffers.

Too many platforms are built with a tech-first mindset. We need business-first thinking.

A successful platform should:

- Speed up innovation.
- Abstract complexity.
- Deliver a seamless experience.
Internal platforms should be treated like customer products — with investment, user research, and measurable business outcomes. And looking forward, how we evolve the entire discipline will define its future.

## What the Next Two Years Should Bring
What might happen? Platform engineering will follow the DevOps trajectory: from concept to necessity. Adoption will grow, and tools will mature.

What should happen, and what I would preferably love to see? Two critical shifts:

**Open source consolidation:**The[Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention), OpenUK and other such open organizations can play key roles in creating standards that reduce complexity.**Platform as ecosystem:**Like creators on Netflix or partners on Amazon, developers should help platforms grow organically — contributing back, adapting and evolving them over time.
This shift — toward organic growth, contributor engagement and smart integration — will set the stage for long-term success.

## Final Thoughts: Lead With Clarity
The most important takeaway?

Be clear about your platform’s purpose and business model. Without it, you’re just building tools.

Let your strategy — not your stack — drive decisions. Prioritize experience. Think holistically.

I will leave you with a thought from my book, “[Decoding Platform Patterns](https://mybook.to/shwetavohra),” to spark further ideas and innovation: The future of platforms will favor not those who move the fastest, but those who build trust, fairness and deliver exceptional experiences.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)