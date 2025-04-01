# Opengrep Launches as Free Fork After Semgrep License Shift
![Featued image for: Opengrep Launches as Free Fork After Semgrep License Shift](https://cdn.thenewstack.io/media/2025/02/9a2225f8-a-calvar-o5fccjrump0-unsplash-1024x683.jpg)
[Endor Labs](https://thenewstack.io/endor-labs-station-9s-top-10-open-source-security-risks/) has forked [Semgrep](https://thenewstack.io/the-security-tooling-faceoff-open-source-security-vs-commercial/) into [Opengrep](https://www.opengrep.dev/), following what Semgrep describes as the long trusted security tool’s “update.”
Opengrep was created with a governance structure to sustain continued and indefinite open source freedom of use that Semgrep no longer offers, [Varun Badhwar,](https://www.linkedin.com/in/vbadhwar) CEO and co-founder of Endor Labs, told The New Stack.

“The main thing we’re trying to accomplish is to make Opengrep a more neutral ground, ensuring that no single party can pull the rug out from under something like this,” Badhwar said. “The second goal is to bring enough capital investment to close any gaps that Semgrep introduced as a result of their changes.”

Additionally, Badhwar said Opengrep’s developers are improving performance, adding more support for platforms such as Windows, enabling multifile analysis and addressing “many of the gaps that Semgrep has intentionally created or maintained over time to push users toward their paid engine.”

Opengrep is built on three core principles, according to the documentation:

- A better and more capable scanning engine by not hiding essential metadata and new scanning capabilities behind a login. Opengrep will be backward compatible and support common
[JSON](https://thenewstack.io/working-with-json-data-in-python/)and[SARIF](https://sarifweb.azurewebsites.net/)outputs, enabling you to adopt and integrate Opengrep OSS into your workflows; - An improved engine means more capable community rules by unlocking previously pro-only capabilities.
- Long-term assurance that future improvements and features won’t be locked into specific vendors.
Your contributions to Opengrep and PRs are regularly reviewed and accepted on merit, not contingent upon the commercial interest of any single company.

For developers, Opengrep was created to provide:

- Full access to all scanning capabilities without feature restrictions.
- Backward compatibility with existing workflows and JSON/SARIF outputs.
- Portable security rules that work across any environment.
- Community-driven feature development.
- Long-term stability through foundation governance.
## A Backlash Trend
This move mirrors industry trends, as popular open source projects are forked when the terms of use are changed to become more restrictive. A noteworthy example includes the Linux Foundation’s forking of HashiCorp’s [Terraform](https://thenewstack.io/terraform-gets-ai-boost-in-new-cloud-management-platform/) into [OpenTofu](https://thenewstack.io/opentofu-turns-one-with-opentofu-1-9-0/). The open source project Opengrep was initiated in response to what Semgrep describes as a license update, not a change.

However, since December, these updates have made using Semgrep for commercial purposes slightly more restrictive. The new Semgrep Community Edition is now part of a competing software-as-a-service offering.

Endor Labs has long supported open source initiatives and undertakes the significant task of applying security measures to open source code. Endor Labs’ platform, among other things, can be used to vet [GitLab](https://about.gitlab.com/?utm_content=inline+mention) and other repository code, which can often contain numerous vulnerabilities.

[Static Application Security Testing (SAST)](https://thenewstack.io/why-you-still-need-dynamic-application-security-testing/) enforces code standards and policy for code edits, commits and integration. [Aikido Security](https://www.aikido.dev/), Arnica, Amplify, Jit, Kodem, Legit Security, [Mobb](https://thenewstack.io/shifting-left-is-now-mainstream-for-developers-or-is-it/), [Orca Security](https://thenewstack.io/orca-security-launches-first-k8s-testing-staging-environment/) and others support and contribute to the Opengrep project. Companies like Endor Labs will provide resources, such as allowing their in-house engineers to work part-time on the project. Endor Labs has also contributed capital, hired two full-time engineers, and is looking “to add a couple more that are just working on Opengrep,” Badhwar said.
“We want application security teams around the world to be able to really rely on this important piece of software because our thesis is that the engine is ultimately an Opengrep engine. So, it’s not rocket science, but the value is for organizations and users to be able to write their own rules on top of this engine,” Badhwar said. “So, we really want the engine to be a commodity if built correctly and scaled correctly…We’re going to give people the freedom and flexibility to do that and really just make sure that this commodity of the open Opengrep engine, if you will, is well-built and well-scaled out for the needs of hundreds of thousands of people around the world.”

## The New Semgrep World
Under the new terms of use, Semgrep users will only have access to new features introduced as part of the community-contributed rules through its paid or commercial offering. Essentially, users will have to pay for those features. Additionally, other features have been moved behind a pay-for-SaaS platform. Semgrep has downplayed the new restrictions attached to the use of the SAST.

In a blog post,[ Luke O’Malley](https://www.linkedin.com/in/dlukeomalley/), founder and chief product officer of Semgrep, wrote:

We’re making a few updates to the Semgrep OSS engine and rules — now collectively named Semgrep Community Edition — to better distinguish their free community-focused nature from our commercial offerings, and to clarify that other vendors may not use Semgrep Community Edition rules as part of a competing Software as a Service offering.

Starting today:

- Semgrep Community Edition: Semgrep OSS is now named Semgrep Community Edition, reflecting its role as a free, community-focused tool.
- Rule License Change: Semgrep-maintained rules are now licensed under Semgrep Rules License v.1.0, so that they’re available only for internal, non-competing, and non-SaaS contexts.
- Output Clean-up: Certain Semgrep-internal fields in JSON and SARIF outputs are now reserved for our logged-in commercial engine.
- Experimental Features: Features previously marked experimental are now part of our logged-in commercial engine.
Meanwhile, Opengrep’s future consists of possible collaborations with and donations to “all foundations and all kinds of options “are certainly on the table,” Badhwar said. “We’re getting a lot of interest from different organizations,” he said. “We’re just looking for the best long-term home where it continues to receive the investment that it deserves and provides a foundation.”

When asked whether Opengrep could be donated to the [CNCF](https://cncf.io/?utm_content=inline+mention) as a sandbox project, Badhwar said it has not yet been decided whether the project should become a Linux Foundation project, or “something independent.” “The plan is to stabilize it, build on it, get the community behind it, and then transition it into a foundation,” Badhwar said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)