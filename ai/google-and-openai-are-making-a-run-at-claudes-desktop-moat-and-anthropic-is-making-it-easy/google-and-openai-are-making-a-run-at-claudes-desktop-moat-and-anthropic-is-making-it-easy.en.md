*I’m Matt Burns, Chief Content Officer at Insight Media Group. Each week, I round up the most important AI developments, explaining what they mean for people and organizations putting this technology to work. The thesis is simple: workers who learn to use AI will define the next era of their industries, and this newsletter is here to help you be one of them.*

---

For two years, Anthropic owned the desktop AI surface. Claude has became the product power users keep open all day. This week, Google and OpenAI both shipped serious desktop alternatives — a native Mac app from Google, a consolidated superapp from OpenAI — and Anthropic is seemingly making it easier for power users to consider alternatives.

Consider Anthropic’s stumbles this week: the new Opus 4.7 model is drawing mixed early reviews, a Claude Code redesign that multiplied token consumption against existing quotas, another round of outages, and a surprise identity verification scheme for some users. At this rate, Google and OpenAI just need to keep pace and let Anthropic continue to underwhelm users.

## Google gets serious about the desktop

On Tuesday, Sundar Pichai [announced Gemini for Mac](https://blog.google/innovation-and-ai/products/gemini-app/gemini-app-now-on-mac-os/), a native Swift app built by a small team in under 100 days with Google’s Antigravity coding agent. Option + Space from anywhere, screen sharing, local file access. It works the way Claude Desktop and ChatGPT’s Mac app work. It’s a 1.0 and it doesn’t do much the web version can’t yet. But Pichai mentioned in his [launch post](https://x.com/sundarpichai/status/2044452464724967550) that the team built “100+ features in less than 100 days.” That’s the detail I keep coming back to. Google is finally shipping consumer AI at the pace Anthropic and OpenAI have been setting. For three years, Google’s problem wasn’t the model; it was that the model sat behind a web interface while everyone else shipped powerful desktop apps. That’s starting to change.

The same week, Google rolled out [Skills in Chrome](https://thenewstack.io/gemini-chrome-saved-prompts/) — reusable one-click Gemini prompts that run across selected tabs — and brought [AI Mode to the Chrome address bar](https://blog.google/products-and-platforms/products/search/ai-mode-chrome/), putting its most powerful AI search directly in the URL bar. Chrome is quietly becoming an AI product, not just a browser with AI attached. Google also [connected Gemini’s Personal Intelligence to Google Photos](https://9to5google.com/2026/04/16/gemini-photos-personal-intelligence), letting the AI generate personalized images using your actual photo library without manual uploads, rolling out to paid subscribers in the US first.

Stack all of that on top of Gmail, Docs, Sheets, Drive, and Meet — where Gemini is already included across Workspace Business Standard and above — and Google is making a bundled-AI argument that gets harder to ignore for the millions of organizations already paying for Workspace. Anthropic doesn’t have a browser. Anthropic doesn’t have an email client. Google has both, plus a Mac app now. That’s the moat Anthropic was quietly eroding by owning the best desktop experience. Google just started filling it back in.

*The Information* also reported that Google and the Pentagon are [discussing a classified AI deal](https://www.theinformation.com/articles/google-pentagon-discuss-classified-ai-deal-company-rebuilds-military-ties), rebuilding military ties the company walked away from during Project Maven in 2018. Google already holds a government-wide Gemini deal with GSA, so this isn’t a cold start.

## OpenAI is consolidating for the same fight

Google isn’t the only one showing up. OpenAI’s superapp started [taking shape this month](https://thenewstack.io/openais-superapp-takes-shape/), merging ChatGPT, Codex, and the Atlas browser into a single desktop application. Application CEO Fidji Simo said in an internal memo that OpenAI had been “dispersing efforts across too many applications and platforms” and that “this fragmentation has been hindering our progress.” So they stopped fragmenting.

I’ve been using it. Codex agents run asynchronously in isolated git worktrees — multiple agents on the same repo, no merge conflicts — and you can review diffs and open outputs directly in VS Code. ChatGPT 5.5 launched alongside it on April 6 with improved memory management, so long sessions don’t feel like you’re restarting the conversation every few turns. The practical difference is that you stop switching between apps. Chat, code, and browse live in one window, and the context carries across them. That’s what keeps it open on your desktop all day.

The superapp exists partly because OpenAI’s individual products were falling behind — Codex was losing developers to Claude Code, Atlas hadn’t broken through against Chrome. Simo’s memo essentially admits this. But even OpenAI, with the largest consumer AI user base in the market, decided the desktop app was the product that needed fixing first. That says something about where AI companies are focusing especially when considering Google’s similar moves.

## Anthropic shipped its best model and its roughest week

Let’s start with the new model. [Opus 4.7 looks strong on paper](https://thenewstack.io/claude-opus-47-launch/): 13% better on a 93-task coding benchmark, 21% fewer document reasoning errors, 3x more production task resolution on engineering evaluations, same $5/$25 per million token pricing. But the early user reaction has been mixed. On [Hacker News](https://news.ycombinator.com/item?id=47793411) and across Reddit’s r/ClaudeAI, users and developers are saying Opus 4.7’s adaptive thinking — now the only supported reasoning mode — frequently chooses not to think when it should, forcing them to manually set `/effort xhigh` just to restore baseline performance. Some report that the API parameter is [returning errors](https://medium.com/vibe-coding/opus-4-7-is-the-worst-release-anthropic-has-ever-shipped-12772c21ca1e), that token costs have increased meaningfully under the new tokenizer, and that thinking tokens are hidden by default. Others report the model performs worse with longer context, not better. Though Anthropic is quick to point out that the benchmarks went up, the early experience, for a vocal group of users, seems to be going sideways. Anthropic may sort this out (model launches often stabilize after the first week) but the timing is difficult when Google and OpenAI are finally matching Anthropic’s pace.

And then there’s the product. Claude.ai, the API, and Claude Code went down Wednesday morning — 40-minute major outage, 73-minute partial outage — the latest in a pattern that’s hit Claude several times since early 2026. Opus 4.6 went down again the next night. Anthropic [shipped a redesigned Claude Code desktop](https://thenewstack.io/claude-code-desktop-redesign/) around parallel sessions, and early user reports were rough with multiple users reported burning through 5-hour quotas in minutes, likely because four parallel sessions at 100K tokens each adds up fast. Anthropic recently [shut off OpenClaw](https://techcrunch.com/2026/04/10/anthropic-temporarily-banned-openclaws-creator-from-accessing-claude) and other third-party harnesses from subscription access, revoking OAuth. And *The New Stack* [covered Anthropic’s new identity verification requirement,](https://thenewstack.io/anthropic-claude-identity-verification) which routes some users through Persona — the KYC vendor used by financial services — to submit a government ID and a live selfie before accessing certain capabilities. Anthropic says the trigger is narrow and the data sits with Persona, not Anthropic. *Decrypt* put it plainly [here](https://decrypt.co/364509/claude-anthropic-government-id-kyc-privacy): “You Switched to Claude Over Surveillance Fears. Now It Wants Your Passport.”

Our site also covered [Claude Code Routines](https://thenewstack.io/claude-code-can-now-do-your-job-overnight/), the new persistent agents that run on Anthropic’s cloud overnight, triggered by schedules, API calls, or GitHub webhooks. Routines are a real product, and the kind of capability that keeps developers around.

It’s hard not to read all of this as connected to a compute constraint. *Fortune* [reported that Anthropic quietly reduced](https://fortune.com/2026/04/14/anthropic-claude-performance-decline-user-complaints-backlash-lack-of-transparency-accusations-compute-crunch/) Claude’s default effort level to economize on tokens, and that OpenAI’s revenue chief called Anthropic’s limited data-center deals a “strategic misstep.” Whether or not that framing is fair, the pattern is visible: reduced effort levels, tighter quotas during peak hours, third-party access cut off, KYC friction added, and a model release where several of the complaints point back to cost-saving tradeoffs in how the model reasons.

I’m not switching off Claude yet. For me, it remains the best user experience for a long list of tasks I perform daily, and I’m sure I’m not alone. But this was the week even the model release — historically the thing Anthropic always gets right — came with disappointment and had me considering the new alternatives.

---

## Previous Editions



[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/976a6c81-1706717710759.jpeg)

Matt Burns is Director of Editorial at Insight Media Group, where he oversees The New Stack, Roadmap.sh, and Towards Data Science — three platforms that collectively help millions of developers figure out what to learn next. Previously, he spent 16...

Read more from Matthew Burns](https://thenewstack.io/author/matthew-burns/)