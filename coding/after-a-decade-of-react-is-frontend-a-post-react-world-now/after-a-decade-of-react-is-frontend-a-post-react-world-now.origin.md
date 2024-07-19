# After a Decade of React, Is Frontend a Post-React World Now?
![Featued image for: After a Decade of React, Is Frontend a Post-React World Now?](https://cdn.thenewstack.io/media/2024/07/29ba2c30-getty-images-hfoa7gkx1bq-unsplash-1024x683.jpg)
Ten years ago, Facebook developer Christopher Chedeau gave [a presentation at Oscon](https://www.youtube.com/watch?v=tXeBZ3WujTs) (O’Reilly Open Source Convention) about a relatively new JavaScript framework called React. As The New Stack’s Chris Dawson [noted at the time](https://thenewstack.io/javascripts-history-and-how-it-led-to-reactjs/), the presentation was fascinating because it explained the concepts behind React — and not just *how* it worked, but *why* it was created.

Given how dominant React has become in the frontend development ecosystem since Oscon 2014, in this article I’ll revisit the concepts behind React and determine how well they’ve aged. This is especially important in 2024, when major software products [like Microsoft Edge](https://thenewstack.io/from-react-to-html-first-microsoft-edge-debuts-webui-2-0/) have begun to explore what I’m calling a [post-React approach](https://thenewstack.io/pivoting-from-react-to-native-dom-apis-a-real-world-example/) to web development (the Microsoft Edge team is calling it “HTML-first”). Also, non-React frameworks like Svelte and Solid offer increasingly viable alternatives to frontend developers.

## Why React Took Web Dev by Storm in 2014
In his 2014 presentation, Chedeau explained that the genesis for React came from an extension of PHP that Facebook had released as open source software in February 2010, called XHP. “We extended the PHP syntax in order to put XML inside of it,” Chedeau said. This was done mainly for security reasons, but it also resulted in “a very fast iteration cycle.”

However, because it was PHP — a server-side language — every time something changed, the page would need to re-render completely. So the Facebook team decided to move a lot of the application logic of XHP into JavaScript, the browser’s native scripting language, because they wanted to avoid round trips — from the server to the client, back to the server, back to the client, etc. They then looked for ways to optimize the way JavaScript was used.

“I tend to think of React as version control for the DOM”

– Christopher Chedeau, 2014 (via AdonisSMU)
Long story short, they ended up creating a JavaScript library called React: the key innovation being the creation of a “virtual DOM.” The DOM (Document Object Model), as Wikipedia [nicely explains](https://en.wikipedia.org/wiki/Document_Object_Model), is “an object-oriented representation of an HTML document that acts as an interface between JavaScript and the document itself.”

As Chedeau explained, React gives you two “virtual” copies of the DOM (a before and after for each interaction), from which you run a “diffing” process to establish what exactly has changed. React then applies those changes to the actual DOM — meaning only a portion of the DOM is changed, with the rest of it staying as-is. That, in turn, means that only a portion of the webpage needs to be re-rendered for the end user.

Chedeau had a nifty quote that summed up the benefits of React: “I tend to think of React as version control for the DOM” (credited to AdonisSMU). So in this framing, React is kind of like Git for the frontend.

Another innovation was the creation of JSX (JavaScript XML, formally JavaScript Syntax eXtension), an XML-like extension to JavaScript syntax. Back in 2013, Facebook’s Pete Hunt [described it](https://tr.legacy.reactjs.org/blog/2013/06/05/why-react.html) as “an optional syntax extension, in case you prefer the readability of HTML to raw JavaScript.”

One of the important ideas behind React was that it wasn’t template-based, like previous popular frameworks (such as Ruby on Rails and Django). As Hunt noted, “React approaches building user interfaces differently by breaking them into components [which] means React uses a real, full-featured programming language to render views.”

React really did provide a revolutionary method of developing web apps — and it was especially suited to large applications where data changed a lot. Influential developers began to take note, and the adoption of React grew in 2014. James Long, then a developer at Mozilla, summed up the buoyant mood around React with a May 2014 post entitled: [Removing User Interface Complexity, or Why React is Awesome](https://archive.jlongster.com/Removing-User-Interface-Complexity,-or-Why-React-is-Awesome) (go read the post if you want the tech nitty gritty, but for our purposes here, the headline says it all!).

## React’s Critics
Despite its popularity, it didn’t take long for complaints to start rolling in about React. By the end of 2015, some developers were complaining of React “fatigue” because of the steep learning curve. [In December 2015](https://medium.com/@ericclemmons/javascript-fatigue-48d4011b6fc4#.vw6jw7oxw), Eric Clemmons wrote:

“Ultimately, the problem is that by choosing React (and inherently JSX), you’ve unwittingly opted into a confusing nest of build tools, boilerplate, linters, & time-sinks to deal with before you ever get to create anything.”

Developers also had issues with the way React handled state management. Here’s Charlie Crawford on The New Stack [in August 2016](https://thenewstack.io/flux-overview-react-state-management-ecosystem/):

“Problems start occurring when the component tree gets tall, and you have components that are far from each other on the tree, and one component is not a descendant of another, AND both components depend on the same bit of state.”

By 2017, some influential developers were starting to regularly voice complaints about React. [In August 2017](https://x.com/slightlylate/status/901580389759696897), Alex Russell — who at that time worked for Google’s Chrome team — kicked back against the notion that virtual DOM was fast:

“[…] there was never any basis in fact for the idea that VDOM was “fast”, still isn’t. It’s trading space for *convenience*, not speed.”

Another time, [June 2019](https://x.com/slightlylate/status/1135350142364659713), Russell pointed out that “diffing” is actually slow compared to other frameworks:

“Turns out diffing is slow! Other frameworks are going faster (Svelte, Lit, Vue, etc.) by taking different approaches, but they get similar surface syntax and they are *much* smaller.

## React’s Defenders
Some of the React issues that developers have complained about over the past decade have either dissipated or been resolved. For instance, the learning curve isn’t much of an issue nowadays — a lot of new frontend developers have come onto the market since 2014 and many started out by learning React. There have also been good solutions to the state management issues, such as Redux or React’s Context API.

Even with the performance issues, React has its defenders. Chief among them, the company Vercel, which runs the industry’s leading React framework, Next.js. In July 2023, Vercel published [a long blog post about React 18](https://vercel.com/blog/how-react-18-improves-application-performance), the current stable version. The post outlined “how concurrent features like Transitions, Suspense, and React Server Components improve application performance.”

But even if those features do improve performance, has that come at the expense of complexity? Some, including Netlify CEO Matt Biilmann, think so. [In January this year](https://thenewstack.io/keep-it-simple-frameworks-netlify-ceo-praises-astro-remix/), Biilmann used a tweet from Vercel CEO Guillermo Rauch to poke fun at the seeming complexity of Vercel (and by extension React).

It should be noted that Netlify is a direct competitor of Vercel! During that presentation, Biilmann pitched Astro as a much simpler framework alternative to Next.js. While Astro does allow users to integrate React, they can also choose alternative UI frameworks, like Vue, Svelte and Solid.

Just this week, Netlify and Astro [announced](https://www.netlify.com/blog/netlify-astro-are-partnering/) a formal partnership — so we can expect more of the “keep it simple” narrative from Netlify.

## Conclusion: Post-React or No?
It’s too early to proclaim we’re in a post-React frontend landscape, because React — and associated frameworks like Next.js — are still enormously popular. But there is a sense that developers have viable alternative approaches to choose from now. Neither Astro nor Svelte uses the virtual DOM approach, so developers can now choose a web framework that doesn’t rely on React (although Astro still has React as an option).

There’s also the “HTML-first” approach that Microsoft Edge is pursuing, which Alex Russell (who is a member of that team) described as “a modern Web Components + HTML-first architecture.”

Either way, frontend development is no longer as tied to React as it was just a few years ago. If you’re a new web developer entering the profession, you might even consider eschewing React altogether — although admittedly, that will diminish your short-term job prospects. But it’s at least an option to seriously consider, and might even help you land a job with a forward-thinking employer.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)