Enterprises are pouring billions into AI and getting garbage back. A new startup says it knows why and has built the first platform designed to fix it.

Clario launched from stealth Wednesday with $6 million in seed funding to tackle what co-founder and CEO [Yousuf Khan](https://www.linkedin.com/in/yousufakhan/) calls data ROT: redundant, obsolete, and trivial files inflating storage costs and poisoning AI projects at the source.

“Four years post-ChatGPT, enterprises have spent billions on projects that are failing to make a meaningful impact,” Khan says in a statement. “Garbage in, garbage out isn’t a cliché, it’s an incredibly costly mistake.”

Industry estimates put more than a third of all stored [enterprise data](https://thenewstack.io/how-precog-adds-business-context-to-make-enterprise-data-ai-ready/) in the garbage category. And Gartner projects that 60% of AI projects will be abandoned by end of year due to poor data quality. Clario’s own early customer work has pushed that figure higher. In tests with design partners, the company has found garbage rates as high as 60%, Khan says.

Khan, a five-time CIO who held the role at Pure Storage and Moveworks before becoming a general partner at Ridge Ventures, says he kept running into the same wall at every stop. “I tried to solve this multiple times with all the big file systems. I couldn’t do it,” he tells *The New Stack*. The problem only compounded as AI-generated content began flooding enterprise repositories after ChatGPT’s launch.

Co-founder and CTO [Madhu Vohra](https://www.linkedin.com/in/madhu-vohra/) brings the infrastructure side of the equation. She spent her career building the systems where this data ends up — architecting clustered SAN at NetApp, scaling engineering teams at Nutanix, and leading Oracle’s block and object storage in OCI.

“I’ve built major systems that enabled people to accumulate,” she tells *The New Stack*. “So here I am atoning.”

## How it works

Clario connects directly to enterprise file and content systems including [Google Drive](https://thenewstack.io/address-high-scale-google-drive-data-exposure-with-bulk-remediation/), SharePoint, OneDrive, Box, and Confluence — and scans metadata to surface garbage without ever opening the files themselves. Classification is currently heuristics-based, using file checksums, naming patterns, access timestamps, and format support status, Vohra says. AI and embedding-based detection are on the roadmap, she notes.

When Clario flags a file, it triggers a workflow via Slack or Teams, notifying the person who created or owns the content and asking them to keep, archive, or delete it. The system learns from those decisions to build an increasingly autonomous cleanup engine over time. Clario only gets paid when customers act on a flagged file. This is an outcome-based model that aligns the company’s incentives with actual data reduction.

The ROT breaks down into three buckets: redundant files (duplicates and near-duplicates), obsolete files (legacy formats no one can open, documents untouched for years, content from departed employees), and trivial files (hidden files, noise). Early customer analysis has uncovered terabytes of junk, including knowledge base articles for discontinued product lines and full-length feature films downloaded by former employees, Vohra says.

To avoid false positives, Clario’s model is tuned for precision over recall designed for flagging only what it’s confident is garbage.

“Anything which we think is difficult to decipher, we want to bring up,” Khan says, adding that the goal is to tackle low-hanging fruit first and build confidence before moving into more ambiguous territory.

## The AI cost angle

The timing argument is about more than storage bills. As enterprises build internal agents and [RAG](https://thenewstack.io/a-blueprint-for-implementing-rag-at-scale/)-based systems, the quality of the underlying data directly determines whether those systems work. Vohra puts it bluntly: “Did my AI hallucinate or did it because you fed it all 15 million files?”

Khan says he sees the issue in token economics: internal agents built on unclean knowledge bases force [LLMs](https://thenewstack.io/llm/) to sift through outdated policies, discontinued product documentation, and obsolete support articles, burning compute budget on noise.

“You’re literally processing tokens on garbage,” he notes.

One early customer with 5.5 million files found that more than 20% was data ROT — and that it traced back largely to four departed employees.

## Competitive landscape

Khan acknowledged the field is thin. Backup vendors and archiving companies have touched the edges of data cleanup, but none have built an end-to-end workflow from classification through employee notification to action and learning, he says. “If they were there, I would have used them,” he says. “I haven’t seen a company that’s done this.”

Vohra notes that compression and storage efficiency tools address the cost of bits, not the number of them. “The core of the problem continues to be that the 15 million files you have continue to be exactly those 15 million problems.”

## Investors and customers

“The enterprise data crisis isn’t new, but the cost of ignoring it today is becoming impossible to justify,” said [Saad Siddiqui](https://www.linkedin.com/in/saadsiddiqu/), Partner at Preface Ventures, says in a statement. “We backed Clario because they are the only company working to get enterprises to AI-ready on a foundational level.”

Clario has about a dozen customers in early analysis and deployment. The company is about six months old and plans to expand beyond file and content systems to image repositories, video stores, and knowledge bases in platforms like ServiceNow and Salesforce Service Cloud.

Khan puts the product vision simply: “Our goal is to make sure that data hygiene is a continuous process in the enterprise.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)