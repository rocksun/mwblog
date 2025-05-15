# Recce Believes Data Reviews Will Become as Important as Code Reviews
![Featued image for: Recce Believes Data Reviews Will Become as Important as Code Reviews](https://cdn.thenewstack.io/media/2025/04/2d16070b-rose-galloway-green-mzpnzk3prtu-unsplash-1024x602.jpg)
[Rose Galloway Green](https://unsplash.com/@rgreen?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/a-blue-pipe-laying-on-top-of-a-pile-of-dirt-MzPnzK3prTU?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
Data has become the lifeblood of many businesses, and tools like dbt and others have transformed how that data is managed and consumed, including by AI systems. But [CL Kao](https://www.linkedin.com/in/clkao/), the founder and CEO of [Recce](https://datarecce.io/), argues that while many of these tools make it easier to build [data pipelines](https://thenewstack.io/finding-the-right-data-architecture-for-rag-pipelines/) and manage data programmatically, what’s missing are modern tools for evaluating the impact of upstream code changes on downstream data. Kao believes that in the near future, data reviews will become as important as code reviews, and the company is looking at how it can apply these same ideas to the output of large language models (LLMs) and AI agents as well.

Kao, who also co-founded the Git precursor [SVK](https://www.perl.com/pub/2004/03/03/svk.html/), launched the Recce open source project in 2023. With $4 million in pre-seed funding led by Heavybit (with participation from Vertex Ventures US, Hive Ventures and a number of angel investors), the company is now launching Recce Cloud into private beta. Meanwhile, the Recce open source project today hit version 1.0.

![](https://cdn.thenewstack.io/media/2025/04/1c9668c7-data-consistency-with-automated-row-count-and-schema-checks.png)
Data consistency with automated row count and schema checks.

“When we started this project, we figured there’s an interesting gap in the CI/CD workflow for data systems,” Kao said when I asked him about the origins of the project. “In software — traditional software — you have pretty clear criteria for how the software should behave. But for data systems, a lot of the time, you don’t have very easy-to-write tests.”

Developers can check whether a value is within an expected boundary — and some of the existing tools already do that — but Kao argues that it is very hard to write exhaustive tests for these systems. And how would you know if any deviation from the development environment to the production environment is intended or not, for example? Any of these changes could have unforeseen downstream impacts and lead to faulty metrics and costly mistakes.

What happens today is that developers will make changes to production systems, but even with added tests, they won’t know if the results are correct or not. Add AI models into the mix here, with their probabilistic results, and it becomes even more important to have the right tooling to ensure that these results are correct.

![](https://cdn.thenewstack.io/media/2025/04/e7559255-lineage-diff-in-recce-app-helps-you-visualize-the-impact-area-of-dbt-data-model-changes.png)
Lineage Diff in Recce app helps you visualize the impact area of dbt data model changes.

“With the initial analysis, we can very precisely pin down where the potential changes are happening. And then, to add a dimension of risk or how important one thing is, the user can selectively add certain checks, checks in comparison to production. Did they change in a meaningful way? Or did you not expect a change, and indeed it didn’t?“

Since a lot of these pipelines handle massive amounts of data, Recce users typically only sample the data they create to check for issues or create a limited look-back period.

Clearly, there is demand for a tool like this, with the open source version seeing well over 3,500 downloads per week on GitHub now. Recce says the tool’s users range from the Philadelphia Inquirer to telecom companies, health tech startups and even government agencies in Brazil and Australia.

It’s maybe no surprise then that Recce is also gearing up its efforts to monetize this service. Here, it is following the standard playbook by launching a hosted version of its service under the Recce Cloud moniker. This new service includes a number of collaboration features like data-validation context sharing across teams with lineage diffs, custom query results and checklists included. Recce Cloud also includes an integration with GitHub to ensure that code is only merged when all data validation checks have been approved.

“Data pipelines are the New Secret Sauce for every company building with AI, enabling teams to create and improve high-quality training data from their own IP,” said Heavybit general partner and DevOps trailblazer [Jesse Robbins](https://www.linkedin.com/in/jesserobbins/), who is joining Recce’s board. “Recce provides the essential toolkit for unlocking the full value of their data with iteration, refinement, and monitoring, while mitigating the risk of errors and corruption. Heavybit is thrilled to support them as they grow the ecosystem for data pipeline validation in the age of AI as part of our ongoing mission of 10+ years: Bringing critical enterprise infrastructure to market.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)