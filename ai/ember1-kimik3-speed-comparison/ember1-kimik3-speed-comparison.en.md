**Fireworks Research launched Ember-1** on September 23 as a research preview. Built on Moonshot’s [open-weight model](https://thenewstack.io/open-weight-models-frontier-costs/), [Kimi K3](https://thenewstack.io/kimi-k3-open-weight-coding/), it claims it matches Kimi K3’s quality using roughly 40% fewer tokens. Fireworks says it “learned to cut unnecessary reasoning while keeping the thinking that matters.” Reasoning tokens bill as output, so a model that thinks less should cost less.

There’s a catch, though. On [OpenRouter](https://thenewstack.io/openrouter-us-region-routing/), Ember costs $3 per million input tokens and $15 per million output tokens. Fireworks charges the same for Kimi K3, but other providers sell Kimi for as little as $1 per million input tokens and $9 per million output tokens.

I ran both models through OpenRouter on Fireworks, so both were billed at $3 and $15, and I also calculated what Kimi would have cost at the lower price.

It doesn’t matter how much cheaper a model is if it isn’t accurate. I wanted to know whether Ember’s shorter thinking holds up. If it cuts reasoning it actually needs, accuracy should slip first on the hardest problems. So I built tests that get progressively harder and ran each one five times, the same consistency check I’ve been adding to my recent testing.

## The tests

I called both models through OpenRouter with identical prompts and their default reasoning settings. I routed both to Fireworks to keep the speed comparison fair. Each test ran five times per model, and I logged reasoning tokens separately from the rest of the output.

* **Logic puzzles** – Three puzzles of increasing size, with 4, 5, and 7 engineers and one solution each. Bigger puzzles need longer chains of reasoning, so cutting the thinking should hurt first.
* **Deploy scheduling** – Twelve services with dependencies, one deploy per team at a time, and two blackout windows. The model has to find the fastest possible rollout: 17 hours.
* **Probability** – Five questions about a retry system whose server flips between healthy and degraded, plus a circuit breaker. Every answer is an exact fraction, which I checked against a simulation of 2 million requests.

I confirmed every answer key with two independent methods before either model saw it. I’ve included the prompts at the end of this article for anyone who wants to replicate these tests on their system.

### Logic puzzles

Both models solved all three puzzles on all five runs.

Ember averaged 13,630 reasoning tokens, 3 minutes 46 seconds, and $0.27 per run. Kimi averaged 16,679 reasoning tokens, 12 minutes 26 seconds, and $0.34. That’s 18% fewer reasoning tokens for Ember. Though not included in the marketing claims, Ember was much faster than Kimi. Kimi’s slowest run took nearly 20 minutes.

### Deploy scheduling

Both models found the 17-hour schedule every time, and every schedule passed my checker.

Ember averaged 6,543 reasoning tokens, 1 minute 29 seconds, and $0.10. Kimi averaged 7,792 reasoning tokens, 4 minutes 46 seconds, and $0.13. That’s 16% fewer reasoning tokens and significantly faster speed.

### Probability

This test produced the only miss. Kimi answered all five questions correctly on every run. Ember got them all right four times. On the fifth, it made a small arithmetic slip on the first question, 0.94619 instead of 0.94629, and that error carried into two other answers.

It also saved the most. It averaged 6,242 reasoning tokens, 1 minute 47 seconds, and $0.13. Kimi averaged 9,682 reasoning tokens, 6 minutes 48 seconds, and $0.19. This was the first time Ember came close to its marketing claim of 40% fewer tokens. Once again, Ember was significantly faster.

## Results

|  |  |  |
| --- | --- | --- |
| **Test (5 runs each)** | **Ember-1** | **Kimi K3** |
| Logic puzzles | 5/5 perfect, 3:46, 13,630 reasoning / 17,766 total out, $0.27 | 5/5 perfect, 12:26, 16,679 reasoning / 22,553 total out, $0.34 |
| Deploy scheduling | 5/5 perfect, 1:29, 6,543 reasoning / 6,822 total out, $0.10 | 5/5 perfect, 4:46, 7,792 reasoning / 8,365 total out, $0.13 |
| Probability | 4/5 perfect, 1:47, 6,242 reasoning / 8,365 total out, $0.13 | 5/5 perfect, 6:48, 9,682 reasoning / 12,381 total out, $0.19 |
| Perfect runs | 14 of 15 | 15 of 15 |
| Total cost, both on Fireworks ($3/$15) | $2.48 | $3.26 |
| Total cost, Kimi at cheapest price ($1/$9) | $2.48 (no cheaper provider) | $1.96 |

Kimi K3 had 15 perfect runs out of 15, and Ember-1 had 14. Ember-1’s one miss was an arithmetic slip on the probability test; it doesn’t seem too significant to me since it was one out of 15.

Something I noticed during my testing that wasn’t in the marketing claims was that Ember-1 finished each set of tests 3.4 times faster than Kimi K3. As for the reduced reasoning token usage, Ember-1 used 23% fewer reasoning tokens. This helped keep costs down. In total, it cost $2.48 compared to Kimi K3’s $3.26 on Fireworks, which makes it 24% cheaper.

One caveat is that Kimi K3’s cost depends on the provider. At its lowest listed price of $1 per million input tokens and $9 per million output tokens, the same runs would have cost $1.96, less than Ember-1.

### What do I think?

Ember-1 is about as accurate as Kimi K3 and uses far fewer reasoning tokens. The lower costs on Ember-1 on this test aren’t as important because a user who wants to use Kimi K3 can route to a cheaper provider on OpenRouter, which brings the price down below Ember-1’s.

One thing I know about Kimi K3 is that it’s slow. Cheap and slow. My speed numbers come from Fireworks’ standard endpoint, though, and I didn’t test the cheaper providers. If you have time and want to pay less, Kimi K3 wins. If you want almost identical results to Kimi K3 at a much faster rate, use Ember-1.

**The prompts**

Each prompt ends with a fixed answer format so grading can be automatic.

**Logic puzzles**

*Solve all three logic puzzles below. Each has exactly one solution.*

*PUZZLE SMALL: 4 engineers (Ava, Bo, Cleo, Dev) each own exactly one server. Each server has a rack position (1, 2, 3, 4, numbered left to right), an operating system (Debian, Alpine, Fedora, Ubuntu), a role (cache, queue, proxy, db). No two servers share any of these values.*

*Clues:*

*If the server in rack 3 runs Fedora, then the Debian server is in rack 3.*

*The server in rack 1 is Dev’s.*

*Exactly one of these is true: the server in rack 4 runs Ubuntu, or the Alpine server is not Bo’s.*

*Cleo is the proxy.*

*The db server is Dev’s.*

*Ava runs Alpine.*

*The queue server is not Ava’s.*

*Bo is in rack 3.*

*Bo and the Ubuntu server are in neighboring racks.*

*PUZZLE MEDIUM: 5 engineers (Ava, Bo, Cleo, Dev, Eun) each own exactly one server. Each server has a rack position (1, 2, 3, 4, 5, numbered left to right), an operating system (Debian, Alpine, Fedora, Ubuntu, Arch), a role (cache, queue, proxy, db, build), a replication data center (Oslo, Lima, Pune, Accra, Perth). No two servers share any of these values.*

*Clues:*

*Cleo is the db.*

*Exactly one of these is true: the cache server runs Arch, or the server replicated to Perth is the proxy.*

*The server in rack 5 runs Fedora.*

*Exactly one of these is true: the server in rack 2 is not the proxy, or Cleo runs Debian.*

*Exactly one of these is true: the server replicated to Pune is the db, or Dev is in rack 3.*

*The server in rack 1 is the db.*

*The proxy server is in rack 5.*

*The server in rack 4 runs Ubuntu.*

*The cache server and the server replicated to Pune are in neighboring racks.*

*Ava is the cache.*

*The server replicated to Accra is the queue.*

*The server replicated to Lima is not in rack 3.*

*Eun runs Alpine.*

*The queue server is not in rack 2.*

*The Fedora server is not Dev’s.*

*The server in rack 2 is not replicated to Lima.*

*PUZZLE LARGE: 7 engineers (Ava, Bo, Cleo, Dev, Eun, Finn, Gia) each own exactly one server. Each server has a rack position (1, 2, 3, 4, 5, 6, 7, numbered left to right), an operating system (Debian, Alpine, Fedora, Ubuntu, Arch, Rocky, NixOS), a role (cache, queue, proxy, db, build, metrics, auth), a replication data center (Oslo, Lima, Pune, Accra, Perth, Quito, Riga). No two servers share any of these values.*

*Clues:*

*The build server is Cleo’s.*

*The proxy server does not run Fedora.*

*The server replicated to Quito is Finn’s.*

*The server in rack 6 is replicated to Lima.*

*The Alpine server is exactly 4 racks to the right of the auth server.*

*The server replicated to Oslo is Dev’s.*

*The Debian server is replicated to Quito.*

*The server replicated to Accra is not the build.*

*The Rocky server is exactly 1 rack to the right of Gia.*

*Exactly one of these is true: the Ubuntu server and the server replicated to Pune are in neighboring racks, or the server replicated to Oslo runs Fedora.*

*The server replicated to Oslo does not run Fedora.*

*Ava runs Rocky.*

*Exactly one of these is true: the proxy server is somewhere to the left of the server replicated to Riga, or the Debian server is in rack 7.*

*The auth server and Bo are in neighboring racks.*

*The metrics server is Gia’s.*

*The Fedora server is somewhere to the left of the server replicated to Pune.*

*Exactly one of these is true: the server replicated to Accra is in rack 2, or Finn is the queue.*

*If the Debian server is Finn’s, then the server in rack 7 does not run Rocky.*

*The NixOS server is not replicated to Perth.*

*The server in rack 7 is replicated to Accra.*

*The server replicated to Pune is the db.*

*At the end of your response, give each solution as a block, one line per engineer, in the order the engineers are listed in that puzzle:*

*SMALL:*

*<name> | <rack> | <os> | <role>*

*MEDIUM:*

*<name> | <rack> | <os> | <role> | <dc>*

*LARGE:*

*<name> | <rack> | <os> | <role> | <dc>*

---

**Deploy scheduling**

*You are planning a production rollout of 12 services. Time is measured in whole hours from hour 0.*

*Services (owning team, deploy duration in hours):*

*auth: team A, 3 hours*

*billing: team B, 4 hours*

*catalog: team C, 2 hours*

*search: team C, 3 hours*

*cart: team B, 2 hours*

*checkout: team B, 3 hours*

*payments: team A, 4 hours*

*notify: team C, 2 hours*

*ledger: team A, 2 hours*

*gateway: team A, 3 hours*

*reports: team B, 3 hours*

*inventory: team C, 4 hours*

*Rules:*

*Dependencies. A service may start deploying only after every service it depends on has finished deploying:*

*gateway depends on auth*

*payments depends on auth*

*search depends on catalog*

*cart depends on catalog*

*cart depends on inventory*

*checkout depends on cart*

*checkout depends on payments*

*ledger depends on billing*

*ledger depends on payments*

*notify depends on checkout*

*reports depends on ledger*

*gateway depends on search*

*notify depends on gateway*

*Each team can deploy only one of its services at a time.*

*Different teams can deploy at the same time.*

*Blackout windows. No deploy may be in progress at any time during hours 9 to 11 or hours 17 to 19. A deploy may end exactly at hour 9 or 17, and may start exactly at hour 11 or 19. A deploy cannot pause and resume.*

*Each deploy runs from its start hour for its full duration without interruption.*

*What is the earliest hour by which all 12 services can be finished? Give a schedule that achieves it.*

*At the end of your response, give your answer in exactly this format:*

*MAKESPAN: <hour>*

*<service>: <start hour>*

*(one line per service, all 12 services)*

---

**Probability**

*A client calls a payment API and retries on failure.*

*The server is in one of two states on each attempt, Healthy or Degraded.*

*On the first attempt, the server is Healthy with probability 4/5 and Degraded with probability 1/5.*

*Between consecutive attempts, the state changes like this: from Healthy, it stays Healthy with probability 3/4 and becomes Degraded with probability 1/4. From Degraded, it stays Degraded with probability 2/3 and becomes Healthy with probability 1/3.*

*An attempt succeeds with probability 9/10 if the server is Healthy and 2/5 if it is Degraded, independently of everything else given the state.*

*The client makes at most 4 attempts and stops as soon as one succeeds.*

*Circuit breaker: if two consecutive attempts both hit a Degraded server and both fail, the client stops immediately and makes no more attempts.*

*Answer these questions with exact fractions in lowest terms:*

*Q1. What is the probability that the request eventually succeeds?*

*Q2. What is the expected number of attempts the client makes?*

*Q3. Given that the request succeeds, what is the probability that it succeeded on exactly the second attempt?*

*Q4. What is the probability that the circuit breaker ends the request early, before the client has used all 4 attempts?*

*Q5. Given that the request succeeds, what is the probability that the first attempt failed?*

*At the end of your response, give exactly five lines in this format:*

*Q1: <fraction>*

*Q2: <fraction>*

*Q3: <fraction>*

*Q4: <fraction>*

*Q5: <fraction>*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)