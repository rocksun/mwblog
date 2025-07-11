Known as the go-to language for tasks like data processing and analyzing large datasets, it is no surprise [Python](https://thenewstack.io/python/) offers multiple ways to iterate through datasets of all sizes.

Iteration is the process of repeating an action for each item in a collection, one at a time. In programming, it usually means going through a list, string or other group of values step by step. You “visit” each item, often to read it, change it or perform some action with it. Think of iteration like folding laundry. You take out one item, fold it, then move on to the next until the basket is empty.

Two common ways to iterate over data in Python are [`for`](https://thenewstack.io/how-to-use-loops-in-python/) [loops](https://thenewstack.io/how-to-use-loops-in-python/) and looping with indexing. `for` loops process each item in a sequence, one by one. Use a loop in combination with [Python’s indexing system](https://thenewstack.io/how-to-use-the-python-slice-function/) to access both the position and the value of each element.

Both approaches can get you to the same result in many cases. But the reasons you might choose one over the other, as well as how they operate under the hood and impact application performance at scale, are quite different.

## What Is Python Indexing in a Loop?

Looping with indexing is a way to iterate through a sequence (like a [list, tuple or string](https://thenewstack.io/write-better-python-with-list-comprehensions/)) by looping over its indexes, then using those indexes to access each element. This method combines the structure of a for loop with the precision of Python’s indexing system, which starts counting at 0.

### When To Use Indexing in a Loop

* You need both the position and value of each element.
* You plan to modify elements in place, such as updating values by index.
* You work with multiple sequences and need to synchronize them by position.
* You want explicit control over which elements to access and how.

### Python Indexing in a Loop: Basic Syntax

```
for i in range(len(sequence)):
    # Access each element with sequence[i]
    # Perform actions using i or sequence[i]
```

### Python Looping With Indexing Example

```
data = [4, 7, 9, 1, 5]


for i in range(len(data)):
    print(data[i])
```

Output:

4

7

9

1

5

### What Is a Python `for` Loop?

A `for` loop iterates directly over the elements of a sequence, executing a block of code for each item without explicitly using their indexes. This approach is simpler and more readable, especially when you do not need the position of each element or to modify the sequence.

### When To Use a `for` Loop

* You just need to read or process each item.
* You don’t need to modify the original list.
* You don’t care about the index of each item.

### Python `for` Loop: Basic Syntax

```
for element in sequence:
    # Perform actions using element
```

### Example of `for` Loop

```
data = [4, 7, 9, 1, 5]


for item in data:
    print(item)
```

### Capability: Indexing vs. `for` Loops

While both loops can perform similar tasks, indexing offers more native capabilities. For example, to double every number in a list, you can easily do this with indexing in a loop:

```
data = [4, 7, 9, 1, 5]


for i in range(len(data)):
    data[i] = data[i] * 2  # Modify the list element by index


print(data)
```

Output:

[8, 14, 18, 2, 10]

Trying the same thing with a `for` loop will yield a different result.

```
data = [4, 7, 9, 1, 5]


for item in data:
    item = item * 2  # Only changes the loop variable, NOT the list element


print(data)
```

Output:

[4, 7, 9, 1, 5]

Why the difference in results? When using the syntax `for item in data`, `item` is a temporary copy of each element’s value, whereas the index points to the actual value itself. Changing `item` inside the loop does not affect the original list. Indexing in a loop, however, accesses the actual elements by their index, so assigning to `data[i]` modifies the original list directly.

### Speed and Performance: Indexing vs. `for` Loops in Python

Capabilities are not the only difference between indexing and `for` loops. Their performance characteristics differ as well. Both allow you to iterate over data, but how they access elements internally affects speed (and memory).

## Benchmarking Methods

Let us put this to the test using Python’s `time` module and a function that measures how long a function takes to run.

```
import time


def time_function(func):
    start = time.time()
    func()
    return time.time() - start
```

### Example 1: Small Dataset Comparison

```
data = list(range(1000))


def with_indexing():
    for i in range(len(data)):
        _ = data[i] * 2


def with_for_loop():
    for item in data:
        _ = item * 2


print("Indexing:", time_function(with_indexing))
print("For loop:", time_function(with_for_loop))
```

Output:

Indexing: 0.00013685226440429688

`for` loop: 7.009506225585938e-05

It looks like both the `for` loop and indexing are performing the same functionality in this example, so why is one faster? Because though they may look similar, under the hood, they perform differently.

* `with_indexing()` loops over a range of indices, accessing each element by index (`data[i]`).
* `with_for_loop()` loops directly over each item in the list without calculating indexes.

The `for` loop skips the overhead of generating index numbers and performing indexing lookups. This reduces computation by a small amount, which matters over many iterations.

### Example 2: Large Dataset Comparison

```
data = list(range(10_000_000))


def with_indexing_large():
    for i in range(len(data)):
        _ = data[i] * 2


def with_for_loop_large():
    for item in data:
        _ = item * 2


print("Indexing (large):", time_function(with_indexing_large))
print("For loop (large):", time_function(with_for_loop_large))
```

Output:

Indexing (large): 0.8469340801239014

`for` loop (large): 0.405224084854126

Again, the `for` loop outperforms indexing. The cost of calculating indices and performing lookups in every iteration adds up. The `for` loop avoids this by using an internal iterator that:

* Does not compute index positions.
* Does not repeatedly look up values with bracket notation.
* Has lower CPU and memory overhead.

### Why Are `for` Loops Faster?

Indexing explicitly references positions (`data[i]`). While list indexing is a constant-time operation (O(1)), each iteration involves calculating the index and performing a lookup, adding overhead.

`for` loops use Python’s internal iterator protocol to fetch elements directly without index calculation. This streamlined process reduces overhead, making `for` loops faster, especially on large datasets.

In practice, `for` loops are more efficient for simple iteration, while indexing provides more control but with a slight performance cost.

## Factors Influencing Speed: Indexing vs. `for` Loops

Several factors affect the speed difference between indexing and `for` loops.

* Python implementation: Different interpreters like [CPython](https://thenewstack.io/python-under-the-hood/) and [PyPy](https://thenewstack.io/python-3-13-blazing-new-trails-in-performance-and-scale/) handle loops differently. PyPy’s JIT compiler may optimize indexing better than CPython, affecting results.
* Data types: Lists and tuples work well with both methods. However, for [Numpy](https://thenewstack.io/what-is-the-numpy-python-library-and-how-do-you-use-it/) arrays, vectorized operations usually outperform loops regardless of style.
* Dataset size: Indexing overhead grows with larger datasets, making `for` loops generally faster. For small datasets, the difference is minor.
* Operation complexity: Simple tasks highlight iteration overhead. Complex operations or I/O may mask differences.

## Common Mistakes and Misconceptions

* Using indexing when not needed: This increases code complexity and can reduce performance due to index management overhead. Use simple `for` loops if you do not need element positions.
* Assuming indexing is always faster: As we can see, it’s not. `for` loops often perform better by avoiding repeated index calculations and are usually more readable.
* Modifying lists during iteration: Changing a list while iterating can cause bugs such as skipped elements or errors. Use copies, careful indexing or build new lists to avoid problems.

## Summary of Findings

`for` loops are generally more efficient and more readable for simple iteration when you only need to process each item. Their clarity reduces bugs and improves maintainability.

Indexing with looping is useful when you need element positions or must modify items in place. This control comes at some cost in readability and sometimes performance.

As datasets grow large, performance differences between these methods become significant. Choosing the right approach can impact speed and resource use.

## Next Steps for Python Developers

To make informed performance decisions in your own projects, use profiling tools like `cProfile` or `timeit` to measure how your code behaves in real-world scenarios. This helps you identify specific bottlenecks rather than relying on general assumptions. Explore libraries such as NumPy or Pandas, which offer optimized, vectorized alternatives to manual loops for data processing.

As you write Python code, favor the more readable and Pythonic approach of direct iteration using for `item in iterable` whenever possible. This practice reduces bugs, improves clarity and often enhances performance. By understanding the trade-offs between different looping techniques and applying best practices, you’ll be better equipped to build efficient, maintainable Python applications.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)