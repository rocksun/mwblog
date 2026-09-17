**When OpenAI launched GPT Images 2.5 this week**, the company promised better results for a common editing task: changing one part of an image without messing up the rest.

And so developers have two new models to try, Flare and Sunburst, but some homework awaits anyone choosing between them. OpenAI lists identical token rates for both, without explaining how their per-image costs compare.

Flare is positioned as the faster, “default” option for most applications, while Sunburst offers greater precision and control over edits, but with longer generation times. OpenAI lists the same token rates for both models, though it’s less clear how their real-world costs will compare.

## Flare vs Sunburst

OpenAI [calls](https://openai.com/index/introducing-chatgpt-images-2-5/) Flare “the default choice for most applications,” letting developers level up image quality with lower latency than its previous model. Per the AI company, that means the model can handle any everyday image-generation workload, such as social content, rapid image prototyping, visual search, and image generation.

Most interestingly, OpenAI says Flare delivers higher-quality images than does GPT-Image-2 with 50% lower latency.

Meanwhile, the AI company positions Sunburst as the more precise option, saying the image model is “built for premium visual workflows that benefit from tighter control across edits.” For developers working on high-stakes creative assets, like production-ready campaigns or product imagery, Sunburst looks like the better pick.

But OpenAI doesn’t make it clear how much Sunburst’s greater precision will cost compared to Flare in time and money.

## Same token rates, not necessarily the same bill

On paper, OpenAI says Flare and Sunburst have the same token rates: $5 per million text input tokens, $8 per million image input tokens, and $30 per million image output tokens. But that doesn’t necessarily mean using either model will cost the same for the same kind of image.

Although image generation pricing is based on the number of tokens, the AI company gives no explicit note on how to estimate GPT-Image-2.5 token consumption.

And if developers think they can look to OpenAI’s existing [image-cost calculator](https://developers.openai.com/api/docs/guides/image-prompting) for an estimate on what image generation may cost with the new models, think again. One [explicit](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst) statement the company does make is: “Token rates match GPT Image 2. The GPT Image 2 calculator does not estimate GPT Image 2.5 token consumption.”

> On paper, OpenAI says Flare and Sunburst have the same token rates: $5 per million text input tokens, $8 per million image input tokens, and $30 per million image output tokens. But this doesn’t necessarily mean using either model will run up the same bill for the same kind of image.

Without a guaranteed way to estimate how many tokens each model will use, that means there’s no way to tell from OpenAI’s published pricing what it’ll cost to generate the same kind of image with Flare versus Sunburst before getting started.

Then there’s the latency question.

OpenAI says Flare delivers higher-quality images than GPT-Image-2 with 50% lower latency. But what about Flare versus Sunburst?

Neither its launch announcement nor the model pages for [Flare](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare) or [Sunburst](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst) make clear the difference in generation time between the two. Only in its launch announcement does it say Sunburst’s better precision comes with “longer generation times,” leaving developers wondering how much longer exactly.

![](https://cdn.thenewstack.io/media/2026/09/ad835913-openai-image-1-1024x576.webp)

Source: [OpenAI](https://openai.com/index/introducing-chatgpt-images-2-5/)

## In general, Images 2.5 gets better at changing one thing without breaking everything else

With ChatGPT Images 2.5, OpenAI promises better image quality, editing, and speed.

Specifically, teams building with the API, teams can look forward to more reliable reference-led workflows thanks to greater image fidelity that keeps each variation more closely tied to the original source.

Editing also gets an upgrade with a new precision ability that lets developers make changes to just one piece of a picture, like a product, background, or piece of copy, while preserving the surrounding scene. ChatGPT can now also follow editing instructions more closely, even across multiple rounds of edits. In production workflows, where developers often need precise revisions, this can save teams from rebuilding an entire asset for just a few tweaks.

With promised intelligence and style improvements, ChatGPT can hopefully get more images right on the first try, before additional edits are even needed. OpenAI also says its new image model is “better at understanding complex visual instructions and translating them into coherent results.”

Easier editing, higher image quality, and faster image generation with Flare will likely smooth image-heavy workflows. But developers will have to experiment with both models to see whether Sunburst’s added precision is worth the extra time and, potentially, the cost.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)