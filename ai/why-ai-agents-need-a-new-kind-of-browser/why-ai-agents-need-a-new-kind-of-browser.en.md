AI agents need to browse the web, but traditional browser automation tools are too brittle for the job. That’s the problem second-time founder [Paul Klein IV](https://www.linkedin.com/in/paulkleiniv/) is solving with [Browserbase](https://www.browserbase.com/) and its open source [Stagehand](https://www.stagehand.dev/) framework: creating a browser tool that AI agents can use effectively.

“I really love thinking about, how can I help power the future of software with primitives that power that software?” Klein explained on the fourth edition of our The New Stack Agents podcast. “I’ve done that at Twilio. I’ve done that at Mux. Now with Browserbase we’re doing it again, but in a much newer category, which is this idea of the agentic browser, or a browser that can be controlled by AI.”

## A Headless Browser for Smart AI Agents

Traditional headless browser tools built for testing are notoriously brittle. Tests break when a button moves even a few pixels. But AI agents need something entirely different.

“As developers built more software that exists online, more websites and web applications, they needed a way to test those applications,” Klein explained when asked about the history of headless browser, that is, browsers without the typical user interface around them. “Turns out, it’s quite tedious after shipping a feature to go into your new feature on a website and click all the buttons 100 times, and to continue to do that every time you change a feature. So developers started thinking about ways that, okay, now we have people using browsers, but for our software testing workflows, we need to have computers. […] So let’s make a browser that can be controlled by some code.“

In a way, he explained, those tools were brittle by design because when a change breaks a web app, the developer needs to know about it. Stagehand, Browserbase’s open-source tool, take a different approach. Klein noted that Stagehand was built to be more durable than existing frameworks because it can handle those kinds of changes on a site — and handle the fuzziness of LLM prompts.

“In the old world, you can say: click the Login button. It’s the fifth button on the page. The color is red. It says ‘login’ on it,” Klein explained. “In the New World, you can tell AI: hey, I want to click the login button. You figure that out for me. And if the login button changes color, maybe it changes position, maybe changes from ‘login’ to ‘sign in,’ you can still find the button on the page using large language models.”

This shift unlocks massive potential, Klein argues. “In the old world, if you wanted to automate 100 websites, you have to write 100 scripts. In the new world with AI, you can write one script that can control hundreds or thousands or millions of websites.”

## Building a Browser Infrastructure for the AI Future

“At Browserbase, we help AI agents interact with the Internet,” Klein said. “So we provide the browser tool, which is an important tool, to let AI work on your behalf. When you think about all the work that you and I do every day, a lot of it happens on a browser, interacting with websites on the internet. So if we want to have this future where AI is going to help work on our behalf, we have to give AI the tools to interact with the work we already do, and that is the web browser.”

Klein’s vision extends beyond just making browsers smarter. He sees a future where the interface between humans and software fundamentally changes. “I think the future of software isn’t actually you’re thinking about browsers at all. You’re thinking about more powerful buttons,” he said. “When I say, submit my taxes, it’s not going to give me a PDF I print out. It’s just going to go to the website and do it for me.”

But building this infrastructure isn’t trivial. “The browser itself was not designed to run on a server. Headless has always kind of been a hack,” Klein admitted. The technical challenges in building a browser tool for agents are numerous, ranging from handling emojis and codecs to managing time zones and locales across distributed systems.

## What Do You Do When AWS Calls?

We recorded the podcast on the same day AWS announced its Bedrock AgentCore service for running AI agents in production and at scale. This service includes a browser tool and as it turns out, Klein had a meeting with AWS this April to discuss a potential partnership. On X/Twitter, Klein had [been pretty outspoken](https://x.com/pk_iv/status/1945183371987935732?s=46) about what he thought of this meeting. “We’re not worried. It’s lacking everything that makes Browserbase great,” he wrote. “But three months ago AWS ambushed us with a ‘partnership meeting’ to try steal our secrets. We saw right through it,” he wrote on X. 

Naturally, we asked him about a few more details about this meeting.

“I was a little disappointed to see some of the behavior here from AWS, but it’s par for the course. It’s not illegal. You know, it’s certainly not illegal to try and get a meeting and ask me about their product, and in the end, I told them the same things I’m telling you now: the thing that makes Browserbase great is our community of developers who love us, the people who contribute to Stagehand, and our complete obsession with building this next category defining company that’s going to allow all types of AI to go out and automate the web.”

As for the meeting itself, Klein said it reminded him of a scene in the Silicon Valley show “where the Pied Piper folks get pulled into a meeting and all of a sudden there’s a whiteboard, and they’re asking you to write down how your architecture works.”

You can find the full episode [in our podcast feed](https://thenewstack.io/podcasts/) and [on YouTube](https://www.youtube.com/watch?v=SBEfTwNqGik).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)