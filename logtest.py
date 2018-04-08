#!/usr/bin/env python3

import logtools
rlmid="RL00001"
print (logtools.Today())
logdates = logtools.FindUniqueLogDates(rlmid)
print(logdates)
for logdate in logdates:
    print( "Date : %s" % logdate)
    logtools.PackAllFiles(rlmid,logdate,False)
