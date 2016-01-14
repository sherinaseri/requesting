from reader import *
import dpkt
import socket


class features:
    def __init__(self, pcapfile, withping, name):
        self.pcapfile = pcapfile
        self.withping = withping
        self.name = name
        self.totalpktnum = 0
        self.countlendir = {}
        self.lendir = []

    def extractsizedir(self):
        rd = PcapReader(self.pcapfile)
        clientip = '192.168.100.179'
        serverip = '128.119.247.197'
        if not rd.noFile:
            for ts, pkt in rd.fpcap:
                eth = dpkt.ethernet.Ethernet(pkt)
                if eth.type == dpkt.ethernet.ETH_TYPE_IP:
                    self.totalpktnum += 1
                    ip = eth.data
                    pktsrcip = socket.inet_ntoa(ip.src)
                    # add the size of the all of the packets (with pinging packets)
                    if self.withping:
                        self.updownstream(pktsrcip, clientip, serverip, pkt)
                    else:
                        if len(eth) != 107 and len(eth) != 119 and len(eth) != 135:
                            self.updownstream(pktsrcip, clientip, serverip, pkt)

        return self.lendir

    def updownstream(self, pktsrcip, clientip, serverip, pkt):
        if pktsrcip == clientip:  # upstream is positive
            self.lendir.append(len(pkt))
        elif pktsrcip == serverip:  # downstream is negative
            self.lendir.append(-1 * len(pkt))

    def gettotalpktnum(self):
        return self.totalpktnum


    def getcountlendir(self):
        for i in self.lendir:
            if not self.countlendir.has_key(i):
                self.countlendir[i] = 0
            self.countlendir[i] += 1
        return self.countlendir

    def getFeatureString(self):
        self.getcountlendir()
        fstring = ''
        for i in range(52,1500):
            fstring = fstring + '%d,%d,'%(self.countlendir.get(i,0) , self.countlendir.get(-1 * i,0))

        return fstring+self.name

