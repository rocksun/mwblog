Legacy [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) shops are sitting on a growing pile of unpatched vulnerabilities. [Chainguard](https://www.chainguard.dev/) says it has a fix for that.

This week, the company announced that [Chainguard Libraries](https://thenewstack.io/javascript-gets-supply-chain-security-with-chainguard-libraries/) for Java is generally available, adding CVE remediation to its secure [software supply chain](https://thenewstack.io/securing-the-software-supply-chain-a-2035-blueprint/) offering. The company is starting with the [Spring Boot](https://thenewstack.io/quarkus-gives-spring-boot-users-a-path-to-serverless-and-live-coding/) ecosystem, backporting fixes for critical and high-severity CVEs across spring-boot, spring-framework, spring-security, and h2database. Dozens of CVEs have been remediated at launch, the company says.

## More hostile environments, more vulnerabilities

The threat environment has grown significantly more hostile. AI-assisted scanning tools are generating vulnerability reports at a rapid pace.

“AI tools are now scanning open source projects at a rate that produces hundreds of new security reports each month,” writes [Ross Gordon](https://www.linkedin.com/in/rosscgordon/), Staff Product Marketing Manager at Chainguard, in a [blog post](https://www.chainguard.dev/unchained/chainguard-libraries-for-java-is-now-ga-and-includes-cve-remediation). “Spring received 482 new reports in April 2026 alone.”

That exposes a potentially painful problem for the 90% of Fortune 500 companies that rely on Java for core systems. Many of those organizations are using older framework versions — Spring Boot 2.7, for example, reached end of life in November 2023 and carries 143 CVEs across 79 projects, none of them patched upstream, the company says.

## Three options

Engineering teams are left with three options, Gordon explains:

1. **They could try to get an exception from their security team to use the library.** However, this doesn’t make them any safer and doesn’t solve the risk problem at hand.
2. **They could try to backport CVE fixes themselves.** However, this takes hours and doesn’t scale across teams using the same vulnerable library across hundreds of applications and APIs.
3. **They could try upgrading to a newer version that addresses the critical CVEs**. However, upgrading can take months (sometimes even a year) and prevents the team from building new product functionality that drives revenue. Like option two, it also doesn’t scale, as each team needs to upgrade to major versions while ensuring their applications don’t break in the process.

## A fourth path

Chainguard is offering a fourth path, Gordon explains. Teams swap their vulnerable library for a Chainguard-remediated version by updating a single reference in their pom.xml file. The remediated package includes a backported fix and ships under a new version identifier with a -0.cgr.N suffix, so the artifact appears clean to vulnerability scanners and auditors rather than flagging as a patched vulnerable version.

That distinction matters for audit purposes, Gordon says. Competing approaches that layer a patch on top of the original library leave the original version identifier visible to scanners, creating an awkward paper trail of a known CVE with a manual modification sitting on top of it.

Each remediated package ships with an [SBOM](https://thenewstack.io/sbom-everywhere-the-openssf-plan-for-sboms/) and provenance attestation. Wiz, AWS Inspector, [Grype](https://thenewstack.io/how-to-create-a-software-bill-of-materials/), and [Trivy](https://thenewstack.io/teampcp-trivy-supply-chain-attack/) all recognize Chainguard’s remediated Java libraries, with additional scanner support planned. The Chainguard console surfaces which CVEs are addressed in a given version, which other versions carry the same backported fix, and links to advisory details. Remediated versions are also accessible through Chainguard’s public [VEX](https://thenewstack.io/vex-standardization-for-a-vulnerability-exploit-data-exchange-format/) feed.

## Staying secure

Chainguard’s solution is that teams can stay secure at their current version while completing the upgrade on their own schedule, without the pressure of known critical CVEs forcing a rushed migration. For organizations managing hundreds of applications across multiple teams, the ability to apply a remediated drop-in without coordinating parallel upgrades could represent risk reduction at scale.

Supply chain security has become one of the hot battlegrounds in enterprise software, and [Chainguard has been among the more aggressive vendors](https://thenewstack.io/chainguard-os-packages-containers/) expanding its coverage.

The company [built its initial reputation around hardened container images](https://thenewstack.io/chainguard-its-all-about-that-base-image/). Extending that posture into the Java library ecosystem, specifically targeting Spring Boot across the Fortune 500, signals an intent to address vulnerability debt further up the dependency stack.

Finally, Ross adds, “This announcement is specific to Chainguard Libraries for Java. More broadly, Chainguard Libraries is a secure catalog of JavaScript, Python, and Java dependencies that replaces an engineering team’s reliance on [npm](https://thenewstack.io/18-popular-npm-packages-compromised-in-attack/), [PyPI](https://thenewstack.io/what-developers-can-grok-from-the-latest-pypi-package-attack/), and [Maven Central](https://thenewstack.io/how-camunda-automated-dev-releases-to-maven-central/). Today, [Chainguard Libraries for JavaScript](https://thenewstack.io/javascript-gets-supply-chain-security-with-chainguard-libraries/) (like our other languages) provides multiple layers of security controls, including building from source, cooldowns, malware and greyware scanning, and custom block policies.”

Chainguard Libraries for Java is available now.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)