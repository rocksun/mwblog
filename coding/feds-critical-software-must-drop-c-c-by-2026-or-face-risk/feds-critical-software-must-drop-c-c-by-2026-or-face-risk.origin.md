# Feds: Critical Software Must Drop C/C++ by 2026 or Face Risk
![Featued image for: Feds: Critical Software Must Drop C/C++ by 2026 or Face Risk](https://cdn.thenewstack.io/media/2024/10/543f458a-getty-images-bxeiwnalzai-unsplash-1024x683.jpg)
The federal government is heightening its warnings about dangerous [software development](https://thenewstack.io/software-development/) practices, with the U.S. Cybersecurity and Infrastructure Security Agency ([CISA](https://thenewstack.io/who-should-be-responsible-for-software-security/)) and the Federal Bureau of Investigation (FBI) issuing stark warnings about basic security failures that continue to plague critical infrastructure.

A recent report issued jointly by CISA and the FBI on [Product Security Bad Practices](https://www.cisa.gov/resources-tools/resources/product-security-bad-practices) warns software manufacturers about bad practices such as using memory-unsafe programming languages like [C and C++](https://thenewstack.io/out-with-c-and-c-in-with-memory-safety/).

“The development of new product lines for use in service of critical infrastructure or [national critical functions] NCFs in a [memory-unsafe language](https://thenewstack.io/white-house-warns-against-using-memory-unsafe-languages/) (e.g., C or C++) where there are readily available alternative memory-safe languages that could be used is dangerous and significantly elevates risk to national security, national economic security, and national public health and safety,” the report says.

## Three Categories
The report says bad practices are divided into three categories:

- Product properties, which describe the observable, security-related qualities of a software product.
- Security features, which describe the security functionalities that a product supports.
- Organizational processes and policies, which describe the actions taken by a software manufacturer to ensure strong transparency in its approach to security.
The report is aimed at software manufacturers who develop software products and services — including on-premises software, cloud services, and Software as a Service (SaaS) — used in support of critical infrastructure or NCFs, the report said

## Avoid Bad Practices, Follow Recommendations
Moreover, the report also encourages all software manufacturers to avoid these product security bad practices. And “By following the recommendations in this guidance, manufacturers will signal to customers that they are taking ownership of customer security outcomes, a key [Secure by Design](https://www.cisa.gov/securebydesign) principle,” the report said.

“This guidance certainly follows up on the U.S. government’s earlier statement on the matter, statements that date back to 2022, admonishing technology providers and enterprise adopters alike to adopt or migrate to memory-safe languages,” said [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/), an analyst at [Omdia](https://omdia.tech.informa.com/).

“Putting all new code aside, fortunately, neither this document nor the U.S. government is calling for an immediate [migration from C/C++ to Rust](https://thenewstack.io/can-darpas-tractor-pull-c-to-rust-for-memory-safe-overhaul/) — as but one example,” he said. “CISA’s Secure by Design document recognizes that software maintainers simply cannot migrate their code bases en masse like that.”

The guidance, while voluntary, represents CISA’s strongest stance yet on baseline security practices — putting companies on notice about what constitutes negligent software development practices when it comes to critical infrastructure.

## The Clock Is Ticking
However, the clock is ticking for software manufacturers. Companies have until January 1, 2026, to create memory safety roadmaps.

“For existing products that are written in memory-unsafe languages, not having a published memory safety roadmap by Jan. 1, 2026, is dangerous and significantly elevates risk to national security, national economic security, and national public health and safety,” the report said.

In addition, default passwords must be eliminated from admin accounts by the same date. These deadlines signal a shift from recommendations to expected standards.

The report also states that the memory safety roadmap should outline the manufacturer’s prioritized approach to eliminating memory safety vulnerabilities in priority code components (e.g., network-facing code or code that handles sensitive functions like cryptographic operations).

“Manufacturers should demonstrate that the memory safety roadmap will lead to a significant, prioritized reduction of memory safety vulnerabilities in the manufacturer’s products and demonstrate they are making a reasonable effort to follow the memory safety roadmap,” the report said.

“There are two good reasons why businesses continue to maintain COBOL and Fortran code at scale. Cost and risk,” Shimmin told The New Stack. “It’s simply not financially possible to port millions of lines of code, nor is it a risk any responsible organization would take.”

Yet, according to the report, critical infrastructure still suffers from “exceptionally risky” practices like:

- Default passwords.
- Direct SQL injection vulnerabilities.
- Lack of basic intrusion detection.
- Missing multifactor authentication.
## Open Source
Regarding open source software, the report says special attention should be paid to open source vulnerabilities. Other recommendations include:

- Companies must maintain software bills of materials (SBOMs).
- Required to cache dependencies rather than pulling from public sources.
- Need to contribute responsibly to open source projects they depend on.
“Software manufacturers should responsibly consume and sustainably contribute to the open source software that they depend on,” the report said.

The report also urges more transparency, stating that:

- Companies must publish vulnerability disclosure policies.
- Required to issue CVEs for all critical vulnerabilities.
- Must provide clear documentation about security issues.
- Expected to maintain six months of security logs.
## It’s a Good Thing
Finally, it is good that CISA is recommending that companies with critical software in their care should create a stated plan of attack by early 2026, Shimmin said. It’s good because it will give the industry more time to come up with a more skillful means of ensuring the safety of our critical software assets, he said.

“Those means will likely involve hardware manufacturing shoring up potential attack vectors and programming language maintainers coming up with things ideas like the [Safe C++ proposal](https://safecpp.org/P3390R0.html)), which calls for the creation of a superset for[ C++ that addresses memory safety issues](https://thenewstack.io/can-the-safe-c-proposal-copy-rusts-memory-safety) without forcing major code rewrites,” he said.

## Paper Tiger?
“CISA is putting its foot down on memory unsafe application, built with C / C++ or assembler. With the deadline leaving less than 15 months, it will see users and providers scramble to stay compliant, as numerous and critical assets of government systems still use C/C++,” [Holger Mueller](https://www.linkedin.com/in/holgermueller/), an analyst at Constellation Research, told The New Stack. “Now all eyes will be on provider and developers to see if that deadline can be achieved – we will see in a few months if this CISA order is a paper tiger, a toothed tiger or a largely complied with standard regulation. Time will tell.”

## Shifting to Memory Safety
According to [Tim McNamara](https://www.linkedin.com/in/timmcnamaranz/?originalSubdomain=nz), founder of [Accelerant.dev](https://accelerant.dev/) and author of [Rust in Action](https://www.manning.com/books/rust-in-action), the temperature is definitely rising for companies to build more secure software. The industry is being biased away from insecure practices, which is a healthy shift.

“The document still leaves plenty of wriggle room to maintain the status quo, however,” McNamara told The New Stack. “It seems that the authors are clearly mindful of overstepping their authority. Notice that terms such as ‘strongly encourage’, ‘should’, and ‘reasonable effort’ are used in the text.”

Moreover, the document’s requirements are also fairly light, McNamara said. New software should be written in a memory-safe programming language. Software producers with current products are being requested to produce a “memory safe roadmap” in 2025.

“This roadmap is the producer’s plan for reducing memory safety bugs over time,” McNamara said. “There are also important exceptions. Roadmaps are not required for products that have an end of life in 2030, despite the fact that lots of software has a tendency to linger for far longer than intended.”

McNamara noted that in 2007, [MITRE](https://www.mitre.org/) produced a report called [Unforgivable Vulnerabilities](https://cwe.mitre.org/documents/unforgivable_vulns/unforgivable.pdf) that listed a memory safety issue on top. Yet, these bugs are not treated as negligence in software development. “I don’t see other fields where it’s acceptable not to apply known solutions to major safety problems,” he said.

Still, “It’ll be interesting to observe how the industry responds to the invitation to comment, especially given that there’s an election in the intervening time,” McNamara said. “Hopefully the concerns will transcend political bickering.”

CISA has opened a public comment period on its guidance until December 16, 2024. Please visit the [Federal Register](https://www.federalregister.gov/documents/2024/10/29/2024-25078/request-for-comment-on-product-security-bad-practices-guidance) to submit comments.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)