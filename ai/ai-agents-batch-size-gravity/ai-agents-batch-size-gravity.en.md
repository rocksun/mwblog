With the introduction of AI-assisted coding tools and agents, many people hoped we’d solve all the problems for human teams.

Without the people, politics, and personalities, software delivery would be easy.

This vision is appealing because we’ve long blamed people for the failures in the system. But the evidence from multi-agent AI provides an awkward truth. The same classes of failure still occur in the same places, for reasons unrelated to humanity.

So why do large batches of work still fail even after you’ve eliminated laziness and stupidity?

## Project village

Traditional thinking on software projects is like a strange village. It has been cut off from the rest of the world for thousands of years and has developed some interesting beliefs about the laws of nature. They carpet their walls, which makes it hard to vacuum. They make their roofs out of glass and struggle with indoor temperatures. And they make clothes from hair, because nobody is allergic to their own hair.

Perhaps the strangest thing about the village is that they believe gravity is an act of human willpower.  
All the animals in the valley are birds, which seem to cling to the branches of bushes, else they glide away into the sky. They also have no fruit trees, which means they’ve never had a Newtonian epiphany. Without evidence to the contrary, their collective delusion has persisted for many generations.

If you visited the village, you’d hear such philosophical musings as “The earth keeps those who keep themselves,” and “I will, therefore I stand.” Every Wednesday, they gather in the town hall to remind each other that “If you stand firm in mind, the ground will rise to meet you.”

To tackle the problem of carpet cleaning, the village invented a cast-iron humanoid robot that vacuum-cleans the walls. To stop the robot from floating away, they built suction devices into its heels. One day, a robot is being moved between houses when its power fails.

To their amazement, the robot doesn’t float away. The village philosophers gathered together to discuss this strange event. The only logical conclusion they could reach was that the robot had developed human willpower, which allowed it to remain earthbound. How else could it stay on the ground?

## It’s not willpower, it’s gravity

Outside of the village, we all know that gravity works on robots, just like it works on people, birds, and rocks. That doesn’t prevent us from making a similar mistake when building software.

Large software projects frequently fail, and the people in charge blame human factors. Blaming people for these failures because they’re slow, lazy, dim-witted, and require rest is like the village believing gravity is a manifestation of willpower.

The reality is that software delivery has a form of gravity that increases relative to batch size. This is why swarms of AI agents fail in all the same ways teams do when you give it large and complex tasks.

In [*The Organizational Physics of Multi-Agent AI*](https://zenodo.org/records/18809207), Jeremy McEntire describes an experiment in which the same multi-service backend system was created using different arrangements of AI agents. There is a belief that coordinating a team of AI agents will enable more complex tasks to be handled by AI, but the experiment showed that the coordination complexity outweighs the benefits of dividing work among multiple agents.

The failures of multi-agent work look familiar. They are the same as the failures of large projects, except there are no humans to blame. This proves the challenges are inherent to complex work and cannot be attributed to human factors.

It strikes me that we have been blaming human factors for bad systems for too long and we need to acknowledge they’re not the reason for past IT system failures.

## A babbling equilibrium

*“When I use a word,” Humpty Dumpty said in rather a scornful tone, “it means just what I choose it to mean — neither more nor less.” –* Lewis Carroll*, Alice’s Adventures in Wonderland*

When I say “rock”, some of you will think of geology (*rocca* comes from Latin) while others will think of music (*roccian* comes from Old English). A select few may think of a seaside hard sugar treat or a tool used to hold unspun fibers.

For something as simple as a word, I can reduce your interpretive preference by putting the word into a sentence. When communication becomes more complex, it’s rare to have perfect alignment on the meaning we intend to convey. Communication precision decreases from perfect alignment and can degrade to a *babbling equilibrium* in which no information is conveyed in the message.

This misalignment can be understood through the pre-DevOps problem of having a development team measured for throughput and an ops team measured for reliability. When you communicate the same information to these two silos, interpretation will vary drastically.

This challenge of transferring information persists when a human instructs an AI agent to perform work. Hence, the counter-arguments of “you’re prompting it wrong.” What surprises more people is that it remains when AI agents send messages to other AI agents. This is why the multi-agent configurations performed worse than single-agent setups.

When you understand why agent swarms compound the problem rather than solving it, the answer starts to look familiar. These aren’t new problems. Long before AI agents, human development teams were failing for exactly the same structural reasons. The teams that recovered did so by tackling the structure, not the people.

## Fixing the system of work

In my past roles, I was often asked to join a company to “fix the development team.” They had reached a stage where every deployment turned into a high-severity incident, every change resulted in highly visible bugs, and the business had lost faith in the team’s ability to deliver working software.

The teams usually had basic tools in place, like version control and automated builds. What was missing was the rest of the deployment pipeline, and this was the root cause of all the problems. Here’s how I’d fix it.

**Deployment automation** made production releases repeatable and reliable, removing the most painful and wide-reaching failures of these teams. This led to more frequent deployments, which in turn reduced the size of work batches. Breaking work into smaller steps is a good way to improve communication success.

**Test automation** increased our confidence that the software was deployable. It wasn’t uncommon to find teams with no automated tests, so adding characterization tests for the most important features reduced the number of embarrassing software versions the team produced, such as those where nobody could even sign in.

**Monitoring and alerting** helped the team understand how the system ran in production. As we fine-tuned the tools, the team became the first people to know when there was a problem, or the early signs a problem was emerging. By prioritizing work that kept the software healthy, we improved our relationship with the business, including executives who handled complaint escalations, and made customers happier with the software.

The result of these three changes isn’t just improvements to deployments, software quality, and observability. Having a complete pipeline lowers your batch size. This keeps complexity low and solves the communication and coordination problems that become insurmountable in large batches of work. The kinds of problems that make it impossible for AI agents to deliver working software are just the ones that prevented teams from doing it.

## Batches have gravity

There are fundamental laws of software delivery that mean batches have a gravitational force that becomes unmanageable by human teams or AI agents. The larger the batches, the heavier everything gets, increasing the energy required to move them.  
Rather than searching for bigger tractors to move giant objects, organizations with modern software engineering practices make everything fit in a lightweight backpack. Small batches are the secret sauce behind Continuous Delivery, and the [DORA research](https://dora.dev/research/?view=detail) increases our confidence in this approach.

Just as Fred Brooks observed in *The Mythical Man Month*, adding people to a late software project makes it later. McEntire’s research suggests this applies equally to situations where you simply increase the number of AI agents tackling the work.  
Continuous Delivery remains the best way to deliver software, no matter who or what is writing the code.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/10/e54f7c3f-cropped-fc6cbbe0-steve-fenton-600x600.jpg)

Steve Fenton is an Octonaut at Octopus Deploy, a DORA community guide and a six-time Microsoft MVP with more than two decades of experience in software delivery. He has written books on TypeScript (Apress, InfoQ), Octopus Deploy, and web operations....

Read more from Steve Fenton](https://thenewstack.io/author/steve-fenton/)