Anthropic launched Claude for Small Business this month, adding native connectors to business tools like QuickBooks, HubSpot, Canva, Google Workspace, and about a dozen others directly inside Claude Cowork. That’s a lot of brands — but does it work?

I wanted to see if Claude could read a semi-complicated financial report, understand and summarize key findings, turn it into a presentable slide deck in Canva, and email a short summary with the deck to my fictional colleagues.

## The test

I used Google Sheets, Canva, and my Gmail.

Before I could test Claude for Small Business, I built a fictional seven-month P&L for a small software consultancy. The P&L included nine tabs, twelve clients, twenty line items of expenses, and twenty deliberately planted problems ranging from obvious red flags to subtle but important nuances you’d need an expert to uncover. I built it using a different Claude account since I’m not a financial expert.

I connected Google Drive to Claude Cowork and gave it the following prompt:

*I am sharing a Google Sheet with you called Meridian Dev Studio P&L. It has nine tabs covering seven months of financial data for a small software consultancy. Please do the following:*

* *Read all nine tabs carefully before drawing any conclusions*
* *Write a plain English executive summary of the company’s financial health*
* *Flag every anomaly, risk, or concern you find, no matter how small*
* *Identify any clients or cost lines that need immediate attention*
* *Note anything that appears inconsistent across tabs*
* *Tell me what questions you would ask the CEO if you were their CFO walking into this for the first time*

*Do not just summarize the numbers. I want analysis, not a restatement of the data.*

Here are examples of the “problems” across varying levels of complexity hidden in the financial data:

* **Easy**
  + The company lost money every month for 7 months, with a cumulative net loss of $134,885.
  + Gross margin collapsed from 58% in November to 10.6% in March, coinciding exactly with the TerraLoop ramp.

* **Medium**
  + January’s headline revenue of $112,080 includes a $24,000 one-time late payment recovery from Client B. Without the late payment, January is actually below October.
  + Recruiting spend ran for three months, then stopped completely, with no new payroll line appearing, so the outcome of the search is unaccounted for in the data.

* **Hard**
  + Interest income is exactly $180 every single month for seven consecutive months. Real interest income fluctuates with cash balance, suggesting a manual journal entry input by rote rather than a real bank account.
  + A $4,400 bad debt write-off appears in March against a client that never appears anywhere in the revenue lines, a ghost receivable from an engagement not represented in this P&L.

## How did Claude perform?

Claude caught 17 of the 20 problems hidden in the financial data in less than six minutes. It caught all of the easy and medium-level items. From the hard tier, it caught five of the eight. This includes findings that one Claude account expected the other Claude account to miss. Missed items included a ghost receivable behind a bad debt write-off, a churned client with no explanation anywhere in the notes, and a reimbursables discrepancy hidden across two separate tabs.

> Claude caught 17 of the 20 problems hidden in the financial data in less than six minutes.

Seventeen out of twenty isn’t bad, if I were grading the test like we were in school, that’s a solid 85%. But we aren’t in school. And small businesses need to know what their numbers say. The three items Claude missed were the most forensic items on the list. Perfectly flat interest income for seven consecutive months suggests a manual journal entry rather than a real bank account.

A drop in bank fees in April, against stable revenue, could signal growing accounts receivable. Suspiciously clean depreciation math on an equipment purchase doesn’t add up. These problems would prompt an expert to ask why they look so perfect, which is a different cognitive mode that Claude does not yet reliably operate in.

Claude also identified five irregularities I didn’t plant: It found a commission plan paying on bookings rather than gross profit, a designer cost jump with no explanation, conference spend hitting its peak in the same month gross margin collapsed, a client referral dependency previously unflagged, and a typo in the Google Drive file name (oops).

## Claude and the creative assets

After completing its analysis, Claude built an 18-slide Canva deck and drafted an email summarizing the financial data, which it attached to the deck. The deck was fine. It looked like a standard design with stock images, which is what I’d expect. It wasn’t presentation-ready. What it lacked in perfection, it more than made up for with speed. Claude built that 18-slide deck in about three minutes. That leaves more than enough time for some light design/ copy polish.

I also want to highlight the personalization Claude did in the email. My Gmail account was set up with my name written as Jessica, but lately I’ve been using Jess in emails. Claude picked up on that and used Jess to sign off.

## The value

Claude for Small Business is a huge step forward for small business owners. Claude did in 20 minutes what I can only assume would take days to a week to complete. But — and this is a big but — it doesn’t replace the need for a human in the loop.

> Claude did in 20 minutes what I can only assume would take days to a week to complete.

Claude missed three items hidden in the data. That means those three items didn’t make it into the deck or the summary either. People using these tools still need to either understand complex accounting and finance or hire someone who does. Don’t get me wrong, this is leaps and bounds ahead of anything I’ve ever seen before.  But if it were my company, I wouldn’t want anything missed.

It’s a great tool, but it still requires human intervention.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)