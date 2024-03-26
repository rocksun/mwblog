# Why Isn’t the World Upgrading Its Databases?
![Featued image for: Why Isn’t the World Upgrading Its Databases?](https://cdn.thenewstack.io/media/2024/03/6fef3377-database-upgrade-2-1024x576.jpg)
[Databases](https://thenewstack.io/data/) are the foundations of applications and software. They are also somewhat invisible; as the lingua franca of software has it, they are the backend, the implication being that they’re situated *behind* or *beneath* everything else.
This means that when it comes to upgrading, it’s easy to fall into one of two traps: either forgetting that they’re there or feeling intense anxiety that you’re messing around with something you shouldn’t touch.
This is a point made by
[David Stokes](https://www.linkedin.com/in/davidmstokes/), technology evangelist at [Percona](https://www.percona.com/?utm_content=inline-mention), an organization that provides support and services for [open source databases](https://thenewstack.io/open-source-databases-in-the-age-of-the-dbaas/).
“Part of it is if it’s working, and [teams] are not sure about what the database really does or how it works, they don’t want to touch it,” he told The New Stack.
Similarly, he added, “Who would take something out of production to upgrade it? If it doesn’t come back on time, what are the repercussions?”
The attitude, he suggested, is typically: “It’s working now… why touch it? Wait until it breaks.”
The question of upgrading databases is particularly significant in the context of certain versions of open source databases reaching their end of life (EOL).
In 2023, for instance, the end came for
[MySQL 5.7](https://thenewstack.io/oracle-support-for-mysql-5-7-ends-soon-key-upgrades-in-8-0/), a hugely popular release that had been around for almost a decade (it was [released all the way back in 2015](https://thenewstack.io/mysql-5-7-gets-savvy-with-a-cool-replication-hack/)), PostgreSQL 11, Apache Cassandra 3, and MongoDB 6.3. Of course, when a software is being ‘retired’ (for want of a better term) there are typically new versions that a vendor or community has decided to put its energy behind — [MongoDB 7.0](https://thenewstack.io/how-to-plan-your-mongodb-upgrade/) was released in August 2023, [PostgreSQL 16](https://thenewstack.io/postgresql-16-expands-analytics-capabilities/) in September 2023 and [Apache Cassandra 5](https://thenewstack.io/cassandra-5-0-what-do-the-developers-who-built-it-think/) in November 2023.
## The End of Life Cliff Edge
For many teams, EOL represents a cliff edge. It means the software will no longer be patched and updated, opening up an even greater risk of
[security](https://thenewstack.io/security/) issues, and potentially, performance ones as well. [Documentation](https://thenewstack.io/an-engineers-best-tips-for-writing-documentation-devs-love/) won’t, of course, be maintained, and any support (if there was anything in the first place) will completely disappear. In some instances it can be a compliance issue — in the world of payments, for example, organizations that are PCI-DSS certified — those that need to comply with payment card industry data security standards — must deploy any critical patches no more than a month after they are released. [Jan Wieremjewicz](https://www.linkedin.com/in/janwier/), senior product manager at Percona, recalls the [Log4J security breach](https://thenewstack.io/log4j-the-pain-just-keeps-going-and-going/). “Imagine running on end-of-life software that doesn’t get patched to exclude potential Zero Day exploits,” he told The New Stack. “I have goosebumps the moment I think about it!”
The risks of not upgrading databases are substantial. In essence, what should be the robust foundations of your wider systems come to be a liability, a time bomb that could derail what seems functional and stable at any moment.
But it’s also worth noting that the release of new versions — especially major releases — can represent opportunities for engineering teams. Consider the new features and improved experience that is customary when any software is launched. While some of this could be dismissed as marketing hype, it’s important to nevertheless recognize that failing to upgrade might mean you’re missing out on a better way of doing things.
## Why Not Upgrade?
Given these substantial risks, it’s worth digging deeper into the sense of avoidance (if not quite fear) that characterizes certain organizations. One reason Wieremjewicz highlighted is the changing makeup of software engineering teams.
Database architects “are a dying breed,” he said — and they’re getting crowded out by site reliability engineers. “There are
[fewer and fewer DBAs and more and more SREs](https://thenewstack.io/why-a-dataops-team-needs-a-database-reliability-engineer/), who are, very often, not as expert in database problems as DBAs are.”
This is partly, he suggested, a symptom of the rise of the cloud-based
[Database as a Service (DBaaS)](https://thenewstack.io/developer-caveats-for-database-as-a-service/). Although, on the one hand, it has simplified many aspects of database configuration and management, in turn, it has allowed complexity to creep in elsewhere, while skills and organizational structures evolve in ways that aren’t necessarily equipped to handle that complexity.
“We’ve gone from having maybe a handful of databases years ago to thousands if not more, databases,” Stokes says. “You still need someone to go through and check on the queries and do the basic hygiene work, making sure the accounts are right, the passwords, the software is up-to-date, that is replicating properly, that things are being backed up.”
This isn’t tangential to the question of database upgrades: it highlights the very core of the problem. At a time when databases are treated as lightweight building blocks rather than heavy, seemingly unmovable anchors, the very moment we are reminded that databases are complicated things that require sustained attention and care, we want to pretend that they simply cannot be touched, or that they’re tomorrow’s problem.
## A Lack of Sex Appeal?
The argument could be made that upgrading a database just doesn’t have the sex appeal (or, more specifically, the obvious commercial value) that other projects have. It is very much “hygiene work,” to use Stokes’ phrase.
He explained it another way: “You have a senior VP come in and say, ‘Hey, I have this great idea for this new thing we’re going to do. This is my pet project. I want you to take care of it. You say ‘Yeah, but the old system that manages the inventory process needs some upgrades.’ ‘Yeah, but this is my pet project I really needed this.’”
There’s only one way this goes, Stokes argued — and it’s not in favor of the upgrades.
“Database upgrades are always tricky,” he said, “because they’re just subtle changes, even at the best of times. it’s a lot of going through the release notes, and hopefully doing a test or two, to make sure that everything works well.”
## The Unique Challenges of Open Source Databases
Open source databases are particularly challenging when it comes to upgrading. You are almost on your own, probably dependent on the
[contributing community](https://thenewstack.io/how-community-helps-developers-grow/) for relevant documentation and even support.
In these situations, the flexibility that an open source database can offer engineering teams becomes a burden. Teams are hampered by something that they cannot easily manage on their own — even the most active open source projects can only do so much when it comes to supporting teams with their specific implementation.
This is where Percona comes in. It started life some time ago, with Wieremjewicz telling the story of how Founder
[Peter Zaitsev](https://thenewstack.io/author/peter-zaitsev/) left MySQL after working there as a developer with an ambition to provide greater support for users.
Although MySQL is a fundamental part of the company’s origin story, its scope covers open source databases more broadly. The team is as likely to be providing support to companies using PostgreSQL or MongoDB as it is MySQL.
This platform or tool agnosticism can be advantageous, for a number of reasons.
“We are able to advise on solutions — even on moving from one database to another, in a very true and honest capacity, because there is no money we are making, pushing some software that we create,” Wieremjewicz said. “It’s literally for the benefit of the user.”
In the particular context of upgrading databases, vendor agnosticism can presumably allow organizations to be more open-minded or even creative in how they approach a database problem. Sure, upgrading from MongoDB to MongoDB might make sense, but what if exploring a new database would be more relevant for your specific technical context?
It’s very hard to make those decisions on your own, even with the most knowledgeable and open team — external, agnostic advice can be immensely valuable in providing the necessary support and drive for change.
## The Key to Upgrading: Anticipate and Prepare
There’s no getting away from the fact that upgrading databases can be challenging. What’s crucial is planning and remaining one step ahead.
“You have to plan way ahead, you cannot wait for the end of life to happen, you should anticipate way earlier,” said Wieremjewicz.
Failing to do so could have significant technical — and maybe commercial — issues that are much harder to correct down the line.
Stokes doesn’t believe there’s one right way to upgrade a database. How it’s approached will ultimately depend on the maturity and confidence of the organization actually doing it.
“This is one of those things we’re like learning to ride a bicycle,” he said. “A few people jump on and do it by themselves — other people need someone to settle and steady the seat while you learn how to push the legs up and down and how to steer.”
He’s convinced that as long as there are people who need to learn about databases, Percona will remain valuable to those customers: “We’ve been around long enough to know where to steer around the potholes and to avoid going up the hills.”
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)