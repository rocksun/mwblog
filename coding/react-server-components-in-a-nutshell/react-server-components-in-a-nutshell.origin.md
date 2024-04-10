# React Server Components in a Nutshell
![Featued image for: React Server Components in a Nutshell](https://cdn.thenewstack.io/media/2024/04/de6cd4b4-react-server-components-in-a-nutshell-featured-image-1024x538.jpg)
Woah, there’s been a lot of noise about
[React Server Components](https://react.dev/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023) (RSCs) lately and, for the most part, after reading all the really smart explanations by [the internet’s smartest people](https://thenewstack.io/react-panel-frontend-should-embrace-react-server-components/), I didn’t really understand anything. But I’ve since spent time experimenting with [Waku](https://waku.gg/) and now I think RSCs are a lot simpler than I first thought.
## What Is Waku?
Waku (wah-ku) or わく means “framework” in Japanese. As
[a minimal React framework](https://thenewstack.io/new-framework-lets-devs-explore-react-server-components/), it’s designed to accelerate the work of developers at startups and agencies building small to medium-sized React projects. According to the Waku website, these include marketing websites, light ecommerce, and web applications.
What the introduction from the site is missing, however, is that Waku supports React Server Components — so if you want to try them out for yourself, you don’t need to use Next.js (which I for one am thankful for). It’s worth mentioning though that Waku is currently in rapid development and should only be used in non-production projects.
## React Server Components in a Nutshell
So here’s my take: RSCs give React developers access to asynchronous server-side requests and the resulting data, at the component level.
Before RSCs, frameworks like Next.js, Gatsby, Remix and Astro would require you to make server-side requests at the route level.
Here are some examples of how you’d achieve that in each framework mentioned above.
## Next.js Route (App Router)
Within this route, there’s a function called
getData which makes an asynchronous request to the GitHub API and returns the response, which can then be extracted and made available to the route or page using the
getData function.
## Next.js Route (Pages Router)
Within the route, there’s a function called
getServerSideProps which makes an asynchronous request to the GitHub API and returns the response back to the route or page via the
data prop.
## Gatsby Route
Within this route, there’s a function called
getServerData which makes an asynchronous request to the GitHub API and returns the response back to the route or page via the
data prop.
## Remix Route
Within this route, there’s a function called
loader which makes an asynchronous request to the GitHub API and returns the response, which can then be extracted and made available to the page using the
useLoaderData hook.
## Astro Route
Within this route, an asynchronous request is made to the GitHub API from within
[Astro’s special “frontmatter” fences](https://thenewstack.io/how-to-use-astro-with-a-sprinkling-of-react/). The
data can then be directly accessed by the route or page.
## Prop Drilling
You’ll notice that with all of these examples, the data is passed down to a component named ParentComponent via a prop named
data.
### ParentComponent
The ParentComponent might look something like this, where the data is passed down again to another component named ChildComponent.
### ChildComponent
Finally, in the ChildComponent is where you’ll perhaps want to do something with this data; and as you can see, the data had to go on a little bit of a journey before it reached its destination.
## Component Level Data Fetching
As you’ll probably know, if you were to refactor this application, or move the Parent or Child component, you’d need to also re-wire the data journey.
It’s not uncommon that over the life of an application, this will happen, and depending on how complex your application is will determine how far down you’ll need to go before your data reaches its intended destination.
This is where RSCs can really help. Here’s how I’ve approached this using Waku.
## Waku Route
Using Waku I still have a route, but no data fetching happens at this level.
### Waku ParentComponent
The ParentComponet still imports and returns the ChildComponent, but there are no props and nothing is passed down to the ChildComponent.
### Waku ChildComponent
And here’s the ChildComponent; once again, there’s no data passed down via props. Instead, all the data fetching happens within the component, server-side.
## Familiar to Some
This approach of accessing data at the component level might feel familiar to some. It does to me because I was an avid Gatsby user.
### Gatsby’s useStaticQuery hook
In
[February 2019 Gatsby introduced the useStaticQuery hook](https://www.gatsbyjs.com/blog/2019-02-20-introducing-use-static-query/), and whilst the method for fetching data is vastly different (I’m not trying to compare this to RSCs) the theory is kind of similar, and here’s why.
In Gatsby you were never fetching data using GraphQL (a common misunderstanding); instead, you were querying it. The fetching of data happened at build time, but with the
useStaticQuery hook you were able to access the data from any component, at any level, without needing to pass it around via props.
With RSCs the data fetching happens at runtime, so while the method for fetching data is different between RSCs and Gatsby’s
useStaticQuery hook, there is something to be said for the architectural choices you could make when you were able to access the data from within any component.
## Data Fetching Requires Thought
However, with RSCs you will still have to think about in which scenarios it makes sense to perform component-level data fetching, versus route-level data fetching.
On one hand yes, it is convenient to fetch and have access to data right there in the component where it’s needed; but on the other hand, if you have several components all on the same route that are fetching data independently, would this have a negative impact on performance?
In some cases, it might still make sense to make a single route-level request and pass the resulting data down via props to the components that need it, rather than multiple component-level data requests. It’s worth mentioning here that employing sensible caching strategies would likely limit the impact of multiple component-level data requests.
## Final Thoughts
RSCs, in my opinion, are just another option that’s available to you when building data-intensive React applications. I don’t think they will solve every use case, nor are they intended to. In many cases, they probably won’t be the right choice, but that’s ok.
As every developer will have said about any given approach many times in their career, it depends.
I know from my experience with Gatsby that there are advantages to having data easily accessible from within a component. It can really help with understanding what an application is doing because the logic, data, and the resulting user interface elements are neatly co-located in the same file, and when compared to chasing down props and attempting to follow the data journey, the developer experience is often better.
To conclude, I really like RSCs and I think in time we’ll all discover best practices and things to watch out for when developing. But for now, I think they’re a super cool step forward and I look forward to experimenting further. If you’re interested in experimenting with RSCs yourself, give Waku a try.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)