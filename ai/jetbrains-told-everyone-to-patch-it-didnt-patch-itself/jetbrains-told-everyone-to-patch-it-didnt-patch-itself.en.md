JetBrains is urging users of its Cadence cloud development service to rotate credentials and treat previous executions and their outputs as untrusted after attackers exploited a critical TeamCity vulnerability on a server the company failed to patch.

The irony is hard to miss. JetBrains disclosed [CVE-2026-63077](https://blog.jetbrains.com/teamcity/2026/07/cve-2026-63077/), a critical vulnerability in TeamCity On-Premises, on July 27. The flaw allows an unauthenticated attacker with HTTP or HTTPS access to a vulnerable TeamCity server to execute arbitrary operating system commands with the privileges of the TeamCity server process.

By August 7, the company announced that attackers were already exploiting unpatched TeamCity servers.

But one vulnerable server was still exposed: JetBrains’ own.

“The server should have been patched as part of our response to the vulnerability, but it was not,” JetBrains acknowledged in its disclosure of the Cadence incident.

> “The server should have been patched as part of our response to the vulnerability, but it was not,”

## Cadence’s unpatched TeamCity server

Attackers targeted `api.cadence.jetbrains.com`, which is the server behind Cadence, JetBrains’ cloud compute service for PyCharm. JetBrains found out about the attack on August 23 and took the server offline the next day. Their investigation shows that malicious activity started on August 8, so the affected period is from August 8 to August 24.

Cadence integrates with PyCharm via an optional plugin, giving developers the ability to run projects on cloud compute resources. TeamCity sat behind the service, orchestrating those workloads.

That put the compromised server in a particularly sensitive part of the development environment.

## Exposed credentials and source code

JetBrains says the attackers got hold of a complete Cadence server backup from 2024, potentially exposing everything stored in it, including credentials, configuration files, artifacts, and logs.

The company also confirmed that multiple AWS IAM users and their associated credentials were compromised, including IAM users belonging to JetBrains employees who had used Cadence.

Attackers accessed files in S3 buckets within JetBrains AWS accounts used by the service. JetBrains is still determining the full scope and says it does not yet know whether customers’ storage buckets were accessed.

Developers using the PyCharm plugin could sync project files to Cadence before running them, so source code and any credentials or configuration files included with those projects may also have been exposed.

The breach also exposed usernames, real names, email addresses, last-login timestamps, and last-accessed IP addresses. Credentials used during Cadence executions may have provided access to other connected services as well.

## Supply chain risk compounds quickly

JetBrains says users should consider any credentials or secrets stored in Cadence, included in the compromised backup or used during an execution to be compromised.

That could mean rotating AWS, Azure, and Google Cloud credentials, as well as tokens for GitHub, GitLab, and Bitbucket. JetBrains also warns about credentials for npm, Maven, NuGet, PyPI and container registries such as Docker Hub, ECR, GCR, and ACR.

Access to those registries creates another problem. An attacker with publishing credentials could push a malicious package that gets pulled into other projects, similar to [a recent npm attack that used provenance attestations to spread through the software supply chain](https://thenewstack.io/npm-supply-chain-worm-attack/).

The warning also covers Slack tokens, webhooks, API tokens, SSH and deployment keys, service account credentials and signing keys or certificates.

Anything run through Cadence during the affected period, including the resulting output, should also be treated as untrusted, according to JetBrains. The concern isn’t limited to exposed data and credentials; anything Cadence ran during that time could potentially have been altered.

CI/CD and remote execution systems often have access to private repositories, dependencies, cloud storage, package registries and deployment systems. Their central role in software delivery is [part of what has made CI/CD infrastructure an acquisition target](https://thenewstack.io/anthropic-mendral-cicd-acquihire/) and also gives attackers more places to go after gaining access. Once the environment itself has been compromised, developers can’t assume the credentials that passed through it or the artifacts it produced are safe.

> Once the environment itself has been compromised, developers can’t assume the credentials that passed through it or the artifacts it produced are safe.

## Audit logs reveal lateral movement

Changing potentially exposed credentials is only part of JetBrains’ advice. Users also need to check if those credentials were used elsewhere and if anything changed in systems connected to Cadence.

JetBrains recommends checking source control audit logs for unexpected repository clones or downloads, unauthorized commits, and changes to repository secrets or webhooks. Users should also look for new or changed personal access tokens, API tokens, and SSH keys.

> JetBrains recommends checking source control audit logs for unexpected repository clones or downloads, unauthorized commits, and changes to repository secrets or webhooks.

Cloud environments need the same careful review. JetBrains says users should look for unexpected IAM changes, new users or service accounts, and unusual access to storage like S3 buckets. Authentication logs can also show if credentials used in Cadence were later used from unknown places.

Package repositories and release histories should be checked for unexpected publications or changes, especially where Cadence had credentials that could publish packages or artifacts.

Since JetBrains treats previous Cadence executions and their outputs as untrusted, the investigation goes beyond just checking account logs alone. Developers may also need to review artifacts made through the service during the affected period and make sure they match trusted source code and expected build results.

The company published six IP addresses associated with detected exploitation: 150.109.230.104, 43.153.227.206, 62.210.127.48, 210.247.242.190, 15.235.225.205 and 152.233.30.18 with a warning that these indicators are not complete, so not seeing them does not mean an account or system was not compromised.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)