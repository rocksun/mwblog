**For the past 18 months, the corporate approach to artificial intelligence** has been a gold rush. The mandate was simple: adopt, integrate, and scale. For engineering teams, this meant a sudden, open-ended access to large language models. It led to a bizarre, hyper-competitive phenomenon where internal leaderboards tracked which engineers — or which departments — could consume the most tokens. It was [tokenmaxxing](https://thenewstack.io/lanai-token-tuner-tokenmaxxing/), a metric driven by misguided enthusiasm, devoid of any correlation to business outcome.

For the record, AI tokens are the fundamental building blocks of data — such as word fragments, punctuation, or pixels — that LLMs use to process and generate information. In English, one token is roughly equivalent to three-fourths of a word, or 4 characters. They dictate AI context limits, performance, and API billing.

But this party, driven by corporate direction to use as many tokens as possible in a short amount of time to pile on the AI secret sauce, is ending. The hangover is now arriving in the form of massive, unforecasted cloud bills.

> “You can spend (lots of) money by doing nothing useful at all.”

[Jason Cumberland](https://www.linkedin.com/in/jasoncumberland/), co-founder and Chief Product Officer at Herndon, Virginia-based [Revenium](https://www.revenium.ai/), tells *The New Stack* about the change:

“The world went crazy one way and then came back down to earth,” Cumberland says. “We watched that, and we’re just like, this is insane. You can spend (lots of) money by doing nothing useful at all.”

As the cost of AI has shifted from a theoretical experimentation budget to a tangible line item affecting the bottom line, enterprise leaders are pivoting from reckless expansion to strict control. This friction is where Revenium, an advanced [observability](https://thenewstack.io/introduction-to-observability/) toolset, has positioned itself. This is a company that originated as an API monetization specialist and has successfully pivoted to become what it calls an AI economic control system.

On Tuesday, Revenium launched a new feature, [AI Insights](https://docs.revenium.io/optimize-performance/ai-insights), within its [AI Economic Control System](https://www.revenium.ai/) to identify and recover wasted AI budget. By analyzing transaction history using a multi-stage detection pipeline, the tool generates a ranked list of optimization recommendations, each tied to specific dollar amounts and linked directly to the underlying transaction data. This approach addresses the analysis gap that often plagues enterprises, where teams are overwhelmed by usage data and lack actionable insights for remediation.

In beta testing, AI Insights identified significant inefficiencies, including costly circular dependencies in agent requests, reliance on outdated, expensive models, and high failure rates with specific model providers. By prioritizing these issues based on potential monthly savings, the tool provides engineers with a clear punch list for quick fixes. Rather than just surfacing raw dashboards, Revenium’s engine automates the discovery and ranking of waste, enabling teams to act quickly on the findings that will have the greatest impact on their bottom line.

## **The API roots of AI observability**

Revenium spent the first phase of its six-year history focused on API monetization, partnering with giants such as [Salesforce](https://salesforce.com) and [Mulesoft](https://mulesoft.com). When the generative AI bubble began to inflate, the company realized that the metering infrastructure it had already built for high-volume API transactions was uniquely suited to the AI era.

“All AI is just APIs,” Cumberland says. “We realized that the metering back-end we built for high-volume transactions could be really valuable in the AI world.”

Revenium is not another [FinOps](https://www.apptio.com/resources/ebooks/finops-new-approach-cloud-financial-management/?utm_source=google&utm_campaign=cloud-ams-multi-en-finops_low-intent&utm_medium=cpc&utm_content=low_intent&gad_source=1&gad_campaignid=23649566128&gclid=Cj0KCQjw0JnRBhDJARIsALobnXaRYBmlGFqqPl8xUBjBNRkmA9j7xzVA428LRKx8lAocWZ8fI7K7d5kaAreDEALw_wcB) tool. While companies such as competitor [CloudZero](https://www.cloudzero.com/) have adapted their marketing to capture the AI ROI trend, Revenium approaches the problem from a runtime instrumentation perspective. It doesn’t wait for billing APIs, which can be delayed by hours or days. Instead, Revenium’s code injects itself at runtime, metering transactions as they occur and enabling immediate blocking if budgets are breached.

## **The iceberg problem**

To understand the scope of the problem, Cumberland refers to what he calls the “iceberg chart.”

Most organizations view AI spend through a narrow lens: the cost of tokens. That is the tip of the iceberg visible above the water. Beneath the surface, however, lies a massive, obscured expanse of downstream costs. AI agents are now rarely isolated; they connect to systems such as [Snowflake](https://snowflake.com), [Stripe](https://stripe.com), or third-party identity services. Each of these calls carries a cost — yet in most corporate environments, the AI agent is completely disassociated from these downstream impacts.

“Imagine an agent who’s involved in a financial services workflow,” Cumberland says. “Its job is to process loans, look at data, and make compliance decisions. During this process, an agent can make API calls to external services such as [Equifax](https://equifax.com) or [TransUnion](https://transunion.com). A single credit report might cost $25. You’ll get a bill for tokens from the LLM provider, and you’ll get a bill from Equifax at the end of the month, but you have no way to understand that when your Equifax bill goes up, it’s actually tied to an agent running wild.”

Revenium’s system is designed to break down these silos, creating a data model that allows companies to associate the costs of external services directly with the agent who triggered them.

## **The three horizons of AI maturity**

Cumberland and his team view the adoption of AI observability through three horizons of maturity:

* **Attribution:** This is the baseline. It’s the ability to see where money is being spent, which providers are involved, and which specific agents or business units are consuming those tokens. It’s about shifting from a global, murky cloud bill to clear, actionable data.
* **Downstream system association:** This is where the “iceberg” problem is solved. Companies connect the dots between AI agents and the third-party infrastructure (such as Snowflake or credit-check APIs) they interact with, creating a holistic view of the true cost of an automated process.
* **ROI and outcome analysis** are the ultimate goals. They move beyond “how much are we spending” to “is it worth it?”

In this third horizon, Revenium tracks the relative performance of AI against human workflows. It instruments rescue metrics to calculate how much human time is spent fixing, reviewing, or cleaning up after an AI agent. “When the AI agent fails, and it bounces back to a human, you have the token costs of the initial execution, and now you have the human time on top of it,” Cumberland says. “What we’re helping companies do is track both.”

## **Toward AI workforce management**

Perhaps the most provocative aspect of Revenium’s vision is its approach to workforce management for AI agents. This parallels workforce management.

We have decades of sophisticated management and performance review systems for human employees. Yet, as companies deploy thousands of agents to handle tasks ranging from code implementation to support deflection, there is no equivalent infrastructure to manage them.

> “I pretty firmly believe that eventually, when employees go to their performance review in the future, it’s going to be: ‘How good of a job did you do, and how many tokens did you spend?'”

“I pretty firmly believe that eventually, when employees go to their performance review in the future, it’s going to be: ‘How good of a job did you do, and how many tokens did you spend?'” Cumberland says.

For now, the urgency is driven by financial necessity. As enterprise leaders realize that AI adoption without observability is essentially a flight in the dark, the demand for control systems like Revenium is surging. The goal is not to stop innovation, but to replace the “leaderboard” mentality with a metrics-driven reality.

For a new stack of technology built on the promise of efficiency, the next logical step is learning how to quantify the value of the intelligence that drives it. For Revenium, the future of AI isn’t just about generation; it’s about the bottom line.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2024/09/314a85cc-cropped-89f126f8-chrisp-600x600.png)

Chris J. Preimesberger, a contributing writer/editor at several publications since June 2021, is former editor in chief of eWEEK. He was responsible for the publication's coverage for a decade (2011-2021). In his 16 years and more than 5,000 articles at...

Read more from Chris J. Preimesberger](https://thenewstack.io/author/chris-j-preimesberger/)