# The Feds Push WebAssembly for Cloud Native Security
![Featued image for: The Feds Push WebAssembly for Cloud Native Security](https://cdn.thenewstack.io/media/2024/12/aa7a059d-planet-volumes-92k84okjqrw-unsplash-1-1024x731.jpg)
The use of [WebAssembly](https://thenewstack.io/webassembly/) could become mandatory to meet security-compliance requirements while solving other ongoing security conundrums as [Wasm](https://thenewstack.io/what-makes-wasm-different/) becomes more widely adopted.

According to a [National Institute of Standards and Technology (NIST)](https://thenewstack.io/nist-secures-encryption-for-a-time-after-classical-computing/) paper, [“A Data Protection Approach for Cloud-Native Applications,”](https://doi.org/10.6028/NIST.IR.8505.ipd) released earlier this year, WebAssembly could and should be integrated across the cloud native service mesh sphere in particular to enhance security. The framework outlined in the paper may lead to future compliance requirements for WebAssembly or cloud native environments, while also setting the stage for broader use of WebAssembly for security in general.

The paper provides a comprehensive overview of how Wasm can be leveraged for data protection in modern cloud native application architectures, while also critically examining its security implications and areas for future development.

The paper emphasizes how WebAssembly modules, with their in-situ or in-proxy approach, make WebAssembly a strong candidate for data categorization as data travels between services. With Wasm, data checks across any type of data distributed across one or more cloud native environments are provided.

The need for Wasm’s proxy reach and extended capabilities has become especially apparent as SaaS solutions and the need to transport more data through these pipes much more securely. “The SaaS thing that happened over the past 10 years where you’ve got a lot of products that send the data to a SaaS environment from a customer’s cloud environment: It doesn’t sit very well with cybersecurity, and it adds friction,” [Wesley Hales](https://www.linkedin.com/in/wesleyhales) from [LeakSignal,](https://www.leaksignal.com/) told The New Stack. Hales wrote the paper with [Ramaswamy Chandramouli,](https://www.linkedin.com/in/ramaswamy-chandramouli-64b8446) a supervisory computer scientist at NIST. “You go from very friction-filled installations to get what you need to understanding network traffic. What Wasm does is it bypasses all of that because it is running inside of envoy proxy today in many environments.”

In the cloud native world, all data traffic is forced through the [service mesh](https://thenewstack.io/service-mesh/) [Istio](https://thenewstack.io/istio-1-23-drops-the-sidecars-for-a-simpler-ambient-mesh/)’s proxy and Wasm by its modular or “sandboxed” design. “You may have 10,000 containers sitting behind an Istio proxy, while all the logging traffic, all the web traffic, even the database traffic all has to go in the proxy and then to wherever the destination is,” Hales said. “So we get to look at all that with Wasm.”

Beyond Istio’s proxy, Wasm covers in a more extensive way than [eBPF](https://thenewstack.io/ebpf-is-coming-for-windows/) can, covering data transfers through HTTP, gRPC or [GraphQL](https://thenewstack.io/graphql-federation-the-missing-api-for-your-platform-strategy/), or wherever the network traffic goes, Hales said. “It doesn’t matter since they’re still all traveling through that pipe of layer seven through layer four,” Hales said.

The NIST paper’s analysis correlates with [Fermyon](https://www.fermyon.com/?utm_content=inline+mention)’s open source SpinKube security capabilities in use. “WebAssembly is unique in its dual focus on security and portability,” [Matt Butcher,](https://www.linkedin.com/in/mattbutcher) Fermyon co-founder and CEO, told The New Stack. “While that design was necessary for the browser environment, it’s precisely the reason WebAssembly is such an excellent fit for the cases NIST outlines.”

## Big Government
An NIST paper is mainly published to provide information based on established scientific methodology. While it is not a part of the U.S. federal government’s [Executive Orders on Improving the Nation’s Cybersecurity,](https://www.gsa.gov/technology/it-contract-vehicles-and-purchasing-programs/information-technology-category/it-security/executive-order-14028) the paper’s findings carry significant weight in the community. WebAssembly’s security benefits described in the paper in question here could find their way into mandated compliance and, why not, one day, into a U.S. government executive order. Already, [Google](https://cloud.google.com/?utm_content=inline+mention) and Microsoft are working on protocols described in the paper, for example, for undisclosed projects.

“NIST has a long history of research and development in the hard sciences, including in computer science,” Butcher said. “Because their science is ‘in practice’ (such as with the atomic clock), I find their perspective to be respectful for both theory and practice.”

Key findings the paper reveals include (in addition to an in-depth analysis of WebAssembly’s history, structure and other background information):

Wasm modules offer several advantages for data protection, including:

- Extensibility of proxies without modifying core code.
- Security and isolation through sandboxing.
- Portability across different platforms.
- Potential for better performance compared to traditional proxy extensions.
Key data protection techniques that can be implemented in Wasm modules include:

- Dynamic data masking
- User and entity behavior analytics
- Data loss prevention
Wasm modules can be used to protect data in various scenarios, including:

- Web traffic
- API security
- Microsegmentation
- Log traffic
- Large language model (LLM) interactions
- Credit-card transactions
The paper provides a detailed security analysis of the Wasm execution environment, covering aspects like:

- Memory model and safety
- Control flow integrity
- Protection against side-channel and injection attacks
The Wasm security model aims to protect users from buggy/malicious modules while providing developers with useful primitives for building safe applications.

Though Wasm offers many security benefits, some vulnerabilities still exist, such as potential for code reuse attacks and race conditions.

The paper emphasizes the need for continuous evolution of data protection techniques in Wasm modules to keep pace with increasingly sophisticated attacks.

Wasm modules can provide telemetry data for monitoring tools, enabling visualization of sensitive data flows.

The document highlights the transition of Wasm from browser environments to server-side applications, particularly in cloud native and microservices architectures, said [Torsten Volk](https://www.linkedin.com/in/torstenvolk/), an analyst at TechTarget’s Enterprise Strategy Group.

## Big Science
The authors note that WebAssembly fixes align with this new class of in-proxy applications to achieve these goals. The paper also highlights some well-known security attributes of WebAssembly. Larger cloud providers, in particular, are exploring this proxy-based approach to improve security using WebAssembly. While some implementations have encountered increased latency, efforts are underway to address these issues as standards are developed within the open source ecosystem. These efforts involve collaboration among cloud providers, serverless providers and WebAssembly suppliers, such as Fermyon and Cosmonic.

“Wasm could become the ideal ‘security guard’ for serverless applications due to its small size and high degree of portability,” Butcher said. “If they can solve the performance overhead, this could make a big impact on app-level security.”

The paper’s authors also describe how WebAssembly modules provide [observability](https://thenewstack.io/observability/) data through their reach, extending from the kernel outward. This observability is particularly valuable for monitoring sensitive data flows. However, as the authors caution, this approach must continuously evolve to address increasingly complex and sophisticated attacks.

“Telemetry used to be an add-on, a negotiation point between application developers and operations teams. Tooling in this space has boomed recently,” Butcher said. “WebAssembly’s bytecode format dovetails beautifully into today’s tooling, making it the easiest modern environment to instrument.”

For the time being, WebAssembly appears to be a strong candidate to mitigate the notorious security shortcomings of cloud native environments. Wasm has significant disruptive potential in many areas, including security being one of them. All this technology needs is large-scale production deployments by big-name vendors to show to the world, including VC firms, that the promise is real,” Volk said. “I can definitely see Wasm-based ‘security agents’ patrol [Kubernetes](https://thenewstack.io/kubernetes/) clusters to keep the bad guys out.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)