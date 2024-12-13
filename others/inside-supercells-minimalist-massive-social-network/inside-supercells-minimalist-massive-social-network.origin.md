# Inside Supercell’s Minimalist Massive Social Network
![Featued image for: Inside Supercell’s Minimalist Massive Social Network](https://cdn.thenewstack.io/media/2024/12/5658749a-image1-1024x480.png)
With just two engineers, Supercell took on the daunting task of expanding its basic account system into a social platform connecting hundreds of millions of gamers. Account management, friend requests, cross-game promotions, chat, player presence tracking and team formation — all of this had to work across Supercell’s five major games. And the team wanted it all to be covered by a single solution that was simple enough for a single engineer to maintain, yet powerful enough to handle massive demand in real time.

Supercell’s server engineer, Edvard Fagerholm, recently shared how a mighty team of two tackled this task. He explained how the team transformed a simple account management tool into a comprehensive cross-game social network infrastructure that prioritized both operational simplicity and high performance.

* Note: If you enjoy hearing about engineering feats like this, join us at Monster Scale Summit (free + virtual). Engineers from Disney+/Hulu, Netflix, American Express, Slack, Salesforce, Atlassian and more will be sharing strategies and case studie*s.
## Background: Who’s Supercell?
Supercell is the Finland-based company behind the hit games “Hay Day,” “Clash of Clans,” “Boom Beach,” “Clash Royale” and “Brawl Stars.” Each of these games has generated $1 billion in lifetime revenue.

Somehow the company manages to achieve this with a super-small staff. Until quite recently, all the account management functionality for games servicing hundreds of millions of monthly active users was being built and managed by just two engineers. And that brings us to Supercell ID.

## The Genesis of Supercell ID
Supercell ID was born as a basic account system — something to help users recover accounts and move them to new devices. It was originally implemented as a relatively simple HTTP API.

Fagerholm explained: “The client could perform HTTP queries to the account API, which mainly returned signed tokens that the client could present to the game server to prove their identity. Some operations, like making friend requests, required the account API to send a notification to another player. For example, ‘Do you approve this friend request?’ For that purpose, there was an event queue for notifications. We would post the event there, and the game backend would forward the notification to the client using the game socket.”

## Enter Two-Way Communication
After Fagerholm joined the Supercell ID project in late 2020, he started working on the notification backend, mainly for cross-promotion across Supercell’s five games. He soon realized that they needed to implement two-way communication themselves and built it as follows:

Clients connected to a fleet of proxy servers, then a routing mechanism pushed events directly to clients (without going through the game). This was sufficient for the immediate goal of handling cross-promotion and friend requests. It was fairly simple and didn’t need to support high throughput or low latency.

But it got them thinking bigger. The team realized they could use two-way communication to significantly increase the scope of the Supercell ID system.

Fagerholm explained, “Basically, it allowed us to implement features that were previously part of the game server. Our goal was to take [features that any new games under development](https://thenewstack.io/are-cloud-based-ides-the-future-of-software-engineering/) might need and package them into our system, thereby accelerating their development.”

With that, Supercell ID began transforming into a cross-game social network that supported features like friend graphs, teaming up, chat and friend state tracking.

## Evolving Supercell ID Into a Cross-Game Social Network
At this point, the social network side of the backend was still a single-person project, so the team designed it with simplicity in mind. Enter abstraction.

### Finding the Right Abstraction
“We wanted to have only one simple abstraction that would support all of our uses and could therefore be designed and implemented by a single engineer,” explained Fagerholm. “In other words, we wanted to avoid building a chat system, a presence system, etc. We wanted to build one thing, not many.”

Finding the right abstraction was key. And a hierarchical key-value store with change data capture fit the bill perfectly. Here’s how the team implemented it:

- The top-level keys in the key-value store are topics that can be subscribed to.
- There’s a two-layer map under each top-level key —
*map(string, map(string, string))*. Any change to the data under a top-level key is broadcast to all that key’s subscribers. - The values in the innermost map are also timestamped. Each data source controls its own timestamps and defines the correct order. The client drops any update with an older timestamp than what it already has stored.
A typical change in the data would be something like “level equals 10” changing to “level equals 11.” As players play, they trigger all sorts of updates like this, which means a lot of small writes are involved in persisting all the events.

### Finding the Right Database
Fagerholm needed a database that supported the project’s technical requirements and wouldn’t require constant babysitting from their two-engineer team. That translated to the following criteria:

- Handles many small writes with low latency
- Supports a hierarchical data model
- Manages backups and cluster operations as a service
ScyllaDB Cloud turned out to be a great fit. ScyllaDB Cloud is the fully managed version of ScyllaDB, a database known for delivering predictable low latency at scale.

## How It All Plays Out
For an idea of how is implemented in Supercell games, let’s look at two examples.

First, consider chat messages. A simple chat message might be represented in the data model as follows:

123 |
<room ID> -> <timestamp_uuid> -> message -> “hi there” metadata -> … reactions -> … |
Fagerholm explained, “The top-level key that’s subscribed to is the chatroom ID. The next level key is a timestamp-UID [unique identifier], so we have an ordering of each message and can query chat history. The inner map contains the actual message together with other data attached to it.”
Next, let’s look at “presence,” which is used heavily in Supercell’s new (and highly anticipated) game, “mo.co.” The goal of presence, according to Fagerholm: “When teaming up for battle, you want to see in real time the avatar and the current build of your friends — basically the weapons and equipment of your friends, as well as what they’re doing. If your friend changes their avatar or build, goes offline or comes online, it should instantly be visible in the ‘teaming up’ menu.”

Players’ state data is encoded into Supercell’s hierarchical map as follows:

123 |
<player ID> -> “presence” -> weapon -> sword level -> 29 status -> in battle |
Note that:
- The top level is the player ID, the second level is the type and the inner map contains the data.
- Supercell ID doesn’t need to understand the data; it just forwards it to the game clients.
- Game clients don’t need to know the friend graph since the routing is handled by Supercell ID.
## Deeper Into the System Architecture
Let’s close with a tour of the system architecture, as provided by Fagerholm.

“The backend is split into APIs, proxies and event routing/storage servers. Topics live on the event routing servers and are sharded across them. A client connects to a proxy, which handles the client’s topic subscription. The proxy routes these subscriptions to the appropriate event routing servers. Endpoints (for instance, for chat and presence) send their data to the event routing servers, and all events are persisted in ScyllaDB Cloud.

“Each topic has a primary and backup shard. If the primary goes down, the primary shard maintains the memory sequence numbers for each message to detect lost messages. The secondary will forward messages without sequence numbers. If the primary is down, the primary coming up will trigger a refresh of state on the client, as well as resetting the sequence numbers.

“The [API for the routing layers](https://thenewstack.io/onions-have-layers-ogres-have-layers-apis-should-have-layers-too/) is a simple post-event RPC containing a batch of topic, type, key, value tuples. The job of each API is just to rewrite their data into the above tuple representation. Every event is written in ScyllaDB before broadcasting to subscribers. Our APIs are synchronous in the sense that if an API call gives a successful response, the message was persisted in ScyllaDB. Sending the same event multiple times does no harm since applying the update on the client is an idempotent operation, with the exception of possibly multiple sequence numbers mapping to the same message.

“When connecting, the proxy will figure out all your friends and subscribe to their topics, same for chat groups you belong to. We also subscribe to topics for the connecting client. These are used for sending notifications to the client, like friend requests and cross promotions. A router reboot triggers a resubscription to topics from the proxy.

“We use Protocol Buffers to save on bandwidth cost. All load balancing is at the TCP level to guarantee that requests over the same HTTP/2 connection are handled by the same TCP socket on the proxy. This lets us cache certain information in memory on the initial listen, so we don’t need to refetch on other requests. We have enough concurrent clients that we don’t need to separately load balance individual HTTP/2 requests, as traffic is evenly distributed anyway, and requests are about equally expensive to handle across different users. We use persistent sockets between proxies and routers. This way, we can easily send tens of thousands of subscriptions per second to a single router without an issue.”

## But It’s Not Game Over
If you want to watch the complete tech talk, just press play below:

And if you want to learn more about ScyllaDB’s role in the gaming world, you might also want to read:

-
[Epic Games](https://thenewstack.io/how-epic-games-revs-up-unreal-engine-cook-time-for-devs/): How Epic Games used ScyllaDB as a binary cache in front of NVMe and S3 to accelerate global distribution of large game assets used by Unreal Cloud DDC.[Tencent Games](https://thenewstack.io/inside-tencent-games-real-time-event-driven-analytics-system/): How Tencent Games built service architecture based on command and query responsibility segregation (CQRS) and event sourcing patterns with Pulsar and ScyllaDB.[Discord](https://discord.com/blog/how-discord-stores-trillions-of-messages): How Discord used ScyllaDB to power its massive growth, moving from a niche gaming platform to one of the world’s largest communication platforms.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)