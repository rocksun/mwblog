**This week, Cohere released** North Small Translate 1.0 under a CC BY-NC 4.0 license: the weights are there to download, evaluate and study, but not to run in production without a commercial agreement.

It’s an interesting choice from the Canadian foundation model company, which has built its pitch around [AI sovereignty for regulated industries](https://thenewstack.io/cohere-sovereign-coding-model-north-mini-code/) and describes this release as part of a mission “to make sovereign AI a technological reality.” Sovereignty there means control over where the model runs and who sees the data. A commercial license keeps that promise intact. It stops short of independence from Cohere. Enterprises keep their data and their infrastructure. They don’t get to fork the model, build a product on it, or keep running it if the terms change at renewal.

## Open weights, except for commercial production

North Small Translate is an open-weights mixture-of-experts model built for machine translation across over 50 languages and locale variants. It has [218 billion total parameters](https://docs.cohere.com/docs/north-small-translate-1.0), with 25 billion active parameters and a 16,000-token context window.

> Not all users have the same access to those weights.

[Per Cohere](https://docs.cohere.com/changelog/north-small-translate-1-0), the model is designed to give researchers, developers, and enterprises “flexible ways to evaluate and deploy machine translation while retaining control over their data and infrastructure.”

That’s an appealing description for organizations keen on pursuing sovereign AI. But the open-weight release comes with an important caveat: Not all users get the same rights to take advantage of those weights.

North Small Translate is available today on Cohere’s free tier through the Chat V2 API. For those who intend to use the model weights for non-commercial use, the FP8 weights are available on Hugging Face under the CC BY-NC 4.0 license.

But if enterprises want to put them into production, then a different set of terms applies. They’ll have to purchase a commercial license and deploy North Small Translate through [Model Vault](https://cohere.com/solutions/model-vault), Cohere’s fully managed inference platform.

## Cohere’s not the only one drawing a line around open-weight use

Other AI companies are starting to attach more conditions to their open-weight models, too.

Last month, Chinese AI lab [Z.ai](https://z.ai) released the weights for its flagship GLM-5.3 model on Hugging Face. But like the Canadian AI company, it also [changed its licensing terms depending on who is deploying the model](https://thenewstack.io/zai-glm-weights-license/) — a departure from its previous approach. While GLM-5.2 shipped under the permissive MIT license, GLM-5.3 adds new requirements for certain commercial users.

> Cohere, for its part, has been similarly mum about why it made North Small Translate’s open weights noncommercial.

These requirements apply only to companies with aggregate revenue over $10 billion over 12 consecutive months. Additionally, if these companies want to host GLM-5.3 or its derivative works for commercial purposes, they have to first pass the Chinese lab’s security review.

Z.ai didn’t explicitly spell out why it decided to make such an about-face for GLM-5.3, which is especially puzzling given that its predecessor shipped under MIT without any commercial stipulations. Cohere, for its part, has been similarly mum about why it made North Small Translate’s open weights non-commercial.

## Sovereign deployment, with restrictions

The Canadian company’s decision to make North Small Translate available as open weights but gate commercial use is a head-scratcher, given its history of selling sovereign AI to enterprises.

In fact, in June, it pitched [North Mini Code](https://cohere.com/blog/north-mini-code), its first coding model, as a response to developers demanding the same sovereignty guarantees that regulated industries have long required.

Unlike North Small Translate, though, this open-weight model was released under an Apache 2.0 license from the get-go — without any comparable restrictions for commercial users.

Clearly, Cohere is going in a different direction with its latest open-weight release, emerging as another example of AI companies putting tighter terms around increasingly capable open-weight models.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)