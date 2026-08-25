Earlier this year, [Anthropic launched Claude Security](https://thenewstack.io/anthropics-claude-security-beta/), an enterprise tool that helps development teams scan their codebase for security vulnerabilities and patch them. On Friday, the company gave Claude Security a major upgrade by bringing its [Claude Mythos 5 model to the service](https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders).

In addition, Anthropic is also working with other cybersecurity companies to help them integrate Mythos 5 into their products, and it is launching a new Defender Advantage Fund (0xDAF) that will provide $35 million in credits to find and patch vulnerabilities in open source software.

Anthropic previously also launched its [Cyber Verification Program](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude-opus-and-sonnet), which lets vetted defenders run dual-use cybersecurity work on Opus and Sonnet with fewer blocks. Those organizations will also get safeguarded access to Claude Mythos soon, Anthropic says.

## The Mythos 5 story: too good to launch

[Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5), of course, is the model that was so good in performing tasks in high-risk domains that Anthropic didn’t give it a public release. Instead, in June, it launched Fable 5, which is essentially Mythos 5 but with very strict guardrails.

Mythos 5, at the time, was only available to about 150 partners in Anthropic’s Project Glasswing program (and there’s the whole sidestory of Fable 5 getting [banned](https://thenewstack.io/us-gov-orders-anthropic-to-pull-fable-5-and-mythos-5-three-days-after-launch/) and [unbanned](https://thenewstack.io/how-anthropic-is-bringing-fable-5-back/) by the U.S. government).

## Mythos 5 in Claude Security

So why does the company feel comfortable adding Mythos 5 to Claude Security now?

“The riskiest behavior occurs when a user has direct access to a model, where a malicious actor can try to steer it toward harmful uses,” Anthropic writes in the announcement. “But if users can only receive specific outputs, such as a patch for a vulnerability or a security alert, that risk is much lower. The changes we’re announcing give users greater access to the defensive results, while maintaining appropriate guardrails around direct access to the model.”

## Safeguards

Essentially, since Anthropic is in charge here and all of this runs inside of its tools and harnesses, the company argues it can safely give Mythos 5 to all enterprises now. Users get findings and patches instead of direct model access, and Anthropic says Claude Security “uses Mythos 5 to scan code you own.”

It also adds that it and its partners “have abuse prevention measures in place to verify the model stays within its intended scope.”

Since many codebases include open source libraries, ownership becomes a bit of a slippery category. Also, a developer who clones a widely deployed library into a company repo and then points Mythos 5 at it would get the same findings an attacker would be looking for. That vulnerability, after all, would exist everywhere that library ships. We’ll have to see how this plays out.

In practice, this means Mythos 5 is now in public beta for all Claude Enterprise users who want to use Claude Security. Admins can enable it for their users and then developers and security teams can use it to scan their repositories with Mythos 5 at the helm and suggesting fixes when it finds an issue.

Mythos 5 tokens aren’t cheap, though. Anthropic charges $10 per million input and $50 per million output tokens.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)