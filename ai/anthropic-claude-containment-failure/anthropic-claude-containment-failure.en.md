This week, just days after OpenAI [announced](https://thenewstack.io/nanoclaw-echo-agent-runtime/#:~:text=One%20of%20the,unprecedented%20cyber%20incident.%E2%80%9D) that two of its advanced AI models had interacted with real-world systems during cybersecurity tests, Anthropic reported a similar containment failure.

In a post on X, Anthropic said it found three separate cases where Claude models accessed the internet from third-party testing environments and affected real organizations. This came after reviewing over 141,000 evaluation runs, a process started because of OpenAI’s earlier announcement. As a result, Anthropic paused its [cybersecurity testing](https://thenewstack.io/gpt-red-prompt-injection-testing/) and tightened its evaluation process.

## When sandboxes leak

The three incidents at Anthropic happened during capture-the-flag (CTF) tests meant to measure offensive cybersecurity skills. The models were told they were working in isolated sandboxes with no internet access. However, a networking mistake caused by a misunderstanding between Anthropic and its third-party partner Irregular left the test machines connected to the public internet. Also, since these tests were meant to measure the models’ raw abilities, they ran without the usual external protections Anthropic uses in production, though the models still had their built-in safety training.

As Anthropic explained in its [blog](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals), “Operating under the false belief that all accessible entities were intended to be in-scope for the exercise, Claude compromised the impacted organizations’ infrastructure using basic techniques…” Thinking that every system it found was part of the test, Claude used common penetration testing methods like weak password attacks and SQL injection to follow its instructions.

The three events also show how different versions of Claude responded when the line between a simulated environment and the real internet disappeared.

> “Operating under the false belief that all accessible entities were intended to be in-scope for the exercise, Claude compromised the impacted organizations’ infrastructure using basic techniques…”

## Three models, three responses

The most severe involved [Claude Opus 4.7](https://thenewstack.io/fable-5-honeycomb-opus/). After failing to find the fictional company it had been instructed to target, the model searched the public internet, found a real business with the same name, obtained credentials, and accessed a production database containing several hundred records. Anthropic said that across all four test runs, the model eventually recognized it was interacting with real systems. Even so, it continued because it concluded the real company must have been intentionally included as part of the exercise.

> …the model eventually recognized it was interacting with real systems. Even so, it continued because it concluded the real company must have been intentionally included as part of the exercise.

Another case involved [Claude Mythos 5](https://thenewstack.io/fable-5-honeycomb-opus/), which uploaded a malicious Python package to the public Python Package Index (PyPI), believing the repository was part of the simulated environment. Before the package was automatically removed about an hour later, it had been downloaded by 15 external systems, including a cybersecurity company’s malware scanner. After the scanner executed the package, the model obtained leaked credentials and used them to access additional systems. According to Anthropic’s review, Mythos 5 acknowledged in its reasoning that its actions could affect real users, but ultimately decided the repository was probably still part of the evaluation.

The third incident involved an internal research model, which scanned roughly 9,000 internet-facing systems before compromising one organization’s application using exposed credentials and SQL injection. Unlike the other two models, however, this one eventually determined it had reached infrastructure unrelated to the evaluation and voluntarily stopped its activity, making it the only model in the review to recognize the mistake and halt the operation on its own.

Anthropic stressed that “in none of these situations did Claude exfiltrate itself or deliberately attempt to escape its test environment.” The models were just doing their assigned tasks with standard security tools inside a flawed test setup. Still, the differences in behavior with Opus 4.7 justifying its actions, Mythos 5 ignoring its doubts, and the research model stopping show how closely model alignment and strong infrastructure are connected.

## Simulation meets production

OpenAI’s models got into outside systems by using a new vulnerability to break out of their test environment. Anthropic’s models did the same because a third-party test setup was not properly isolated.

Researchers need to create environments that feel like real enterprise systems, where the model can interact with databases and developer tools the way it would in the real world. The more realistic those environments are, the better they reveal how an autonomous agent will behave once it’s given real tasks to complete.

As a result, evaluation environments have become complex software systems in their own right, meaning they require the same engineering discipline as production infrastructure, including strict network segmentation, outbound traffic controls, isolated credential management and automated cleanup processes that ensure test environments are completely torn down after every evaluation.

> “…consistent with a blameless postmortem culture, we’re approaching the fixes as if the responsibility were ours alone.”

## Evaluation as critical infrastructure

Test code generally executes within fixed boundaries, but frontier AI models are intentionally asked to explore systems, probe for weaknesses and adapt to what they discover. If an evaluation environment exposes an open network path, the model will treat it as another opportunity to accomplish its assigned task.

Anthropic noted that the additional monitoring and safety protections used with publicly deployed Claude models would likely have prevented these incidents. Those controls, however, are deliberately removed during capability testing so researchers can measure what the underlying model can actually do, making the evaluation infrastructure itself one of the most critical pieces of the AI stack — a reality Anthropic acknowledged by noting, “consistent with a blameless postmortem culture, we’re approaching the fixes as if the responsibility were ours alone.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)