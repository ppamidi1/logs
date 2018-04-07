#!/usr/bin/env python3

import time
import glob

def Yesterday():
    td = time.time()
    yd = td - 23 * 3600
    ydl = time.gmtime(yd)
    ydstr = time.strftime("%Y%m%d" , ydl )
    return ydstr

def YesterLogFiles(pn):
    slog = "%s/%s_*stats.log" %(pn,Yesterday())
    ylog = "%s/%s_[0-9][0-9][0-9][0-9].log" % (pn,Yesterday())
    return [glob.glob(slog),glob.glob(ylog)]
