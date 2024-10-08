# OSI’s Definition of Open Source AI Raises Critical Legal Concerns for Developers and Businesses
As the CTO of [Lightning AI](https://lightning.ai/) and early core contributor to [PyTorch](https://thenewstack.io/official-pytorch-documentary-revisits-its-past-and-its-future/), I take open source to heart. Operating in open source for two decades and in AI for the last, I am particularly interested in the Open Source Initiative’s (OSI) [recent definition](https://thenewstack.io/open-source-ai-osi-wrestles-with-a-definition/) of [open source AI](https://thenewstack.io/why-open-source-ai-has-no-meaning/). While comprehensive in many respects, I believe it leaves a critical question unanswered, particularly for developers and businesses looking to adopt open source AI models with confidence.

The elephant in the room that the draft leaves out — until the last footnote in the document — is that it doesn’t “take any stance as to whether model parameters require a license or any other legal instruments, and whether they can be legally controlled by any such instruments once disclosed and shared.”

What does that mean in practice? An OSI-approved open source license for an AI system may not reasonably imply that it is “free for commercial use” as it does for regular software with the usual disclaimers.

A model may be trained on unlicensed data (like books or movies). However, it may still be considered open source if all information about data sources, [data preparation scripts](https://thenewstack.io/dont-let-the-script-kiddies-steal-your-cloud-data/), and related materials is shared. This guarantees transparency, enabling due diligence on the source data and its licensing status, but it differs from the general perception of what open source should guarantee.

Understanding these nuances is crucial for businesses to make informed decisions about adopting open source models in their AI systems. To be of practical value, especially in a business context, a definition of open source AI needs to give reasonable confidence that what is being licensed can be licensed (or used) that way.

To understand why, we need to consider two fundamental questions tied to the use of licensed software, open source or not:

- What conditions does the licensor impose on the users? Can the software be used for any purpose, or are there exceptions? Can modified versions be redistributed without limitations? Can a SaaS be built with it without restrictions, or are there royalties involved?
- Can the licensor release the software under the stated terms? The copyright notice accompanying the license typically indicates this.
In essence, the licensor must own the copyright or hold a license to the material used to produce their software and clearly define the permissible uses and conditions for redistribution of their software. Let’s explore this with a few examples:

**Example 1: Software Systems**
I write software from scratch. Since I created it, I own the copyright and can choose to release it under the Apache 2.0 license (for example), which allows anyone to use, modify, and redistribute it.

**Example 2: Software Systems**
I write a piece of software by copying and slightly modifying pieces of software released under restrictive licenses. I decide to release it under the Apache 2.0 license. However, whether I can legally do so is questionable. Users adopting this software risk being sued by the original authors.

**Example 3: AI Systems**
I train a [model on data](https://thenewstack.io/nosql-data-modeling-mistakes-that-ruin-performance/) for which I do not hold the copyright (e.g., books or YouTube videos). I decide to release the resulting model under the Apache 2.0 license, sharing the code and weights. The question arises: can I claim copyright over those weights? Opinions vary, making this a complex issue.

The OSI’s definition states that this matter is out of scope. Suppose a model is trained on unlicensed data, but the scripts and weights are available under an open source license. In that case, it is still considered open source by its standards as long as the methods and source data are openly documented. While this stance is understandable, it offers limited practical value for companies assessing the legal viability of adopting such models.

By neglecting to deal with weights licensing, the OSI is leaving a gaping hole that will make licenses less effective in determining whether OSI-licensed AI systems can be adopted in real-world contexts.

Open source AI can only move forward toward [widespread enterprise adoption](https://thenewstack.io/whats-stopping-webassembly-from-widespread-adoption/) with this understanding. If outside the OSI, more precise definitions will likely emerge elsewhere to fill the gap.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)