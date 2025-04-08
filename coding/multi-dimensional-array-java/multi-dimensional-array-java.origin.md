# Taking Java Arrays to Another Dimension
![Featued image for: Taking Java Arrays to Another Dimension](https://cdn.thenewstack.io/media/2025/04/65946d37-shine-1200800_1280-1024x682.jpg)
Java, along with many other programming languages, includes the concept of arrays. An array is an object that contains a number of variables. Since an array is itself an object, the variables in an array can also be arrays, which leads us to the idea of multidimensional arrays.

## What Is a Multidimensional Array in Java?
There are several ways of defining and populating multidimensional arrays in Java.

## Declaring a Multidimensional Array
Firstly, you can declare an array variable, for example:

int[][] ai;

int aai[][];

As you can see, the position of the square brackets (used to indicate an array) can be placed after the array type or after the variable name. My preference is to put the brackets after the array type so that all the type information is in one place.

## Mixing Bracket Positions
It is also possible to mix the positioning of these:

int[] ai[];

This is not recommended, as it makes the structure of the array harder to understand at first glance. This example makes that painfully obvious:

int[][] x[][], y[][][], z[];

This is equivalent (but not obviously) to the separate definitions:

int[][][][] x;

int[][][][][] y;

int[][][] z;

In these examples, we are simply declaring variables that can be used to reference an array, but no arrays are being created. Local variables are subject to definite assignment; if you declare a local variable, you must set its value to something. If you use these local variables without assigning them to an array, the compiler will report that x, y and z may not have been initialized.

## Creating a Multidimensional Array
There are two ways we can create a multidimensional array (as there are for single-dimensional arrays).

Firstly, we can use an array initializer. For example:

int[][] aiv = {{1, 2}, {3, 4}, };

Here, we define a two-dimensional array and give the first array the values 1 and 2 and the second array the values 3 and 4. I deliberately included the comma after the second set of braces as this is valid syntax, even though there is no third set of values (this comma is optional). The array’s dimensions are determined by the compiler from the values specified. In this example, a 2×2 array will be created.

The second way is to instantiate an array with explicit dimensions:

int[][] aie = new int[2][2];

Again, we have a 2×2 array, but without putting specific values in it.

## Default Values in Arrays
We must also remember that an array is an object in Java, which is why we use the new operator. Why is this important? As a local variable, we already know that if we don’t assign a value to our array reference, the code won’t compile. Now, we have a reference, but what happens if we try to print out the first element of the first array? Because we have instantiated new array objects, the value of aie[0][0] will be 0 (we’ll see why later). If we had a two-dimensional array of Strings, the value would be null. Even though it is a local variable, the array we instantiate has default values stored in it.

## Understanding Jagged Arrays
One of the key things to understand about multidimensional arrays in Java is that they can be ragged (or jagged, depending on who’s describing them). This differs from languages like C (whose syntax Java is heavily based on), which has rectangular arrays.

Let’s look at what this means to you as a developer.

We’ll reuse one of our earlier examples:

int[][] aiv = {{1, 2}, {3, 4}};

This array is implemented as an array of references to arrays, as shown in the diagram.

In effect, there are three arrays: one to hold the values 1 and 2, one to hold the values 3 and 4, and one to hold the references to those two arrays. Since the array references are independent, we are not required to make them the same size.

We can change the second array to hold three values:

int[][] aiv = {{1, 2}, {3, 4, 5}};

The array storage now looks like this:

If we had a three-dimensional array, each element in the second dimension would become an array reference. For example:

int aiv[][][] = {{{1},{2,3}},{{4,5},{6,7},{8,9}}};

The array storage will look like this:

If we were to print out the value aiv[1][0][1], we would get 5.

## Understanding JVM Bytecodes for Array Creation
If we dig a little deeper and look at how the JVM handles array creation, we find three bytecodes are used, depending on what type of array we have.

## Bytecode for Arrays of Primitives
- To create an array of primitives, the anewarray bytecode is used. This takes an argument that indicates the type of primitive the array will store. Each element of the new array is initialized to the default initial value for the element type of the array type. This is why we don’t get a compiler error when asking for the value in a local variable array of primitives that has not been explicitly initialized.
## Bytecode for Arrays of Objects
[Anewarray](https://asmsupport.github.io/jvmref/ref-anewarray.html)bytecode is used to create a one-dimensional array of object references. This takes an argument that is an index into the run-time constant pool, which defines the type of object the array will hold. This bytecode can also be used to create the first dimension of a multidimensional array. Again, all elements will contain a null unless array initializer code is used.
## Bytecode for Multidimensional Arrays
- The multi-anewarray bytecode can be used to create a multidimensional array of objects. Like anewarray, this uses an index into the run-time constant pool to determine the type of objects the array will hold (or null). In addition, it also has a count for the number of dimensions the array will have and a set of values for the size of each dimension of the array.Note that this bytecode is not used for multidimensional arrays of primitives (since there is no type in the constant pool for these). For those, the array is constructed using a combination of anewarray and newarray.For ragged arrays of objects, multianewarray may be combined with anewarray, or the whole array may be created using anewarray. The javac compiler will determine the most efficient approach.
## Performance Considerations With Multidimensional Arrays
Be careful how you use multidimensional arrays, as simple changes can significantly impact performance. For example, looping through a two-dimensional array:

int[][] aiv = {{1,2,3,4,5},{6,7,8,9,10},{11,12,13,14,15}};

for (int x = 0; x < 3; x++)

for (int y = 0; y < 5; y++)

aiv[x][y] = aiv[x][y] + 1;

for (int y = 0; y < 5; y++)

for (int x = 0; x < 3; x++)

aiv[x][y] = aiv[x][y] + 1;

The first version of the loop will be much more efficient than the second. The reason for this is the structure of a multidimensional array that we saw earlier. The second version keeps switching between array references to access the individual elements, with associated overhead. The first version maintains a reference to an array and loops through all the objects stored in it.

## Benchmarking Performance Differences
I ran a similar benchmark on my MacBook using 2,000 arrays, each with 2,000 elements and repeated the loop a thousand times. The first version of the loop was completed in 620ms and the second in 4,200ms. That’s nearly seven times slower.

## Concluding Thoughts
Multidimensional arrays are a fundamental feature in the Java language and are very useful where the size of dimensions is known at compile time. Hopefully, you now have a better understanding of how they work and how to use them effectively in your code.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)