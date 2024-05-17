# Outer Excuses: Why JavaScript Developers Should Learn SQL
![Featued image for: Outer Excuses: Why JavaScript Developers Should Learn SQL](https://cdn.thenewstack.io/media/2024/05/46766d59-tns-outer-excuses-learn-postgresql-featured-image-1024x538.jpg)
Hello. You’re a JavaScript developer, right? Would I also be right in assuming that you don’t know SQL, and you don’t want to learn SQL?
In this article, I’d like to introduce you to
[Outerbase](https://www.outerbase.com/) which, among other things, allows you to create, edit, visualize and explore the data in your database — all without having to write SQL. More on that in just a moment, but first, let’s address the elephant in the room (pun intended)
JavaScript developers are running out of excuses not to learn SQL.
Many JavaScript developers will do quite literally anything to avoid
[learning SQL](https://thenewstack.io/how-to-write-sql-queries/), and after a little bit of research, I’ve boiled it down to three key reasons:
- I haven’t got time to learn SQL.
- I don’t want to learn SQL.
- SQL isn’t type-safe.
In a previous article:
[Automatically Generate Types for Your PostgreSQL Database](https://thenewstack.io/automatically-generate-types-for-your-postgresql-database/), I addressed point 3, so now it’s time to circle back and tackle points 1, and 2.
## You Don’t Want to Learn SQL?
I can’t, and won’t ever, understand why you don’t have time to invest in yourself, so let’s skip point 1.
Point 2, however, is something I’d like to address. The lines between frontend and backend are becoming more and more blurred in JavaScript land, and I think that’s actually pretty cool. Frontend devs can now do things that before would have required deep backend knowledge. However, that doesn’t mean you should skip the fundamentals.
SQL is the language of databases and if you’re a JavaScript developer using PostgreSQL, it’s beneficial to have at least a basic understanding of SQL, even if you do eventually end up using a JavaScript client to query your database.
The road to learning SQL can be a little rocky, but thankfully with the rise of AI and the developer tools companies using it, learning SQL might have just become a lot easier.
## Getting Started With Outerbase
Go ahead and
[sign up](https://app.outerbase.com/signup/), then [connect Outerbase to your database](https://docs.outerbase.com/bases/connect-database). Once you’re connected, you can begin to write queries using natural language and Outerbase AI will convert your “conversation” into a SQL query.
I’ve connected Outerbase to my PostgreSQL database which I use to capture site visits and display them on the
[dashboard of my site](https://www.paulie.dev/dashboard/). I store geolocation data from site visitors in a table named
analytics. The table schema looks like this:
In the below “conversation” I’ve asked Outerbase to count the number of visits from each country in the
analytics table.
And without any bother at all, Outerbase wrote the following SQL query, which I’ve run right there in the browser to see the results.
From here I could very easily copy and paste this query into my code, and et voilà, I’d have data to display any which way I like in my frontend.
## Write SQL Without Learning SQL
By using Outerbase AI, you can describe the data you’d like to query using natural language, and Outerbase AI will write the SQL query for you. It feels like a nice middle ground for developers wishing to dip their toe in the PostgreSQL pool (again, pun intended), but without getting snagged up on unfamiliar syntax.
If you’re coming from JavaScript, SQL at first can appear to be like an Alien language, but it’s really not. For instance, can you read this?
I’d imagine you probably can, and that’s by design.
Take a look at this
[video of Don Chamberlin](https://twitter.com/hieuSSR/status/1786270259206668643), one of the principal designers of SQL. In the video, Don explains the fundamental goals guiding the design of the SQL language. Goals 2, 3, and 4 are particularly pertinent.
- We wanted to use the term tables instead of relations…
- We wanted to base the language on ordinary English words like select.
- The language should have no special symbols, and it should be easy to type on a keyboard.
- We wanted it to have something that we called the walk-up and read property. Meaning, in simple cases, a user with no special training should be able to understand a query just by reading it.
I think you’ll agree that the simple
SELECT statement above meets these requirements. Even just simply reading it in the context of an ordinary sentence makes sense. E.g. select name, country, and email from users.
Fun fact: SQL doesn’t have to be written in uppercase.
In JavaScript land, things are a little, well, weird. For instance, here’s the same query used above, but written in Supabase and Xata-specific JavaScript syntax.
### Supabase
### Xata
*It’s worth noting that both Supabase and Xata can be queried using “ordinary” SQL too, FYI!*
Whilst there are advantages to using JavaScript syntax to query a database (
[type safety is not among them](https://thenewstack.io/automatically-generate-types-for-your-postgresql-database/)), I do still wonder why JavaScript developers are so reluctant to learn SQL.
In most cases, SQL expressed in JavaScript requires special knowledge and can’t be read like an ordinary sentence (in English). And more than that, learning what I’m calling
[SamQL-Jackson](https://twitter.com/PaulieScanlon/status/1783547347475067172) (provider-specific JavaScript syntax) is shortsighted. Why spend the time learning something that can only be used with one provider, when you could invest the same amount of time developing skills that are much more widely used and that will greatly improve both your understanding of the technology you’re using and probably your chances of getting hired.
However, there is one remaining point that I do think is a reasonable rationale for using SamQL-Jackson, and that’s
**autocomplete**. For instance, if you were to type
supabase. In your code editor, you’ll be presented with a list containing a number of options to choose from to construct your query.
Arguably though, if you already know SQL, you don’t need autocomplete. You could very easily write queries just as quickly, or take advantage of the ~40 years of internet history that will help you understand SQL; or, better still, something like ChatGPT which also has ~40 years of internet history to reference. If both of those fail, there’s now Outerbase AI, which will write SQL for you!
This might be a little spicy, but JavaScript developers are really running out of excuses not to learn SQL.
## Final Thoughts
It might sound like I’ve got an axe to grind with JavaScript and SaaS PostgreSQL providers, but I don’t. I do, however, have a vested interest in developer education. The “best practices” noise you hear around “
[ship it culture](https://thenewstack.io/say-no-to-ship-it-culture-slow-and-steady-wins-the-race/)” doesn’t apply to you when you’re learning. Speed doesn’t factor in when you’re investing in yourself. If it takes you a year to learn SQL, so be it. SQL is a foundational skill. Learning it, and even perhaps struggling with it, will eventually help you understand why abstractions exist. From there you can make your own decisions about whether or not they suit your requirements.
Starting with abstractions, however, means you miss out on the backstory. That would be like watching a movie and just skipping straight to the last five minutes, just so you can say you reached the end — or, “Look what I shipped”. Of course, it takes longer to watch the entire thing, but during that time you’ll understand the characters, the plotline, and (if the story is told well) you’ll be engaged throughout.
For me, learning is kind of the same thing. I don’t want to skip to the end, I want to experience the whole story. I don’t know if I’ll have changed your opinion about SQL, but I think by using Outerbase AI you might start to see it’s not as scary and verbose as you thought. Give it a go!
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)