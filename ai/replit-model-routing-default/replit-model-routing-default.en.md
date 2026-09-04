AI coding company [Replit](https://replit.com/) is throwing its weight behind the model-routing trend by making its “intelligent model routing” system the default across every account.

The system automatically chooses which underlying model should handle a task as it evolves, with Replit weighing quality, speed and cost in its routing decisions.

The company says the feature, dubbed [Auto mode](https://docs.replit.com/chat/auto-mode), will become the default option for all users, though [Core and Pro subscribers](https://replit.com/pricing) are still able to override it and manually select models when they want more control.

## Model-routing momentum

The announcement comes hot on the heels of a [flurry of activity](https://thenewstack.io/cursor-ramp-meta-model-router/) in the model-routing realm. Earlier in August, [Stripe agreed to acquire](https://thenewstack.io/stripe-acquires-openrouter-tokens/) model gateway platform OpenRouter for a reported $8 billion, and on the very same day, [Ramp launched Router.com](https://www.prnewswire.com/news-releases/ramp-launches-routercom-to-cut-companies-rising-ai-bills-302855572.html), which routes requests to the lowest-cost model that meets a specified performance bar.

Prior to all that in July, SpaceX-owned Cursor [launched its own router](https://cursor.com/blog/router), which automatically chooses models for coding requests and claims to deliver comparable performance at substantially lower cost. Meanwhile, [Meta is reportedly](https://www.theinformation.com/articles/metas-ai-incubator-developing-openrouter-rival-cut-coding-costs) developing an internal router called “Switchboard” that scores coding tasks by difficulty and sends simpler jobs to cheaper models.

> “Across one model family, per-token rates can span orders of magnitude. At the same time, the intelligence of cheaper, smaller models is now much closer to their larger frontier counterparts, providing us a lot of room for cost optimizations.”

[Michele Catasta](https://www.linkedin.com/in/pirroh/), president and head of AI at Replit, says that one reason for the wider push into routing is simple economics — the growing gap between what models cost and the level of capability developers actually need for a given task.

“Across one model family, per-token rates can span orders of magnitude,” Catasta tells *The New Stack*. “At the same time, the intelligence of cheaper, smaller models is now much closer to their larger frontier counterparts, providing us a lot of room for cost optimizations.”

Replit, for its part, has been moving in this direction for some time. Catasta says that the company has spent recent months experimenting with early versions of Auto mode, subagent routing and multiple iterations.

“Like any pivotal launch, we thoroughly tested Intelligent Model Routing in beta for a long period of time before we decided to release it in public,” he says. “The most important learning is understanding from first principles the failure modes of every experiment, so we could keep hill climbing on the final system that we just shipped.”

## Enter Auto mode

The foundation of that work surfaced last week when [Replit introduced Free Mode](https://replit.com/blog/replit-introduces-free-mode), a lower-cost Agent mode that doesn’t consume usage credits and uses Auto to choose the model on the user’s behalf, subject to usage limits.

Now, that same Auto routing approach is being pushed across Replit more broadly. The company says intelligent model routing will become the default across every account, with all users starting in Free Mode and Replit deciding which model is best suited to the task.

Free Mode, it’s worth noting, isn’t “free” in the sense of unlimited usage. When it launched, Replit made it available to Core and Pro subscribers without consuming their usage credits, but imposed limits that reset every five hours, with higher allowances for Pro users. In Free Mode, users cannot manually select a model.

Core and Pro subscribers can, however, switch to Replit’s Power or Max modes, where they can turn off Auto and choose a model themselves. Replit may also suggest moving a task into one of those higher-powered modes when it determines that more capability is required, though those modes can incur usage costs.

![Auto Mode in Replit](https://cdn.thenewstack.io/media/2026/08/a4ac5fa0-replit-router-1024x476.png)

*Auto mode in Replit*

For Enterprise customers, meanwhile, administrators can restrict Auto to an approved set of models for each workspace, allowing Replit to continue routing tasks automatically while keeping model choice within company policy.

## The agent advantage

Even before SpaceX agreed to pay a cool [$60 billion](https://uk.finance.yahoo.com/news/spacex-completes-record-60-billion-131413932.html) to [acquire Cursor](https://cursor.com/blog/joining-spacex), the AI coding startup had long been investing in its own coding models, including its [Composer family](https://thenewstack.io/cursors-composer-2-beats-opus/). More recently, under the auspices of SpaceX, Cursor has been [developing more cutting-edge models](https://thenewstack.io/grok-4-6-agent-training/), too.

Replit, by contrast, isn’t making ownership of the underlying model layer central to its pitch. Instead, it’s betting that controlling the agent and the systems around it gives Replit enough insight to make better model-selection decisions on the fly.

> “Replit has owned, from the start, both the agent harness and the infrastructure surrounding models which in turn allows us to train sophisticated model routers.”

“Replit has owned, from the start, both the agent harness and the infrastructure surrounding models which in turn allows us to train sophisticated model routers,” Catasta said. “Only in this way, we can always offer useful intelligence to our users at the most competitive price point.”

That becomes particularly relevant as an Agent task unfolds, with Replit noting that its system can change which model it uses as the task develops, seeking a better trade-off between capability and cost at different points in the process. But for Catasta, that kind of dynamic routing is still only one part of a much broader research problem around how agents should use models.

“Model routing is still in its early development phase and we expect further research will move the needle on serving the best intelligence when customers most need it,” Catasta explains. “Routing is but one piece of the puzzle that is tightly integrated to many other aspects of our harness research.”

> “No third-party router company could reproduce the same results for our own agent.”

Replit also argues that seeing how people use its own Agent gives it an advantage that a standalone routing provider would struggle to reproduce. Catasta says a router has to infer the nature, difficulty, scope and intent of a request, with Replit able to train against proprietary usage data and observe those signals across its user base.

“No third-party router company could reproduce the same results for our own agent,” he says.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)