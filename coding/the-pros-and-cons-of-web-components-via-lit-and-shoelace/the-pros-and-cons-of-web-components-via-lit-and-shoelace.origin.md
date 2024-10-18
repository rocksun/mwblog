# The Pros and Cons of Web Components, Via Lit and Shoelace
![Featued image for: The Pros and Cons of Web Components, Via Lit and Shoelace](https://cdn.thenewstack.io/media/2024/09/40a2df9e-getty-images-ft2uhxkefwe-unsplashb-1024x576.jpg)
While developers enjoy working with components in framework libraries, [web components](https://thenewstack.io/introduction-to-web-components-and-how-to-start-using-them/) are gaining more interest because they work with HTML and CSS and reduce the need for JavaScript. But they also offer the ability to write custom components, enabling larger internal software estates to keep more control of the look and feel on their pages. After [our recent story on Shoelace](https://thenewstack.io/shoelace-web-components-library-that-works-with-any-framework/) (soon to be re-named Web Awesome) I thought I would take [that library](https://shoelace.style/) for a spin.

Before we look at Shoelace, let’s take a quick look at the level just below it, the [Google web component library](https://thenewstack.io/polymers-web-component-library-litelement-and-how-it-compares-to-react/) called [Lit](https://lit.dev/).

## A Quick Look at Lit
This gives us an idea of how components are constructed. We just want to pick out the basic bits, because this is what Shoelace is built on. We’ll just look at the code through the playground [here](https://lit.dev/playground/#project=W3sibmFtZSI6ImluZGV4Lmh0bWwiLCJjb250ZW50IjoiPCFET0NUWVBFIGh0bWw-XG48aHRtbD5cbiAgPGhlYWQ-XG4gICAgPHNjcmlwdCBzcmM9XCIuL2luZGV4LmpzXCIgdHlwZT1cIm1vZHVsZVwiPjwvc2NyaXB0PlxuICAgIDxzdHlsZT5cbiAgICAgIHNwYW4ge1xuICAgICAgICBib3JkZXI6IDFweCBzb2xpZCByZWQ7XG4gICAgICB9XG4gICAgPC9zdHlsZT5cbiAgPC9oZWFkPlxuICA8Ym9keT5cbiAgICA8cmF0aW5nLWVsZW1lbnQgcmF0aW5nPVwiNVwiPjwvcmF0aW5nLWVsZW1lbnQ-XG4gIDwvYm9keT5cbjwvaHRtbD4ifSx7Im5hbWUiOiJpbmRleC5qcyIsImNvbnRlbnQiOiJpbXBvcnQge0xpdEVsZW1lbnQsIGh0bWwsIGNzc30gZnJvbSAnbGl0JztcblxuY2xhc3MgUmF0aW5nRWxlbWVudCBleHRlbmRzIExpdEVsZW1lbnQge1xuICBzdGF0aWMgZ2V0IHN0eWxlcygpIHtcbiAgICByZXR1cm4gY3NzYFxuICAgICAgOmhvc3Qge1xuICAgICAgICBkaXNwbGF5OiBpbmxpbmUtZmxleDtcbiAgICAgICAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbiAgICAgIH1cbiAgICAgIGJ1dHRvbiB7XG4gICAgICAgIGJhY2tncm91bmQ6IHRyYW5zcGFyZW50O1xuICAgICAgICBib3JkZXI6IG5vbmU7XG4gICAgICAgIGN1cnNvcjogcG9pbnRlcjtcbiAgICAgIH1cblxuICAgICAgOmhvc3QoW3ZvdGU9dXBdKSAudGh1bWJfdXAge1xuICAgICAgICBmaWxsOiBncmVlbjtcbiAgICAgIH1cblxuICAgICAgOmhvc3QoW3ZvdGU9ZG93bl0pIC50aHVtYl9kb3duIHtcbiAgICAgICAgZmlsbDogcmVkO1xuICAgICAgfVxuICAgIGA7XG4gIH1cbiAgXG4gIHN0YXRpYyBnZXQgcHJvcGVydGllcygpIHtcbiAgICByZXR1cm4ge1xuICAgICAgcmF0aW5nOiB7XG4gICAgICAgIHR5cGU6IE51bWJlcixcbiAgICAgIH0sXG4gICAgICB2b3RlOiB7XG4gICAgICAgIHR5cGU6IFN0cmluZyxcbiAgICAgICAgcmVmbGVjdDogdHJ1ZSxcbiAgICAgIH1cbiAgICB9O1xuICB9XG4gIFxuICBjb25zdHJ1Y3RvcigpIHtcbiAgICBzdXBlcigpO1xuICAgIHRoaXMuX3JhdGluZyA9IDA7XG4gICAgdGhpcy5fdm90ZSA9IG51bGw7XG4gIH1cbiAgXG4gIHdpbGxVcGRhdGUoY2hhbmdlZFByb3BzKSB7XG4gICAgaWYgKGNoYW5nZWRQcm9wcy5oYXMoJ3ZvdGUnKSkge1xuICAgICAgY29uc3QgbmV3VmFsdWUgPSB0aGlzLnZvdGU7XG4gICAgICBjb25zdCBvbGRWYWx1ZSA9IGNoYW5nZWRQcm9wcy5nZXQoJ3ZvdGUnKTtcblxuICAgICAgaWYgKG5ld1ZhbHVlID09PSAndXAnKSB7XG4gICAgICAgIGlmIChvbGRWYWx1ZSA9PT0gJ2Rvd24nKSB7XG4gICAgICAgICAgdGhpcy5yYXRpbmcgKz0gMjtcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICB0aGlzLnJhdGluZyArPSAxO1xuICAgICAgICB9XG4gICAgICB9IGVsc2UgaWYgKG5ld1ZhbHVlID09PSAnZG93bicpIHtcbiAgICAgICAgaWYgKG9sZFZhbHVlID09PSAndXAnKSB7XG4gICAgICAgICAgdGhpcy5yYXRpbmcgLT0gMjtcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICB0aGlzLnJhdGluZyAtPSAxO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgfVxuICB9XG5cbiAgcmVuZGVyKCkge1xuICAgIHJldHVybiBodG1sYFxuICAgICAgPGJ1dHRvblxuICAgICAgICAgIGNsYXNzPVwidGh1bWJfZG93blwiXG4gICAgICAgICAgQGNsaWNrPSR7KCkgPT4ge3RoaXMudm90ZSA9ICdkb3duJ319PlxuICAgICAgICA8c3ZnIHhtbG5zPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmdcIiBoZWlnaHQ9XCIyNFwiIHZpZXdib3g9XCIwIDAgMjQgMjRcIiB3aWR0aD1cIjI0XCI-PHBhdGggZD1cIk0xNSAzSDZjLS44MyAwLTEuNTQuNS0xLjg0IDEuMjJsLTMuMDIgNy4wNWMtLjA5LjIzLS4xNC40Ny0uMTQuNzN2MmMwIDEuMS45IDIgMiAyaDYuMzFsLS45NSA0LjU3LS4wMy4zMmMwIC40MS4xNy43OS40NCAxLjA2TDkuODMgMjNsNi41OS02LjU5Yy4zNi0uMzYuNTgtLjg2LjU4LTEuNDFWNWMwLTEuMS0uOS0yLTItMnptNCAwdjEyaDRWM2gtNHpcIi8-PC9zdmc-XG4gICAgICA8L2J1dHRvbj5cbiAgICAgIDxzcGFuIGNsYXNzPVwicmF0aW5nXCI-JHt0aGlzLnJhdGluZ308L3NwYW4-XG4gICAgICA8YnV0dG9uXG4gICAgICAgICAgY2xhc3M9XCJ0aHVtYl91cFwiXG4gICAgICAgICAgQGNsaWNrPSR7KCkgPT4ge3RoaXMudm90ZSA9ICd1cCd9fT5cbiAgICAgICAgPHN2ZyB4bWxucz1cImh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnXCIgaGVpZ2h0PVwiMjRcIiB2aWV3Ym94PVwiMCAwIDI0IDI0XCIgd2lkdGg9XCIyNFwiPjxwYXRoIGQ9XCJNMSAyMWg0VjlIMXYxMnptMjItMTFjMC0xLjEtLjktMi0yLTJoLTYuMzFsLjk1LTQuNTcuMDMtLjMyYzAtLjQxLS4xNy0uNzktLjQ0LTEuMDZMMTQuMTcgMSA3LjU5IDcuNTlDNy4yMiA3Ljk1IDcgOC40NSA3IDl2MTBjMCAxLjEuOSAyIDIgMmg5Yy44MyAwIDEuNTQtLjUgMS44NC0xLjIybDMuMDItNy4wNWMuMDktLjIzLjE0LS40Ny4xNC0uNzN2LTJ6XCIvPjwvc3ZnPlxuICAgICAgPC9idXR0b24-YDtcbiAgfVxufVxuXG5jdXN0b21FbGVtZW50cy5kZWZpbmUoJ3JhdGluZy1lbGVtZW50JywgUmF0aW5nRWxlbWVudCk7In0seyJuYW1lIjoidGh1bWJfZG93bi5zdmciLCJjb250ZW50IjoiPHN2ZyB4bWxucz1cImh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnXCIgaGVpZ2h0PVwiMjRcIiB2aWV3Qm94PVwiMCAwIDI0IDI0XCIgd2lkdGg9XCIyNFwiPjxwYXRoIGQ9XCJNMTUgM0g2Yy0uODMgMC0xLjU0LjUtMS44NCAxLjIybC0zLjAyIDcuMDVjLS4wOS4yMy0uMTQuNDctLjE0LjczdjJjMCAxLjEuOSAyIDIgMmg2LjMxbC0uOTUgNC41Ny0uMDMuMzJjMCAuNDEuMTcuNzkuNDQgMS4wNkw5LjgzIDIzbDYuNTktNi41OWMuMzYtLjM2LjU4LS44Ni41OC0xLjQxVjVjMC0xLjEtLjktMi0yLTJ6bTQgMHYxMmg0VjNoLTR6XCIvPjwvc3ZnPiJ9LHsibmFtZSI6InRodW1iX3VwLnN2ZyIsImNvbnRlbnQiOiI8c3ZnIHhtbG5zPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmdcIiBoZWlnaHQ9XCIyNFwiIHZpZXdCb3g9XCIwIDAgMjQgMjRcIiB3aWR0aD1cIjI0XCI-PHBhdGggZD1cIk0xIDIxaDRWOUgxdjEyem0yMi0xMWMwLTEuMS0uOS0yLTItMmgtNi4zMWwuOTUtNC41Ny4wMy0uMzJjMC0uNDEtLjE3LS43OS0uNDQtMS4wNkwxNC4xNyAxIDcuNTkgNy41OUM3LjIyIDcuOTUgNyA4LjQ1IDcgOXYxMGMwIDEuMS45IDIgMiAyaDljLjgzIDAgMS41NC0uNSAxLjg0LTEuMjJsMy4wMi03LjA1Yy4wOS0uMjMuMTQtLjQ3LjE0LS43M3YtMnpcIi8-PC9zdmc-In1d).

All we want to do is make a rating button, which takes a thumbs up (and goes green) or thumbs down (red) and changes the rating accordingly.

You can see that we pull in the JavaScript index.js as a module and use our own defined tag called `rating-element`
. The span defined in `style`
doesn’t affect the component because of the isolation of the shadow DOM.

Let’s extract the interesting bits from the code:

You can see the import of Lit, and the definition of the *RatingElement* class extending a *LitElement*. At the bottom of the file, you can see the registration of the tag as a custom element based on RatingElement:

1 |
customElements.define('rating-element', RatingElement); |
There is a render method that basically builds the basic element:
1234567891011121314 |
render() { return html` <button class="thumb_down" @click=${() => {this.vote = 'down'}}> <svg xmlns="http://www.w3.org/2000/svg" height="24" viewbox="0 0 24 24" width="24"><path d="..."/></svg> </button> <span class="rating">${this.rating}</span> <button class="thumb_up" @click=${() => {this.vote = 'up'}}> <svg xmlns="http://www.w3.org/2000/svg" height="24" viewbox="0 0 24 24" width="24"><path d="..."/></svg> </button>`; } |
So, that is quite a bit of code to do something quite simple, but you do get your own reusable component.
## Shoelace
Let’s go one layer up and use some Shoelace. Now we get built components.

We will install a Shoelace template that uses the [rollup bundler](https://rollupjs.org/) and start from there. The bundler helps to resolve components without lazy loading them from the web. This brings us closer to a standard developer workflow.

First I clone the rollup example template. That will have the right npm packages we need:

Then we install the packages. You may well need to do an `npm update`
too.

And finally, run the project:

And kick up the page on a different shell tab:

This is what you should see:

So how did we get these components to show?

First of all, we state in index.js which components we want to load in the bundle:

1234567891011 |
import '@shoelace-style/shoelace/dist/themes/light.css'; import '@shoelace-style/shoelace/dist/themes/dark.css'; import SlButton from '@shoelace-style/shoelace/dist/components/button/button.js'; import SlIcon from '@shoelace-style/shoelace/dist/components/icon/icon.js'; import SlInput from '@shoelace-style/shoelace/dist/components/input/input.js'; import SlRating from '@shoelace-style/shoelace/dist/components/rating/rating.js'; import { setBasePath } from '@shoelace-style/shoelace/dist/utilities/base-path.js'; // Set the base path to the folder you copied Shoelace's assets to setBasePath('/dist/shoelace'); // <sl-button>, <sl-icon>, <sl-input>, and <sl-rating> are ready to use!% |
So that is where the Shoelace button, input and rating components come from. This leaves the index.html to be very lean:
1234567891011121314151617 |
<!doctype html> <html> <head> <title>Shoelace Rollup Example</title> <link rel="stylesheet" href="dist/bundle.css"> </head> <body> <h1>Shoelace Rollup Example</h1> <sl-button type="primary">Click me</sl-button> <br><br> <sl-input placeholder="Enter some text" style="max-width: 300px;"></sl-input> <br><br> <sl-rating></sl-rating> <script src="dist/index.js"></script> </body> </html> |
Note that the index.js the HTML refers to is the one unrolled by rollup and placed in the distribution directory.
Want a dark theme? Just alter the index.html to:

1 |
<html class="sl-theme-dark"> |
And because we already imported the dark theme in the index.js:
Finally a little bit of interactivity (don’t forget to refresh your cache between bigger changes).

Let’s add a toast-style alert (one that goes to the corner) to the button and give the toast a duration countdown before switching off.

We include the alert component to index.js:

123456 |
...import SlIcon from '@shoelace-style/shoelace/dist/components/icon/icon.js';import SlInput from '@shoelace-style/shoelace/dist/components/input/input.js';import SlRating from '@shoelace-style/shoelace/dist/components/rating/rating.js';import SlAlert from '@shoelace-style/shoelace/dist/components/alert/alert.js';... |
We place the component in our index.html, replacing the button code:
1234567 |
<div class="alert-duration"> <sl-button variant="primary">Show Alert</sl-button> <sl-alert variant="primary" duration="3000" countdown="rtl" closable> <sl-icon slot="icon" name="info-circle"></sl-icon> This alert will automatically hide itself after three seconds, unless you interact with it. </sl-alert> </div> |
And some control code back in the index.js, before the end:
1234 |
const container = document.querySelector('.alert-duration'); const button = container.querySelector('sl-button'); const alert = container.querySelector('sl-alert'); button.addEventListener('click', () => alert.toast()); |
And the result is already quite impressive:
(What you can’t see is the blue countdown line shrinking at the bottom of the alert)

## Conclusion
This is just an introduction to using web components with a library like Shoelace — they need a bit of attention initially, but (like a framework) have a lot of rich content. However, unlike a framework, these are working mainly with HTML and CSS.

To make things easier for React users to transition, every Shoelace component can be available to import as a React component. The downside is that SSR (server-side rendering) is still not suitable with web components. And it is true that custom elements are not quite the same as components; the problems that this might cause are fleshed out [here](https://dev.to/ryansolid/web-components-are-not-the-future-48bh).

But overall, if you are thinking of working in or leading a larger web implementation team, make sure you understand the possible benefits of a web component library.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)