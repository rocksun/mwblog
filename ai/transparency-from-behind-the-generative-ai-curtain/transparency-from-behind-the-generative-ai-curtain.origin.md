# Transparency From Behind the Generative AI Curtain
![Featued image for: Transparency From Behind the Generative AI Curtain](https://cdn.thenewstack.io/media/2024/07/4bd1b47b-curtain-1024x576.jpg)
AI foundation models have become like supermodels: In this post-ChatGPT world, names like [LLaMA](https://llama.meta.com/), [Gemini](https://gemini.google.com/) and [Claude](https://claude.ai/) now carry the same buzz and instant recognition for tech pundits that human celebrities once commanded.

However, as AI rises in global importance, so does our need to know about the technology that produces the results we get from typing into those prompt boxes. [Two recent studies](https://crfm.stanford.edu/fmti/May-2024/index.html) from researchers at Stanford, MIT and Princeton delved into the AI foundation models that are behind some of the world’s most advanced — and wildly popular — generative AI tools, used by millions ([even billions](https://blog.google/inside-google/message-ceo/google-io-2024-keynote-sundar-pichai/#gemini-era)) of people each day. The need for transparency is paramount.

However, results from the [2024 Foundation Model Transparency Index](https://crfm.stanford.edu/fmti/May-2024/index.html) show that, over time, as companies are investing more and more money into developing their flagship foundation models, they are becoming less and less transparent about the massive mountains of data they use to train these models, and where that data comes from.

## What Are Foundation Models?
The term “foundation model” arose as a collective descriptor for the massive, deep-learning neural networks that underpin generative AI. [Foundation models](https://thenewstack.io/vision-foundation-models-when-does-size-matter/) are trained on mountains of data to perform a wide spectrum of jobs, from generating text, images and programming code to fluently conversing in natural language in response to written prompts and questions. Arguably, though, their greatest power is to underpin new AI applications: Rather than building your own models from scratch, foundation models allow engineering teams to develop new generative AI applications more quickly and cost-effectively.

## Why AI Transparency Matters
Because the same relatively small handful of foundation models are behind so many human-facing generative AI tools, the need for transparency is paramount. When we use, for instance, [ChatGPT](https://openai.com/chatgpt/) to generate text, [Stable Diffusion](https://stability.ai/) to create images and [Tabnine](https://www.tabnine.com/) to generate code, we need to understand how their foundational ML models are developed and deployed. Users want to know that we can trust the AI tools we have rapidly come to not just know and love, but also heavily depend upon. We need to know that they are fair, explainable and safe.

This sense of urgency in building trust and transparency now, during what is essentially AI’s Wild West period, comes from lessons learned in the early, unregulated days of social media. Knowing better now, it’s possible to prevent similar crises as we begin to adopt AI. But how do we measure actual, functional transparency within still-emerging technology?

## Measuring AI Transparency
In October 2023, researchers from Stanford, MIT and Princeton collaborated to plant an important AI transparency flag by assessing the flagship models from the (then) top 10 foundation models. The resulting white paper, titled “[The Foundation Model Transparency Index](https://crfm.stanford.edu/fmti/May-2024/index.html)” (FMTI) presented a transparency index of those top 10 then-major foundation models. Meta’s model scored the highest by meeting 54 out of 100 transparency protocol factors, while Amazon scored the lowest (12 out of 100). The mean score of 37 for all model providers — not exactly a passing grade — reveals an industry struggling to [open itself](https://thenewstack.io/transparency-and-community-an-open-source-vision-for-ai/) to public scrutiny.

[The same researchers issued a follow-up report in May 2024, with some changes](https://crfm.stanford.edu/fmti/May-2024/company-reports/index.html). The original report relied on publicly available data; for the six-month follow-up study, the model developers themselves submitted transparency reports disclosing their practices for each of the FMTI’s 100 indicators. This time, 14 organizations submitted transparency reports. Participating developers also went above and beyond the original 100 transparency protocol factors that the researchers had defined; overall, organizations presented an average of 17 new indicators of transparency information in their individual reports.
## Rising Transparency Scores
What did the FMTI 2024 reveal in terms of changes from 2023, and what does that tell us about the new status quo for transparency?

This time, the top transparency score rose to 85 out of 100 for the StarCoder foundational model from BigCode/Hugging Face/ServiceNow. The mean score for all 14 model developers climbed to 58 out of 100, a 21-point improvement over the October 2023 FMTI mean.

Overall, the 2024 FMTI documents noticeable improvement: The top transparency score rose by 31 points, and the bottom score by 21 points. The eight developers who appeared in both the first and the follow-up report each improved their scores; Amazon made the greatest gain overall, jumping from 12 points in 2023 to 41 in 2024. Even more reassuringly, one developer satisfied an impressive 96 out of the 100 transparency indicators established by the researchers, and multiple developers managed to satisfy 89 of the indicators.

These trends are on the whole quite positive, but the numbers also reveal some less than rosy results. While there is significant improvement in the overall status quo for transparency, some areas remain stubbornly inaccessible. According to the report, “Information about data (copyright, licenses, and PII), how effective companies’ guardrails are (mitigation evaluations), and the downstream impact of foundation models (how people use models and how many people use them in specific regions) all remain quite opaque.”

In other words, there are some critical areas where model developers are still obscuring their practices, particularly with regard to data sourcing, privacy and mitigation.

## Where Do We as a Community Go From Here?
Possibly the most important takeaway: transparency around data access declined from 20% in October 2023 to merely 7% in May 2024. In the new report, the researchers attribute this to “significant legal risks that companies face associated with disclosure of the data they use to build foundation models.” Particularly, “these companies may face liability if the data contains copyrighted, private or illegal content.” Unfortunately, 2024 participating model developers also had low “model mitigation” scores, meaning that they don’t adequately disclose their strategies for addressing problems with copyright violations or privacy infringements.

It is crucial that tech companies prioritize transparency in AI, because outside of the sector itself, most people simply do not understand what it is or how it actually works. To be fair, just as the technologies are new, standards and expectations around transparency are new as well.

These are uncharted waters for technology, and in some ways we are making the path by walking. The greatest value derived from these FMTI reports and protocols is in providing model developers with defined and actionable steps toward improving model transparency.

The information delta between the 2023 and 2024 FMTI reports reveals areas of sustained — and systemic — opacity within foundation model providers. When it comes to AI, foundational model developers’ orgs themselves need to earn the trust and confidence of not only end users but government entities and, not to overstate things, humanity in general.

As a community, our job is to push for accessibility. No matter how — or even if — those of us in software development are making use of AI and ML technologies, we share the responsibility of ensuring that these emerging technologies function based on ethical standards, and with a collective aim of reducing any potential harm.

As consumers of AI, enterprises can push for this accessibility by asking informed questions before moving forward with adopting specific AI tools. This report reveals why it’s crucial to review the actual license agreements and terms of service of not just the vendor providing an AI code assistant tool, but also the license agreement and TOS of the models used behind the tool.

Our takeaway: Until transparency becomes simply the default way that foundational model developers operate, the only way to guarantee absolute privacy for the data used to interact with any AI platform is for there to be no way for that data to leave your perimeter.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)