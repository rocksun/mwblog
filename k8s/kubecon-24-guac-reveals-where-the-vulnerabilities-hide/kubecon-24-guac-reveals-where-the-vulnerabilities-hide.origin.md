# KubeCon 24: GUAC Reveals Where the Vulnerabilities Hide
![Featued image for: KubeCon 24: GUAC Reveals Where the Vulnerabilities Hide](https://cdn.thenewstack.io/media/2024/03/df7a3bf0-guac-1024x696.png)
![](https://cdn.thenewstack.io/media/2024/03/8cbb2856-kubecon24-eu-300x206.jpg)
KubeCon
So now your security team has a
[software bill of materials](https://thenewstack.io/sboms-sboms-everywhere/) ( [SBOM](https://thenewstack.io/a-good-sbom-is-hard-to-find/)) for its open source applications. What’s next? If you are [KubeCon + CloudNativeCon EU](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) March 19-22 in Paris, stop by the [Kusari booth](https://www.kusari.dev/about) (#M30) to learn more about the [Graph for Understanding Artifact Composition (GUAC)](https://guac.sh/), which puts all that SBOM data into a more readily-understandable graph data format, augmenting it with vulnerability data.
On Thursday, the
[Open Source Security Foundation](https://openssf.org/) (OpenSSF) [adopted GUAC](https://openssf.org/projects/guac/) as [an incubating project](https://openssf.org/blog/2024/03/07/guac-joins-openssf-as-incubating-project/). Open SSF will bring many things to GUAC, including access to and feedback from SBOM and [CycloneDX](https://cyclonedx.org/capabilities/vex/) domain experts.
“There’s a lot of a lot of tools generating [security] data, but not a lot of things taking all this information together and like actually utilizing it,” said
[Michael Lieberman](https://www.linkedin.com/in/michael-lieberman-65786ba/), Kusari co-founder and CTO, in an interview with The New Stack. “GUAC aggregates all this information into a graph database, which you can actually use for actionable insights.”
Kusari, Google and researchers from Purdue University and Citi developed GUAC, which attracted support from companies such as Yahoo,
[Microsoft](https://news.microsoft.com/?utm_content=inline-mention), [Red Hat](https://www.openshift.com/try?utm_content=inline-mention), Guidewire and ClearAlpha Technologies.
Thus far the project has attracted 50 contributors, 300 community members and more than 1,100 stars on GitHub.
GUAC was truly a community effort, Lieberman said.
Security academics have long suggested dependency graphs could be useful. Lieberman — who is an OpenSSF Governing Board and TAC member; as well as a CNCF Security TAG lead — saw a lot of interest from the commercial sector for a tool of this nature.
“Instead of us all building different things, we came together and started building something,” Lieberman said.
## How Does GUAC Work?
The current version is available
[as a beta](https://docs.guac.sh/guac-use-cases/), offering results via a standard Rest API, [GraphAPI](https://thenewstack.io/why-graphql-needs-an-open-federation-approach/), and by command line.
GAUC provides the data to display a
[detailed graph](https://thenewstack.io/linkedins-real-time-graph-database-is-liquid/) that visualizes all the software in an SBOM, including first-party, third-party or open source software. The software ingests SBOMS in either the [SPDX](https://thenewstack.io/improving-open-source-supply-chain-transparency-with-spdx/) and [CycloneDX](https://thenewstack.io/2023-the-year-open-source-security-supply-chain-grew-up/) formats.
It has a set of collectors to pull data from repositories such as
[Docker Hub](https://thenewstack.io/docker-hub-limits-what-they-are-and-how-to-route-around-them/). It can also take in data from local file systems, [Amazon Web Services](https://aws.amazon.com/?utm_content=inline-mention)‘ S3, [Google Cloud](https://cloud.withgoogle.com?utm_content=inline-mention), and external package repositories like GitHub Releases.
To augment this data, GUAC pulls in and integrates vulnerability data, via APIs, from sources such as the Open Source Insights’
[deps.dev](https://deps.dev/) and [Open Source Vulnerabilities](https://osv.dev/).
“We’re enriching the SBOMs with these other open source tools,” Lieberman said.
GUAC in collates this data and returns the information as a set of data nodes and relationships. These artifacts can be used to understand the gaps in software supply chain data, and pinpoint areas of weaknesses in the software stack.
You can query a graph to pinpoint the vulnerabilities within an SBOM, including transitive dependencies where one application depends on a library which in turn relies on a vulnerable element.
Beyond security, it can also highlight packages with restrictive licensing (which can cause a lawsuit).
![](https://cdn.thenewstack.io/media/2024/03/5a1d2c94-expandviewvisualization.png)
Is there a vulnerability in your command line interface? GUAC
[can show](https://docs.guac.sh/querying-via-cli/) you.
## Input from KubeCon
At KubeCon, the GUAC team is looking for more input from folks who feel they don’t have enough visibility into their supply chain issues. They are looking for heretofore undiscovered use cases.
They are looking for new data sources and feedback on new features, or features that should be added.
Last month, OpenSSF
[posted a set of principles](https://repos.openssf.org/principles-for-package-repository-security) for securing packaging repositories, establishing a taxonomy and a tier security maturity, from one to four.
As for Kusari itself, it is building a security platform based on GUAC and other tools. The company is contemplating offering it as a service, or maybe selling a version with additional analytics.
“Your software environments are becoming more and more complicated every year. And in order to understand those complex environments, you need to have tools to help out with that. And that’s where Kusari comes in” Lieberman said.
![](https://cdn.thenewstack.io/media/2024/03/588996aa-cliimage.png)
GAUC
[ exposes an image](https://docs.guac.sh/querying-via-cli/) that has log4j and text4shell vulnerabilities. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)