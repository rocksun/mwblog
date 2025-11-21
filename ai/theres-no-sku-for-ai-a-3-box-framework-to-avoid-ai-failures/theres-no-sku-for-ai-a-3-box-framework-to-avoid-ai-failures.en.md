The numbers are sobering. A highly publicized report from [MIT shows](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/) that 95% of generative AI pilots at companies are failing to deliver meaningful financial impact. Meanwhile, t[he RAND Corp.](https://www.rand.org/pubs/research_reports/RRA2680-1.html) found that over 80% of AI projects fail — twice the rate of regular IT projects. And [S&P Global reports](https://www.rand.org/pubs/research_reports/RRA2680-1.html) that companies are now scrapping 42% of their AI initiatives, up from just 17% the previous year.

But here’s the thing: These aren’t technology failures. They’re strategy failures.

## **There’s No SKU for AI**

Walk into any enterprise software conference today and you’ll see vendors hawking “AI solutions” like they’re selling laptops or office chairs. The implicit message is that AI is a product you can simply purchase, plug in and watch the magic happen. This commoditized view of AI — treating it like a stock keeping unit (SKU) you can order from a catalog — is exactly why so many projects crash and burn.

The reality is that there’s no SKU for AI because AI isn’t a solution looking for a problem. It’s a powerful tool that requires thoughtful application to specific, well-defined business challenges. Most failures aren’t happening because the [AI models](https://thenewstack.io/data-infrastructure-not-ai-models-will-drive-it-spend-in-2025/) aren’t sophisticated enough; they’re happening because organizations are approaching AI in the wrong way.

## **The Science Experiment Trap**

Many of those [AI projects that fail](https://thenewstack.io/why-most-genai-projects-fail-only-1-in-3-make-it-to-production/) never had a clear path to return on investment from the start. They’re science experiments dressed up as business initiatives. A data science team gets excited about a new model, leadership hears about AI’s transformative potential and suddenly there’s a six-figure budget for an AI pilot with vague success criteria like “improve efficiency” or “enhance customer experience.”

These (doomed) projects follow a predictable pattern: impressive demos, initial enthusiasm, months of development, mounting costs and eventually a quiet abandonment when no one can point to concrete business impact. The MIT research confirms this, finding that purchased AI tools succeed 67% of the time while internal builds succeed only one-third as often, largely because vendor solutions come with clearer use cases and success metrics tied to specific business outcomes.

## **Avoid Panic Buying**

Another avenue where AI projects fail to yield meaningful value is when directives come from the top of the corporate hierarchy in a vacuum. “We need an AI strategy” directives can lead to panic buys.

For example, one deep-pocketed financial services organization received a mandate and immediately purchased the latest GPU-filled server to meet it. However, only after the server arrived on its data center floor did the organization realize that it hadn’t thought through how it would use it to solve business problems. Instead, it thought that the GPU server purchase alone checked the box mandated from above.

There’s a better way. . .

## **A Better Framework: The 3-Box Approach**

Instead of starting with AI and looking for applications, smart organizations flip the script. Here’s a framework that addresses the root causes of AI failure:

### **Box 1: Start with Your Top Business Problems**

List your organization’s 10 biggest challenges. Not technology challenges, business challenges. Think revenue growth, cost reduction, customer satisfaction, employee productivity, risk management or operational efficiency. These should be problems that keep your executives awake at night, not interesting technical puzzles that excite your developers.

This problem-first approach ensures you’re solving something that matters. As one executive quoted in the RAND study put it: “AI projects often fail when they focus on the technology being employed instead of focusing on solving real problems for their intended end users.”

### **Box 2: Assess Your Data Quality**

Of those top problems, which ones have good, clean, accessible data? This is where most AI projects hit their first reality check. Indeed, [CDO research](https://www.informatica.com/lp/cdo-insights-2025_5039.html?formid=26474&programName=25Q1-DPDS-NAM-CDO-NP-NI-NV-CDODataStrategy2025-0-PT5039-G&utm_source=google&utm_medium=paid_search&utm_campaign=25Q1-DPDS-NAM-CDO-NP-NI-NV-CDODataStrategy2025-0-PT5039-G&utm_country=us&utm_creative=CDO_Data-Quality_NB_Phrase_Google_Search_NAM_US_Leads_CPA_English&utm_journey=cdo&utm_cost=cpc&utm_term=ai%20data%20quality&gad_source=1&gad_campaignid=21305762875&gbraid=0AAAAADnfLNMpizTzLKIKNK8hgyixXQe7w&gclid=CjwKCAjw2brFBhBOEiwAVJX5GE6pNIv7LIKdxwPRqi6N-zC3wtU7wYT1x7_mNIewv8sT9F4KHhQr7hoC3vkQAvD_BwE) shows that data quality issues are a top obstacle, cited by 43% of organizations as their primary barrier to AI success.

With AI, “garbage in, garbage out” is still the phrase that pays. If your customer data is scattered across six systems with different formats, or if your operational data is incomplete and inconsistent or locked away in an ancient SQL database, [no amount of sophisticated modeling](https://thenewstack.io/the-evolution-of-the-ai-stack-from-foundations-to-agents/) in a standalone vector database will save you. The [problems with the best data](https://thenewstack.io/make-data-ready-for-ai-with-hygiene-governance-and-experimentation/) become your best AI candidates, not because they’re the most important problems, but because they’re the most solvable with current technology.

### **Box 3: Verify Existing Metrics**

Of the top problems that have good data, which ones already have established business metrics? This is crucial because it determines whether you’ll be able to prove ROI after a period of deployment of the AI solution. If you can’t measure the current state of the problem, you can’t demonstrate improvement after implementing AI.

Look for problems where you already track metrics like resolution time, accuracy rates, cost per transaction or customer satisfaction scores. These existing measurement frameworks become your success criteria and help avoid the vague goals that doom so many AI initiatives.

## **The RAG Chatbot Example: A Perfect 3-Box Fit**

Many early AI success stories revolve around implementing a retrieval-augmented generation (RAG) chatbot for support ticketing systems like those used by IT, HR or customer-facing teams. Let’s look at the internal use case, which checks all three boxes beautifully:

**Box 1 — Clear business problem**: Employee support requests consume significant time and resources. IT and HR teams spend hours answering repetitive questions about password resets, benefits enrollment, software access and policy clarifications. This directly affects productivity and employee satisfaction.

**Box 2 — Good data**: Your ticketing systems already contain thousands of resolved tickets with questions, responses and resolution paths. Internal websites often have answers to commonly asked questions, but employees rarely look at them. Your knowledge bases, policies and documentation provide clean, structured information that can feed a RAG system effectively.

**Box 3 — Existing metrics**: You already measure ticket volume, first-call resolution rates, average resolution time and employee satisfaction scores. These become your AI success metrics.

The beauty of this approach is that it’s employee-facing rather than customer-facing, making it lower risk while you learn. Employees are more forgiving of occasional AI quirks than paying customers, and the downside of a wrong answer is typically frustration rather than lost revenue.

## **Implementation Reality Check**

Even with this disciplined approach, remember that success isn’t guaranteed. [According to Gartner](https://www.gartner.com/en/newsroom/press-releases/2024-05-07-gartner-survey-finds-generative-ai-is-now-the-most-frequently-deployed-ai-solution-in-organizations#:~:text=The%20survey%20found%20that%2C%20on%20average%2C%20only,to%20go%20from%20AI%20prototype%20to%20production), research shows that only 48% of AI projects make it to production, and it takes an average of eight months to get there. But by following the three-box framework, you’re dramatically improving your odds by ensuring that:

* You’re solving a real business problem (not a technology hammer looking for nails).
* Your data foundation can support the solution.
* You can measure and prove success.

## **The Path Forward**

The high failure rates in AI projects aren’t an indictment of the technology; they’re a wake-up call about implementation strategy. Organizations that treat AI as a magic bullet or a commodity purchase will continue to join the 95% failure statistics. Those who approach it as a powerful tool requiring careful application to well-defined problems will find themselves in the successful 5%.

The next time someone pitches you an “AI solution,” ask them which of your top business problems it solves, what data it requires and how you’ll measure success. If they can’t answer all three questions clearly, you’re looking at another potential science experiment.

There’s no SKU for AI because AI isn’t a product; it’s a capability that requires strategy, preparation and discipline to deploy successfully and achieve a meaningful business outcome. The organizations getting this right aren’t the ones with the most sophisticated models; they’re the ones with the [clearest problems and the best data to solve them](https://thenewstack.io/data-dignity-developers-must-solve-the-ai-attribution-problem/).

Start with your problems, not your possibilities. Your ROI will thank you!

***Disclaimer:*** *The views expressed here are those of the author and should not be taken as the official position of MongoDB.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

Pete Johnson is the AI field CTO at MongoDB, where he regularly discusses topics like large language models, vector search and the Model Context Protocol with analysts, press and customers alike. A 30+ year technology industry veteran, he has held...

Read more from Pete Johnson](https://thenewstack.io/author/petejohnson/)