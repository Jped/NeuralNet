import os.path
from node import Node
import sys
from math import exp

def sigmoid(x):
    return 1 / (1 + exp(x))

def sigmoidprime(x):
    return sigmoid(x) * (1 - sigmoid(x))
class NeuralNet:
    def __init__(self):
        print "making nn"
        self.nlist=[]
        self.nin=0
        self.nhid=0
        self.nout=0

        # if not os.path.isfile(file):
        #     print "no file"

    def importFile(self, file):
        f =open(file)
        fl=f.readlines()
        top=fl[0].strip().split(' ')
        self.nin=int(top[0])
        self.nhid=int(top[1])
        self.nout=int(top[2])
        ml=fl[1:(self.nhid+1)]
        bl=fl[(self.nhid+1):]
        nilist=[Node() for i in range(self.nin)]
        nhlist=[Node() for i in range(self.nhid)]
        nolist=[Node() for i in range(self.nout)]
        for x in xrange(len(ml)):
            l=ml[x].strip().split(' ')
            l=map(float,l)
            nhlist[x].bias=l[0]
            nhlist[x].weights=l[1:]

        for x in xrange(len(bl)):
            l=ml[x].strip().split(' ')
            l=map(float,l)
            nolist[x].bias=l[0]
            nolist[x].weights=l[1:]

        self.nlist=[nilist,nhlist,nolist];
        # print self.nlist
        f.close()
    
    # def print_file()   
    

    def train(self,file, lrate, nepochs):
        print "training"
        f=open(file)
        fl=f.readlines()
        top=fl[0].strip().split(' ')
        if int(top[1]) is not self.nin or int(top[2]) is not self.nout:
            print "incompatible with init file"
            sys.exit()

        d=[]
        output=[]
        for x in xrange(1,len(fl)):
            l=fl[x].strip().split(' ')
            d.append(map(float,l[:-1]))
            output.append(map(int, l[-1]))

        f.close()
        for epoch_num in xrange(nepochs):
            print "Epoch " + str(epoch_num) + " of "+str(nepochs)
            for i in xrange(self.nin):
                for k in xrange(len(d[i])):
                    self.nlist[0][i].activation=d[i][k]

            for l in xrange(1,3):
                for k in xrange(len(self.nlist[l])):
                    sum=0
                    for i, n in enumerate(self.nlist[l-1]):
                        sum+=self.nlist[l][k].weights[i]*n.activation
                    self.nlist[l][k].inval=sum
                    self.nlist[l][k].activation=sigmoid(sum)
        
                    





                    



