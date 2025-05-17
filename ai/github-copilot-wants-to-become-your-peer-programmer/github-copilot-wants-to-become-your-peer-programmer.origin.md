# GitHub Copilot Wants To Become Your Peer Programmer
![Featued image for: GitHub Copilot Wants To Become Your Peer Programmer](https://cdn.thenewstack.io/media/2025/04/7b5ec6b7-mvimg_20171129_165458-1024x768.jpg)
GitHub first [introduced](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/) its now ubiquitous Copilot back in 2021. At the time, the Microsoft-owned company described it as “a new AI pair programmer that helps you write better code.” That overall mission of augmenting developers and using AI to do away with much of the day-to-day busy work hasn’t changed. But as GitHub CPO [Mario Rodriguez](https://www.linkedin.com/in/mariorodriguez3/) told me during an interview on the sidelines of [Google’s Cloud Next](https://thenewstack.io/event/google-cloud-next-25/) conference in Las Vegas earlier this month, the company is now squarely in phase two of the Copilot project.

“We named this Copilot for a reason,” he said. “The idea was, hey, the human is at the center, and we’re going to go and augment this human with the power of Copilot to take out the toil, help them code faster, increase productivity, all of those things. And I think wave one of that strategy played out over two plus years — and we’ve been very successful at that.”

In a separate interview, shortly after Microsoft announced its latest quarterly earnings, GitHub CEO [Thomas Dohmke](https://www.linkedin.com/in/ashtom/) noted that Copilot now has 15 million users, a number that is in part driven by GitHub opening up [the free Copilot tier](https://thenewstack.io/microsoft-makes-github-copilot-free-in-vs-code/) late last year.

## 2025: The Year of SWE Agents
Almost exactly a year ago, GitHub launched Workspace, its take on letting developers code with natural language — long before “[vibe coding](https://thenewstack.io/vibe-coding-is-here-how-ai-is-reshaping-the-software-developer-profession/)” entered the mainstream. Rodriguez admits that GitHub may have been a bit too early with this, but he also clearly believes that this is where things are going, with a large dose of AI agents added to the mix.

In February of this year, GitHub announced [Project Padawan](https://github.blog/news-insights/product-news/github-copilot-the-agent-awakens/), Copilot’s autonomous SWE agent, which in many ways takes the Workspace concept to the next level.

“We’re now entering, in my opinion, wave two of this — the next is kind of the next evolution of what software development will be,” Rodriguez said. “This next evolution is all about agent tech, in our opinion, and it’s really taking two modalities — synchronous, by which I mean VS Code or any other tool, and be able then to use these agents to augment me. But now, through natural language, I could tell it, ‘Go, do this,’ and the agent will figure out all of the steps on it.”

This, he said, is what Project Padawan is all about. The idea here is for the system to be able to tackle multiple GitHub issues in parallel, for example, by assigning multiple issues to the agent — something an individual developer couldn’t do.

“I think it’s fair to say 2025 is the year of the SWE agent, where for more and more tasks, the developer can either synchronously or asynchronously work with an agent,” Dohmke said.

## Peer Programming
Currently, in VS Code, the agent mode handles the synchronous tasks, which Dohmke likened to working with a pair programmer, as it’s essentially a back and forth between the Copilot and the developer.

The original Copilot, Dohmke noted, was mostly a tool for pair programming with the AI model.

“I think the original Copilot, first with autocompletion, then with chat, solved that scenario, and Agent Mode extends it to a degree where you are effectively handing the keyboard to the other person, have them write for a while, but you’re still in charge from [the perspective of] how the roles are within the pair,” Dohmke said.

But with Project Padawan, that now changes. Dohmke noted how most developers work in teams, and how they have peers within those teams that they communicate with throughout the day, while the manager (or Scrum master) assigns work. Once you bring SWE agents into the loop, the developer becomes a peer of multiple agentic developers, Dohmke believes. Those agentic developers may even work together with a site reliability engineering (SRE) agent, for example, who monitors the health of a company’s infrastructure and then assigns GitHub issues to the SWE agent when things go awry.

![](https://cdn.thenewstack.io/media/2025/05/a2c33c92-img_20180924_115324-scaled.jpg)
Image credit: Frederic Lardinois/The New Stack.

“That’s the peer programmer, where you basically become peers with a group of agents, or, as I like to call it, the orchestra of agents,” Dohmke said. “Now, they’re all still working on the behalf of a human developer, right? That’s the conductor of the orchestra, because at the end of the day, these agents still need to get their work assigned to them, and at the end of the process, somebody needs to review that.”

Right now, Rodriguez said, the team is fully focused on executing on this agent vision, which has in part become possible because the models themselves have become so much more sophisticated since GitHub first demoed Workspace. Rodriguez noted, for example, that in the early days of Workspace, GitHub — and the user — were handling the planning stages. But now, with the models having become so much better at planning themselves and also having the ability to call tools, the models themselves can handle most of this.

“Now these models can go and pick the right tools a lot better than before. There’s still more that needs to happen there, but once you get something that is very good at planning, very good at picking the right tools, and then they continue to get better at code writing and understanding — once you’ve got those three components, you could unlock things that didn’t exist before,” he said.

That’s where Copilot’s recently [launched](https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode) Agent Mode comes in. It can create apps from scratch or help developers debug, refactor or extend their existing applications. (It can create documentation, too.)

With Microsoft’s annual Build conference right around the corner, chances are we’ll hear more about the state of Project Padowan in the coming days.

## Copilot Competitors
Obviously, GitHub isn’t the only company in this game and even though it was among the first to launch AI code completion tools, companies like Cursor, replit, Windsurf and others may almost have as much mindshare today as GitHub has in this space.

“I think the place where we will shine, it’s on context,” Rodriguez said. “If you pass the model the right context, the model does a pretty good job. If you pass the model the wrong context, it does not.”

For GitHub, this context isn’t just the code but also what it knows about how people on a team collaborate. “We already inherently have essentially a people graph and a work graph as well. So the combination of this code graph, people graph, and then, as we expand into the application graph as well, I think it’s going to give us a way to have context, and it’ll be really interesting to try to see what Copilot can do with that,” he said.

Rodriguez also notes that he isn’t worried about competitors. “I think that’s a healthy thing for humanity. That’s the normal modus operandi of being in this space. And I think the North Star for Thomas [Dohmke] and I going through this is: can we create the best product? And if we create the best product that is solving the customer needs, then that is success for us and that’s what we continue to be obsessed about.“

The fact that Copilot is also available inside all of the popular IDEs, as well as GitHub.com itself, is another area where Rodriguez believes the company has a major advantage.

## How To Price a More Advanced Copilot?
In the early days, Copilot set the baseline for how to charge for a service like this by going with a $10/month flat fee. Over time, it added additional tiers, but earlier this year, when it made a number of higher-end models available in Copilot, it switched things up a bit by putting a limit on “premium model requests.” For these, users will receive a limited allotment of requests (300/month for Pro users and 1,500/month for those on the new $39/month Pro+ plan). Additional requests will cost $0.04 per request.

“That’s one way that we’re going,” Rodriguez said about these changes. “That is mainly to support this synchronous Agent Mode and asynchronous Agent Mode as well. So I think that’s kind of a direction we’re going. […] We always take a look at how we should evolve our business model, and where is it that we want to evolve it, and how we want to evolve it, and all those things. Right now, that’s where we’re going. There’s a license and then a consumption model past that.”

## What Will Software Development Look Like in a Few Years?
GitHub and its executives often talk about how they want to get to a billion users and make programming available to virtually anyone. Like its competitors, the way the company plans to get there is by using natural language, with the large language model (LLM) as an intermediary between the request and the actual code.

“We took a big bet on natural language in 2021,” Rodriguez said, “The beauty of Copilot at the very beginning, by the way, was not that it could go ahead and write some code. IntelliSense already could do that at that moment and autocomplete things. The thing that blew me away in 2021 was the fact that you could have a comment, type something in the comment, and the machine understood it and then was able to write something big after that. I had never seen that in my life, with that level of accuracy — and it wasn’t highly accurate, maybe 15 or 20 percent — but no MLOps pipeline ever had done that. So I think natural language is the unlock.

“The thing that needs to keep up is human interfaces to be able to then unlock what you want to get done,” he added. “The cool thing also about natural language is you could speak in your native language and accomplish things in your native language, which in programming, that hasn’t been the case.”

Rodriguez does not seem all that worried about what this means for the overall coding skills, especially for junior developers.

“I think for us, what needs to happen is more of a redefinition of what a software developer is, and this is why it’s 1 billion for us,” he said. ”If you think about it, the IDE today is this thing called professional developers, which I think limits the acceleration of human progress. In my opinion, you should go and look at what happens if 10% of the world population can become software developers?”

But what happens when these developers can’t read and understand the code that the models wrote for them? Rodriguez believes that may be a short-term problem, but “what is reading the code in the future, like, 100 years?” he asked. “And why does it need to be so static? […] I think you do have to bet on humanity and there will be an evolution.”

When I asked Dohmke a similar question, he offered a similar answer, but also added that in his view, the difference between junior and senior developers is not the amount of code they’re writing, but the quality of that code. And while models will likely only get better at coding over time — and may hence become more akin to senior developers themselves in some ways — they will likely continue to lack in some aspects.

“I think, fundamentally, they’re lacking what I would call craft,” he said. “And as such, they cannot actually replace the real senior developer. They’re always going to be an assistant, a helper to the senior developer that is still in charge, flying the plane or driving the software life cycle.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)