[Java 22 introduces stream gatherers](https://www.infoworld.com/article/3709529/possible-java-streams-enhancement.html), a new mechanism for manipulating streams of data. Stream gatherers are the delivered feature for [JEP 461](https://openjdk.org/jeps/461), allowing developers to create custom intermediate operators that simplify complex operations. At first glance, stream gatherers seem a bit complex and obscure, and you might wonder why you'd need them. But when you are confronted with a situation that requires a certain kind of stream manipulation, gatherers become an obvious and welcome addition to the Stream API.
## The Stream API and stream gatherers
Java streams model dynamic collections of elements. As [the spec](https://openjdk.org/jeps/461) says, “A stream is a lazily computed, potentially unbounded sequence of values.”

That means you can consume and operate on data streams endlessly. Think of it as sitting beside a river and watching the water flow past. You would never think to wait for the river to end. With streams, you just start working with the river and everything it contains. When you are done, you walk away.

The [Stream API](https://docs.oracle.com/javase/8/docs/api/java/util/stream/Stream.html) has several built-in methods for working on the elements in a sequence of values. These are the [functional](https://www.infoworld.com/article/3613715/what-is-functional-programming-a-practical-guide.html) operators like `filter`
and `map`
.

In the Stream API, streams begin with a source of events, and operations like `filter`
and `map`
are known as “intermediate” operations. Each intermediate operation returns the stream, so you can compose them together. But with the Stream API, Java will not start applying any of these operations until the stream reaches a “terminal” operation. This supports efficient processing even with many operators chained together.

Stream's built-in intermediate operators are powerful, but they can’t cover the whole realm of imaginable requirements. For situations that are out of the box, we need a way to define custom operations. Gatherers give us that way.

## What you can do with stream gatherers
Say you are on the side of the river and leaves are floating past with numbers written on them. If you want to do something simple, like create an array of all the even numbers you see, you can use the built-in `filter`
method:

```
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6);
numbers.stream().filter(number -> number % 2 == 0).toArray()
// result: { 2, 4, 6 }
```
In the above example, we start with an array of integers (the source) and then turn it into a stream, applying a filter that only returns those numbers whose division by two leaves no remainder. The `toArray()`
call is the terminal call. This is equivalent to checking each leaf for evenness and setting it aside if it passes.

## Stream Gatherers' built-in methods
The [java.util.stream.Gatherers](https://docs.oracle.com/en%2Fjava%2Fjavase%2F22%2Fdocs%2Fapi%2F%2F/java.base/java/util/stream/Gatherers.html) interface comes with a handful of built-in functions that enable you to build custom intermediate operations. Let's take a look at what each one does.

### The windowFixed method
What if you wanted to take all the leaves floating by and collect them into buckets of two? This is [surprisingly clunky](https://blog.payara.fish/introducing-stream-gatherers-jep-461-for-enhanced-java-stream-operations) to do with built-in functional operators. It requires transforming an array of single digits into an array of arrays.

The `windowFixed`
method is a simpler way to gather your leaves into buckets:

```
Stream.iterate(0, i -> i + 1)
.gather(Gatherers.windowFixed(2))
.limit(5)
.collect(Collectors.toList());
```
This says: Give me a stream based on the iterating of integers by 1. Turn every two elements into a new array. Do it five times. Finally, turn the stream into a `List`
. The result is:

```
[[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
```
Windowing is like moving a frame over the stream; it lets you take snapshots.

### The windowSliding method
Another windowing function is [windowSliding](https://docs.oracle.com/en%2Fjava%2Fjavase%2F22%2Fdocs%2Fapi%2F%2F/java.base/java/util/stream/Gatherers.html#windowSliding(int)), which works like `windowFixed()`
except each window starts on the next element in the source array, rather than at the end of the last window. Here's an example:

```
Stream.iterate(0, i -> i + 1)
.gather(Gatherers.windowSliding(2))
.limit(5)
.collect(Collectors.toList());
```
The output is:

```
[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
```
Compare the `windowSliding`
output with the output of `windowFixed`
and you’ll see the difference. Each subarray in `windowSliding`
contains the last element of the previous subarray, unlike `windowFixed`
.

### The Gatherers.fold method
`Gatherers.fold`
is like a refined version of the [Stream.reduce](https://docs.oracle.com/javase/8/docs/api/java/util/stream/Stream.html#reduce-java.util.function.BinaryOperator-) method. It’s a bit nuanced to see where `fold()`
comes in handy over `reduce()`
. A good discussion is found in [this article](https://cr.openjdk.org/~vklang/Gatherers.html). Here's what the author, Viktor Klang, has to say about the differences between `fold`
and `reduce`
:
Folding is a generalization of reduction. With reduction, the result type is the same as the element type, the combiner is associative, and the initial value is an identity for the combiner. For a fold, these conditions are not required, though we give up parallelizability.

So we see that `reduce`
is a kind of `fold`
. Reduction takes a stream and turns it into a single value. Folding also does this, but it loosens the requirements: 1) that the return type is of the same type as the stream elements; 2) that the combiner is associative; and 3) that the initializer on `fold`
is an actual generator function, not a static value.

The second requirement is relevant to parallelization, which I'll discuss in more detail soon. Calling `Stream.parallel`
on a stream means the engine can break out the work into multiple threads. This only works if the operator is associative; that is, it works if the ordering of operations does not affect the outcome.

Here’s a simple use of `fold`
:

```
Stream.of("hello","world","how","are","you?")
.gather(
Gatherers.fold(() -> "",
(acc, element) -> acc.isEmpty() ? element : acc + "," + element
)
)
.findFirst()
.get();
```
This example takes the collection of strings and combines them with commas. The same work done by `reduce`
:

```
String result = Stream.of("hello", "world", "how", "are", "you?")
.reduce("", (acc, element) -> acc.isEmpty() ? element : acc + "," + element);
```
You can see that with `fold`
, you define a function (`() -> “”`
) instead of an initial value (`“”`
). This means if you require more complex handling of the initiator, you can use the `closure`
function.

Now let’s think about the advantages of `fold`
with respect to a diversity of types. Say we have a stream of mixed-object types and we want to count occurrences:

```
var result = Stream.of(1,"hello", true).gather(Gatherers.fold(() -> 0, (acc, el) -> acc + 1));
// result.findFirst().get() = 3
```
The `result var`
is 3. Notice the stream has a number, a string, and a Boolean. Performing a similar feat with `reduce`
is difficult because the accumulator argument (`acc`
) is strongly typed:

```
// bad, throws exception:
var result = Stream.of(1, "hello", true).reduce(0, (acc, el) -> acc + 1);
// Error: bad operand types for binary operator '+'
```
We could use a `collector`
to perform this work:

```
var result2 = Stream.of("apple", "banana", "apple", "orange")
.collect(Collectors.toMap(word -> word, word -> 1, Integer::sum, HashMap::new));
```
But then we’ve lost access to the initializer and folding functions body if we need more involved logic.

### The Gatherers.scan method
[Scan](https://docs.oracle.com/en/java/javase/22/docs/api/java.base/java/util/stream/Gatherers.html#scan(java.util.function.Supplier,java.util.function.BiFunction)) is something like `windowFixed`
but it accumulates the elements into a single element instead of an array. Again, an example gives more clarity (this example is from [the Javadocs](https://docs.oracle.com/en/java/javase/22/docs/api/java.base/java/util/stream/Gatherers.html#scan(java.util.function.Supplier,java.util.function.BiFunction))):
```
Stream.of(1,2,3,4,5,6,7,8,9)
.gather(
Gatherers.scan(() -> "", (string, number) -> string + number)
)
.toList();
```
The output is:

```
["1", "12", "123", "1234", "12345", "123456", "1234567", "12345678", "123456789"]
```
So, `scan`
lets us move through the stream elements and combine them cumulatively.

### The mapConcurrent method
With [mapConcurrent](https://docs.oracle.com/en/java/javase/22/docs/api/java.base/java/util/stream/Gatherers.html#mapConcurrent(int,java.util.function.Function)), you can specify a maximum number of threads to use concurrently in running the `map`
function provided. Virtual threads will be used. Here’s a simple example that limits the concurrency to four threads while squaring numbers (note that `mapConcurrent`
is overkill for such a simple dataset):

```
Stream.of(1,2,3,4,5).gather(Gatherers.mapConcurrent(4, x -> x * x)).collect(Collectors.toList());
// Result: [1, 4, 9, 16, 25]
```
Besides the thread max, `mapConcurrent`
works exactly like the standard `map`
function.

## Conclusion
Until stream gatherers are promoted as a feature, you still need to use the `--enable-preview`
flag to access the `Gatherer`
interface and its features. An easy way to experiment is using JShell: `$ jshell --enable-preview`
.

Although they are not a daily need, stream gatherers fill in some long-standing gaps in the Stream API and make it easier for developers to extend and customize functional Java programs.