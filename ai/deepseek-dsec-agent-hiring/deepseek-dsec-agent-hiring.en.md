Hundreds of thousands of AI agent sandboxes can already run concurrently on a single DeepSeek cluster. Now the company is staffing up to handle what happens as that number — along with its training, evaluation, and other backend workloads — keeps climbing.

[Cui Tianyi](https://www.linkedin.com/in/tianyicui/), who joined DeepSeek in March and works on its Harness team, the group responsible for the infrastructure and environments used to run and evaluate agents, [announced in an X](https://x.com/tianyi) post that roughly 150 engineering positions on September 7, with the hiring concentrated in server-side engineering and Agent Elastic Compute rather than AI research. The work spans operating systems, virtualization, networking, storage, scheduling, and the control-plane services that coordinate those resources.

Cui said DeepSeek’s existing backend systems will need upgrades, maintenance, and rewrites as workloads grow. One such system at the center of that scaling challenge is DeepSeek Elastic Compute, or DSec, the sandbox infrastructure DeepSeek built to execute agent workloads during post-training and evaluation.

> Cui said DeepSeek’s existing backend systems will need upgrades, maintenance, and rewrites as workloads grow.

## Four sandboxes, one SDK

Agent workloads require more than GPUs for inference, with each agent also needing an isolated environment to run code, call tools, change files, and collect the results.

DSec supports four types of those environments through the same Python SDK. Simple function calls go to pre-warmed containers, while Docker-compatible containers handle jobs that need a persistent environment. DeepSeek uses Firecracker microVMs when stronger isolation is needed and QEMU virtual machines for workloads that require a full guest operating system.

That range means the same infrastructure can handle anything from a simple tool call to a software-engineering task that needs an entire OS. It’s a similar challenge to the one the rest of the industry is bumping into as agents move from demos to production. OpenAI, for instance, recently [designed custom silicon](https://thenewstack.io/openai-jalapeno-inference-chip/) specifically to address the compute pressure that agent workloads create, and DeepSeek [open sourced its own agent harness](https://thenewstack.io/deepseek-harness-open-source-plugins/) in August.

## Lazy loading agent environments

Every sandbox needs its own environment, but copying complete container or VM images onto every host would consume enormous amounts of storage and network bandwidth while adding to startup time. DeepSeek gets around that by tying DSec into 3FS, the distributed filesystem it originally built for its AI infrastructure, and keeping container base images and filesystem commits as read-only layers backed by 3FS.

The metadata stays local, but the underlying data blocks are fetched only when they’re actually needed. MicroVMs use a similar setup, sharing their read-only base layer through 3FS while writes from individual sandboxes are kept in local copy-on-write layers.

[DeepSeek says DSec reduces duplicate page-cache usage](https://api-docs.deepseek.com/news/news260424/) across virtualized environments and reclaims memory to allow safe overcommitment, while changes to the container runtime cut the CPU overhead of each sandbox.

The team also had to deal with spinlock contention inside the container runtime. At small scale, the CPU time spent there barely registers. At scale, it limits how densely those environments can be packed onto each host.

> DeepSeek says DSec reduces duplicate page-cache usage across virtualized environments and reclaims memory to allow safe overcommitment, while changes to the container runtime cut the CPU overhead of each sandbox.

## When replay breaks training

During reinforcement learning and other post-training workloads, large numbers of agent rollouts can be running at once, and jobs may be interrupted as compute gets reassigned. Starting over wastes everything the agent has already done, but picking up where it left off isn’t as simple as replaying its previous commands.

Some of those commands may have changed a file or otherwise altered the environment, so running them again could produce a different result or leave the training trajectory in the wrong state. DSec avoids that with a globally ordered trajectory log that records commands along with their results.

When a rollout resumes, DSec can fast-forward through the completed work using those recorded results rather than executing the commands a second time. That reduces the cost of interruptions across thousands of training and evaluation runs, while the same logs preserve a history of how each sandbox changed and allow earlier sessions to be replayed.

## Engineers, not researchers, wanted

The roughly 150 openings reach across DeepSeek’s backend, including the lower-level systems work behind Agent Elastic Compute as well as the services that support its models and agents.

[DeepSeek said in June](https://www.reuters.com/world/asia-pacific/chinas-deepseek-plans-least-double-staff-all-departments-2026-06-25/) that it planned to at least double the size of every department, but this round of hiring leans heavily toward the systems underneath its models rather than the models themselves. DSec is part of that work, with hundreds of thousands of sandboxes running concurrently and putting pressure on everything from how jobs are scheduled to how they recover after an interruption.

> The roughly 150 openings reach across DeepSeek’s backend, including the lower-level systems work behind Agent Elastic Compute as well as the services that support its models and agents.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)