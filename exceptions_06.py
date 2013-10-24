# Example #6: raise (no arguments)

import time

print "I'm going to count down from 1000 as fast as I can.  Hit Ctrl+C three times to stop."

x = 1000
times_paused = 0

while x > 0:

    try:
        print x
        x-=1
    except KeyboardInterrupt:

        times_paused += 1
        
        print " You have paused {0} time(s).".format(times_paused)

        if times_paused == 3:
            print "You paused 3 times.  Ending early by raising the original exception (KeyboardInterrupt)"
            raise # this will raise the *original* exception, which in this case is KeyboardInterrupt

        print "Pausing for {0} seconds.".format(times_paused)
        time.sleep(times_paused)
