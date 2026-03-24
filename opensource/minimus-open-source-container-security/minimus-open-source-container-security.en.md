Container security company [Minimus](https://www.minimus.io/) has outlined a new initiative to help open-source project maintainers strengthen the security and integrity of their software supply chains.

The [Minimus Open Source Program](https://www.minimus.io/open-source) will now allow eligible projects to access the company’s secure container images, Software Bill of Materials (SBOM) generation and analysis services, and its threat intelligence tooling at no cost.

## Reliance on ruggedized rigor

Software developers working with cloud-native tools and services that make use of containers know why an industrially ruggedized approach to container state is fundamental; it prevents privilege escalation or lateral movement across a cluster (where a malicious actor is able to move from one compromised node to another) that might lead to data loss or wider system failure.

Constructed around a template, a hardened container image is built according to strict configuration standards. It is stripped of extraneous and unnecessary tool functionality and code libraries that could introduce vulnerabilities. This smaller attack surface means that only core, essential processes can be executed within a live production Kubernetes cluster.

Minimus reminds us that open source software underpins a vast share of the world’s critical digital infrastructure. But, says the company, in real-world operational terms, open-source project maintainers lack access to the security tooling that enterprises take for granted.

The new program aims to solve this long-festering security problem, putting modern supply chain security directly in the community’s hands.

## Hmm, does this sound familiar?

But doesn’t that make this initiative sound a little like [Chainguard](https://thenewstack.io/chainguard-os-packages-containers/), with its specialism in ultra-minimal hardened container images? Come to think of it, isn’t Minimus doing what Red Hat does with [Project Hummingbird](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux/hummingbird), the open source giant’s zero-CVE (Common Vulnerabilities and Exposures) catalog of minimal, hardened images for developers?

[Kat Cosgrove](https://www.linkedin.com/in/katcosgrove/), head of developer advocacy at Minimus, sets the record straight and explains the extent of her organization’s ambitions in this space.

“Minimus is purely a security platform. We’re not trying to be the next Red Hat. Our priorities are slightly different, and you can see that in some of the product’s standout features. For instance, we support self-hosted registries, including full air-gapping. Our images are aligned with CIS and NIST benchmarks out of the box and don’t need to be individually verified by hand,” Cosgrove tells *The New Stack*.

She explains that her Minimus includes an advanced threat intelligence dashboard, allowing developers to prioritize mitigating the few remaining CVEs by exploitability rank. The company has also included a host of integrations, and developers can build their own workflows without writing any code. This way, Cosgrove says it’s easy to onboard and build Minimus into a team’s existing workflows.

> Where open source projects are left without access to the tooling needed to make software easier to develop and more secure, that model isn’t good for anyone…

## Which projects are eligible?

The program is open to open source projects using an [OSI-approved license](https://opensource.org/licenses) that meet minimum project health criteria.

Accepted projects receive access to hardened, compliant images from the Minimus Image Gallery, as well as custom image creation, Helm charts, and automatically generated SBOMs. Projects also receive real-time exploit intelligence to prioritize CVE remediation and patch efforts, as well as image updates in accordance with Minimus’ commercial SLAs.

“Where open source projects are left without access to the tooling needed to make software easier to develop and more secure, we don’t believe that model is good for anyone, i.e., not the maintainers and not the developers building on top of these projects,” Cosgrove tells *The New Stack*.

Projects accepted into the program can integrate Minimus images into their build pipelines, immediately reducing attack surface for their users. Maintainers will also gain visibility into dependencies and potential vulnerabilities through Minimus’s threat intelligence dashboard.

## The dawn of containers

For the big picture, from someone who was there at the dawn of containers, [Christopher “CRob” Robinson](https://www.linkedin.com/in/darthcrob/), chief technology officer of the OpenSSF and chief security architect of the Linux Foundation, is the man in the know.

“Containerized images have become the predominant way most developers and consumers interact with software today.  They provide an ‘easy button’ to quickly add capabilities to a solution a developer is composing, but who made them and how they did that isn’t always visible. Unfortunately, not all containers are made equal. Many misunderstand what a container should be, thinking it is more like a traditional virtual machine, rather than a layer of code and configs that integrates with other work. Consequently, they incorporate too many things into that image,” Robinson tells *The New Stack*.

“Minimizing your attack surface is a core tenet of cybersecurity: the less there is to monitor, update, or protect, the easier the defenders’ job becomes. Containers can save an organization time in creating and managing its base images. Harden minimized containers relieve security teams of the overhead of constant maintenance and reacting to the CVE de jure,” he tells us.

## 1200 hardened images (and counting)

Since its public launch in April 2025, Minimus has expanded its Image Gallery service to include over 1,200 hardened container images. The company has also shipped new capabilities, including [Image Creator](https://www.minimus.io/post/introducing-minimus-image-creator-create-custom-minimal-images), which enables enterprises to build and manage their own hardened images on the Minimus platform.

Minimus images are now supported by major cloud security platforms, including Aqua Security, AWS, Google Cloud, Orca Security, Snyk, and Wiz.

The technology proposition here seems clear enough to interpret. Maintainers want to reduce the attack surface of their projects, and, equally, developers who are consumers of open source want to build knowing they’re starting from a smaller attack surface.

That way, end users get a hardened, ruggedized, and essentially compliant application or data service, even if they remain blissfully unaware of the back-end galvanization.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)