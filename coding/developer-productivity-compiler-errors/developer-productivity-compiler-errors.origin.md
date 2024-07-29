**Other Articles**
*Inkmi is Dream Jobs for CTOs and written as a decoupled monolith in Go, HTMX, Alpinejs, NATS.io and Postgres.
I document my adventures and challenges in writing the application here on this blog, tune in again.*
**TLDR** *Compiler error messages are widely different and there is no standard or common understanding of compiler messages. The range from the short and confusing to long explanations. Non detect reversed arguments*
Language | Compiler Messages |
---|---|
Java | Very short compiler errors, wording is confusing |
Scala | Good compiler errors, showing offending values |
Kotlin | Short, unclear error messages |
Python | Runtime errors, short but clearer wording than Java |
Typescript | Very very short error message, does not show offending source line, only works with IDE, good wording |
Go | Similar to Typescript, does not show offending source line, only works with IDE, good workding |
Rust | Long compiler messages, different parts of source code where the error corresponds. Suggests help with existing
methods. Has long, optional explanations for errors. Probably the best |
Elm | Long error messages with the developer in mind. Suggests existing methods for typos. Error messages also have a hint to understand/mitigate the error circumstances. |
## 🦄 Developer Productivity
Developer productivity has many factors. Today we will look into compiler errors. The better and more helpful compiler errors, the faster developers can fix the problem and keep coding.

For this, we compare

- Rust (1.64.0)
- Go (1.18.2)
- Python (3.8.5)
- Elm (0.19.1)
- Java (19 Amazon)
- Scala (3.2.0)
- Kotlin (1.7.20)
- Typescript (4.8.4)
While `Elm`
isn’t a mainstream language, it is considered one of the best when it comes to compiler error messages.
We’ll see if this is justified.

## Call a non-existing method or function
We start by calling a method or function that does not exist.

`Java`
has a plain and simple error message, though the `cannot find symbol`
message is not very clear (why did you lose the symbol?) and the rest of the message is only repeating itself:
```
$ javac -classpath java/ java/Error1.java
java/Error1.java:6: error: cannot find symbol
e.notThere();
^
symbol: method notThere()
location: variable e of type Error1
1 error
```
Moving on to `Python`
, another old language on the block that went through many iterations just like `Java`
. Same as before, simple message. Compared to Java the `'Error1' object has no attribute 'notThere'`
is much clearer.

```
$ python3 python/Error1.py
Traceback (most recent call last):
File "python/Error1.py", line 6, in <module>
e.notThere()
AttributeError: 'Error1' object has no attribute 'notThere'
```
Moving on to a newer JVM language, `Scala`
. A fancier output (with color), but the same error message as in Python, easy to find the problem if you’re not an absolute beginner.

```
$ scalac scala/Error1.scala
-- [E008] Not Found Error: scala/Error1.scala:4:7 -----------------------------------------------
4 | e.notThere()
| ^^^^^^^^^^
| value notThere is not a member of Error1
1 error found
```
I throw in Kotlin because `SDKman`
made it so easy to install more languages. Also, people building Android apps use Kotlin. A short and simple error message, but `unresolved reference: notThere`
to me is worse than the one of Java.

```
$ kotlinc kotlin/Error1.kt
kotlin/Error1.kt:4:11: error: unresolved reference: notThere
e.notThere()
^
```
Leaving the `JVM`
we come to Go, a language I currently try to learn. Very short error message (one line), with a good explanation `type Error1 has no field or method error`

```
$ go build go/Error1.go
# command-line-arguments
go/Error1.go:12:7: e.error undefined (type Error1 has no field or method error)
```
The same with `Typescript`
, one line error message with a good explanation. We also get an error number `TS2339`
. Sadly googling the number does not turn up more information. Also, Typescript does not show the offending line or the affected type. This probably is fine when you’re only using the IDE, which I don’t.

```
$ npx tsc typescript/Error1.ts
typescript/Error1.ts(4,11): error TS2339: Property 'notThere' does not exist on type 'Error1'.
```
Then `Rust`
! A language I rather like a lot (very good toolchain), if it didn’t have the borrow checker for structs and just used an optional GC instead of plastering everything with `Arc`
(love `move`
and &mut for method calls though, every language should have this, but I digress). Let’s see how it fares on compiler errors.

It throws a large error message at you, with some information. It is the first that tries to help you and shows a similar method which is called `error1`
. It also shows the struct where it tried to find the method.

```
$ rustc rust/Error1.rs
error[E0599]: no method named `error` found for struct `Error1` in the current scope
--> rust/Error1.rs:12:7
|
1 | struct Error1 {
| ------------- method `error` not found for this struct
...
12 | e.error();
| ^^^^^ help: there is an associated function with a similar name: `error1`
error: aborting due to previous error
For more information about this error, try `rustc --explain E0599`.
```
But `Rust`
doesn’t stop there. When using the suggested `rustc --explain E0599`
it explains the error in great detail. It might be trivial for this example but makes learning a language much easier, which helps with onboarding and productivity.

```
$ rustc --explain E0599
This error occurs when a method is used on a type that doesn't implement it:
Erroneous code example:
struct Mouth;
let x = Mouth;
x.chocolate(); // error: no method named `chocolate` found for type `Mouth`
// in the current scope
In this case, you need to implement the `chocolate` method to fix the error:
struct Mouth;
impl Mouth {
fn chocolate(&self) { // We implement the `chocolate` method here.
println!("Hmmm! I love chocolate!");
}
}
let x = Mouth;
x.chocolate(); // ok!
```
Last we check the fabled `Elm`
for compiler errors. It’s a little different because I didn’t use a class and how functions in `Elm work`
. Just like `Rust`
, it shows something similar it found, `error1`
.

```
Compiling ...-- NAMING ERROR ------------------------------------------------- src/Error1.elm
I cannot find a `error` variable:
7| error { msg = "Error happened"}
^^^^^
These names seem close though:
error1
floor
xor
acos
Hint: Read <https://elm-lang.org/0.19.1/imports> to see how `import`
declarations work in Elm.
Detected problems in 1 module.
```
When working with `Elm`
, I made some beginner mistakes. One was the wrong naming of files. `Elm`
kindly helped me with the naming. Where quite often it takes some time to learn about what a language expects files to look like, `Elm`
was very helpful in explaining the problem and the reasoning behind it. I’m impressed and wished more languages would do such a thing.

```
Compiling ...-- UNEXPECTED FILE NAME --------------------------------------------------------
I am having trouble with this file name:
src/error0.elm
I found it in your /home/stephan/Development/prod_compilererrors/elm/src/
directory which is good, but I expect all of the files in there to use the
following module naming convention:
+--------------+------------------------------------------------------------------------+
| Module Name | File Path |
+--------------+------------------------------------------------------------------------+
| Main | /home/stephan/Development/prod_compilererrors/elm/src/Main.elm |
| HomePage | /home/stephan/Development/prod_compilererrors/elm/src/HomePage.elm |
| Http.Helpers | /home/stephan/Development/prod_compilererrors/elm/src/Http/Helpers.elm |
+--------------+------------------------------------------------------------------------+
Notice that the names always start with capital letters! Can you make your file
use this naming convention?
Note: Having a strict naming convention like this makes it a lot easier to find
things in large projects. If you see a module imported, you know where to look
for the corresponding file every time!
Detected a problem.
```
Comparing the compiler errors from the first batch, I’d say Java is the worst with its short `cannot find symbol`
tied with Typescript for not showing the offending source line. Elm is very good as promised but to my taste, the `Rust`
compiler errors are the best. They make it easy to get into the language or fix errors you haven’t encountered yet. Some may call this a nanny compiler, but I take all the help I can get as I can always trim down error reporting.

## Call method with wrong arguments
The second thing to compare is we call a method with `int, String`
instead of `String, int`
.

With `Java`
we get again a small error message. While right, it doesn’t detect that we reversed the arguments to our method. This time we get a more verbose message, including the source line.

```
java/Error2.java:6: error: incompatible types: int cannot be converted to String
e.error(42, "Hello");
^
Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output
1 error
```
Using the suggested `-Xdiags:verbose`
results in a more verbose (duh!) error message that better explains the problem (found/required). The reason is still confusing though.

```
java/Error2.java:6: error: method error in class Error2 cannot be applied to given types;
e.error(42, "Hello");
^
required: String,int
found: int,String
reason: argument mismatch; int cannot be converted to String
1 error
```
On to `Scala`
. We get two errors, one for each argument. This time we used the `-explain`
compiler switch as suggested to see the longer error message. The good thing about the `Scala`
error messages is that they show the buggy line of code, the values (42, “Hello”), the type of the values, and what they should be. The explanation is rather lengthy and not helpful in this case. As `Scala`
can have very complicated types that might or might not match arguments, I guess this is helpful with more complicated custom types. Yeah for effort, not helpful here.

```
-- [E007] Type Mismatch Error: scala/Error2.scala:4:12 - - - - - - - - - - - - - - - - - - - - -
4 | e.error(42, "Hello")
| ^^
| Found: (42 : Int)
| Required: String
|- - - - - - - - - - - - - - - - - - - - -
| Explanation (enabled by `-explain`)
|- - - - - - - - - - - - - - - - - - - - -
|
| Tree: 42
| I tried to show that
| (42 : Int)
| conforms to
| String
| but the comparison trace ended with `false`:
|
| ==> (42 : Int) <: String
| ==> (42 : Int) <: String
| ==> Int <: String (left is approximated)
| <== Int <: String (left is approximated) = false
| <== (42 : Int) <: String = false
| <== (42 : Int) <: String = false
|
| The tests were made under the empty constraint
- - - - - - - - - - - - - - - - - - - - -
-- [E007] Type Mismatch Error: scala/Error2.scala:4:16 - - - - - - - - - - - - - - - - - - - - -
4 | e.error(42, "Hello")
| ^^^^^^^
| Found: ("Hello" : String)
| Required: Int
|- - - - - - - - - - - - - - - - - - - - -
| Explanation (enabled by `-explain`)
|- - - - - - - - - - - - - - - - - - - - -
|
| Tree: "Hello"
| I tried to show that
| ("Hello" : String)
| conforms to
| Int
| but the comparison trace ended with `false`:
|
| ==> ("Hello" : String) <: Int
| ==> String <: Int (left is approximated)
| <== String <: Int (left is approximated) = false
| <== ("Hello" : String) <: Int = false
|
| The tests were made under the empty constraint
- - - - - - - - - - - - - - - - - - - - -
2 errors found
```
With `Kotlin`
we also get two errors, each argument is wrong.

```
kotlin/Error2.kt:4:17: error: the integer literal does not conform to the expected type String
e.error(42,"Hello")
^
kotlin/Error2.kt:4:20: error: type mismatch: inferred type is String but Int was expected
e.error(42,"Hello")
^
```
Typescript for now is the worst. It doesn’t show the line or the values but a cryptic, technically correct, error message. This feels like 1992 C to me.

```
typescript/Error2.ts(4,17): error TS2345: Argument of type 'number' is not assignable to parameter of type 'String'.
```
`Go`
does the same, with two errors, and no context.
```
# command-line-arguments
go/Error2.go:12:10: cannot use 42 (untyped int constant) as string value in argument to e.error
go/Error2.go:12:14: cannot use "Hello" (untyped string constant) as int value in argument to e.error
```
Let’s see how `Rust`
deals with this wrong code. The first part is some `Rust`
jargon including lifetimes and
a confusing message `an argument of type `
String` is missing`
instead of reversed or wrong arguments. The second part is
kind of more useful, as it suggested using a `String`
(hey, tell me to use “hello”) before the `42`
(still thinking the String is missing though). Not a very good error message I think.

**[As pointed out correctly by Esteban Kuber the &str is a mistake on my part. I think the compiler explained it correctly and I’ve showed the wrong thing]**
```
error[E0308]: arguments to this function are incorrect
--> rust/Error2.rs:12:7
|
12 | e.error(42,"Hello");
| ^^^^^ -- ------- argument of type `&'static str` unexpected
| |
| an argument of type `String` is missing
|
note: associated function defined here
--> rust/Error2.rs:5:8
|
5 | fn error(&self, arg1: String, arg2: u8) -> bool {
| ^^^^^ ----- ------------ --------
help: did you mean
|
12 | e.error(/* String */, 42);
| ~~~~~~~~~~~~~~~~~~~~~~~
error: aborting due to previous error
For more information about this error, try `rustc --explain E0308`.
```
When we go into the explanation as suggested, this is better than the error message as it points us to using the wrong type as an argument (but didn’t see that we reversed the arguments).

```
Expected type did not match the received type.
Erroneous code examples:
fn plus_one(x: i32) -> i32 {
x + 1
}
plus_one("Not a number");
// ^^^^^^^^^^^^^^ expected `i32`, found `&str`
if "Not a bool" {
// ^^^^^^^^^^^^ expected `bool`, found `&str`
}
let x: f32 = "Not a float";
// --- ^^^^^^^^^^^^^ expected `f32`, found `&str`
// |
// expected due to this
This error occurs when an expression was used in a place where the compiler
expected an expression of a different type. It can occur in several cases, the
most common being when calling a function and passing an argument that has a
different type than the matching type in the function declaration.
```
Last but not least, on to `Elm`
. It shows the second argument as wrong, not the first. A little bit confusing but `Elm`
has an explanation here: ```
Hint: I always figure out the argument types from left to right. If an argument
is acceptable, I assume it is “correct” and move on. So the problem may actually
be in one of the previous arguments!
```
- so the 42 might be also wrong.

Not correct here, but helpful is the hint of `Hint: Want to convert a String into an Int? Use the String.toInt function!`
.

Then `Elm`
moves to the second error, which is the first argument. A little bit confusing, but I’d guess as an `Elm`
developer the evaluation strategy becomes second nature.

```
Compiling ...-- TYPE MISMATCH ------------------------------------------------ src/Error2.elm
The 2nd argument to `error` is not what I expect:
8| error 42 "Hello"
^^^^^^^
This argument is a string of type:
String
But `error` needs the 2nd argument to be:
Int
Hint: I always figure out the argument types from left to right. If an argument
is acceptable, I assume it is “correct” and move on. So the problem may actually
be in one of the previous arguments!
Hint: Want to convert a String into an Int? Use the String.toInt function!
-- TYPE MISMATCH ------------------------------------------------ src/Error2.elm
The 1st argument to `error` is not what I expect:
8| error 42 "Hello"
^^
This argument is a number of type:
number
But `error` needs the 1st argument to be:
String
Hint: Try using String.fromInt to convert it to a string?
Detected problems in 1 module.
```
I think `Rust`
is the longest, but slightly confusing. `Elm`
is good and has some useful hints, though the error ranking is strange. I do think I like Scala’s error messages best here although the deeper explanation does not help, the types are too simple here. But this is partially subjective and your opinion might differ.

## Conclusion
There are huge differences in compiler errors and our industry doesn’t seem yet to have consent on the importance or style of compiler error messages. The messages range from cryptic and misleading to lengthy ones with detailed explanations. There are many factors to choosing a development platform, perhaps we should take error messages more into account.

### About Inkmi
*Inkmi is a website with Dream Jobs for CTOs. We're on a mission to transform the industry to create more dream jobs for CTOs.
If you're a seasoned CTO looking for a new job, or a senior developer ready for your first CTO calling, head over to
https://www.inkmi.com*