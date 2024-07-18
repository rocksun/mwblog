# Sustainability: How Did Amazon, Azure, Google Perform in 2023?
![Featued image for: Sustainability: How Did Amazon, Azure, Google Perform in 2023?](https://cdn.thenewstack.io/media/2024/07/e4a141c5-sustainability-how-did-amazon-azure-google-perform-in-2023-sunset-2-1024x576.jpg)
The leading cloud providers and the mammoth global companies that run them are adopting environmentally sustainable practices, but it is a complicated work in progress.

As [Amazon](https://aws.amazon.com/?utm_content=inline+mention), [Google](https://cloud.google.com/?utm_content=inline+mention) and [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) continue to grow, they’re all [grappling with the challenges of reducing their carbon emissions ](https://thenewstack.io/how-much-energy-is-really-being-consumed-by-data-centers/)in the f[ace of increased resource usage of AI, while making the right investments in renewable energy infrastructure around the world.](https://embrace.io/?utm_content=inline+mention)

Customers of cloud providers need detailed information to understand and [optimize the sustainability of their own workloads](https://thenewstack.io/why-software-developers-should-be-thinking-about-the-climate/). While Amazon is [making the biggest sustainability investments](https://thenewstack.io/how-amazon-matches-power-needs-to-green-energy-sources/) and getting some good results, it has historically been the least transparent cloud provider.

Amazon released its [sustainability report covering the whole of 2023](https://sustainability.aboutamazon.com/2023-sustainability-report.pdf) on July 9, Google [released its report on July 2](https://www.gstatic.com/gumdrop/sustainability/google-2024-environmental-report.pdf), and Microsoft [released its in May](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RW1lMjE).

I’ve been leading the [Real Time Cloud project at the Green Software Foundation](https://github.com/Green-Software-Foundation/real-time-cloud) for the last year or so. We have made a deep dive into the information available, identifying gaps and subtle differences in the data from each cloud provider. I’m going to compare these three reports to see what’s new since last year; my analysis here is my own, not the project’s.

## Amazon Leads in Carbon Output Reductions
Amazon reduced total carbon 3% from 70.74 MmTCO2e (millions of metric tons of carbon dioxide equivalent) to 68.82 MmTCO2e. Normalized against the growth of the business, they were down 13% from 93.0 gCO2/$ (grams of carbon dioxide per gross merchandise dollar) to 80.8 gCO2/$.

This continues a trend that started last year, of a small reduction in total carbon despite growing the business, as more of the internal projects started over the last few years mature and begin to have material impact. There’s a long way still to go but it’s a commendable result.

Google however, increased its total carbon by 13% to 14.3 MmTCO2e for 2023, on top of an increase the previous year, slipping on carbon progress due to investment in data centers for AI, which was also the story at Microsoft, up from 16.5 to 17.2 MmTCO2e.

The physical delivery and manufacturing business of Amazon dominates its carbon footprint to a much greater extent than its more software-focused competitors, and Amazon’s revenue growth rate is a bit lower. But over the years, Amazon has also been more aggressive in buying renewable energy than Google and Microsoft.

Amazon’s carbon footprint was reduced for all categories apart from fossil fuels, as its delivery fleet continues to grow as a business, faster than those vehicles are being electrified. This trend is driven in part by Amazon bringing more deliveries in-house; in the report, the category that includes third-party delivery carbon declined 4%.

Increased focus on rail-based delivery in Europe and India is reducing delivery carbon. The electric delivery fleet grew more than sevenfold, to 19,000 vans, but still has a long way to go before it makes a material difference.

Over time, the electricity use of Amazon for retail and delivery is adding a lot more demand in addition to the growth of data centers, compared to Microsoft and Google. This is why Amazon is investing in so many more energy projects.

## Renewable Energy Projects: Making Good Progress
The most progress so far has been made in renewable energy. [Carbon-free energy matching was up from 90% to 100% for all of Amazon](https://www.amazon.science/news-and-features/how-amazon-achieved-its-100-percent-renewable-energy-goal), including retail and deliveries.

This is much more than just the AWS data center usage. Energy matching means that renewable energy is being generated and put into a grid somewhere in the world in an amount that matches any non-renewable energy that’s being used.

The energy projects that make up the portfolio are geographically positioned as close as possible to where the power is needed. But it’s not always possible for them to be located nearby, and the amount of energy generated doesn’t exactly match how much is currently being used locally.

The Amazon generation portfolio increased from 20GW to 28GW, making it the world’s largest purchaser of renewable energy for the fourth year in a row. Google added half as much, 4GW in 2023, which is still a record for the company.

Forty-two new utility-scale projects came online for Amazon in 2023. The Amazon sustainability report also states that the company is investing in nuclear energy alongside solar, wind and battery projects. Amazon has also purchased a nuclear-powered data center in Pennsylvania.

Amazon’s energy storage increased from 445MW in 2022 to 1.3GW in 2023 to help smooth out the daily supply and demand mismatch as solar and wind come and go. It’s now become common for new solar power developments to include battery storage, as the peak daily output could be curtailed and the excess can be stored then supplied to the grid in the evening.

## 100% Carbon-Free Energy Match Still Emits Carbon
The 100% carbon-free energy match metric uses the annual “market-based” method, which is based on energy purchases, averaged over the whole year. As we noted previously, the in-house generating capacity won’t ever match the right location at the right time, so there’s a market for trading excess renewable energy.

Renewable energy certificates (RECs) can be traded for up to a year, so when companies have final data for 2023, additional “unbundled RECs” can be purchased as needed to cover for the non-renewable energy that was used, and obtain any desired percentage, at a cost.

Amazon committed to reach 100% by 2030, with a goal of 2025, and is proud to get to 100% in 2023. It looks less impressive to realize that Amazon has finally caught up with Google, which has been at 100% carbon-free energy match using the same annual market-based method for the last seven years. The Amazon sustainability report states that there was 2.79 MmTCO2e of energy-related carbon emissions (known as Scope 2). In other words, when Amazon reached 100% carbon-free energy, there were still 2.79 million tons of carbon equivalent emitted.

A few years ago Google started measuring and reporting a much more stringent “24×7” hourly matching location-based method. Microsoft has dabbled with 24×7, but only for the Azure Sweden region, and AWS hasn’t done anything with it.

Amazon hides its location-based energy emissions in a footnote of the [Scope 1 and 2 Audit report](https://sustainability.aboutamazon.com/2023-ghg-verification-scope-1-2.pdf): “Amazon’s Scope 2 (Indirect) GHG emissions: Location-based method (LBM) are 15.67 MmTCO2e.” Most of the difference comes from Amazon’s generation projects, which aren’t counted by the location-based method. When the methods were defined, the report’s authors didn’t consider that large end users of energy could also be large generators of energy across multiple locations.

Google discloses location-based data to customers for all its cloud regions individually, and AWS needs to follow suit and start to report Scope 2 location-based data on a per-region basis.

Given the locations and sizes of the Amazon renewable power projects, I think AWS will often have lower location-based method carbon than Google and Azure. But AWS needs to publish its results — regardless of whether those numbers are better or not.

## Amazon Is Leaning Into Future Energy Capacity
The new Amazon report includes a statement that the company is “purchasing additional environmental attributes (such as renewable energy credits) to signal our support for renewable energy in the grids where we operate, in line with the expected generation of the projects we have contracted.”

It takes two to three years to bring a wind or solar farm online, so Amazon buys RECs on the open market that match the future generation capacity that they have committed to building. This is a good policy, as unbundled REC purchases have a bad reputation when they are used across regions and countries as a cheap substitute for actual investments. But here they are being purchased to match investments in new generating capacity.

However, there is also a footnote on page 26 of the sustainability report:

“AWS aims to procure renewable electricity in the same grids where it consumes electricity. In certain cases (e.g., renewable energy in the same grid is not available), AWS may procure renewable energy attributes in other locations.”

A similar footnote in the audit report on energy also reads:

“Amazon takes a global approach to calculating the percentage of electricity consumed by Amazon’s global operations matched by renewable energy sources. Amazon aims to procure renewable electricity in the same grids where it consumes electricity. In certain cases, Amazon may procure renewable energy in other locations.”

This is an unfortunate fact of life: there just isn’t enough renewable energy in regions in Asia in particular, so cross-border RECs are used. This is the first time I’ve seen Amazon make this statement, and Amazon joins Google and Microsoft, who’ve been buying cross-border RECs and carbon offsets for many years.

Amazon provides a [list of 22 AWS regions](https://sustainability.aboutamazon.com/products-services/the-cloud?energyType=true) where 100% renewable energy is procured in market. This covers all of the Canada, China, Europe, India, Japan and U.S. regions. Cross-border RECs are used to reach 100% match for Australia, Bahrain, Brazil, Hong Kong, Indonesia, Israel, Korea, Singapore, South Africa, and the United Arab Emirates. The difference since 2022 is that the “in-market” wording was added and Japan was added to the previously published 100% list.

However Amazon has far more generating capacity in Asia than either Google or Microsoft, and Amazon positions cross-border RECs as a last resort, which is the best we can expect in the circumstances.

The problem with this is that by the market method, cloud energy use in Asia will be reported as zero carbon, because cloud providers will pay extra by buying RECs elsewhere. However, increased use of regions in Asia will cause extra carbon to be emitted compared to the same use in Europe or the U.S., and to measure the difference the location-based method needs to be used and reported.

## More Investments in De-Carbonizing Supply Chains
Amazon announced a new program to engage major suppliers to decarbonize its supply chain with [Amazon Sustainability Exchange](https://exchange.aboutamazon.com/), sharing internally developed playbooks and sustainability science models for things like renewable concrete and hydrogen. There’s some interesting work and good advice here; it was put together by sustainability scientists in the Amazon central sustainability team.

Low-carbon concrete and steel for construction is a good investment and is growing fast, up from 16 AWS data centers to 36 in 2023, but it’s still a small impact on the carbon total. Efficiency and electrification upgrades and the use of local solar power on existing buildings are having a bigger effect.

AWS, Azure and Google have all started to transition to bio-diesel (mostly from recycled cooking oil) for backup generators, and AWS has reduced the use of air freight for deliveries and started to use electric vehicles for trucking equipment to data centers. This is worthwhile, as it helps develop a market for the supply of biodiesel globally, although this is currently a very small part of the total carbon footprint.

Amazon is correctly positioning investment in nature-based solutions and carbon capture as a second priority to direct reductions in carbon emissions. But it’s a worthwhile additional investment, as it’s expected to be necessary to scale these solutions over time to meet the 2040 Net Zero [Climate Pledge](https://www.theclimatepledge.com) goal, as the remaining direct emissions become harder to eliminate.

## Sustainable Water Resources: Good Progress
Sustainability is about a lot more than carbon and climate change. There are global shortages of clean water in particular, and concern about the amount of water used to cool data centers, which has increased a lot in recent years. A few years ago the cloud providers started to measure and report their water usage, and they all have targets to use less, and to return more clean water to the locations where they operate.

There are two ways to measure water, one is how much water is used as a proportion of the energy being used in a data center. Water usage effectiveness (WUE) is measured in liters per kilowatt hour. The other is how much water is replenished as a proportion of what is used.

AWS’s WUE improved by 5% from 0.19 to 0.18 Liters/kWh in 2023, averaged across all the facilities AWS runs globally. It’s unfortunate that AWS only provided a global average, which removes any opportunity to optimize via workload placement.

Microsoft Azure provided WUE on a region-by-region basis, varying from zero to over 2 Liters/kWh. Google did not report WUE figures.

AWS reports 41% “water positive” as a new metric in 2023, with a 100% goal. This appears to be another name for “water replenishment.”

Google reports improving from 6% to 18% water replenishment in 2023, but the company has a goal of eventually returning more water than it uses. Google was [dinged for poor water use ](https://time.com/5814276/google-data-centers-water/)a few years ago, and is clearly playing catch up, while AWS has already made good progress.

Azure doesn’t provide a replenishment figure. This is the kind of thing the Green Software Foundation’s Real Time Cloud project is working on, trying to get all the cloud providers to standardize on the same metrics with the same names by pointing out the gaps.

## Amazon’s Reporting Needs More Transparency.
AWS had previously published data center versus cloud carbon reduction comparison reports for Asia, Europe and the U.S. that were used as the basis for a lot of marketing claims over the years. They were getting a bit old and were updated by a new [carbon reduction comparison](https://sustainability.aboutamazon.com/carbon-reduction-aws.pdf) report in June.

Accenture was commissioned to write the report, and while it’s a helpful document and the claims it makes do seem reasonable, there’s no transparency in the calculations, and a lot of private AWS data was used by Accenture that isn’t available for customers to use to model their own specific situations.

Customers need more than marketing claims, and the report could have included a lot more of the underlying data and calculations, not just the headline results.

AWS is still not providing power usage effectiveness (PUE) information at all. Google published updated PUE data per region in its sustainability report a few weeks ago and releases quarterly updates. Microsoft Azure publishes PUE data for all its regions.

When you measure energy use for a workload in a cloud region (e.g. by collecting NVIDIA GPU energy use metrics), you need to multiply by PUE to account for how much energy was supplied to the data center to cover cooling and transmission inefficiencies then multiply by the carbon content of that energy.

PUE is much higher in hot and humid climates. Of course, some workloads have to be in a specific region. But a significant amount of compute and storage capacity (like backup/archives) could be located anywhere. It’s just not possible to optimize global workload placement without regional PUE and WUE data.

The other data provided by both Google and Azure is the companies’ carbon-free energy (CFE) proportion on a per-region basis. This takes the local method grid carbon mix into account, then subtracts out the locally generated capacity from renewable projects that are up and running. It’s a good way of indicating which regions are benefiting from low-carbon energy that can be used for optimizing global workload placement.

There is still no mention of Scope 3 supply chain reporting for AWS customers (Scope 3 refers to emissions from assets not owned or controlled by an organization, but that the organization’s supply chain directly affects.)

It has been many years since Azure and GCP started to report Scope 3 and it is now years since AWS promised that Scope 3 would be provided. They’ve told me they have a team working on it, but until something is released, this is a huge gap. Microsoft released a [good white paper](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/microsoft-scope-3-emissions.pdf) on their Scope 3 methodology back in 2021.

The [AWS Customer Carbon Footprint Tool ](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/)(CCFT) was embarrassing when it was initially released in 2022, and it has made no progress in the years since then. It is going to report zero for everyone for their Scope 1 and 2 carbon footprint, according to the market methodology, has no Scope 3 data, and aggregates too much data together.

I recently tried to use the CCFT data to track progress for a company, and the three usage categories EC2, S3 and Other combined with three geographies EU, Americas and Asia made it impossible to figure out what was going on. The Other category in the Americas is dominating, but that’s all it tells you.

Customer carbon tracking tools from GCP and Azure give you all the details you need, but with AWS you can’t see which region or what service. Escalating to AWS support has produced nothing. Completely useless.

In summary, Amazon is making decent progress towards a reduced carbon footprint, while Google and Microsoft are slipping. However, someone at AWS needs to read and follow the advice given in the [Amazon Exchange Carbon Measurement Guide](https://d3hkct5o8d50yt.cloudfront.net/locale/en-us/resource-type/playbook/playbook-carbon-measurement-and-reporting.pdf). The guidance says that metrics and transparency are needed, and AWS is still at ground zero, with no transparency, and no progress on metrics that their customers have been asking for for years.

## Additional Resources
[Amazon Reporting website](https://sustainability.aboutamazon.com/reporting)[Amazon Carbon Methodology](https://sustainability.aboutamazon.com/carbon-methodology.pdf)[Amazon Renewable Energy Methodology](https://sustainability.aboutamazon.com/renewable-energy-methodology.pdf)[Carbon Free Energy](https://sustainability.aboutamazon.com/climate-solutions/carbon-free-energy?energyType=true)[AWS Sustainability Reporting Framework Summary](https://sustainability.aboutamazon.com/2023-sustainability-reporting-framework-summary.pdf)[Amazon Exchange Carbon Measurement and Reporting guidelines](https://d3hkct5o8d50yt.cloudfront.net/locale/en-us/resource-type/playbook/playbook-carbon-measurement-and-reporting.pdf)[Water Positive Methodology](https://sustainability.aboutamazon.com/aws-water-positive-methodology.pdf)[Accenture report on AWS carbon reduction](https://sustainability.aboutamazon.com/carbon-reduction-aws.pdf)[Amazon Energy Audit](https://sustainability.aboutamazon.com/2023-renewable-energy-assurance.pdf)[Amazon Scope 1 and 2 Audit](https://sustainability.aboutamazon.com/2023-ghg-verification-scope-1-2.pdf)[Amazon Scope 3 Audit](https://sustainability.aboutamazon.com/2023-ghg-verification-scope-3.pdf)
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)