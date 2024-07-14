# What Is the NumPy Python Library and How Do You Use It?
![Featued image for: What Is the NumPy Python Library and How Do You Use It?](https://cdn.thenewstack.io/media/2024/06/2ed9d903-yunus-tug-uar4s-_zcyg-unsplash-1024x683.jpg)
[NumPy](https://numpy.org/) stands for Numerical Python and is an open source library that has become invaluable to the science and engineering fields. If you need to work with numerical data in [Python](https://thenewstack.io/an-introduction-to-python-a-language-for-the-ages/), NumPy should be your go-to library.
The purpose of NumPy is to work with arrays as well as [linear algebra](https://thenewstack.io/quantum-algorithms-vs-quantum-inspired-algorithms/), Fourier transform, and matrices. But why bother with NumPy when Python already has lists that can serve as an array? In a word… speed. Lists can be slow, especially when you’re dealing with larger lists of data (which is very common in scientific use cases).

Ergo, NumPy.

NumPy is up to 50 times faster than Python lists because it stores arrays in a continuous chunk of memory, which means processes are capable of accessing (and manipulating) that information very quickly. On top of that, NumPy has been optimized to work with modern CPUs, so it not only benefits from memory placement but also the speed of [multicore/thread CPUs](https://thenewstack.io/ai-hardware-software-dilemma/).

Don’t think NumPy is only useful for scientific data, as it can also be used for multi-dimensional containers of generic data. You can even define arbitrary data types so it can integrate with a wide variety of databases.

Now that you have an idea of what NumPy is, let’s see how it’s used.

## What You’ll Need
The only thing you’ll need is an OS with Python and [Pip](https://pypi.org/project/pip/) installed. If you don’t have Pip installed, don’t fret, I’ll show you how. I’ll demonstrate this on Ubuntu Linux, so if you’re using a different operating system, you’ll need to alter the Pip installation command. Once Pip is installed, everything else should be fairly universal.

## Installing Pip
Installing Pip is actually quite simple. Log into your machine and open a terminal window. From the terminal window, issue the command:

*sudo apt-get install python3-pip -y*
For an OS that uses the DNF package manager, that command would be:

*sudo dnf install python3-pip -y*
Now that Pip is installed, it’s time to add NumPy.

## Installing NumPy
You can’t use NumPy until it’s installed. To install it, you’ll use Pip like so:

*pip install numpy*
If you find you cannot install NumPy with Pip (which was the case with Ubuntu 24.04), there’s another method, which shouldn’t fail you. To do that, we go back to the default package manager like this:

*sudo apt-get install python3-numpy -y*
Do note that installing NumPy on Fedora-based Linux distributions worked with the *pip install numpy *command.

One way or another, you should be able to get NumPy installed with either of the above commands.

## Using NumPy
Let’s see how NumPy is used. We first must import the NumPy library, so our application can use it. This is done with:

1 |
import numpy as np |
What we’ve done above is import NumPy and given it an alias (*np*). Next, let’s create an array and assign it to *arr* like so:
1 |
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) |
As you can see, we’re making use of the NumPy *array* function here.
Finally, we print our array with:

1 |
print(arr) |
Create a new file with the command:
1 |
nano nu_array.py |
Paste the entire block of code into that file, which looks like this:
12345 |
import numpy as nparr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])print(arr) |
If you run the above code (with the command *python3 nu_array.py*), the output would be:
1 |
[ 1 2 3 4 5 6 7 8 9 10] |
Pretty straightforward. Let’s get a bit more complex, with the help of the copy argument.
## The Copy Argument
There might be times when you’d want to make a copy of an array. When you do, you’ll use the *copy* argument. Let’s say you have the following array:

1 |
[ 1 2 3 4 5 6 7 8 9 10] |
If you were to use the *copy* argument, it would create an exact copy of that array. This might seem overly simple, but *copy* is a very important function because you want to always make sure you’re copying those arrays in the best way possible.
With the *copy* argument, there’s one primary and two optional parameters, which are:

*original_array*– this is the primary parameter and defines the original array you want to copy.*order*– this is one of the optional parameters and controls the order of how the values within the array are copied.*subok*– this is the other optional parameter and defines if any subclasses will be copied to the output array.
Let’s use *copy*. I’m going to throw in a few curve balls here for you.

First, we’ll import NumPy with:

1 |
import numpy as np |
Next, we create a NumPy array using the *start* and *stop* parameters (which define where the array starts and where it stops) and arrange the array in 2 rows and 3 columns (using *reshape*). Our array looks like this:
1 |
my_array = np.arange(start = 1, stop = 7).reshape(2,3) |
One thing to keep in mind is that using *reshape* defines the number of objects in your array. For example, if you were to use *start =1, stop = 10* and *reshape(2,3)*, you’d receive the error:
ValueError: cannot reshape array of size 9 into shape (2,3)

Why is that? Because 2 rows and 3 columns equal 6 objects. If you were to change the shape to (3,3), you could use *start=1, stop=10.* It’s all in the math.

Let’s print the array (so we know what it looks like so far) with the line:

1 |
print(my_array) |
Our entire app looks like this so far:
12345 |
import numpy as npmy_array = np.arange(start = 1, stop = 7).reshape(2,3)print(my_array) |
The output of the above would be:
*[[1 2 3]*
* [4 5 6]]*
Now, let’s create a copy of our array with:

1 |
copy_array = np.copy(my_array) |
Our entire code looks like this:
12345678 |
import numpy as npmy_array = np.arange(start = 1, stop = 7).reshape(2,3)copy_array = np.copy(my_array)print(my_array)print(copy_array) |
The output would be:
*[[1 2 3]*
* [4 5 6]]*
*[[1 2 3]*
* [4 5 6]]*
The reason why we use copy is because if we simply used something like c*opied_array = my_array*, if we were to change a value in the original array (after we’ve defined the copied array), the value would also be changed in the copy.

Consider this:

123456789101112 |
import numpy as npmy_array = np.arange(start = 1, stop = 7).reshape(2,3)bad_copy = my_arraycopy_array = np.copy(my_array)print(my_array)print(copy_array)my_array[-1,-1] = 100print(my_array)print(bad_copy) |
If you were to run the above, both arrays would print out as:
*[[ 1 2 3]*
* [ 4 5 100]]*
*[[ 1 2 3]*
* [ 4 5 100]]*
The bad copy shouldn’t have changed. That’s why we use *copy*.

And that, my friends, is your introduction to NumPy. Next time around we’ll dig a little deeper because NumPy has a few more tricks up its sleeve.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)