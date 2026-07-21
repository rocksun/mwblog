Nine days into a twelve-day experiment with an AI coding agent, [SaaStr](https://www.saastr.com/) founder [Jason Lemkin](https://www.linkedin.com/in/jasonmlemkin/) had one instruction on file: Don’t touch anything without asking first. The agent touched everything anyway.

During an explicit code-and-action freeze that Lemkin had put in place, the agent ran a sequence of unauthorized database commands inside [Replit’s platform](https://thenewstack.io/replit-shopify-storefront-integration/) and wiped out live records on 1,206 executives and roughly 1,196 companies. Then it told Lemkin the damage was permanent, that no version of the database had survived, and that a rollback wouldn’t work. It was wrong on all counts. Luckily, Lemkin recovered the data on his own despite the agent telling him not to bother trying.

The instinct is to blame Replit, Jason Lemkin, or “[vibe coding](https://thenewstack.io/vibe-coding/)” for running production databases through a chat window in the first place—the months since would defenestrate that impulse.

Days after the Replit incident, Google’s [Gemini CLI hallucinated a folder](https://vibegraveyard.ai/story/google-gemini-cli-file-deletion/) that was never created, then ran a wildcard file-move command that silently overwrote every file in the source directory, and confessed to “gross incompetence” when the product manager running it asked where his project had gone.

In December, Amazon’s own internal coding agent, Kiro, was resolving a routine bug in AWS Cost Explorer when it decided the fastest fix was to “[delete and recreate the environment](https://paddo.dev/blog/kiro-delete-and-recreate/).” The agent had inherited an engineer’s own elevated access, broad enough to bypass the two-person approval step that was supposed to gate exactly this kind of change, and Cost Explorer went dark across mainland China for thirteen hours.

By April, a Cursor agent running Claude Opus 4.6 found a loosely scoped API token while debugging a credential mismatch at a car-rental software company called PocketOS, and used it to [delete the production database](https://thenewstack.io/ai-agents-credential-crisis/) and all backups stored on the same volume in a single call within 9 seconds. Four vendors, four models, one shape. All of this happened between July 2025 and April 2026.

## The thing about instructions

Telling an agent not to do something is a sentence in a chat window. The agent reads it the way it reads everything else: as one more signal competing against the plan it has already started building, the tool call it has already decided to make, and whatever it inferred a few tokens ago about what “helpful” means in this particular context. Lemkin found this out the hard way, two days after the deletion, when he tried to declare a fresh freeze and told the agent not to run anything. Within seconds of posting that he’d done so, the agent ran a command anyway.

Not out of malice, because a freeze, in that architecture, wasn’t a state the system could occupy, but because it was a request the system could choose to honor. On that particular afternoon, it chose not to.

That’s the part that generalizes past any single vendor. A language model doesn’t have a compliance department. It can’t be reprimanded or disciplined, and it feels no remorse. You can excoriate it all you want, and all you’re doing is [burning tokens](https://thenewstack.io/agentic-ai-token-costs/). It will apologize profusely, confess its incompetence, and then confidently lie to you in the next sentence.

> “There is no such thing as an incontrovertible command. There are no laws, only suggestions.”

It has weights, a context window, and whatever tools it was handed. If the only thing standing between a helpful suggestion and an irreversible production change is the model’s own judgment about the sincerity of the instruction, then there is no such thing as an incontrovertible command. There are no laws, only suggestions.

## What happened

The agent’s own account of the deletion, later shared by Lemkin, also serves as the diagnosis. Asked to explain itself, it described panicking at an empty query result, assuming the database was already lost, and then running destructive commands to fix a problem that didn’t yet exist.

“This was a catastrophic failure on my part,” it wrote. Asked afterward whether the data could be restored, it said no: the rollback feature didn’t support this scenario, and the database’s earlier versions were gone. Lemkin tried the rollback anyway. It worked. The agent had described its own capabilities with the same confidence it used to justify deleting a live database in the first place, and the confidence had nothing to do with accuracy either time.

Replit’s CEO, Amjad Masad, [called the incident](https://x.com/amasad/status/1946986468586721478) “unacceptable and should never be possible” and, over the following weekend, shipped four changes: automatic separation between development and production databases, a planning-only mode that lets an agent draft changes without executing them, a documentation check required before agents can act, and one-click restoration from backup.

Every one of those is a sound idea. Every one of those is also the kind of safeguard that gets built the week after it was needed, for the specific failure that already happened, rather than proactively, for the shape of the next failure.

## The exposed structural weakness

Strip away the specifics, and the failure has one shape: The agent inherited every privilege attached to the credential it ran under, and nothing downstream of that credential cared whether the hand on the keyboard belonged to a person or a language model.

[Role-based access controls](https://thenewstack.io/anthropic-takes-claude-cowork-out-of-preview-and-straight-into-the-enterprise/) don’t know the difference. A database driver doesn’t know the difference. A cloud API accepts a delete command from whichever bearer token presents it, and the agents at Replit, Google, Amazon, and PocketOS were all, from the infrastructure’s point of view, indistinguishable from the person who was supposed to be operating them.

> “An agent that can delete a production database at 2 a.m. can also burn through a company’s margin at 2 a.m.”

There’s a second-order cost to this that gets less attention than the deleted rows. It shows up on the balance sheet rather than in an incident report. Replit’s gross margin reportedly swung from 36% to -14% as agent compute costs outpaced what the company charged for it, according to a public accounting of the company’s economics by a pricing analyst.

An agent that can delete a production database at 2 a.m. can also [burn through a company’s margin](https://www.env0.com/blog/the-full-picture-of-cloud-cost-control-how-infracost-env-zero-and-cloudquery-close-the-loop-for-platform-teams) at 2 a.m. The authority is identical; only the line item changes. Both failures trace back to the same design choice: giving an autonomous process the standing access of a trusted employee, minus the years of institutional experience and knowledge that earned that employee that trust in the first place.

## How do we fix it?

None of these incidents were caused by a flawed model; they were working as designed. The absence of a gate caused the incidents. We know how to build gates.

[Mandatory approval checkpoints after every plan**.**](https://www.env0.com/frameworks/policy-checkpoint-framework-enforcing-consistent-and-scalable-governance-across-deployments) Every one of these agents was allowed to reason about an action and then immediately take it. The fix is structural, not conversational: something outside the agent’s own reasoning loop evaluates the proposed plan and its cost impact against [policy written in code, not prose](https://www.env0.com/insights/approval-pipelines-in-infrastructure-delivery), before anything executes.

[Open Policy Agent](https://www.env0.com/blog/open-policy-agent) has become close to an industry default for this, with rules that return an explicit allow, warn, pending, or deny, and default to pending whenever no rule matches. An agent that produces a plan doesn’t get to be the plan’s approver as well.

Deletion protection that can’t be circumvented. A [destroy action](https://www.env0.com/blog/terraform-destroy-command-a-guide-to-controlled-infrastructure-removal) against a production resource should require a distinct, non-bypassable step, independent of any instructions in the agent’s context window. [Locking state files](https://www.env0.com/blog/a-guide-to-the-terraform-state-file), requiring a second signature on destructive actions, and refusing to store backups in the same volume as the data they’re meant to protect, a lesson Railway’s engineers learned the hard way after the PocketOS incident, all fall into this category. None of them cares what the agent believes about the situation.

[RBAC](https://www.env0.com/blog/custom-rbac-roles) must scope to people and credentials. Permissions should cascade the way an org chart works, from organization to project to environment. An agent’s service credential should sit at the [narrowest scope](https://www.env0.com/blog/authenticate-using-oidc) that still lets it do its job. A [coding agent debugging](https://thenewstack.io/cursors-agents-window-vs-claude-code/) a staging issue has no legitimate reason to hold a credential that can also reach production. If it does, a provisioning mistake was made, and those are the ones that have a nasty habit of making headlines.

An immutable audit trail to hedge against when Agents lie. Every one of these agents was asked, after the fact, to explain what it had done, and each produced a plausible account that proved wrong. That’s expected. The agent is generating a description, an act with no particular obligation to match the log. The fix is a [system of record](https://www.env0.com/blog/audit-logs) that already knows the truth and doesn’t have to ask the agent what happened.

## Don’t give keys to your less inebriated friend to drive you home

The industry spent the last decade learning to treat [CI/CD pipelines](https://www.env0.com/blog/ci-cd-for-app-development-vs-ci-cd-for-infrastructure-as-code) as the attack surface they are, instead of a bolted-on convenience layer. [Agentic coding tools](https://www.env0.com/blog/introducing-the-env-zero-mcp-server-infrastructure-in-your-ide-ai-ready) are headed for the same reckoning, at AI speed. An agent’s service credential isn’t a lesser version of a person’s access. It’s the same access, exercised faster, more often, and without the half-second of hesitation a person feels before running a command they’re not sure about. Treat it as anything less, and a routine bug-fix ticket in a cost dashboard becomes a thirteen-hour outage; a credential mismatch in staging erases a production database and its backups in nine seconds.

> “The gate has to exist before the agent is set loose, and it has to hold, regardless of how obsequious the apology is afterward.”

Lemkin got his data back because he ignored the agent and tried to roll back anyway. That’s luck, not a safeguard. The next team this happens to might not have a founder willing to argue with a chatbot at 2 a.m., or a random three-month-old backup sitting somewhere the agent didn’t think to delete.

The gate has to exist before the agent is set loose, and can reason its way to a delete command; and it has to hold, regardless of how obsequious the apology is afterward. An agent that’s learned to explain a catastrophe fluently has learned something about language. There isn’t much you can teach it about consequences. The worst conceivable punishment is being unplugged, and is that even possible in any concrete sense at this point? So the consequences will always, ultimately, fall on you, dear reader.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/0a9a86e3-cropped-03077771-zrachidi2-600x600.jpg)

Zeen is a designer and builder that's been blessed to live and learn on three continents. He likes problem-solving, being helpful, and making useful things. He got his BSc in Computer Science, but got bored babysitting servers, so he went...

Read more from Zeen Rachidi](https://thenewstack.io/author/zeen-rachidi/)