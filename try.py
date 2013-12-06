from nn import NeuralNet
from node import Node

nn=NeuralNet()
nn.importFile("sample.NNWDBC.init")
nn.printFile("sup.txt")