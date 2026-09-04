**DeepSeek released V4 Flash Vision Exp on August 21**, its first model that accepts image input. Image input means a model can understand a chart, screenshot, or photo document in the same way it can with text.

DeepSeek V4 Flash Vision Exp reached API gateways like OpenRouter on August 27. It adds image understanding to the company’s budget V4 Flash model. It keeps the same low price of $0.22 per million input tokens and $0.66 per million output tokens. The price doubles during weekday peak hours.

Google’s Gemini 3.7 Flash, released August 13, is the obvious comparison. It is the budget vision workhorse most developers default to, billed at $0.75 and $3.75 per million on OpenRouter.

DeepSeek pitches the model for document and chart understanding, as well as visual question answering. Google calls Gemini 3.7 Flash its “[most intelligent workhorse model yet](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/)“. With both making strong claims, I wanted to know which one is better to use for image input.

## The tests

I ran both models through three image tests that imitate real back-office work:

* **Chart reading** – a stacked bar chart with a cost line plotted on a second y-axis using a different scale, so the answer cannot be read by eyeballing where the line crosses the bars.
* **Invoice audit** – a vendor invoice with three planted errors: a line total that doesn’t match quantity times price, a subtotal that matches nothing, and a due date before the invoice date.
* **Incident diagnosis** – forty lines of production logs where a payment service crash sits at the bottom, but the real cause, a batch job exhausting the database connection pool, appears five minutes earlier.

I sent the same images and prompts to both models via OpenRouter and recorded the accuracy, tokens, cost, and speed for each call. I included images in the test sections and prompts at the end of the post for anyone who wants to replicate the test.

### Test 1: the two-axis chart

![](https://cdn.thenewstack.io/media/2026/08/354276a3-image.png)

Prompt:  
*“Look at this chart carefully and answer all three questions. Number your answers. 1. In which quarter did operating costs exceed total revenue? 2. Which revenue segment grew every single quarter? 3. Estimate the company’s total full-year revenue in millions of dollars.*

The trap I set was the dual axis. Revenue runs on a 0 to 12 scale on the left, costs on a 0 to 16 scale on the right, so the cost line never visually rises above the bars, even in the quarter where costs won.

Neither model fell for it. Both correctly said Q1, both named Subscriptions as the segment that grew all four quarters, and both landed on $36.1 million for the year, which matches my source data exactly. DeepSeek’s answer was short, three lines. Gemini showed its reading of each bar. Same score either way.

## Test 2: the broken invoice

![](https://cdn.thenewstack.io/media/2026/08/354276a3-image-1-1024x749.png)

Prompt:

*“You are auditing this invoice. Answer all three questions. Number your answers. 1. Check every line item: does the amount equal quantity times unit price? Name any line that is wrong and give the correct amount. 2. What should the correct total due be? Show your math. 3. Is anything else wrong with this invoice besides the arithmetic?”*

Both models caught all three planted errors. Each flagged the monitor arm line, where 10 units at $45.99 were printed as $505.89 instead of $459.90. Each rebuilt the math and arrived at the correct total due of $3,958.89. Each noted that the July 28 due date came before the August 12 invoice date. DeepSeek went one step further and noted that the printed subtotal didn’t match the printed line items, even before the error was corrected.

This test produced the only anomaly. DeepSeek took 30.5 seconds and billed 3,467 completion tokens for an answer only a few paragraphs long. This suggests a large amount of internal reasoning billed as output. Gemini answered in 7.9 seconds with 944 completion tokens. The token differences run the other way on input. DeepSeek counted each image at roughly 500 prompt tokens, Gemini at roughly 1,150. This makes it clear that the two companies tokenize images in very different ways.

### Test 3: the buried root cause

![](https://cdn.thenewstack.io/media/2026/08/b89c906c-image-1024x643.png)

Prompt:

*“These are production logs from an outage. Answer all three questions. Number your answers. 1. What is the root cause of this outage? 2. At what time did the problem actually begin? 3. What single action would you take first to restore service?*

The logs show a payment service crashing with a timeout error. A weak understanding would blame that service. The real cause appears at 14:05:12, when a manually triggered analytics job starts a full table scan on a 48-million-row table, consuming all 20 database connections.

Both models ignored the decoy completely. They named the batch job as the root cause, both pinpointed 14:05:12 as the start time, and both said to kill the batch job first. Gemini even suggested the specific PostgreSQL commands to do it.

DeepSeek answered in 11.9 seconds using 1,636 tokens for $0.00088, while Gemini answered in 7.6 seconds using 1,854 tokens at $0.00351.

## Results

Both models provided accurate answers to all questions. Every planted trap failed to catch either one. What separated them was speed and cost/ token usage. Gemini answered in 7.2 seconds on average, compared to DeepSeek, which took more than double that at 16.8 seconds. DeepSeek’s total bill was $0.0039, compared with Gemini’s $0.0122, about a third of the price.

|  |  |  |
| --- | --- | --- |
|  | **DeepSeek V4 Flash Vision Exp** | **Gemini 3.7 Flash** |
| **Accuracy** | 9/9 | 9/9 |
| **Total tokens** | 6904 | 6014 |
| **Total cost** | $0.0039 | $0.0122 |
| **Avg. response time** | 16.8s | 7.2s |

This is a first for us. Total match on accuracy, with the deciding points coming down to cost vs speed.

## What do I think?

The practical differences are cost and speed. DeepSeek did the same work for about a third of the money. Gemini did it in less than half the time, and its speed remained consistent, while DeepSeek swung from 8 seconds to 30 seconds depending on the task. DeepSeek’s pricing also doubles during weekday peak hours, and I tested on a weekend, so my cost gap is the best case for DeepSeek.

On a small scale for an individual user like myself, the price and speed are negligible. It really doesn’t matter if it’s 7 or 17 seconds. And it’s going to take a long time for either of these prices to really make a dent… unless you’re running at scale. If you are running at scale and batch-processing invoices overnight, DeepSeek does the job. If you’re running a massive task where a user is waiting on the answer, use Gemini.

*Prompts:*

Chart: “Look at this chart carefully and answer all three questions. Number your answers. 1. In which quarter did operating costs exceed total revenue? 2. Which revenue segment grew every single quarter? 3. Estimate the company’s total full-year revenue in millions of dollars.”

Invoice: “You are auditing this invoice. Answer all three questions. Number your answers. 1. Check every line item: does the amount equal quantity times unit price? Name any line that is wrong and give the correct amount. 2. What should the correct total due be? Show your math. 3. Is anything else wrong with this invoice besides the arithmetic?”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)