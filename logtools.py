#!/usr/bin/env python3
import os.path
import time
import glob
import zipfile

def Today():
    td = time.time()
    tdl = time.gmtime(td)
    tdstr = time.strftime("%Y%m%d" , tdl )
    return tdstr

def Yesterday():
    td = time.time()
    yd = td - 23 * 3600
    ydl = time.gmtime(yd)
    ydstr = time.strftime("%Y%m%d" , ydl )
    return ydstr

def YesterLogFiles(pn):
    slog = "%s/journal/%s_*stats.log" %(pn,Yesterday())
    ylog = "%s/journal/%s_[0-9][0-9][0-9][0-9].log" % (pn,Yesterday())
    slogs = glob.glob(slog)
    ylogs = glob.glob(ylog)
    if len(slogs) > 0 or len(ylogs) > 0:
        return glob.glob(slog)+glob.glob(ylog)
    return []

def FindUniqueLogDates(pn):
    all = "%s/journal/*.log" % (pn)
    uniqdates=[]
    allfiles=glob.glob(all)
    for fn in allfiles:
        fnb=os.path.basename(fn)
        print(fnb)
        fns=fnb.split("_")
        if fns[0] not in uniqdates:
            uniqdates.append(fns[0])
    return uniqdates

def PackAllFiles(pn,dt,rm):
    zipfilename="%s/journal/%s.zip" % (pn,dt)
    filestozip=glob.glob("%s/journal/%s*.log" % (pn,dt))
    print("Creating %s " % zipfilename)
    with zipfile.ZipFile(zipfilename,'w') as savefile:
        for fz in filestozip:
            savefile.write(fz,os.path.basename(fz))
            print("Added %s" % fz)
            if rm:
                os.remove(fz)
                
def IdentifyRLMs(rootfolder):
    print("Root folder %s" %  rootfolder)
    rlmfolders=glob.glob("%s/*00*" % rootfolder)
    return rlmfolders 
