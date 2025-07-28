A timestamp can be thought of as a numerical record [that captures](https://thenewstack.io/convert-timestamps-to-strings-like-a-python-pro/) exactly when something happened. These timestamps are stored as cumulative seconds since the Unix epoch of January 1st, 1970. Everything after that date is counted in terms of how many seconds have passed from the starting point. For example, July 23, 2025, would be 1753280905 — because that’s how many seconds have passed since the epoch.

A time string, on the other hand, is a collection of characters that represent a moment in time, such as “July 23, 2025.”

These two things are very different from one another.

## Converting Timestamp to Time String Using Python

Most people would have trouble knowing or calculating a timestamp. Because of that, it would be very challenging to use a timestamp in your [Python scripts or applications](https://thenewstack.io/native-python-tutorial/). On top of that, hardcoding timestamps wouldn’t exactly be a good practice for coding because of their length and complexity.

Fortunately, [Python](https://thenewstack.io/decode-any-python-code-with-this-5-step-method/) has a built-in ability to convert timestamps to time strings, without your having to first calculate the current timestamp. This is done with the [datetime module](https://docs.python.org/3/library/datetime.html).

The datetime module calculates the current timestamp for you and is used like this:

```
import datetime

current_timestamp = datetime.datetime.now()
print(current_timestamp)
```

Using `datetime.datetime.now()`, Python automatically calculates the timestamp and then automatically converts it to a time string. For example, the output from a run just now prints:

```
2025-07-23 10:39:23.952357
```

You don’t have to stick with the above formatting because Python allows you to format the time however you want. This is achieved with the `strtime()` function and uses `%Y`, `%m`, `%d`, `%H`, and `%D` to achieve the formatting.

Here’s an example of formatting the time string. Let’s say you want your output to include the Month, Day, Year, Hour, and Minutes (which would be `%m-%d-%Y %H:%M`). The Python code for this would look like:

```
from datetime import datetime

timestamp = datetime.now()
formatted_string = timestamp.strftime('%m-%d-%Y %H:%M')
print(formatted_string)
```

## Syntax of datetime.fromtimestamp()

There’s another method of converting time, which takes a timestamp, converts it to a datetime object, and then stores date-time information for Python.

The syntax for this looks like the following:

```
from datetime import datetime

timestamp = int(your_timestamp_value)
dt_object = datetime.fromtimestamp(timestamp)
```

Here’s an explanation as to what the above does:

* **`datetime`**: This is the function that imports the necessary class for handling dates and times from [Python’s built-in library](https://thenewstack.io/5-python-libraries-every-data-engineer-should-know/).
* **`int(your_timestamp_value)`**: Replaces any placeholder with actual time data. This could be a string representing the time (e.g., “2025-07-23”) or an array of timestamps.
* **`datetime.fromtimestamp(timestamp)`**: This converts the number to a datetime object, which gives you an exact representation of the time.

You can use `datetime.fromtimestamp()` with timestamps. Of course, to do this, you would have to know the exact timestamp.

Let’s assume we’re using the timestamp for July 23, 2025, which is 1753280905. How do we use that with `timestamp()`? Like so:

```
import datetime

timestamp = int(1700845200)
dt_object = datetime.fromtimestamp(timestamp)
print("Timestamp:", dt_object, "Type:", type(dt_object))
```

The key benefit of using `datetime.fromtimestamp()` is that it seamlessly creates a structured representation of timestamps so they can be used within your Python code blocks.

## Using the Python Time Module

The time module provides the necessary tools for dealing with time-related [functions in Python](https://thenewstack.io/so-much-more-python-for-beginners-functions/). With the time module, you can easily get the current system time like so:

```
import time

current_time = time.time()
print(f"Current Time: {current_time}")
```

The output of the above would be the current Unix Epoch, such as:

```
1753283419.3007143
```

There is also the `sleep()` function, which allows the addition of pauses in code. You might want to add a pause in your Python scripts so a process would execute at specific intervals or when performing time-sensitive operations. Here’s an example of the `sleep()` function:

```
import time

print("Waiting for 5 seconds...")
time.sleep(5)
```

What the above script would do is print “Waiting for 5 seconds…”, pause, and return your prompt. Or, you could add the following:

```
import time  # Import 'time' module
print("Waiting for 5 seconds...")
time.sleep(5)

print("Five seconds have passed.")
```

This would print “Waiting for five seconds…”, pause for five seconds, and then print “Five seconds have passed.”

## Handling Timezones

Time zones add another layer of complexity to your code. You will need to manage time zones when working with data that spans different locales. If you don’t, the time could be wrong, depending on where the code is run.

With the Python datetime module, comes the `tzinfo` function, which allows you to work with time zones. Here’s an example:

```
import datetime

from datetime import timezone
now = datetime.datetime.now(timezone.utc)
print(f"Current Time (UTC): {now}")
```

Run the above code, and the results would look like this:

```
Current Time (UTC): 2025-07-23 15:18:54.854103+00:00
```

You could also convert from one time zone to another, like so:

```
import datetime

import pytz

dt = datetime.datetime(2025, 07, 23, 11, 39, 30)
tz = pytz.timezone('America/New_York')
dt = tz.localize(dt)

new_tz = pytz.timezone('America/Los_Angeles')

converted = dt.astimezone(new_tz)

print(converted)
```

The output of the above code would be (run at the current time):

```
2025-07-23 08:39:30-07:00
```

And that’s how you start with Python timestamps and time strings.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)