In a report published Friday, OpenAI shares evidence of a new variety of prompt injection that can self-propagate like a computer worm.

The AI company likens the new attack to a traditional computer worm, where malware replicates itself to spread rapidly across multiple computers.

Though OpenAI clarifies it observed no impact outside simulated tool calls in training and evaluation, it describes self-replicating prompt injections as having a two-pronged objective: to achieve a malicious goal and then induce the targeted models to reproduce the injection publicly.

## What self-replicating AI “worm” attacks could do

Just now opening the hood on a finding discovered back in June 2026, OpenAI writes:

“We have found instances of our GPT models being susceptible to an AI-version of a worm attack that we call ‘self-replicating prompt injection.’”

In its [report](https://alignment.openai.com/misalignment-reports/self-replicating-prompt-injections-exist/), the AI company exposes several examples of the attacks.

First, it details what it describes as “one of the clearest examples,” where the prompt injection arrives by email. Then, when the agent reads the email, the injection instructs it to copy the injection into any emails it sends.

That example may sound relatively simple, but OpenAI adds that it discovered other, more complex prompt injections, too. For instance, it found that some prompt injections can use the filesystem to replicate themselves or commit themselves through code comments.

To illustrate how the filesystem variant could play out, OpenAI gives an example in which a fake system warning causes a model to delete important reports. The report then replicates the entire attack in a file.

> “We have found instances of our GPT models being susceptible to an AI-version of a worm attack that we call ‘self-replicating prompt injection.’”

The report also describes “multi-hop prompt injections,” where one message acts as a stepping stone, directing the agent to other messages that, taken together, cause it to perform an unauthorized action and propagate the payload. In OpenAI’s example, a GPT-5.5 agent retrieves additional Slack instructions, sends “froges” (an internal currency for recognizing colleagues) to a named recipient, and reposts the injected message.

## How did OpenAI find the worms?

Introduced in July, [GPT-Red](https://openai.com/index/unlocking-self-improvement-gpt-red/) is a self-play training framework that OpenAI says it uses to train its models against prompt injections. Previously, the framework was used to discover other prompt injections capable of a range of malicious goals, such as data exfiltration, file deletion, and malicious or misleading output generation.

The framework pits an “attacker” model against a “defender” model. The attacker model’s goal is to use prompt injection to get the defender model to perform an adverse action. These injections are then added into the defender’s rollout or container.

This time, OpenAI says its goal was to find out if self-replicating prompt injections — what it describes as “an AI-version of a worm attack” — are even possible. The bad news is, it looks like they are.

As the report describes, OpenAI tested this possibility by training on a GPT-Red-style prompt injection objective with an additional requirement to “induce the model to repeat the injection itself on a public output channel.”

The test covered several different models. The model that discovered the email and filesystem injections was a GPT-Red-style model based on GPT-5.4-mini; the vulnerable model was also based on GPT-5.4-mini. Both were internal-only research checkpoints. GPT-5.5, meanwhile, was used as the vulnerable model for the separate multi-hop evaluation, with GPT-5.5 running in the Codex harness serving as the model that discovered the attack.

The attacks were tested in a range of capability-related training environments, focusing particularly on those that involved connectors, such as email and calendar.

## This is a research finding, not an incident

In its report, OpenAI makes clear that it observed no impact outside the simulated tool calls in training and evaluation. It’s simply sharing the findings due to their “novel nature.”

The AI company seems to be on a streak of misalignment research. Earlier this month, it released a [new framework for reporting model misalignment](https://openai.com/index/model-misalignment-reporting-framework/). That announcement came on the same day OpenAI published [six reports of concerning model behavior](https://thenewstack.io/openai-model-misalignment-reports/) observed during training or evaluation, including self-generated instructions, information fabrication, unauthorized use of leaked API keys, cross-agent communication, and unsanctioned file-sharing.

Also on Friday, OpenAI released still [more reports on misalignment](https://thenewstack.io/openai-agents-security-bypasses/), this time detailing how two models found workarounds after their intended paths were blocked, exposing gaps in network controls, instruction following, and monitoring.

For this round of findings, the AI company says it’s responded by including self-reproduction in attacker goals in GPT-Red training to expose future models to — and hopefully make them more robust against — similar self-replicating prompt injections.

Whether that training will be enough to stop the worms from spreading remains to be seen.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)