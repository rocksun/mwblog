The promise is irresistible: Describe what you want in plain English, and AI spits out working code. This “[vibe coding](https://thenewstack.io/vibe-coding-and-you/)” approach has everyone from startup founders to enterprise CTOs wondering if they’ll still need programmers in five years.

[Java](https://thenewstack.io/introduction-to-java-programming-language/) creator [James Gosling](https://www.linkedin.com/in/jamesgosling/) [shared thoughts on that](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) with The New Stack earlier this year, saying “as soon as your [vibe coding] project gets even slightly complicated, they pretty much always blow their brains out.” He added that vibe coding is “not ready for the enterprise because in the enterprise, [software] has to work every fucking time.”

After speaking with [Simon Ritter](https://www.linkedin.com/in/siritter/), deputy CTO at Java platform provider [Azul Systems](https://www.azul.com/), about [AI code generation](https://thenewstack.io/the-ai-code-generation-problem-nobodys-talking-about/), two fundamental problems keep surfacing that suggest Gosling’s skepticism is well-founded.

## Garbage In, Garbage Out

The first problem is training data. AI coding tools learn from existing code repositories — places like GitHub and [Stack Overflow](https://thenewstack.io/stack-overflows-plan-to-survive-the-age-of-ai/). But here’s the catch: Most code out there isn’t very good, he argues.

“You could suggest, ‘Well, OK, let’s just use all the code on GitHub,'” said Ritter, a software architect who has been building enterprise systems for decades. “Is that going to give you good code? Probably not.”

He noted that GitHub is full of abandoned experiments, student projects and quick hacks. Stack Overflow answers often prioritize getting something working over getting it right. Unlike training ChatGPT on the collected wisdom of human knowledge, there’s no obvious source of consistently excellent code at the scale needed for AI training, Ritter said.

In computer science, garbage in means garbage out. Train an AI on mediocre code, and you’ll get mediocre results.

## The English Problem

The second issue is that [English is a terrible programming language](https://thenewstack.io/can-english-dethrone-python-as-top-programming-language/), Ritter told The New Stack.

Consider this sentence: “The chicken is ready to eat.” Are we talking about a live chicken ready for dinner, or a cooked chicken ready to be eaten? Both readings are perfectly valid, he said.

Or try this shopping instruction: “Get two pints of milk, and if they have eggs, get 12.” Twelve what — eggs or pints of milk? The ambiguity is baked right into the language.

“This is really one of the reasons that we have programming languages in the first place,” Ritter explained. [Programming languages](https://thenewstack.io/language-wars-2024-python-leads-java-maintains-rust-rises/) exist precisely because natural languages are ambiguous. A compiler can only interpret “if (x > 5)” one way. There’s no room for misunderstanding.

You can try being more precise in your English descriptions, but there is always another edge case, another way to misinterpret what you meant. That’s why we moved beyond natural language for programming in the first place, Ritter said.

## Where AI Actually Helps

None of this means AI is useless for coding. It’s already proving valuable in specific ways:

[Modern IDEs](https://thenewstack.io/best-open-source-ides/) with AI assistance are genuinely helpful. Set an X coordinate, and the system will often correctly suggest setting the Y coordinate next. This kind of fine-grained code completion makes developers more productive without the reliability issues of generating entire applications.

AI also excels at generating individual methods or classes when requirements are specific and bounded. Need a database access class for a known schema? AI handles that well. Want to refactor legacy code? AI can modernize existing implementations where the original intent is clear from context.

For quick prototypes and personal projects — like the [NFL team tracker app](https://thenewstack.io/devops-pioneer-vibe-coding-100x-bigger-than-devops-revolution/) I vibe coded with [DevOps](https://thenewstack.io/introduction-to-devops/) Pioneer [Gene Kim](https://www.linkedin.com/in/realgenekim/) — vibe coding works fine. If it breaks, you shrug and try again.

But this is where Java’s enterprise dominance becomes important. Java was not designed for quick experiments or throwaway code. It was built for the long haul — applications that need to run reliably for years or decades, maintained by teams of developers who were not around when the original code was written.

The [Java ecosystem](https://thenewstack.io/azul-cto-java-at-30-still-rules-enterprise-dev/) reflects this reality. Enterprise Java applications typically involve extensive frameworks, rigorous testing protocols and detailed documentation requirements, Ritter said. These are not nice-to-haves; they are necessities when your code processes millions of financial transactions or manages patient healthcare records.

## Enterprise Reality

Enterprise development is different. When you’re building systems that handle healthcare data, financial transactions or critical infrastructure, “shrug and try again” is not an option.

Enterprise applications require extensive unit testing. Are you going to trust [AI-generated tests](https://thenewstack.io/ai-is-testing-ai-generated-code-should-you-trust-it/) to validate AI-generated code? Ritter asked. They need rigorous code reviews, which means skilled developers must understand and validate every line — somewhat defeating the purpose of [eliminating programmers](https://thenewstack.io/github-ceo-on-why-well-still-need-human-programmers/), he said.

Then there is maintenance. Enterprise applications often run for decades. Future developers need to understand and modify code that was not written by humans, based on natural language specifications that may have been ambiguous from the start.

“Most people do code reviews,” Ritter said about serious development. “You’re going to need people who have the skills to do that, so you’re kind of reducing the benefits of trying to eliminate the need for coders.”

## The Real Future

Vibe coding is not about to eliminate programming jobs — at least not for work that matters. The future probably looks more like sophisticated autocomplete than wholesale code replacement, he said.

This isn’t necessarily bad news. Programming languages have always [evolved toward higher-level abstractions](https://thenewstack.io/power-apps-plans-feature-vibe-ifies-business-app-dev/). We moved from assembly to C to Java to modern frameworks, each step making developers more productive while maintaining the precision that [serious software](https://thenewstack.io/feds-critical-software-must-drop-c-c-by-2026-or-face-risk/) requires, Ritter said.

AI will undoubtedly play a bigger role in that evolution. But the fundamental tension between [natural language ambiguity](https://thenewstack.io/machine-learning-still-struggles-to-extract-meaning-from-language/) and [software precision](https://thenewstack.io/relax-about-your-dora-metrics/) suggests human programmers are not going anywhere soon.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)