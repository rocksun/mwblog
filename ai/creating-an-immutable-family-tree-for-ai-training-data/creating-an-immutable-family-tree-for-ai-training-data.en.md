The race for every company to embrace AI has them combining myriad and often inconsistently documented datasets in their training, raising legal and ethical questions about where the data actually originated.

[MIT’s Data Provenance Initiative](https://www.media.mit.edu/projects/data-provenance-for-ai/overview/) audit of more than 1,800 datasets found that companies can’t reliably track where their AI training data comes from. In fact, the researchers have concluded that [authenticity, as well as consent practices and provenance, are broken](https://mit-genai.pubpub.org/pub/uk7op8zs/release/2) in AI, leaving companies without the [training data transparency](https://thenewstack.io/ethical-and-explainable-ai-are-startup-imperatives-in-2025/) necessary to understand the limitations of their AI models.

Lawsuits such as [The New York Times’ suit against OpenAI](https://www.reuters.com/legal/litigation/judge-explains-order-new-york-times-openai-copyright-case-2025-04-04/) and [evolving](https://thenewstack.io/regulating-ai-presents-confounding-issues/)regulations like the EU AI Act are adding pressure for companies using AI to get data transparency right. But proving the provenance of training data isn’t necessarily clear-cut, as vast and diverse datasets are combined in previously unimaginable ways.

Texas-based blockchain provider [Hedera](https://hedera.com/) is working with AI governance startup [EQTY Lab](https://www.eqtylab.io/), as well as chip makers NVIDIA and Intel, to provide a trusted record of data’s origins.

“It’s exciting to see all this happening [with AI], but it’s just happening so fast that the world is trying to catch up,” said [Leemon Baird](https://www.linkedin.com/in/leemon-baird/), co-founder of Hedera, in an interview. “I think there is fantastic potential here for good, but also quite a bit of potential for something to go wrong, and so it’s important to do a number of things, to have safety for AI.”

It’s not just that the data can be used for ill, but it might be violating copyright or permissioning regulations. And when datasets are combined, there’s “this whole family tree of where your AI came from, and all the different [datasets] that influenced it,” he said.

“If you suddenly discover one of those data sets is bad, you have to figure out, ‘Well, how far back do I have to revert my AI to get to one that isn’t bad?’” he said. “And if people have looked at what some of these data sets and signed off on it, you need to know, well, who is it that looked at it, and can you prove that they signed off on it?”

Its solution to the problem begins with an on-chip provenance-tracking architecture. Both [NVIDIA](https://developer.nvidia.com/blog/confidential-computing-on-h100-gpus-for-secure-and-trustworthy-ai/#:~:text=NVIDIA%20Confidential%20Computing%20using%20hardware,is%20established%20through%20the%20following:) and [Intel](https://docs.scrt.network/secret-network-documentation/introduction/secret-network-techstack/privacy-technology/intel-sgx) use a [trusted execution environment (TEE)](https://thenewstack.io/confidential-computing-is-transforming-data-encryption-in-healthcare-finance/) to securely store secret keys. When the AI model is trained, the TEE uses its private signing key to generate a digital signature that attests to the provenance of the model. This signature cryptographically proves that the model was created from a specific data set on a specific chip.

Next is the digital notary and certificate system called [Verifiable Compute](https://www.eqtylab.io/blog/verifiable-compute-and-hedera) that EQTY Lab created with Intel and NVIDIA to isolate sensitive AI operations and create tamper-proof records of every data object and code used in AI training and inference. A series of attestations originating from the TEEs can be used to describe entire AI pipelines.

The technology creates a detailed compute attestation that cryptographically links the inputs, compute and outputs of each specific session, creating an auditable record of exactly what was done each time. These certificates can cover different processes, computing environments and what was done by different organizations, creating an end-to-end record of the data’s lineage. Verifiable Compute can also enforce business policies and regulatory compliance requirements on the data.

The data’s digital signature, along with metadata about the training data and process, is then recorded on a distributed ledger such as open source Hedera. This provides an immutable, timestamped and publicly verifiable record of every operation performed on the data. The system can also track the “family tree” of models, including cases where models are combined or further trained, by chaining provenance records.

Baird considers blockchain an ideal way to prove data provenance.

“You could think of Hedera as being a big billboard, and anyone in the world can come up and write something on it, and once you have written it, we guarantee it will never be erased, ever, for the rest of the history of humanity. And we will put a little timestamp next to it that says when it was written there. No one will be able to come along and change it, and that little time that was written next to it will never be changed. This is what Hedera is. It is a ledger that the whole world can read and can never be changed, and you can trust the times in it.”

Blockchain provides:

* **Transparency:** The public ledger allows anyone to verify the provenance of a data set or AI model.
* **Immutability:** Once written, it cannot be changed or erased. The record is permanent and tamper-proof.
* **Decentralization:** Used by multiple independent organizations, no single one can alter the records, which reduces the risk of malicious acts.
* **Timestamps:** Each entry carries a trustworthy record of when it occurred.
* **No single point of failure:** As long as a majority of participants are honest, the data remains secure and accurate.
* **Support for complex provenance chains:** It can track complex histories, such as when models are combined, retrained or when permissions are granted and revoked.

“You know for sure that the whole world is seeing the same thing, and you know exactly on what date this happened. And no one can ever lie and pretend something happened in the past when it really didn’t. They can’t backdate it and say, ‘Oh yes, this was done earlier,’ or ‘This thing was done later,’ and pretend it was done earlier,” Baird said.

“You can find out that your AI is trustworthy. It’s written on Mount Rushmore for all the world to see that this AI model that you’re using is trustworthy. That’s what you do if you’re using somebody else’s AI and you want to know that you can trust it. Honestly, I think everyone on earth should be doing that.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

Susan Hall is the Sponsor Editor for The New Stack. Her job is to help sponsors attain the widest readership possible for their contributed content. She has written for The New Stack since its early days, as well as sites...

Read more from Susan Hall](https://thenewstack.io/author/susanhall/)