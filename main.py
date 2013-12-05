from nn import NeuralNet
from node import Node

nn=NeuralNet()
nn.importFile("sample.NNWDBC.init")
nn.train("wdbc.train",.1, 2);
