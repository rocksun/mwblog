# How Much Energy Is Really Being Consumed by Data Centers?
![Featued image for: How Much Energy Is Really Being Consumed by Data Centers?](https://cdn.thenewstack.io/media/2024/07/d1cef112-an-aws-data-center-in-northern-virginia-screenshot-from-amazon-2022-sustainability-report-1024x702.jpg)
What impact do data centers have on greenhouse gas emissions? It’s a “known issue” receiving some serious scrutiny.

In May, [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) released its [2024 Environmental Sustainability Report](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RW1lMjE), admitting that its emissions of greenhouse gases grew 29% (over 2020’s baseline). But that increase was primarily driven by the construction of new data centers, Microsoft explained, “and the associated embodied carbon in building materials, as well as hardware components such as semiconductors, servers, and racks.” These increases offset what was actually a 6.3% reduction in emissions coming from company-controlled assets and power supplies.

But there was more bad news last week. The Associated Press reported [Google](https://cloud.google.com/?utm_content=inline+mention) was [“nowhere near” meeting its goal of net-zero emissions by 2030](https://apnews.com/article/climate-google-environmental-report-greenhouse-gases-emissions-3ccf95b9125831d66e676e811ece8a18) — citing the [2024 Environmental Report](https://www.gstatic.com/gumdrop/sustainability/google-2024-environmental-report.pdf) released by Google on July 2. “Compared to its baseline year of 2019, emissions have soared 48%,” the article noted, adding that even in Google’s most recent figures, “its emissions grew 13% in 2023 over the year before.” And Google blamed last year’s jump on AI, according to the Associated Press, “and the demand it puts on data centers, which require massive amounts of electricity.”

Google’s chief sustainability officer [Kate Brandt](https://blog.google/authors/kate-brandt/) told the news outlet that Google’s approach “will need to continue to evolve,” and “will require us to navigate a lot of uncertainty, including this uncertainty around the future of AI’s environmental impacts.”

These are just scenes in a larger story, as the world faces two simultaneous revolutions — in cloud computing, and in climate-conscious energy consumption. But the detailed reports also offer evidence that tech companies are at least assaying the scope of the problem, exploring its ramifications — and investigating ways to address it.

## If Japan Were a Data Center
There were several eye-popping predictions in this year’s analysis from the long-running [International Energy Agency](https://en.wikipedia.org/wiki/International_Energy_Agency). Data centers consumed 460 terawatt-hours (TWh) in 2022 around the world, according to their calculations — but by 2026 could be consuming more than 1,000 TWh, an amount “roughly equivalent to the electricity consumption of Japan.”

Just fully implementing AI into search tools like Google could bump the energy those tools use up to 10x, they estimate — “almost 10 TWh of additional electricity in a year.”

U.S. data centers consumed about 200 TWh in 2022 — about 4% of all U.S. electricity demand. But by 2026 their analysis sees that climbing to almost 260 TWh (6%), driven by increased adoption of 5G networks and cloud-based services, as well as state tax incentives. (The IEA predicts data centers will account for more than one-third of America’s demand for additional energy in 2026.) In April Goldman Sachs [predicted that growth will continue](https://www.goldmansachs.com/intelligence/pages/gs-research/generational-growth-ai-data-centers-and-the-coming-us-power-surge/report.pdf), with data centers currently consuming about 3% of U.S. power, but by 2030 consuming 8% (with a fifth of that demand coming from AI).

![Screeenshot from April 2024 Goldman Sachs equity research on the coming US power demand surge](https://cdn.thenewstack.io/media/2024/07/d9bebf6f-screeenshot-from-april-2024-goldman-sachs-equity-research-on-the-coming-us-power-demand-surge.png)
Screenshot from April 2024 Goldman Sachs equity research on the coming US power demand surge

Yet it’s in the EU where the IEA expects electricity consumption from data centers to surge, rising 30% higher by 2026 over 2023’s levels, “as new data facilities are commissioned amid increased digitalization and AI computation. Ireland and Denmark alone make up 20% of the expected increase in data center electricity demand to 2026.” (Ireland has one of the EU’s lowest corporate tax rates, according to the report — and by 2026 they predict almost one-third of Ireland’s electricity demand will come from data centers, and almost 20% of Denmark’s.)

Last month Bloomberg reported that the number of data centers in the world has nearly doubled since 2015, and “The almost overnight surge in electricity demand from data centers is now [outstripping the available power supply in many parts of the world](https://www.bloomberg.com/graphics/2024-ai-data-centers-power-grids/), according to interviews with data center operators, energy providers and tech executives… By one official estimate, Sweden could see power demand from data centers roughly double over the course of this decade — and then double again by 2040. In the UK, AI is expected to suck up 500% more energy over the next decade.”

## Better With Cloud?
What about [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention)? [Phil Reay-Smith](https://www.linkedin.com/in/philreaysmith/?originalSubdomain=uk), Amazon’s senior corporate communications lead, pointed us to their last sustainability report (released in mid-July of 2023, covering the year 2022).

That report argues there’s “a lot of wasted energy” in running a low-utilization, on-premises data center. Seen in that light, cloud computing “also plays a role in reducing our customers’ environmental impact,” says [Kara Hurst](https://www.linkedin.com/in/karahhurst/), Amazon’s VP of worldwide sustainability, in the report. Citing Amazon’s energy-efficient hardware, Hurst wrote that AWS “can lower customers’ workload carbon footprints by nearly 80% versus on-premises computing workload, and we expect that number to increase once AWS is fully powered by renewable energy.”

Hurst backs up this claim with 2019 data gathered by [Global Market Intelligence firm 451 Research](https://d39w7f4ix9f5s9.cloudfront.net/e3/79/42bf75c94c279c67d777f002051f/carbon-reduction-opportunity-of-moving-to-aws.pdf). “[B]y the server efficiency metric, AWS is over 2.5 times more energy efficient than the median of surveyed U.S. enterprises… the result of much higher utilization of servers and an infrastructure that is heavily weighted toward more recent server technology generations that are inherently more energy efficient. In addition, AWS also designs its own servers for maximum efficiency, while enterprises might give more consideration to other features such as hardware redundancy and expandability.” Adding in the efficiency of actual data center facilities, the 2019 report found that AWS was over 3.6 times more energy efficient than the median of enterprises surveyed.

Amazon’s sustainability report also shows ways they hope to reduce the energy consumption of their data centers:

- AWS is investing in purpose-built chips like the AWS Graviton3 — an energy-efficient Arm-based machine learning chip that uses “up to 60% less energy for the same performance than comparable Amazon EC2 instances.”
- Amazon is also seeking “lower-carbon concrete options” for constructing data centers and other buildings.
- They’re designing efficient, low-carbon data centers (including servers and hardware). Amazon also uses an Enterprise Building Management System to manage energy use and reduce emissions. (It was already in 1,000 facilities by the end of 2022, with further expansions planned for 2023…)
- There are also investments in offsetting green-energy projects, including two developers of electrolyzers to convert water into green hydrogen.
Amazon has committed to net-zero carbon by 2040, according to the report…

## More Exotic Solutions
Other industry players are exploring even more new energy solutions. To reduce cooling costs, Microsoft [began testing an underwater data center](https://thenewstack.io/life-aquatic-microsofts-experimental-submersible-data-centers/) back in 2015. And while last week it was reported that funding “dried up,” Microsoft’s Cloud Operations/Innovation chief [Noelle Walsh](https://www.linkedin.com/in/noelle-walsh-b29356108/) had [reportedly said](https://redmondmag.com/articles/2024/06/24/project-natick-dries-up.aspx) “We learned a lot about operations below sea level and vibration and impacts on the server. So we’ll apply those learnings to other cases.” Meanwhile, last month the Washington Post [reported](https://www.msn.com/en-us/money/technology/ai-is-exhausting-the-power-grid-tech-firms-are-seeking-a-miracle-solution/ar-BB1oDl5z) that Microsoft is also “betting on an effort to generate power from atomic fusion.” The same article notes that Google is funding “a futuristic geothermal power plant in the northern Nevada desert that harnesses heat from deep underground.

And in the EU there’s even been feasibility studies on [building data centers in space](https://www.msn.com/en-us/news/technology/putting-data-centers-in-space-could-reduce-their-carbon-footprint-european-study-finds/ar-BB1p08Gj).

Even The IEA’s analysis suggests an important role in “technological improvements” (along with new government regulations). Some examples they cite?

- The IEA notes data centers “are evolving towards more sustainable and efficient operations, including transitioning to Hyperscale Data Centres, which can run large-scale operations without a significant increase in electricity consumption.”
- Looking to the future, the IEA notes that
[quantum computers](https://thenewstack.io/perpetual-motion-time-crystals-could-power-quantum-compute/)“deliver more and faster processing power than supercomputers while consuming less energy” (though they also need to be cooled to near absolute zero). - They recommend shifting power loads based on “carbon-awareness” (
[defined](https://learn.greensoftware.foundation/carbon-awareness/)by the non-profit Green Software Foundation as “doing more when more energy comes from low carbon sources and doing less when more energy comes from high carbon sources.”)
Maybe it’s all a reminder that it’s not all bad news. The IEA’s analysis also projected that despite increasing energy demand, global CO2 emissions would decline by 2% this year — after a 1% rise last year — with additional “small declines” projected for 2025 and 2026.

And “the share of fossil fuels in global generation is forecast to decline from 61% in 2023 to 54% in 2026, falling below 60% for the first time in IEA records dating back to 1971… Low-carbon sources — renewables and nuclear together — are expected to account for 46% of the world’s electricity generation by the end of 2026, rapidly approaching the halfway mark, up from 39% in 2023. And finally, on a global scale, low-carbon generation is set to meet all the additional demand growth towards 2026…

Power generation is currently the largest source of [carbon dioxide emissions](https://thenewstack.io/sustainability-focus-cloud-efficiency-not-carbon-emissions/) in the world, but it is also the sector leading the transition to net zero emissions through the rapid expansion of renewable energy sources such as solar and wind power.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)