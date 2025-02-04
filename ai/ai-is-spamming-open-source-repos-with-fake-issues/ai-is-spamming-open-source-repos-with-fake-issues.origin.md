# AI Is Spamming Open Source Repos With Fake Issues
![Featued image for: AI Is Spamming Open Source Repos With Fake Issues](https://cdn.thenewstack.io/media/2025/02/f41ddf87-fake_ai_issues_hit_repos-1024x576.jpg)
AI is being used to open fake feature requests in open source repos, according to some maintainers. So far, AI-driven issues have been reported in [Curl](https://news.ycombinator.com/item?id=38845878), React, CSS and Apache Airflow.

It’s not known how widespread the issue might be, but it’s bad enough that maintainers are speaking out about it. Jarek Potiuk is a committer and PMC Member of [Apache Airflow](https://thenewstack.io/how-apache-airflow-better-manages-machine-learning-pipelines/), an open source platform that allows users to design, schedule, and monitor data pipelines. Potiuk went public about the [AI-submitted requests on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7289278690213990400/#) last week and spoke with TNS about his experience.

## Double the Issues
Apache Airflow maintainers noticed they had nearly double the number of issues filed one day, up to 50 from a normal run of more like 20-25. They investigated and noticed the issues seemed to be very similar but didn’t actually make sense. They began to suspect AI created these fake issues.

“Over the last days and weeks we started receiving a lot of issues that make no sense and are either copies of other issues or completely useless and make no sense,” Potiuk explained in his LinkedIn post. “This takes valuable time of maintainers who have to evaluate and close the issues.”

Potiuk explained to us that AI submissions don’t just create more work for [maintainers](https://thenewstack.io/open-source-paid-maintainers-keep-code-safer-survey-says/); they also can lead to legitimate issues being overlooked or incorrectly closed.

“We have like 30 issues a day, maybe 40, but now in 24 hours, we’ve got 30 more, so like 100% more, this means that we couldn’t make as many decisions on other things, because we had to make decisions on: Is this a good issue or bad issue?” he said. “Because of the very detrimental effect of it, there were at least two or three issues which were created by real people, and some of the maintainers, who are already sensitive, they closed them as spam.”

He reviewed the issues later and noticed two to three issues that were closed but legitimate. He reopened them, but the potential to miss a real issue is there. He’s also heard from other maintainers who have experienced a similar issue with “strange” requests, although they did not have as many issues as AirFlow saw.

## Tracking Down the AI Problem
Potiuk pleaded with those affiliated with the AI-driven issues to explain what was happening. One submitter reached out with an apology.

The person also told Potiuk that they had been following an [Outlier AI](https://outlier.ai/) training video about using AI to submit issues to repos. The person was not aware that they were submitting to a real repo.

“Outlier. You are doing it wrong,” Potiuk wrote in a LinkedIn post that tagged Outlier. “Please stop all the people who you are tricking into creating AI-generated, completely nonsense issues in many open-source repositories.”

Outlier is a platform that recruits subject matter experts to help train Generative AI. It’s also a Silicon Valley unicorn and subsidiary of Scale AI.

At first, Potiuk thought Outlier was trying to train AI somehow on their responses to the requests, but that turned out to be incorrect.

“Outlier. You are doing it wrong. Please stop all the people who you are tricking into creating AI generated, completely nonsense issues in many open-source repositories.”

— Jarek Potiuk, a committer and PMC Member of Apache Airflow
Potiuk said Scale representatives told him they did not intend for the video viewers to file the request with the actual repos. It was supposed to be just an exercise in creating issues. They also denied they were trying to use the repos to train their AI.

“You will work on a variety of projects from generating training data in your discipline to advance these models to evaluating the performance of models,” [Outlier says in its FAQ](https://outlier.ai/faq).

Scale declined an on-the-record interview, but referred The New Stack to their LinkedIn response, where [George Quraishi](https://www.linkedin.com/in/george-quraishi-980b871aa/), who handles ops at Scale AI, wrote:

“For context, we are constantly exploring new ways to train and evaluate models; coding is one area of interest. The goal of this project in particular was to teach a model how to help developers analyze issues and implement code changes — not to submit those tickets to your repo,” he wrote. “Unfortunately, a small number of our contributors misinterpreted the project requirements and took this additional step. We immediately updated the requirements to make them clearer.”

He continued to say that Scale values the work maintainers do and that they “have absolutely no interest in purposefully submitting tickets to inconvenience maintainers.”

This is not the first time Outlier has attracted press attention for its actions. Last summer, Inc.com reported that [some workers had accused Outlier of being a scam](https://www.inc.com/sam-blum/its-a-scam-accusations-of-mass-non-payment-grow-against-scale-ais-subsidiary-outlier-ai.html) after the company did not pay them.

## AI Spamming Security
It’s unlikely this problem is just caused by one AI company. AI is being used to spam security reports as well.

The problem goes back to at least early 2024, when [cURL author Daniel Stenberg wrote](https://daniel.haxx.se/blog/2024/01/02/the-i-in-llm-stands-for-intelligence/) about it. More recently, the security developer-in-residence at the Python Software Foundation, [Seth Larson, called out the issue](https://sethmlarson.dev/slop-security-reports).

“Recently, I’ve noticed an uptick in extremely low-quality, spammy, and LLM-hallucinated security reports to open source projects,” Larson wrote. “The issue is in the age of LLMs; these reports appear at first glance to be potentially legitimate and thus require time to refute.”

The issue was “distributed across thousands of open source projects and due to the security-sensitive nature of reports open source maintainers are discouraged from sharing their experiences or asking for help,” Larson wrote.

“Recently I’ve noticed an uptick in extremely low-quality, spammy, and LLM-hallucinated security reports to open source projects.”

— Seth Larson, security developer-in-residence, The Python Software Foundation
Larson pleaded with developers not to use AI or LLMs for detecting vulnerabilities.

“These systems today cannot understand code, finding security vulnerabilities requires understanding code AND understanding human-level concepts like intent, common usage, and context,” he wrote.

He also suggested a bit of thinking goes a long way.

“Some reporters will run a variety of security scanning tools and open vulnerability reports based on the results seemingly without a moment of critical thinking,” he wrote. “For example, [urllib3](https://pypi.org/project/urllib3/) recently received a report because a tool was detecting our usage of SSLv2 as insecure, even though our usage is to explicitly disable SSLv2.”

## Could Some Attacks Be State Actors?
[Craig McLuckie](https://www.linkedin.com/in/craigmcluckie/), a co-founder of [Kubernetes](https://thenewstack.io/build-an-open-source-kubernetes-gitops-platform-part-1/) and now founder and CEO of Stacklok, told TNS that his team had discovered someone trying to ambush repos by creating packages with similar names to well-known packages.
They discovered someone was trying to scam the [Tea protocol](https://tea.xyz/resources/about), which is a decentralized framework for managing recognition and compensation for open source software developers.

“They were publishing thousands and thousands and thousands of packages, with the sole intent of making those packages look like they were an important part of the open source ecosystem,” McLuckie said. “Just the volume of these ambush packages, it’s just going through the roof, and it seems to me that, like, for someone to produce the volume and the sort of slight variations that we’re seeing, there’s probably a generative AI agent behind the scenes.”

He spoke with the Tea protocol developers, who agreed it was “definitely bad behavior,” then worked with [npm](https://www.w3schools.com/whatis/whatis_npm.asp) to take the packages down.

McLuckie suspects a state actor was behind the submissions.

“Increasingly, there’s generative AI being used to create light variations on something and just doing that at scale, and I think it’s only going to get worse,” he said.

## Responding to AI Submissions
A GitHub engineer posted to Potiuk’s LinkedIn thread that they were looking into the issue, so TNS asked [GitHub](https://thenewstack.io/root-out-vulnerabilities-in-github-as-you-merge-code-changes/) about it’s response to the problem of AI submissions to repos.

“GitHub hosts over 150M developers building across over 420M repositories, and is committed to providing a safe and secure platform for developers,” a spokesperson told TNS. “We have teams dedicated to detecting, analyzing, and removing content and accounts that violate our Acceptable Use Policies.”

GitHub added that they employ manual reviews and at-scale detections that use machine learning and constantly evolve and adapt to adversarial tactics.

“We also encourage customers and community members to report abuse and spam,” the spokesperson said.

Potiuk also suggested maintainers continue to report AI submissions to GitHub. He also advised open source groups to work with “good” AI companies to identify fake issues. His team is working with an AI company called [Dosu,](https://dosu.dev/) which he has found helpful for sorting through issues. It’s a very different experience because the AI company is working closely with the team, he added.

“They automatically assign labels to the issue based on the content that people create, and that allows us to classify the issues without spending a lot of time,” he told TNS. “They talked to us. We had calls with them, and they explained it to us, and they gave it to us for free to do open source projects.”

*TNS Senior Editor Joab Jackson contributed to this article.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)