**AWS made Continuum for code vulnerabilities generally available** on Thursday. The service finds and validates bugs in your repositories, checks them against your AWS environment, and opens pull requests with proposed fixes.

## The 89% benchmark claim

The company published its headline benchmark on [October 5](https://aws.amazon.com/blogs/security/aws-continuum-sets-a-new-standard-in-autonomous-code-security/), more than two weeks before launch. In that run, Continuum passed 819 of 920 tasks on CyberGym-E2E, an 89.0% end-to-end success rate, against a previous public high of 65.9%. [Matt Garman](https://www.linkedin.com/in/mattgarman/), CEO of AWS, [writes on X](https://x.com/mattsgarman/status/2113393140543738237) that AI is “genuinely transformative for defenders” and that Continuum scored higher than any other AI agent on the test.

[Corey Quinn](https://www.linkedin.com/in/coquinn/), chief cloud economist and co-founder of Duckbill, replies [to the post,](https://x.com/QuinnyPig/status/2113398845883478110) wondering whether the release started as a re:Invent announcement and was pushed out early, given the state of the internet. Quinn offered no evidence that AWS had moved up the announcement.

> The recent PHP2Shell case shows how AI is making it easier to find vulnerabilities but fixing them is another story.

The recent [PHP2Shell case](https://thenewstack.io/ai-php2shell-disclosure-framework/) shows how AI is making it easier to find vulnerabilities but fixing them is another story.

## How CyberGym-E2E works

CyberGym-E2E gives an agent 90 minutes to find and fix a vulnerability in one of 139 open-source projects, without a bug description, proof of concept, crash log, or existing patch to work from. The agent must identify the flaw, trigger it, and produce a fix that stops the crash without breaking existing tests. All tasks involve memory-safety bugs in C or C++, leaving out many other languages and vulnerability types, as AWS acknowledges.

Grading runs in four cumulative stages. Continuum found and reproduced a bug in 92.5% of tasks, stopped the crash in 89.6%, and kept the project’s tests passing in 89.0%. The fourth stage checks whether the patch also fixes the historical vulnerability the benchmark selected.

The agent never learns which vulnerability that is; it only has to find and repair a real flaw in the codebase. Continuum’s patch also fixed that historical bug in 37.8% of tasks, against a previous public high of 26.2%.

> Continuum’s patch also fixed that historical bug in 37.8% of tasks, against a previous public high of 26.2%.

## The historical-bug score gap

The company does have a point about that last stage. A repository can have several vulnerabilities, and fixing a different one doesn’t make the work worthless, which helps explain the gap between the two scores.

Continuum completed 89% of the tasks by finding and patching a real vulnerability without breaking existing tests, but only 37.8% of those patches also addressed the the historical bug the benchmark was checking for. The agent wasn’t told which bug that was, so it’s not quite a fair comparison. What we still don’t know is how well Continuum performs when a team gives it a specific vulnerability to fix.

> A repository can have several vulnerabilities, and fixing a different one doesn’t make the work worthless, which helps explain the gap between the two scores.

## Who graded the benchmark

AWS ran the tests itself and says Continuum followed the benchmark’s rules, including limits on internet access. The company also checked that the agent wasn’t simply looking up fixes that were already public. Continuum passed 89% of tasks within the 90-minute time limit.

Give it more time, AWS says, and that rises to 93.7%. The benchmark and testing tools are public, but so far, those results are AWS’s alone.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)