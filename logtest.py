#!/usr/bin/env python3

import logtools
rlmid="RL00001"
today=logtools.Today()
logdates = logtools.FindUniqueLogDates(rlmid)
print(logdates)
for logdate in logdates:
    print( "Date : %s" % logdate)
    if logdate == today:
        print("Leaving out today's files")
    else:
        logtools.PackAllFiles(rlmid,logdate,False)
