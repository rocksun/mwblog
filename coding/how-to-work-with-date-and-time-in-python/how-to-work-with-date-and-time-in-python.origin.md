# How To Work With Date and Time in Python
![Featued image for: How To Work With Date and Time in Python](https://cdn.thenewstack.io/media/2024/09/d8198a9e-fabian-albert-vjlpdzvlz-u-unsplash-1024x589.jpg)
We expect our applications and services to always be on time. Tasks like automation, [data collection](https://thenewstack.io/why-its-time-to-decouple-data-collection-from-monitoring-analytics/), scheduling, security and [IoT integrations](https://thenewstack.io/building-an-iot-weather-station-with-micropython-or-arduino/) would look completely different without the confidence of precise timing. The world would look completely different if each developer built their applications and functions based on their watch. Fortunately, we have the system clock, which provides a universal reference across all programming languages and hardware. In [Python](https://thenewstack.io/python-mulls-a-change-in-version-numbering/), you can easily access this clock using the `datetime`
module.

The `datetime`
module references the system clock. The system clock is a hardware component in computers that tracks the current time. It counts the seconds since a fixed point known as the “epoch,” which is Jan. 1, 1970, on most systems.

Operating systems provide an interface for applications to access the system clock through system calls or [APIs](https://thenewstack.io/api-management/). These system calls and APIs return the current date and time. The accuracy and precision of this time depend on the hardware and the OS’s timekeeping mechanisms, but it all starts from the same place.

Python’s time interface is the `datetime`
module. It calls system APIs to retrieve the current date and time.

## How Does `datetime`
Work?
To first work with dates and times, you’ll need to import the `datetime`
module. The module will import all the methods and attributes of the `datetime`
object into your application. Working with the `datetime`
object will follow the object-oriented programming syntax.

To get the current date and time, you can use the `datetime.now()`
method. It will return the full `datetime`
object with the current date and time down to the nanosecond.

The format is: 2024-07-30 08:59:46.989846

You can also split this if you only need the date or only need the time. Calling the following two methods will extract more limited information from the `datetime`
object.

To print today’s date, use the `date.today()`
method:

To pull just the current time for your application, you’ll have to extract the time from the `datetime`
object.

## Formatting
You can reformat the dates and times as strings using the `strftime()`
method. This allows you to specify your preferred format using format codes. Here’s a common format code:

– `%Y`
updates the year

The following codes update the specified time as a zero-padded decimal number (for example, 01):

– `%m`
updates the month
– `%d`
updates the day
– `%H`
updates the 24-hour clock
– `%M`
updates the minute
– `%S`
updates the second

A complete block of code that utilizes these format codes might look like this:

## Working With Time Zones
You can adjust the `datetime`
object to reflect different time zones using the `pytz`
library. Before you use it, you’ll need to import it:

It’s not required that you get the UTC time first, but it is best practice because the UTC never changes (including during daylight savings time), so it’s a strong reference point.

Python’s `datetime`
module saves the date!

The `datetime`
module simplifies working with timing in Python. It eliminates much of the complexity involved in synchronizing applications and ensures they operate with accurate, consistent timing.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)