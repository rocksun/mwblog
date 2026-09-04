**Vercel ran more than 200 agent runs** to build `design.md`, a new public prompt file designed to help agents create web pages that look and feel like Vercel, even when they don’t have access to the company’s internal codebase.

In a [post](https://vercel.com/blog/how-our-agents-build-on-brand-pages-with-design-md) published Monday, Vercel shared the behind-the-scenes process of how it built and evaluated the file to determine whether the corrections it encoded to prevent failures worked — the answer is yes, but not perfectly.

The release offers a broader lesson for developers: Encoding human judgment into reusable agent guidance can help reduce recurring failures, but it’s no silver bullet.

In three desktop scenarios, when Codex with GPT-5.5 generated the page once with `design.md` loaded and once without, Vercel’s deterministic checks counted 39 instances of known failure modes with `design.md`, compared to 91 without it — a 57% reduction in this six-page test.

> Encoding human judgment into reusable agent guidance can help reduce recurring failures, but it’s not a silver bullet.

While Vercel acknowledged that every one of the six pages (an admittedly small sample size) had a failure large enough to prevent shipping, the experiment suggests that failures explicitly named and encoded are less likely to recur.

## The problem with keeping design knowledge in the codebase

In June, Vercel shared the thinking behind product design, a skill that teaches coding agents working in its codebase to design pages with the brand’s look and feel. Vercel says it’s proven valuable — but only for agents working inside the codebase. Once it’s time to get tools that live elsewhere to produce the same on-brand content, they can’t reach the same design context.

So the company decided to build a public file that any agent or tool, even outside Vercel’s development environment, can load to access the relevant design knowledge and produce on-brand pages.

First, Vercel tried to port product design to a public prompt simply, but that proved a bust. Because the prompt included subjective design language, each model interpreted it differently. Plus, the prompt only tells half the story; important information about design and implementation lives in the codebase, which works for product design, not for a public prompt.

Making that design knowledge accessible, then, Vercel decided, would take a new file, built from the ground up.

## How Vercel built and tested design.md

In building that file, Vercel tested every iteration against a repeatable set of seven evaluation prompts, designed to expose how changes in guidance ultimately affected the generated output. With every round, these prompts allowed Vercel to measure two things: 1) what changes the file caused; 2) how different agents interpreted it.

As `design.md` cycled through different tests and iterations, ultimately covering more than 200 agent runs, Vercel settled on a three-part system to make the guidance both reusable and testable.

First, the prompt file itself gives agents guidance on how to make design decisions, including writing copy, composing hierarchy, typography, and color, as well as publishing. Importantly, it also spells out what design patterns are not allowed so agents can avoid them.

A public stylesheet, meanwhile, defines reusable implementation details so agents don’t go rogue on things like spacing and layout. Finally, an evaluation loop turns human feedback into updated guidance and deterministic checks for mechanical failures.

Vercel then built a local app to serve as an eval harness for reviewing the generated pages from each round and for storing the prompt, inputs, model configuration, file version, screenshots, and reviewer feedback. Corrections were routed to each layer accordingly: judgment changes were encoded as prose directly in the file; the stylesheet captured reusable mechanics; mechanical failures became deterministic checks in code.

With each round of feedback, Vercel reviewed the results, encoded the accepted corrections, and reran the same eval prompts to ensure no changes inadvertently broke anything else.

## How ongoing feedback becomes updates

To keep the shipped file up to date, Vercel then built design-agent. With just a mention in a Slack thread, the agent loads the current `design.md`, builds the requested website page using the published stylesheet, and then posts a full screenshot and URL back in Slack, giving Vercel a compact record that connects the request, output, and subsequent feedback.

At the end of the week, all that feedback is consolidated with comments from GitHub reviews and Figma, and each repeated complaint automatically becomes a proposed change for human review and approval.

> Better guidance still doesn’t guarantee agent reliability.

Over time, Vercel says it tracks how often each complaint recurs. Ideally, once a fix is implemented, that count should start to decline; if it doesn’t, that’s a sign the fix needs refinement.

## What developers can take from design.md

Vercel’s experiment offers an example of how teams can turn human judgment into reusable agent guidance — more evidence that [agent instructions should be managed like software with a development lifecycle](https://thenewstack.io/agent-context-development-lifecycle).

But it’s important to bear in mind that better guidance still doesn’t guarantee agent reliability. Vercel’s tests show that even after more than 200 runs refining the system, not one of the six tested pages was ready to ship without correction. Still, the drop in recurring failures suggests that naming and encoding failures can make a difference.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)