# Introduction to Gleam, a New Functional Programming Language
![Featued image for: Introduction to Gleam, a New Functional Programming Language](https://cdn.thenewstack.io/media/2024/06/5af404eb-getty-images-n7fry417ibk-unsplash-1024x683.jpg)
When my colleague read my
[Virgil post](https://thenewstack.io/introduction-to-virgil-a-new-language-by-wasms-co-creator/), he immediately suggested I look at [Gleam](http://gleam.run). It is cool and new — version 1 was released [in March](https://gleam.run/news/gleam-version-1/) this year — and comes out solidly on the functional side of programming life.
Gleam is a type-safe functional programming language for building scalable concurrent systems. It compiles to
[Erlang](https://thenewstack.io/past-present-future-erlang/) and [JavaScript](https://thenewstack.io/javascript/), so has straightforward interoperability with other “BEAM” languages such as Erlang and Elixir. (BEAM is the virtual machine that executes user code in the Erlang Runtime System. I believe its short for *Bogdan’s Erlang Abstract Machine.* Don’t ask.)
Erlang was an early telecoms industry language, very much focusing on concurrency and fault tolerance. Its ways of doing things is still respected and accounts for
[Elixir](https://thenewstack.io/past-present-future-erlang/)’s popularity. In this post, I won’t assume you are familiar with these; and actually, Gleam is particularly friendly, so it doesn’t make too many assumptions either.
Let’s start with
*hello world*:
|
1
2
3
4
5
|
import gleam/io
pub fn main() {
io.println("hello world!")
}
This is pretty similar to the same thing in
[Zig](https://thenewstack.io/introduction-to-zig-a-potential-heir-to-c/).
There is a very pleasant
[language tour](https://tour.gleam.run/) that makes use of Gleam’s compiling to JavaScript to give dynamic checking. You can also use it as a playground. [Installing Gleam](https://gleam.run/getting-started/installing/) also means installing Erlang. For my Mac, I just used Homebrew:
|
1
|
> brew install gleam
Homebrew installs Erlang, automatically.
Gleam comes with a template (or project) generator, much like Rails. So to make a new
*hello* project, I just typed:
Rather than saving time for the moment, the “hello world” style one-liner is already there as the default code in
**hello.gleam**:
If I run the whole project:
Note that the two packages were only compiled on the first run.
## Package Management
There are two
*.toml* files (apparently *Tom’s Own Markup Language.* Don’t ask), which act as configuration.
As they should be simple, we can have a quick peek. In the
**gleam.toml:**
|
1
2
|
[dependencies]
gleam_stdlib = ">= 0.34.0 and < 2.0.0"
Note that they have a
*version constraint* — mentioning the maximum version in order to reduce incompatibility.
The actual version downloaded and used is mentioned in the
**manifest.toml.**
We can learn a little Gleam and work with the package manager if we
[follow](https://gleam.run/writing-gleam/) a simple example. We’ll add a couple of packages, and write some code to print out environment variables. I’ll use the same *hello* project template, but with the new code inserted.
First, we’ll add the new packages to allow environment reading (
*envoy*) and the reading of command line arguments ( *argv*) — which you might expect to be built-in but might reflect system differences.
So let’s replace the code in
**hello.gleam** with the code to print out environment variables on demand:
|
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
|
import argv
import envoy
import gleam/io
import gleam/result
pub fn main() {
case argv.load().arguments {
["get", name] -> get(name)
_ -> io.println("Usage: get <name>")
}
}
fn get(name: String) -> Nil {
let value = envoy.get(name) |> result.unwrap("")
io.println(format_pair(name, value))
}
fn format_pair(name: String, value: String) -> String {
name <> "=" <> value
}
Added to the public
main entry point, we have two functions. They use exactly the same format as we saw in Virgil. It turns out that type annotations are optional, but considered good practice. Now, we get a bit functional. The
*argv* load does what you expect, and pulls in a list of hopefully exactly two strings — with the first string equal to “get”. This is used in a
case statement.
As a quick aside, the Gleam
case is a little more flexible than in most non-functional languages. Here we see a lists’ contents being compared:
|
1
2
3
4
5
6
7
|
let result = case x {
[] -> "Empty list"
[1] -> "List of just 1"
[4, ..] -> "List starting with 4"
[_, _] -> "List of 2 elements"
_ -> "Some other list"
}
So,
[patterns can be compared](https://tour.gleam.run/flow-control/list-patterns/) in case statements. That underline
_ represents a default, and the possible cases are exhaustively checked.
Going back to our environment variable reading code, if the pattern
*isn’t* a list of two strings, then the helper text is spat out. Otherwise, it calls the *get* function.
We see the pipe function, which just helps to make long functional calls a little more readable from left to right.
|
1
|
let value = envoy.get(name) |> result.unwrap("")
This is the same as:
|
1
|
let value = result.unwrap(envoy.get(name),"")
Because Gleam doesn’t throw exceptions, it uses the built-in
[Result](https://tour.gleam.run/data-types/results/) type, and *unwrap* fetches the good path value.
The final oddity is:
|
1
|
name <> "=" <> value
…which is just string concatenation.
And here I run it, with the required arguments the second time:
Gleam has no
null, no implicit conversions, and no exceptions. So if it compiles, you are good. Also, there is no numerical operator overloading, so the code for adding integers is different to that for adding floats:
|
1
2
|
io.debug(1 + 1) //ints
io.debug(1.0 +. 1.5) //floats
Equality works for any type. The general concept of immutability is best experienced by using a functional language for a bit, so I won’t gloss over it. It does help cut out a whole subset of bugs.
## Algebraic Data Types
Finally, we saw
**Algebraic Data Types** (ADTs) used in [Virgil](https://thenewstack.io/introduction-to-virgil-a-new-language-by-wasms-co-creator/), so I’m keen to see how the equivalent works in Gleam. In fact, we’ve already seen the use of the
case statement.
We get custom types, which we pattern match over. So we are part of the way there:
|
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
|
pub type Season {
Spring
Summer
Autumn
Winter
}
fn weather(season: Season) -> String {
case season {
Spring -> "Mild"
Summer -> "Hot"
Autumn -> "Windy"
Winter -> "Cold"
}
}
Types can hold data in
[records](https://tour.gleam.run/data-types/records/), which is how we get close to my Virgil example:
|
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
|
import gleam/io
pub type Travel {
Walk(hours: Int)
Cycle(hours: Int)
Drive(hours: Int, speed: Int)
}
pub fn main() {
let walking = Walk(1)
let cycling = Cycle(1)
let bus_trip = Drive(2, 50)
let trip = [walking, cycling, bus_trip]
io.debug(trip)
}
// [Walk(hours: 1), Cycle(hours: 1), Drive(hours: 2, speed: 50)]
I don’t think I can associate a method inside a type, but I can access the record values to get a similar result as we got in Virgil. I’ll leave this as an exercise for a more fluent user!
For someone like me who doesn’t work with functional code much, Gleam is very approachable and doesn’t immediately confront me with terminology like “currying” and other functional shocks. But it should be a good way to get you to appreciate the immutable advantages of programming if you are not already an advocate.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)