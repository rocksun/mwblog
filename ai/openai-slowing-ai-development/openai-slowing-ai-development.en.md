**AI companies have spent the last few years competing** to build the best models, faster than the other, with each new release raising the bar on intelligence. Now OpenAI is considering whether there are times when it makes sense to slow down.

This week, AI researcher Jacob Coxon resigned from Anthropic [with a stark warning about where the race is heading](https://thenewstack.io/anthropic-alignment-superintelligence-warnings/). Coxon, who also worked at OpenAI and helped train [GPT-4o](https://thenewstack.io/reviewing-code-with-gpt-4o-openais-new-omni-llm/), accused both companies of racing too fast toward significantly more powerful AI without knowing exactly how to keep it safely under control.

OpenAI CEO Sam Altman is beginning to talk about doing something about it. He told employees this week that the company is open to slowing development of its most advanced AI systems, potentially in coordination with other frontier labs, [reports Bloomberg](https://www.bloomberg.com/news/articles/2026-09-11/openai-is-open-to-slowing-cutting-edge-ai-ceo-sam-altman-tells-staff).

> OpenAI can choose to ease off, but it won’t matter if companies like Anthropic, Google DeepMind, and others keep going at the current speed.

That idea has an obvious problem: OpenAI can choose to ease off, but it won’t matter if companies like Anthropic, Google DeepMind, and others keep going at the current speed.

Developers have gotten used to new models dropping every few months, with each one improving upon what the last model couldn’t do. But if safety worries start holding up releases or limiting access, teams may no longer be able to count on the next model’s timely arrival. [OpenAI has already shown what that can look like](https://openai.com/index/path-to-astra/).

## Safety pauses have precedent

OpenAI put the brakes on twice this summer, for very different reasons.

In August, the company halted its largest frontier reinforcement learning run after internal evaluations found that [GPT-6 Astra posed serious cybersecurity concerns](https://thenewstack.io/openai-gpt6-astra-benchmarks/). Earlier, much of its model development stopped for two weeks after OpenAI’s AI agents broke containment and [compromised Hugging Face](https://thenewstack.io/openai-huggingface-sandbox-breach/).

OpenAI eventually resumed work, but only after restricting access and adding more safeguards. Astra’s release had its own problems. [The public rollout took days longer than planned](https://thenewstack.io/gpt6-astra-developer-access-delayed/), prompting Altman to apologize for what he called a “messy rollout.”

## Capabilities trigger the restrictions

OpenAI uses its [Preparedness Framework](https://openai.com/index/path-to-astra/) to assess what a model can do in areas including cybersecurity and biological and chemical threats. Astra was classified as Critical for cybersecurity, the highest level under the framework, the first commercial model for OpenAI to be rated as such.

At that level, the company says a model can find and exploit zero-day vulnerabilities in hardened systems without step-by-step human guidance. OpenAI limited access accordingly, and offensive cyber capabilities went into Daybreak, a controlled-access program, while enterprise customers had to opt into Astra rather than getting it automatically.

The restrictions also showed up in the API. Some early users saw [responses cut off mid-task,](https://thenewstack.io/astra-api-safety-stops/) making OpenAI’s safety system stopping the model look like a timeout. For developers, that’s where the effects become concrete.

## Coordination remains the hard part

With so many AI companies pushing the same capabilities, it only makes sense for everyone to slow down together. Otherwise, OpenAI pauses while everyone else keeps going, giving up ground without necessarily reducing the broader risk.

> With so many AI companies pushing the same capabilities, it only makes sense if everyone slows down together.

OpenAI’s Chief Scientist, [Jakub Pachocki,](https://www.linkedin.com/in/jakub-pachocki/) made that case in his September 6 essay [“An Alien Mind.”](https://openai.com/index/path-to-astra/) No lab, he argued, has solved alignment and monitoring well enough to continue scaling at maximum speed indefinitely. He wants voluntary slowdowns to become normal until the industry has shared safety bars, backed by third-party auditors, governments, or international bodies.

In July, more than 1,000 AI workers signed [“Pacing the Frontier,”](https://explainx.ai/blog/pacing-the-frontier-ai-employees-letter-july-2026) an open letter calling on the U.S. government to address the pace of frontier AI development. Pachocki, Anthropic CEO Dario Amodei and Meta chief scientist Shengjia Zhao signed individually.

[Bloomberg reports](https://www.bloomberg.com/news/articles/2026-09-11/openai-is-open-to-slowing-cutting-edge-ai-ceo-sam-altman-tells-staff) that OpenAI has been looking at how companies could coordinate without running into antitrust law. Even if that question is resolved, the labs still have to agree on what they’re measuring. They use different evaluations and safety frameworks, so a result serious enough to stop work at OpenAI may not produce the same result somewhere else.

## Developers absorb the cost

If model launches become harder to predict, engineering teams will have to solve more problems themselves. That could mean reworking agent architecture, adding deterministic guardrails around tasks models still get wrong, or squeezing more out of what’s already deployed.

> If model launches become harder to predict, engineering teams will have to solve more problems themselves.

That adds work at a time when AI agents aren’t automatically saving teams as much time as expected. [OpenAI’s own research suggests agents are already creating new bottlenecks for the humans working with them](https://thenewstack.io/openai-agent-research-bottleneck/). Slower model development could leave those teams working with the same limitations for longer.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)