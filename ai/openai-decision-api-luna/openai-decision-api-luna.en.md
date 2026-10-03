**With the sudden rise of [TypeSafe’s Jev](https://thenewstack.io/typesafe-jev-system-one/)**, decision models have become incredibly popular, so it’s not surprising that OpenAI is also announcing its take on this model type at its annual DevDay conference on Tuesday.

The company’s new Decisions API is based on the company’s Luna model — the smallest and most affordable model in its current lineup.

## Limited preview

The Decisions API is likely a reaction to TypeSafe and Jev, and OpenAI probably rushed the announcement ahead of its DevDay, so for now, this is all OpenAI is sharing about the Decisions API.

An OpenAI spokesperson tells *The New Stack* that the company plans to share more “at broad rollout.”

For now, the new API is available in limited preview, and the broad release is planned for the coming days.

## Predefined answers, real confidence scores

The core idea behind these decision models is that they are explicitly not chat models; instead, they return a set of predefined answers with confidence scores. Regular LLMs are not always very good at this. Their confidence scores, after all, are often a rough guess — and they burn quite a few tokens to get there.

This makes this kind of model ideal for classifying content, routing requests, or choosing an agent’s next action from a limited set of choices.

Decision models, however, can provide more realistic confidence scores, and they tend to return them extremely fast. OpenAI says its model returns results in 150 milliseconds, compared to GPT-6 Luna, which would take 1.6 seconds.

All the developer has to do is provide the questions, answers, and context.

---

###### OpenAI DevDay 2026 coverage:

---

## Prompts vs. small classifiers

Today, most teams handle this today with a regular chat model and a carefully worded prompt, asking it to pick from a list and, if they’re lucky, reading the token probabilities to get something that resembles a confidence score.

The alternative is to train a small classifier. That is fast and cheap but needs labeled data and a retraining run every time the label set changes.

A decision model basically sits between those two options. It takes new labels in the prompt but returns a score a developer can work with.

This isn’t a completely new concept for OpenAI. Its Moderation API has long returned per-category scores instead of prose, too, though in this API, the categories are pre-set by OpenAI, not the developer.

What’s still unclear is what the Decision API costs per call, how many candidate answers a single request can handle, and whether developers can tune it on their own data. Those details will decide whether this becomes a standard building block in agent frameworks or stays a niche tool next to the chat models.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)