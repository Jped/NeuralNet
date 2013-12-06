from nn import NeuralNet
from node import Node

nn=NeuralNet()
nn.importFile("sample.NNWDBC.1.100.trained.1")
nn.test("wdbc.test");
# nn.printFile("sup.txt")