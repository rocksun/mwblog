# Introducing FizzBee: Simplifying Formal Methods for All
![Featued image for: Introducing FizzBee: Simplifying Formal Methods for All](https://cdn.thenewstack.io/media/2024/05/896e8605-fizzbee-1024x683.png)
Two years back, we shared an article in The New Stack about
[Amazon’s use of formal methods to verify its distributed systems](https://thenewstack.io/tla-the-best-debugger-optimizer-youve-never-heard-of/) since 2012. Now, major players like [Amazon](https://aws.amazon.com/?utm_content=inline+mention), [Microsoft](https://news.microsoft.com/?utm_content=inline+mention), [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention), [Confluent](https://www.confluent.io/?utm_content=inline+mention), [Oracle](https://developer.oracle.com/?utm_content=inline+mention), Elastic, [CockroachDB](https://www.cockroachlabs.com?utm_source=tns&utm_medium=sponsor&utm_campaign=brand-pipe-tns-sponsor-page-description&utm_content=lp-homepage-learn-more&utm_term=prosp&utm_content=inline-mention), and many more are all embracing formal methods for their systems. Despite the immense benefits and relevance of this technique in modern software development, its widespread adoption has been hindered by the complexity of existing tools.
In this article, we’ll introduce you to
[FizzBee](https://fizzbee.io), a new formal methods system that you can grasp in just a weekend.
## What Are Formal Methods?
Formal methods encompass rigorous techniques employed to specify, model, design, and verify complex systems using mathematical logic. Particularly relevant to software engineers working on cloud-based SaaS or distributed systems, concurrent programming, and similar domains, these methods offer a systematic approach to guarantee correctness and
[reliability in both software and hardware systems](https://thenewstack.io/a-site-reliability-engineers-advice-on-what-breaks-our-systems/).
Formal methods find bugs in system designs that cannot be found through any other technique we know of.
— Chris Newcombe, AWS
## How Do We Find System Design Bugs Today?
Today, we rely on drafting design documents and team reviews to uncover system design bugs. However, this approach falls short due to its inefficiency and limited effectiveness. We rely on pattern matching based on past
[experiences and known anti-patterns to identify design](https://thenewstack.io/the-power-of-prototyping-in-user-experience-design/) flaws because we lack the mental capacity and time to explore every possible outcome. This is where computers excel: effortlessly exploring billions of states in minutes.
## Why Formal Methods Aren’t Catching on
The most popular formal methods tool for distributed system specification is TLA+. While many recognize its potential to improve their work, the barrier lies in the lack of time to learn or use TLA+.
Even at Amazon,
[Chris Newcombe](https://www.linkedin.com/in/chris-newcombe-b33a081/), who first started using TLA+ at Amazon, faced challenges persuading colleagues to adopt TLA+, as engineers have little spare time unless compelled by necessity or executive mandate.
TLA+ offers powerful verification capabilities for system designs. However, its syntax and mathematical approach can be intimidating for many software engineers, particularly those more accustomed to conventional programming languages like
[Python](https://thenewstack.io/what-is-python/). Expressing certain algorithms in TLA+ may require complex mathematical formulations, whereas the same logic can be easily conveyed using Python’s familiar syntax.”
## FizzBee: Formal Methods for All
FizzBee, a recent addition to formal methods systems, closes the accessibility gap with its user-friendly interface and Python-like syntax. This makes it easy for developers of all levels to express
[complex algorithms and system](https://thenewstack.io/tutorial-use-ansible-collections-to-help-configure-and-manage-more-complex-systems/) designs.
- Easy to learn: If you’ve written a few Python scripts, you can grasp FizzBee code in just 10 minutes. Then, you can learn model-checking principles in a few hours.
- Enhanced Readability: FizzBee specifications are designed for easy comprehension by both reviewers and developers. Unlike other tools like TLA+, FizzBee’s familiar syntax ensures that even non-authors can understand the specifications, facilitating smoother review processes and implementation.
- Multi-Paradigm Flexibility: FizzBee offers versatile programming options, including functional, imperative, structured, procedural, and object-oriented styles. This allows developers to choose the best approach for each problem, leading to concise and adaptable solutions.
- Visualization: FizzBee’s state transition graph aids in debugging by providing a visual representation. This also improves understanding of the model-checking process and helps users identify and resolve issues more effectively.
- Online Playground: FizzBee provides an
[online playground](https://fizzbee.io/play)for practicing, experimenting, and exploring examples, making it accessible for both learning and exploration.
## Modeling a Wire Transfer System
Let’s model a simple money transfer between two accounts, a classic example showcasing database transaction consistency. The aim is to ensure that no money is lost or gained unexpectedly, maintaining the total amount across all users in the system at the end of the day.
### First Implementation
Let’s keep it simple, we have two users: Alice and Bob. Only Alice is permitted to initiate wire transfers to Bob.
**Actions:** *Actions* are building blocks of the system’s behavior specification, representing various behaviors, operations, or events like user interactions or timer events. The model checker calls these actions repeatedly in different sequences to explore the system’s potential states.
In our model, we define two actions using the
*action* keyword. The first is *Init*, a special action called first and only once. The second action is *FundTransfer*, which is the sole action in our model and called repeatedly. **State:**
The variables defined in the
* Init* action become the system’s state variables, which later actions can modify. In our example, a single state variable is represented by a Python dictionary containing two accounts with balances of 3 and 2. **Non-determinism:**
When testing an implementation, we often test with a single value. However, with FizzBee, you specify the possible values, and the model checker explores all combinations.
In this example, you select an amount to transfer from the range 0 to 100.
*any* is one of two keywords used to specify non-determinism. Syntactically, this is equivalent to a Python *for* statement, allowing you to rerun the same test with different amounts.
The remaining code is straightforward: if Alice has the funds to transfer, the amount is deducted from her account and added to Bob’s.
**Invariants:**
In system modeling, it’s crucial to ensure certain properties hold true. One essential property is that the sum of balances in all accounts must equal 5.
There are three types of invariants: safety (conditions that must always be true), liveness (conditions that must eventually become true), and stability (conditions that must eventually become true and remain true).
Let’s start with an assertion that balances should always match, similar to transfers between accounts in the same bank. Invariants are specified using the “assertion” keyword.
Invariants are implemented using the
*assertion* keyword.
An assertion is akin to a Python function but expects a Boolean return value.
*True* implies the condition is true in that state.
The
*always* keyword implies that this condition must hold true in every state. **Run the model checker.**
The model checker will indicate a failure, showing a trace where a context switch occurs after deducting from Alice’s account but before crediting Bob’s account.
![](https://cdn.thenewstack.io/media/2024/05/1cf40e21-invariant.png)
Fix: Put these two steps in a transaction.
**atomic keyword**:
Using
*atomic* ensures that both intermediate steps happen together or not at all, shielding them from the rest of the system. During development, this translates to a transaction or lock. By default, the behavior is serial, but you can explicitly specify otherwise.
After applying
*atomic*, running the model checker succeeds. You can also review the full state graph to observe the system’s behavior. **Wire transfer — non atomic money transfer**
Let us change the requirement to say once a wire transfer request is received, Alice’s account will be deducted immediately, but Bob’s account may not be credited immediately. We just want to ensure it will be credited eventually.
Let us start with the assertion. Instead of saying always, change from always to always eventually. From any state it will eventually reach a state where the predicates become true. This is called liveness expectation. (The stability expectation is specified with eventually always, this is less used and not covered here).
Now, as a first attempt, remove the atomic keyword (or replace it with the serial keyword). So, the debiting and crediting happens in two separate steps
Now, when you run the command, you will see it failed with this trace.
This indicates, after deducting, the system could crash and if it did, it loses the next steps and stutter Stutter indicates, the system may not make any more progress.
Actions indicate what may happen in the system, not what must happen. We need to specify what must happen. This is done by adding keyword fair to an action.
Note: in this case, if we mark the FundTransfer action as fair, it just implies Alice would be able to keep sending the money, but it will be possible, the money will never reach Bob.
**Implementing wire transfer**
It happens in two actions. In the first action, atomically, record the wire request and deduct from Alice’s account. On a second action, again atomically mark the transfer as complete and credit Bob’s account.
Here, we are keeping a list of wire requests indicating the pending requests for wire transfers that need to be completed. And the Action DepositWireTransfer completes the step by crediting Alice’s account.
Run this model, you will notice an error — Deadlock.
That is because, as the system starts transferring funds from Alice to Bob, Alice runs out of money and the system cannot make any progress. This is an issue with our problem statement, rather than the model or implementation. We can easily fix it by allowing Bob to transfer money back to Alice. We will make that change later. For now, to keep things simple, let us do a tiny trick — add an action that does nothing. Real code would never need this.
Note: Pass is a standard Python keyword to represent an empty block.
Now run this model checker, you will notice the model checker passes. This implies this design is correct.
Note: The model will not be directly transferable to code because wire_requests cannot be implemented in the current form. Is it a database in the same bank as the sender? Then, the receiver’s bank will not be able to atomically update along with crediting the sender. We will address it in a later post.
You can read more about FizzBee and try other examples at
[https://fizzbee.io](https://fizzbee.io).
### Formal Verification Is Testing Your Design Before Coding
Formal verification allows you to test your design before coding. As demonstrated above, it helps you concentrate on the essentials and abstract away the details, similar to explaining a design using a basic example on a whiteboard.
By using formal verification, you can make sure your design is clear and correct before you start coding. However, it’s essential to remember that while formal verification tests the design well, it doesn’t replace the need for regular testing. Bugs can still crop up during implementation, but they’re usually easier to fix.
## Final Thoughts:
Formal methods stand out as the premier choice for design validation. Practitioners consistently highlight significant design simplification and faster implementation. For instance, in a recent project where I redesigned a buggy v1 system, specifying the v2 system’s design with TLA+ led to a 4x reduction in code size while incorporating additional features. However, it’s important to note that tools like TLA+ are notoriously challenging to use.
As shown in the example above, FizzBee code is easy to read and write, unlike TLA+, making it a compelling alternative for experienced software engineers to start formal methods for the first time. With FizzBee’s model checker, design correctness is ensured, while its concise and clear specifications communicate and document the design.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)