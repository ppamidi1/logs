import sys
import time
import os
import socket
import telnetlib
import json
import extract

class RenderLogs(object):
    def __init__(self):
        #self.console_ip = sys.argv[1]
        #self.connect_telnet()
        self.connect_graphite()

    def connect_graphite(self):
        """ Connect the graphite server
        Arguments(s):
        None
        
        Return(s):
        None
        """

        CARBON_SERVER = '172.16.1.149'
        CARBON_PORT = 2003
        self.sock = socket.socket()        
        self.sock.connect((CARBON_SERVER, CARBON_PORT))

    def getReboots(rc, vst):
        reboots = rc/((vst+1)/(3600*24))
        return reboots

    def getUpTime(nmt, vst):
        upTime = (1-(nmt-vst)/nmt)*100
        return upTime

    def getFilesPerDay(frc, vst):
        files = frc/(vst/(3600*24))
        return files

    def send_data_to_graphite(self):
        extract.main()
        d = os.listdir()
        delay = 1
        for files in d:
            if (("RL" in files or "TU" in files) and ".txt" in files):
                data = json.load(open(files))
                f = files[0:7]
                if f in data:
                    rc = int(data[f][3].get('rc'))
                    vst = int(data[f][3].get('vst'))
                    nmt = int(data[f][3].get('nmt'))
                    frc = int(data[f][3].get('frc'))
                    reboots = rc/((vst+1)/(3600*24))
                    upTime = (1-(nmt-vst)/nmt)*100
                    #return(f,getReboots(rc,vst),getUpTime(nmt,vst),getFilesPerDay(frc,vst))
                    print ('RLname : %s Reboot : %d Uptime : %d' % (f,reboots,upTime))

                    timestamp = int(time.time())
                    lines = [
                        'RLname.%s.UpTime %d %d' % (f, upTime, timestamp),
                        'RLname.%s.Restarts %s %d' % (f, reboots, timestamp)
                        ]

                    message = '\n'.join(lines) + '\n'
                    print(message)
                    self.sock.send(message.encode("utf-8"))
                    time.sleep(delay)

        #RLname = 'RL00004'
        #timestamp = os.system ('ls /home/ppamidi/RL00004/journal/2*stats.log | tail -1 | grep -o "[0-9]\+stats" | sed "s/[^0-9]*//g" >')
        #UpTime = os.system ('cat "$(ls /home/ppamidi/RL00004/journal/2*stats.log | tail -1)" | grep "Up Time:" | grep -Eo "\b[0-9]+\b"')
        #print(timestamp)
        
if __name__ == '__main__':
    performance = RenderLogs()
    try:
        while True:
            #data = performance.get_data_from_console()
            performance.send_data_to_graphite()
            break;
    except KeyboardInterrupt:
            print("Key Pressed...")
    finally:
        print("Script exited!!!")
