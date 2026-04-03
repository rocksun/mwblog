I’ve always felt that AI found its footing in software engineering first because, frankly, the environment is honest. When you’re writing a blog post or a marketing strategy, “correctness” is a vibe. But in our world, it’s binary. Your code either compiles or it doesn’t. Your tests pass, or they fail.

That’s why software is such a perfect laboratory for these models. We already have the infrastructure they crave, like fast failure, clear signals, and the ability to undo/rollback changes. In a domain where the system itself enforces the rules, AI doesn’t have to wonder if it did a good job; the compiler tells it.And it turns out that the reasons coding is a good fit for AI offer valuable lessons for other industries trying to figure out where AI actually fits.

## Beyond the autocomplete phase

I remember when AI in coding was just glorified autocomplete. It was a neat trick for looking up documentation or finishing a line of boilerplate, but it wasn’t a partner.

The “aha!” moment for me, and I think for the industry, was when LLMs started showing they actually understood the intent of a codebase.

> “The “aha!” moment for me, and I think for the industry, was when LLMs started showing they actually understood the intent of a codebase.”

Once tools like [GitHub Copilot](https://thenewstack.io/copilot-reshapes-developer-work/) started respecting our local styles and naming conventions, everything started to change. We stopped chatting with a bot in a separate tab and started working alongside it. It’s now so deeply embedded in our IDEs and CI pipelines that I barely notice where my typing ends and the AI’s suggestions begin. It’s moved from being a tool to being a teammate.

## We’ve seen this script before

Whenever I hear people worry that we’re losing the art of coding, I think back to the stories of the mid-20th century. Moving from assembly to high-level languages followed the exact same script:

* **The “old guard”** called it cheating.
* **Everyone panicked** about losing control over every single byte.
* **We all gave in** because the productivity gains were just too huge to ignore.

For every C++ dev complaining that Python is too easy, there is an assembly programmer in the background thinking the C++ dev has it just as easy.

But the reality is that higher-level languages didn’t make us less rigorous; they freed us from managing registers, allowing us to focus on systems. To me, AI is just the next layer of that stack. The contract is still the same: You can use whatever abstraction you want, as long as you can execute it and verify the results.

## Toward true autonomy

We’ve come a long way from simple code completion.

These days, I’m seeing AI tackle some of the heavy lifting. Things like [refactoring messy legacy code](https://thenewstack.io/whats-missing-with-ai-generated-code-refactoring/), generating test suites, and even helping map out high-level architecture. This shift coincided with the emergence of reasoning-optimized models from organizations such as OpenAI and Anthropic, where [training on code](https://github.com/deepseek-ai/DeepSeek-R1/blob/main/DeepSeek_R1.pdf) was explicitly linked to improvements in multi-step reasoning and problem decomposition.

It turns out that when you train a model on code, you’re actually teaching it how to think through complex, multi-step problems. Programming queries now represent one of the largest and fastest-growing categories of AI usage across both consumer and enterprise systems.

But the real frontier right now is agentic workflows. We’re moving past the stage where the AI just hands us a suggestion. Now, these systems are navigating our repositories, running tests, and fixing their own mistakes in real-time.

What fascinates me most about this is the sheer density of use. Software is the one place where AI is being pushed to its limits every day, against real-world production constraints. This has created a massive virtuous cycle: the more we use it, the faster we get feedback. That feedback improves the models, making the workflows smoother and, of course, making us want to use it more.

To really understand why this cycle took off in programming while other industries are still figuring it out, you have to look at the main thing that defines a developer’s life: the feedback loop.

## Programming is a hostile environment, and that’s the advantage

Progress in any learning system has less to do with how smart the base model is and more with the quality of the feedback it receives. This principle is well established in machine learning, particularly in reinforcement learning, where the structure and timing of reward signals often matter more than the complexity of the policy itself. If the feedback is immediate and objective, you learn fast. If it’s delayed or fuzzy, you stall.

In most fields, feedback is soft. A writer has to wait for a subjective reaction from an audience; a lawyer might wait months to see how a judge rules. In those worlds, the signals are noisy and slow, which makes it incredibly hard for an AI (or a human, for that matter) to know if they’re actually getting better.

Programming is the opposite. It’s a hard-truth environment. It’s arguably hostile — one missing semicolon can crash a billion-dollar system. But that’s exactly why it’s the perfect place for AI to grow.

When an AI writes code, the environment takes a “maybe” and turns it into a “yes” or “no.” It doesn’t matter how plausible the code sounds because the moment it hits a parser, a type checker, or a test suite, the truth comes out. These tools — the compiler, the linter, the test harness — act as impartial judges. They provide the reward signal that these models need to actually improve.

This tight loop changes the entire dynamic:

* **Invisible errors become loud:** Instead of hallucinating something that looks right but is factually wrong, the AI’s mistakes surface as concrete tracebacks. You can’t argue with a stack trace.
* **Self-correction is cheap:** Because the code is executable, the AI can actually try to run its own work, see the error, and fix it before I ever see it.
* **Trust is earned, not blind:** I don’t have to believe the AI is right. I trust it because the machine verified the output before I even looked at the PR.

At the end of the day, programming provided the rigor that AI desperately needed to be useful at scale. By forcing these models to work inside a system that demands objective correctness, we’ve turned AI from a suggestion engine into a functional participant in our daily work.

## Code trains reasoning, reasoning improves code

In code, you can’t just sound smart. Because the machine is going to execute your logic, it rewards structured reasoning and punishes plausible-sounding nonsense. Those logical gains then flow right back into our daily work.

As these models get better at planning and handling constraints, they become better partners for us. They stop being just code generators and start helping us refactor massive modules, hunt down dependency hell, and explore architectural alternatives we might have missed.

### The recursive loop

This has created what I see as a recursive loop.

Better models give us better tools. Better tools mean we write, test, and review more code with AI in the loop. That entire process generates a massive amount of high-quality data, execution traces, bug fixes, and human-in-the-loop evaluations, which then go right back into making the next model even sharper.

As engineers, we aren’t just passive users of this tech. We’re actively shaping it every time we write a prompt, fine-tune a model, or integrate a new tool into our workflow. We do it because we’re the ones closest to the pain points, and we’re the first ones to benefit when the toil of the job starts to vanish.

### From software 1.0 to 3.0

You can see the whole history of our industry in this shift:

* **Software 1.0** gave us the compilers and the rigid rules of correctness.
* **Software 2.0** taught us how to build systems that learn from data.
* **Software 3.0** is what we’re living through now: using language models to orchestrate software, turning our natural-language intent into executed reality.

Programming is unique because it concentrates pain, control, and feedback all in the same place. It’s the domain where AI is evolving the fastest because every single improvement is immediately tested and reinforced by the people doing the work.

## What the rest of the world can learn from programming with AI

I don’t believe the success of AI in software is just a “tech thing.” It’s actually a blueprint. If you want AI to have a real, durable impact in any other field, you have to follow the lessons we’ve learned in the trenches.

First: Make the outcomes executable. AI is at its best when you can actually run, simulate, or mechanically test what it produces. If the output is just a document that [needs a human](https://thenewstack.io/github-ceo-on-why-well-still-need-human-programmers/) to feel if it’s right, it’s going to be very challenging to have confidence about putting that system into production. You need to turn abstract ideas into something the system can verify.

Second: Design for fast (and cheap) failure. We learn faster when we break things early. In programming, the compiler tells us we’re wrong in seconds. Other industries need to build their own test suites if they ever want AI to move beyond just giving vague advice. If it takes three months to realize the AI made a mistake, you’ve already lost because your pace of learning is too slow.

Third: Separate the brain from the guardrails. In software, we let the AI explore the creative intent, but we let deterministic systems, the compiler, and the linter, enforce the correctness. This is the secret to safety: You let the probabilistic model be messy, but you keep it inside a cage of rigid, reliable rules.

Fourth: Build an undo button into everything. You can’t have autonomy without reversibility. We have version control, sandboxes, and rollbacks, which make experimentation feel safe. If an industry doesn’t have a clear path to recover from a mistake, it’ll never have the confidence to let an AI agent take the wheel.

Finally: Put the AI where the work actually happens. GitHub Copilot was successful because it didn’t ask us to leave our code editor. It met us where we were. Continuous, daily use is what creates the feedback we need to get better.

## AI will spread outward from the hard-truth domains

Programming represents the starting point for large-scale AI adoption rather than its final destination. The reason we’ve seen such a lopsided explosion of AI in dev work is that we already had the hard-truth infrastructure ready to go. We didn’t have to change our culture to fit AI; we already lived in an environment where we were forced to prove our ideas work every time we hit run.

Other industries will follow, but only as they start to adopt that same mindset. As fields like medicine, law, and manufacturing invest in high-fidelity simulations and automated testing, they will become safe enough for AI to move from advising to acting.

We don’t need smarter models as much as we need better ways to stress-test their decisions and hit the undo button the second something goes sideways.

> “We don’t need smarter models as much as we need better ways to stress-test their decisions and hit the undo button the second something goes sideways.”

The roadmap is simple: Success with AI comes down to redesigning your world so decisions can be checked by a machine.

* With simulation and undo buttons, AI moves fast.
* Where you are still relying on a human gut feeling, AI stays cautious and limited.

Software development became the ultimate laboratory because it already had the machinery to expose failure and enforce the truth. It’s where we learned how to move from a suggestion engine to a production system.

The next wave of AI progress won’t be defined by a new model architecture or a bigger GPU cluster. It’s going to be driven by verifiability. Programming has already shown us what happens when you force an AI’s ideas to confront reality. The next big breakthroughs will belong to whichever industry is brave enough to do the same.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2024/12/0417379b-cropped-a5739559-sean-falconer-600x600.jpg)

Sean is the Head of AI at Confluent where he leads AI strategy and thought leadership. Sean’s been an academic, startup founder, and Googler. He has published works covering a wide range of topics from AI to quantum computing. Sean...

Read more from Sean Falconer](https://thenewstack.io/author/sean-falconer/)