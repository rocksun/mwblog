# Introduction to Bolt: Does It Suit Professional Developers?
![Featued image for: Introduction to Bolt: Does It Suit Professional Developers?](https://cdn.thenewstack.io/media/2025/02/16baf448-alex-shuper-ilywf8exiem-unsplashb-1024x576.jpg)
As a developer, I know my responsibility is to create or work with maintainable solutions — and we usually consider that to mean writing in such a way as to transmit knowledge to other human developers. That position isn’t necessarily about to change, but trying to build software programatically using LLMs to assist will clearly play part of the development workflow in an increasing number of cases.

With that in mind, it’s likely we’ll need to get used to wielding components in a kind of lego instruction kit. So I tried out [Bolt.new](https://Bolt.new), which promises to “prompt, run, edit, and deploy full-stack web apps.” I wasn’t sure whether I would have an “agentic experience” or [whether this is still considered a coding tool](https://thenewstack.io/how-developers-are-using-bolt-a-fast-growing-ai-coding-tool/). The following definition within a landscape view places Bolt as the former:

So, let’s get to building with Bolt. Once you’ve logged in with GitHub, the start page is bold enough:

First let’s pin down some requirements for what we want to build. I’d like to build a blog, with the front page showing my latest entry. And I want a column of thumbnails to show previous entries on the right. I’ll assume that my standfirst (first paragraph) will be used as the text with the thumbnail image. There will be one “hero” image per post. That’s all pretty standard.

I’m not sure I have a “favourite stack,” but this might be a good way of learning a new site builder. It actually suggests Astro, which is built on [Vite](https://vite.dev/) — although these days a blog is simple enough to design anywhere.

Once I chose Astro, we get a chat box on the left, and code and preview on the right. Astro starts off setting things up:

Bolt never told me *where* I would be working — on the cloud or locally? Since there is a chat box, I asked Bolt and it clarified:

So this is good and interesting. It does mean, of course, that there might be issues or gateways to actually getting hold of my code. But for the meantime, I’ll assume that my interest is building.

I am shown a nice Astro blog starter template in a preview tab, with code in the other tab. So it is obvious that my experience will be fully mediated by Bolt — even if I’m at a page from Astro.

In order to see what we have now, I hit the big deploy button, and this is relayed in the chat box. This is done in collaboration with Netlify, which has a partnership with Bolt for this purpose. So I get a nice personalized URL to check the current work on:

Now we’ll compare the template with what I had specified earlier. On the blog page, the thumbnails don’t quite have the format I want:

I want to use a standfirst as the main visual style, and a much smaller image with a date. No title. The blog content is in Markdown, with the title, standfirst (named description), date and hero image placed in the front matter.

So we need to look at the layout.

Looking through the files with left pane, I come across the description of the blog thumbnails in src/pages/blog/index.astro:

As I started editing, the page kept scrolling upwards as I typed. Of course, I asked the AI what this bizarre behavior was due to, but it didn’t help.

Because the editor is just a web page and not an IDE, I don’t really have much control. I was using Chrome on my MacBook, so perhaps this was the problem. But at least my page had a URL, so I could immediately try another browser: Safari. Of course, I had to log back in, let Safari show me pop-ups, and reverify. Eventually, I got this, which was highly ironic:

So, the browser I was using to check on a bug was probably not ideal, and the one I had left was recommended. Was my problem fixed? No. After about line 50 onwards, any attempt to edit just made the code scroll up way past my cursor. At least I could close Safari.

I found no reference to this, so I assume it was a recent bug.

Now you might say, “surely the idea is to change everything with chat, not do it yourself” and you would have a point.

First, I asked Bolt to change the first standfirst for each blog so that they didn’t all have the same ipso lorem Latin. It did that:

Then I asked for the color and font of the date to be swapped with that of the description. It did that but also reversed my other changes of position and removed the title:

The conclusion here is not to have a granular language battle with the LLM, but to let the LLM make the big changes, while fixing the details later. I was battling a scroll bug, too. But the scrolling bug will be fixed with (human) developers. The LLM attitude can’t be controlled by Bolt, because they don’t build the models.

OK, we can fix the position of the date, and the leading (line spacing) easily enough.

I want this in a column and eventually on one page. Again, Bolt did this but then altered the other template parts without asking me, although it did tell me it was doing this:

Finally, we want the blog to be on the front page and the list of old posts to the side of the current post. After this final request…

…the main change was done, and on a wide screen was what I wanted.

I could then revert my style changes back in.

## Conclusion
Now, while I was fighting with the system — and it clearly can’t read my mind — it did its best to make my changes while keeping the blog looking like what *it thought* was a good-looking blog site.

And that is the nub; if essentially you want to let an outside source maintain an overall look, this will work for you. If you want fine-grained control, then this approach clearly will not work. I think a hybrid approach would work — but this clearly needs more training.

Apart from the scrolling bug, I think the ability of Bolt to manipulate Astro for my tasks was fairly strong — it did the grunt work. Also the layout of Bolt allowing me to see the results of chats, the code and a preview was very good. Overall, it’s a good start; the problem now is how to integrate the role of the human in a consistent way.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)