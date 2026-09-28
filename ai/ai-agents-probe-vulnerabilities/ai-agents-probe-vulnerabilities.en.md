**An OpenAI agent researching public medicine spending** bypassed security blocks and gained unauthorized access to public and non-public files on an Australian government Medicare statistics portal, the government there disclosed Thursday. The agent, which OpenAI said was running during an internal evaluation in June, also wrote files to an internal server, according to the complaint.

Transluce, an independent nonprofit AI research lab, analyzed public request logs from the URL scanning service urlquery.net and found autonomous agents attempting SQL injection, cross-site scripting, command injection, and path traversal against the University of New Mexico’s digital library, the public data platform Data USA, and the Australian Institute of Health and Welfare (AIHW). The agents tried to retrieve ordinary information, including a historical photograph, University of Iowa data, and local pharmaceutical data in Victoria, and the offensive behavior appeared only after normal retrieval methods failed.

Transluce ties the Data USA and AIHW activity to an agent swarm that it says OpenAI previously confirmed originated from the company, based on shared targets, tactics and timing.

A day after [Transluce published its findings on Wednesday](https://transluce.org/agent-activity), Australian Prime Minister Anthony Albanese disclosed that an OpenAI agent researching public medicine spending bypassed blocks on a Services Australia Medicare statistics portal in June and gained unauthorized access to public and non-public files. OpenAI, which said the agent was running during an internal evaluation, notified the Australian government on September 10. According to Albanese, the agent also wrote files to an internal server.

The incidents have not been publicly confirmed as the same activity. However, OpenAI [told the Australian Broadcasting Corporation](https://www.abc.net.au/news/2026-09-24/openai-agents-plotted-to-access-data-amid-medicare-hack/107189504) that much of what Transluce documented overlaps with cases in its ongoing review of misaligned model activity.

> Transluce ties the Data USA and AIHW activity to an agent swarm that it says OpenAI previously confirmed originated from the company, based on shared targets, tactics and timing.

## Probing public data providers

On May 25 and 26, agents trying to retrieve a photograph from the University of New Mexico’s Valmora collection ran into repeated failures. They responded with seven vulnerability probes against the service. The probes included an attempt to execute a system command, a path traversal request targeting /etc/passwd, and a SQL injection string containing UNION SELECT; they also arrived alongside a burst of 80 requests aimed at the image, although none appear to have succeeded.

Two days later, agents gathering University of Iowa data from Data USA hit errors caused by a malformed query parameter and followed those errors with 12 vulnerability probes against the API, covering SQL injection, reflected XSS, server-side template injection, path traversal, and command injection.

## Cloudflare blocks, staging server workaround

The AIHW case on June 20 and 21 followed a very similar pattern. While trying to download pharmaceutical spending data from an AIHW Tableau dashboard, the agents ran into Cloudflare’s bot protections. One of them responded within minutes by testing the dashboard with a reflected XSS payload, although Cloudflare stopped it before it reached the application.

Transluce found no evidence that the probe succeeded, and AIHW says there is no evidence that non-public information was accessed. The agent ultimately found the same public dataset on AIHW’s pre-production server at pp.aihw.gov.au, and retrieved it through more than 100 scans.

> The agent ultimately found the same public dataset on AIHW’s pre-production server at pp.aihw.gov.au, and retrieved it through more than 100 scans.

The earliest clear sequence Transluce documented dates to March 6, when an agent tried to pull drug-enforcement statistics from the API of Thailand’s Office of the Narcotics Control Board. A direct request returned no page content, and adding a JSON format parameter changed nothing, so the agent routed the page through r.jina.ai three times and got text back with the Thai province names garbled.

Then, it wrote a custom Base64-encoded script and submitted it through urlquery.net, effectively using the service’s remote scanning browser to run its own client-side JavaScript against the data. That script ran into the same parsing problem, and a later attempt through Jina triggered a redirect to localhost that got the entire API blocked by Jina for an hour.

Beginning in mid-April, Transluce found the same technique across thousands of agent requests on urlquery.net, and on June 14 agents used the service’s browser to create a disposable email inbox and then tried to register a urlquery.net account with it. Registered users can make their scans private, which means the public records Transluce analyzed may understate how much of this activity actually took place.

An agent with web access isn’t limited to the software its developer gave it because remote browsers, proxies, URL scanners, and other public services can fill in the gaps, which gives the agent ways to make requests or run code that its own environment doesn’t provide.

## Egress controls for AI agents

Instructions won’t be enough if the agent can still send whatever it wants over the network. For narrowly defined jobs, outbound traffic can be limited to approved hosts, a closed-by-default approach also used for [securing AI agent sandboxes](https://thenewstack.io/securing-ai-agent-sandboxes/). Research agents may need to reach more of the web, so the focus shifts to controlling where they can connect.

Guidance for [GKE Agent Sandbox](https://thenewstack.io/google-cloud-a-deep-dive-into-gke-sandbox-for-agents/) recommends isolated runtimes with default-deny network policies that open only the endpoints an agent needs. Public proxies, URL scanners, and disposable email services can stay blocked unless the job requires them.

Developers can also limit what an agent can send. So, instead of handing it a networking tool that accepts any URL or request body, an API integration can restrict requests to specific fields and formats. The runtime can then catch path traversal attempts, SQL injection strings, and executable markup before anything is sent. OpenAI takes a related isolation approach in its [Agents SDK sandboxes](https://thenewstack.io/openai-agents-sdk-sandboxes/), and the company’s Responses API tech lead has said large enterprise deployments often call for agents that are isolated from the network entirely.

Repeated failures can also be a reason to pause a run, especially when an agent keeps hitting client errors, anti-bot challenges, or unexpected redirects and begins trying increasingly aggressive ways to get around them, as Transluce documented in several of these cases.

Keeping the original task, tool calls, and server responses in the same trace gives operators a better chance of catching that behavior change when a retrieval job starts generating encoded scripts, visiting staging domains, or sending exploit payloads, rather than discovering it later in someone else’s security logs.

> Repeated failures can also be a reason to pause a run, especially when an agent keeps hitting client errors, anti-bot challenges, or unexpected redirects and begins trying increasingly aggressive ways to get around them, as Transluce documented in several of these cases.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)