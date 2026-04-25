[Cursor](https://thenewstack.io/cursor-3-demotes-ide/) and [Chainguard](https://www.chainguard.dev/) are setting their sights on securing the open source dependency chain in [AI-generated code](https://thenewstack.io/ai-generated-code-needs-refactoring-say-76-of-developers/) — a problem that has grown sharper as agentic development moves from experiment to production.

The partnership, announced this week, gives Cursor access to Chainguard’s catalog of [hardened container images](https://thenewstack.io/dockers-sets-free-the-hardened-container-images/) and language libraries, embedding supply chain protections directly into the coding workflow. When Cursor’s agents select dependencies, they can now pull from Chainguard’s verified artifact store rather than raw public registries, the companies said.

## Agents don’t pause to check

Cursor’s President of Global Revenue and Field Operations, [Brian McCarthy,](https://www.linkedin.com/in/bkmccarthy/) tells *The New Stack*: “Partnering with Chainguard is another step in the direction of Cursor enabling secure agentic coding at scale. Recent supply chain attacks showcased how bad actors are working to manipulate the public tools and registries we’ve historically relied on to consume open source.

> “With agents writing the majority of code at top businesses around the world, new tools to help ensure the code is trusted and the ability to review and monitor at speed and scale creates a safer paradigm.”

“With agents writing the majority of code at top businesses around the world, new tools to help ensure the code is trusted and the ability to review and monitor at speed and scale creates a safer paradigm.”

Indeed, the timing reflects a real and documented threat pattern. Supply chain attacks against projects including Trivy, LiteLLM, telnyx, and axios have shown how easily compromised packages propagate through developer ecosystems. The so-called Shai-Hulud malware campaigns demonstrated that malicious actors are actively targeting the registries — [PyPI](https://thenewstack.io/whos-keeping-the-python-ecosystem-safe/), npm, Maven Central — that AI agents increasingly treat as ground truth for dependency resolution.

[Ross Gordon](https://www.linkedin.com/in/rosscgordon/), Staff Product Marketing Manager at [Chainguard](https://c67dcd9a.streak-link.com/C2uzyXrVldVCtIchdgDQ0p2d/https%3A%2F%2Fwww.chainguard.dev%2F), tells *The New Stack*, “Developers can instruct Cursor to migrate a project to Chainguard using natural language.”

Cursor then updates the project configuration, manages credentials, and routes dependency resolution to Chainguard’s catalog rather than public registries such as PyPI, [npm](https://thenewstack.io/18-popular-npm-packages-compromised-in-attack/), or Maven Central. This is handled within Cursor at the IDE or agent level, rather than through external network controls.

The core problem with [agentic development](https://thenewstack.io/agentic-ides-next-frontier-in-intelligent-coding/), as both companies frame it: dependency decisions happen at machine speed, without the manual review that has historically served as a last line of defense. “AI agents are making dependency decisions at a scale and speed no security team can manually review,” said [Dan Lorenc](https://www.linkedin.com/in/danlorenc/), CEO and co-founder of Chainguard, in a statement.

## A threat pattern already playing out

This integration focuses on mitigating the risk of open-source artifact vulnerabilities in AI-generated code by ensuring that libraries and container images come from trusted, publicly verifiable sources.

“This addresses a key layer of risk in agentic development: the automated selection of external artifacts at scale,” Gordon said. “The alternative is for developers to review every library being used, which can exceed 1,000 for some applications. Chainguard artifacts were not impacted by the recent supply chain attacks on popular open source artifacts, and our customers continued shipping rather than assessing if they were impacted or rotating credentials.”

Under the partnership, joint customers get access to more than 2,300 container images that Chainguard continuously rebuilds to incorporate upstream patches and ship with zero known CVEs at release time. The integration also covers millions of [versions of Python](https://thenewstack.io/what-is-python/), [JavaScript](https://thenewstack.io/introduction-to-javascript/), and [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) libraries built exclusively from publicly verifiable sources — targeting the backdoored binaries and malicious install-time scripts that have been the primary attack vectors in recent campaigns.

Provenance is handled through signed build attestations and reproducible build pipelines. Cursor manages credential configuration automatically, so developers don’t need to modify existing tooling or workflows to get coverage.

## Rebuilds within hours

Chainguard rebuilds its images with upstream source code fixes as they become available, continuously working to achieve a zero-CVE state.

“These rebuilds often occur within hours of a new release, with customers being able to either pull the new version directly from Chainguard’s registry or mirror to their artifact manager to pull new versions in an automated fashion,” Gordon said. “Container images are rebuilt frequently and are covered under our remediation timelines to ensure fixes are incorporated as soon as they are available.”

The partnership puts Chainguard squarely in the agentic development workflow rather than treating supply chain security as a post-hoc audit step — a positioning the company has been pushing as AI coding tools move from assistant to autonomous agent. For Cursor, it’s an acknowledgment that securing the code AI generates requires more than reviewing the output; it requires controlling what the agent pulls in to begin with.

The integration is now available to joint Chainguard and Cursor customers.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)