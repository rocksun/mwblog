# Automatically Generate Types for Your PostgreSQL Database
![Featued image for: Automatically Generate Types for Your PostgreSQL Database](https://cdn.thenewstack.io/media/2024/04/397f878b-tns-automatically-generate-types-for-your-sql-queries-featured-image-1024x538.jpg)
I’ve been doing a lot of work in and around
[PostgreSQL](https://thenewstack.io/from-a-fan-on-the-ascendance-of-postgresql/) for JavaScript developers lately, and my general understanding is that JavaScript developers will do absolutely anything to avoid writing code that isn’t JavaScript. They’ll put their [CSS in JavaScript](https://thenewstack.io/tailwind-css-for-developers-style-without-using-css-code/), [HTML in Jsx](https://thenewstack.io/how-to-build-a-server-side-react-app-using-vite-and-express/) and now SQL in JavaScript!
This is what I’m talking about.
This syntax doesn’t have an official name, and in the case of Supabase, it’s an abstraction on top of
[PostgREST](https://postgrest.org/en/v12/#). However, I’d like to propose we call this syntax [SamQL-Jackson](https://twitter.com/PaulieScanlon/status/1783547347475067172).
There are a number of reasons why JavaScript developers would choose this syntax over “raw SQL,” and from my observations, they broadly fall into three categories:
- I haven’t got time to learn SQL.
- I don’t want to learn SQL.
- SQL isn’t type safe.
## 1. “I haven’t got time to learn SQL.”
This is subjective and can’t really be argued. If you’re too busy to learn new things, I completely understand.
## 2. “I don’t want to learn SQL.”
Point 2 is also somewhat subjective — learning something you have little interest in is usually more difficult. However, my one caveat to that point would be that SQL is widely used, so it might be a good arrow to have in your quiver.
## 3. “SQL isn’t type safe.”
Point 3 is a little difficult to address, so here’s an explanation from Jiri Cincura:
[Type safety of SQL commands](https://www.tabsoverspaces.com/232264-type-safety-of-sql-commands#:~:text=Summary%3F,your%20code%20and%20compiler%27s%20rules.). *“SQL commands are type safe but only on server. Written in your applications code it’s still type safe, but not from point of view of type safety of your code and compiler’s rules”*
What this boils down to is that if SQL queries aren’t typed, there’s no type preview available within the code editor. For example:
Not having type definitions available can make it harder to work with database responses.
Other than manually inspecting table schema, or using a
console.log(), there’s no easy way to see what values are contained within a response or table. There’s also the mental shift of understanding how to, in your head, convert Postgres schema; e.g.
VARCHAR(255) to a TypeScript type, e.g.,
string. You could perhaps use a
typeof in your
console.log(), but it’s still not a great solution.
In short, there is absolutely a need to provide type definitions when using SQL in a “JavaScript” codebase, but creating these types manually could be time-consuming and will likely change over time — requiring further manual intervention and further time spent.
It is understandable, then, why many JavaScript developers would choose to use SamQL-Jackson over “raw SQL,” as many of these JavaScript database vendors have type safety built-in to their clients and SDKs. But in these scenarios, you’ll still need to learn their vendor-specific syntax, because unfortunately, each vendor handles this syntax slightly differently.
Here’s an example of a simple SQL query which selects the values
first_name,
country and
users.
And here’s the same query for Supabase and Xata.
### Supabase
### Xata
You’ll notice that both of these queries are different from one another, which might be okay if you’re only ever planning on using Supabase. But if you do ever need to switch database providers, you’d have to learn a whole new syntax — not to mention rewriting a bunch of queries.
Naturally, if you write SQL then the queries will work with every PostgreSQL solution, and while I can’t say for sure, these reasons do somewhat challenge the above points 1 and 2.
*It’s worth noting that both Supabase and Xata can be queried using “ordinary” SQL too, FYI!*
In any case, should you decide to go the “raw SQL” route and need types, here are a couple of options for you.
## Automatic Type Generation
There are two solutions I’ve experimented with:
[kysely-codegen](https://github.com/RobinBlomberg/kysely-codegen) and [pg-to-ts](https://github.com/danvk/pg-to-ts). Both have worked out pretty well for me, so here’s how to use them.
## How to Use kysely-codegen
[kysely-codegen](https://github.com/RobinBlomberg/kysely-codegen) generates Kysely type definitions from your database. That’s it.
### Kysely Installation
Run the following to install the main Kysely package. Also check the
[install instructions](https://github.com/RobinBlomberg/kysely-codegen?tab=readme-ov-file#installation), because in my case, I also needed to install [pg](https://www.npmjs.com/package/pg).
You’ll also need to run the following to install the codegen package.
### Kysely package.json script
For convenience, I added a script to my
package.json. Using the
-out-file flag this script will create a file named
kysely-db.d.ts and the root of my project.
### Kysely .env
Kysely requires you to have an environment variable named
DATABASE_URL in your
.env file.
### Kysely generate
You can now run the following script, and you should see a new .d.ts file at the root of your project, containing all the types for all the tables and columns in your database.
Here’s a snippet of what my test database looks like. It only contains one table named
*users*.
### Kysely typed query
And here’s how I’ve used the generated types in my PostgreSQL query, but these type definitions could also be used as part of a component’s props interface.
## How to Use pg-to-ts
[pg-to-ts](https://github.com/danvk/pg-to-ts) generates TypeScript types that match your Postgres database schema. It works by querying the Postgres metadata schema (pg_catalog) and generating equivalent TypeScript types, as well as some JavaScript values that can be helpful for generating queries at runtime.
### pg-to-ts Installation
Run the following to install the main pg-to-ts package.
### pg-to-ts package.json script
For convenience, I added a script to my
package.json. Using the
-c flag you can reference the
DATABASE_URL, which you can pass along when running the script from your terminal. This script will create a file named
pg-to-ts-db.d.ts and the root of my project.
### pg-to-ts generate
You can now run the following script providing your
DATABASE_URL before the npm run command, and you should see a new .d.ts file at the root of your project containing all the types for all the tables and columns in your database.
Here’s a snippet of what my test database looks like. It only contains one table named
*users*.
### pg-to-ts typed query
And here’s how I’ve used the generated types in my PostgreSQL query, but these type definitions could also be used as part of a component’s props interface.
## Finished
So there you have it, SQL can be typesafe (in the JavaScript sense of the word). It’s automated, so it’s not a massive problem when schema changes occur. But more than that, I hope you’re now a little less reluctant to work with “raw SQL.” It is, after all, the language of databases.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)