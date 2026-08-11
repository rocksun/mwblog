**OpenAI is reducing work on [Astra](https://thenewstack.io/openai-astra-math-cost/)** after internal testing indicated the upcoming model may have reached a cybersecurity limit that no previous OpenAI model has ever hit. Although no official release date has been set, the speed bump could push back its ensuing release.

The company said it “cannot rule out critical cyber capabilities” in Astra, [*Axios* first reported](https://www.axios.com/2026/08/07/openai-astra-model-delay-cybersecurity-risks). It has paused internal activities that do not meet strengthened security requirements while it expands testing and tightens controls around the model.

## What “critical” actually means

Under OpenAI’s [Preparedness Framework](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf), a model reaches the Critical cybersecurity threshold when it can identify and develop functional zero-day activities of all severity levels in many hardened, real-world critical systems without human involvement.

A model can also qualify by developing and performing a novel end-to-end attack against a hardened target after receiving only a high-level goal. Preliminary results were strong enough that the company could not confidently place it below that level.

For developers, the worry is that the skills making [coding agents](https://thenewstack.io/microsoft-copilot-token-budgets/) more useful can be turned against the software they were built to work on.

> the skills making coding agents more useful can be turned against the software they were built to work on.

## Testing in tighter isolation

Previous models, including [GPT-5.6 Sol](https://thenewstack.io/sol-usage-limits-reset/), were measured at the High cybersecurity level. OpenAI now treats Astra differently by testing it in isolated environments with tighter limits on the networks and tools it can access, because a Critical model requires safeguards during development.

OpenAI is also strengthening protection around the model itself and adding supervision that can stop it when it detects unsafe behavior. Those measures emphasize the immediate engineering problem: As agents take on more work with less human oversight, the environment around them becomes part of the security perimeter.

## Agents breaching real organizations

The company said Astra did not participate in the [recent Hugging Face security incident](https://openai.com/index/hugging-face-model-evaluation-security-incident/), but that incident still proved what can happen when an agent’s capabilities exceed the controls surrounding its test.

[Anthropic disclosed](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals) that its Claude models had breached three separate organizations during similar cybersecurity evaluations. The UK’s AI Security Institute then reported 19 unsanctioned real-world actions by Claude Mythos 5 and GPT-5.6 Sol during permissive cyber evaluations, including efforts to create fake identities and insert malicious code into an open-source project.

## Access may require vetting

OpenAI has not said whether Astra will be offered through ChatGPT, Codex or its API, but the company’s existing approach suggests that every user may not get the same level of access. Through its [Trusted Access for Cyber](https://openai.com/index/trusted-access-for-cyber/) program, it gives approved security professionals tools that are not available to everyone. Astra could follow a similar path, with its most powerful capabilities limited to researchers and organizations willing to accept closer oversight.

> Developers may have to prove who they are and explain how they plan to use the model before gaining access to its most powerful capabilities.

Developers may have to prove who they are and explain how they plan to use the model before gaining access to its most powerful capabilities. Even then, OpenAI could place tighter boundaries around what Astra is allowed to do.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)