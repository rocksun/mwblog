Vercel recently released a new open source tool called [json-render](https://json-render.dev/) that signals a step toward generative user interfaces (UI), a term Vercel coined for AI-generated web interfaces.

“What if, instead of just generating text, the LLM [large language model] could give us UI on the fly?” [Guillermo Rauch](https://www.linkedin.com/in/rauchg/), the founder and CEO of Vercel, asks *The New Stack*. “We’re basically plugging the AI directly into the rendering layer.”

AI and infrastructure will soon be able to support [generative UI](https://thenewstack.io/a-guide-to-generative-ai-for-devops-team-managers/), he says. Json-render is one piece of the puzzle.

Developers can use json-render to define the AI guardrails, such as what components, actions, and data bindings the AI can use. Then, end users can describe what they want in natural language through an AI prompt. The AI then generates JSON and renders it progressively as the model responds.

Rauch calls it a “very disruptive technology” because it bypasses that step of producing the software. It’s been deployed as part of Vercel Labs, which is for Vercel’s experimental projects. It’s considered an early research prototype, but the technology is already “very sound,” he says.

One developer was able to run json-render on Quinn, a low-parameter, open source model locally deployed, Rauch says.

“If you extrapolate from here, you could imagine a world where you open a website and UI just generates itself spontaneously for you using json-render,” he says. Think about it as a piece of infrastructure.

“It enables any company to take the AI and convert it into UI, and it can be plugged into systems,” he says. “Again, it’s experimental for now, but if you wanted to embed this generative UI capability into a system, you would use json-render.”

## Json-render under the hood

Json-render is a tool decades in the making, according to Rauch. He credits Vercel Software Engineer [Chris Tate](https://www.linkedin.com/in/ctatedev/) for his work on the tool, adding that json-render involved 10 years of thinking about the generative UI challenge, even before LLMs.

Json-render has an opinionated set of predefined components that give the AI the freedom to compose.

“We don’t want the AI to get so creative that it changes your brand guidelines, it changes your color system if it is something that doesn’t look good,” Rauch says. “The engineer will have the job of curating the brand identity, look, and feel of the system that’s being rendered.”

It can even be used to build game UI on demand, he adds. It’s model- and framework-agnostic, he adds, so it works with your JavaScript framework of choice.

Rauch envisions a web where users go to their favorite e-commerce site and it automatically reminds the user of past orders, updates the user on shipping, or offers customized product recommendations.

“It basically automates the job of the programmer, even an AI-powered programmer, of creating these UI rules. It just does it all in the math,” he says.

## How should frontend developers prepare?

Rauch believes technology is “very close” to enabling generative UI — he predicted we’ll see glimpses of generative UI this year — so I asked where that leaves frontend developers?

Rauch has a warning for frontend developers: Focus on shipping agents.

“Maybe a bit of a warning siren to enterprise and developers, etc., [is] if you don’t start shipping agents, you might miss out on the internet of tomorrow,” he says. “You might get outcompeted. You might not be able to plug into the new protocols.”

He points to [Google](https://cloud.google.com/?utm_content=inline+mention)’s recent announcement of UCP, a protocol for e-commerce, as one example of a protocol that developers will want to “plug into.”

> “I would still encourage people to learn to use JavaScript. But my advice would be, target the internet of tomorrow. Try to deploy an agent. Find how these models work. Try to experiment with json-render.”
>
> **— Guillermo Rauch, Vercel CEO and co-founder**

While developers won’t be needed to build UIs, they still have a role to play in defining agentic behavior. Shopify CEO [Tobias Lütke](https://ca.linkedin.com/in/tobiaslutke) calls this [context engineering](https://www.linkedin.com/posts/mattpaige_the-shopify-ceo-has-done-it-again-coining-activity-7341816822641377281-A6Fm/).

“Engineers will take a step back, and instead of focusing so much in the UI layer, they’ll focus on the behavior of the agent, making sure it has the right data, making sure it has the right context, setting up evaluations,” Rauch says. “Maybe the next step of industry will be taking a step back and focusing more on that engine, rather than the last mile UI.”

And JavaScript? Rauch notes the popular language has survived every large generation of software. He predicts it will survive this shift to generative UI as well.

“When the cloud and serverless happens, JavaScript played a central role. When server rendering happens, and rendering moves back to the server, JavaScript played a central role,” he says. “Now we’re seeing this with the AI SDK. The easiest way to create an agent today is JavaScript. Again.

“I would still encourage people to learn to use JavaScript. But my advice would be, target the internet of tomorrow. Try to deploy an agent. Find how these models work. Try to experiment with json-render.”

## Vercel’s AI long game

Vercel has released a number of AI tools in the past year, including the AI cloud, the AI SDK, and an AI gateway. I asked Rauch whether these piecemeal offerings were adding up to an overarching strategy.

> “Chapter two of Vercel will be dominated by tokens and agents. We call that the AI cloud.”
>
> **— Guillermo Rauch**

“Yes, for sure,” Rauch says. “Chapter one of Vercel was dominated by pages and pixels. We called it the frontend cloud.

“Chapter two of Vercel will be dominated by tokens and agents. We call that the AI cloud. So the AI cloud, which I actually [wrote about on my blog](https://rauchg.com/2025/the-ai-cloud), is this idea that you’re going to need new services, you’re going to need new frameworks, you’re going to need new standards.”

With the AI SDK, Vercel created a lot of the plumbing that allows it to take a model and stream it to UI, Rauch adds.

“One important thing that needs to be mentioned is over the last few years, we’ve been investing in the infrastructure to switch from one shot — you go to a website and you get it all at once — to this idea that you can stream over time,” he says. “It was an enabling technology.”

Increasingly, he says, the company has seen AI agents deployed on its platform or on [Vercel Sandbox](https://vercel.com/docs/vercel-sandbox), which allows developers to run arbitrary code in isolated, ephemeral Linux VMs.

“Agents need a place where we can fully trust them,” he explains. “They can make mistakes, so we need to create a sandbox around their behavior.”

This is a continuation of what Vercel has tried to do from the beginning, which is to democratize access to cloud services while removing all the headaches, such as configuration, he adds. Rauch calls this the self-driving infrastructure.

“If you use [AWS](https://aws.amazon.com/?utm_content=inline+mention) or if you use Google Cloud, it’s like driving a manual car,” he says. “Vercel is like the Waymo of the cloud or the Tesla — full self-driving.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)