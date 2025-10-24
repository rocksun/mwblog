[Seth Webster](https://www.linkedin.com/in/swebster) doesn’t think we’re in a [post-React world](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/) — or at least, not *only* a post-React world.

“We’re actually in a post-frontend-framework world, because the AI spits out React and nobody cares what it’s spitting out,” said the executive director of the newly created [React Foundation](https://thenewstack.io/new-react-foundation-to-manage-framework/). “We’re heading for a post-code-the-plumbing world, and we get to focus more on ,‘What [are] the delightful parts I want to create?’”

The problem is, large language models aren’t trained on the *best* [React](https://thenewstack.io/react-compiler-is-coming/) code, he continued; in fact, [LLMs](https://thenewstack.io/introduction-to-llms/) mostly have been trained on really bad React.

“They’re trained on the lowest common denominator React, which is what’s out in the world. They’re trained on the worst [Svelte,](https://thenewstack.io/svelte-adds-asynchronous-sync-inside-components/) they’re trained on the worst [Swift](https://thenewstack.io/get-started-with-swift/), because what they’re training on is publicly available code,” he [told The New Stack](https://thenewstack.io/react-foundation-leader-on-whats-next-for-the-framework/). “The best code in the world, oftentimes, is hidden behind private repo, and so they didn’t get to scrape that.”

## Why AI Is a Middling Engineer

LLMs haven’t had access to the best code or how tools are built, he added. As a result, AI is more like a middle-of-the-road, mid-career engineer. It’s not the best engineer you’ve ever met, he said, but it’s also not the worst.

For instance, one of the things [Claude](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/) likes to do is to use refs in React to track state.

“It’s not like the worst pattern we see in React, but it’s not a good pattern,” Webster said. “It’s basically indicative of the model doesn’t understand that the best way to build these things is to create an external service and integrate that using hooks with React, instead of trying to cram all the business logic into React, which is what everybody in the world does because we made it so easy to do that.”

It’s one of the mistakes the React maintainers made in React’s architecture, he added, because it’s “just too simple to put everything in React” — when developers really need [to think like engineers](https://thenewstack.io/ai-engineering-what-developers-need-to-think-about-in-2024/) and build the business logic a bit differently.

“If I’m doing authentication with [Google](https://thenewstack.io/googles-gemini-cli-agent-comes-to-zed/) or [GitHub](https://thenewstack.io/github-will-prioritize-migrating-to-azure-over-feature-development/) or whatever, I should have separate services that handle that,” Webster said. “I should have an authorization service, and it integrates with my different providers for different things. It handles telling the React app when someone has been logged in and so forth, when their authentication token expires, or just whatever.

“That should be integrated via hooks. You shouldn’t be putting that in your components, and the code the models have read is all crammed in the business logic, since it does not default to creating services.”

## A Goal to Improve LLMs’ React Output

One of the goals he hopes to accomplish as the head of the React Foundation is to improve the React code that popular [large language models generate](https://thenewstack.io/better-llm-agent-quality-through-code-generation-and-rag/).

That will mean a combination of [Model Context Protocol (MCP) servers](https://thenewstack.io/10-mcp-servers-for-frontend-developers/) and [evaluations](https://thenewstack.io/where-ai-benchmarks-fall-short-and-how-to-evaluate-models-instead/), he said. Evals are used to systematically assess an LLM’s accuracy and reliability against predefined metrics and business objectives, according to the global consultancy [Thoughtworks](https://www.thoughtworks.com/en-us/insights/decoder/a/ai-evals), a global consultancy.  [Evals, he said, help AI](https://thenewstack.io/ai-agentic-evaluation-tools-help-devs-fight-hallucinations/) deliver on its “intended purpose.”

Until then, Webster said, [AI needs help](https://thenewstack.io/ai-generated-code-needs-refactoring-say-76-of-developers/) from developers to get the code right: “It requires a lot of guidance, and it will for a while to come.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)