**Enterprise AI company Cohere** [announced](https://thenewstack.io/cohere-translation-commercial-licensing/) North Small Translate last week, a mixture-of-experts (MOE) open-weight machine translation model that works across 50 languages.

Developers can [download](https://huggingface.co/CohereLabs/North-Small-Translate-1.0) the weights for noncommercial use under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.en). Cohere offers commercially licensed deployment through [Model Vault](https://docs.cohere.com/docs/model-vault), which is a Cohere-managed inference environment. Cohere positions the model as part of its sovereign AI strategy, aimed at organizations that want greater control over where their models run and how their data is handled.

North Small Translate builds on Cohere’s multilingual and translation lineage, which includes its Tiny Aya and Command A Translate model families. The company claims North Small Translate outperforms “similarly sized open-weight models” under 1T parameters, as well as API-based translation models in various dimensions of machine translation on average.

Cohere co-founder [Nick Frosst](https://www.linkedin.com/in/nick-frosst-19b80463/) tells *The New Stack* that the model’s efficiency draws from the fact that it is [non-reasoning](https://www.zansara.dev/posts/2026-07-05-reasoning-makes-translations-worse/), i.e., it relies on learned statistical patterns without a step-by-step logic process, which means it uses fewer tokens.

## Machine translation is still broken for most of the world’s languages

“We spent nine years scaling an architecture invented to fix translation, and machine translation is still broken for most of the world’s languages,” Frosst says. “General-purpose models get you most of the way and then stop. The next phase of enterprise AI in this space is smaller, more specialized, and runs inside your own walls.”

> “…machine translation is still broken for most of the world’s languages.”

In Cohere’s reported evaluation using WMT26 benchmarks, the company states that North Small Translate leads with a WMT26 All Languages benchmark score of 83.60, compared with 81.56 for Qwen 3.5 397B A17B, 76.50 for GLM 5.2 FP8, 81.37 for DeepL NextGen, 79.46 for Gemma 4 31B (on), and 68.20 for Google Translate.

With its mixture-of-experts architecture and 218 billion total parameters, with 25 billion active. Cohere points to North Small Translate’s smaller compute & memory footprint than other models. Some model-to-model comparisons in this space aren’t fully substantiable, since not every vendor discloses parameter counts.

## With current solutions, long documents start to fall apart

“Machine translation allows documents to be translated from one language to another automatically. With current solutions, long documents start to fall apart,” Frosst says. “Google Translate scores 21.3 on our long-context test, Gemma 4 31B 19.4; we score 48.9. That’s [for example] a safety manual that reads fine on page one… and has drifted by page ten. The other risk is where the text goes. Once you push HR policies or regulated documents through a third-party API, that data has left your building, and necessarily that means your control over it is diminished.”

> “The risk [in machine translation] is where the text goes. Once you push HR policies or regulated documents through a third-party API, that data has left your building and necessarily that means your control over it is diminished.”

Explaining why the model offers “stronger translation performance” across complex enterprise translation tasks, Frosst says the model can support work spanning “a high volume” of sensitive documents.

As well as its 50 languages (32 ‘high-resource’ languages + 18 others), the Cohere team explains that the model also supports translation-workflow-focused capabilities, such as structured translations (i.e., [Markdown](https://daringfireball.net/projects/markdown/) or [JSON](https://thenewstack.io/an-introduction-to-json/) documents), instruction following (i.e., recommended tone & format), and terminology guides (i.e., providing specific vocabulary to use in the translation), all as part of the model.

“North Small Translate works with a multi-pass workflow,” explains Frosst. “The model translates, reviews its own output, finds errors, and fixes them – and this is the same loop we used in training. We ship both because standard is one pass and built for volume, while the agentic [version] spends more tokens for 84.36 against 83.60 on WMT26. That difference ends up being worth it when the document is a contract or a safety procedure, for instance, but in other cases you’d rather optimize for efficiency.”

> “The model translates, reviews its own output, finds errors and fixes them.”

## Model ‘steerability’ drives suggesting language tone and formatting

This model uses the same architecture as prior Cohere models but improves performance through post-training advances, including reinforcement learning and new datasets, specifically for machine translation tasks.

Frosst concludes that, across the translation model marketplace, generative machine translation models offer the highest quality and steerability (i.e., suggesting tone, formatting, etc.) but typically cost much more than Neural Machine Translation (NMT) models commonly used in commercial use cases.

North Small Translate was developed in partnership with [RWS](https://www.rws.com/), an AI solutions company pioneering in language technology and services. Collaboration with RWS, specifically with its [Language Weaver](https://www.rws.com/language-weaver/lp/?utm_term=language%20weaver&utm_campaign=TRAN-EMEA-FY26-PAID-gg-branded-all&utm_source=google&utm_medium=paid_search&hsa_acc=2231159122&hsa_cam=23072234561&hsa_grp=189111716551&hsa_ad=801934122649&hsa_src=g&hsa_tgt=kwd-300064526129&hsa_kw=language%20weaver&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=23072234561&gbraid=0AAAAADqF18SP0hbwSs9l0dRMDlJoNs73d&gclid=Cj0KCQjwk5nVBhDiARIsAHNGqafiPRsX7yxI16JQE_8BnAuadEfY8k_46ZWLD54CMkVif72wfMZ8sqMaAkyREALw_wcB) research and science teams along with its language experts, helped shape the model’s real-world translation performance throughout development.

As noted above, developers can access the weights free of charge for non-commercial use in three quantizations. There is also a Hugging Face [Space](https://huggingface.co/spaces) and an API for those who lack the required hardware.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)