# Golang Variables and Data Types: An Introduction
![Featued image for: Golang Variables and Data Types: An Introduction](https://cdn.thenewstack.io/media/2024/04/786e8015-cat-7928232_1280-1024x703.png)
Now that you’ve got
[ a taste](https://thenewstack.io/learn-the-go-programming-language-start-here/) of how the [Go language works](https://thenewstack.io/import-and-use-a-third-party-package-in-golang/), it’s time we take a step back and talk about variables and data types. If you’ve ever worked with any [other programming language](https://thenewstack.io/best-practices-for-naming-variables-what-the-research-shows/), you should already be [familiar with these concepts](https://thenewstack.io/python-for-beginners-data-types/). However, if [Go](https://thenewstack.io/golang-co-creator-rob-pike-what-go-got-right-and-wrong/) is your first language, it’s important that you understand the purpose of both variables and data types and how they function.
Without this understanding of variables and data types, you’ll struggle to get up to speed with Go (or any language for that matter). But don’t worry, neither variables nor data types are complex concepts. In fact, variables are quite simple. As far as data types are concerned, you just have to know the types and how they work.
## Variables
A typical variable works in key-value pairs like this:
key = value
Pretty straightforward.
In Go you can declare a variable, define its data type, and then give it a value. The syntax looks like this:
|
1
|
var variableName dataType
We declare the variable with var give the variable a name with
*variableName* and define the data type with *dataType*. Let’s say we’re creating a variable for first names
|
1
|
var fname string
What we’ve done is declare a variable named
*fname* (for first name) as a string. We use string because the first name will be comprised of characters a/A-z/Z (more on data types in a bit).
We can also initialize that variable (if we so choose) with a value in the same line like this:
|
1
|
var fname string = New
Let’s use that in a block of code along with a variable for last name as well. Remember (from our previous tutorials) we have to call the main package with:
|
1
|
package main
Next, we have to import “fmt” from main with the line:
|
1
|
import ("fmt")
Now, we’ll create a function that defines our variables and prints the first and last name. The function looks like this:
|
1
2
3
4
5
|
func main() {
var fname string = "New"
var lname string = "Stack"
fmt.Println(fname,lname)
}
Our entire app (named vars.go) looks like this:
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
|
package main
import ("fmt")
func main() {
var fname string = "New"
var lname string = "Stack"
fmt.Println(fname,lname)
}
We run the app with:
|
1
|
go run vars.go
The output would be:
|
1
|
New Stack
Simple and effective.
But how do you initialize a variable with data inputted from the user? Now that’s a cool trick. We’ll stick with our example above. For this, we’ use the
*fmt.Scan* function from the main package. The first thing we have to do (after calling both *main* and *fmt*) is declare our variables (inside our function) with:
|
1
2
|
var fname string
var lname string
Next, we write four lines:
- Instruct the user to type their first name.
- Accept input for the first name.
- Instruct the user to type their last name.
- Accept input for the last name.
This section looks like:
Finally, we write a line to print it all out like so:
|
1
|
fmt.Println("Your name is:", fname, lname)
The entire code looks like this:
When you run the app, it will ask for a first name, then a last name, and print out both names.
## Data Types
Go has a number of included data types, which are broken into three categories:
- Basic (bool, int, float64, complex128, string)
- Aggregate (array, slice, struct)
- Reference (pointer, channel, map, interface)
The basic types are obvious and are defined like so:
- var boolean bool = true
- var integer int = 100
- var float float64 = 100.09
- var comp complex128 = 1 + 3i
- var st string = “New Stack”
These break down like so:
- boolean is true/false
- int is a whole number
- float64 is a number with a decimal
- complext128 is the set of all complex numbers with boat float64 and imaginary components
- string is a string of characters
Next, we have the aggregate types, which could be in the following forms:
- someArray := [10]int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
- var slice []int = someArray[0:5]
The struct aggregate type is a bit more complex because it can contain custom fields. You declare a struct like this:
|
1
2
3
4
|
type Box struct {
X int
Y int
}
You could then initialize those values like this:
|
1
|
b := Box{1,2}
Finally, there are the reference types, such as pointers, which contain the memory address of a variable on which they are based. Pointers use the * character like so:
|
1
|
var p *int
We could then declare something like this:
|
1
|
myInteger := 100
We then create the pointer from the variable like this:
We’re going to dive deeper into these concepts later on, but it’s important you understand the basic types included with Go.
Congratulations on taking yet another step with the Go language. It may
[not be as simple as Python](https://thenewstack.io/an-introduction-to-python-for-non-programmers/) but it’s not nearly as complicated as C, C++, or similar programming languages. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)