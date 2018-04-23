 import os
import json
import time

def find():
    d = os.listdir()
    RLM = []
    for dirs in d:
        if(("RL0" in dirs or "TU0" in dirs) and ".txt" not in dirs):
            RLM.append(dirs)
    return(RLM)


def getStatLogs(RLM):

    for rl in RLM:
        stats = []
        logs = os.listdir('/home/ppamidi/RemoteLinkLogs/'+rl+'/journal')
        if(logs != []):
            for files in logs:
                if ('stats.log' in files and '.zip' not in files):
                    stats.append(files)
                    stats.sort()
            if(len(stats) > 1):
                del stats[-1]
                f = stats[-1]
                statLogs = convert(rl,f)
    return statLogs


def convert(rl,f):
    statDict = {}
    statLogFile = open("/home/ppamidi/RemoteLinkLogs/"+rl+"/journal/"+f,"r")
    stlog = statLogFile.read()
    lines =stlog.splitlines()
    if (len(lines) > 1):
        SOM = {}
        SOMData =  lines[0].split(":")
        SOM[SOMData[0]]=SOMData[1]

        Network = {}
        NetData = lines[8].split(":")
        Network[NetData[0]] = NetData[1]

        UpTime = {}
        UpData = lines[17].split(":")
        UpTime[UpData[0]] = UpData[1]

        keys = lines[23].split(",")
        values = lines[24].split(",")
        Chart = dict(zip(keys, values))

        data = [SOM,Network,UpTime,Chart]
        statDict[rl] = data

    with open(rl + ".txt", "w") as json_data:
        json.dump(statDict, json_data)
    json_data.close()
    return json_data


def main():
    RLM = find()
    statLogs = getStatLogs(RLM)


if __name__ == '__main__':
    main()



