
<!--
title: 比较Go、Rust、Scala、Java、Kotlin、Python、Typescript 和 Elm中的编译器错误
cover: /cover.png
-->

开发人员的生产力受多种因素影响。我们比较了 Go、Rust、Python、Typescript、Scala 和 Java 中的编译器消息。

> 译自 [Comparing Compiler Errors in Go, Rust, Scala, Java, Kotlin, Python, Typescript, and Elm](https://www.inkmi.com/blog/developer-productivity-compiler-errors.html)，作者 Stephan Schmidt。

**TLDR** *编译器错误消息差异很大，并且没有关于编译器消息的标准或共同理解。从简短且令人困惑到冗长的解释。*

语言 | 编译器消息 |
---|---|
Java | 非常简短的编译器错误，措辞令人困惑 |
Scala | 良好的编译器错误，显示了有问题的数值 |
Kotlin | 简短、不清楚的错误消息 |
Python | 运行时错误，简短但比 Java 更清晰的措辞 |
Typescript | 非常非常简短的错误消息，不显示有问题的源代码行，仅与 IDE 配合使用，措辞良好 |
Go | 与 Typescript 相似，不显示有问题的源代码行，仅与 IDE 配合使用，措辞良好 |
Rust | 冗长的编译器错误消息，错误对应的源代码的不同部分。建议使用现有方法进行帮助。具有冗长、可选的错误解释。可能是最好的 |
Elm | 以开发人员为中心的冗长错误消息。建议使用现有方法来解决拼写错误。错误消息还包含一个提示，以了解/减轻错误情况。 |

## 开发人员效率

开发人员效率有许多因素。今天我们将研究编译器错误。编译器错误越完善、越有帮助，开发人员就能越快地解决问题并继续编码。

为此，我们比较

- Rust (1.64.0)
- Go (1.18.2)
- Python (3.8.5)
- Elm (0.19.1)
- Java (19 Amazon)
- Scala (3.2.0)
- Kotlin (1.7.20)
- Typescript (4.8.4)

虽然 `Elm` 不是主流语言，但它在编译器错误消息方面被认为是最好的语言之一。我们将看看这是否合理。

## 调用不存在的方法或函数

我们首先调用一个不存在的方法或函数。

`Java` 有一个简单明了的错误消息，尽管 `cannot find symbol`
消息不太清楚（为什么你丢失了符号？）并且消息的其余部分只是在重复自己：

```
$ javac -classpath java/ java/Error1.java

java/Error1.java:6: error: cannot find symbol
        e.notThere();
         ^
  symbol:   method notThere()
  location: variable e of type Error1
1 error
```

接下来是 `Python`，另一种像 `Java` 一样经历过多次迭代的古老语言。与之前一样，简单的消息。与 Java 相比，`'Error1' object has no attribute 'notThere'` 更清晰。

```
$ python3 python/Error1.py

Traceback (most recent call last):
  File "python/Error1.py", line 6, in <module>
    e.notThere()
AttributeError: 'Error1' object has no attribute 'notThere'
```
接下来是更新的 JVM 语言 `Scala`
。更花哨的输出（带颜色），但与 Python 中的错误消息相同，如果你不是绝对的初学者，很容易找到问题。

```
$ scalac scala/Error1.scala

-- [E008] Not Found Error: scala/Error1.scala:4:7 -----------------------------------------------
4 |     e.notThere()
  |     ^^^^^^^^^^
  |     value notThere is not a member of Error1
1 error found
```

我加入 Kotlin 是因为 `SDKman`
使安装更多语言变得如此容易。此外，构建 Android 应用程序的人使用 Kotlin。简短而简单的错误消息，但 `unresolved reference: notThere`
对我来说比 Java 的更糟糕。

```
$ kotlinc kotlin/Error1.kt

kotlin/Error1.kt:4:11: error: unresolved reference: notThere
        e.notThere()
          ^
```

离开 `JVM`，我们来到 Go，一种我目前正在学习的语言。非常简短的错误消息（一行），并有很好的解释 `type Error1 has no field or method error`

```
$ go build go/Error1.go

# command-line-arguments
go/Error1.go:12:7: e.error undefined (type Error1 has no field or method error)
```

`Typescript` 也是如此，一行错误消息，并有很好的解释。我们还得到了一个错误编号 `TS2339`。遗憾的是，在 Google 上搜索该编号没有找到更多信息。此外，Typescript 不会显示有问题的行或受影响的类型。这可能在你只使用 IDE 时没问题，但我没有。

```
$ npx tsc typescript/Error1.ts

typescript/Error1.ts(4,11): error TS2339: Property 'notThere' does not exist on type 'Error1'.
```

然后是 `Rust`！我非常喜欢的一种语言（非常好的工具链），如果它没有为结构体使用借用检查器，而是使用可选的 GC，而不是用 `Arc`（喜欢 `move` 和 &mut 用于方法调用，每种语言都应该有这个，但我离题了）来修补所有内容。让我们看看它在编译器错误方面的表现。

它向你抛出一个大型错误消息，其中包含一些信息。它是第一个尝试帮助你并显示类似方法的，该方法称为 `error1`。它还显示了尝试查找方法的结构体。

```
$ rustc rust/Error1.rs

error[E0599]: no method named `error` found for struct `Error1` in the current scope
  --> rust/Error1.rs:12:7
   |
1  | struct Error1 {
   | ------------- method `error` not found for this struct
...
12 |     e.error();
   |       ^^^^^ help: there is an associated function with a similar name: `error1`

error: aborting due to previous error

For more information about this error, try `rustc --explain E0599`.
```

但 `Rust` 并没有止步于此。当使用建议的 `rustc --explain E0599` 时，它会详细解释错误。对于这个例子来说，这可能微不足道，但它使学习一门语言变得容易得多，这有助于入门和提高生产力。

```
$ rustc --explain E0599

This error occurs when a method is used on a type that doesn't implement it:

Erroneous code example:

struct Mouth;

let x = Mouth;
x.chocolate(); // error: no method named `chocolate` found for type `Mouth`
//        in the current scope

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


最后，我们检查了著名的 `Elm`
的编译器错误。它有点不同，因为我没有使用类，以及 `Elm 中函数的工作方式`。就像 `Rust` 一样，它显示了它找到的类似内容，`error1`。

```
Compiling ...-- NAMING ERROR ------------------------------------------------- src/Error1.elm

I cannot find a `error` variable:

7|    error { msg = "Error happened"}
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

在使用 `Elm` 时，我犯了一些初学者错误。其中一个是文件命名错误。`Elm` 友好地帮助我命名。通常情况下，需要花一些时间才能了解一门语言对文件格式的期望，而 `Elm`
在解释问题及其背后的原因方面非常有帮助。我印象深刻，希望更多语言能做到这一点。

```
Compiling ...-- UNEXPECTED FILE NAME --------------------------------------------------------

I am having trouble with this file name:

    src/error0.elm

I found it in your /home/stephan/Development/prod_compilererrors/elm/src/
directory which is good, but I expect all of the files in there to use the
following module naming convention:

    +--------------+------------------------------------------------------------------------+
    | Module Name  | File Path                                                              |
    +--------------+------------------------------------------------------------------------+
    | Main         | /home/stephan/Development/prod_compilererrors/elm/src/Main.elm         |
    | HomePage     | /home/stephan/Development/prod_compilererrors/elm/src/HomePage.elm     |
    | Http.Helpers | /home/stephan/Development/prod_compilererrors/elm/src/Http/Helpers.elm |
    +--------------+------------------------------------------------------------------------+

Notice that the names always start with capital letters! Can you make your file
use this naming convention?

Note: Having a strict naming convention like this makes it a lot easier to find
things in large projects. If you see a module imported, you know where to look
for the corresponding file every time!

Detected a problem.
```

比较第一批编译器错误，我认为 Java 最糟糕，它的简短 `cannot find symbol` 与 Typescript 并列，因为它们没有显示有问题的源代码行。Elm 非常出色，正如承诺的那样，但就我个人而言，`Rust`
编译器错误是最好的。它们使学习语言或修复尚未遇到的错误变得容易。有些人可能称之为“保姆编译器”，但我乐于接受任何帮助，因为我总是可以减少错误报告。

## 使用错误参数调用方法

要比较的第二件事是，我们使用 `int, String` 而不是 `String, int` 调用方法。

使用 `Java`，我们再次得到一条简短的错误消息。虽然正确，但它没有检测到我们颠倒了方法的参数。这次我们得到了一条更详细的消息，包括源代码行。

```
java/Error2.java:6: error: incompatible types: int cannot be converted to String
        e.error(42, "Hello");
                ^
Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output
1 error
```

使用建议的 `-Xdiags:verbose`
会导致更详细（当然！）的错误消息，更好地解释了问题（找到/需要）。但原因仍然令人困惑。

```
java/Error2.java:6: error: method error in class Error2 cannot be applied to given types;
        e.error(42, "Hello");
         ^
  required: String,int
  found:    int,String
  reason: argument mismatch; int cannot be converted to String
1 error
```

接下来是 `Scala`。我们得到两个错误，每个参数一个。这次我们使用了建议的 `-explain` 编译器开关来查看更长的错误消息。`Scala` 错误消息的优点是它们显示了有问题的代码行、值（42，“Hello”）、值的类型以及它们应该是什么。解释相当冗长，在这种情况下没有帮助。由于 `Scala` 可以具有非常复杂的类型，这些类型可能与参数匹配，也可能不匹配，我想这对更复杂的自定义类型很有帮助。是的，努力是好的，但在这里没有帮助。

```
-- [E007] Type Mismatch Error: scala/Error2.scala:4:12 - - - - - - - - - - - - - - - - - - - - -
4 |    e.error(42, "Hello")
  |            ^^
  |            Found:    (42 : Int)
  |            Required: String
  |- - - - - - - - - - - - - - - - - - - - -
  | Explanation (enabled by `-explain`)
  |- - - - - - - - - - - - - - - - - - - - -
  |
  | Tree: 42
  | I tried to show that
  |   (42 : Int)
  | conforms to
  |   String
  | but the comparison trace ended with `false`:
  |
  |   ==> (42 : Int)  <:  String
  |     ==> (42 : Int)  <:  String
  |       ==> Int  <:  String (left is approximated)
  |       <== Int  <:  String (left is approximated) = false
  |     <== (42 : Int)  <:  String = false
  |   <== (42 : Int)  <:  String = false
  |
  | The tests were made under the empty constraint
   - - - - - - - - - - - - - - - - - - - - -
-- [E007] Type Mismatch Error: scala/Error2.scala:4:16 - - - - - - - - - - - - - - - - - - - - -
4 |    e.error(42, "Hello")
  |                ^^^^^^^
  |                Found:    ("Hello" : String)
  |                Required: Int
  |- - - - - - - - - - - - - - - - - - - - -
  | Explanation (enabled by `-explain`)
  |- - - - - - - - - - - - - - - - - - - - -
  |
  | Tree: "Hello"
  | I tried to show that
  |   ("Hello" : String)
  | conforms to
  |   Int
  | but the comparison trace ended with `false`:
  |
  |   ==> ("Hello" : String)  <:  Int
  |     ==> String  <:  Int (left is approximated)
  |     <== String  <:  Int (left is approximated) = false
  |   <== ("Hello" : String)  <:  Int = false
  |
  | The tests were made under the empty constraint
   - - - - - - - - - - - - - - - - - - - - -
2 errors found
```

使用 `Kotlin` 我们也得到两个错误，每个参数都是错误的。

```
kotlin/Error2.kt:4:17: error: the integer literal does not conform to the expected type String
        e.error(42,"Hello")
                ^
kotlin/Error2.kt:4:20: error: type mismatch: inferred type is String but Int was expected
        e.error(42,"Hello")
                   ^
```

Typescript 现在是最糟糕的。它没有显示行或值，而是显示了一个神秘的、技术上正确的错误消息。这对我来说感觉就像 1992 年的 C 语言。

```
typescript/Error2.ts(4,17): error TS2345: Argument of type 'number' is not assignable to parameter of type 'String'.
```

`Go` 也一样，有两个错误，没有上下文。

```
# command-line-arguments
go/Error2.go:12:10: cannot use 42 (untyped int constant) as string value in argument to e.error
go/Error2.go:12:14: cannot use "Hello" (untyped string constant) as int value in argument to e.error
```

让我们看看 `Rust` 如何处理这段错误代码。第一部分是 `Rust` 的一些术语，包括生命周期和一个令人困惑的消息 `an argument of type `
String` is missing` 而不是反转或错误的参数。第二部分更有用，因为它建议使用 `String`（嘿，告诉我使用“hello”）在 `42`（仍然认为 String 丢失了）之前。我认为这不是一个很好的错误消息。

**[正如 Esteban Kuber 正确指出的那样，&str 是我的错误。我认为编译器解释得很好，而我展示了错误的东西]**

```
error[E0308]: arguments to this function are incorrect
  --> rust/Error2.rs:12:7
   |
12 |     e.error(42,"Hello");
   |       ^^^^^ -- ------- argument of type `&'static str` unexpected
   |             |
   |             an argument of type `String` is missing
   |
note: associated function defined here
  --> rust/Error2.rs:5:8
   |
5  |     fn error(&self, arg1: String, arg2: u8) -> bool {
   |        ^^^^^ -----  ------------  --------
help: did you mean
   |
12 |     e.error(/* String */, 42);
   |       ~~~~~~~~~~~~~~~~~~~~~~~

error: aborting due to previous error

For more information about this error, try `rustc --explain E0308`.
```

当我们按照建议进入解释时，这比错误消息更好，因为它指出了我们使用错误的类型作为参数（但没有看到我们反转了参数）。

```
Expected type did not match the received type.

Erroneous code examples:

fn plus_one(x: i32) -> i32 {
x + 1
}

plus_one("Not a number");
//       ^^^^^^^^^^^^^^ expected `i32`, found `&str`

if "Not a bool" {
// ^^^^^^^^^^^^ expected `bool`, found `&str`
}

let x: f32 = "Not a float";
//     ---   ^^^^^^^^^^^^^ expected `f32`, found `&str`
//     |
//     expected due to this

This error occurs when an expression was used in a place where the compiler
expected an expression of a different type. It can occur in several cases, the
most common being when calling a function and passing an argument that has a
different type than the matching type in the function declaration.
```

最后但并非最不重要，我们来看看 `Elm`。它显示第二个参数是错误的，而不是第一个。有点令人困惑，但 `Elm`在这里有一个解释： 

```
Hint: I always figure out the argument types from left to right. If an argument
is acceptable, I assume it is “correct” and move on. So the problem may actually
be in one of the previous arguments!
```

- 所以 42 也可能是错误的。

这里不正确，但有帮助的是提示


```
Hint: Want to convert a String into an Int? Use the String.toInt function!
```


然后 `Elm` 然后移动到第二个错误，即第一个参数。有点令人困惑，但我猜想作为一名 `Elm` 开发人员，这种评估策略会变得自然而然。

```
Compiling ...-- TYPE MISMATCH ------------------------------------------------ src/Error2.elm

The 2nd argument to `error` is not what I expect:

8|   error 42 "Hello"
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

8|   error 42 "Hello"
           ^^
This argument is a number of type:

    number

But `error` needs the 1st argument to be:

    String

Hint: Try using String.fromInt to convert it to a string?


Detected problems in 1 module.
```

我认为 `Rust` 最长，但略微令人困惑。`Elm` 很好，并提供了一些有用的提示，尽管错误排名很奇怪。我认为我更喜欢 Scala 的错误消息，尽管更深入的解释没有帮助，但这里的类型太简单了。但这部分是主观的，你的观点可能会有所不同。

## 结论

编译器错误存在巨大差异，我们的行业似乎还没有就编译器错误消息的重要性或风格达成共识。消息从神秘且误导性到包含详细解释的长篇大论。选择开发平台有很多因素，也许我们应该更多地考虑错误消息。