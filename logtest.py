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

print( logtools.Yesterday())
yl=logtools.YesterLogFiles(rlmid)
print(yl)
if len(yl) == 0:
    print("%s had no logs yesterday" % rlmid)
else:
    print("%s had some logs yesterday (%d)" % (rlmid,len(yl)))
