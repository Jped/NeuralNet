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
            l=bl[x].strip().split(' ')
            l=map(float,l)
            nolist[x].bias=l[0]
            nolist[x].weights=l[1:]

        self.nlist=[nilist,nhlist,nolist];
        # print self.nlist
        f.close()
    
    def printFile(self, file):
        f=open(file, 'w')
        f.writelines("%i %i %i\n" %(self.nin, self.nhid, self.nout))
        for nh in self.nlist[1]:
            f.writelines("%f"%nh.bias)
            for w in nh.weights:
                f.writelines(" %f"%w)
            f.writelines("\n")
        for no in self.nlist[2]:
            f.writelines("%f"%no.bias)
            for w in no.weights:
                f.writelines(" %f"%w)
            f.writelines("\n")
        f.close()

    

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
        print(len(d))
        print(len(d[0]))

        f.close()
        # print len(d[299])
        # print self.nin
        for epoch_num in xrange(nepochs):
            print "Epoch " + str(epoch_num+1) + " of "+str(nepochs)
            for e in xrange(len(d)):
                # print "example # " + str(e)
                # print len(d[e])

                for i, act in enumerate(d[e]):
                    self.nlist[0][i].activation=act
                    # print i 

                for l in xrange(1,3):
                    for k in xrange(len(self.nlist[l])):
                        sum=0
                        for i, n in enumerate(self.nlist[l-1]):
                            sum+=self.nlist[l][k].weights[i]*n.activation
                        sum+= -1*self.nlist[l][k].bias
                        self.nlist[l][k].inval=sum
                        self.nlist[l][k].activation=sigmoid(sum)

                for i, onode in enumerate(self.nlist[2]):
                    # print output[e][i]
                    onode.delta=sigmoidprime(onode.inval) * output[e][i] - onode.activation

                for i, hnode in enumerate(self.nlist[1]):
                    sum=0
                    for n in xrange(len(self.nlist[2])):
                        sum+=self.nlist[2][n].weights[i]*self.nlist[2][n].delta
                    hnode.delta=sigmoidprime(hnode.inval)*sum
                for l, layer in enumerate(self.nlist[1:]):
                    # print "layer" + str(l)
                    for n, node in enumerate(layer):
                        for w, weight in enumerate(node.weights):
                            weight+= lrate*self.nlist[l][w].activation*node.delta
                        node.bias+= -1*lrate*node.delta


        
                    





                    



