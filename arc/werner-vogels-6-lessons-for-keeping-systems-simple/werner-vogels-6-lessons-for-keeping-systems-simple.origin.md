# Werner Vogels’ 6 Lessons for Keeping Systems Simple
![Featued image for: Werner Vogels’ 6 Lessons for Keeping Systems Simple](https://cdn.thenewstack.io/media/2024/12/1a783e2c-aws-vogels-occam.jpg)
*ntities should not be multiplied beyond necessity” — William of Ockham, Occam’s Razor.*
Say what you will about [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention), but the cloud giant has been able to scale its systems and services for more than two decades now, continually introducing new features while keeping the user experience manageable.

For his [customary Thursday](https://thenewstack.io/werner-vogels-6-rules-for-good-api-design/) keynote at [AWS re:Invent](https://thenewstack.io/red-hat-brings-ansible-automation-to-amazon-web-services/), AWS CTO [Werner Vogels](https://www.allthingsdistributed.com/) shared some of the lessons he has learned around the practice of *keeping it simple and stupid *in his 20 years of employment with the cloud giant.

Complexity sneaks into system design all the time, so the engineer must be diligent at managing that complexity.

The goal has always been to “scale our systems to become more complex over time in a safe manner,” he said.

## From Flexible to Fatal
The goal is not to eliminate complexity but to manage it effectively.

The danger with enhancing any system is that it brings undue complexity, which is difficult to maintain and robs the user of joy.

But as Larry Tesler [pointed out](https://lawsofux.com/teslers-law/), complexity can’t be eliminated, it can only be moved around.

Now, there is good complexity, which was added to help the systems grow, and then there is the kind that happens without architectural oversight, which just slows down users and makes systems harder to maintain, he explained.

Complexity is not just counted by the number of components in a system but how those components are placed.

![Tessler quote.](https://cdn.thenewstack.io/media/2024/12/00096194-aws-vogels-tesler.jpg)
“You cannot reduce the complexity of a given task beyond a certain point. Once you’ve reached that point, you can only shift the burden around.” — Larry Tesler

Here, Vogels gave an example of bicycle design.

Actually, the simplest form of a cycle is the unicycle, which has only one wheel. Unicycles are very flexible (“they can turn on the spot”), but are very difficult to ride.

On the other side of the spectrum are the tricycles, which are very easy to ride but cumbersome and difficult to maneuver, as anyone who has driven one knows.

The best design is actually the two-wheeled bicycle, which offers ease of use and flexibility.

“The bicycle has more components, but it is the simplest form from a holistic point of view,” he said. It is no accident that bicycles are the most popular form of cycling.

Place the complexity where it needs to go.

Amazon S3 (Simple Storage Service) served as an example, offering only eventual consistency and not strong consistency. This meant that if a customer procured an Amazon S3 bucket, it would be available eventually, but maybe not immediately.

However, customers want strong consistency and have started building workarounds to ensure strong consistency within their own designs on top of S3, which has led to undue complexity in their own systems.

AWS finally re-engineered S3 for strong consistency, “moving the complexity to where it needed to be,” namely away from the customer.

So, how does a system engineer manage complexity in their own systems?

Vogels offered six tips:

## 1. Build Systems That Can Evolve
Software systems that don’t move forward die. Even the most stable software sees the world move forward without it.

Besides, who doesn’t want to see their favorite app with new features or go faster?

Your systems will grow over time, and you will need to revise your architectures, Vogels advised.

“Whenever you change an order of magnitude in scale, you’ll need to revisit your architecture,” Vogels said. When S3 was rolled out, the design engineers knew they would be changing the architecture. Over time, it has accrued a staggering range of features despite its simple footprint of an API.

” You see that every year, we added new functionality without any impact on the functionality we were delivering for our customers,” he said.

Same with network services, which, following user requests, evolved significantly.

“We knew that whatever networking capabilities we were giving you in 2006 would be radically different in 2010 and definitely in 2020,” Vogels said.

You need to have a strategy to deal with complexity, which will grow in your system over time.

Evolvability is a precondition for managing complexity, Vogels said.

## 2. Break Up Complexity
Complexity can sneak up on your app, like the heat on the proverbial frog stew.

“Small changes seem manageable, easy to absorb at first, but if you ignore the warning signs, systems become more complex and harder to manage and to understand,” he said.

The answer is to break systems into multiple, more manageable components.

[Amazon CloudWatch](https://thenewstack.io/amazon-cloudwatch-gets-feature-flags-user-based-monitoring/) started as a simple monitoring service. As more features were added, they were each loaded on the landing page until the page got so busy that AWS redesigned it so that it only held the core functionality. Other features were moved into their own environments.
How big should a service be? It should be able to fit into one engineer’s brain.

“If you can’t keep it in your head, your service in general is getting too big,” Vogels said.

## 3. Align Architecture to Business Needs
Build business-focused components with “smart end points” and “fine-grained interfaces” via well-documented APIs, Vogels said. Decentralize them so that they “evolve independently.”

Enterprise technology is not built for its own sake. It is built for customers. So system architects need to work closely with the business units they serve.

Collaboration is essential. The business unit may say it wants 100% uptime. This is doable, but expensive. So, the system designer may have to point out how expensive 100% reliability will be.

“And then you can have a conversation,” he said.

Everything fails all the time, Vogels has been quoted as saying. So the trick is to plan for failure.

## 4. Organize Work into Cells
As the app grows in popularity and features, it incurs complexity in how it must be operated as well. Look to a cell-based architecture to keep this growing complexity simple.

“The time to build a system is often minuscule compared to the time that you’re going to run the system. So investing in manageability up front is crucial,” Vogels said.

Managing these operations must also decomposed into smaller building blocks. This is to reduce the scope of impact, which is essential for minimizing downtime.

“Cells create order in a complex system,” he said. “They isolate issues to specific units without impacting the other units.”

A router and control plane are needed to route requests to individual cells. Routing tags can be based on Zone ID, Host ID, customer ID.

“Decomposing into cells is something that will help you, over time, maintain reliability and security for your customers,” he said.

## 5. Design Predictable Systems
Uncertainty is hard to handle. So, design your system up front to reduce uncertainty.

AWS runs a hyperplane for its customer-facing load balancers to handle all the changes that millions of customers are using to change configurations.

Surprisingly enough, AWS did not use an [event-driven architecture](https://thenewstack.io/the-basics-of-event-driven-architectures/) to set up this service, which, contrary to popular belief, would be a bad approach for this task, because the rate of workload requests coming from users would be unpredictable.

Instead, AWS writes the changes to an S3 file, which the load balancers pick up in regular polling intervals.

“Simplicity requires discipline” — AWS CTO Werner Vogels

“It’s a pattern we call constant work, ” Vogels said. This approach avoids spikes, backlogs, and bottlenecks and also makes the system self-healing since “[S3 is impermeable](https://thenewstack.io/with-warpstream-confluent-got-a-new-type-of-kafka-platform/).”

AWS’ [Route 53](https://aws.amazon.com/route53/) domain name service operates its health checkers operates on the same principle: polling not queuing.

## 6. Automate All the Things
To manage complexity, automate complexity.

AWS uses automation to complete many tasks, even building out a new regions, which is completely automated.

The question is not what to automate but what not to automate. Only those decisions that humans truly need to be in the loop should there be human intervention. Automation should be for everything else.

“Automation should be the standard, and the exception should be where we have humans in the loop,” Vogels said. “Manual input should only be required in those areas that truly require human judgment.”

Security is one heavily automated process at AWS, with processes such as automated threat intelligence. AWS gets, “Literally trillions” of DNS change requests each day, with at least 100,000 malicious domains are identified each day through an automated process — a process that would be impossible to do by hand.

Support tickets are another area ripe for automation [through agents](https://thenewstack.io/aws-launches-new-ai-agents-to-simplify-legacy-migrations/). Agents are best for very narrow use cases, where they are given a range of tools to resolve an issue through a process called “serverless prompt chaining.”

If an agent can’t resolve an issue, only bring it to humans’ notice.

“Automate everything that doesn’t require high judgment,” Vogels said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)