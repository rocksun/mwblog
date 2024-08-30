# How Supabase Is Building Its Platform Engineering Strategy
![Featued image for: How Supabase Is Building Its Platform Engineering Strategy](https://cdn.thenewstack.io/media/2024/08/44d188b4-wesley-tingey-7paifc4fohk-unsplash-1-1024x683.jpg)
[Platform engineering](https://thenewstack.io/platform-engineering/) is not a destination, but is an evolving and constant process of improvement, innovation and experimentation to provide consistent, tested and productive application development tools for developer teams. That is the plan as most companies begin their platform engineering strategies, and that is how it continues to work for open source [PostgreSQL](https://thenewstack.io/benchmarking-postgresql-vs-mongodb-for-genai/) database infrastructure application vendor, [Supabase](https://supabase.com/).
Supabase, which describes itself as an [open source alternative to Google’s mobile and web app development platform, Firebase](https://kinsta.com/blog/firebase-alternatives/), began using platform engineering several years ago. The project began as the company realized that building its own [internal development platform (IDP)](https://thenewstack.io/internal-developer-platform-vs-internal-developer-portal-whats-up/) for its approximately 50 developers would allow the company to consolidate, standardize and automate its development applications to drive increased productivity, code quality and other benefits for its teams. Supabase has been in business since 2020.

“It is growing over time,” [Samuel Rose](https://www.linkedin.com/in/samrose/), a platform engineer at Supabase who came to work for the company in February 2024, told The New Stack. “They were already doing this kind of thing and they [began to] formalize things that everybody was doing into a role that that we can all be responsible for throughout the company.”

“Supabase has always had an evolving platform engineering approach, but I was brought on board to formalize and expand it more across the organization,” said Rose. “We will continue to grow this on a weekly basis and have already made huge progress” in the company’s evolving platform engineering strategy.

The company’s platform engineering project came about as IT administrators and developers across many teams contributed to an effort to create a platform engineering approach for their work, said Rose. “The needs grew so great that Supabase needed to take on at least one person full-time to drive it forward,” which is how he joined the company.

Leading to these decisions was Supabase’s continuously growing customer base and growing technical complexity in managing build, test, and release processes, Rose explained. Also important was the company’s “desire to use and leverage our product where it makes sense on our internal platform,” he added.

“I have been in this industry for more than 20 years,” said Rose. “Supabase started four years ago, and it is quite natural that this company would grow into these needs now, after four years of work and expansion. At Supabase we eat our own dog food and use some of our own components as tools in our internal platform.”

## Doing Platform Engineering the Supabase Way
Supabase did not start from scratch to build and create its platform engineering strategy. Instead, it began with pre-built recommendations for platform engineering tools that were brought together in sample [cloud native landscape](https://landscape.cncf.io/?view-mode=grid) outlines from organizations such as the [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention), added Rose.

“Our platform pretty well maps to those [platform engineering approaches](https://thenewstack.io/platform-engineering-it-is-all-about-the-tooling/),” he said. “But we use some of our own products in our platform, including our own API and Postgres-centered development,” instead of using some off the shelf or Software as a Service components offered in the pre-built recommendation grids.

This custom platform engineering approach works well for Supabase, allowing the company to bring together tools from inside and mix them with other industry-standard tools for application building.

“The main goal is to take the existing building blocks that we are using to do platform engineering and consolidate them, automate and give everybody a more solid foundation to stand on,” said Rose. “It is not a super-conventional platform engineering approach, but it is one that is a good fit for the company. It is growing over time.”

To accomplish this, Supabase is consolidating around certain standards and certain tools in key places for now, according to Rose.

“Sometimes when people talk about platform engineering, they mean adopting this whole platform that is literally like some other software that somebody wrote and putting everything in there, like diving all the way headfirst to the bottom of the pool,” said Rose. “We are not really doing that. We are [also using] our own tools.”

These platform engineering efforts began through a natural outgrowth of Supabase’s development efforts and processes, said Rose. “So, it was easy for them to see this need — they started working on this before I ever got involved. I have been working with them, and we … brought it into reality, in terms of doing the things you described as platform engineering, to the point that it is going to into production. It is ongoing.”

## What’s Included in Supabase’s Internal Developer Platform
To give its developers the tools they need to build their applications for Supabase, the company’s IT administrators have built their platform engineering platform around a spare number of development applications.

“We try to be economical about it so that we do not create [problems], because if you keep throwing tools at the basket, you are going to have to manage it all,” said Rose. “So, we are judicious about this. We have about five to seven major kinds of like components that we use, and we try to consolidate and leverage as much as we can of the existing systems.”

The tools included in Supabase’s IDP feature:

**Developer control plane**: Supabase utilizes internal wikis, GitHub,[Terraform](https://thenewstack.io/terraform-isnt-dead/)and[Pulumi](https://thenewstack.io/pulumi-rocks-ai-infused-infrastructure-as-code-platform/). The company also uses custom tooling based on[Docker](https://www.docker.com/?utm_content=inline+mention), other related tools to run its platform locally, and its SaaS backend as a service product that can also be run locally.**Integration plane**: Supabase uses GitHub Actions, Nix package manager/Debian packages, Docker, Amazon S3 and a self-hosted Nix binary cache. In addition, it uses Humanitec’s Platform Orchestrator with in-house custom applications.**Security plane**: Web application firewall (WAF),[AWS](https://aws.amazon.com/?utm_content=inline+mention)GuardDuty,[Google](https://cloud.google.com/?utm_content=inline+mention)Cloud Platform Intrusion Detection System (IDS), AWS Secrets Manager, AWS EC2 Instance Connect and[its own tools](https://github.com/supabase/auth)in some cases.**Monitoring and logging plane**: Vector, Sentry, BigQuery, VictoriaMetrics and its own[Logflare tool](https://logflare.app/).**Resource plane**: Supabase mostly uses the tools built into AWS and GCP platform, along with strategic use of its own product to manage metadata, clustering and more.
So far, the results of its platform engineering efforts are promising for Supabase.

“One thing is that it is giving us a pathway to manage doing new versions of Postgres for our customers that are better,” said Rose. “Our people in our teams internally can [create] what they call a deterministic build that they can build once and do not have to build again. That is part of the new platform that we are creating for platform engineering. [You] can just use that again and again unless you change something, so it can cut down on the build times and it can help assure that things are repeatable across systems. That was harder to do in the past.”

And by using the IDP, developers can just focus on their code, do their work and move on to the next projects without having to spend their valuable time configuring, collecting and maintaining their development tools, explained Rose. “We are already at the point where many developers can self-service the majority of their needs, while having secure access to monitoring and testing, and supporting production deployments.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)