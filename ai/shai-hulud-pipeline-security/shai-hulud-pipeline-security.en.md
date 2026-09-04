On September 15, 2025, npm’s registry did something unprecedented: Packages began updating themselves.

No maintainer ran `npm publish`. No pull request got merged. New versions just materialized, each carrying a hidden passenger that would go on to publish even more versions of more packages, on more machines, with no human involvement whatsoever. Between September 14th and 18th, more than 500 package versions were altered. The worm’s authors had their creation leave a calling card with an intriguing literary sobriquet: every stolen credential was uploaded to a new public GitHub repo named Shai-Hulud, after the untamable apex keystone species of Frank Herbert’s Dune book series.

> “What should we learn about trusting infrastructure from a worm that writes and republishes its own malware?”

That wasn’t the end of the story. Two months later, on November 24, a larger variant christened Shai-Hulud 2.0 was able to backdoor 796 packages, move its execution earlier in the install process to render developer triggers irrelevant, and salt the wound on its way out by deleting the user’s home directory if it couldn’t find credentials to steal or a way to spread. By spring of 2026, its offspring, Mini Shai-Hulud, had evolved from hunting generic developer secrets to specifically targeting credentials belonging to Claude, Codex, Cursor, and Gemini, and had come to the logical conclusion that AI coding tools are involved in all the most interesting projects, making them a ripe hunting ground.

The latest variant, named ChainDrop, appeared a few weeks ago, on August 4, 2026. In less than four hours, it compromised more than 400 packages by riding a legitimate, cryptographically signed release pipeline, which granted each poisoned version a valid SLSA provenance attestation. This allowed them to circumvent the very mechanism built to verify that a package hadn’t been tampered with. Even its command infrastructure was parked inside an Ethereum smart contract, rendering any domain blocklists moot.

## Who can you trust?

Every package manager and infrastructure registry runs on the same precarious assumption: installing something means running whatever’s in the package, sight unseen, with whatever permissions the install process has. When publishing required a person to sit down and do it, that assumption was safe enough.

> “If publishing can now be automated by non-human agents already in the environment, it is no longer safe at all.”

If publishing can now be automated by non-human agents already in the environment, it is no longer safe at all. In such an environment, the worm doesn’t need to convince anyone of anything. It simply needs one compromised credential and an install script. After that, the registry confers trust and credibility, and every subsequent dependency reinforces it.

## What happened

The strategy is brutally simple. A compromised npm package runs a postinstall script (in Shai-Hulud’s case, a single file called `bundle.js`) that searches the infected machine for anything resembling credentials, including npm and GitHub personal access tokens, AWS or GCP secrets, and whatever it can extract from a cloud instance’s metadata service. It downloads Trufflehog, a legitimate open-source secret-scanning tool, and uses it to confirm the validity of any credentials it finds. So, the silver lining is that you at least get a free security audit (of sorts) out of the infection.

Upon locating a GitHub token, it exfiltrates everything to a new public repo and, for extra credit, makes any private repos it can reach public as well, republished under the original name with a “-migration” suffix appended, perhaps to make it appear as if the victim had requested the move themselves. If it finds an npm token, it calls the registry’s API to list every package the compromised developer maintains, downloads them, injects itself into the `postinstall` step, bumps the version number, and republishes them. That’s it. No further input required. [Palo Alto Networks’ Unit 42](https://unit42.paloaltonetworks.com/npm-supply-chain-attack/) is moderately confident that the malicious script was partly written by an LLM, based on stylistic tells such as code comments and emoji embedded in the payload.

## We must not fear. Fear is the mind-killer.

This vulnerability isn’t specific to npm. Trade `npm publish` for `terraform apply`, and the mechanics hardly change. A Terraform provider pulled from a public registry, like an npm package pulled from its registry, is code that a publisher’s account [was trusted to ship](https://thenewstack.io/kubernetes-teams-trust-automation/), running with whatever access the machine that requested it holds.

A CI runner with a standing cloud credential and an open path to the internet is the same target as a maintainer’s laptop with a valid npm token: one a worm can compromise once and then use to spread itself to everything downstream of it, at whatever speed automation allows.

> “Attestation tells us where a package came from; it doesn’t say anything about whether the commit should exist at all.”

Up until now, the industry’s answer to this problem was provenance: sign the package, attest to the build, and prove cryptographically that what shipped and what’s reviewed match. ChainDrop is the answer to that answer. It didn’t forge a signature. It compromised a maintainer account with legitimate write access and let that account’s legitimate, signed pipeline build and publish the malware on its behalf. Attestation tells us where a package came from; it doesn’t say anything about whether the commit should exist at all.

## The fix

**Every dependency should be pinned to an immutable reference.** Terraform’s dependency lock file, `.terraform.lock.hcl`, has a recorded cryptographic checksum for every provider version since Terraform 0.14, operating on a trust-on-first-use model. Once a checksum is recorded, any future `terraform init` that doesn’t match it fails rather than accepting a swapped-out binary. Modules deserve the same discipline. Pin a module’s `source` to a full commit SHA, not a branch or even a tag, since tags can be moved or deleted at the origin in a way a commit hash cannot. Checkov’s CKV\_TF\_1 rule and TFLint’s module-pinned-source check both exist because reviewers keep forgetting this.

**Source providers and modules through a registry your organization curates.** The public Terraform registry, like the public npm registry, will resolve whatever its maintainers choose to publish. If a maintainer account is compromised, everyone downstream inherits the problem on their next `init`. Routing provider and module resolution through a private, versioned, allow-listed registry means the potential sources a deployment can pull from are controlled by somebody on your team, not the entire public internet’s worth of Terraform code.

**Credentials should be scoped to the deployment, not the developer or runner.** Every stage of Shai-Hulud’s lineage depends on a long-lived secret that sits still, whether a token in a `.npmrc` file or a key in a CI environment variable. [Short-lived, per-deployment credentials](https://thenewstack.io/securing-ai-agent-sandboxes/) issued through OIDC, an identity token traded for temporary cloud access at the moment a deployment runs and discarded the moment it finishes, mean there’s no standing secret for a Trufflehog pass to find. A worm can still steal a credential that lives in memory for the ninety seconds an apply takes, but it can’t steal one that was never written down in the first place.

**Control what a runner is allowed to talk to on its way out.** Every generation of this worm relied on an open outbound path: a webhook endpoint for exfiltration, the GitHub API for persistence, npm’s own registry API for propagation, and, in ChainDrop’s case, an Ethereum RPC endpoint chosen specifically because no domain blocklist could touch it. Restricting a runner’s egress to the handful of domains a deployment actually needs (the registry, the state backend, the cloud API), and nothing else, means any attempt the worm makes to phone home runs straight into a firewall before it ever leaves the building.

## Those that can destroy a thing, they control it

A build pipeline isn’t a convenience layer sitting tasteful and demure outside your security boundary. It’s production infrastructure, running unattended, typically wielding more standing privileges than the systems it deploys.

> “A build pipeline isn’t a convenience layer sitting tasteful and demure outside your security boundary. It’s production infrastructure.”

Pipelines weren’t built this way intentionally. They ended up like this because until these vulnerabilities were exposed, everyone treated them like plumbing, as if history weren’t replete with examples of plumbing used to evade defenses. Turns out, it’s also a perfect avenue for worms to get to the keys that protect your secrets.

Shai-Hulud figured this out within its first 24 hours. The industry is scrambling to catch up, in progressively more painful installments, paid every couple of months.

Software supply chains used to get compromised. Now, they get infected; and infections don’t wait; they spread. The humble worm that started as a credential thief has now learned to forge the very cryptographic proof meant to catch it. Its latest prey is the AI tooling teams use to speed up production. An unpinned reference and open registry pull are all it would take for this to spread to [Terraform providers and modules](https://thenewstack.io/build-terraform-modules-that-your-team-will-actually-reuse/). The only remedies are: pin what can be pinned; allow-list what can’t; scope credentials for what’s left. Close all paths out.

Otherwise, by the time you notice the next worm, it’ll have already spread to everything downstream of the one reference you forgot to pin.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/0a9a86e3-cropped-03077771-zrachidi2-600x600.jpg)

Zeen is a designer and builder that's been blessed to live and learn on three continents. He likes problem-solving, being helpful, and making useful things. He got his BSc in Computer Science, but got bored babysitting servers, so he went...

Read more from Zeen Rachidi](https://thenewstack.io/author/zeen-rachidi/)