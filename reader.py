import dpkt


class PcapReader:
    filename=''
    fpcap=None
    noFile = False
    def __init__(self,filename):
        try:
            self.filename=filename
            self.fpcap=dpkt.pcap.Reader(open(filename,'r'))
            self.noFile = False
        except IOError:
            self.noFile = True
            print filename,'There is no such a File'