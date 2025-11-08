Reliability engineers are the quiet force that keeps modern software running. After decades of refining practices on deterministic systems, many teams are chasing yet another “nine” beyond 99% uptime. But the AI era, especially LLM-backed features, changes the game. Outputs are non-deterministic, data pipelines shift underfoot, and key components behave like black boxes. As a result, many of the tools and rituals SREs have mastered for decades no longer map cleanly to production AI.

At SREcon EMEA 2025, I co-organized the [MLOps discussion track](https://www.usenix.org/conference/srecon25emea/presentation/vechtomova-dt) with Cauchy Co-founder Maria Vechtomova. We brought leading voices for a conversation with the audience, discussing how reliability practitioners can navigate this AI landscape. Here are the key takeaways.

## SREs Face a New Paradigm

At SREcon Americas 2025, Microsoft Corporate VP Brendan Burns [said](https://www.usenix.org/conference/srecon25americas/presentation/burns) Azure vets new models in two ways: the LLM-as-a-judge strategy, where LLMs judge their outputs; second, and more surprisingly, with Microsoft employees providing “thumbs-up/thumbs-down” feedback. The audience laughed and then continued discussing it during the conference. For reliability [engineers used to measurable SLOs and objective metrics](https://thenewstack.io/limitations-in-measuring-platform-engineering-with-dora-metrics/), this sounded uncomfortably squishy. And this was perhaps a pivotal moment that signaled to the industry that [changes were on the way](https://thenewstack.io/2-ways-ai-assistants-are-changing-kubernetes-troubleshooting/). As Stanza CEO Niall Murphy puts it, “SREs are going to have to wrestle with this stochasticism for a while to come.”

For most traditional software, [running the same code on the same infrastructure](https://thenewstack.io/how-to-run-deepseek-r1-on-aws-using-infrastructure-as-code/) yields the same result. With machine learning workloads, that’s not guaranteed. As Vechtomova [explained](https://www.youtube.com/shorts/bgvRu6UbcuE), “the statistical properties of the data can change, and your model stops performing. That’s what happened during COVID: forecasting and recommender systems broke because we had never seen that kind of data before.”

And while AI has been around for a while in different shapes, we are entering a new era. As Zalando’s director of AI, Alejandro Saucedo, observed, “GenAI/LLMs are shifting the paradigm from training toward inference.” Training used to be the center of gravity; models weren’t good enough for most applications, and ML engineers focused on fixing that. With LLMs now delivering almost magical results, the hard problems have moved to serving time: inference. SREs are entering the show, being asked to go from zero to production-grade quickly, often without mature tools or established playbooks.

Reliability practitioners are used to deterministic systems, where, for example, status codes (2xx/5xx) could serve as rough health proxies. Because LLM outputs are non-deterministic, there is often not a straightforward way to know if an AI-generated answer is any good.

## Monitoring Must Evolve

If your LLM app generates news summaries, how do you know today’s output is as good as yesterday’s? There’s no single, obvious signal. So what should you track to catch quality drift? Meta senior staff production engineer Jay Lees argues for anchoring on business metrics. For ads, that might be the click-through rate (CTR): if the CTR rises, your AI is likely improving the experience; if it falls, something has regressed.

LLMs push SRE’s metric philosophy up the stack. The only reliable arbiter of “correct” is the business outcome: did the assistant resolve the case, did the user convert, did revenue per session hold? That means service owners must define outcome-level SLIs and SLOs. But outcomes can lag, and it is best practice to pair them with classic indicators. Together, this stack gives both truth with [business impact and speed](https://thenewstack.io/how-event-processing-builds-business-speed-and-agility/) with early drift signals.

That paints a clear picture that AI makes observability non-optional. But, as Honeycomb CTO Charity Majors puts it, “most companies don’t even have high-quality observability for their non-AI workloads.” So either we’re in for a long ramp to proper AI observability, or AI becomes the catalyst that drags observability forward. And for companies trying to do it right, a [recent survey](https://ethical.institute/state-of-ml-2024.html) found that monitoring and observability were the biggest challenges when productionising machine learning models, with only 50% of companies having some sort of model monitoring in place.

## No One Has It Figured Out

Even if we instrument aggressively, there are limits to what’s practical today. Anthropic’s Head of Reliability, Todd Underwood, put it bluntly: “in theory, you could track and version everything: data, prompts, embeddings, models, retrieval indices, and policies to explain deviation. In practice, that level of end-to-end provenance is heavy and unrealistic for most companies.”

That gap between the ideal and the practical exists for a reason: the ground keeps moving, quickly. Underwood and Murphy, co-authors of [Reliable Machine Learning: Applying SRE Principles to ML in Production](https://www.oreilly.com/library/view/reliable-machine-learning/9781098106218/), added that a challenge in writing the book was staying ahead of the pace of change; they aimed to propose practices that wouldn’t become obsolete by the time of publication.

After ninety minutes of discussion with the panel and audience, one theme stood out: No one has it fully figured out. Many engineering teams feel they are behind on AI, but the truth is that we are all flying a plane that is still being built. Some organizations are ahead, but few have mature processes, tooling, and playbooks for operating these non-deterministic systems at scale.

At this point, MLOps has more [open problems](https://spawn-queue.acm.org/doi/10.1145/3762989) than settled answers, nothing new for tech, but at a scale we haven’t seen in a while. As Andrej Karpathy has [noted](https://www.dwarkesh.com/p/andrej-karpathy), getting agentic applications “right” may take a decade. Many LLM demos have hit the first nine — they work about 90% of the time — but there are many more nines to conquer before we reach production-grade reliability.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/d18c6a77-cropped-5b2d8eb1-sylvain-kalache-768x768-1.jpeg)

Sylvain Kalache is a tech entrepreneur and software engineer. As Head of AI Labs at Rootly, he oversees developer relations and AI initiatives. He previously founded a software engineering school whose graduates were hired by organizations such as Apple, Google,...

Read more from Sylvain Kalache](https://thenewstack.io/author/sylvainkalache/)