from nn import NeuralNet
from node import Node

nn=NeuralNet()
print "Enter Neural Net filename"
infile=raw_input()
print "Enter training filename"
trainfile = raw_input()
print "Enter learning rate"
lrate = raw_input()
print "Enter # of Epochs"
ep = raw_input()
print "Enter output filename"
outfile = raw_input()
nn.importFile(infile)
nn.train(trainfile,float(lrate), int(ep));
nn.printFile(outfile)

