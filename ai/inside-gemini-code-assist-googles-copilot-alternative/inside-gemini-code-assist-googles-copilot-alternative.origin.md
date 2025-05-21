# Gemini Code Assist vs. Copilot: The Rise of AI Coding Agents
![Featued image for: Gemini Code Assist vs. Copilot: The Rise of AI Coding Agents](https://cdn.thenewstack.io/media/2025/05/0d27859d-google-io-gemini-1024x576.jpg)
At today’s Google I/O, the general availability of [Gemini Code Assist](https://codeassist.google/) for individuals was announced. In the lead-up to the event, I spoke to [Ryan J. Salva](https://www.linkedin.com/in/ryanjsalva/), a senior director of product management at Google Cloud, about this latest iteration of Gemini Code Assist, Google’s AI coding tool. In particular, we focused on the product’s embrace of agentic AI and its ongoing competition with Microsoft’s GitHub Copilot.

I’m not sure if you’re aware, but AI agents are the hot new thing for developers this year. Of course, I’m kidding: it’s an anomaly if a dev tool announcement these days *doesn’t* feature the word “agent”! We saw evidence of that just yesterday, when the [GitHub Copilot Coding Agent was launched](https://thenewstack.io/github-launches-its-coding-agent/) at Microsoft Build.

Gemini Code Assist agents were [announced](https://techcrunch.com/2025/04/09/gemini-code-assist-googles-ai-coding-assistant-gets-agentic-upgrades/) as a “private preview” at last month’s Google Cloud Next event. At that time, Google invited developers to [apply](https://developers.google.com/profile/badges/community/sdlcagents/gca-agents) to use “a suite of SDLC agents via Gemini Code Assist in VS Code and Firebase Studio.”

Also today, Google announced it is opening access to [Jules](https://jules.google.com/home), an AI coding agent “that does the coding tasks you don’t want to do.” (However, Jules is not part of Code Assist.)

## ‘Mixture of Agents’
Google has clearly been targeting GitHub Copilot users since late-February, when it announced a free version of Gemini Code Assist that [offered 90 times more code completions](https://thenewstack.io/google-ai-coding-tool-now-free-with-90x-copilots-output/) than its primary competitor. So I asked Salva what the difference is between how Google has approached agents technology in Gemini Code Assist, and how GitHub Copilot uses agents.

Salva replied that Copilot’s “agent mode” (he also mentioned Cursor’s Yolo Mode) resembles a single developer working through a plan alone, whereas Gemini uses a “mixture of agents” approach. This involves multiple specialized agents — for example in the roles of developer, tester, and security analyst — working together. As Salva put it, these agents are essentially “adversarial collaborators with each other, in order to check each other’s work.” He compared this to a virtual team in a shared chat room.

Gemini Code Assist agents are “adversarial collaborators with each other, in order to check each other’s work.”

– Ryan J. Salva, Google Cloud
I asked whether developers will be able to create their own agents — for example, create an “e-commerce specialist” agent?

He replied that custom agents is Google’s vision for Gemini Code Assist, but that currently they only offer predefined agents.

“We don’t yet have the ability for the developers to go and define each of their own experts and own agents, but as we head towards general availability, that is certainly the intent,” he said.

While there are no specific updates to the Code Assist agents in today’s I/O event, Google is announcing “more customization options” in Gemini Code Assist — including “more ways to customize workflows to fit different project needs, the ability to more easily pick up tasks exactly from where you were left off, and new tooling to enforce a team’s coding standards, style guides and architectural patterns.”

## Learning To Trust AI Agents
Salva gave further insight into Google’s approach to coding agents by suggesting there’s a shift happening in how developers interact with AI tools. Developers are moving from low-trust, high-oversight modes of working with AI, to “a position of increasing autonomy and increasingly high trust,” he said.

According to Salva, there are four interaction modes — each one more sophisticated than the last — that developers go through with AI.

- Predictive text, for simple code completions.
- Chat: AI-assisted conversations for coding tasks.
- Collaborative “vibe coding”: using AI to make broad, coordinated code changes.
- Agent mode: AI autonomously operating in the background, possibly making changes without direct oversight.
Obviously, number four — agent mode — is where the industry is at in the coding tools hype cycle. Where Google seems to be positioning itself is by emphasizing agents across the SDLC (software development life cycle). Or as Salva put it, “how do we bring more and more of these agents to bear to help developers effectively get their job done — not just for writing code, but also raising code quality.”

## One LLM To Rule Them All
In related news, Google also announced today that Gemini 2.5 now powers Gemini Code Assist, and that paying customers of Code Assist will get a 2 million token context window “when it’s available on Vertex AI.”

Gemini 2.5 was launched at the end of March, with Google [calling it](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/) “our most intelligent AI model” — adding that it “excels at creating visually compelling web apps and agentic code applications, along with code transformation and editing.”

That brings up another point of difference with GitHub Copilot. Gemini Code Assist, as its name implies, only uses one brand of LLM (Gemini). But GitHub Copilot offers a range of models, such as Claude 3.7 Sonnet, OpenAI o1, and Google Gemini 2.0 Flash. I asked Salva why Code Assist is limited to Gemini.

“The reason that we use Gemini models, first and foremost they are actually really good models for coding — and so we get good results out of them. And also, one of the real benefits that we have making both the tools and the models — in very, very close organizational partnership — is that we can improve the models much faster when we do it in a tight coupling with the tools themselves.”

What he’s hinting at here is that Code Assist is tightly integrated into the Google Cloud ecosystem — just like other AI products at Google. In another of [April’s Cloud Next announcements](https://cloud.google.com/blog/products/application-development/an-application-centric-ai-powered-cloud), Google announced Gemini Cloud Assist, which “provides AI-powered assistance across the application lifecycle in the Google Cloud environment.” Code Assist is slightly different, because it can also be used for free by individuals, but at the same time it is becoming a key part of Google’s enterprise cloud platform too.

## AI Agent Semantics
It remains to be seen which of Google’s or Microsoft’s AI agents are more effective for developers. Although it does seem like GitHub’s offerings are a little further along — being available now to their highest paying users. The Gemini Code Assist agents are still in a private preview.

It also struck me that Google is being a bit more cautious with how it describes a coding agent. GitHub has recently been referring to its agent technology as “[peer programming](https://thenewstack.io/github-copilot-wants-to-become-your-peer-programmer/)” — a play on words of “[pair programming](https://thenewstack.io/advance-your-devops-with-pair-programming-even-remotely/),” a more traditional IT technique. Google, on the other hand, refers to Code Assist as “a developer’s coding companion.” Perhaps I’m reading too much into it, but a “peer” implies someone or something of equal standing, whereas a “companion” is a word that can just as soon be applied to a dog as to a human (or an AI agent).

We’ll see whether AI agents turn out to be closer to a human peer or a canine companion. Regardless, we’re well and truly into the era of AI coding agents now.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)