import os.path
from node import Node
import sys
class NeuralNet:
    def __init__(self, file=None):
        print "making nn"
        if not os.path.isfile(file):
            print "no file"

    def importFile(file):
        f =open(file)
        fl=f.readlines()
        top=fl[0].strip().split(' ')
        nin=int(top[0])
        nhid=int(top[1])
        nout=int(top[2])
        ml=fl[1:(nhid+1)]
        bl=fl[(nhid+1):]
        nilist=[Node() for i in range(nin)]
        nhlist=[Node() for i in range(nhid)]
        nolist=[Node() for i in range(nout)]
        for x in xrange(len(ml)):
            l=ml[x].strip().split(' ')
            nhlist[x].weights=float(l[1:])
            nhlist[x].bias=float(l[0])

        for x in xrange(len(bl)):
            l=ml[x].strip().split(' ')
            nolist[x].bias=float(l[0])
            nolist[x].weights=float(l[1:])

        nlist=[nilist,nhlist,nolist];
        print nlist
        f.close()
        
		

    def train(file, lrate, nepochs):
        print "training"
        f=open(file)
        fl=f.readlines()
        top=fl[0].strip().split(' ')
        if fl[1] is not nin or fl[2] is not nout:
        	print "incompatible with init file"
        	sys.exit()

        d=[]
        output=[]
        for x in xrange(1,len(fl)):
        	l=fl[x].strip().split(' ')
        	d.append(float(l[:-1]))
        	output.append(int(l[-1]))

        f.close()
        for epoch_num in xrange(nepochs):
            print "Epoch " + str(epoch_num) + " of "+str(nepochs)
            for l in data:
            	



