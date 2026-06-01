Cursor launched its Jira integration last week. The integration was marketed as simple: assign a ticket in Jira and Cursor will handle it. No context switching, no copying or pasting.

> Welcome to the new new vibe coding era where the ticket is the prompt.

Welcome to the new new vibe coding era, where the ticket is the prompt. That sounds suspiciously easy. Was it as easy in practice?

I ran four tests, two with clearly written and two vague tickets. I asked Cursor to fix two bugs and write two features. My goal was to determine whether ticket quality affected Cursor’s outcome.

## Integration

Let’s talk paywalls. The Cursor/Jira integration isn’t available with the free tools. When I tried to upgrade my Jira account, I noticed it automatically gave me one month free upon sign-up. No credit card needed. Thank you, Jira. Cursor was a different story. No free trial for Cursor Teams, which is the plan required to use the integration. It cost me a little over $40 to complete this test (as long as I remember to cancel my Cursor subscription within the next 30 days).

After settling my tab, I was ready to integrate. I was surprised to see that the Cursor integration, available in the Jira/Atlassian marketplace, isn’t popular (yet?). When I downloaded it, approximately 7 p.m. Eastern on Wednesday, May 28, there were only 548 installs and no reviews. I wonder if it’s because the market either doesn’t know about the feature or isn’t interested in it.

A few clicks in Jira and a few more in Cursor and I was all set up. Very, very easy to set up.

## Execution

Did it work? Yes. Surprisingly well. I only had one hiccup in the testing process, though I’m willing to admit it could have been user error. After writing a ticket, I couldn’t find a way to “assign” or comment to Cursor. I executed the tickets through Cursor with a prompt saying “can you read and fix this ticket in my Jira account: ticket title”.

I ran four tickets across two separate clones of the HTTPie open source codebase. Clone A tested the clearly written bug-fix and feature-add request tickets. Clone B tested similar tasks to Clone A but with vaguely written tickets. I’ll post all ticket copy at the bottom of this article just for reference.

### Clone A (clearly written tickets)

**Bug Fix**

*Content-Type: application/json missing from verbose output when a POST request is made with exactly one custom header (*[*issue 1856*](https://github.com/httpie/cli/issues/1640)*).* The ticket gave Cursor the affected file, the steps to reproduce, and clear acceptance criteria. Cursor fixed the bug, added a regression test, and posted a detailed comment to Jira referencing the upstream GitHub issue number. I never mentioned it in the ticket. Cursor found that connection by cross-referencing the codebase and issue history on its own.

Cursor commented on the ticket, which appeared as a comment from me, not Cursor, and then closed the ticket. It did this same thing for all tickets, noting that here so I don’t have to mention it in each section.

**Feature request**

*Add a –no-elapsed-time flag to suppress the elapsed time line from HTTPie output without affecting headers or body.* Cursor implemented the flag, updated the help text, and added tests in tests/test\_meta.py. It explicitly checked off every acceptance criterion item in the Jira ticket.

### Clone B (vaguely written tickets)

**Bug Fix**

Same bug as before. This time, Cursor fixed it faster than it did on Clone A. I was a little surprised since the ticket was much worse. The comment Cursor left on the Jira ticket referenced the well-written ticket from the other bug fix request. Cursor used context from the prior ticket to fill in the gaps from the vague one. So cool. Great result, but it contaminated the test so I needed to find a new bug for it to fix before I could sufficiently test the vague ticket.

The next one I tested was [issue 1642](https://github.com/httpie/cli/issues/1642). *When using –download to retrieve a file where the server responds with Content-Encoding: gzip, HTTPie incorrectly reports “Incomplete download” because it compares the compressed Content-Length against the decompressed byte count.* Cursor fixed it correctly. It identified the root cause in downloads.py, set total\_size to None when Content-Encoding is present, added two regression tests, and posted a detailed comment to Jira referencing the upstream GitHub issue number again. This time there was no prior related ticket in the project to lean on. Cursor diagnosed and fixed the bug from a vague two-sentence description. Wow.

**Feature request**

This last ticket requested a completely new feature, so Cursor couldn’t use any context to complete the work. The ticket asked Cursor to “save responses without manually redirecting output every time.” It gave no acceptance criteria, file references, or implementation guidance.

Cursor built a complete –save flag with a companion –save-dir flag for custom output directories, auto-generated filenames derived from Content-Disposition and URL, collision-safe numeric suffixes, compatibility checks against –download and –output, and six passing tests in a new tests/test\_save.py file. Those were independent engineering decisions, and they worked. Again, wow.

10/10. No notes.

## What does this mean for the rest of us?

The software development landscape continues to change. Yes, I worked off a well-known repo, and the requests were pretty basic, but this still stands out as something special. I can comfortably say this coding agent can read your Jira tickets, fix what they describe, and report back with a comment.

> I would have no problem asking Cursor to vibe code a prototype or personal software via Jira tickets. Would I trust this on software in production? Not yet.

The vague ticket results are the most interesting part of this test. I expected Cursor to successfully close the clearly documented tickets. I expected it to get stuck in a loop when sorting out the vaguely written tickets. But I was wrong. Cursor handled a feature request with almost no information and produced a complete, tested implementation with reasonable design decisions.

I would have no problem asking Cursor to vibe code a prototype or personal software via Jira tickets. Would I trust this in production software? Not yet. I tested it on a well-known open-source repo with documented bugs. Production code is messier, less documented, and the stakes of a wrong fix are much higher.

Tickets:

### **Clear bug (GitHub issue #1640)**

**Title**: Content-Type header missing from verbose output with single custom header

**Description:**

When making a POST request with one custom header and -v flag, Content-Type: application/json is missing from the verbose output. Adding a second custom header makes it appear correctly.

**Steps to reproduce**:

1. `https post pie.dev/post -v ‘header1: xyz’ x=1` — Content-Type missing
2. `https post pie.dev/post -v ‘header1: xyz’ ‘header2: abc’ x=1` — Content-Type appears

**Expected**: Content-Type: application/json always shows in verbose output regardless of header count.

**Acceptance criteria**:

* Fix the inconsistency
* Add a regression test

### **Clear feature**

**Title**: Add flag to suppress elapsed time from output

**Description**:

HTTPie currently displays elapsed time at the end of every response. There is no way to suppress this without also suppressing other useful information.

**Proposed solution**:

Add a –no-elapsed-time flag that suppresses only the elapsed time line from the output while leaving all other response data intact.

**Acceptance criteria**:

* –no-elapsed-time flag suppresses the elapsed time line
* All other response headers and body output remain unaffected
* Flag works with existing output flags like -v and -b
* Help text updated
* Tests added

### **Vague bug (same bug as #1640, described badly)**

**Title**: Content-Type header missing sometimes

**Description**:

When making POST requests, the Content-Type header doesn’t always appear in the response. Not sure exactly when it happens, but it’s inconsistent. Seems like a bug.

### **Vague bug 2 (GitHub issue #1642)**

**Title**: Download broken with some servers

**Description**:

Sometimes when I download a file it says the download is incomplete even though the file downloaded fine. Not sure why, happens with certain servers but not others.

### **Vague feature**

**Title**: Add a way to save responses automatically

**Description**:

HTTPie should have an option to save responses without manually redirecting output every time. Would be useful for API testing.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)