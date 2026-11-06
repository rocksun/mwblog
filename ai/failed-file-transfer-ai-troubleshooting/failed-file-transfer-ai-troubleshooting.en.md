**Fortra makes software that moves files between companies on a schedule** and says AI could give admins back up to 160 hours a year. That’s 3.1 hours a week admins would otherwise spend figuring out why a transfer failed.

Managed file transfer (MFT) sits behind payroll exports, bank settlements, and purchase orders. Fortra ships two MFT platforms, GoAnywhere MFT and Globalscape EFT. The new AI feature behind the estimate here is Guided Diagnostics, which works inside GoAnywhere.

[Heath Kath](https://linkedin.com/in/heath-kath-66305a17), Team Lead, Solutions Engineering at Fortra, is joining me for a demonstration on Thursday, November 19, at noon (9 a.m. Pacific). Kath will run Guided Diagnostics against a simulated failure and take questions on how the estimate was built.

REGISTER NOW FOR THIS WEBINAR

You have successfully registered for the webinar.

## **One failed transfer took 50 minutes to figure out**

Kath tells *The New Stack* that most failed transfers he sees come down to a connection or login problem with an outside trading partner. The log usually shows one of four error types: authentication, network, permissions, or a missing file. He mostly works in GoAnywhere and said the pattern holds on Globalscape and other MFT platforms.

He points to an example of a financial services company that sends a daily settlement file to a trading partner over SFTP, a secure way to move files between servers. And one day, the partner reports the file never arrived.

So the admin searches logs to find the right one, which shows an authentication failure. The admin then checks the SFTP connection settings and tests the password. When that doesn’t work, the admin asks the partner to inspect its own server logs.

And that’s where the answers are found. The partner had rotated its SSH keys without notifying others, so GoAnywhere was signing in with a key the partner no longer accepted. The team deployed the right key, tested the connection, and reran the job. The file went out as expected.

Kath’s tally:

![](https://cdn.thenewstack.io/media/2026/11/0856811c-fortra-v2-time-breakdown-1024x576.jpg)

Forty minutes of the 50 were spent investigating the problem. The fix took only 5 to 10 minutes.

“The opportunity isn’t simply making file transfers faster,” Kath says. “It’s reducing the administrative friction around managing them.”

## **Guided Diagnostics points to the likely cause and leaves the fix to the admin**

Guided Diagnostic lives in GoAnywhere’s admin console. So when a job fails, it reads the failure and lays out a ranked list of things to check. The admin can skip the set that matches logs, settings, and help articles.

On the settlement-file failure, it would flag “Authentication failure detected,” list the likely causes, and suggest next steps. It doesn’t change any setting, Kath says. “It would reduce the effort required to identify the likely cause and determine the next appropriate action.”

The admin can still make the change, and that’s the right call for software that handles a bank’s settlement files.

This online event will also cover three related features: Anomaly detection, log insights, and AI-generated documentation of how to build each workflow.

## **160 hours of troubleshooting**

The 160 hours is one part of a bigger number. Fortra MFT asked dozens of customers how long routine MFT tasks take by hand, then compared that with the same tasks using the AI features. Across each task it asked about, the estimate reached 571 hours a year per user. Troubleshooting spent up to 160 of the 571 hours.

Here’s how Kath splits the troubleshooting estimates.

![](https://cdn.thenewstack.io/media/2026/11/9ac661e6-fortra-v2-estimate-counts-1024x576.jpg)

In Kath’s own example, the root cause was on the partner’s own server. The time spent waiting for the partner to respond was not part of the estimate.

## **Repeat errors get the most help**

Kath expects Guided Diagnostics to help with the common failures that leave an error message behind. It helps less with intermittent network drops, problems found on the partner’s side, complex workflow failures, performance bottlenecks, or custom integrations.

A good admin should still take over when the cause sits outside GoAnywhere, when several things break simultaneously, when a fix carries security or operational risk, or when no one on the team has experienced the specific error.

Kath will take questions on all of this during the live Q&A on November 19. [Register here](https://thenewstack.io/webinar/ai-managed-file-transfer-troubleshooting/) to join the discussion. The research behind the number will also appear in *The Next Era of MFT: How AI Transforms Managed File Transfer*, an upcoming ebook from Fortra. [Sign up to get an advance copy here.](https://thenewstack.io/ebooks/observability/how-ai-transforms-managed-file-transfer/)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/976a6c81-1706717710759.jpeg)

Matt Burns is Director of Editorial at Insight Media Group, where he oversees The New Stack, Roadmap.sh, and Towards Data Science — three platforms that collectively help millions of developers figure out what to learn next. Previously, he spent 16...

Read more from Matthew Burns](https://thenewstack.io/author/matthew-burns/)