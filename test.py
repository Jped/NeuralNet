from nn import NeuralNet
from node import Node

nn=NeuralNet()
print "Enter trained Neural Net filename"
infile=raw_input()
print "Enter test filename"
testfile = raw_input()
print "Enter output filename"
results = raw_input()
nn.importFile(infile)
nn.test(testfile,results);
