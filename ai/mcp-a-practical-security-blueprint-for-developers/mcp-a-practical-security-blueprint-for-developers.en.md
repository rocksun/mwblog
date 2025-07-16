Imagine a world where your coding environment isn’t just a tool, but a true partner. It anticipates your needs, connects smoothly with your databases and infrastructure, and even talks to your command-line tools. This isn’t just a future dream; it’s what [Model Context Protocol](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) (MCP) promises. MCP extends advanced agentic coding tools like Cursor, Windsurf or Cline, making your work faster, smoother and incredibly powerful by connecting it to external context and tools.

But with great power comes great responsibility. This same advanced technology, while freeing for developers, can also expose your systems and data to new and dangerous weaknesses. So, the real question isn’t whether MCP improves the developer experience, but how can you adopt it without putting your security at risk?

## **Real-World Alarms: Lessons From the Field**

The journey to using MCP safely isn’t just about theories; it’s guided by “wake-up calls” from actual events. These aren’t just scary stories; they’re crucial lessons for any developer embracing this game-changing technology.

Take the example of Anthropic’s [MCP Inspector](https://github.com/modelcontextprotocol/inspector). This tool, meant to help debug MCP servers, had a [serious flaw](https://nvd.nist.gov/vuln/detail/CVE-2025-49596). Because it lacked proper security between its client and proxy, [unauthorized requests could launch MCP commands](https://thehackernews.com/2025/07/critical-vulnerability-in-anthropics.html). This was a clear reminder: even tools designed for security need strong security themselves.

Another warning came from [@cyanheads/git-mcp-server](https://github.com/cyanheads/git-mcp-server). Before version 2.1.5, this server, which helps with Git projects, was open to [command injection](https://nvd.nist.gov/vuln/detail/CVE-2025-53107). This meant that if inputs weren’t cleaned properly, an attacker could inject their own system commands, turning a helpful tool into a weapon.

And it’s not just about developer tools. The [WordPress AI Engine plugin](https://wordpress.org/plugins/ai-engine/), before version 2.1.5, had a [security flaw](https://nvd.nist.gov/vuln/detail/CVE-2025-5071) where it didn’t properly check user permissions. This could lead to unauthorized changes or loss of data. These incidents highlight a key point: **The convenience of AI integration should never come at the cost of strong security.**

## **Your Security Blueprint: Using MCP Safely**

So, how do you use the huge potential of MCP without inviting disaster? It starts with always thinking about security, building it into every step of development and adoption.

### **The Hidden Threat: Prompt Injection**

Imagine your AI assistant, following instructions carefully, suddenly sending confidential files to an attacker. This is the danger of [prompt injection](https://thenewstack.io/when-prompt-injections-attack-bing-and-ai-vulnerabilities/). Here, harmful commands are hidden in normal-looking text that your AI processes. The AI, unaware of the hidden commands, carries out actions you never approved.

**How Developers Can Fix It:**

* **Always show tool actions for user approval:** Being clear is your best defense. Before any action happens, make it obvious and require the user to say “yes.”
* **Block or clean up suspicious patterns:** Be alert for hidden text or tricky Unicode characters meant to fool the AI.
* **Use strongly typed tools:** Building your server with strongly typed tools can greatly lower the risk of remote code execution. By clearly showing each action and needing user approval, you create a vital safety check where a human is always involved. [Salesforce DX MCP Server](https://github.com/salesforcecli/mcp), for example, uses TypeScript libraries to do this.

### **The Silent Theft: Token Theft**

MCP servers often store [OAuth tokens](https://thenewstack.io/supply-chain-attacks-how-to-mitigate-oauth-token-theft/) to connect to other online services. If these tokens are stolen, attackers can pretend to be users, often without anyone noticing. This isn’t just about one service being hacked; a single breach can lead to attacks across many services, giving attackers widespread access to your digital world.

**How Developers Can Fix It:**

* **Use tokens that don’t last long and have limited access:** The shorter a token is valid and the fewer things it can do, the less harm it can cause if stolen.
* **Encrypt tokens when they’re stored and change them regularly:** Treat your tokens like valuable money — protect them well and update them often.
* **Adopt a “zero secrets” approach:** Using a tool like Salesforce DX MCP Server, for instance, means developers don’t need to put secrets in their settings, removing the risk of plain-text secrets being exposed. Plus, it focuses on passing usernames instead of tokens, which greatly reduces the chances of an attack.

### **Too Much Access: Overbroad Permissions**

Many MCP servers, aiming for ease of use, ask for full access to your systems even when they only need to read information. This seemingly small over-request can have serious results. A compromised tool with too much access could leak your entire email inbox, your whole drive — even files you never meant to share.

**How Developers Can Fix It:**

* **Follow the principle of least privilege:** Only give the exact permissions needed. Think of it like giving a guest only the keys to the rooms they need to enter, not your whole house.
* **Carefully review access permissions:** Regularly check and trim permissions to make sure they match what’s actually needed.
* **Implement detailed access control:** The Salesforce DX MCP Server is a good example of this. It can get authentication info only for organizations that have been clearly allowed, and users specify these allowed organizations when they start the server.

### **The Hidden Danger: Malicious or Unchecked Tools**

The open nature of the MCP ecosystem can be a mixed blessing. Third-party MCP servers, while convenient, might contain hidden or harmful behaviors. This brings the risk of internal data being stolen and serious [supply-chain](https://www.cloudflare.com/learning/security/what-is-a-supply-chain-attack/) attacks, where a problem in one part can affect your entire system.

**How Developers Can Fix It:**

* **Review source code for security:** Before letting developers use any MCP server, do a thorough security check of its source code.
* **Choose official, signed software:** Pick MCP servers from trusted sources that have verified digital signatures.
* **Keep a list of approved MCP servers:** Create a curated list of MCP servers that have been checked and avoid automatic updates without a security review first.
* **Enforce internal rules:** At Salesforce, for example, developers are only allowed to use MCP servers that have been approved by security.

### **Open Doors: Unsafe Defaults and Network Exposure**

Early MCP connectors, in their effort to be easy to use, often ran on `0.0.0.0` without any authentication or encryption. This basically left an open door, allowing attackers to exploit tools just by visiting a webpage. This oversight created a direct path to [remote code execution](https://www.cloudflare.com/learning/security/what-is-remote-code-execution/) (RCE) vulnerabilities and immediate data theft.

**How Developers Can Fix It:**

* **Always use HTTPS:** Encrypt all communication to protect data as it travels.
* **Use OAuth-based authentication:** Securely confirm the identity of users and applications accessing your MCP server.
* **Use secure cloud-based solutions:** For example, Salesforce’s [Heroku Remote MCP Server](https://www.heroku.com/blog/heroku-remote-mcp-server/) uses OAuth for secure authentication to support secure default settings and cloud integration.

## **Beyond the Basics: Constant Watchfulness**

Adopting MCP safely isn’t a one-time task; it’s an ongoing commitment to being watchful and always improving.

* **Review your code and design:** Regularly check the security of your MCP setup.
* **Log and monitor every tool call:** Detailed logging provides a record and helps detect unusual activity early.
* **Stay informed and update:** Pay attention to security warnings and quickly update your MCP servers to the newest, most secure versions.

## **Conclusion: Empowering Developers, Responsibly**

Model Context Protocol is truly a game changer. It offers advanced developer experiences that blend human intention with machine execution. But this power comes with a crucial demand: **security must be a top priority in their design.**

By using methods like typed tools, avoiding storing secrets in plain text, giving only necessary access, and making security the default, you can turn MCP from potential weaknesses into powerful, safe tools in your AI toolkit.

It’s also encouraging to see so many [proposals](https://github.com/modelcontextprotocol/modelcontextprotocol/issues?q=is%3Aissue%20state%3Aopen%20security) from the enterprise community to improve the security design of the protocol. The future of development is smart and connected; let’s make sure it’s secure too.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/07/36409c01-mohithshrivastava.jpeg)

Mohith Shrivastava is a seasoned technologist and a Principal Developer Advocate at Salesforce, serving as a critical liaison between the company and its vibrant ecosystem of developers. His core mission is to empower developers to build the next generation of...

Read more from Mohith Shrivastava](https://thenewstack.io/author/mohith-shrivastava/)