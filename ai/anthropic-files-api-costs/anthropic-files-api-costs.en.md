**Anthropic moved the Files API and computer-use toolset out of beta** on August 19 and launched a browser-use toolset. It lets developers upload a document once and reference it by ID in subsequent requests, rather than sending its contents each time. The common alternative is what most developers do today: pasting the reference material into every prompt.

I wanted to measure how uploading a file once compares to pasting the document into each request, in terms of tokens, accuracy, and setup. I built a test with a verifiable answer key and ran the same workload through both, plus a third approach, prompt caching, that came out of the results.

## The test

I wrote a fake API reference for an invoicing company called Ledgerline, about 1,200 words covering authentication, rate limits, idempotency, webhooks, bulk endpoints, and a sandbox. The scenario is a developer support bot that answers questions using only the Ledgerline API reference. Then I wrote five developer questions that the document can answer:

* How to tell apart two different 403 errors, and the fix for each
* How to safely retry payment creation after a timeout
* How to verify webhook signatures and block replay attacks
* The right way to create 2,000 invoices in one night
* What to do after committing a secret API token to a public repo

Each question has a specific correct answer in the reference, including details that are easy to miss. One fix depends on knowing that token scopes can’t be edited after creation. Another requires a separate rate limit for the bulk endpoint.

I ran the same five questions three ways, in Python scripts against the API directly, on claude-sonnet-5 with identical instructions:

* Arm 1 pasted the full reference into every request
* Arm 2 uploaded the reference once through the Files API and referenced its file ID in every request
* Arm 3 pasted the reference once into the system prompt with prompt caching enabled

The API reports token usage on every response, so each arm produced its own count.

## Getting it running

Two things broke before the first run. The scripts originally set temperature to zero for reproducibility, and the API rejected it. Temperature is deprecated on claude-sonnet-5. Second, one response led with a thinking block instead of text, which caused my printing code to crash. Both fixes were one-liners.

The Files API upload itself was uneventful. One call, one file ID back, and the ID worked in every following request.

## The results

All fifteen answers were correct against the answer key, across all three arms. Every arm caught the subtle details, the uneditable token scopes, the separate bulk rate limit, the constant-time signature comparison, the five-minute replay window. Whatever else changed between arms, answer quality did not.

> Whatever else changed between arms, answer quality did not.

While the answer quality remained consistent, the token counts didn’t.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Tests** | **Regular input tokens** | **Cache write** | **Cache read** | **Output** |
| Arm 1, paste every time | 15,246 | 0 | 0 | 1,399 |
| Arm 2, Files API | 15,371 | 0 | 0 | 1,434 |
| Arm 3, prompt caching | 271 | 2,990 | 11,960 | 1,642 |

Arm 2 billed slightly more input than Arm 1, which was interesting. The marketing doesn’t say this, but I thought using the files from one API might require slightly fewer tokens. The uploaded file’s contents are still processed into every request, at roughly 3,050 input tokens per question either way, and referencing the file added a small amount of overhead on top, about 25 tokens per request. Across five requests, upload-once cost 125 more input tokens than pasting. There is no volume at which that flips.

Arm 3 is the one that behaved as I assumed the Files API would. The document was billed in full once, as a 2,990-token cache write on the first request. The four requests after that read it from cache, and cache reads bill at about one-tenth the rate of normal input tokens. The questions themselves cost between 48 and 63 regular input tokens each. Cache writes carry a 25 percent premium over normal input, so the first request is the most expensive, and subsequent requests are where the reduction occurs.

Two caveats on the caching numbers. The cache expires after five minutes of inactivity, so the reduction assumes requests keep coming in steadily. And caching required restructuring the request, moving the document into the system prompt with a cache marker.

## When to use each approach

The interesting result is that the two features solve different problems. The Files API manages documents. Prompt caching lowers costs.

### **Files API**

Use the Files API when the problem is the file itself. It gives you one uploaded copy referenced by ID instead of the document text living in your code; it handles formats you can’t paste, like PDFs and images; and stored files now support expiration settings. What it doesn’t change is cost. The document is processed for every request, and Anthropic’s announcement never claimed otherwise.

### **Prompt caching**

Use prompt caching when the problem is paying for the same document on every request. In this workload, it cut billed input to roughly a third of pasting across five requests, and the gap keeps widening because every request after the first reads the document at about a tenth of the normal rate. The tradeoffs are the five-minute cache expiry, which assumes steady traffic, and restructuring your request to add the cache marker.

Use the files API and prompt caching together when both problems apply. Files API documents can be cache-marked the same way as pasted text. I tested them separately to isolate what each does on its own.

### **Paste the documents**

Pasting still wins in some cases. Use pasting when prototyping and making one-off calls, where uploading first is just an extra step. This is also the best option for documents that change with every request, where nothing is reused so neither feature helps. Keep in mind that this is short reference text, since documents under 1,024 tokens can’t be cached on most models. Pasting also has the fewest moving parts: no upload step, no file IDs, no stored copies to manage.

I did this test expecting to find out whether the Files API beats pasting in terms of accuracy or cost. It turns out I asked the wrong question. They tie on cost, and the feature that wins on cost was something I tested at the last minute to try to force a different result.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)