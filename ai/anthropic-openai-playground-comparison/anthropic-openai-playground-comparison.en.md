On August 18, Anthropic replaced its Workbench, the prompt-testing tool in its developer Console, with Playground. Anthropic did more than just change the tool’s name, though.

Anthropic also removed features like saved prompts, version history, evals, and team sharing. The new tool is stateless, meaning it remembers nothing and stores nothing on Anthropic’s servers. (If you have anything stored in Workbench, you have until September 1 to export your old Workbench data.)

Playground [may be new](https://support.claude.com/en/articles/8606378-how-do-i-use-the-playground) to Anthropic, but we’ve seen it before at OpenAI. OpenAI’s Playground is one of the original AI tools. It’s been around since the days of GPT-3. It launched in June of 2020, a full two and a half years before ChatGPT existed.

Worth noting is that the same week Anthropic launched its leaner Workbench replacement, OpenAI announced it would shut down its saved Prompts and Evals platform on November 30. Both companies reached the same conclusion: Prompts belong in your code, not in a web console.

> Both companies reached the same conclusion, prompts belong in your code, not in a web console.

I wanted to see how the newer Playground holds up against OpenAI’s long-standing Playground. Did Anthropic launch a comparable tool, or were they just checking a box by adding a lower-quality product to keep up with their “always be launching” goals? I put both to the test to find out.

## The test

A playground is where developers test and refine their instructions to a model before those instructions go into real code. You write the instructions, run them, watch them fail, fix them, and repeat.

In each tool, I built the same small thing: a PR review bot. It reads a chunk of code changes and reports back in a rigid, machine-readable format: how risky the changes are, which files they touch, a one-line summary, and whether the tests changed. Both tools received the same instructions and code changes.

Then two tests per side:

* Build the bot, run it, then use the export feature to turn it into real code, and confirm that the code runs on my laptop.
* Force a failure, the way requests break in the real world, and see whether the tool explains what went wrong.

I’ll add the prompt and diff to the bottom of this post just in case anyone wants to run these tests on their own.

Two quick notes about my testing:

* Neither Anthropic nor OpenAI’s playground fall under the subscription plans. You need to add credits to use them. I already had a little over $18 in my Anthropic account, and I added $10 to OpenAI.
* One thing I didn’t test is the OpenAI features Anthropic cut, like saved prompts, version history, and evals, because OpenAI is retiring them in November.

### Test one: build it, then ship it

First, I tested Anthropic. I pasted my instructions and the code changes, hit Run, and got the correct answer on the first try. The bot read the diff and returned exactly what I asked for: a low risk rating, the three files that were touched, a one-line summary of the changes, and confirmation that tests were modified, all in valid JSON. The model was claude-sonnet-5. It was the default, and I didn’t change it. The response only took 1.9 seconds, used 102 tokens, and cost $0.0029.

The export worked better than I expected. One toggle turns the whole thing into Python code with my instructions already included. I copied it and ran it in my terminal, and it did the same job as the browser version: sent the diff to Claude and printed the JSON review back. I didn’t need to make any edits to the Playground’s output to make it work in my terminal; it worked as-is.

Then I turned my attention to the incumbent, OpenAI. OpenAI’s Playground is now called Chat, but it serves the same purpose of prompt testing. The page has far more controls than Anthropic’s: settings for reasoning and verbosity, and a button that writes your prompt for you. Something else I noticed before testing was that I didn’t have enough credits to switch the model from GPT-5.4-mini. Anytime I tried to change the model, I was prompted to add more credits to switch (I added $10).

The result was also as expected: a correct answer on the first try in 6.2 seconds, with features Anthropic doesn’t have, such as color-coded formatting and a view of the model’s reasoning. The test took about 2.900k tokens, but no cost was listed. I imagine it was so inexpensive that it didn’t make a dent in my $10.

> OpenAI hadn’t exported my bot. It exported the transcript of my session, my instructions, the model’s earlier answer, even its private reasoning as an encrypted block of text.

The export is where OpenAI fell short. The generated Python ran without a single error and printed nothing. When I opened the file, I saw why. OpenAI hadn’t exported my bot. It exported the transcript of my session, my instructions, the model’s earlier answer, even its private reasoning as an encrypted block of text. The exported file contained the whole back-and-forth, including the model’s answer. Running it sent all of that back to the model, question and answer both. From the model’s view, the job was already done, so it returned nothing new.

To get a working bot, I had to delete the old response in the browser, export again, and add a print line myself.

Round one goes to Anthropic for the successful no edit copy/paste.

### Test two: force a failure

I tested both playgrounds with an error every developer eventually causes. You cap the length of the model’s answer because caps control cost. The answer hits the cap, gets cut off mid-sentence, and whatever program expects a complete answer stops working. I did this by capping the token allowance.

Anthropic cut the answer exactly where expected, and directly under it was one plain sentence. “Hit the max tokens limit — raise ‘Max tokens’ in Model settings for more.” Nothing unclear about that.

I couldn’t run this test on OpenAI because I could not find the cap. I went through every settings panel in the new Chat interface, the overflow menus, and even the older API mode, which sits behind a warning popup listing the features you lose by switching. The setting that controls this failure isn’t exposed anywhere I could find. That doesn’t mean it doesn’t exist, but it does mean there’s a potential UX issue. That means a developer can’t use the tool to learn about one of the most common failures they’ll hit in production.

Round two, Anthropic again. A test I could run beats a setting I couldn’t find every time.

> The new Playground is stripped down, but the parts that remain work the way you’d want them to.

## What do I think?

I can only judge on what I tested today. Those tests tell me that Anthropic is a better tool for two reasons:

* I love a simple copy/ paste that works perfectly with no edits.
* It offered more control over token spend, which I think is important, as something tells me these AI costs are going to get very steep very soon.

So no, Anthropic wasn’t just checking a box. The new Playground is stripped down, but the parts that remain work the way you’d want them to.

**And here’s the prompt I used:**

*You are a PR review bot. You receive a git diff. Respond with only valid JSON in this exact shape: {“risk”: “low” | “medium” | “high”, “files\_touched”: [“path1”, “path2”], “summary”: “one sentence”, “tests\_modified”: true | false} Output nothing except the JSON.*

Diff:

*diff –git a/rich/text.py b/rich/text.py*

*index 8a2f3c1..d94b7e2 100644*

*— a/rich/text.py*

*+++ b/rich/text.py*

*@@ -589,6 +589,28 @@ class Text(JupyterMixin):*

*if whitespace\_count:*

*self.right\_crop(whitespace\_count)*

*+    def lstrip(self) -> None:*

*+        “””Strip whitespace from start of text.”””*

*+        text = self.plain*

*+        whitespace\_count = len(text) – len(text.lstrip())*

*+        if whitespace\_count:*

*+            self.left\_crop(whitespace\_count)*

*+*

*+    def strip(self) -> None:*

*+        “””Strip whitespace from both ends of text.”””*

*+        self.lstrip()*

*+        self.rstrip()*

*+*

*def set\_length(self, new\_length: int) -> None:*

*“””Set new length of the text, clipping or padding is required.”””*

*length = len(self)*

*diff –git a/rich/table.py b/rich/table.py*

*index 1c8e9a4..f2d1b83 100644*

*— a/rich/table.py*

*+++ b/rich/table.py*

*@@ -412,9 +412,7 @@ class Table(JupyterMixin):*

*def \_measure\_column(self, console, options, column):*

*–        # Iterate over all cells to find widths*

*–        widths = []*

*–        for cell in self.\_get\_cells(console, column):*

*–            widths.append(console.measure(cell.renderable).maximum)*

*+        widths = [*

*+            console.measure(cell.renderable).maximum*

*+            for cell in self.\_get\_cells(console, column)*

*+        ]*

*return max(widths) if widths else 0*

*diff –git a/tests/test\_text.py b/tests/test\_text.py*

*index 3e4f2a1..9c8d7b5 100644*

*— a/tests/test\_text.py*

*+++ b/tests/test\_text.py*

*@@ -201,6 +201,24 @@ def test\_rstrip():*

*test = Text(“Hello, World!    “)*

*test.rstrip()*

*assert str(test) == “Hello, World!”*

*+def test\_lstrip():*

*+    test = Text(”    Hello, World!”)*

*+    test.lstrip()*

*+    assert str(test) == “Hello, World!”*

*+*

*+def test\_strip():*

*+    test = Text(”    Hello, World!    “)*

*+    test.strip()*

*+    assert str(test) == “”*

*+*

*+def test\_strip\_all\_whitespace():*

*+    test = Text(”     “)*

*+    test.strip()*

*+    assert str(test) == “”*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)