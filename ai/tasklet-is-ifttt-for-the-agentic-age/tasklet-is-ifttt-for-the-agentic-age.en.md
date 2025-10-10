There are plenty of tools on the market now that let you build AI agents. Maybe you’ve used AWS AgentCore, Crew.ai, n8n or even [OpenAI’s Agent Builder](https://thenewstack.io/openai-launches-a-no-code-agent-builder/), which launched earlier this week.

[Tasklet.ai](https://tasklet.ai/), which is [launching](https://tasklet.ai/release-notes) out of beta today, is nothing like those.

Instead of using code or a graphical drag-and-drop interface, you create your agent by chatting with it. Built by the team behind the [Shortwave email client](https://thenewstack.io/how-shortwave-wants-to-reinvent-email-with-ai/), Tasklet also focuses more on personal and team productivity than building enterprise agents backed by complex data pipelines (though it’s most definitely also meant to be a business tool as well, with a number of enterprise features like logging, security controls and cost management on the roadmap.

To me, it feels more like a cross between an automation service like IFTTT or Zapier (thanks to a focus on automatically triggering workflows) and an agent builder.

[![A screenshot of the Tasklet AI interface.](https://cdn.thenewstack.io/media/2025/10/93590ca0-tasklet-2.png)](https://cdn.thenewstack.io/media/2025/10/93590ca0-tasklet-2.png)

As Tasklet/Shortwave CEO [Andrew Lee](https://www.linkedin.com/in/startupandrew/) told me, the team had worked on this idea for a while, but the focus was on adding some of this functionality to the Shortwave email client, which has an AI chat built in. Users kept telling the team that they regularly wanted to run the same queries without having to type them into the chatbox over and over again. As the team worked on this, they realized that what they were building could be a more general-purpose tool, especially now that the models had gotten so much better.

“I think the thing that we figured out is, if you look at Zapier or n8n or even the thing OpenAI came out with on Monday, their AgentKit stuff, all of them have AI features, but it’s a code-defined workflow that wraps the whole thing and then the AI is inside that,” Lee explained, “If you invert that and you say, well, what if the workflow goes away? And you just let the agent reason about what to do. And I think the argument in the past was: it’s not reliable enough because the models aren’t smart enough. But I think the models are smart enough now. “

## Triggers

To kick off a workflow, Tasklet uses triggers. That could be an action or event within an application, such as a new email arriving in Gmail, a new contact being added in HubSpot, a timer (every 15 minutes), or you could set up the agent to respond to webhooks from external services.

## Building Workflows

In practice, this means the workflow of building an agent is as simple as describing what you want in the chatbox. Maybe you want to kick off a given workflow when you flag an email in Gmail as a to-do list item. This could involve checking your inbox for previous emails on this topic, searching the web for more info, and then compiling everything and dropping it into a Todoist task. Or you could have Tasklet send out a briefing document an hour before every meeting on your calendar and send that to Slack.

[![A screenshot of the Tasklet AI setting up a Gmail integration.](https://cdn.thenewstack.io/media/2025/10/ce105dd6-tasklet.png)](https://cdn.thenewstack.io/media/2025/10/ce105dd6-tasklet.png)

I have it set up to send me a morning briefing about the emails that came in during the night, for example. But you can easily think about building a workflow that automatically updates HubSpot when you get an email from a new contact that isn’t in your CRM yet. Or if you’re a developer, you can set up an agent that looks at the work you’ve logged in GitHub or Linear, compiles it, and creates a post in Slack to update your manager.

The agents will reason over the task, retry when something fails and, unlike more brittle workflow automation tools, automatically adapt when something changes.

The agents will obviously work in the background, but while you are setting them up, you can always see their reasoning and, if necessary, adjust your prompt.

As Lee told me, Tasklet can connect to thousands of applications out of the box, thanks to using [Piepdream](https://pipedream.com/) as its integrations service.  The service can also connect to any MCP server, but he also noted that these days, the models are so good at working with APIs that it’s often easier to just do that.

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

## No API? Tasklet Will Use a Computer?

One of Tasklet’s niftier tricks, though, is that it has a built-in computer-use agent, too, which the company built itself. When the agent needs to use a browser — maybe because no API is available or because the built-in web browser tool gets blocked — Tasklet spins up a virtual machine (using Ubuntu) in Google’s cloud and, using computer vision, starts browsing for you.

That computer persists across sessions, so if you log in to a service there, the agent will be able to use it again later. That’s always going to be slower than using an API, but it works. I noticed the computer also gives you access to a terminal, so there’s virtually no limit to what you could do with it.

[![](https://cdn.thenewstack.io/media/2025/10/97705374-screenshot-2025-10-09-at-9.32.55%E2%80%AFam.png)](https://cdn.thenewstack.io/media/2025/10/97705374-screenshot-2025-10-09-at-9.32.55%E2%80%AFam.png)

Running all of these agents doesn’t come cheap. There is a lot of reasoning to do and that burns up quite a few tokens. Still, Tasklet offers a free but limited tier that, at least for the time being, uses the same model as the paid tiers.

That [free tier](https://tasklet.ai/pricing) does not come with access to computer usage, though, and you’ll likely run into your daily usage quota quite regularly. On the free tier, you also can’t opt out of sharing your chats with the Tasklet team.

Paid plans start at $35/month, with higher usage limits, the usage of one computer use instance, the ability to opt out of sharing data with Tasklet and higher upload limits for when you want to work with files. At the $100/month and $250/month tiers, all of those limits will go up and over time, Tasklet will also give users access to smarter language models.

“The reality is it is super expensive to run,” Lee told me. “And basically, we just charge a lot. We have a bunch of the beta users that are already on the [more expensive] plans, and the pitch I basically make to a business user is this is going to be way more expensive than using a Zapier or something like that, but it’s going to be way more powerful.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)