# Brex’s Web Dev Revamp Makes Code LLM Friendly, by Design
![Featued image for: Brex’s Web Dev Revamp Makes Code LLM Friendly, by Design](https://cdn.thenewstack.io/media/2025/03/3469338d-hooks-1024x578.png)
When the engineering team at [Brex](https://www.brex.com/) decided to revamp its frontend, the plan was to rebuild to better serve their customers. Along the way, the project had an unusual side effect: it made the website friendlier to [large language models](https://thenewstack.io/top-5-large-language-models-and-how-to-use-them-effectively/) (LLMs).

“We originally decided to rebuild Brex’s [frontend stack](https://roadmap.sh/frontend) to better serve our customers — from startups to Fortune 500s — for the years to come,” Brex senior software engineer [Marcelo Terreiro Prado](https://www.linkedin.com/in/marcelo-t-prado/?originalSubdomain=br), who oversees AI products, told The New Stack via email. “We’ve learned that when the code is easy for people to understand, it works great with LLMs, too.”

## Frontend Problems
Brex HQ is a financial technology company that provides a suite of financial services designed for businesses, particularly startups and high-growth companies. It offers corporate credit cards, cash management accounts, expense management software and other financial services.

Brex’s original [React-based frontend](https://thenewstack.io/new-york-public-library-on-choosing-react-to-rebuild-website/) had served them well for many years, Terreiro Prado said, but the fintech’s customer base was changing.

The fintech company had moved more upmarket in the past two years and began acquiring larger enterprise clients, he said.

“We realized that we hit the ceiling of the stack and could no longer afford the limitations that came with it,” he said.

There were two main problems they experienced with the original architecture. First, due to excessive network requests and expensive React re-renders, it suffered from performance issues. Second, codebase complexity had skyrocketed.

“I felt like I needed a Ph.D. degree to understand our FE [frontend] codebase,” [Terreiro Prado shared via X](https://x.com/marceloterreiro/status/1883148631123071228). He wasn’t alone, he added: new hires shared his frustration.

## Four Web Dev Guiding “First Principles”
With the rebuild, the web development team wanted to get back to [first principles](https://thenewstack.io/web-development-trends-in-2024-a-shift-back-to-simplicity/) for [frontend development](https://thenewstack.io/introduction-to-frontend-development). First principles thinking involves breaking down complex problems into their most basic elements and then reasoning upward from there.

Engineering manager [Derek Stavis](https://www.linkedin.com/in/derekstavis/), senior software engineer [Victor Magalhães](https://www.linkedin.com/in/vhfmag/?originalSubdomain=br) and Terreiro Prado came up with four guiding principles for the redesigned frontend:

**All data that can be preloaded must be preloaded.**“All of the data needed for a given route should be requested at the route’s root component; preloading needs to be the path of least resistance,” Terreiro Prado explained.**It should be obvious which components trigger queries.**“Previously, components from all levels could trigger queries, which made waterfall requests a real problem,” he stated. In the new architecture, only a handful of component types can initiate queries: the route’s entry point and components that query upon interaction (e.g., a select input that depends on backend data).**It should be obvious which data a component depends on (data colocation).**“You should be able to explain exactly how a component works just by reading its source code,” he said. “There should be no layers of indirection between[GraphQL](https://thenewstack.io/how-apollo-makes-llms-more-reliable-with-graphql/)and the rendered React component. We must feel like we are writing ‘dumb’ code, and not one filled with clever abstractions we may not fully understand.”**Opt for convention over configuration.**“The[platform team provides tools to make adopting](https://thenewstack.io/platform-teams-adopt-these-7-developer-productivity-drivers/)the golden pathway as straightforward as possible, like code generators, documentation and recipes,” he said. “Features written with the new arch perform considerably better in both UX and raw performance, and we trust engineers to follow the conventions.”
Dumb code may seem like an odd addition. But it’s a key component to their redesign.

“We think [dumb code is the best](https://x.com/marceloterreiro/status/1883148626891047309) type of code,” Terreiro Prado wrote on X. “Dumb code is one that everyone at your company can immediately read and understand it, without jumping into dozens of hoops and abstractions.”

## The Problem with React Hooks
The team was happy with React, which is used on all “frontend surfaces,” he said. They wanted to stick with it, but did upgrade from React 17 to React 18 as part of the revamp.

The React 18 upgrade further compounded the performance benefits of the new architecture, thanks to the concurrent rendering model, Terreiro Prado said.

One big problem they did have, though, was with [React Hooks](https://react.dev/reference/react/hooks).

React Hooks are a feature in React that allow developers to use state and other React features in functional components. They provide a way to manage component logic, such as state, side effects and context, without writing class components.

But Hooks have a side effect of making it easy for bad GraphQL schemas to go unnoticed, Terreiro noted.

“The best thing about Hooks is also its worst problem: it hides complexity,” Terreiro said. “When working with GraphQL, your data should be easily accessible by reading the graph. If you need multiple hoops or fancy logic to compute a Boolean, that smells like a bad schema.

“Hiding it away into a hook won’t solve the problem for your organization — it’s just sweeping the dirt under the rug.”

“This is why strong and opinionated principles are so important. It sets the foundation and tone for collaboration across your organization.”

— Marcelo Terreiro Prado, senior software engineer, Brex
In his [X thread, he provided examples](https://x.com/marceloterreiro/status/1883148624785441144) of Hooks hiding a bad GraphQL schema.

“For example, a hook such as ‘`useCanSubmitReimbursement`
’ is widely used in our frontend,” he wrote. “Innocent at first sight, but filled with a ton of waterfall requests and insane logic to compute a bool.”

He pointed out that some might counter that’s the result of a bad GraphQL schema, and not React Hooks.

“Absolutely, I couldn’t agree more. However, Hooks make this **really** easy to go unnoticed,” he wrote on X. “And because of their virus nature, you will soon have a looot of places using this bad implementation.”

One of the hard lessons he’s learned is that product engineers will use whatever’s available to them, regardless of the implementation being good or not.

“Therefore, it’s imperative you avoid shipping shit hooks, or your performance will slowly degrade over time,” he tweeted.

The previous architecture also didn’t encourage frontend and [backend](https://thenewstack.io/introduction-to-backend-development/) collaboration, he added. That led to more use of Hooks.

“When a frontend engineer needed data that didn’t map cleanly to the schema, they would often default to computing it with hooks. That hook would frequently fire multiple queries to fetch the necessary data, and then would compute the value using frontend business logic, which is always a code-smell,” he told The New Stack.

In the new architecture, that’s not possible because it would break principles 1, 2 and 3, he added.

Under the redesign, when a frontend developer needs data that doesn’t map to Brex’s graph, they have to collaborate with the backend to fix the GraphQL schema.

“This is why strong and opinionated principles are so important,” Terreiro Prado said. “It sets the foundation and tone for collaboration across your organization. GraphQL in particular has been on top of our Engineering leadership’s mind.”

## Switching Apollo for Relay: How It Changed the Site for LLMs
To reduce the problems they encountered with React Hooks, the team replaced [Apollo](https://thenewstack.io/apollo-graphql-now-connects-to-rest-apis-with-little-fuss/) with Relay.

Apollo is a general-purpose GraphQL client by design, Terreiro Prado explained.

“As part of that, it makes things like querying from within components really easy (ideas that go against our principles),” he said. “Relay, on the other hand, was designed with Meta’s requirements in mind. It was never built to be a general purpose client.”

[Relay is Meta’s JavaScript framework](https://thenewstack.io/facebooks-relay-javascript-framework-building-react-applications/) for building data-driven [React applications](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/). It’s specifically designed to work with GraphQL, which is a query language and runtime for APIs.
“Relay assumes your code to be written in a very particular way, and because of that, it’s able to derive a handful of smart optimizations,” Terreiro added. “Concepts like fragment masking, preloaded queries and data colocation are ideas baked into Relay’s core.”

The switch to Relay and its support for colocation also brought the unexpected result of making it easier for LLMs to understand the site.

![X post that reads, "Previously, I felt like I needed a PhD degree to understand our FE codebase. This was a common belief between new hires who were new to our codebase.Due to accidental complexity, things were WILD. Our new arch addresses this primarily through one principle: local reasoning."](https://cdn.thenewstack.io/media/2025/03/2aa716f9-marcelo_phd_tweet.png)
Brex senior software engineer Marcelo Terreiro Prado’s [post to X](https://x.com/marceloterreiro/status/1883148631123071228).

“It turns out that when you write fewer queries, and make your components tightly coupled to their data requirements, your entire architecture becomes easier to grasp,” he said. “Inspecting one component is all that it takes to explain how it works. You no longer need to jump into dozens of nested hooks, or inspect its parent to find which data it depends on.”

This is an idea he referred to as local reasoning. Local reasoning is the practice of structuring and organizing code in a way that allows [developers to understand](https://thenewstack.io/codesee-helps-developers-understand-the-codebase/) and modify individual components or sections of code without needing to have a comprehensive understanding of the entire application.

“The less hoops a model has to jump or files it needs to load into its context to understand the codebase, the more effective it will be,” he said.

This was also key to enabling LLMs.

“Building our architecture in a very principled and opinionated way also enables more structured guidance to LLMs,” he said. “We have a lot of recipes and docs on how to solve a frontend need. We feed this to the LLM so it knows exactly how to solve a particular problem, vs. inventing a solution.”

Data colocation — which is the third “principle the team adopted — also plays a part in this,” he continued.

LLMs are bound to their context window, and the more focused and specific the prompts are, the higher the chance the output will match what developers desire, he said.

“Colocation is a principle that resonates strongly with this,” he said. “Having most of the code in one file means LLMs don’t need to search through a large codebase to find how a particular field is computed.”

## The Future of LLMs and Web Dev
While Brex’s [spring release](https://www.brex.com/spring-2025) of the site — which included the rollout of React 18 and the Relay migration — worked well for LLMs, the landscape is evolving rapidly, and what works well before doesn’t necessarily always map to the newer models, he cautioned.

“However, our experience so far shows that there’s one key insight: make your code and APIs easy for humans to understand,” he said. “This is a simple yet surprisingly powerful observation.”

Brex recently shipped a [Model Context Protocol](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) (MCP) server that allows LLMs to generate multiple components, such as option inputs, tables, routes and multistep flows that strictly follow the team’s golden pathways, he said. One area of research Terreiro is excited about is how to make machines aware of and able to use Brex’s vast design systems library.

He shared one final important lesson about frontend development: alignment between leadership and the frontend is critical to [fixing web development problems](https://thenewstack.io/top-problems-developers-need-you-to-fix-now/).

“If our leadership team’s only focus was shipping multiple things as quickly as possible, and not quality/architecture, it would be hard to advocate for these changes,” he said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)