# Unlocking Platform Engineering Success with North Star Metrics and OKRs
# Background
Platform engineering is an essential aspect of modern software development. It encompasses a range of skills and practices, including Cloud and infrastructure engineering, DevSecOps, and SRE — all of which are critical to ensuring the successful development and operations of complex software systems.

To drive success and ensure optimal performance in platform engineering, it’s essential to establish North Star Metrics and OKRs. These metrics provide a clear measure of success and help teams to stay focused on their goals.

# NSMs and OKRs
As I [posted](https://www.linkedin.com/feed/update/urn:li:activity:7020153031744790528/) few months ago, ever wondered how to measure the impact of your platform engineering team’s work, especially in challenging economic times? This blog dives deep into how North Star Metrics (NSMs) and Objectives and Key Results (OKRs) can be your secret weapons.

As a platforms and infrastructure leader, I’ve seen firsthand how these tools can transform the way teams track progress and demonstrate their value. Let’s explore how we’ve implemented NSMs at Palo Alto Networks and Cohesity, and how you can apply these strategies to your own organization.

**Discover how NSMs and OKRs can:**
**Illuminate your team’s impact:**Clearly demonstrate the business value of your platform engineering efforts.**Optimize processes:**Identify areas for improvement and streamline workflows.**Navigate economic uncertainty:**Weather the storm by aligning your team’s goals with broader business objectives.
# Difference
First let’s understand the[ difference](https://www.slingshotapp.io/blog/north-star-metric) between NSMs and OKRs. In simple terms the difference can be described as below.

OKRs align the goals of the individual with the team and goals of the team with the group or company, the NSM provides the necessary visibility and accountability that brings knowledge for the next steps and data-driven decisions.

Now let’s deep dive into NSMs for platform engineering at[ Palo Alto Networks](https://www.linkedin.com/post/edit/7025957335961391104/#).

A north star metric should consist of 2 parts:

- a statement of your product vision and
- a metric that serves as a key measure of your current product strategy.
# Platform Engineering NSMs at Palo Alto Networks
Following the above said criteria , here is our engineering platform’s vision and associated NSM

In the process of coming up with right north star metrics for our team, we’ve adopted an unwritten rule of “not having more than 3 NSMs’ . Now that our team’s vision and one of the NSMs have been identified, we’ve had numerous discussions to narrow down on “what would be other north star metrics” that can be used to measure the performance and the impact of the platform engineering initiatives. Eventually, we arrived at the below 3 NS metrics -

- Platform adoption and usage frequency
- Productivity index
- Developer NPS
Once you identify those NSMs then start working backward to identify[ KPIs](/wise-engineering/platform-engineering-kpis-6a3215f0ee14) (Key Performance Indicators) for each initiative or project.

# Examples for KPIs to NSM alignment
# KPIs per initiative
The above illustration is focusing on how we can work backward to identify KPIs per initiative to track north star metric but one can also track NSMs and KPIs per platform initiative too.

Let’s take an example of specific project/initiative to deep dive into KPIs i.e. our internal observability platform and it’s associated key performance indicators we track -

- Number of team/s or engineers leveraging the platform
a. #tenants(i.e. Unique products) sending observability data

b. #unique user logins per day

c. #downloads per SDK per month

2. SLOs for platform stability

a. Availability of key components

b. Performance of critical components

3. Costs associated with the platform

a. Chargeback to each team based on unit economics

b. Comparative costs analysis with vendor offerings as well as other product teams

3. Quarterly developer NPS survey

a. NPS score

4. Productivity Index

a.Meantime to onboard new tenants (Platform)

b. Meantime to resolve production issues (MTTR) per tenant

## Meta Monitoring of observability platform
## Usage analytics
# Conclusion and the next steps
While NSMs play a critical role in creating required visibility and understanding on the platform engineering value chain, we as a platform team should continue to focus on pushing this visibility within platform engineering and product teams to ensure the KPIs data is actionable. Also, note that KPIs are not static and are dynamic and hence should be reviewed and updated on a periodic basis.

As next steps, we are planning to automate end to end feedback mechanisms where applicable. For example — we not only send observability costs in the weekly report but also provide the recommendations to optimize those costs. In my next blog, I will be covering platform engineering OKRs in detail. Feel free to reach out with any questions or feedback.