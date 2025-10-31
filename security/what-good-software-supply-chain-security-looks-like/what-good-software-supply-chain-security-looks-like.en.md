Organizations running their business on open source software are faced with a more aggressive and complicated security and compliance landscape than ever before. Malicious actors are bypassing transitional security tools by directly targeting developers, according to [Sonatype’s](https://www.sonatype.com/?utm_content=inline+mention)[10th annual “State of the Software Supply Chain” report](https://www.sonatype.com/state-of-the-software-supply-chain/Introduction). The number of malicious packages logged in 2024 increased 156% year over year, the report says.

While the cloud native and [DevOps](https://thenewstack.io/devops-moves-beyond-automation-to-tackle-new-challenges/) movements of the past decade-plus have made progress in promoting the idea of integrating security throughout the application development and delivery cycle, software vulnerability exploits are among the most commonly reported external attack methods (cited by 29% of respondents in Forrester’s 2025 report “[The State Of Application Security](https://www.forrester.com/blogs/application-security-2025-yes-ai-just-made-it-harder-to-do-this-right/)”), followed closely by software supply chain breaches (28%).

Faced with this increasingly complex security and compliance landscape, security teams, app dev leaders and IT execs alike are figuring out what good software [supply chain security](https://thenewstack.io/are-we-thinking-about-supply-chain-security-all-wrong/) looks like. Based on thousands of hours working with highly regulated industries — from public sector agencies to global financial services organizations — we’ve recognized some specific patterns.

## **Taking** **Hardened Images Beyond Table Stakes**

Hardened container images are a default in today’s IT environments. Many software vendors promise hardened images and [near-zero common vulnerabilities and exposures (CVEs)](https://thenewstack.io/the-cure-for-your-zero-cve-hangover-is-transparency/). However, to truly take advantage of hardened images, organizations need to ensure they have a defensible space within their infrastructure.

In fire-prone California, the notion of defensible space is monitored by Cal Fire. Homeowners are mandated to create 100 feet of defensible space around their buildings by removing material that could turn into fuel for a fast-moving fire from the perimeter of their property.

Similarly, removing extraneous material from your container images accomplishes the same goal. Each additional line of code in your software is an opportunity for a bug to be introduced that a hacker can exploit.

By removing packages and dependencies that aren’t required to run an application, there are fewer chances for something to go wrong that a bad actor can use to their advantage. Catastrophes happen when a sufficient number of things fail at once. So even if you can’t eliminate risk entirely, reducing the points of failure can improve your odds of withstanding an attack.

Distroless images remove everything except what is absolutely required for the software to run. This not only makes the image lighter, taking up less space on your machine — it also makes your apps more secure by reducing the available attack points.

For developers who need the ability to dynamically add libraries to a container runtime, distroless images are not the right option. The distroless form factor shines when an application has passed the proof-of-concept phase and the scale of trade-offs tilts from ease of use toward reducing risk of exploitation.

Distroless images are a must-have for teams that are ready for state-of-the-art container security in their infrastructure. Not everyone will be able to start with this type of image, but teams that are already doing sophisticated things like air-gapped or disconnected networks, zero-trust or mandatory access control authorization models will be right at home using distroless images.

By creating a “clean room” environment in the container, distroless images are not designed for humans to work in because they only have the bits needed by the low-level binaries of the application. But because they lack the human-oriented parts of the operating system — like shell, package manager, filesystem tools — they are that much harder for a hacker who somehow made it into the container to exploit.

Plus, the container image size is vastly smaller because it sheds a lot of excess weight that those tools require. It makes the container more secure at the expense of ease of use when it comes to debugging and troubleshooting.

However, new tools are being developed in this ecosystem to make distroless containers easier to work with, thus raising the bar of defensible space and proactive security for everyone in the industry.

To be sure, distroless images are less convenient but more secure. This is why it’s best to make them an optional format for the most popular apps. More advanced users will have the appetite for this level of security and understand the trade-off.

### **Comprehensive Coverage**

A catalog of images built the right way with security in mind is great, but what if the application or component your developers need isn’t in that catalog?

If developers are frequently leaving the walled garden of your [trusted supply chain](https://thenewstack.io/build-software-supply-chain-trust-with-a-devsecops-platform/) because they can’t find what they are looking for, you can no longer make claims about the compliance of your platform. And these exceptions may be introducing [risk that is not being tracked or mitigated](https://thenewstack.io/mitigating-safety-risks-with-ai-powered-applications/).

This is why having a catalog with sufficient coverage of the apps and open source projects your platform users need is crucial to a successful compliance story. Without it, the promise of open source compliance is an empty one.

### **Accreditation Optimized Images**

Most compliance requirements and framework controls are based on NIST 800-53 and the Risk Management Framework (RMF) that implements and manages those controls. Finding a vendor who understands the security and compliance landscape deeply is critical.

Furthermore, vendors who design images to meet those controls out of the box can improve your security posture, ensure you are meeting basic compliance requirements. Those vendors can greatly reduce toil and provide templates to respond to the controls and how the images meet them.

### **OS Package Format**

Many organizations may need to customize the standard images they are using to meet their needs. Having an industry-standard package format, such as [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) Package Manager (RPM), is a safe way to do that.

Some other hardened image providers only support [Alpine Package Keeper (APK)](https://wiki.alpinelinux.org/wiki/Alpine_Package_Keeper), which is not considered an industry standard and can make it harder to find packages in that format.

You will get a better security outcome with familiar technologies that are invisible to developers, so they can focus on code.

### **STIG Readiness**

The U.S. Department of Defense (DoD) requires all IT systems to adhere to the Risk Management Framework, as defined in [DoDI 8510.01](https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/851001p.pdf). An important part of RMF is the mandatory use of Security Technical Implementation Guides (STIGs) and Security Requirements Guidelines (SRGs) maintained by the Defense Information Systems Agency (DISA). Where a specific STIG for a product is unavailable, the relevant SRGs must be used instead.

Whether you are working with the DoD or in a highly regulated industry, it is important to understand these requirements, as they could affect your compliance posture. Look for tools and vendors who publish STIGs and demonstrate experience in following SRG requirements for risk management.

STIG Readiness is the process of preparing content that meets DISA’s standards, similar to the official DISA process. Products marked as “STIG Ready” typically require minimal changes if they were submitted for official DISA publication. When choosing a vendor to improve your security and compliance posture, refer to its STIG Readiness documentation.

### **FIPS and SLSA**

Developed by the National Institute of Standards and Technology (NIST), Federal Information Processing Standards (FIPS) are used when there are no acceptable industry standards or solutions for a particular government requirement. Although FIPS are developed for use by the federal government, many in the private sector voluntarily use these standards to secure their information and systems and establish strong information security programs.

To secure your supply chain and protect against cryptographic attacks, a curated catalog of FIPS-approved software sets the foundation for a stronger security posture. You can find the list of the most current FIPS [here](https://csrc.nist.gov/publications/fips). We recommend looking at FIPS 140-2 and 140-3, which specify the cryptographic and operational requirements for modules within security systems that protect sensitive information.

The Supply-Chain Levels for Software Artifacts  [(SLSA)](https://slsa.dev/) framework consists of a set of incrementally adoptable guidelines for supply chain security, established by industry consensus (as opposed to a governing body). It is designed to track code handling from source to binary to protect against infiltration by bad actors across the ever-increasing complexity of the [software supply chain](https://thenewstack.io/how-an-ospo-can-help-secure-your-software-supply-chain/).

Ideally, you have options for producing provenance attestations for all distributed assets so you can verify information about software artifacts describing where, when and how something was produced, that meets SLSA Build Level 3. The table below shows the requirements needed to be SLSA-compliant for Level 3 based on this specification.

### **Support for Disconnected Environments**

Many federal agencies and highly regulated organizations require isolating computer systems from external connections like the internet. Physically isolated — or air-gapped — systems protect highly sensitive data, and ensure the integrity of that data by blocking remote access to your systems. In many cases, they also support regulatory compliance standards related to data and privacy protection.

Disconnected or air-gapped networks are an effective way to increase your infrastructure’s security defenses. However, it comes at a cost, especially if the software you rely on was designed to always be connected to the internet. This is why it’s important to identify solutions early on in your systems design that can support disconnected environments well.

For a supply chain security strategy to be effective, updates to your software, especially those with CVE fixes, need to make their way over the air gap in a timely manner. You should expect your solutions provider to offer a well-documented procedure and tools for moving software from the internet to the disconnected environment.

The danger is if it’s too difficult to deal with software updates, the benefits of a disconnected network strategy will be muted by the impaired functioning of your supply chain. Luckily, there are tools, like the open source Bitnami [charts-syncer](https://github.com/bitnami/charts-syncer), which makes it trivial to synchronize and move chart packages and associated container images between chart repositories and highly regulated environments.

### **Automated Compliance Documentation**

Larger, security-conscious corporations and federal agencies are requiring software bills of materials (SBOMs), Vulnerability Exploitability eXchange (VEX) statements and in-toto attestations be included with any software they run or ship.

The ability to automatically gather compliance documents via APIs certainly simplifies the audit process; it can also reduce an organization’s mean time to recover from a potential software supply chain attack.

[Here](https://blogs.vmware.com/tanzu/speed-up-your-cve-response-time-with-sboms/) is an example of how SBOMs can reduce your time to recover from an outage or attack. This type of holistic view is critical for supporting continuous compliance.

## **From Building Blocks To A Whole House**

Ultimately, software supply chain security requires multiple tools and processes throughout the app dev and delivery cycle. It’s no longer enough to shift security left — it’s shift security everywhere.

As we see [cloud native patterns settle](https://thenewstack.io/cloud-native-app-platforms-new-research-shows-struggles-and-hope/) into Platform as a Service territory, it makes sense to architect your systems for a seamless security experience. There, outcomes are realized throughout the systems, so security does not hinder your ability to release high-quality software more regularly, recover from setbacks and attacks more quickly and make developers happier.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/01/1815de83-cropped-60bb08d8-rita-manachi-e1672939182784.jpg)

Rita Manachi is a marketing and communications pro with decades of experience in high tech. She is a marketing manager at VMware Tanzu.

Read more from Rita Manachi](https://thenewstack.io/author/rita-manachi/)

[![](https://thenewstack.io/wp-content/uploads/2025/10/4cb5420d-cropped-e0cac6f4-williamjimenez-600x600.jpeg)

William Jimenez is a product manager at Broadcom. His career in technology started in site reliability engineering. He would later use that experience to help leading enterprises implement the latest technology as a solutions architect at Rancher Labs and other...

Read more from William Jimenez](https://thenewstack.io/author/william-jimenez/)