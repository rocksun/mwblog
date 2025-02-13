# How Developers Are Using Bolt, a Fast Growing AI Coding Tool
![Featued image for: How Developers Are Using Bolt, a Fast Growing AI Coding Tool](https://cdn.thenewstack.io/media/2025/02/65d91009-getty-images-uyefhxjj4xs-unsplashb-1024x576.jpg)
Last month StackBlitz, formally a [Cloud Development Environment](https://thenewstack.io/stackblitz-launches-codeflow-and-announces-figma-investment/) (CDE), [rebranded itself](https://x.com/boltdotnew/status/1881185271548657965) to Bolt, an AI-based online web app builder. Why the sudden pivot and how is [Bolt](https://bolt.new/) faring against a plethora of other [AI coding tools](https://thenewstack.io/whats-ahead-for-ai-assisted-coding-open-source-and-more/) now on the market? I spoke with CEO [Eric Simons](https://www.linkedin.com/in/eric-simons-a464a664/) to find out.

Simons admitted that launching an AI developer tool has saved StackBlitz from the fate of most Silicon Valley startups. “If we didn’t kind of figure out how to change the trajectory of the company, we were going to start spinning down the company,” he said.

By Simons’ account, StackBlitz had “a lot of developers using it and […] we were selling to enterprises, but it was not venture scaling.” He says that StackBlitz, the CDE tool, had less than a million dollars in annual recurring revenue (ARR) after “seven years in the game.” So they needed to do something, especially given the sudden rise in [AI-assisted coding](https://thenewstack.io/top-5-ai-engineering-trends-of-2024/) over the past couple of years.

“So Bolt was kind of like the last experiment that we basically had on the books, before we were gonna start, you know, looking at selling the company, or…whatever,” Simons said.

Bolt launched last October and seems to have had a remarkable growth spurt in its first months of operation. Simons says that Bolt “did 20 million of ARR” after just two months — “and we’ve continued to grow since then.”

According to [a thread on X](https://x.com/ericsimons40/status/1882106925795696674) last month, Bolt now has 2 million registered users.

## Other CDEs Have Pivoted to AI Coding
It turns out StackBlitz isn’t the only CDE company to have recently pivoted to AI dev tooling. In December, CodeSandbox — a CDE [I profiled in November 2022](https://thenewstack.io/the-race-to-be-figma-for-devs-codesandbox-vs-stackblitz/), a few weeks after I’d profiled StackBlitz — was [acquired by AI Together](https://codesandbox.io/blog/joining-together-ai-introducing-codesandbox-sdk), a heavily VC-funded company. It immediately launched a new product, CodeSandbox SDK, which allows you to “programmatically spin up (AI) sandboxes.”

“CodeSandbox started back in 2017 as a React playground,” [commented the company](https://x.com/codesandbox/status/1867233573037572437) on their X account. But despite growing to respectable 4.5 million monthly users in 2024, it saw bigger opportunities in the AI space: “As the world entered the era of AI, we found that our VM sandboxes made for a perfect solution for executing code in agentic workflows.”

Another CDE I profiled in 2022, Gitpod, released its AI-based product [last October](https://www.gitpod.io/blog/introducing-gitpod-flex): Gitpod Flex, described as an “automation platform.” Among the automations featured is the ability to configure “LLM-powered agentic workflows.”

“…back in May, we got kind of a sneak peek of Sonnet 3.5, and I was like, woah, this is gonna change everything here, because it’s actually outputting really good code.”

– Eric Simons, StackBlitz / Bolt CEO
For his part, Simons told me that the idea for Bolt came about a year ago, when [generative AI hype](https://thenewstack.io/more-than-an-openai-wrapper-perplexity-pivots-to-open-source/) was forcing nearly every Silicon Valley company to integrate AI into their product. The core of StackBlitz had always been its proprietary WebContainers technology, which [has been described](https://blog.stackblitz.com/posts/introducing-webcontainers/) as allowing you “to create full-stack Node.js environments that boot in milliseconds.” So the initial idea was to marry that with ChatGPT. Simons takes up the story from early last year.

“We were using OpenAI’s models for that, and they just weren’t good enough to actually output good working code […] that just didn’t have a ton of errors. So we put the idea on the shelf. And then back in May, we got kind of a sneak peek of [Claude] Sonnet 3.5, and I was like, woah, this is gonna change everything here, because it’s actually outputting really good code. And so we ended up green-lighting the project. It [what became Bolt] started in July, and then we launched in October. And then it’s just taken off like wildfire since then.”

## How Devs Are Using Bolt
A CDE is basically a browser-based IDE. So pivoting from that to a browser-based IDE *with AI functionality* makes a lot of sense in today’s environment. But it’s not just assisting developers with AI generated suggestions, as the first wave of AI coding products did — GitHub Copilot, Cursor, Tabnine, and others. Bolt promises to take over the coding of a web app or website almost entirely.

In my own tests, I was able to spin up a brand new Astro blog using one of the default prompts in Bolt (Netlify CEO Matt Biilmann [did the same thing](https://biilmann.blog/articles/i-built-a-blog/)).

Within a minute or two, Bolt had created a whole repository for an Astro blog, which I then deployed for free to Netlify. Ok, this process is not that different to cloning a project on GitHub. But I was then able to make several bespoke changes to my Astro blog, using the AI chat interface, and Bolt seemed to handle this well. There were errors along the way, but Bolt fixed them ok.

I’m just an amateur developer, though. I was curious about the usage pattern with professional developers on Bolt. Are they starting apps in Bolt and then moving the code to a full IDE, like VS Code, to finish it?

Firstly, Simons noted that over half of their users are like me — not professional developers. “They’re PMs [product managers], designers, entrepreneurs, etc.” Later in the conversation, he said that around 60-70% of Bolt users are “non-technical.”

“In the developer case, a lot of people are using this as a crazy-fast, zero-to-one scaffolding tool for generating UI designs, prototypes, etc.”

– Simons
But in terms of actual developers, Simons has identified a few usage patterns. Sometimes developers are building their entire app in Bolt, he said. He’s also seen what noted AI expert Andrej Karpathy (one of the founders of OpenAI) has called “[vibe coding](https://x.com/karpathy/status/1886192184808149383).”

“Developers who are starting to let the AI build stuff, and then you’re just sitting there, just clicking ‘accept changes’ or whatever,” explained Simons.

But Bolt users are also going back and forth between Bolt and their usual IDE.

“In the developer case, a lot of people are using this as a crazy-fast, like, zero-to-one scaffolding tool for generating UI designs, prototypes, etc, and then taking that into Cursor [or] VS Code to keep working on it,” Simons said. “Then you bring it back to Bolt […] to add major features, or whatever.”

## Replacing Figma?
When I last interviewed Simons, in October 2022, he likened his company at that point to Figma — the company that had improbably built a “[PhotoShop in the browser](https://www.sequoiacap.com/article/dylan-field-figma-spotlight/)” app which [Adobe nearly acquired](https://thenewstack.io/adobe-buys-figma-what-does-this-mean-for-web-standards/) for $20 billion (the deal was [later cancelled](https://www.theverge.com/2023/12/18/24005996/adobe-figma-acquisition-abandoned-termination-fee) after pressure from EU and UK regulators). “StackBlitz is very much the development analogy of what Figma did for design,” Simons told me in 2022.

What he was getting at is that StackBlitz did everything in the browser, [just like Figma](https://thenewstack.io/the-race-to-be-figma-for-devs-codesandbox-vs-stackblitz/). What’s fascinating about Bolt, compared to what StackBlitz was pitching a couple of years ago, is that the Figma comparison has now been blown out the water.

“We’ve entered a new era where it’s now faster to make working prototypes with code, than design them in Figma,” claimed Simons in [a tweet](https://x.com/ericsimons40/status/1882106931479031841) earlier this month.

“What you traditionally would be doing in Figma for making a prototype, […] it’s faster to do it in code.”

– Simons
In our current discussion, Simons softened that stance a little (perhaps because Figma is an investor in StackBlitz). But he still insists that Bolt replaces at least some of the prototyping process.

“What you traditionally would be doing in Figma for making a prototype, […] it’s faster to do it in code. That’s actually the better way to do it because it’s real, you know? And you can actually play around with it, right?”

This makes total sense. Why bother designing a prototype user interface when you can just describe to Bolt — using words — what you want your app to look like?

## Token Costs
It should be noted that although you can start Bolt for free, you soon find yourself needing to buy “tokens” to continue developing your project (this was the case for my Astro blog!). Pricing starts at $20 per month for a “Pro” account (10 million tokens) and goes up to $200 per month for 120 million tokens. However, it’s not entirely clear how many tokens you’ll need for a project. Opinions in [Bolt’s Reddit community](https://www.reddit.com/r/boltnewbuilders/) varied widely on this.

Some of Bolt’s users are taking the hybrid approach — using both Bolt and their full IDE — perhaps partly due to the cost. Commented this user [on Reddit](https://www.reddit.com/r/boltnewbuilders/comments/1iex3lt/comment/maekb67/):

“There is no reason to use Bolt to create the entirety of the project. I have Bolt create the framework and get the style right, then I take the project to VSCode or Current and finish it there, with DeepSeek, OpenAI, Claude.”

In any case, Bolt is another potential AI assistant tool for developers — professional or amateur — to consider. There are quite a number of these tools now, such as [Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/), Devin and [Solver](https://thenewstack.io/self-driving-software-solver-launches-autonomous-ai-coder/). So you should give a few of them a go and see which one suits you best.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)