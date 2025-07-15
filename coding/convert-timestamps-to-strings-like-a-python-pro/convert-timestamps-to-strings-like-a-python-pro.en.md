An easy way to think about [timestamps vs. time strings](https://thenewstack.io/how-to-convert-a-timestamp-to-a-string-in-python/) is that one is machine-readable and the other is human-readable. Computers work best with simple numeric representations, like how they ultimately process everything as 0s and 1s. A timestamp is like that: a clean, efficient number that a program can store, sort and calculate with.

But humans require context, words, formatting and images to understand the world. That’s where [time strings](https://thenewstack.io/pythons-built-in-string-tools-every-developer-needs/) come in. Converting a timestamp into a readable date and time transforms machine code into something we humans can interpret at a glance.

Think of it this way:

The timestamp is for the computer. The time string is for us.

## Understanding Python Timestamps

A timestamp is a floating-point or integer number that represents the time elapsed (counted by seconds) since the [Unix](https://thenewstack.io/fosdem-24-can-the-unix-shell-be-improved-hell-yes/) epoch. Huh? The Unix Epoch took place on January 1, 1970. Back when Unix designers created the system, they needed a single fixed point in time to count from. They also needed a date that wouldn’t conflict with important historical dates and was recent enough to start counting from in modern computing.

### What Is a Timestamp?

Each second that passes since the Unix Epoch adds +1 to the number. January 1, 1970, at 00:00:00 UTC was 0. January 1, 2000, 00:00:00 was 946,684,800. January 1, 2025, at 00:00:00 UTC was 1,735,689,600, meaning 1,735,689,600 seconds had passed since the Unix Epoch.

### Example of a Timestamp in Python

First, we need to import the `time` module, as this is [Python](https://thenewstack.io/python/)’s built-in way to work with dates, times and timestamps. We can use `time.time()` to get the current timestamp.

```
import time


current_timestamp = time.time()
print("Current timestamp:", current_timestamp)
```

The output you’ll see will be the exact number of seconds that have elapsed since January 1, 1970.

## Converting a Timestamp to a Time String in Python

For those of us who aren’t able to reference time using the seconds counter, we have the Python `datetime` module. The `datetime` module turns those seconds into a time format we can understand.

### Using the `datetime` Module

`datetime` is a built-in Python library that provides classes for manipulating dates. By using the `datetime` module, we can use the same starting date of January 1, 1970, but turn the output into dates (calendar dates), time of day, perform time arithmetic, format and parse strings, and (as we saw above) access the timestamp.

### Syntax of `datetime.fromtimestamp()`

`fromtimestamp()` is the class method of the `datetime` class. It’s the method you call to create the `datetime` object from the timestamp.

In the code below, `timestamp` is the variable assigned to the numeric value returned from `time.time()`. The function returns the `datetime` object.

```
from datetime import datetime
import time


timestamp = time.time()


datetime_object = datetime.fromtimestamp(timestamp)


print("Current timestamp:", timestamp)
print("Corresponding datetime:", datetime_object)
```

### Example Conversion With `datetime`

You don’t have to print the full `datetime` object every time. Here’s an example that prints out smaller chunks of information.

```
from datetime import datetime


timestamp = time.time()
datetime_object = datetime.fromtimestamp(timestamp)


print("Year:", datetime_object.year)
print("Month:", datetime_object.month)
print("Day:", datetime_object.day)
print("Hour:", datetime_object.hour)
print("Minute:", datetime_object.minute)
print("Second:", datetime_object.second)
```

## Formatting Time Strings in Python

Why do we want time strings? Pulling the `datetime` object gives you a much more readable result than the timestamp, but we can do better. Formatting time strings allows you to customize the time into a way that’s more readable globally (i.e., different countries format times differently, time zones exist, etc.).

### Using `strftime()` for Formatting

Similarly to `fromtimestamp()`, `strftime()` is a class method from the `datetime` class. `strftime()` lets you create custom date/time string formats.

Here are some formatting codes:

* `%Y` is the year in 4 digits (2025)
* `%m` is the zero-padded month (06)
* `%d` is the day of the month (01)
* `%H` is the hour in a 24-hour clock (13)
* `%M` are the minutes (23)
* `%S` are the seconds (16)

### Common Time String Formats

```
from datetime import datetime
import time


timestamp = time.time()
datetime_object = datetime.fromtimestamp(timestamp)


print(datetime_object.strftime("%Y-%m-%d"))
print(datetime_object.strftime("%d/%m/%Y %H:%M"))  
print(datetime_object.strftime("%I:%M %p")) 
```

## Alternative Methods

`datetime` is the most commonly used way to bring the date and time into an application. But it’s not the only way. Python’s `time` method (what we’ve been using to generate the timestamp) can also do conversions.

### Using the `time` Module

The `time` The module turns the timestamp into readable structures, but is considered a bit lower-level and less flexible (more on that soon). You would prefer using the `time` module if you only need simple formatting or require compatibility with older Python code.

```
import time


timestamp = time.time()
time_struct = time.localtime(timestamp)
time_string = time.strftime("%Y-%m-%d %H:%M:%S", time_struct)


print("Time string:", time_string)
```

### Comparison Between the `datetime` and `time` Modules

Released in Python 2.3 in 2003, the `datetime` module came after the `time` module. The `time` module goes *way* back to the 1990s. The `time` module is simpler but more limited, especially when it comes to things like date arithmetic or identifying time zones.

`datetime` brings with it added features like:

* Rich attributes (`year`, `month`, etc.)
* `timedelta`, which handles date math
* Better formatting and parsing
* Cleaner handling of time zones

`datetime` didn’t replace `time` (as you can see, both are used in our coding examples), but `datetime` is the recommended way to display dates and times.

`time` is still the quickest way to get the timestamp as a float. You can get the timestamp from `datetime`, but as you can see, it’s a little more code (hence `time` = simpler):

```
from datetime import datetime
timestamp = datetime.now().timestamp()
```

## Handling Time Zones

By default, `datetime.fromtimestamp()` uses the local time zone of the machine running the code. If you run this on a laptop in New York, it will show Eastern time. Running the same script on a server in Germany will show Central European time.

### Using a Uniform Time Zone

Let’s say you want to display Eastern time for every user of an application, no matter where they are. You can do this with the `pytz` library. Make sure to `pip install pytz` before trying to use it.

### Converting to UTC

Before we can specify the time zone, we need to convert the timestamp to UTC.

```
from datetime import datetime
import time


timestamp = time.time()


datetime_utc = datetime.utcfromtimestamp(timestamp)


print("UTC Time:", datetime_utc.strftime("%Y-%m-%d %I:%M %p %Z"))
```

After we convert the timestamp to UTC, we can use `pytz` to convert the UTC time to Eastern time.

```
from datetime import datetime
import pytz
import time


timestamp = time.time()


# convert the timestamp to a UTC datetime object
datetime_utc = datetime.utcfromtimestamp(timestamp)


# define the US Eastern Time timezone
eastern = pytz.timezone('US/Eastern')


# localize the UTC datetime and convert to eastern time
datetime_eastern = pytz.utc.localize(datetime_utc).astimezone(eastern)


print("Eastern Time:", datetime_eastern.strftime("%Y-%m-%d %I:%M %p %Z"))
```

## Best Practices and Common Pitfalls

A lot of this has been covered based on the way we practiced in our examples (i.e., converting to UTC before specifying a time zone). The rest are pretty straightforward and follow the usual coding best practices, such as using `datetime` over `time` when working with new code. It’s also important to use consistent formatting across your project.

## Error Handling and Troubleshooting

Similarly to the best practices, there’s nothing special about error handling and troubleshooting when it comes to working with `datetime` and `time`, just make sure variables are named correctly, use the correct types when making conversions and be careful when you use formatting codes with `strftime()`.

You can use similar error handling as well:

```
from datetime import datetime


try:
    timestamp = "not_a_timestamp"
    datetime_obj = datetime.fromtimestamp(float(timestamp))
except (TypeError, ValueError) as e:
    print("Error converting timestamp:", e)
```

## Conclusion

Converting timestamps to readable dates is easy with Python. Using the `datetime` module, you can quickly convert a timestamp to a date string Python developers trust. With `strftime()`, Python timestamp formatting lets you customize your time strings.

Turning epoch time into human-readable date is simple, and tools like `pytz` help manage time zones. Mastering these techniques means handling time data confidently, making Python datetime timestamp-to-string conversions a breeze.

Start converting and see how straightforward it is to convert Unix timestamps to clear, readable time strings!

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)