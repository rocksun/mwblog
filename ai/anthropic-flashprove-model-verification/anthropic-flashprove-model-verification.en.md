Developers using AI APIs have little way of knowing whether the model answering their requests is actually the one they’re paying for. A provider could route requests to a cheaper model, or an attacker could interfere with responses, without customers having an obvious way to detect the switch.

Now, Anthropic wants to change that. The company’s Frontier Red Team has released [FlashProve](https://www.anthropic.com/research/provable-inference), an open-source cryptographic system designed to verify which AI model produced a response without exposing its underlying weights.

[Announced Tuesday](https://x.com/AnthropicAI/status/2117710942826123294), the research could eventually help developers verify third-party AI services and detect compromised inference systems. But FlashProve remains a research prototype, and the cost of generating proofs makes it impractical for routine API traffic.

> But FlashProve remains a research prototype, and the cost of generating proofs makes it impractical for routine API traffic.

## How FlashProve proves the model

FlashProve uses [zkSNARKs](https://www.anthropic.com/research/provable-inference) to verify that a response came from a specific set of model weights without revealing those weights. The commitment still has to come from a trusted source, or the proof means little.

Anthropic has released [FlashProve on GitHub](https://github.com/anthropics/FlashProve), where developers can download the code and test the system themselves. It’s still a research prototype, however, and isn’t available as a feature of the Claude API.

## The cost of every proof

Anthropic tested FlashProve on Meta’s Llama 4 Maverick, a 400-billion-parameter mixture-of-experts model, rather than Claude.

According to Anthropic’s [benchmarks](https://www.anthropic.com/research/provable-inference), FlashProve processed roughly 110 prompt tokens per second while generating proofs on a single Nvidia H100 GPU. Each proof was about 18.78 MB and took around 21 seconds to verify on a single CPU thread. Generating the proof is far more expensive than checking it.

Compared with standard inference using vLLM, FlashProve needed 70 to 95 times more GPU time to generate proofs. It also generates them in batches after requests are completed, rather than verifying tokens as they’re delivered.

> FlashProve cuts proof sizes to roughly 19 MB and verification times to seconds

FlashProve cuts proof sizes to roughly 19 MB and verification times to seconds, although generating those proofs remains expensive and less practical for applications that need immediate verification of every response.

For developers already [watching every token of their inference spend](https://thenewstack.io/minimax-flash-agent-costs/), adding that much GPU overhead would be difficult to justify for routine API traffic.

Still, Anthropic says FlashProve is substantially faster than previous open-source systems. An earlier system called [VerInf](https://github.com/JamesPetrie/VerInf) needed 14.3 hours to generate a proof covering 1,000 tokens. The resulting proof was 93.6 GB and took almost a day to verify.

## Claude built it, humans verified

Anthropic credits Claude with much of FlashProve’s development, including optimizations that made its cryptographic proofs substantially faster. But the researchers still had to verify that those improvements hadn’t compromised the protocol’s security guarantees.

The team used [Lean](https://www.anthropic.com/research/provable-inference) to formally verify the protocol’s mathematical properties, including that it accepts valid proofs, rejects forged proofs with overwhelming probability, and doesn’t reveal the model’s weights beyond what the responses disclose.

FlashProve includes two verifiers: a faster C++ implementation and a Lean version backed by formal proofs. The C++ verifier passed Anthropic’s comparison tests, but it hasn’t been formally verified. Neither has the GPU prover.

Anthropic says the C++ verifier and GPU prover have been tested against the formally defined protocol, but neither has the same mathematical guarantees as the Lean implementation.

## Why FlashProve isn’t production-ready

FlashProve is still limited to 1,024 tokens of context. It also uses integer-based inference and greedy decoding, while production models typically rely on floating-point calculations and sampling.

> There’s no indication of when, or whether, FlashProve will make its way into the Claude API.

There’s no indication of when, or whether, FlashProve will make its way into the Claude API. Anthropic describes the [GitHub release](https://github.com/anthropics/FlashProve) as a research artifact that isn’t being maintained or accepting contributions.

[Cyber Security Expert
Step by step guide to becoming a Cyber Security Expert in 2026

Fundamental IT Skills
CTFs (Capture the Flag)
Operating Systems
Networking Knowledge
Certifications
Security Skills and Knowledge
Cloud Skills and Knowledge
Programming Skills](https://roadmap.sh/cyber-security?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=anthropic-flashprove-model-verification)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)