from nn import NeuralNet
from node import Node

nn=NeuralNet()
nn.importFile("sample.NNWDBC.init")
nn.train("wdbc.mini_train",.1, 1);
nn.printFile("sup.txt")