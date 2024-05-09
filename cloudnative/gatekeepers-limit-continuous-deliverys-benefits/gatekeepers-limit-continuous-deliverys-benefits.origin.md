# Gatekeepers Limit Continuous Delivery’s Benefits
![Featued image for: Gatekeepers Limit Continuous Delivery’s Benefits](https://cdn.thenewstack.io/media/2024/05/0f7b4026-restrain-1024x576.jpg)
Developer experience and burnout may have put platform engineering in the spotlight, but focusing on continuous delivery will likely improve developer experience (DevEx) the most at your organization.
There is, however, a speed bump ahead for those automating their deployment pipeline: deployment gatekeepers.
If you don’t increase the number of people with deployment authority, you’ll miss many of the
[benefits of continuous delivery](https://thenewstack.io/ci-cd/). A single deployment gatekeeper will lower your chances of getting a return on your investment within the first 100 days and permanently limit your software delivery performance.
So, how does this happen?
## Failing To Respond to Change
There is a dramatic shift in your work system once you automate your
[deployment pipeline](https://thenewstack.io/ci-is-not-cd/). You’ll have saved many hours of manual work and made the deployment process more reliable. These benefits are often so dramatic you might stop looking for further gains.
Accepting a faster version of your current deployment process means failing to respond to change. This holds back your software delivery performance and reduces the impact of your software on its users and your organization.
In the
[Octopus Deployment Survey](https://octopus.com/whitepapers/deployment-survey-report-2023), we found that teams with a single deployment gatekeeper were less likely to see efficiency gains within the first 100 days than teams with more than one deployer.
CD tools bring granular role-based access controls, so deployers don’t need privileged infrastructure access. Your automation captures the process, so your CD tool will deploy the same way every time. Your IT service management tools can capture and streamline change approvals. Deployments are more repeatable and reliable. Pressing “go” on an automated deployment should be low risk and low ceremony. It might not even be a technical task any longer.
There are two hidden costs when you fail to use your tool’s deployment-specific features. It delays return on investment and stops automation from delivering its full promise. With more than one deployer, 96% of organizations obtained efficiency improvements in the first 100 days, compared to 83% of organizations with deployment gatekeepers.
![The number of organizations reporting efficiency savings within 100 days.](https://cdn.thenewstack.io/media/2024/05/a2879b62-image2.png)
The number of organizations reporting efficiency savings within 100 days (n=250).
You must acknowledge that
[continuous delivery](https://thenewstack.io/continuous-delivery-gold-standard-for-software-development/) and automated deployment pipelines change the nature of software delivery. Don’t be satisfied with the reliability improvements. Look outside your organization for inspiration and you’ll find industry peers who have sped up their software delivery.
Fully embracing modern software delivery benefits teams, users and organizations.
## Gatekeeping’s Impact on Software Delivery Performance
Since the survey, we’ve further tested our findings on gatekeepers. We looked at how the number of deployers related to the throughput metrics from the
[Accelerate State of DevOps Reports](https://dora.dev/research/). **Deployment frequency**: How often your organization deploys code to production **Lead time for changes**: The time it takes for code changes to make it into production
Teams with four or more deployers achieved the highest performance level for throughput. They had shorter lead times for changes, and deployed more often. In terms of the other two groups, there was an interesting result: Gatekeepers deploy more often than teams with two to three deployers, but their lead times are longer.
The chart shows the difference in performance, with the sweet spot being the top left.
![The effect of gatekeeping on software delivery performance.](https://cdn.thenewstack.io/media/2024/05/00797aef-image1.png)
The effect of gatekeeping on software delivery performance (n=212).
One explanation for gatekeeping is that deployments are only partially automated.
Teams without fully automated deployment pipelines will likely require gatekeepers, as they must perform tasks that require privileged access. They might manually update traffic on a load balancer or run a script to perform a post-deployment task such as cache clearance.
Finding a way to automate these final tasks would make it possible to safely increase the number of deployers. Training additional deployers is a crucial improvement opportunity in the free and anonymous Octopus
[Deployment Capability Assessment](https://octopus.com/deployment-capability-assessment), which you can use as part of your continuous improvement process.
## One of Many Factors
You need many skills for high-performance software delivery, but gatekeeping will likely limit most other improvement attempts. If you have to wait on one person or a small group of authorized deployers, you’ll have a limit on how much you can improve your deployment frequency and change lead times.
Gatekeepers are the constraint, so optimizing other parts of your software delivery won’t make a difference. Add more deployers and see how it transforms your performance.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)