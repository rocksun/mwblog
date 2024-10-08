# Mix Human Expertise With LLM Assistance for Easier Coding
![Featued image for: Mix Human Expertise With LLM Assistance for Easier Coding](https://cdn.thenewstack.io/media/2024/10/b252051c-getty-images-illocmbfppc-unsplash-1-1024x576.jpg)
This box full of ready-to-mail letters was my problem, and the checklist shown at the upper right was the solution. As an enthusiastic [Vote Forward](https://votefwd.org) volunteer, I was losing track of which bundles were completed by which of my team of helpers. I needed a snippet of JavaScript to make a checklist so I could track our progress. Here’s how my [AI assistants](https://thenewstack.io/elevating-the-conversation-with-llm-assistants/) helped me write it.

All the information needed for a checklist is available on the Vote Forward dashboard, which provides columns of info cards for incomplete and complete bundles.

I get best results when I have knowledge and experience that I can use to drive the interaction, and when I decompose the problem into small pieces that are easy to test.

But there isn’t an easy way to match the bundle IDs on those digital info cards with the same IDs on the cover sheets of the bundles accumulating in my box of ready-to-mail letters. My LLM assistants helped me make a checklist to bridge that information gap. The task is admittedly mundane, but so are many information-processing chores. The fewer cycles wasted on them, the better.

Here’s how the dashboard looks on the site.

If you’re unfamiliar with [LLM-assisted coding](https://thenewstack.io/using-llm-assisted-coding-to-write-a-custom-template-function/), you might imagine a prompt like this.

Read this HTML page and make a sorted list of the IDs of unprepared and prepared bundles. The IDs are five-character alphanumeric strings.

But that isn’t how these things work — at least not yet, for me. I get the best results when I have knowledge and experience that I can use to drive the interaction and when I decompose the problem into small pieces that are easy to test. The first order of business was to find info cards on the page and extract two items from them: the bundle ID and the status (unprepped or prepped). This isn’t hard, but it’s a tedious chore that I’m happy to delegate.

Let’s see how ChatGPT and Claude handle this prompt.

## Find Bundle IDs and Statuses



wLMPw PREPPEDGive me JavaScript code to produce that output.


This kind of thing is trivial for both LLMs.

Plus, it’s easy to test these snippets in the browser’s console.

## Find All the Bundle IDs and Statuses
We’re not done yet, though. Both snippets return the same incomplete set of results. That’s because the site packages the two lists in elements that only display them partially; you have to scroll to see more than a handful of info cards. Here’s an approach that’s almost guaranteed to fail.

And sure enough, both of these solutions do fail. When I asked both LLMs for a different approach, they went off the rails. In retrospect, I can see how my language misled them. Initially I too imagined a solution that entailed scrolling.

Fortunately, I bring knowledge and experience to the table. On reflection, I realized that by increasing the heights of the columns, I could expose all the info cards to my script. Inspecting the page, I found that the two columns of bundles were wrapped in div elements styled with relative position and a dynamically computed height. These were the droids I was looking for. To verify that I could find them and adjust their heights to get rid of the scroll bars, I asked an assistant for another snippet that I couldn’t be bothered to write.

123456 |
document.querySelectorAll('div[style]').forEach(div => { let inlineStyle = div.getAttribute('style'); if (inlineStyle.includes('position: relative')) { div.style.height = '20000px'; }}); |
## Sort the Output
Now that I could find all the bundles, I wanted a two-level sort of the output: first by status (descending), then by id (ascending). Here’s more of the kind of code that I’ll never again write from scratch.

123456789 |
dataList.sort((a, b) => { if (a.dataTestId.includes("PREPPED") && b.dataTestId.includes("UNPREPPED")) { return 1; // UNPREPPED comes before PREPPED } else if (a.dataTestId.includes("UNPREPPED") && b.dataTestId.includes("PREPPED")) { return -1; } // Sort by ID if they belong to the same category return a.id.localeCompare(b.id);}); |
I’ve used this idiom countless times, in JavaScript and Python and other languages, but it isn’t something I do frequently — so it always slows me down to reacquire the method. I’m happy to delegate this kind of chore to an assistant that gives me a solution which, again, is easy to verify.
## Package the Results for Convenient Use
When I asked ChatGPT and Claude how to make this code available to other users of the Vote Forward site, both suggested making it a bookmarklet. But while it’s a minor miracle that this age-old technique can still work, my knowledge and experience told me it wouldn’t be the right answer. It’s gotten much harder to explain how to “install” a bookmarklet in various browsers. And a browser extension would be overkill. Sadly, my conclusion was that nowadays, for a small thing like this, you might as well just show people how to open a browser console and paste in code.

That still requires instructions, and writing them was another chore to outsource. You can see the instructions that Claude wrote in [this blog post](https://blog.jonudell.net/2024/09/30/making-a-vote-forward-checklist/). Full disclosure: I only tested on Chromium and Firefox, because I don’t have Safari handy, but the stakes are low here and I think the saving of time and effort is warranted.

## Adjust the Timing
There was one final problem. The script still wasn’t finding all the infocards on the page. Here was another case where my knowledge and experience won out. When asked about this problem, ChatGPT and Claude began spewing ever more convoluted variants of the script that failed to address the core issue: timing. I needed another age-old technique to overcome JavaScript’s asynchrony: a delay to let height adjustment finish before processing the items. Once I realized that, I could hand off the script to an assistant to implement the method because, again, an idiom like *setTimeout* is the kind of thing I use infrequently and so always need to refamiliarize with.

## A New Cost/Benefit Ratio
When confronted with a mundane information processing chore like this, I always have to weigh the benefit of automating it against the cost of doing so. In this case, we’re talking about the time to manually search for bundle IDs on the dashboard and match them with bundles of letters in the box.

If I’m totally honest, I’m not sure the time required to make the checklist, plus the time spent using it, added up to less than the time it would have taken to do the chore manually. But there’s no doubt that the automation came together much faster than it otherwise would have. Plus, it is available to others who may need it, so that’s an unquantifiable extra benefit. However the calculation works out in this case, it’s clear that much automation that formerly wasn’t cost effective can become so with the help of these assistants.

That isn’t a given, though. There are plenty of ways to use LLMs ineffectively. For best results, lean into your own intelligence, experience, and creativity. Delegate the boring and routine stuff to closely supervised assistants whose work you can easily check.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)