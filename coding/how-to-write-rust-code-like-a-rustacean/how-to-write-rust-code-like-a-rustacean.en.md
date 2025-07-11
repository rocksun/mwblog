[Rust](https://thenewstack.io/rust/) is no longer the “new kid on the block.” It’s become a [staple of a developer’s tech stack](https://thenewstack.io/rust-programming-language-guide/), helping to power performance-critical systems, and trusted by technologists for [its memory safety](https://thenewstack.io/survey-memory-safe-rust-gains-45-of-enterprise-development/), zero-cost abstractions and expressive type system. If you’ve worked with [JavaScript](https://thenewstack.io/javascript-kung-fu-elegant-techniques-to-master-the-language/) and want to explore something that’s both expressive and system-level, Rust is the perfect next step, especially in our [Linux-driven](https://training.linuxfoundation.org/training/programming-in-rust-lfd480/) world.

In this tutorial, I will show you how to write “idiomatic” Rust code, meaning code that is succinct and follows Rustaceans’ (the Rust community’s name) established style and practices. I’ll focus on best practices, safety and performance, all while embracing Rust’s environment and tooling. I’ll also explain some of the most common mistakes Rust developers make and their implications.

So why should you choose Rust for [Linux development](https://thenewstack.io/introduction-to-linux-operating-system/)? Whether you’re building command-line tools, daemons or even kernel-level software, Rust’s design is perfect for Linux environments. It’s fast, with predictable performance, powerful compiler checks, an excellent type system and memory safety without a garbage collector. Its package manager, [Cargo](https://github.com/rust-lang/cargo), is a big plus too. You basically get C-level speed without the risk of segmentation faults or buffer overflows.

## Install Rust

On macOS, you can install Rust using `rustup,` the official installer that handles versions and toolchains with:

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Whereas on Windows, visit the [Rust installation page](https://www.rust-lang.org/tools/install) to download `rustup-init.exe`, and then follow the command-line prompts in the installer (default settings are fine for most users).

Once installed, you can use the `cargo` CLI to create and manage projects. Use these commands to create and run a new project:

```
cargo new hello_rust 
cd hello_rust
cargo run
```

[![Create a new Rust project](https://cdn.thenewstack.io/media/2025/07/2ddd82b7-rust_new-project1.png)](https://cdn.thenewstack.io/media/2025/07/2ddd82b7-rust_new-project1.png)

Source: Zziwa Raymond Ian

Note: I am using VS Code as my text editor with the `rust-analyzer` extension.

## Write and Use Idiomatic Rust Code

Now on to the key principles of writing idiomatic Rust.

To start off, Rust favors safety with `Option` and `Result.`With this capability, Rust helps you avoid nulls. Instead, it uses `Option<T>` and `Result<T, E>` to explicitly handle missing or failed data.

Take a look at the code below.

[![Rust code performs division functions](https://cdn.thenewstack.io/media/2025/07/be89c8f4-rust_division.png)](https://cdn.thenewstack.io/media/2025/07/be89c8f4-rust_division.png)

Source: Zziwa Raymond Ian

In the `main` function, two division operations are performed using the `divide` function. The first divides 10.0 by 2.0, and the result is matched: if it returns `Some(value)`, it prints the result; if it returns `None`, it prints an error message indicating division by zero. The second attempt divides 10.0 by 0.0, which triggers the `None` case and outputs the error message. This demonstrates how the `divide` function safely performs division between two `f64` numbers by returning an `Option<f64>`, which helps prevent runtime errors like division by zero. If the divisor `b` is 0.0, the function returns `None` to indicate an invalid operation; otherwise, it returns `Some(a / b)` with the result.

This approach uses Rust’s `Option` type to handle potential failure in a controlled and type-safe manner, encouraging developers to explicitly deal with the possibility of an absent result.

### Crates in Rust

In Rust, **crates** are the fundamental units of code compilation and sharing — they can be libraries or executable packages. The Rust ecosystem is rich with high-quality crates that make it easy to build robust applications quickly and safely.

Consider the snippet below to see how to use crates via your project’s `Cargo.toml` file:

[![Using crates in Rust](https://cdn.thenewstack.io/media/2025/07/b2593f05-rust_crates.png)](https://cdn.thenewstack.io/media/2025/07/b2593f05-rust_crates.png)

Source: Zziwa Raymond Ian

This configuration adds the following crates as dependencies:

* **`serde`** → A framework for **serializing and deserializing** data formats such as JSON, YAML, TOML, etc. The `derive` feature allows automatic generation of boilerplate code via macros.
* **`tokio`** → An **asynchronous runtime** used to write concurrent programs using async/await syntax, commonly used in networked applications.
* **`clap`** → A powerful and ergonomic crate for **parsing command-line arguments**, making it easy to build user-friendly CLI tools.

Once added, you can run `cargo build` or `cargo run`, and Cargo will automatically download, compile and link these crates to your project, as shown in the screenshot below.

[![Using cargo to add dependencies in Rust](https://cdn.thenewstack.io/media/2025/07/bad3f24a-rust_cargo.png)](https://cdn.thenewstack.io/media/2025/07/bad3f24a-rust_cargo.png)

Source: Zziwa Raymond Ian

### Iterators in Rust

Rust encourages a functional programming style through its powerful and flexible **iterator system**. Instead of relying on traditional `for` loops, you can use iterators to **chain operations** such as `map`, `filter` and `fold` directly on collections. This results in code that is often more concise, expressive and efficient.

#### **For example:**

```
let nums = vec![1, 2, 3, 4, 5];
let doubled: Vec<_> = nums.iter().map(|x| x * 2).collect();
```

#### **What’s happening:**

* `nums` is a vector containing the integers 1 through 5.
* `nums.iter()` returns an iterator over **references** to each element (`&i32`).
* `.map(|x| x * 2)` applies a function that multiplies each item by 2. Since `x` is a reference, Rust automatically dereferences it during the operation.
* `.collect()` gathers the transformed items into a new `Vec`, which is assigned to `doubled`.

#### Why Use Iterators?

* **Lazy evaluation**: Iterators don’t compute values until they’re needed, enabling better performance.
* **Memory safety**: Iterators avoid common errors like out-of-bounds access.
* **Loop fusion**: The compiler can optimize chained operations into a single pass over the data.
* **Readability and maintainability**: Complex logic can often be expressed more clearly with chained iterator methods.

Rust’s iterator system is a key feature that empowers you to write high-performance, clean and safe code with minimal effort.

### Pattern Matching

Pattern matching is powerful in Rust because it provides a clear, concise and exhaustive way to handle different cases. It ensures all possible inputs are considered, reduces bugs and makes code more readable and maintainable, especially when working with enums, ranges and complex data structures.

The code in the screenshot below illustrates the strength of pattern matching.

[![Pattern matching in Rust](https://cdn.thenewstack.io/media/2025/07/d59fe1b0-rust_pattern-matching.png)](https://cdn.thenewstack.io/media/2025/07/d59fe1b0-rust_pattern-matching.png)

Source: Zziwa Raymond Ian

This Rust function `describe` takes an `i32` value and returns a string slice describing the value based on pattern matching. It uses a `match` expression to compare `value` against multiple patterns:

* If it’s `0`, it returns `Zero`.
* If it’s within the range `1..=10`, it returns `Between 1 and 10`.
* For all other values (handled by the wildcard `_`), it returns `Greater than 10`.

The return type `&'static str` indicates the function returns a string with a static lifetime, such as string literals.

## Run Tests in Rust

It’s easy to run tests in Rust:

[![Running tests in Rust](https://cdn.thenewstack.io/media/2025/07/0f0cf221-rust_tests.png)](https://cdn.thenewstack.io/media/2025/07/0f0cf221-rust_tests.png)

Source: Zziwa Raymond Ian

This Rust code defines a test module using `#[cfg(test)]`, which tells the compiler to include the module only when running tests. Inside the `tests` module, `use super::*;` brings the items from the parent module (like the `divide` function) into scope. It contains two unit tests:

* `it_divides_correctly` checks that dividing 10.0 by 2.0 returns `Some(5.0)`.
* `it_handles_divide_by_zero` verifies that dividing by zero returns `None`.

The `#[test]` attribute marks each function as a test case.

Using this approach allows you to automatically verify that code behaves as expected, making it easier to catch bugs and ensure code correctness over time.

Run the test with the command:

```
cargo test
```

You can add a linter and a formatter by running:

```
cargo fmt # Format your code
cargo clippy # Catch potential issues
```

## Use Rust to Build a Calculator

To demonstrate how Rust works, I’ll build a tiny command-line calculator using `clap`.

```
use clap::Parser;

/// Simple calculator
#[derive(Parser)]
struct Args {
#[arg(short, long)]
a: i32,

#[arg(short, long)]
b: i32,
}

fn main() {
let args = Args::parse();
println!("{} + {} = {}", args.a, args.b, args.a + args.b);
}
```

This uses the `clap` crate to create a simple command-line calculator that adds two integers. The `Args` struct is annotated with `#[derive(Parser)]`, which automatically generates code to parse command-line arguments. Each field (`a` and `b`) is marked with `#[arg(short, long)]`, allowing the user to specify them using short flags like `-a` or long flags like `--a`. In the `main` function, `Args::parse()` reads and parses the arguments from the command line, then the program prints the sum of `a` and `b`.

## Debug Errors

Diving into Rust as a beginner is both exciting and challenging. Rust’s strong emphasis on safety, performance and correctness means the compiler is strict, but that strictness is your ally, not your enemy.

It’s easy to make mistakes in Rust, though. Fixing the common mistakes below are stepping stones on your path to becoming a confident Rustacean.

### 1. Using a Value After Move

```
let v = vec![1, 2, 3];
let moved = v;
// println!("{:?}", v); // ❌ Error: value used after move
```

This code creates a vector `v` containing the values `[1, 2, 3]` and then assigns the ownership to `moved.` In Rust, most types like `Vec<T>` do not implement the `Copy` trait, so assigning them to another variable transfers ownership rather than duplicating the data.

As a result, trying to access `v` after the move (such as with `println!("{:?}", v))` causes a compile-time error: `value used after move`. This behavior enforces Rust’s ownership rules, which ensure memory safety without needing a garbage collector.

To sort this mess, you can clone or reference when needed.

```
let v = vec![1, 2, 3];
let cloned = v.clone();
println!("{:?}", v); // ✅ OK
```

This creates vector `v` with the values `[1, 2, 3]`, then creates a deep copy of it using `v.clone()`, storing the copy in `cloned`. Unlike a move, cloning explicitly duplicates the data in memory, so both `v` and `cloned` own separate copies of the same values. This allows `v` to remain valid and accessible after the cloning operation, so calling `println!("{:?}", v)` works without error.

Cloning is useful when you need to preserve the original data while also passing or storing a copy elsewhere, though it can be more costly in terms of performance compared to moving.

### 2. Cloning Everything to Fix Ownership

```
fn print_length(v: Vec<i32>) {
println!("{}", v.len());
}

let v = vec![1, 2, 3];
// print_length(v.clone()); // ❌ Unnecessary clone
```

This code defines a function `print_length` that takes ownership of a `Vec<i32>` and prints its length. When calling `print_length(v.clone())`, it creates a full copy of the vector just to pass it to the function, which is often unnecessary and inefficient.

Instead, since `print_length` only needs to read the length and not modify or keep the vector, it would be better to change its parameter to take a reference (`&Vec<i32>`) so that the original vector can be borrowed without cloning.

Cloning here is an unnecessary performance cost because Rust allows safe, non-owning references that avoid duplicating data when only read access is needed.

To fix this, use borrowing.

```
fn print_length(v: &Vec<i32>) {
println!("{}", v.len());
}
print_length(&v); // ✅ OK
```

This defines a function `print_length` that takes an immutable reference to a `Vec<i32>` instead of taking ownership. When calling `print_length(&v)`, the vector `v` is borrowed, not moved, allowing the function to read its length without taking ownership. This means `v` remains usable after the function call, and no data is cloned or copied, making it both efficient and safe.

Using references like this is idiomatic in Rust when you only need to read from a value, as it avoids unnecessary memory allocation and preserves ownership.

### 3. Misunderstanding Lifetimes

```
fn get_str<'a>() -> &'a str {
let s = String::from("hello");
&s // ❌ Error: returns reference to local variable
}
```

This reference returned points to `s`, which is dropped when the function ends, so the reference is invalid.

There are two options to fix this. The first is to return an owned string.

```
fn get_str() -> String {
String::from("hello")
}
```

Or you can accept an input reference and return a reference tied to the input.

```
fn get_str<'a>(input: &'a str) -> &'a str {
input
}
```

### 4. Shadowing Confusion

```
let x = 5;
let x = x + 1;
println!("{}", x); // prints 6
```

Variable shadowing is allowed and common in Rust. Beginners might be confused if they expect reassignment but don’t realize shadowing creates a new variable.

This is not necessarily an error, but be mindful that shadowing creates a new variable and can be used intentionally.

### 5. Using `&String` Instead of `&str`

```
fn print_str(s: &str) {
println!("{}", s);
}

let s = String::from("hello");
print_str(&s); // works fine

// But...

fn print_string(s: &String) {
println!("{}", s);
}

print_string(&s); // valid but less flexible
```

Using `&str` is more flexible than `&String`. Use `&str` for function parameters unless you need ownership or specific `String` methods.

### 6. Using `for` Loop Without `mut` When Needed

```
let mut v = vec![1, 2, 3];
for x in v {
x += 1; // ❌ Error: cannot assign to `x` because it is not mutable
}
```

In the above code, the loop variable `x` is immutable by default.

To fix this, use the `mut` keyword to make `x` a mutable reference.

```
let mut v = vec![1, 2, 3];
for x in &mut v {
*x += 1; // works because x is a mutable reference
}
```

### 7. Not Importing Traits for Methods

```
fn main() {
let v = vec![3, 1, 2];
v.sort(); // ❌ Error: cannot borrow immutable local variable `v` as mutable
}
```

Some methods require trait imports. For example, `.sort()` requires the vector to be mutable and in scope.

```
let mut v = vec![3, 2, 1];
v.sort(); // works fine on mutable vector
```

### 8. Forgetting to Use `mut` When Modifying Variables

```
let x = 5;
x = 6; // ❌ Error: cannot assign twice to immutable variable
```

Variables are immutable by default in Rust. However, the `mut` keyword lets you modify variables.

```
let mut x = 5;
x = 6; // works fine
```

### 9. Not Handling Errors with `Result`

```
use std::fs::File;

fn main() {
let f = File::open("hello.txt"); // ❌ warning: unused Result
}
```

`File::open` returns a `Result`. Ignoring it can hide errors and will cause compiler warnings.

Fix the above issue with:

```
use std::fs::File;

fn main() {
let f = match File::open("hello.txt") {
Ok(file) => file,
Err(e) => panic!("Error opening file: {}", e),
};
}
```

This code attempts to open a file named `hello.txt` using `File::open`, which returns a `Result` type indicating success (`Ok`) or failure (`Err`). It uses a `match` expression to handle both cases: If the file is successfully opened, the file handle is stored in the variable `f`; if an error occurs (e.g., the file doesn’t exist), the program immediately calls `panic!`, which crashes the program and prints the error message.

This approach is useful for basic error handling, especially when file access is critical and the program cannot proceed without it. However, in production code, more graceful error handling, like logging or fallback behavior, is often preferred over panicking.

### 10. Using `.expect()` Without a Helpful Message

```
let v: Vec<i32> = Vec::new();
println!("{}", v[0]); // panics at runtime

v.get(0).expect("Oops"); // panics with generic message
```

Using `.expect()` without descriptive messages makes debugging harder.

```
v.get(0).expect("Index 0 should exist in vector");
```

### 11. Using `.iter()` When `.into_iter()` or `.iter_mut()` Is Needed

```
let mut v = vec![1, 2, 3];
for x in v.iter() {
*x += 1; // ❌ error: cannot assign to `*x`
}
```

The above code causes an error because `.iter()` gives immutable references. Use `.iter_mut()` to solve this error.

```
for x in v.iter_mut() {
*x += 1;
}
```

## How to Improve Your Rust Skills

Each of these mistakes, from borrowing issues to lifetime confusion, shows how Rust forces you to think deeply about memory, ownership and correctness. This thinking pays off with software that’s safer, faster and more maintainable. While it can be frustrating at first, every compile-time error you encounter is a chance to write better, more reliable code.

To keep getting better:

* **Read compiler errors thoroughly.**: Rust’s compiler is famously helpful. Take the time to read the suggestions it gives, as they often point you directly to the solution.
* **Use tools like `clippy` and `rust-analyzer`.** These tools can help you catch subtle mistakes and improve your code style.
* **Learn from the community.** The Rust community is welcoming and full of great learning resources. Read blogs, follow discussions on the [Rust Users Forum](http://users.rust-lang.org/) or ask for help on the Rust Discord.
* **Build projects.** The best way to internalize Rust’s principles is by building real projects. Start small, and gradually increase complexity.
* **Contribute to open source**. Reading and contributing to open source Rust projects help you see how experienced developers structure and write idiomatic Rust code.

Deep-dive further into Rust. Read Andela’s guide and discover how to [Dockerize a Rust Application with AWS ECR and GitHub Actions](https://www.andela.com/blog-posts/dockerize-a-rust-application-with-aws-ecr-and-github-actions/?utm_medium=contentmarketing&utm_source=&utm_campaign=brand-global-the-new-stack&utm_content=rust-docker&utm_term=writers-room).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/05/9b23d2ba-cropped-9585988f-zzwia-raymond.jpeg)

Zziwa Raymond Ian is a full-stack engineer and a member of the Andela Talent Network, a private global marketplace for digital talent. Specializing in Next.js, React, JavaScript, TypeScript, NestJs and others, he has developed a deep holistic understanding of both...

Read more from Zziwa Raymond Ian](https://thenewstack.io/author/zziwa-raymond/)