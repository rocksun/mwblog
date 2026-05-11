Anthropic is expanding Claude’s reach across Microsoft 365, [adding Outlook support](https://support.claude.com/en/articles/14855664-use-claude-for-outlook) while bringing Word, Excel, and PowerPoint integrations into general availability.

The update means Claude can now follow work across emails, documents, spreadsheets, and slide decks within a single ongoing conversation, allowing context to persist as users move between apps.

The launch builds on Anthropic’s earlier Microsoft 365 push [unveiled in February](https://thenewstack.io/anthropic-accelerates-its-cowork-enterprise-play/), which introduced shared context between Excel and PowerPoint alongside a broader plugin ecosystem for [Claude Cowork](https://thenewstack.io/how-claude-cowork-helps-developers-spread-the-ai-knowledge/). The expansion pushes Claude further into day-to-day workplace workflows, particularly inside Microsoft’s productivity suite.

> “Claude can now follow work across emails, documents, spreadsheets, and slide decks within a single ongoing conversation, allowing context to persist as users move between apps.”

## **One chat, four apps**

The biggest addition is Outlook, which enters public beta as Claude’s newest Microsoft 365 surface.

Anthropic says Claude can now reference emails alongside spreadsheets, presentations, and documents within the same conversation thread.

![Claude in Outlook](https://cdn.thenewstack.io/media/2026/05/db2ade52-outlook.gif)

*Claude in Outlook*

At the same time, Claude’s Word integration is now broadly available after quietly [entering beta in April](https://www.linkedin.com/posts/claude_claude-for-word-now-in-beta-activity-7448436011535204352-8sus/). Claude for Word can draft, edit, and revise documents directly from a sidebar while preserving formatting and surfacing edits as tracked changes.

Notably, the integrations are designed to share context between applications. For example, Claude can move from Outlook into Word while retaining the surrounding conversation, emails, and action items gathered earlier in the workflow.

![Using Claude between Outlook and Word](https://cdn.thenewstack.io/media/2026/05/e5b9cce1-outlooktoword.gif)

*Using Claude between Outlook and Word*

Across the suite, a user could, for example, begin by triaging an inbox in Outlook, ask Claude to extract key figures from an attached spreadsheet in Excel, generate a client-facing summary in Word, and then update a PowerPoint presentation using the same underlying context — all without repeatedly re-explaining the task between applications.

Claude can also work across multiple open files simultaneously. Anthropic says spreadsheets, documents, and presentations can remain open side by side while Claude carries changes and context between them. Conversations also persist on a per-file basis, allowing users to return to the same document or workflow later without restarting the conversation from scratch.

That continuity may also raise new questions around oversight and data exposure, particularly as AI assistants gain broader access to a broad array of internal business context. In its [blog post](https://claude.com/blog/collaborate-with-claude-across-excel-powerpoint-word-and-outlook), Anthropic notes that users remain responsible for approving outbound actions before Claude sends or schedules anything on their behalf.

“You review every reply and calendar invite before it goes out, and nothing goes out until you click send,” the company writes.

## An enterprise play

The broader opportunity here is difficult to ignore. Despite the flood of standalone AI products over the past two years, much of enterprise work still flows through Microsoft’s productivity stack — Outlook inboxes, Excel models, PowerPoint decks, and Word documents that remain deeply embedded across large organizations.

As [one commenter on LinkedIn put it](https://www.linkedin.com/feed/update/urn:li:ugcPost:7458211439950983168?commentUrn=urn%3Ali%3Acomment%3A%28ugcPost%3A7458211439950983168%2C7458218247184732160%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287458218247184732160%2Curn%3Ali%3AugcPost%3A7458211439950983168%29) following the launch: “Claude inside Office is the wedge most enterprise AI plays missed.”

> “Claude inside Office is the wedge most enterprise AI plays missed.”

That observation gets at a broader shift underway across enterprise AI. Companies are competing over who becomes embedded inside the everyday software environments where work already happens – and there is no bigger player in that sphere than Microsoft.

Claude for Excel, PowerPoint, and Word are now generally available on paid plans across Windows and macOS, while Claude for Outlook is currently available in public beta. Organizations can deploy the integrations through Microsoft’s AppSource marketplace and the Microsoft admin center.

Anthropic says enterprise customers can also configure OpenTelemetry support to monitor prompts, tool calls, and document references across applications, while analytics tooling can break down usage by user, app, and day.

Organizations can either access the add-ins directly through Claude accounts or route requests through existing enterprise AI infrastructure using Claude models hosted on Amazon Bedrock, Google Vertex AI, or Microsoft Foundry.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)