
# Getting a timestamp in the format YYYYMMDDHHMMSS

## NOTE: For clarity and consistency, all examples below will use the same timestamp; 2013 October 20 09:38:26

import time

print time.localtime() # time chunks smaller than ten are not zero-padded
    ##time.struct_time(tm_year=2013, tm_mon=10, tm_mday=20, tm_hour=9, tm_min=38, tm_sec=26, tm_wday=6, tm_yday=293, tm_isdst=1)

# The slices that I want are year (slice zero) through second (slice five), so I need the slicing indices [0:6]

print time.localtime()[:6]
    ##(2013, 10, 20, 9, 38, 26

# So my instinct is to use a str.join() to glue together all of the pieces that I want, slices [0:6]

    ##>>> ''.join(time.localtime()[:6])
    ##
    ##Traceback (most recent call last):
    ##  File "<pyshell#9>", line 1, in <module>
    ##    ''.join(time.localtime()[:6])
    ##TypeError: sequence item 0: expected string, int found

# But that instinct turns out to be wrong, because join wants to glue together strings, not ints.


# There are many solutions to this problem.

# Method #1: Looping (the easy but long way)
timestamp = []

for time_chunk in time.localtime()[:6]:
    timestamp.append(str(time_chunk))

print "Method #1: ", ''.join(timestamp)

# Method #2: Passing an arbitrary number of arguments (quick but somewhat ugly)

print "Method #2: ", '{0}{1}{2}{3}{4}{5}'.format(*time.localtime()[:6])

# Method #3: List comprehension

print "Method #3: ", ''.join([str(time_chunk) for time_chunk in time.localtime()[:6]])
