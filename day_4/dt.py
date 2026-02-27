#  Datetime library
#  datetime module is used
#  allows you to work with dates and times in your code.
#  includes functions for formatting and manipulating date
#  and time data, as well as classes for reppin dates, times and
#  time intervals.
from datetime import datetime, timedelta

#  Get the current date and time
now = datetime.now()
print(now) # Output: Current date and time

#  Create a datetime object for a specific date and time
date = datetime(2026,2,25,0)
print(date) # Output 2026-02-25 12:00:00


#  Calcuate the difference between two dates
delta = now - date
print(delta) # Output : Difference