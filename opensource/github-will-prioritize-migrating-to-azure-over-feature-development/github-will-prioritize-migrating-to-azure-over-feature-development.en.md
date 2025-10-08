After acquiring GitHub in 2018, Microsoft mostly let the developer platform run autonomously. But in recent months, that’s changed. With GitHub CEO [Thomas Dohmke leaving the company](https://thenewstack.io/github-loses-its-ceo-and-independence/) this August, and GitHub being folded more deeply into Microsoft’s organizational structure, GitHub lost that independence. Now, according to internal GitHub documents The New Stack has seen, the next step of this deeper integration into the Microsoft structure is moving all of GitHub’s infrastructure to Azure, even at the cost of delaying work on new features.

In a message to GitHub’s staff, CTO Vladimir Fedorov notes that GitHub is constrained on capacity in its Virginia data center. “It’s existential for us to keep up with the demands of AI and Copilot, which are changing how people use GitHub,” he writes.

The plan, he writes, is for GitHub to completely move out of its own data centers in 24 months. “This means we have 18 months to execute (with a 6 month buffer),” Fedorov’s memo says. He acknowledges that since any migration of this scope will have to run in parallel on both the new and old infrastructure for at least six months, the team realistically needs to get this work done in the next 12 months.

To do so, he is asking GitHub’s teams to focus on moving to Azure over virtually everything else. “We will be asking teams to delay feature work to focus on moving GitHub. We have a small opportunity window where we can delay feature work to focus, and we need to make that window as short as possible,” writes Fedorov.

While GitHub had previously started work on migrating parts of its service to Azure, our understanding is that these migrations have been halting and sometimes failed. There are some projects, like its data residency initiative (internally referred to as Project Proxima) that will allow GitHub’s enterprise users to store all of their code in Europe, that already solely use Azure’s local cloud regions.

“We have to do this,” Fedorov writes. “It’s existential for GitHub to have the ability to scale to meet the demands of AI and Copilot, and Azure is our path forward. We have been incrementally using more Azure capacity in places like Actions, search, edge sites and Proxima, but the time has come to go all-in on this move and finish it.”

GitHub has recently seen more outages, in part because its central data center in Virginia is indeed resource-constrained and running into scaling issues. AI agents are part of the problem here. But it’s our understanding that some GitHub employees are concerned about this migration because GitHub’s MySQL clusters, [which form the backbone of the service](https://github.blog/engineering/infrastructure/upgrading-github-com-to-mysql-8-0/) and run on bare metal servers, won’t easily make the move to Azure and lead to even more outages going forward.

In a statement, a GitHub spokesperson confirmed our reporting and told us that “GitHub is migrating to Azure over the next 24 months because we believe it’s the right move for our community and our teams. We need to scale faster to meet the explosive growth in developer activity and AI-powered workflows, and our current infrastructure is hitting its limits. We’re prioritizing this work now because it unlocks everything else. For us, availability is job #1, and this migration ensures GitHub remains the fast, reliable platform developers depend on while positioning us to build more, ship more, and scale without limits. This is about ensuring GitHub can grow with its community, at the speed and scale the future demands.”

For some open source developers, having GitHub linked even closer to Microsoft and Azure may also be a problem; though for the most part, some of the recent outages and rate limits developers have been facing have been the bigger issue for the service. Microsoft has long been a good steward of GitHub’s fortunes, but in the end, no good service can escape the internal politics of a giant machine like Microsoft, where executives will always want to increase the size of their fiefdoms.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)