# How To Build Web Components Using ChatGPT
![Featued image for: How To Build Web Components Using ChatGPT](https://cdn.thenewstack.io/media/2025/02/62417fe4-aakash-dhage-en8upg7tuou-unsplashb-1024x576.jpg)
I’ve been thinking about [web components](https://thenewstack.io/introduction-to-web-components-and-how-to-start-using-them/) for a long time. In a 1996 BYTE story entitled [On-Line Componentware](https://web.archive.org/web/19961220012005/http://www.byte.com/art/9611/sec9/art1.htm), I showed how websites were also programmable building blocks. That was long before the advent of Web APIs, as Tim O’Reilly noted in a 2007 article about [Yahoo! Pipes](https://web.archive.org/web/20070209230148/http://radar.oreilly.com/archives/2007/02/pipes_and_filte.html):

*“Back in the summer of 1997, at our first Perl conference, Jon Udell gave a talk that electrified me. Jon expressed a vision of websites as data sources that could be re-used and of a new programming paradigm that took the whole internet as its platform. This was well before web services were au courant.”*
Gartner analyst [Mark O’Neill](https://www.linkedin.com/in/markwoneill/) argues in a recent [LinkedIn post](https://www.linkedin.com/posts/markwoneill_ai-agents-represent-an-existential-moment-activity-7291846704817991680-3eqJ/) — with a nod to my 1996 article — that we’re now entering the post-Web-API era.

*“What if the real Web APIs have been in front of us all along? What if it’s … just the Web itself? The lesson from the history of tech since 2000 is “The Web always wins” (anyone remember WAP and WML?).”*
In the comments, API expert [Kin Lane](https://www.linkedin.com/in/kinlane/) adds:

*“Just so everyone is aware, Mike Amundsen has been saying the web is the API this entire time.”*
O’Neill’s point is that LLMs bypass APIs and work directly with the human-readable web. Thirty years ago, I realized that websites are coarse-grained components amenable to programmatic scraping. Now we don’t need to code the scrapers, the AIs do it for us far more effectively. But there’s another way to think about web components.

## From VBX to React
My 1996 article referred to a 1994 BYTE cover story entitled simply [Componentware](https://web.archive.org/web/19961220155530/http://www.byte.com/art/9405/sec5/art1.htm), which argued:

*“The fact that VBXes (Visual Basic custom controls) today best exemplify the decades-old notion of reusable software has been a surprise for everyone, including Microsoft.”*
Many of us had assumed that the engine of widespread software reuse would be libraries of low-level objects linked into programs written by skilled coders. The surprise was that what actually gained traction were components built by professional developers and used by business developers. The VBX ecosystem offered controls for charting, network communication, data access, audio/video playback, and image scanning/editing. UI controls included buttons, dialog boxes, sliders, grids for displaying and editing tabular data, text editors, tree and list and tab views. People used these controls to build point-of-sale systems, scheduling and project management tools, systems for medical and legal practice management, sales and inventory reporting, and much more.

In the VBX era there wasn’t a universal platform for component reuse. Now there is, but it’s not React — it’s the web browser.

That ecosystem of component producers and consumers didn’t carry forward to the web. We see a pale reflection of it the form of [React components](https://thenewstack.io/react-server-components-in-a-nutshell/), but they’re not available to the kind of developer who could productively use Visual Basic components in the 1990s. You have to be a skilled coder not only to create a React component but also to use one. Plus, of course, those components are bound to the React framework. In the VBX era, there wasn’t a universal platform for component reuse. Now there is, but it’s not React — it’s the web browser, which has matured and standardized to a degree that I wouldn’t have predicted (but am thrilled to see).

The pushback against React ([merchants of complexity](https://thenewstack.io/developers-rail-against-javascript-merchants-of-complexity/), [JavaScript industrial complex](https://infrequently.org/2024/08/the-landscape/)) focuses properly on how its complexity and fragility are taxes that both developers and users pay. What instead? Lean into native web technology, say critics like [Alex Russell](https://www.linkedin.com/in/alexrussell/). Build progressive web applications that work as native HTML supported by simple CSS and JS, then layer on modern web APIs to match the experience of native apps. For components, that means eschewing non-standard React components in favor of standard [web components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components). The poster child for that switch is the Edge browser, which is [replacing React components with Web components](https://thenewstack.io/how-microsoft-edge-is-replacing-react-with-web-components/).

## Working With Web Components
What’s it like to build and use web components? Five years ago, I stuck a toe in the water and used it to make a tool for [searching and viewing Hypothesis annotations](https://jonudell.info/h/facet). There were already frameworks emerging, like [Lit](https://lit.dev/), but I wanted to see what it was like to work directly with the native web platform. And frankly, it wasn’t a great experience. Not because web components are inherently more complex than any other part of the native platform, but because the whole thing is challenging to master. That cognitive burden is one of the problems frameworks aim to solve.

Our AI assistants know all about the native platform and enable us to work far more effectively with it.

Now it’s a new ball game. Our AI assistants know all about the native platform and enable us to work far more effectively with it. So this seems like a good time to try an experiment. How feasible is it, now, for component developers to create simple libraries that enable component users to build basic web apps *without* frameworks like React, in a declarative style, with HTML and CSS and a bare minimum of JavaScript?

Here’s the kind of thing I have in mind for an app that feeds and displays a table of cities (or anything else):

12345678910111213141516171819202122232425 |
<layout-box layout="horizontal" align="center" responsive> <data-source id="citiesDS" table="cities" /> <app-form for="citiesDS" required="city,state"> <layout-box layout="vertical"> <h2>Cities</h2> <text-box style="width:15em" name="city" placeholder="Keene" /> <text-box style="width:2em" name="state" placeholder="NH" /> <text-box style="width:4em" name="population" placeholder="23000" /> <app-button style="text-align: left;" label="Add City" /> <list-view style="text-align: left;" for="citiesDS" fields="city,state,population"> <list-card /> </list-view> </layout-box> </app-form> </layout-box> |
## A Minimal Set of Basic Custom Elements
As the author of this app, you just write some basic HTML and optionally CSS to declare data sources, input fields, and views to display records. The [supporting libraries](https://github.com/judell/SimpleWebComponents), adding up to all of 260 lines of code, define the custom elements used in the HTML:

- layout-box
- data-source
- app-form
- text-box
- list-view
- list-card
- app-button
The libraries, while minimal, do enable an HTML author (the component consumer) to implement basic data entry and display. What made their construction possible for me (the component producer) was, of course, AI assistance.

I planned to use ChatGPT o1, but knowing this would be a long conversation and mindful of o1’s severe rate limit, I used Claude and ChatGPT 4o to get the ball rolling. This was the initial prompt:

*I’m looking for a web components library that is distinguished by absolute simplicity and minimalism, no dependencies.*
I was pretty sure there wasn’t one like that, but it never hurts to ask. Nothing like what I had in mind turned up, so away we went.

The first proof of concept punted on storage by using the browser’s local `IndexedDB`
, and punted on design by avoiding layout and style. The goal of the exercise was to create the handful of web components sufficient to enter and display data, and to support an HTML authoring experience that required no special knowledge to use them.

Almost instantly I had a basic library of custom elements and a simple test app to exercise them.

Working through that process was the best possible way to refamiliarize myself with custom elements, the foundation of web components. Almost instantly, I had a basic library of custom elements and a simple test app to exercise them. Iteration happened in the way we’re coming to take for granted: try a variation, share a screenshot of the error if it failed, or, if successful, discuss the pros and cons of the result and next steps. With the proof of concept in hand, I switched to o1 to tackle the issues we’d shelved.

## Partnering With ChatGPT o1
Instead of `IndexedDB`
I wanted to use SQL, and in the spirit of minimalism, I wanted the engine to be `sqlite`
. Claude had earlier helped me write a [lightweight httpd that embeds SQLite](https://github.com/judell/sqlite-server/), and the next step was to adapt the library’s data layer to use it. Here’s where o1’s reasoning ability came into play.

Things went mostly according to plan, though there was one small wrinkle. On the initial page load (and only then) the query ran twice. Why? The event flow for a custom element needed to be tweaked. It would have taken me a while to work out a solution on my own, but I didn’t need to. o1 offered a couple of alternatives; we discussed the pros and cons, I picked one, and on we went.

Next up: streamline the app author’s experience. The original `index.html`
included big chunks of JavaScript, but I wanted things purely declarative. Meeting that requirement led to a conversation about the age-old tradeoff between an opaque interface that’s easier for the component producer to create, and an extensibile interface that component consumers may demand to use. o1 proposed and implemented a set of extensibility hooks. In the end, I didn’t include the hooks because YAGNI (“you aren’t gonna need it”), but if needed, there’s a reasonable path forward.

## A Matter of Style
If JavaScript wouldn’t be required, what about hiding CSS too? We tried enabling the custom elements to accept simplified declarations for things like alignment, width, background, and color. That felt OK for the layout component, to sweeten the flex model with a bit of syntactic sugar, but otherwise not. When o1 started trying to reinvent style inheritance, I blew the whistle and threw down the penalty flag. For workaday apps that do simple data entry and display and don’t need to be themed, it’s not a stretch for the app author to use a bit of standard CSS.

This quick and cheap experiment exposed a structural flaw. The list component was originally a container for card components that were internal to the list and not visible to, nor styleable by, the app author. That’s what pushed us toward the slippery slope of inheritance. But the nesting didn’t need to be implicit like this:

12 |
<list ...> </list> |
Better to be explicit like this:
1234 |
<list ...> <card ...> </card> </list> |
So we restructured the `list-view`
accordingly.
## Evolving the Component Library
As it stands, the library is a proof-of-concept encapsulation of a common pattern. It enables an HTML author to create simple apps that implement basic data entry and display in a declarative way, supported by a simple set of web components. How to extend this approach to handle a wider variety of patterns?

To motivate the exercise, I had ChatGPT implement a different pattern: multi-row selection + partial edit. Here’s the “source code” for the app:

A salesperson returns from a trade show with a set of scanned prospects in a CSV file:

1234 |
firstname,lastname,company,email,notesAlice,Johnson,TechCorp,alice.johnson@techcorp.com,Bob,Smith,InnovateX,bob.smith@innovatex.com, ... |
The notes column is empty.
Write a standalone HTML/CSS/JS app, with no dependencies, that uses file upload to get the file, parses the records, and builds a form like this:

123456789 |
for each contact, print firstname lastname company email then add two inputs text: notes checkbox: [ ] add to hubspot |
The salesperson reviews the form, checks a subset of records, adds notes to the subset, and presses submit to send the subset to HubSpot. This is the API call:
12345678910111213 |
curl --request POST \ --url "https://api.hubapi.com/crm/v3/objects/contacts" \ --header "Authorization: $TOKEN" \ --header "Content-Type: application/json" \ --data '{ "properties": { "firstname": "Alice", "lastname": "Johnson", "company": "TechCorp", "email": "alice.johnson@techcorp.com", "custom_notes": "Sample note for Alice Johnson" } } |
The app generated from this “source code” worked flawlessly on the first try. How might the component library expand to support this pattern in a more general way? A discussion with o1 yielded some ideas but no clear path forward. A more broadly useful library of web components will need to account for a wider variety of patterns. Fortunately ,we’re now in a situation where we can quickly and easily generate working apps that exhibit a range of such patterns. And as opportunities emerge to distill them into components, we can quickly and easily generate those, too.
The JavaScript industrial complex won’t crumble anytime soon. But the stage is set for a return to an ecosystem of reusable components accessible to business developers, only this time based on the universal web platform and its core standards.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)