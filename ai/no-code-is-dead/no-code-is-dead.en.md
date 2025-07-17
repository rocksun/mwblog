Once again, the [software development landscape](https://thenewstack.io/four-new-areas-where-ai-is-transforming-software-development/) is experiencing another big shift. After years of drag-and-drop, [no-code platforms](https://thenewstack.io/low-code-vs-no-code/) democratizing app creation, [generative AI (GenAI)](https://thenewstack.io/generative-ai-a-new-tool-in-the-developer-toolbox/) is eliminating the need for no-code platforms in many cases.

Mind you, I said “no code” not “[low code](https://thenewstack.io/the-highs-and-lows-of-low-code-tools/)” — there are key differences. (More on this later.)

[GenAI](https://thenewstack.io/generative-ai-in-2023-genai-tools-became-table-stakes/) has introduced the ability for nontechnical users to use natural language to build apps just by telling the system what they want done. Call it “[vibe coding](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/)” — the ability to describe what you want and watch AI generate working applications, or whatever. But will this new paradigm enhance existing no-code tools or render them obsolete?

I sought out insights from industry veterans to explore this pivotal question, revealing a broad spectrum of perspectives on where the intersection of AI and visual development is heading.

## The Technical Debt Dilemma

[David Mytton](https://www.linkedin.com/in/davidmytton/), CEO of [Arcjet](https://arcjet.com/), who has long observed the evolution of development tools, strikes a cautionary note about both traditional no code and its AI-powered successor. “I’ve always found the idea of ‘no code’ a bit odd because for anything other than trivial apps, it still requires significant engineering work to connect databases, hook up forms and understand how all the interactions should work,” he told The New Stack.

However, “I expect GenAI to make building these apps a lot faster and easier, but it’s still going to make a technical mess,” he said. “Vibe coding internal apps is going to be a huge source of technical debt in the coming years!”

This perspective highlights a fundamental tension in the democratization of software development: Speed and ease of use often come at the cost of architectural soundness.

> “I expect GenAI to make building these apps a lot faster and easier, but it’s still going to make a technical mess. Vibe coding internal apps is going to be a huge source of technical debt in the coming years!”
>
> **—David Mytton, CEO of Arcjet**

## The “Vibe-Code Killer” Proposition

[Josh Haas](https://www.linkedin.com/in/joshhaas/), co-CEO and co-founder of [Bubble](https://bubble.io/), takes a different stance, positioning his company as what he calls a “vibe-code killer.” After 13 years of building no-code tools, Bubble is now transforming into an AI company — not to replace visual development, but to create something entirely new, he told The New Stack.

He said vibe coding is fine for building prototypes, “but as soon as you try and actually build a real application on it, you’re going to discover that the AI has made some mistakes,” Haas explains. “You kind of need to understand what that code does as the app owner and creator, and I don’t think AI can substitute.”

Bubble’s solution? AI helps you build, but what it builds is expressed in the company’s visual no-code language. “You can actually understand what the AI is doing. You can tweak it yourself, and you can give AI specific feedback, not just based on the output, but based on sort of a full understanding of the internals of your application,” Haas said.

This hybrid approach acknowledges the power of AI while maintaining the transparency and control that pure code generation lacks.

## The Agent-First Future

[Amjad Masad](https://www.linkedin.com/in/amjadmasad/), founder and CEO of AI app-building platform provider [Replit](https://replit.com/), takes a more radical view, suggesting that the entire no-code versus low-code debate may become irrelevant. “I think both go away. Agents will just do the work,” he predicts, positioning AI as fundamentally different from previous approaches because “it’s more flexible and based on open source languages and libraries.”

Masad envisions a future where the distinction between coding and “no-coding” disappears, replaced by AI agents that handle the technical implementation while humans focus purely on describing desired outcomes.

## No Code’s Death Sentence?

Meanwhile, [Gordon Van Huizen](https://www.linkedin.com/in/gordonvanhuizen/), SVP of strategy at low-code platform provider [Mendix](https://www.mendix.com/), delivered perhaps the most direct verdict on traditional no code’s future. When asked whether GenAI tools eliminate the need for no code, he definitively agreed: “For no code? I definitely agree with that. You know, I think no code responded to a specific problem that existed for a given length of time, and either the nature of the [it] changes significantly to the point where you just wouldn’t call it no code anymore, or it’s gone at the end of the day,” he told The New Stack.

But Van Huizen’s critique goes deeper than simple replacement — he identifies fundamental flaws in pure vibe coding that explain why the transition won’t be straightforward. “The GenAI answer on its own is not good enough, because what you’re going to get is millions of lines of AI-written code that isn’t production-ready, isn’t hardened, has bugs and is going to be an unmaintainable nightmare.”

His concerns center on what he calls the “intent capture problem”: “In a vibe-coding world, if you’re really vibe coding, you know that intent basically evaporates into the ether. You know almost immediately you’re putting in things that probably should be in user stories somewhere …”

Van Huizen also predicted that Microsoft’s Power Platform is best positioned to dominate this evolving landscape, given its access to user data and existing productivity tool integration.

## The Visual Development Persistence

No-code platform provider [Creatio](https://www.creatio.com/)‘s approach offers a stark counterpoint to the “no code is dead” narrative. Rather than seeing AI as a replacement, they view it as an enhancement that makes visual development more powerful, not obsolete.

When directly asked, “Why do you need no code if you could just ask the AI to do everything for you?” [Burley Kawasaki](https://www.linkedin.com/in/burleyk/), chief product officer at Creatio, told The New Stack: “AI, I would argue, is actually a form of no code, right? It’s just, it’s using natural language versus maybe a visual design tool.”

Kawasaki added, “I think there are certain things that natural language is well suited for. There’re other things that the UI design tool is well suited for, especially if you are designing a pixel-perfect user interface, you want to build control of the layout, or if you want to be able to design a dashboard …”

Creatio’s “AI-native” platform embeds conversational interfaces throughout their platform while maintaining visual design tools for tasks where they’re more effective, he said.

> “AI, I would argue, is actually a form of no code, right? It’s just, it’s using natural language versus maybe a visual design tool.”
>
> **—Burley Kawasaki, chief product officer at Creatio**

## The Enterprise Reality: OutSystems’ Agent Orchestration Model

[Miguel Baltazar](https://www.linkedin.com/in/miguelbaltazar/?originalSubdomain=pt), vice president of developers at low-code platform provider [OutSystems](https://www.outsystems.com/), offered a perspective that bridges the theoretical and practical. Baltazar, a 22-year veteran of the low-code space, told The New Stack that OutSystems’ approach illustrates how established platforms are evolving to become orchestrators of AI agents rather than being replaced by them.

“AI is interestingly a little bit more disruptive, because it disrupts both the way you build applications and the applications that are built themselves,” he said. OutSystems has developed “[Mentor](https://www.outsystems.com/low-code-platform/mentor-ai-app-generation/),” a full software development life cycle assistant that can generate databases, UI and logic from requirements in minutes.

But Baltazar focuses on the “agentic AI” trend and its implications for enterprise development. “Applications started being able to have interfaces that were not meant for humans. They were not meant for backends. They were meant for agents,” he said.

The challenge, however, is that agents are imperfect: “A lot of agents, when they execute, they execute perfectly for 60 or 70% of the time, and then there’s 30% that they just either hallucinate or are not able to perform the task,” Baltazar said.

This reliability gap creates a need for sophisticated orchestration — exactly what low-code platforms excel at, he noted. “Building this orchestration, building the interface for the human interfacing with the agent to get all the data, building the [RAG](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/) [retrieval-augmented generation] context for the agent to be able to operate with the current context of the transaction … all of those things are very easily built visually.”

OutSystems and its customers are using this approach for practical applications, he said. OutSystems itself reduced support ticket submissions by 35% using AI agents orchestrated through their platform.

## The Vibe-Coding Reality Check

The OutSystems perspective also provides one of the most candid assessments of pure vibe-coding tools. Baltazar, who has experimented extensively with tools like [Windsurf](https://thenewstack.io/windsurf-an-agentic-ide-that-thinks-and-codes-with-you/) and [Lovable](https://lovable.dev/), acknowledges their appeal while highlighting critical limitations.

“It’s so cool, right? You’re able to go there. You tell it what you want,” he says. “But if you really don’t understand what it’s generating, it really quickly gets out of hand.”

His experience mirrors concerns raised by other experts about the sustainability of AI-generated code: “You spend four hours, five hours there, and what you get in the end is not something I would risk putting in production anywhere to do a business requirement,” he said.

Moreover, Baltazar identified what he calls the “immediate orphan code” problem: “If you don’t understand what the AI has generated, and you cannot read code, you effectively are creating orphan code from Day 1. Because the person that wrote the code is the only one that can understand, and it’s an AI.”

He illustrated this with an analogy: “It’s like trying to write a book in Japanese with an AI. You say, ‘Okay, write this,’ and it gives you the Japanese sentence. Then you say, ‘Okay, here’s my Japanese book, wonderful.’ And you give it to a Japanese person … You’re trying to write something in a language that you don’t understand.”

> “If you don’t understand what the AI has generated, and you cannot read code, you effectively are creating orphan code from Day 1. Because the person that wrote the code is the only one that can understand, and it’s an AI.”
>
> **—Miguel Baltazar, vice president of developers at OutSystems**

## The Building Blocks Advantage

The Bubble approach provides a compelling solution to the “orphan code” problem identified by both Mendix and OutSystems. Rather than generating raw code, their AI builds applications using what Haas describes as “productionized building blocks.”

“You can think of no code is like Legos, different blocks that like we’ve built, that we’ve made sure are secure, that we’ve made sure are robust, that we’ve made sure are scalable,” Haas explained. “So, when AI spits back an application made out of those blocks, you have something that you can actually work with and actually live with when you’re building a business, not just, not just building a prototype.”

This approach addresses both the security concerns raised by Mendix and the maintainability issues highlighted by OutSystems. The visual representation remains comprehensible to business users, while the underlying implementation maintains enterprise-grade standards.

## The Great Divide: Vibers vs. Engineers

[Abhishek Sisodia](https://abhisheksisodia.github.io/), a mobile developer at Scotiabank Digital Factory, offers a nuanced take on this transformation. He sees vibe coding as “the new no code — except now it’s AI doing the heavy lifting instead of drag-and-drop builders.” The advantages are clear, he said: “It’s faster. It’s more accessible. And in many cases, it’s significantly more powerful.”

But Sisodia also identifies a key risk: “While GenAI enables rapid prototyping at a scale we’ve never seen before, it often skips over critical thinking around system architecture, scalability, security and long-term maintainability.”

He predicts a bifurcation in the market. “The ones who learn to blend the ‘vibe’ with real technical validation will build the next generation of transformative products,” Sisodia said. “The rest may vibe their way into irrelevance.”

The OutSystems experience validates this prediction, with Baltazar noting that vibe coding “is definitely a tool for professional, hardcore developers that know what is being generated and understand what is behind it.”

> “The ones who learn to blend the ‘vibe’ with real technical validation will build the next generation of transformative products. The rest may vibe their way into irrelevance.”
>
> **—Abhishek Sisodia, mobile developer at Scotiabank Digital Factory**

## The Platform Acceleration Thesis

Meanwhile, [John Bratincevic](https://www.linkedin.com/in/john-bratincevic/), a principal analyst at Forrester Research, presents a contrarian view backed by market data. Rather than seeing AI as a replacement for low-code platforms, he argues it will accelerate their adoption. “AI in the SDLC [software development life cycle] will increase low-code-ification and platform-ization for software delivery,” he told The New Stack. “Generating software necessitates more abstraction and integration, not less.”

His data suggests that “low-code adoption keeps going up,” and he sees the real disruption happening elsewhere, he said.

“The real threat is to ‘off the shelf’ applications rather than development platforms themselves,” he noted.

Bratincevic predicts convergence.

“Some of the vendors that win will be the existing low-code vendors, while others will be new entrants,” he said. “But all the products will end up looking very similar in a few years.”

## No Code vs. Low Code: A Critical Distinction

The conversations with multiple platform vendors reinforce a crucial distinction that often gets lost in discussions about AI’s impact on visual development. Both Baltazar from OutSystems and Van Huizen from Mendix agree that no code and low code face very different futures.

Baltazar agrees that no code will be subsumed by GenAI, “because the skill set is similar.” His insight into no-code limitations explains why.

“The only thing that no code has that GenAI doesn’t have is a very finite set of parameters that it works in,” he said. “The moment you get outside of those parameters, it’s hell, because it’s three times harder than doing it in high code.”

This creates what he calls a dangerous paradox.

“GenAI is even more dangerous than no code, because in no code, at least you have that walled garden that you play in,” Baltazar added. “But GenAI can generate whatever you want … thousands of classes, incredible amounts of [JavaScript](https://thenewstack.io/javascript/) and other sets of code that if you don’t understand what it’s doing, it’s really going to be orphan code.”

Low-code platforms, by contrast, maintain readability and governance, he noted.

“With low code, what comes out is readable, even for someone that is not an expert developer,” Baltazar said. “You can understand the data flow. You can understand the visual representation.”

> “GenAI is even more dangerous than no code, because in no code, at least you have that walled garden that you play in. But GenAI can generate whatever you want … thousands of classes, incredible amounts of JavaScript and other sets of code that if you don’t understand what it’s doing, it’s really going to be orphan code.”
>
> **—Miguel Baltazar, vice president of developers at OutSystems**

That said, the Bubble model represents an interesting hybrid — maintaining the visual comprehensibility of low code while using AI to accelerate development.

“Our vision is, you know, users of Bubble like, end up learning it, and there is a learning curve, but the learning curve for Bubble compared to the learning curve for code is just radically different,” Haas told The New Stack.

## Integration Over Replacement

[Jason Bloomberg](https://www.linkedin.com/in/jasonbloomberg/?originalSubdomain=nl), an analyst at [Intellyx](https://intellyx.com/), takes a pragmatic middle ground, arguing that “‘subsume’ is perhaps too strong a word.” He notes that “all the low-code/no-code platforms are integrating GenAI these days, either to augment the app specification process or to build working apps.”

Yet, Bloomberg emphasizes the limitations of pure AI generation.

“Building a working app from a prompt is easier said than done,” he told The New Stack. “Either the app has to follow a well-established pattern that the LLM [large language model] has been trained on, or at best it can frame out perhaps 80% of a working app.”

His prediction focuses on user experience evolution. “GenAI is becoming a must-have feature of every no-code platform, but it’s not subsuming them,” Bloomberg said. “The end game is for no-code vendors to add a prompt-based metaphor to the list of other no-code metaphors already in use.”

The experiences at Bubble, Creatio and OutSystems validate this integration approach. Rather than viewing AI as a replacement, they’ve embedded it throughout their development life cycle while maintaining the visual, governable nature that makes platforms sustainable for enterprise development.

## The Paradigm Has Already Shifted

[Brad Shimmin](https://www.linkedin.com/in/bradshimmin/), an analyst at The Futurum Group, suggests the transformation is already underway. “The paradigm has already shifted to no-code tools,” he said, drawing parallels to how business intelligence tools evolved from traditional interfaces to natural language processing.

As proof, he points to real-world examples. “Companies like Airtable use their Cobuilder tool as a starting point for app development, where users simply describe the app they want to build and the context where that app will run,” he said. “The key insight is that users begin their development work with a prompt rather than a pull-down menu,” while still retaining traditional development paradigms such as backup options.

## A Spectrum of Users, A Spectrum of Solutions

Yet, Bloomberg notes that the impact of vibe coding depends heavily on who is using it and what they’re building. “At the low-experience end, business users can easily use vibe coding to create relatively basic applications,” he said. These users don’t really care how the sausage is made, as long as it works.”

However, for advanced developers working on complex systems like “Linux kernel updates or device firmware,” vibe coding offers little value, he said. But for the vast middle ground of enterprise developers, “vibe coding is one tool in the toolbox — but they have to review every line of generated code to ensure they understand it and it doesn’t have security or quality issues.”

## Enterprise Implementation: Microsoft’s Platform Play

The theoretical discussions around AI and no code take on practical dimensions when viewed through Microsoft’s Power Platform strategy. [Ryan Cunningham](https://www.linkedin.com/in/rycu/), corporate vice president of Power Platform Intelligent Applications at Microsoft, offers a counterpoint to the “AI will replace everything” narrative.

“Traditional low code, as we thought about it in the last decade, is probably not the answer for the next decade,” Cunningham acknowledged. “But a platform, an abstraction layer, is more important now than ever.”

Microsoft’s approach illustrates how established platforms are evolving rather than being displaced. Their new “plan” concept moves beyond traditional drag-and-drop interfaces to what Cunningham calls a “digital software team” — AI agents that work as requirements analysts, process analysts, data modelers and solution architects.

> “Traditional low code, as we thought about it in the last decade, is probably not the answer for the next decade. But a platform, an abstraction layer, is more important now than ever.”
>
> **—Ryan Cunningham, corporate vice president of Power Platform Intelligent Applications at Microsoft**

“We’ve actually built agents that work not just as coders but as requirements analysts and process analysts and data modelers,” he told The New Stack. “They come in and start to look at that problem and recommend and build the right way forward and then go generate the assets as a result.”

This represents a middle path between pure AI generation and traditional visual development: AI-powered planning and analysis feeding into enterprise-grade platforms with built-in governance, security and scalability.

## The Abstraction Evolution Continues

Cunningham also added historical context to the current disruption.

“All we’ve been doing for software engineers for the last 40 years is adding layers of abstraction, so we don’t have to write low-level assembly code,” he said. “We are at the precipice of the next layer of abstraction.”

This framing positions AI-powered development not as a revolutionary break from the past, but as the logical next step in a decades-long progression toward higher-level abstractions. The difference is that this abstraction layer can understand natural language requirements and translate them into working software, Cunningham noted.

> “All we’ve been doing for software engineers for the last 40 years is adding layers of abstraction, so we don’t have to write low-level assembly code. We are at the precipice of the next layer of abstraction.”
>
> **—Ryan Cunningham, corporate vice president of Power Platform Intelligent Applications at Microsoft**

The enterprise reality also reinforces the platform advocates’ arguments. With 56 million people using Power Platform monthly and 90% of Fortune 500 companies adopting Copilot Studio, the data suggests that established platforms with AI capabilities are winning in the enterprise market over pure AI-first tools.

## Fusion Teams Become Even More Critical

Indeed, Cunningham argues that AI doesn’t eliminate the need for collaboration between business and technical users — it makes it more important. Cunningham emphasizes that “[fusion development teams](https://thenewstack.io/microsofts-low-code-power-platform-sets-stage-for-fusion-dev-teams-at-build/)” — dev teams with pros and citizen developers — remain central to their strategy.

“It’s hard to teach a businessperson how to build scalable, secure enterprise software. It’s hard to teach a software developer how to operate a business,” he said. “But if I can put them both on the same toolkit, they can do amazing, magical things together.”

This aligns with Bloomberg’s user-centric analysis — the goal is not to eliminate technical expertise but to create better collaboration patterns where business knowledge and technical capabilities can work together more effectively.

> “It’s hard to teach a businessperson how to build scalable, secure enterprise software. It’s hard to teach a software developer how to operate a business. But if I can put them both on the same toolkit, they can do amazing, magical things together.”
>
> **—Ryan Cunningham, corporate vice president of Power Platform Intelligent Applications at Microsoft**

## The Governance Imperative

Moreover, the Microsoft example highlights a challenge that pure AI generation tools have not solved: enterprise governance at scale, Cunningham said. He describes sophisticated capabilities for managing AI-generated applications — automated policies, deployment pipelines, security controls and even AI agents that monitor and clean up orphaned applications.

“We really thought end-to-end about that governance and management plan,” he noted. “And it’s a big reason why customers are building on the platform, particularly customers in highly regulated industries.”

## The Road Ahead

As this expert roundtable expressed, the future of no-code development is not a simple story of replacement or enhancement. It’s more complex, involving multiple user segments, use cases and technological approaches.

For instance, platform vendors pushing established platforms with strong governance, security and enterprise integration capabilities appear to provide advantages in the AI era. Rather than being disrupted by AI-first tools, they are incorporating AI capabilities while maintaining their core platforms.

The Bubble approach of “vibe-code killing” through AI-powered visual development, Creatio’s natural language enhancement of existing workflows and OutSystems’ agent orchestration model all point toward a future where AI enhances rather than replaces visual development — but in fundamentally different ways than traditional no code.

As Sisodia argued, the most useful tools will be those that can harness the speed and accessibility of AI while maintaining the engineering discipline necessary to build sustainable, scalable systems.

Also, as Microsoft’s Cunningham noted: With each new abstraction layer, “We’ve actually substantially expanded who’s building software and how much software they’re building.”

This AI era appears likely to continue this pattern: creating more software builders while increasing rather than decreasing the importance of platforms to manage the results.

My assessment from these experts is that AI will continue to enhance existing platforms while creating new categories of tools. And the most successful solutions will be those that blend the ease of use of AI with the governance and reliability of established platforms.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)