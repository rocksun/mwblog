In July, [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention)[launched Kiro](https://thenewstack.io/kiro-is-awss-specs-centric-answer-to-windsurf-and-cursor/), its answer to Windsurf and Cursor — but with a focus on writing specs over prompts. However, I found that access to it was restricted after a rush of developers went to check it out. I only got off the waitlist a few weeks back, so it’s time now to dive in.

After signing in via [Google](https://cloud.google.com/?utm_content=inline+mention), you should get this screen on the Kiro app:

[![](https://cdn.thenewstack.io/media/2025/09/875b3758-image-1024x921.png)](https://cdn.thenewstack.io/media/2025/09/875b3758-image-1024x921.png)

So enter your code and you should be in.

Apparently, there are at least [six major IDE products](https://visualstudiomagazine.com/articles/2025/07/21/forked-again-awss-kiro-latest-ai-assistant-based-on-vs-code.aspx) based on forks of Visual Code; I know of [Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/) and [Windsurf](https://thenewstack.io/windsurf-an-agentic-ide-that-thinks-and-codes-with-you/). And now Kiro.

Kiro is placed on your path so you can run it from a shell. It opens out looking (unsurprisingly) similar to Visual Code:

[![](https://cdn.thenewstack.io/media/2025/09/d076719d-image-1-1024x766.png)](https://cdn.thenewstack.io/media/2025/09/d076719d-image-1-1024x766.png)

As you can see, it is set to Claude Sonnet 4. I’m going to ignore the “Vibe” option, and switch straight to the “Spec” design path.

## What Is Spec Development?

Kiro’s spec-driven workflow breaks down development into three distinct phases: **generating user stories** with detailed acceptance criteria**, creating a technical design,** and breaking the work into a sequence of **trackable implementation tasks**.

These artifacts should ideally be composable documents with functional business use cases, and are first class objects in the Kiro world. Clearly this is a much more formal approach than just playing poker dice with the large language model. Most teams that follow agile should have no problem with this proposed process, even if your actual workflow varies.

I’ll test Kiro on the same Rails project that I’ve tested a few other [agentic coding products](https://thenewstack.io/developer-walk-through-of-auggie-cli-an-agentic-terminal-app/) on recently. It is my simple game development MVC app that helps me design conversations.

## Vibe to Spec

After loading my codebase as a folder, I can then kick off Kiro by describing the project I want it to work on. In this case, I need a separate utility that only links to one existing model in my system:

[![](https://cdn.thenewstack.io/media/2025/09/b5b5c1b1-image-2.png)](https://cdn.thenewstack.io/media/2025/09/b5b5c1b1-image-2.png)

For my project, I want the user to be able to perform CRUD operations (create, read, update, delete) on a Thought for the Day, which is just some text and an image associated with an existing character voice.

The ghost comes back after looking through the project, and isolating the one related model:

[![](https://cdn.thenewstack.io/media/2025/09/5ecee2c1-image-3-600x1024.png)](https://cdn.thenewstack.io/media/2025/09/5ecee2c1-image-3-600x1024.png)

Let’s look at the first document, requirements.md:

[![](https://cdn.thenewstack.io/media/2025/09/26709886-image-4-1024x279.png)](https://cdn.thenewstack.io/media/2025/09/26709886-image-4-1024x279.png)

This is a good introduction to the normal CRUD operations. It has assumed that the thoughts are inspirational, and that is partly true within the context of the game. It also understands that it should follow convention, as all Rails apps should.

Let’s scroll down to the first user story:

[![](https://cdn.thenewstack.io/media/2025/09/8cdd2a17-image-5-1024x586.png)](https://cdn.thenewstack.io/media/2025/09/8cdd2a17-image-5-1024x586.png)

The role “administrator” isn’t quite right, but the relevant meaning here is “can create content.” Kiro catches the “voice association” criteria, which is the vital connection with the existing voice MVC model. It also spots that a text entry is required, whereas an image is not. This is correct — the writer may not have access to an image when the text is created.

There are six requirement/acceptance sets in total, covering the other CRUD tasks and views.

The last one faces the role of developer, so I know it will use Rails properly:

[![](https://cdn.thenewstack.io/media/2025/09/05bda1dc-image-6-1024x487.png)](https://cdn.thenewstack.io/media/2025/09/05bda1dc-image-6-1024x487.png)

The JSON endpoint is important, as that is how I will move resulting data into the main game. In short, it has covered all the bases — largely without any intervention.

## Design Phase

[![](https://cdn.thenewstack.io/media/2025/09/64677c1e-image-7.png)](https://cdn.thenewstack.io/media/2025/09/64677c1e-image-7.png)

When we are done, we are invited to move on.

Now Kiro looks at the controller and views the code of the other MVC models, so it knows how to proceed. As my project is a Rails app, conventions are already strong:

[![](https://cdn.thenewstack.io/media/2025/09/3d3259eb-image-8-1024x772.png)](https://cdn.thenewstack.io/media/2025/09/3d3259eb-image-8-1024x772.png)

From an agile perspective, this would usually be the domain knowledge of the developer, but it is written in terms that an architect would understand. So it sits between what I would refer to as a “user story” and a “task.” I like the fact it has spotted the Bootstrap styling in the view.

There are about 170 lines of design, so I’ll only show one more section. It captures the relationship again between Voice in the attributes and my existing models, along with the auto-generated things one gets with ActiveRecord:

[![](https://cdn.thenewstack.io/media/2025/09/4fd11ee2-image-9-1024x315.png)](https://cdn.thenewstack.io/media/2025/09/4fd11ee2-image-9-1024x315.png)

There are tests included, but as this is an evolving tool, I will ask for the tests to be removed from the design before we get to tasks:

[![](https://cdn.thenewstack.io/media/2025/09/ebdbaa90-image-10.png)](https://cdn.thenewstack.io/media/2025/09/ebdbaa90-image-10.png)

## Taking Things to Task

Now we are ready to move to implementation:

[![](https://cdn.thenewstack.io/media/2025/09/ba68ae3d-image-11.png)](https://cdn.thenewstack.io/media/2025/09/ba68ae3d-image-11.png)

The task list is written as much for the LLM as it is for a developer:

[![](https://cdn.thenewstack.io/media/2025/09/9af3b7c3-image-12-1024x639.png)](https://cdn.thenewstack.io/media/2025/09/9af3b7c3-image-12-1024x639.png)

However, all the tasks look correct — as you see, they connect back to requirements. Particular concern goes to tasks that affect existing models, as in task three; but it just wants to establish the extra relationship, which should be just one line in the voice.rb model file.

There are little “start task” buttons, so it’s clear these could be used by a team if they wished to work the tasks themselves. Some of the testing tasks feel as if they are a little more for humans:

[![](https://cdn.thenewstack.io/media/2025/09/91856d91-image-13.png)](https://cdn.thenewstack.io/media/2025/09/91856d91-image-13.png)

This underlines an important point, however. Does Kiro expect a human team to work on these tasks, or does it expect the user to be leaning on the LLM for producing code?

At the moment the design leans on the latter, which is the market expectation. But it marks out how the former would work.

## Finalize

[![](https://cdn.thenewstack.io/media/2025/09/2cb730bd-image-14.png)](https://cdn.thenewstack.io/media/2025/09/2cb730bd-image-14.png)

I’m not entirely sure what this phase is truly for, but I am advised to go and start the tasks sequentially.

I won’t go too deep into the result of running the tasks, as we are here to look at specs — we know that LLMs can handle Rails models easily enough. But let’s go through one. The first task starts with the migration file:

[![](https://cdn.thenewstack.io/media/2025/09/b982c14c-image-15.png)](https://cdn.thenewstack.io/media/2025/09/b982c14c-image-15.png)

As this is Rails, it has a defined way to produce a migration file (the database world description of the model), so I can look at the command that is too long for the small box provided:

`rails generate migration CreateThoughtsForTheDay text:text voice_id:integer image_id:string`

Technically, the voice\_id should be a reference, even though it is an integer. But I’ll accept the command. As is the way these days, the LLM looks at what it has done and enhances it:

[![](https://cdn.thenewstack.io/media/2025/09/8f3a18a7-image-16.png)](https://cdn.thenewstack.io/media/2025/09/8f3a18a7-image-16.png)

The resulting migration still doesn’t quite mention the reference directly, but we are now entering the usual world of implementation arguments with your LLM companion. This is a very good time to bow out:

```
class CreateThoughtsForTheDay &lt; ActiveRecord::Migration[8.0]
  def change
    create_table :thoughts_for_the_day do |t|
      t.text :text, null: false
      t.integer :voice_id
      t.string :image_id

      t.timestamps
    end

    add_index :thoughts_for_the_day, :voice_id
    add_foreign_key :thoughts_for_the_day, :voices
  end
end
```

## Conclusion

Kiro is aimed at development teams that can use the artifacts to approve or alter designs outside of the tool. This is a different approach than “vibe coding,” which stays locked within the environment.

I think the workflow may need to be simplified. At the moment I can change an existing requirement and the whole tree will update. I fear the dependency loops caused by user hooks (which I didn’t cover) may get out of hand. Or, more accurately, it might be brittle under stress. But these are early days.

There is a lack of UI “chunkiness” at the moment — there is a lot of text, less iconography and containing graphics. This is initially correct because the shared markdown documents are the “currency” produced.

Because they encroach into a team’s workflow, there will necessarily be quite a lot more user experience work needed to see what teams truly need here, and what they will take on board. I feel that artifact maintenance across a team needs separate tooling.

But overall, I think the approach shown by Kiro is strong. AWS should be commended for backing this ambitious product to launch. It definitely has much more than a ghost of a chance.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)