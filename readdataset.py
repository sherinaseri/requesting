from extractfeature import *
from os import listdir

def readDataSet(dir, website, withping):
    print 'read data set ...'
    traces = []
    directory = dir + website + '/'
    pcapfiles = listdir(directory)

    for i in pcapfiles:
       feature = features(dir + website + '/' + i, withping,website)
       x = feature.extractsizedir()
       if len(x) > 0:
          traces.append(feature)

    return traces




def createsitesdictionary():

    dir = '/home/shahrzad/Projects/uProxy/Dataset/selected_Input/'
    websites = listdir(dir)
    withping = True
    sitesdic = {}
    print websites
    print len(websites)
    for i in websites:
       print i
       sitesdic[i] = readDataSet(dir,i,withping)
    return sitesdic



def savetofile():
    traces = createsitesdictionary()
    output = open('./output/all.csv','w')
    for key in traces:
        onesiteTrace = traces.get(key,None)
        for i in onesiteTrace:
            output.write(i.getFeatureString())
            output.write("\n")
    output.close()


savetofile()
#createsitesdictionary()
