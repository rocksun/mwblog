# Using LLMs Right: Leveraging AI for Augmented Data Quality
![Featued image for: Using LLMs Right: Leveraging AI for Augmented Data Quality](https://cdn.thenewstack.io/media/2025/05/27e80697-mohammad-rahmani-1bnqvgzuy0u-unsplash-1024x683.jpg)
[Mohammad Rahmani](https://unsplash.com/@afgprogrammer?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash.](https://unsplash.com/photos/black-laptop-computer-turned-on-beside-black-ceramic-mug-1bNQVGzuy0U?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
Data quality has evolved from a “nice-to-have” to an essential and, in some cases, mission-critical part of a data operation. When AI started to gain traction, many data governance and data science leads saw the writing on the wall. The playing field is leveling, and those who can properly capitalize on their data will win with new use cases. Companies that underinvest in data quality are struggling to keep up.

Initially, AI was seen as a silver bullet, promising to automate complex processes and handle large volumes of data effortlessly. However, it’s become clear that without a strategic framework, AI can be as problematic as it is beneficial.

Briefly, it seemed like we could overcome the classic problem of ‘garbage in, garbage out’ by scale. However, the recent slowdown in the biggest models shows there are limits. The volume of training data is essential, but data quality is quickly becoming a differentiator.

## Data Quality in the Modern Data Stack
Organizations have been running data quality programs for decades. Guides, best practices, and experts will tell you how to write data quality rules, deploy them, and prioritize different parts of your data stack. So, it should be easy, right?

Unfortunately, the modern data landscape is anything but simple. What worked ten years ago, when every company had one central enterprise data warehouse or database with a few interconnected systems, doesn’t scale anymore.

Instead of dealing with a couple of systems and data formats, businesses must deal with data landscapes comprising hundreds or thousands of different data systems. While technologies to increase processing to a petabyte scale are available (if you have enough money), the recent push for data democratization means data complexity is about to explode.

This is a widely recognized problem. Gartner even reclassified its Magic Quadrant for Data Quality Solutions as [Augmented Data Quality Solutions](https://www.gartner.com/en/documents/6246519), adding a focus on automation and scale.

The writing is on the wall. To win the AI race, you must rethink how to approach data quality.

## AI Will Fix… AI?
In the old days, to [manage growing complexity](https://thenewstack.io/managing-complexity-and-avoiding-chaos-in-digital-operations/), you hired more people to take care of more systems. That approach worked for years and led to whole departments of data engineers cranking out data quality rules, configurations, and reports. This approach doesn’t scale anymore, but fortunately, the modern LLM [revolution has arrived at the right time](https://thenewstack.io/2024-streaming-roadmap-navigating-the-real-time-revolution/).

Consider the following use case. ChatGPT has been used to fix data quality issues in a database of user interactions from various [apps to prepare it for an AI](https://thenewstack.io/real-time-ai-apps-using-apache-flink-for-model-inference/) model that will provide personalized recommendations. It shows how we can use AI to fix data for AI.

In this example, we just need to run this request every day as new data comes in and run it on our other systems as well, covering various data sources and various data volumes…

You can probably see the problem here already, and it’s not isolated.

Consider the reliance on LLMs to automate complex data cleansing without proper oversight, which often [leads to errors](https://thenewstack.io/red-hat-human-error-a-leading-cause-of-kubernetes-security-mishaps/) and inconsistencies that only manifest at scale. Even the example above works well on specific use [cases but will struggle with scale](https://thenewstack.io/case-study-how-lacework-scaled-data-streaming-with-redpanda/), consistency and hallucinations.

## AI Will Fix AI… but It’s Not That Simple
AI can’t scale using only its raw power in its current form. You have to be intentional about where and how to use it. Running LLM-based AI processing on thousands of sources and petabytes of data isn’t feasible. However, we know how to address growing data volumes as there are big data approaches that can run at almost any scale; they just need to be configured correctly. So, what if we ask ChatGPT a different question?

In this scenario, the model was asked to write data quality rules. Instead of a full data set, it only received a sample and was asked to propose rules to be run on top of the data.

The rules the model proposed are examples of logic that can be used repeatably with predictable outcomes. The rules scale to any data size and source if implemented in suitable processing technology.

This prompt will only need to be run when the data source or profile changes significantly. You can take this list of newly generated data quality rules and use it as input for rule mapping, applying it to a different dataset without needing to re-generate rule logic. This scales far better than asking AI to detect issues in your data.

Of course, there are caveats. The problems with predictability and hallucinations are not eliminated, and scaling it for large data landscapes also creates some orchestration challenges.

## Use AI Intentionally
The correct application of LLMs for data quality is a strategic imperative. LLMs possess immense potential to revolutionize data quality practices, but only when used precisely and intentionally.

Organizations [must engage with AI as part](https://thenewstack.io/building-privacy-aware-ai-software-with-vector-databases/) of a broader, well-thought-out data governance strategy. The successful integration of LLMs into data quality processes requires a clear understanding of both the capabilities of these models and the unique challenges of your data landscape.

As we look to the future, the question remains: How will you adapt your data quality strategies to responsibly and effectively leverage AI’s full potential?

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)