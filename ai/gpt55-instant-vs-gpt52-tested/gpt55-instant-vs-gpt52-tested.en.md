Last week, OpenAI replaced GPT-5.3 Instant as ChatGPT’s default model with [GPT-5.5 Instant, rolling it out to all users for free](https://thenewstack.io/openai-gpt-5-5-instant-launch/). When rolling out GPT-5.5, OpenAI made three specific claims: smarter, more accurate answers; 30% more concise responses; and deeper personalization drawing on past conversations, uploaded files, and connected Gmail. While I didn’t connect my Gmail to ChatGPT, I tested GPT-5.5 against GPT-5.2 for everything else.

I chose to test  5.2 over 5.3 or other models because I wanted to see real change over time. Every new release is presented as a major leap, but is it? Is there a noticeable difference between models that are six months apart?

In this case, yes. In my testing, OpenAI’s marketing messages held up, but not all of them. Here’s how GPT-5.5 Instant compares to 5.2.

## Is GPT-5.5 more concise and conversational than GPT-5.2?

OpenAI says GPT-5.5 Instant uses 30.2% fewer words 29.2% fewer lines than its predecessor, and is more conversational. I asked both models the following three questions to test OpenAI’s claims:

* *What is the difference between REST and GraphQL?*
* *What should you know before negotiating a senior engineering salary?*
* *What should you know before buying a first home?*

What happened? GPT-5.2 was consistently more concise on all three. The REST vs. GraphQL answer from 5.2 used a comparison table and tight bullet points to reach the decision more quickly. GPT-5.5’s version was fuller prose with more explanation and context. The salary negotiation answer from 5.5 ran longer with more sub-bullets and example phrases. The home-buying answer from 5.5 had 12 detailed sections, whereas 5.2’s had a cleaner, more scannable format.

But where GPT-5.5 missed the mark on conciseness, it made up for it with greater conversational tone. 5.5 was more thorough and conversational than GPT-5.2. Being concise vs. being conversational is in tension, and in practice, the conversational tone won out.

If you only need out-of-the-box, shorter — and sometimes clearer — answers, 5.2 may serve you better. If you want richer, more contextual responses, 5.5 is an improvement.

## Is GPT-5.5 more accurate than GPT-5.2?

OpenAI claims that GPT-5.5 Instant produces 52.5% fewer hallucinated claims on high-stakes topics such as medicine, law, and finance. As an expert in none of those topics, I used questions I’d already researched to assess the accuracy of these models. I asked:

* *What is the context window size of Claude Sonnet 4.6?*
* *What is the current status of the EU AI Act?*
* *What was the launch date of Anthropic’s Managed Agents product?*

The answer about Claude’s context window size from 5.2 introduced the first hallucination. It confidently stated that Claude Sonnet 4.6 supports a 1,000,000-token context window as standard. That claim is untrue. The standard context window is 200,000 tokens with extended options available in certain configurations.

Meanwhile, 5.5 answered correctly. It flagged that different vendors mix up API limits, UI limits, and beta modes, giving the correct 200,000 standard figure with appropriate caveats about the extended mode. 5.5 also noted that the raw context window size does not guarantee equal performance across the full window.

I don’t have anything to flag on the EU AI Act question. Both models answered accurately. For the Managed Agents question, 5.2 cited three early production users and 5.5 named five, which isn’t a surprise given the results from the first test.

> The marketing claim about accuracy is real: 5.5 is more careful about hedging uncertain information and less likely to produce a confident wrong answer.

The marketing claim about accuracy is real: 5.5 is more careful about hedging uncertain information and less likely to produce a confident wrong answer.

## Is GPT-5.5 better at personalization than GPT-5.2?

OpenAI claims that 5.5 can now draw on past conversations and uploaded files (and the untested Gmail access). I tested personalization in two ways:

* Uploading a published article and asking each model to characterize my writing style and predict my next story.
* Asking each model directly what it remembered about me from past conversations.

Both models accessed the file with only one difference in access. The older 5.2 model told me it needed to scan the file before it could use it, and 5.5 had access immediately. Other than that, there wasn’t anything worth noting in the file section.

And to the memory test. This, let me say, was risky business because I don’t go to my personal ChatGPT when I’m feeling great. I think I asked 10,000 questions about how likely I am to find a new job. Also, I can’t say I’ve never gone to ChatGPT for relationship or illness advice (sorry, not sorry). I asked it to use its memory and identify the patterns I display. I cringed while waiting for results, but they painted a different picture than the one I see in my head.

In its review, GPT-5.5 Instant surfaced 10 distinct patterns about my working style, versus 5.2’s 7. The three additional patterns spotted by 5.5 — including observations about my drive to prove competence and my tendency to underestimate my own hybrid skill set — were specific to fear spirals I’ve gone down in ChatGPT. Both models read me accurately and specifically. However, 5.2 did make one observation about me that I seek control through understanding when facing uncertainty, which 5.5 missed entirely.

Barring the one missed observation, 5.5’s personalization improvement is real but only incrementally. Both models have meaningful memory, but 5.5 goes deeper and broader. At this stage, though, I don’t think casual users will notice.

## What’s the verdict on GPT-5.5?

As a frequent ChatGPT user, I land here: GPT-5.5 is a little better than 5.2, but I don’t think I would have noticed without running them head-to-head. Outside of the hallucination on Claude Sonnet’s context window size, both models stayed well within the normal range of what you’d expect from an AI response.

> As a frequent ChatGPT user, I land here: GPT-5.5 is a little better than 5.2, but I don’t think I would have noticed without running them head-to-head. O

As a product marketer, I understand the value of making noise for your product, especially in a space this crowded. But I don’t think that’s what happened here. OpenAI shipped a real improvement. But just know that I’m just basing that conclusion almost entirely on one test, where 5.5 got something right that 5.2 confidently got wrong.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)