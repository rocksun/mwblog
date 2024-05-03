# Golang: How To Use the Go Install Command
![Featued image for: Golang: How To Use the Go Install Command](https://cdn.thenewstack.io/media/2024/05/9e40387e-monitor-1307227_1280-1-1024x722.jpg)
The
[Go language](https://thenewstack.io/golang-co-creator-rob-pike-what-go-got-right-and-wrong/) has a special command that is used to compile and install a binary package for your application into a path that is accessible to your application’s user.
Let me explain it in a way we can all understand.
First, let’s talk about the PATH. A PATH is a special list of directories that instructs the system where to find the necessary executable files to run commands. For instance: With Linux, run the command…
|
1
|
echo $PATH
You’ll probably see something like this in the output:
|
1
|
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
Essentially, what that means is any executable file in any of those directories can be run from anywhere in the filesystem hierarchy. Thanks to the PATH, you don’t have to use the full path to commands like ls, which would be:
|
1
|
/usr/bin/ls
Instead, you can simply run ls to use the application.
When you install Go, it assumes the path for Go defaults to a particular location. To find out where that path is, issue the command:
|
1
|
echo $GOPATH
You should see something like this:
|
1
|
/home/jack/go/
You can set this path with the command:
|
1
|
go env -w GOPATH=$HOME/go
Note that
* $HOME* is the equivalent of */home/USER* (Where *USER* is your Linux username). You can also set this in your * .bash_profile* file. Open that file for editing with the command:
|
1
|
nano ~/.bash_profile
At the bottom of that file, add the following:
|
1
|
export GOPATH=$HOME/go
Source the file with:
|
1
|
source ~/.bash_profile
You could change that path if you wanted to, but it’s always best (especially at first), to leave it as is.
Okay, now that you understand what GOPATH is, how is it used?
Let me show you.
Let’s write a program that will calculate the approximate value of Pi. Here’s how this application works:
- Imports the packages
[fmt](https://pkg.go.dev/fmt), [math](https://pkg.go.dev/math), and [math/rand](https://pkg.go.dev/math/rand#Rand).
- Seeds the random number generator, sets
*totalPoints*to 1 million and *pointsInsideCircle*to 0.
- Uses a for loop to iterate through
*totalPoints*, setting both x and y to random float 64 numbers and uses those numbers (with the *math.Sqrt*function) to multiple x*x and y*y.
- Sets
*piApprox*to 4 times float64 of *pointsInsideCircle*and *totalPoints*.
- Finally, prints out the value.
Here’s what the code looks like:
Create a new project directory with the following:
|
1
|
mkdir ~/randompi
Change into that directory with the following:
|
1
|
cd randompi
Initialize the project with:
|
1
|
go mod init randompi
Create the
* main.go* file with:
|
1
|
nano main.go
Paste the code into that file and save it.
Build the application with the command:
|
1
|
go build
What you should now see is a binary executable called
*randompi*. You can run the new Go app with the command:
|
1
|
./randompi
That’s great. But what if you wanted to be able to run that command from other directories? Since this is Linux, you could copy that to the
*/usr/local/bin* directory but Go already has its GOPATH available for that very purpose. For this, you use go install, which moves that new binary file to your GOPATH. To do that, issue the command:
|
1
|
go install
If you issue the ls command, you’ll find that
*randompi* executable is now gone. Where did it go? Go moved it into your GOPATH. Remember to list your GOPATH with:
|
1
|
echo $GOPATH
That should print out your GOPATH. The trick here is that Go doesn’t just copy the executable to the root of your GOPATH. Instead, it copies it to the bin directory within that path. In Linux terms, bin is a common directory for binary files (bin = binary). To verify the executable was copied into that path, issue the command:
|
1
|
ls $GOPATH/bin
You should see
* randompi* listed.
If you
[know Linux](https://thenewstack.io/tns-linux-sb00-1-intro-to-the-linux-skill-blocks-repository/), you probably understand what’s coming next. Even though you’ve set GOPATH, that doesn’t mean it’s in your Linux PATH. Even with that caveat, Go has you covered with the run command. If you issue the command:
|
1
|
go run randompi
It will find the binary executable in $GOPATH/bin and run the
* randompi* application for which the output will be something like:
Using this method, our approximate value of π: 3.139740
Here’s a handy trick.
When you initialized the application with
*go mod init randompi*, it creates the ** go.mod** file which will include something like this:
|
1
2
3
|
module randompi
go 1.22.1
Say you want to rename the app to something like gopi. All you have to do is edit the go.mod file and change the module randompi to module gopi. Rebuild and reinstall the app and you can then run your app with:
|
1
|
go run gopi
And that, my
[ Go friends](https://thenewstack.io/how-golang-evolves-without-breaking-programs/) is the basics for using the go install command. This will become an important tool for you as you continue your education in the [Go language](https://thenewstack.io/golang-variables-and-data-types-an-introduction/). [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)