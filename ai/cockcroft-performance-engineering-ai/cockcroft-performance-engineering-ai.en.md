Over its five-year history, P99 CONF has hosted quite a few speakers who’ve offered pointed takedowns of the namesake metric. At last year’s conference, Adrian Cockcroft didn’t explicitly state that [P99s are BS](https://thenewstack.io/if-p99-latency-is-bs-whats-the-alternative/)… but he did allude to it.

If you don’t know [Cockcroft](https://www.linkedin.com/in/adriancockcroft/), he’s spent decades architecting, scaling, and optimizing resilient, high-performance systems at giants like Sun Microsystems, Netflix, eBay, and Amazon. We could probably dedicate an entire day of P99 CONF to discussing the lessons learned from just *some* of his projects (Solaris kernel performance, multi-processor optimization, Netflix’s on-prem to cloud migration, Chaos Monkey…)

Fortunately, RedMonk analyst [Rachel Stephens](https://redmonk.com/team/rachel-stephens/) proved the perfect host for a conference that’s all about making things fast. She sat down with Adrian and led us on a whirlwind tour of how AI has impacted performance engineering. Here are some highlights from the chat (full video below).

*Note: P99 CONF 2026 – a free + virtual conference on all things performance – is going live October 21-22. Grab* [*a complimentary pass*](https://www.p99conf.io/?latest_sfdc_campaign=701Rb00000qrLWi&campaign_status=Submitted&utm_campaign=smo%20new%20stack%202026-10-21%20p99%20conf&utm_medium=social%20media%20-%20organic&utm_source=the%20new%20stack&lead_source_type=the%20new%20stack) *and join us!*

As a performance specialist at Sun in its heyday, getting to the root of performance problems involved lots of digging and divination. Cockcroft recalls, “Back in the old days with Sun, people would look at the output of system metrics in [vmstat](https://www.redhat.com/en/blog/linux-commands-vmstat) or whatever, and they’d be guessing what the numbers meant. There was a very vague understanding of what these things meant. The manual page wasn’t very clear.”

Cockcroft ended up going to the source, literally. “I went and read all the kernel source code and figured out exactly where these numbers came from, exactly what they meant, which ones were approximating what, and wrote all that down.” That led to two performance books: *Sun Performance and Tuning* and *Resource Management*.

> “My speedup is infinite, because this code would never exist without these tools. I wouldn’t have the time to build them.”

Four decades later, there’s now a wealth of helpful tools for end-to-end tracing, but Cockcroft’s curiosity still lies in what the tools are not showing. He continued, “Everything *sort of* looks okay in the tools – but the system isn’t behaving well. I usually come in and try to find a new way of looking at the data. A new type of analysis, or go a little bit deeper or finer grain, or stop looking at averages and start looking at distributions, and find all kinds of interesting things that nobody knew were happening.”

Currently, he’s [vibe coding](https://thenewstack.io/beginners-guide-to-vibe-coding/) tools to better analyze the anomalies he finds. Saved from having to brush up on Python or hunt down graphics library fragments on Stack Overflow, Cockcroft can now stand up custom tooling in minutes. “My speedup is infinite, because this code would never exist without these tools. I wouldn’t have the time to build them.”

## Peaks not percentiles

One specific vibe coding project: Cockcroft built (and open-sourced) tooling to get a better understanding of response time distributions.

Response time distributions have been on Cockcroft’s mind for over a decade. While most people obsess over percentiles – yes, P99 CONF included – Cockcroft is most intrigued by the distribution of response time peaks in a histogram. He believes percentiles don’t work when trying to understand the latency and performance of modern web services. A single number like P99 can’t tell you whether the underlying distribution has one peak or several. And when there’s more than one peak (as is often the case in the real world), the mean, the standard deviation, and even the P99 itself lose most of their meaning.

> “Percentiles don’t work when trying to understand the latency and performance of modern web services.”

![Image showing what people think response time distributions looks like vs what they really look like](https://cdn.thenewstack.io/media/2026/09/a42212ef-image1-1024x559.png)

*(source: [A Tale of Two Histograms](https://github.com/adrianco/slides/blob/master/Monitorama%20Histograms.pdf))*

For example, assume you have a histogram with two response time peaks: a fast one from a cache hit and a slow one for misses that require actual work. As the cache hit rate shifts, each peak’s position remains the same (i.e., the latency values of the fast-response mode and the slow-response mode don’t change), but the peak heights rise and fall. “Your averages and your P99 are changing all over the place, but all that’s really happening is your cache hit rate is changing,” Cockcroft said.

So how do you go beyond measuring P99s and averages? Cockcroft did what he’s done for decades: dive in and [build a custom](https://thenewstack.io/with-nova-forge-aws-makes-building-custom-ai-models-easy/) tool. But these days, it’s much simpler thanks to LLMs.

> “Your averages and your P99 are changing all over the place, but all that’s really happening is your cache hit rate is changing.”

He had already worked out the statistical approach for analyzing the distribution. Once ChatGPT came out, he quickly used it to build a tool that automated it. Instead of collapsing everything into an average, it identifies an arbitrary number of peaks in a distribution and tracks how they fluctuate over time. It’s implemented in R – a language Cockcroft hadn’t used in a while, but ChatGPT knew quite well – and it’s [open source](https://github.com/adrianco/responsetime-distribution-analysis/blob/main/README.md). If you’re curious, learn more in his [Percentiles Don’t Work](https://adrianco.medium.com/percentiles-dont-work-analyzing-the-distribution-of-response-times-for-web-services-ace36a6a2a19) article and “A Tale of Two Histograms” [talk](https://www.youtube.com/watch?v=kKx1E8C2tv0) and [deck](https://github.com/adrianco/slides/blob/master/Monitorama%20Histograms.pdf) (“*It was the best of response times, it was the worst of response times…”)*

## Where do we go from here?

To close, Stephens asked Cockcroft what advice he’d share with teams working on high-performance systems today. His top tip was to start with the macro view to find what’s interesting, then keep digging deeper until you’re inspecting individual slow requests end-to-end.

“Remember the microscope that you got when you were a kid,” Cockcroft said. “First, you have to focus it using the lowest resolution, at 10x, and then you can click it to 100x and adjust that, looking at just one speck now. Once you get that in focus, you click it to 1,000x.”

Cockcroft has spent his career building tools that bring obscure performance issues into focus. We look forward to seeing what others have cooked up with agentic tooling to help identify and [solve performance problems](https://thenewstack.io/the-complexity-of-solving-performance-problems/) this year at P99 CONF.

*Learn about the latest performance optimization techniques, tooling, and case studies at P99 CONF – free and virtual, October 21-22. Grab* [*a complimentary pass*](https://www.p99conf.io/?latest_sfdc_campaign=701Rb00000qrLWi&campaign_status=Submitted&utm_campaign=smo%20new%20stack%202026-10-21%20p99%20conf&utm_medium=social%20media%20-%20organic&utm_source=the%20new%20stack&lead_source_type=the%20new%20stack) *and join us!*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/09/dea56ceb-cropped-523fff7d-tim.jpg)

Tim has had his hands in all forms of engineering for the past couple of decades with a penchant for reliability and security. In 2013 he founded Flood IO; a distributed performance testing platform. After it was acquired, he enjoyed...

Read more from Tim Koopmans](https://thenewstack.io/author/tim-koopmans/)

[![](https://cdn.thenewstack.io/media/2020/01/14adf317-cynthiadunlop.jpeg)

Cynthia Dunlop has been writing about software development and testing for much longer than she cares to admit. She's currently senior director of content strategy at ScyllaDB.

Read more from Cynthia Dunlop](https://thenewstack.io/author/cynthiadunlop/)