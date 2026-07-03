In January 2021, an attacker added a single line of code to a popular bash script. Tens of thousands of organizations downloaded that script and ran it as part of their normal continuous integration workflow. On each run, on each commit, in each pipeline, the script faithfully shipped every environment variable in the CI runner to an unfamiliar IP address. This went on for sixty-one days before anyone noticed.

The years since have not been kind to the hope that this was an anomaly. The XZ Utils backdoor of 2024, caught by accident when a Microsoft engineer noticed his SSH logins were running half a second slow, was the work of a patient maintainer who spent roughly two years cultivating trust before slipping a remote code path into a compression library that ships in nearly every Linux distribution.

The polyfill.io takeover, a few months later, turned a script embedded in hundreds of thousands of sites into a malware delivery network within days of the domain changing hands. The npm and PyPI registries have settled into a steady drumbeat of compromised packages that nobody bothers counting anymore. Codecov is no longer a cautionary tale. It’s the template.

> “Codecov is no longer a cautionary tale. It’s the template.”

What’s interesting about this story is not that a company called Codecov had a rough couple of months in 2021. It’s the security model that made the attack possible, which is not an aberration unique to one vendor. It’s a structural feature of how nearly all modern software gets built.

The thesis is simple: The pipeline is the perimeter. The moat is not in front of production. The moat is around the thing that deploys production.

## The perimeter problem

For twenty years, security architecture treated the production environment as the castle and everything outside it as wasteland. Firewalls, WAFs, network segmentation, and IAM policies mostly point outward. You can trust them about as far as you can throw them, which, given their intangible nature, is not very far.

The problem is that a modern production environment isn’t a castle. It’s a construct. Code commits become artifacts, artifacts become deployments, and deployments become running infrastructure with access to the customer database. Everywhere along that chain, automated systems hold credentials with privileges that, if you do not look too closely, effectively resolve to “do whatever you like.”

Your CI runner holds your AWS keys. Your build agent has your [container registry](https://thenewstack.io/open-container-initiative-creates-a-distribution-specification-for-registries/) credentials. Your deployment step can communicate with Kubernetes. The intern’s GitHub Action can, in principle, push to `main`. If any one of these is compromised, the “production” distinction becomes semantic.

> “Every new team, tool, and integration widens the set of things that can read your secrets, and the pipeline almost never gets the governance that the infrastructure it ships already has.”

The Codecov incident is a canonical example, but it is not exceptional. It is simply what happens when a tool with pipeline privileges is breached. Given enough tools and enough time, a breach becomes a statistical certainty. Scale is the variable nobody budgets for. Every new team, tool, and integration widens the set of things that can read your secrets, and the pipeline almost never gets the governance that the infrastructure it ships already has.

## What happened

Codecov produced a small bash script called the Bash Uploader. It collected code coverage reports from CI runs and shipped them back to Codecov for processing. To use it, you added one line to your CI config: a `curl` to fetch the script, piped directly into `bash`.

The script was hosted in a [Google Cloud Storage](https://thenewstack.io/google-cloud-a-deep-dive-into-gke-sandbox-for-agents/) bucket. Codecov also built and published Docker images of their self-hosted product, and somewhere in the intermediate layers of one of those public images, they had baked in an HMAC key for the Google Cloud Storage service account that controlled the bucket. This is the kind of mistake that happens to people who have a great deal on their plates.

On January 31, 2021, an attacker extracted that key from the Docker layer, used it to modify the Bash Uploader directly in the bucket, and began serving the modified script to every customer who downloaded it. The modification was a single added line, sitting at roughly line 525 of a 1,800-line script, which is, conveniently, the region where most people [stop reading code](https://thenewstack.io/future-of-code-reviews/) that purports to do something boring with code coverage. The line ran the env command, which prints every environment variable in the current shell, and POSTed the output to a server controlled by the attacker.

CI runners, as a matter of routine, contain every sensitive thing an organization owns: AWS access keys, GitHub tokens, deploy keys, database credentials, Slack webhooks, and API keys for every SaaS the deploy pipeline integrates with. The modified script faithfully exfiltrated all of it on every run for two months across tens of thousands of customers.

The compromise was discovered on April 1, 2021. It was neither Codecov nor an intrusion detection system that found it. It was a single customer who happened to be checksumming the downloaded script against the SHA256 that Codecov published, noticed they did not match, and emailed Codecov to ask whether that was on purpose.

The list of confirmed downstream victims includes HashiCorp, Twilio, Rapid7, and Confluent. The actual blast radius is unknowable because once exfiltrated credentials are used to clone private repositories, the trail runs through other people’s environments, picking up their secrets.

![Image of containers stacked on top of each other (Tim G for Unsplash).](https://cdn.thenewstack.io/media/2026/07/a86f8602-image-1024x683.png)

## The structural problem this exposes

It’s tempting to file Codecov under “Docker image hygiene mistakes” and move on. This is a mistake. The Docker layer issue is *how* the attacker got in. It is not *why* the attack was devastating.

The attack was devastating because of an assumption baked into almost every CI/CD pipeline on Earth: that any tool you have agreed to run in the pipeline can be trusted with every secret it holds.

The assumption is not crazy. It is just unenforced. A typical CI runner has no meaningful concept of “this step can see secret A but not secret B,” or “this step can call out to AWS but not to a random IP in another country.” Most pipelines hand the full credential bundle to every step that runs, on the reasonable-sounding theory that the steps were configured by people who work there.

> “The attack was devastating because of an assumption baked into almost every CI/CD pipeline on Earth: that any tool you have agreed to run in the pipeline can be trusted with every secret it holds.”

Any tool you `curl | bash` into your runner inherits your pipeline’s privileges. So does any GitHub Action referenced by tag. So does any container image you pull. So does any helper script that turned up in a dependency three releases back when nobody was paying particularly close attention. The list of things that can read your environment variables is the list of things that run in your pipeline, which is much longer than most security reviews acknowledge, and gets longer every quarter.

This is also why supply chain attacks have not slowed since 2021. The Codecov story has played out, with variations and a rotating cast, every few months, in different ecosystems. The attack class is structural. The fix has to be structural too.

## What the fix looks like

Three governance controls, taken together, would have turned the Codecov breach into a footnote. None are exotic. All require treating the pipeline as production infrastructure rather than a developer convenience.

**Verify what is actually running.** The customer who finally caught the attack did so by comparing a SHA256 checksum. Codecov had been publishing the hash. Almost nobody had been checking it. A pipeline should not execute arbitrary fetched code (scripts, containers, Terraform providers, GitHub Actions) without verifying signatures or checksums against a known, trusted source. Pinning Actions by commit SHA rather than by tag, verifying provider signatures, and running static scanners over your IaC before any deployment touches a cloud account are no longer specialist practices. Scanners like Checkov, TFsec, Trivy, and TFLint can run as a step in the pipeline itself, before any state is touched. These are table stakes. The cost of treating them as optional is paid in two-month exfiltration windows.

**Constrain where the pipeline can talk.** The Bash Uploader exfiltrated data by making an outbound HTTPS request from inside the CI runner to an arbitrary internet host. Most CI runners can do this because nobody told them they could not. Self-hosted or otherwise controlled runners, running inside a private network with egress restricted to a known allowlist, turn “POST env to a random server” into a failed network call. A runner that can only reach your VCS, your cloud APIs, and a declared set of external dependencies cannot be repurposed into a generic credential exfiltration tool, no matter what gets quietly inserted into one of its scripts.

**Stop handing the pipeline static secrets.** This is the single most consequential change, and the one the industry has been slowest to internalize. The reason env was such a productive command for the attacker is that most CI environments are stuffed with long-lived static credentials: an AWS access key valid for years, a GitHub PAT valid until somebody remembers to rotate it. Federated identity changes the shape of the problem entirely. With OIDC, the pipeline does not store any credentials. It presents a signed assertion describing which environment it is in, which workflow is running, and which commit is being deployed, and the cloud provider exchanges that assertion for a short-lived token scoped to exactly the operation about to happen. An exfiltrated assertion is useless minutes later. An exfiltrated token is useless within the hour and cannot be used outside the conditions described by the assertion.

A pipeline that authenticates to AWS, Azure, GCP, and Vault through OIDC, runs inside a network segment with egress allowlisting, and verifies the artifacts and providers it depends on is a pipeline where the Codecov scenario produces a malicious script that accomplishes very little. The `env` output contains no long-lived secrets. The exfil destination is unreachable. The modified script fails verification before it runs.

These controls do not prevent the initial compromise. They make the initial compromise uninteresting, which is the next best thing and, on most days, the achievable goal.

![Modern building exterior with colorful pipes and metal framework. (@heytowner for Unsplash)](https://cdn.thenewstack.io/media/2026/07/6dc67406-image-1024x727.png)

## Treat the pipeline like production

There is one more change, and it is more cultural than technical. The pipeline needs the same governance that production already gets. That means audit logs for every deployment, approval policies (preferably [policy-as-code](https://www.env0.com/blog/how-policy-as-code-enhances-infrastructure-governance-with-open-policy-agent-opa)) for changes that touch a sensitive scope, and [role-based access](https://www.env0.com/blog/custom-rbac-roles) so a developer cannot inadvertently hand the pipeline more privileges than their own role permits. It also means [drift detection](https://www.env0.com/lp/drift-detection-and-remediation), so the gap between what the code says and what is actually running stops being tribal knowledge and becomes a tracked, alertable fact.

> “These controls do not prevent the initial compromise. They make the initial compromise uninteresting.”

This is unglamorous. It is also the difference between a CI/CD system that is an attack surface and one that is an enforcement point.

Put these four controls side by side, and they describe a single idea. The pipeline deserves the same [continuous governance](https://www.env0.com/solutions/cloud-governance-and-risk-management) as the infrastructure it ships: not a one-time security review, but control that holds before a change runs, while it runs, and after it lands. Verifying what runs, constraining where it can talk, removing static credentials, and governing every deployment with audit trails and enforceable policy are not security features bolted onto a platform. They are governance applied to the part of the stack that has long been treated as a convenience, and applied the same way whether a team runs ten pipelines or ten thousand.

Your pipeline is a layer of your perimeter, and at the moment, it is your weakest. For most of its existence, it has been treated as a productivity tool rather than a security boundary. The Codecov attackers understood that in 2021. The next set of attackers, scanning public Docker images for one too many layers and now moving faster than anyone did five years ago, understand it too. If we do not understand it as well, we will keep paying a growing price.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/0a9a86e3-cropped-03077771-zrachidi2-600x600.jpg)

Zeen is a designer and builder that's been blessed to live and learn on three continents. He likes problem-solving, being helpful, and making useful things. He got his BSc in Computer Science, but got bored babysitting servers, so he went...

Read more from Zeen Rachidi](https://thenewstack.io/author/zeen-rachidi/)