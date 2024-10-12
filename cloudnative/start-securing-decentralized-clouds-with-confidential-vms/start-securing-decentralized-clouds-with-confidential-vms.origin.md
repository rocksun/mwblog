# Start Securing Decentralized Clouds With Confidential VMs
![Featued image for: Start Securing Decentralized Clouds With Confidential VMs](https://cdn.thenewstack.io/media/2024/10/f0c8c787-fabrizio-conti-athvihiobko-unsplash-1024x683.jpg)
[Fabrizio Conti](https://unsplash.com/@conti_photos?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/white-clouds-AtHvihIObKo?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
Despite constant improvements in encryption and cybersecurity, data breaches are becoming [more frequent](https://www.statista.com/statistics/273550/data-breaches-recorded-in-the-united-states-by-number-of-breaches-and-records-exposed/) year after year. But it’s not just that black-hat and white-hat hackers are playing an endless game of tug-and-war. There are more basic, fundamental flaws with handling your data.

Your sensitive information, like your bank statements, medical records, and business IP, is typically encrypted when stored and in transit. However, the most vulnerable stage is when it’s being processed. Cloud data involves [82% of breaches](https://secureframe.com/blog/data-breach-statistics), and 74% have a human element. This points to significant risks when data is actively used and processed, especially in cloud environments where people interact. Traditionally, data is unencrypted during computation, increasing risks.

Confidential computing allows data to be encrypted during this stage. Still, decentralized confidential computing takes it a step further, ensuring that *no one *(not even your cloud provider) can access your data while it’s being processed.

**The Technology**
One example of confidential virtual machine (VM) computing is [AMD Secure Encrypted Virtualization (SEV)](https://www.amd.com/en/developer/sev.html). AMD SEV is a hardware-based memory encryption feature integrated into AMD’s EPYC processors. It encrypts the memory of individual VMs so that even the hypervisor cannot access the plaintext data. This is achieved by assigning each VM a unique encryption key, managed by the AMD Secure Processor—a dedicated security subsystem within the CPU.

The encryption process operates transparently to the VM. Memory reads and writes are automatically encrypted and decrypted by the memory controller using the VM-specific key. This ensures that data remains encrypted outside the CPU boundary, rendering any unauthorized access attempts futile. While still responsible for resource allocation and scheduling, the hypervisor cannot intercept or manipulate the VM’s memory content.

Another essential component is a Trusted Execution Environment (TEE). A TEE provides a secure enclave within the main processor, isolating code and data from the rest of the system. TEEs ensure that sensitive computations occur in a protected environment, shielded from malicious software and hardware attacks. In the context of AMD SEV, the TEE is realized through hardware-enforced isolation mechanisms that segregate VM memory spaces.

The AMD Secure Processor plays an essential role in establishing the TEE by handling cryptographic operations and key management. It ensures that encryption keys are generated securely and remain inaccessible to unauthorized entities, including the hypervisor and system administrators. This hardware root of trust underpins the integrity and confidentiality guarantees provided by SEV.

**Decentralized Confidential VMs**
Before transitioning to *decentralized *confidential virtual VMs, it’s worth considering why we need them in the first place. After all, confidential virtual VMs are already out there, and you may not see the issue in sharing your personal data with Google, Amazon, or Microsoft. Up to [90%](https://storecloud.org/store-cloud/node-centralization) of decentralized networks still use centralized infrastructure like AWS to run critical operations. There are a few issues with this approach, however.

One is that centralized models have a single point of failure. By decentralizing the infrastructure, you can eliminate single points of failure and reduce trust dependencies inherent in centralized systems. Aleph.im and TwentySix Cloud have implemented this, using AMD SEV to deploy fully [decentralized confidential VMs](https://console.twentysix.cloud/) across a distributed network. Researchers and developers can sign up for their decentralized cloud, and free access is granted to those who qualify.

Each node in the network runs VMs with memory encryption enforced by SEV, ensuring that data remains confidential even in a multitenant environment.

This approach benefits from blockchain principles, where decentralization enhances [security and resilience](https://thenewstack.io/build-resilient-secure-microservices-with-microsegmentation/). The combination of TEEs and decentralized consensus mechanisms allows the network to maintain integrity in the presence of adversarial nodes. [Data and code within the VMs are protected](https://thenewstack.io/the-data-protection-challenges-of-kubernetes/) from external interference, and the decentralized nature of the network mitigates the risks associated with centralized control.

**Azure’s Confidential VMs vs. Decentralized Confidential VMs**
Microsoft Azure also offers confidential VMs using Intel SGX (Software Guard Extensions) and AMD SEV technologies. Azure’s [platform provides isolated execution environments within its cloud infrastructure](https://thenewstack.io/infrastructure-as-code-or-cloud-platforms-you-decide/), protecting data from other tenants. However, the infrastructure remains under Microsoft’s dominion, introducing trust assumptions regarding the provider’s security posture and governance.

In contrast, decentralized confidential VMs operate across a network of independently controlled nodes. The trust model shifts from relying on a single provider to a consensus among multiple participants. This decentralization reduces the risk of systemic vulnerabilities and coercion by external entities. Plus, it aligns with the Web3 user sovereignty and data ownership ethos.

Technically, Azure’s and decentralized confidential VMs leverage AMD SEV for memory encryption and isolation. However, the deployment models differ significantly. Azure’s solution is confined to its data centers, while decentralized VMs span heterogeneous environments. The latter introduces key management, attestation, and coordination complexities but offers enhanced resilience and trust decentralization.

**Practical Applications and Implications**
Let’s look at some of the real-world applications of decentralized confidential VMs. With all the coverage around privacy issues, you might have guessed the first application: AI.

[Training machine learning models](https://thenewstack.io/machine-learning-for-real-time-data-analysis-training-models-in-production/) often involves sensitive datasets containing personal or proprietary information. Deploying training processes within decentralized [confidential VMs allows organizations to harness distributed computational](https://thenewstack.io/brendan-burns-everything-you-need-to-know-about-confidential-computing-and-containers/) resources without exposing raw data. The models benefit from federated learning, aggregating insights without compromising individual data privacy. [LibertAI](https://libertai.io/), for example, is exploring how Aleph.im’s confidential VMs can be leveraged to run secure, large-scale AI deployments without exposing sensitive personal data.
More broadly speaking, any type of analytics on data can be risky. With decentralized confidential VMs, we can get those analytics-drawn insights without the privacy risks associated with unencrypted and/or centralized computation. Enterprises can perform analytics on encrypted datasets across decentralized nodes. Homomorphic encryption and secure multiparty computation techniques can be employed within confidential VMs, enabling insights without decrypting the data. This mainly benefits industries bound by strict regulatory compliance, such as healthcare and finance.

Another use case is secure decentralized finance (DeFi) protocols and trading algorithms. DeFi platforms can execute complex financial contracts and trading strategies within confidential VMs. Private keys and transaction data are processed in an encrypted memory space, preventing the leakage of sensitive information. This enhances [security for automated](https://thenewstack.io/want-to-mitigate-risk-invest-in-automation/) trading bots and smart contracts handling significant financial assets.

Gaming and NFTs also benefit from this technology. Verifiable Random Functions (VRF) can be securely implemented within confidential VMs, ensuring fair and transparent generation of random numbers for game avatar traits, lotteries, and more.

Ultimately, as the world shifts towards greater transparency, security, and privacy, decentralized confidential VMs represent more than an incremental improvement — they offer a paradigm shift in secure computing. They empower businesses and individuals to protect their information unprecedentedly, ensuring no centralized entity can access their data.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)