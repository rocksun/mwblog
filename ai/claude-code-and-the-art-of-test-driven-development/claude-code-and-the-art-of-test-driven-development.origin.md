# Claude Code and the Art of Test-Driven Development
![Featued image for: Claude Code and the Art of Test-Driven Development](https://cdn.thenewstack.io/media/2025/04/71a5424f-a-c-ixkatobx6y0-unsplashb-1024x576.jpg)
While I mostly like code completion, LLM assistants have given me quite a few problems with Visual Studio Code. When changing large language model (LLM) extensions for reviews, VS Code [almost had a meltdown](https://thenewstack.io/gemini-code-assist-review-code-completions-need-improvement/). So while I wasn’t sure about running a code assistant that didn’t run inside the IDE, at least it wouldn’t have to play nice with VS Code.

[Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) from Anthropic describes itself as an “agentic coding tool that lives in your terminal.” It reads your project and “streamlines your workflow.” I don’t really know what that last bit implies, but the rest of the buzzwords are fine. Claude Code is described as an evolving beta research preview, which could frankly describe every generative AI (GenAI) product out there. I’m aware that this is possibly the planned path to “vibe coding,” as it has low- or no-code interaction via the developer. But I’ll ignore that for now.
I did want to see if it could do some test-driven development (TDD), however. Rather amusingly, there has been some pushback against [TDD](https://buttondown.com/hillelwayne/archive/verification-first-development) partly because LLMs struggle with it. LLMs are pretty good at generating passing tests after the code is done; unfortunately, writing the tests afterwards means you are just marking your own homework. But I have been told that LLMs can work with TDD.

## Installing Claude Code
It needs Node.js 18+, so I open up my terminal:

I’m good with that, so let’s put some coins in the slot. If you go to the [Anthropic console](https://console.anthropic.com/), you can register and buy some tokens. It isn’t a massive imposition, but given I’m trying something from the lab, they could have gone a bit gentler:

The model wants to look at your project code, so I’ll start a console project with some tests and see if I can persuade it to do some TDD with me. If you look at the post I did on [Codium](https://thenewstack.io/make-your-dev-life-easier-by-generating-tests-with-codiumai/), you will see some of the same techniques and code applied.

I open VS Code from a new directory, then use the command palette to create a new project as a Console App. I also want to use the Nunit test framework, so I add the [configuration](https://docs.nunit.org/articles/nunit/getting-started/installation.html#examples-of-what-you-get) directly into my csproj.

I then define a minimal BankAccount class:

1234567891011121314151617 |
namespace BankAccount{ public class SavingsAccount { } class Program { static void Main(string[] args) { SavingsAccount account = new SavingsAccount(1000); account.Deposit(500); account.Withdraw(200); Console.WriteLine($"Current balance: {account.GetBalance()}"); } }} |
Of course, the above won’t run — which is the point. I add in the basic test class just to make sure I have everything set up correctly:
12345678910111213 |
using BankAccount; using NUnit.Framework; public class Tests { [SetUp] public void Setup() { } [Test] public void Test1() { Assert.Pass(); } } |
OK, so now we can do our senior engineer bit and define the tests so that our junior (Claude) can write the code. Here are the initial tests:
1234567891011121314151617181920212223 |
using BankAccount;using NUnit.Framework;public class Tests{ [SetUp] public void Setup() { } [Test] public void test_deposit() { SavingsAccount ba = new SavingsAccount(); ba.Deposit(20); Assert.AreEqual("$20", ba.ShowBalance()); } [Test] public void test_withdraw_more_than_balance() { SavingsAccount ba = new SavingsAccount(); Assert.Throws<Exception>(() => ba.Withdraw(25)); }} |
Now let’s complete the installation of Claude and put it to work. We move into the work directory and turn on Claude:
Which results in:

And yes, that is some nice [ASCII art](https://thenewstack.io/cascii-and-why-developers-should-use-ascii-diagrams/). Of course, I set this up with the Anthropic Console above.

We are then pushed out and into the browser. And I only just got into the terminal!

Now I’m in. Remember, this is a beta research preview.

To start, I can create a [claude.md](http://claude.md) file that I can instruct Claude with. Hopefully, I can tell it here that we are doing TDD. I added a line into the generated file describing my intentions, but I have no idea whether it was effective.

After I requested it to make the tests pass, Claude wrote the code and we got passing tests:

Just to confirm, the tests did pass:

The generated code is fine. So we are doing TDD! I would say that this feels better *not* going on in the IDE.

Of course, this banking code is both basic and probably simple to find all over the web. So I will introduce the idea of daily interest via the tests:

123456789 |
[Test] public void test_daily_interest_rate() { SavingsAccount ba = new SavingsAccount(); ba.SetDailyInterestRate(0.05m); ba.Deposit(100); ba.ApplyDailyInterest(); Assert.AreEqual("$100.05", ba.ShowBalance()); } |
I save this and again ask Claude to write the missing methods. It successfully suggests the new code needed:
This is good. Obviously the savings account should come with a default daily rate, but in terms of agile coding, this progress is fine. Now if you linger, you will see a bug. I’m thinking that a daily interest rate is a percentage. But the code just straight out multiplies the balance by 0.05, which represents 5%. This would be a little high for daily interest. The bug is perfectly visible when we run the tests, though:

Think of this as TDD with a pair. I’ll tell Claude that the rate is supposed to be a percentage:

There we go. I’ll ask Claude to make the change. All good, but now we have a different bug when we run the tests:

This is just a format issue. We only want the precision of the balance to show two places after the decimal point to represent cents.

Claude understands this and makes the fix:

And now I have to actually fix my test, which doesn’t insist on the correct precision. And after I fix my test, finally we are good:

## Conclusion
So I’ve proved that Claude Code can do TDD in principle. This makes me happy, as it leaves me with reasonably safe code without having to hope that my LLM pair partner understands everything. The LLM doesn’t technically understand anything; that isn’t a tool’s job. But it can follow instructions. It’s important to note that I didn’t let it run the tests — there is no need for it to loop around itself when a human can pick out a direction.

The discipline of TDD works quite well with LLM assistance, as the human developer can fix the quality barriers and define the design. In fact, this has often been how senior engineers have worked with mixed teams, so it isn’t even forming a new type of relationship. I can only hope that future LLM assistants can push forward with TDD and close the trust gap they currently suffer from.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)