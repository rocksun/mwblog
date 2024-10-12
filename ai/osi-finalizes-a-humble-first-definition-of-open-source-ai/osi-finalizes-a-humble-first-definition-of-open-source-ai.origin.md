# OSI Finalizes a ‘Humble’ First Definition of Open Source AI
![Featued image for: OSI Finalizes a ‘Humble’ First Definition of Open Source AI](https://cdn.thenewstack.io/media/2024/10/74582bf8-osi-finalizes-a-humble-first-definition-of-open-source-ai-1024x576.jpg)
After nearly three years of planning, including community meetings and [a months-long global “roadshow”](https://thenewstack.io/open-source-initiative-hits-the-road-to-define-open-source-ai/) to [gather feedback](https://thenewstack.io/open-source-ai-osi-wrestles-with-a-definition/), the [Open Source Initiative (OSI)](https://opensource.org/) has published [Release Candidate 1 of its long-awaited definition for open source AI](https://opensource.org/deepdive/drafts/the-open-source-ai-definition-1-0-rc1).

The document, published Oct. 2, includes definitions for four different kinds of data: open, public, obtainable and unshareable.

It also demands transparency from creators and sponsors of AI technology that bears the open source label, requiring that those creators share the data (if shareable), along with the source code used to train and run the system, and the model’s parameters.

What Release Candidate 1 doesn’t include: any attempt to address safety or risk limitations. Those concerns should be handled by governments, OSI Executive Director [Stefano Maffulli](https://www.linkedin.com/in/maffulli) told The New Stack.

“Governments around the world have different frameworks to understand what is acceptable risk, or what is ethical, sustainable, valuable,” he said. “All of these words, they come with trade-offs. It’s not our job to decide which ones they are.”

OSI’s goal in crafting the definition, he suggested, is to leave room in the definition for governments to act as they see fit. “We wanted to make sure that the definition was not going to be an impediment for that,” Maffulli said. “Otherwise, it will be failing on delivery, right?

## ‘No New Features, Only Bug Fixes’
OSI is continuing to gather feedback (on [hackmd](https://hackmd.io/@opensourceinitiative/osaid-1-0-RC1) and [on the OSI forum](https://discuss.opensource.org/)) about Release Candidate 1 and [endorsements](https://opensource.org/deepdive/drafts/the-open-source-ai-definition-1-0-rc1#endorse) ahead of its planned launch at the [All Things Open](https://www.eventbrite.com/e/all-things-open-2024-tickets-916649672847?discount=NEWS20) conference on Oct. 28 in Raleigh, N.C. There will likely be enough minor tweaks to justify a Release Candidate 2 ahead of the rollout, Maffulli said. But the intention is to start wrapping it up for now.

“With the release candidate cycle starting today, the drafting process will shift focus: no new features, only bug fixes,” [reads a note from OSI on its website](https://discuss.opensource.org/t/the-open-source-ai-definition-v-1-0-rc1-is-available-for-comments/628). “We’ll watch for new issues raised, watching for major flaws that may require significant rewrites to the text. The main focus will be on the accompanying documentation, the Checklist and the FAQ.”

However, Maffulli said, [the definition will be a work in progress](https://thenewstack.io/why-open-source-ai-has-no-meaning/): “This is 1.0, but it’s a very humble 1.0. We’re not saying that this is done deal, we’re never going to look at it again and don’t bug us — like, drop the mic and go home.

“What’s going to happen is that we expect that 1.0 is going to be ready for use, which means that corporations, research institutions, academics, etc., deployers, users, can use it as a reference to start interpreting what they find on [Hugging Face](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/) or something. They see a model, and they have now a reference.”

Maffulli added, “We’ve basically built something that is more of a manifesto than an actual working, 10-point checklist definition to evaluate legal documents. We’re very early, in very early stages, and that’s why it’s a humble 1.0 release.”

## What’s in Release Candidate 1?
“Open Source means giving anyone the ability to [meaningfully fork (study and modify) your system](https://thenewstack.io/linux-foundation-joins-opentf-to-fork-for-terraform-into-opentofu/), without requiring additional permissions, to make it more useful for themselves and also for everyone,” reads the FAQ accompanying Release Candidate 1.

In line with that principle, the FAQ states open source AI is “an AI system made available under terms and in a way that grant the freedoms to:

**Use**the system for any purpose and without having to ask for permission.**Study**how the system works and inspect its components.**Modify**the system for any purpose, including to change its output.**Share**the system for others to use, with or without modifications, for any purpose.
So, what’s in this near-final 1.0 version of the open source AI definition? Here are some key components:

### Demands for Transparency
As previously stated, OSI’s Release Candidate 1 requires open source AI project creators to share the data information used to train the system, the complete code used to train and run the system, and the model parameters, “such as weights and other configuration settings.”

Will the level of transparency required for open source AI, under this definition, cause some creators of AI projects to keep them proprietary?

“That’s exactly what I think will happen,” Maffulli said. But, he added, this is also [what’s happened to open source software more generally](https://thenewstack.io/whats-next-for-companies-built-on-open-source/). “There are companies like [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) and [Oracle](https://developer.oracle.com/?utm_content=inline+mention), they don’t release the source code of their — call them ‘crown jewels,’ like Windows and Microsoft Office and the Oracle database.

“That source code is not available. It’s not transparent. And that doesn’t mean that open source is lost or anything like that. Just that it’s another part of the ecosystem, that you know exists.”

### 4 Different Categories for Data
The document’s FAQ section breaks data into four categories, noting that all four might be used to train a language model:

**Open:**“Data that can be copied, preserved, modified and reshared,” reads the FAQ.**Public:**“Data that others can inspect as long as it remains available,” the FAQ described, noting that “this data can degrade as links or references are lost or removed from network availability.”**Obtainable:**“Data that can be obtained, including for a fee.”**Unshareable:**“Data that cannot be shared for explainable reasons, like Personally Identifiable Information.”
For data that falls into the “unshareable” category, the goal of enabling a “meaningful fork” of the technology is the guide:

“[T]he ability to study some of the system’s biases demands a detailed description of the data — what it is, how it was collected, its characteristics, and so on — so that users can understand the biases and categorization underlying the system. This must be revealed in detail so that, for example, a hospital can create a dataset with identical structure using their own patient data.”

The four categories reflect some messy reality that OSI encountered during its long period of research and community feedback.

When the process began, Maffulli said, the impulse was to insist that all three elements of an open source AI — data, code and parameters — be open source. “

But, he added, “Then you start looking a little bit deeper, and we found two main issues. One is on the parameters themselves, parameters weights. What are those things? From the law perspective, it’s not clear whether they have copyright or other exclusive rights on top. So, OK, big, big question mark goes on that box.”

And then, he said, there’s data: “Immediately there is an issue, OK, so maybe there is private data, there is copyrighted data, there is medical data, there is data that you can’t distribute — you can read it and make a copy of, but you cannot redistribute.”

It presented a [conundrum](https://opensource.org/blog/how-we-passed-the-ai-conundrums). “To simplify the conversation,” Maffulli said, “we identified those four blocks.”

The FAQ acknowledges that data, and transparency around data, has been a perennial sticking point throughout the discussion that led to Release Candidate 1.

“Some people believe that full unfettered access to all training data (with no distinction of its kind) is paramount, arguing that anything less would compromise full reproducibility of AI systems, transparency and security,” the FAQ reads. “This approach would relegate Open Source AI to a niche of AI trainable only on open data … That niche would be tiny, even relative to the niche occupied by Open Source in the traditional software ecosystem.”

As data “gets more and more fine-grained and complicated,” Maffulli told The New Stack, “the definition itself, in its final form, provides for an escape route,” that accommodates differences in data and allows for more open source AI projects to emerge.

Large companies and organizations like [OpenAI](https://thenewstack.io/openais-realtime-api-takes-a-bow/), “technically don’t have any obstacle to do whatever they want to do. They have no obstacle, neither technical nor legal, to use any of those four kinds of data for dev training.” But organizations with fewer resources to enter into commercial partnerships with data providers, he said, are at a disadvantage.

He added, “Either the definition open source would have to limit the availability of open source AI by excluding some of that kind of data, or we needed to provide a way for the public, and the open source communities in general, to have access to [large language models](https://thenewstack.io/llm/), just like the large corporations can do it. And that’s what we’re doing.”

**Clarification:** This article has been changed from a previous version, to provide more context for Maffulli’s comment that the OSI open source definition offers “an escape route” in the way it categorizes types of data.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)