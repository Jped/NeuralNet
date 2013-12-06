def genInit():
    inNodes = raw_input("Num input: ")
    hNodes = raw_input("Num Hidden: ")
    oNodes = raw_input("Num Out: ")

    with open("data/nn.init","w") as w:
        w.write("{0} {1} {2}\n".format(inNodes,hNodes,oNodes))

        for hNodeNum in range(int(hNodes)):
            line = [random.random() for i in range(int(inNodes)+1)]
            w.write(" ".join([format(val,'.3f') for val in line])+ '\n')

        for oNodeNum in range(int(oNodes)):
            line = [random.random() for j in range(int(hNodes)+1)]
            w.write(" ".join([format(val,'.3f') for val in line])+'\n')