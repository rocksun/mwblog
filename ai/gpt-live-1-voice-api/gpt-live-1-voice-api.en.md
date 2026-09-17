Building an AI voice agent has always been clunkier than it seems. Most voice agents are really a chain of systems passing a conversation back and forth. What you say gets turned into text so a model can figure out how to respond, then that answer has to be turned back into speech; it’s easy to see why things can get robotic fast. Now, OpenAI is trying to collapse that stack.

On Wednesday, the company launched [GPT-Live-1 in its API](https://openai.com/index/introducing-gpt-live-1-in-the-api/), bringing the native, full-duplex voice architecture behind ChatGPT voice mode to outside developers for the first time. Instead of making developers manage the entire chain, it wants one model to handle the conversation while the heavier thinking happens elsewhere.

> Instead of making developers manage the entire chain, it wants one model to handle the conversation while the heavier thinking happens elsewhere.

## Full-duplex voice delegation

GPT-Live-1 operates as the conversational frontline. Because it’s natively full-duplex, it can keep up with a conversation as it happens, including when someone cuts in mid-sentence, without developers coordinating separate systems. But the voice model doesn’t have to do all the work alone.

When a request needs more time or more processing, GPT-Live-1 can hand it off to another model in the background. That could be [GPT-6 Astra](https://thenewstack.io/openai-gpt6-astra-benchmarks/), a smaller model like Luna, or something from another provider entirely.

Waiting on a bigger model can make a voice agent painfully awkward. Ask a difficult question, and you can end up sitting in silence while the model works through it. GPT-Live-1 can keep the conversation going instead — filling pauses, acknowledging the speaker — then work the answer in once the backend is finished.

OpenAI says GPT-Live-1 performs 30 percentage points better than GPT-Realtime-2.1 on Full Duplex Bench. Paired with GPT-6 Astra at medium reasoning, it also takes the top spot on the [𝜏³-benchmark](https://sierra.ai/resources/research/tau-3-bench).

## What the handoff looks like

OpenAI exposes delegation through an event-driven interface. The voice session generates a `delegation_id,` sends context to whatever backend system is handling the heavier work, and gets the result back through an event called `session.commentary.append`. The voice model folds that result into the ongoing conversation rather than reading a block of text aloud. Developers can still see what the model hears and says and control when it takes a turn — they just don’t have to build the entire conversation out of separate systems. OpenAI’s [API docs](https://developers.openai.com/api/docs/live) walk through the full pattern, including a working example with the Codex SDK.

## Early customers cut code

One early customer deleted 23,000 lines of code after switching to GPT-Live-1.

[Tony Stoyanov](https://www.linkedin.com/in/stoyan-tony-stoyanov-07690a53/), co-founder and CTO of EliseAI, a healthcare company testing the API, said the move shrank his codebase by 80%. His team could spend that time on the patient experience instead — making it easier to book appointments and navigate care.

The language-learning company [Speak](https://www.speak.com/) saw the difference in the conversations themselves. In early tests of its Live Tutor Lessons, GPT-Live-1 was nearly 80% less likely to interrupt someone who had simply paused to think. For someone learning a new language, those extra few seconds can be the difference between getting the answer out and having the AI cut them off.

Yelp is already using GPT-Live-1 in Yelp Host and Hatch. CTO [Alex Levy](https://www.linkedin.com/in/ahlevy/) said the company is seeing more calls successfully handled by AI, and callers are speaking in fuller, more natural sentences — a sign, Levy said, that the experience on the other end of the phone feels different. A demo released with the announcement shows exactly why, when a restaurant reservation kept moving even with background noise, and people spoke over one another.

## Pricing the voice layer

GPT-Live-1 costs $0.05 per minute, or about $3 an hour. Then there’s whatever developers choose to run behind it. If GPT-Live-1 hands a request to GPT-6 Astra, the developer pays for that call too. The more often an agent reaches for a reasoning model, the faster the bill climbs.

OpenAI has been [cutting API prices](https://thenewstack.io/gpt-5-6-api-price-cuts/) as competition from Anthropic, Google, and Chinese labs heats up, but frontier reasoning still isn’t free.

> The more often an agent reaches for a reasoning model, the faster the bill climbs.

The tradeoff is that developers can now be selective about where they spend that money. Something simple, like scheduling an appointment, could go to Luna. A harder question, like one that actually needs multi-step reasoning or tool calls, could go to Astra. OpenAI has already shown how [Astra’s adjustable reasoning settings let developers dial cost up or down](https://thenewstack.io/astra-reasoning-effort-cost/) per call, and GPT-Live-1 gives them a place to apply that same logic to voice.

## Platform control tradeoffs

With the older cascaded approach, teams can choose a different provider for each part of the voice stack and swap pieces out when they want. GPT-Live-1 takes over more of the conversation, which also means handing more of it to OpenAI.

The bet is that developers will give up some of that control if it means voice agents can finally keep up with the people talking to them.

> The bet is that developers will give up some of that control if it means voice agents can finally keep up with the people talking to them.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)