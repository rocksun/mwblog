# Golang: How to Write a For Loop
![Featued image for: Golang: How to Write a For Loop](https://cdn.thenewstack.io/media/2022/05/57bb2a1f-golang.png)
Programming
[Loops](https://thenewstack.io/how-to-use-loops-in-python/): You know them, you love them. Either that or you don’t know them and you’re unsure just how important they are to nearly all programming languages. [Golang](https://thenewstack.io/golang-co-creator-rob-pike-what-go-got-right-and-wrong/) is no exception and uses the for loop to repeat a block of code until a given condition is met. The for loop is actually the most basic type of loop in Go but it’s one you’ll use quite often.
The reasons you might make use of a
[for loop](https://thenewstack.io/golang-1-22-redefines-the-for-loop-for-easier-concurrency/) are varied (depending on your needs). For example, you might want to print out a statement multiple times. Instead of writing the same *fmt.print()* statement over and over, you could use a for loop to take care of the process.
A for loop consists of the following bits:
- The initialization – initializes or declares variables.
- The condition – what is used to evaluate the condition. As long as the condition remains true, the loop is executed.
- The update – updates the value of the initialization each time the loop executes.
- Statement(s) – what is executed
The basic syntax of the for loop looks like this:
|
1
2
3
|
for initialization; condition; update {
statement(s)
}
Remember our printing example above? Let’s say we want to print out New Stack Rocks 10 times. Yes, we could write a Go program that would simply use the
*fmt.Println()* function 10 times like this:
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
|
package main
import "fmt"
func main() {
fmt.Println("New Stack Rocks")
fmt.Println("New Stack Rocks")
fmt.Println("New Stack Rocks")
fmt.Println("New Stack Rocks")
fmt.Println("New Stack Rocks")
fmt.Println("New Stack Rocks")
fmt.Println("New Stack Rocks")
fmt.Println("New Stack Rocks")
fmt.Println("New Stack Rocks")
fmt.Println("New Stack Rocks")
}
If you ran the above code, it would, in fact, print out the following:
*New Stack Rocks*
*New Stack Rocks*
*New Stack Rocks*
*New Stack Rocks*
*New Stack Rocks*
*New Stack Rocks*
*New Stack Rocks*
*New Stack Rocks*
*New Stack Rocks*
*New Stack Rocks*
Of course, you don’t want to do things that way. Not only is it inefficient, but it’s also a great way to introduce errors and it’s not very effective. Instead, we’ll do that same thing with a for loop like so:
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
|
package main
import "fmt"
func main() {
for i := 1; i <= 10; i++ {
fmt.Println("New Stack Rocks")
}
}
You already know that we call the main package and import fmt with the first two lines. The next line
*func main()* initializes the main package. Our for loop is then created with the following: *i := 1 – the initialization that sets i to 1.* *i <= 10 – the condition that says as long as i is less than or equal to 10, continue.* *i++ – the update that adds 1 to the previous value of I.* *fmt.Println(“New Stack Rocks”) – our print statement that is executed so long as i <= 10.*
Along those same lines, you could even create an infinite loop. Why would you want to use an infinite loop? They actually have their purposes. For example, you might want to write application code that has to keep running until it is stopped, such as a web server or an application that requires continuous user input until the application is manually stopped.
An infinite loop can be accomplished with a for loop minus the condition statement. So, a for loop might look something like this:
|
1
2
3
|
for {
fmt.Println("New Stack Rocks")
}
The entire application could look like this:
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
import "fmt"
func main() {
for {
fmt.Println("New Stack Rocks")
}
}
If you run the above code, it will continue printing out New Stack Rocks, until you kill it with something like the Ctrl+C keyboard shortcut.
There’s another really cool trick with the for loop which includes the range keyword. The range keyword is used to iterate over elements within a data structure. Range can be used with arrays, slices, strings, maps, and channels. Let me show you an example of using the range keyword on a for loop iterating over a string.
The for loop with the range keyword will look something like this:
|
1
2
|
for i, ch := range "New Stack Rocks" {
fmt.Printf("%#U starts a position %d\n", ch, i)
What this for loop does is iterate through the string and prints out the letter and position until it completes. The full code looks like this:
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
import "fmt"
func main() {
for i, ch := range "New Stack Rocks" {
fmt.Printf("%#U starts a position %d\n", ch, i)
}
}
If you run this, the output would be:
*U+004E ‘N’ starts a position 0*
*U+0065 ‘e’ starts a position 1*
*U+0077 ‘w’ starts a position 2*
*U+0020 ‘ ‘ starts a position 3*
*U+0053 ‘S’ starts a position 4*
*U+0074 ‘t’ starts a position 5*
*U+0061 ‘a’ starts a position 6*
*U+0063 ‘c’ starts a position 7*
*U+006B ‘k’ starts a position 8*
*U+0020 ‘ ‘ starts a position 9*
*U+0052 ‘R’ starts a position 10*
*U+006F ‘o’ starts a position 11*
*U+0063 ‘c’ starts a position 12*
*U+006B ‘k’ starts a position 13*
*U+0073 ‘s’ starts a position 14*
Notice we use
*fmt.Printf()* instead of *fmt.Println()*. The reason for this is Printf allows you to format numbers, variables, and strings, whereas Println simply prints the line as is. If you used *fmt.Println* instead, the output would be: *%#U starts a position %d 78 0*
Clearly, that’s not correct, so we have to use
*fmt.Printf()* instead.
And that is how you write a for loop in your favorite new language. Now you’ve seen how it works, are you ready to take it to the next level? If so, ready, set, Go!
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)