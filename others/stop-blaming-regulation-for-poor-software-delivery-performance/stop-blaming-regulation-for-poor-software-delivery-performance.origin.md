# Stop Blaming Regulation for Poor Software Delivery Performance
![Featued image for: Stop Blaming Regulation for Poor Software Delivery Performance](https://cdn.thenewstack.io/media/2024/09/1eed2d03-banking-1024x576.jpg)
When discussing the incredible insights from the [DORA research](https://dora.dev/research/), it’s common to hear that people in regulated industries think they should aim for a different level of software delivery performance than non-regulated industries. But when the research shows high throughput goes hand in hand with solid stability, how can they be right?

We can draw on over a decade of research to bust the myth that high-performance software delivery isn’t for the regulated.

## The Throughput/Stability Trade-Off
For clarity, I’ll use the terms throughput and stability in line with [DORA’s four key metrics](https://thenewstack.io/google-says-you-might-be-doing-dora-metrics-wrong/). Throughput is described by low change lead times and high deployment frequency. Stability is defined by low change failure rates and quick recovery times.

Traditionally, organizations believed they could increase the stability of a system by reducing throughput. If you deploy less often, you can spend plenty of time on it and make sure it happens smoothly. One revelation of the DORA research has been that this doesn’t work.

Whether you are using DevOps, agile or something else, you’ll have a [process to validate a new software version](https://thenewstack.io/how-to-do-dora-metrics-right/) before giving it to users. The process involves a series of stages, each increasing your confidence that the software is good. This is a deployment pipeline. You might perform each step manually, it could be fully automated or like many real-world pipelines, it may fall somewhere between the two.

If a software version passes all stages in your deployment pipeline, there should be no quality-related reasons to withhold the deployment. If you improve the speed of the deployment pipeline, throughput will increase. If you still perform all the required stages, no sacrifice has been made to the quality of the software version.

In most cases, optimizations you make to improve throughput, like automation, also improve stability. Automated deployment isn’t just faster, it’s also more reliable and repeatable than deploying manually or by double-clicking home-grown scripts (DIY shadow CD). Many DevOps practices bring this dual benefit.

The only reason for a trade-off to be created between throughput and stability is if you attempt to artificially increase throughput by removing crucial verification steps. DevOps does not recommend this kind of reckless speed. If anything, your deployment pipeline should become more rigorous and disciplined as efficiency increases.

## Hesitation Isn’t a Regulatory Requirement
Regulated industries must satisfy an additional set of requirements set by their regulator. This doesn’t require you to work in large batches or hold onto software changes longer than necessary. Regulations inform and constrain how your product works. They often require you to collect more evidence than other industries. But the fundamental mechanisms don’t have to be slow.

Just as you can build security into your deployment pipelines, you can build in regulatory requirements. You may be able to automate some aspects of regulatory verification, and you can streamline the manual stages by making the information you need easily available. You can reduce your change lead time by reducing manual effort and removing wait times, two improvements that can often be arranged in a mutual positive spiral. For example, if you can make the change advisory board’s life easier, they may be willing to convene more often, perhaps even on demand.

The goals of regulation do not conflict with the outcomes of high-performance software delivery. The organizations and teams pulling ahead aren’t compromising; they are finding ways to move quickly *and* safely, often by reducing toil and reaping the double benefits of automation.

Whether your verification steps are based on good practices or regulations, your deployment pipeline remains the mechanism to satisfy everyone that the software meets all requirements.

As a bonus, I’ve always found that auditors love a good DevOps toolchain that can capture a robust audit trail and enforce appropriate access control for actions.

## What DORA Says
DORA offers a [quick check tool](https://dora.dev/quickcheck/) you can use to assess your performance. The results page lets you compare your performance against specific industries. If you work in a regulated industry like financial services, you can compare your performance with other organizations in the same sector.

You can plot overall performance broken down by industry based on the quick check data. The bars show the average performance scores, and the lines show the standard deviation. [Organizations in every industry](https://thenewstack.io/5-tips-every-organization-must-consider-when-going-cloud-native/) are finding ways to attain high software delivery performance, where they can increase throughput and improve stability.

![Graph of overall software delivery performance by industry](https://cdn.thenewstack.io/media/2024/09/4abf2a16-image1-1024x615.png)
Overall software delivery performance by industry


![Graph: Across all four measures, industry performance is comparable.](https://cdn.thenewstack.io/media/2024/09/71f12a1d-image2-1024x615.png)
Across all four measures, industry performance is comparable.

I asked [Derek DeBellis](https://www.linkedin.com/in/derekdebellis/), DORA research lead, whether software delivery performance was affected in regulated industries.

For more than a decade, DORA has been [measuring software delivery performance](https://thenewstack.io/4-ways-to-measure-your-software-delivery-performance/) across many industry verticals. Our research rarely finds that industry is a predictor of software delivery performance; we see high-performing teams in every industry vertical. One pitfall warned against in the [2023 report](https://dora.dev/research/2023/dora-report/) [p. 18] was “using industry as a shield against improving.” We caution teams in highly regulated industries from using these regulations as a reason not to disrupt the status quo. This isn’t to suggest that there are no unique challenges across industries, but no one industry appears to be uniquely encumbered or uniquely capable when it [comes to software delivery performance](https://thenewstack.io/where-is-the-complexity-of-modern-software-coming-from/), he said.

And this cuts to the heart of the matter. When faced with large-scale change, it’s natural to balk and look for reasons not to take action. But when competitors in your industry are improving, how long can you afford to avoid making the necessary changes?

We now have too much evidence to continue to say throughput and stability are a trade-off. They are not. The myth is busted. High-performance software delivery is increasing throughput, improving stability and satisfying regulatory requirements in ways that require minimal toil.

You can [find out more about the research](https://dora.dev/) and [join the DORA community](https://dora.community/), where topics like this are discussed regularly. The Accelerate State of DevOps Report 2024 is currently being prepared for publication.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)