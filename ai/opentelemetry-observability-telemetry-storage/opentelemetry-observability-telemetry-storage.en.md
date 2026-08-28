**Observability is entering a new phase** now that OpenTelemetry has standardized instrumentation for data collection. Unfortunately, the observability industry still lacks a cost-effective way to store, retain, search, and analyze full-fidelity telemetry data. This results in blind spots in observability and many teams operating without full operational visibility.

As AI systems generate more logs, traces, and metrics — thereby making the blind spots issue worse — **[Bronto](https://bronto.io/)**, a Dublin, Ireland, firm offering an intelligent data observability platform, is betting that the next observability platform battle will be won at the data layer, not the dashboard layer.

## Bolt-ons and incremental efficiency aren’t enough

[Trevor Parsons](https://www.linkedin.com/in/trevparsons/), co-founder and co-CEO of [Bronto](https://bronto.io/), tells *The New Stack* that the industry has been optimizing at the edges rather than rebuilding the economics and architecture of telemetry storage. The industry has introduced a wide array of “hacks” and “capabilities” to avoid tackling this issue head-on and ultimately to protect their margins.

“If you are a couple of times cheaper or 50% cheaper, that ain’t going to cut it,” Parsons says, because data volumes, especially AI telemetry, are growing so quickly, on top of already stretched observability budgets and inefficient datastores.

## Promises, Promises, Promises…

Parsons elaborates, “Observability has always and continues to have a data problem.”

The eternal promise of observability has been delivering teams a clearer view of what’s happening inside their systems.

> “Observability has always and continues to have a data problem.”

But in practice, that view is often incomplete, expensive, and short-lived. For too many teams, observability has become less about asking better questions and more about fighting the cost and complexity of storing the data they already need.

“Sometimes people frame that as a cost problem, where they’ll say observability is up to 20 or 30% of your infrastructure spend,” Parsons says. “I actually think this minimizes the issue; it’s much bigger than that. Teams are actually paying 10, 20, 30% of their infrastructure spend for access to only a sliver of their data.”

[Noel Ruane](https://www.linkedin.com/in/noel-ruane/), co-founder and co-CEO of Bronto, frames the challenge that organizations face and tells *The New Stack*, “Agents and applications are generating more logs, traces, and metrics each day. The software landscape has accelerated, but are observability vendors keeping pace? No, they’re offering workarounds, bolted-on features, and asking teams to accept blind spots.” In short, Ruane says, they’ve failed to solve the data problem.

## Out with the old observability model

“Customers are not getting access to all of their observability data, Parsons explains. “They have to cut their retention from three days to seven days to 30 days. They have to sample data. They have to rehydrate data.”

In other words, today’s tools make customers choose which parts of their own data they’re allowed to see, and you may only get to see it for a short amount of time.”

> “The solutions that are being put in front of customers to give them their data are always full of compromises, forcing teams to choose between cost, coverage, and speed of data access. The burden is always put on the customer by vendors.”

“The solutions that are being put in front of customers to give them their data are always full of compromises, forcing teams to choose between cost, coverage, and speed of data access,” Parsons says. “The burden is always put on the customer by vendors.

“But really this should be the other way around; it’s the vendors’ job to innovate on behalf of the customer”

## OpenTelemetry: Collection solved, storage problem exposed

[Severin Neumann](https://www.linkedin.com/in/severinneumann/), head of community at Bronto, tells *The New Stack* that OpenTelemetry has helped standardize instrumentation and data collection, while reducing reliance on proprietary agents.

But that success has created a new bottleneck, says Neumann, who is also an OpenTelemetry maintainer and member of the OpenTelemetry governance committee. Now that organizations can collect more telemetry, they need somewhere affordable and useful to put it.

“We have fixed the instrumentation problem,” Neumann says. He cautions that enterprises now need ways to handle all this data. And if enterprises can’t store it and instead throw away large parts of it, humans and agents can not make sense of it.

## The observability business model doesn’t align with customer value

The legacy observability tool business model charges customers for data storage, rather than the value teams get from their data, Parsons says. Customers tell him the same thing constantly: “I pay the same price even if I never search my data.” In many cases, customers find existing tools difficult to use and feel that their observability solution is just a really expensive data store that they do not get a lot of value from.”‘

Noel Ruane assessed the market by saying, “Traditional vendors like Datadog know their pricing model isn’t sustainable. They’ve introduced defensive features like ‘Flex Logs’ and a new ClickHouse partnership to try to keep customers from jumping ship, but they’ve only added new complexity for their customers.”

Especially in the AI era, Ruane adds, the traditional business model charges teams in ways that discourage them from capitalizing on their data. Customers should pay much less for data that sits idle and more when they actually derive value from it with queries and analysis.

## Bronto’s technical differentiation

Bronto isn’t selling another observability dashboard. It argues that observability is a storage problem before it’s a visualization problem, and that’s where the company went.

Underneath the platform is a custom-built polymorphic data store called BrontoD, specifically designed for observability data. The pitch: enterprises can keep more than 100 times the observability data they hold now, and it won’t get slower or harder to use.

Why that matters comes down to how the three signals break. Metrics, logs, and traces each hit a wall at different points, and Bronto says it built BrontoDB to tackle these issues head-on. Parsons is blunt about two of them.

“With metrics, we’ve solved the high cardinality problem where costs traditionally explode with high cardinality metrics,” Parsons says. “With logging, we’ve solved the indexing problem where there was always a trade-off between fast logs and paying through the nose for it or having slow logs and getting them slightly cheaper.”

* High cardinality is what wrecks metrics pricing. Add enough unique dimensions and the bill lands somewhere nobody forecast. Bronto says it was built specifically to take that surprise out.
* Logs have always been pick-your-poison: fast and expensive, or cheap and slow. Bronto says that choice goes away — sub-second search across petabytes, no shortened retention windows, no rehydrating cold data, no waiting.
* Traces, Bronto argues, shouldn’t be sampled at all. Sampling exists because tools and pricing models couldn’t handle the full stream. Bronto says teams can send it all.

Billing works differently, too. Most vendors charge for data sitting in storage, whether anyone touches it or not. Bronto charges closer to what teams actually search and analyze. That’s the piece that has to hold up if full-fidelity observability is going to be affordable at AI scale.

AI is what raises the stakes, Parsons says. AI systems are non-deterministic and trace-heavy. They throw off more telemetry, and the data has to stick around longer if you want to debug effectively.

He points to an upside as well. As operations become more automated, telemetry data becomes more useful because agents can chew through volumes of history that no SRE would ever read manually.

AI raises both the volume and the stakes, according to Parsons. AI systems create more telemetry because they are non-deterministic, trace-heavy, and require longer retention for troubleshooting. At the same time, AI-enabled operations will make historical telemetry more valuable because agents can analyze far more data than human SRE teams could manually inspect.

> “If AI is the intersection of where data meets intelligence, you can not apply intelligence if you do not have the data.”

“If AI is the intersection of where data meets intelligence, you can not apply intelligence if you do not have the data,” Parsons says.

## The next observability battle

AI is unlikely to fix observability’s data problem. In fact, it will produce more telemetry, create more edge cases, and increase the cost of missing the right signal at the wrong time.

For Bronto, the data layer is the next major battleground. Dashboards still matter, but in an AI-heavy production environment, the more important question may be whether teams have access to all their data for as long as they need so that they can apply AI to it.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/08/252c2165-cropped-498abf5b-will-kelly-tns-headshot-600x600.png)

Will Kelly is a technology writer covering enterprise and cloud native technologies, with over 10 years of experience reporting on how systems evolve and scale. He currently focuses on generative and agentic AI and on developing AI content pipelines. Will...

Read more from Will Kelly](https://thenewstack.io/author/will-kelly/)