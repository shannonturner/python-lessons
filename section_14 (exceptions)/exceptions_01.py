# Example #1: Simple Exception handling

try:
    print 1/0 # This will fail.
except ZeroDivisionError:
    print "You can't divide by zero!"
