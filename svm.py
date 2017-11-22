# Support Vector Machine attempt
import sys

class attribute():
    def __init__(self):
        self.name = None  
        self.type = None  
        self.rangeBeg = None
        self.rangeEnd = None
        self.offset = None
    
    def print(self):
        print("Name:", self.name, end='')
        print(", Type:", self.type, end='')
        print(", Range:[", self.rangeBeg, end='')
        print(",", self.rangeEnd, end='')
        print("], Offset:", self.offset)
        pass


# python svm.py train.txt attr.txt
def main(): 
    if len(sys.argv) != 3:
        print("Please execute with 2 arguments <Training File> <Attribute File>")
        exit()

    trainingFileName = sys.argv[1]
    attributeFileName = sys.argv[2]

    # Reading in data from training file
    with open(trainingFileName) as trainingFile, open(attributeFileName) as attributeFile:
        attributeList = []  # List of attribute objects
        for line in attributeFile:
            newAttr = attribute()

            splitValues = line.rstrip(" .\n").split()
            attrName = splitValues[0] 
            attrVal1 = splitValues[1] 
            attrVal2 = None
            if len(splitValues) > 2:
                attrVal2 = splitValues[2]

            newAttr.name = attrName.rstrip(" :")  # Remove the ':' from the end
            
            if (attrVal1 == "cont"):
                newAttr.type = "cont" # continuous
                if (attrVal2 is not None):
                    newAttr.rangeBeg, newAttr.rangeEnd = (int(x) for x in attrVal2.split(".."))
            elif (attrVal1 == "0,1"):
                newAttr.type = "bit"  
            else:
                newAttr.type = "offset" # A quick hack to handle 2001,2002,2003,2004,2005,2006
                newAttr.offset = 2001
                newAttr.rangeBeg = 0
                newAttr.rangeEnd = 5

            attributeList.append(newAttr)
        
        # Check attributes where read correctly
        # for attr in attributeList:
        #     attr.print()

        trainingLists = []
        for line in trainingFile:
            splitValues = []
            for i, x in enumerate(line.split()):
                if (attributeList[i].type == "cont"):
                    splitValues.append(float(x))
                else:
                    splitValues.append(int(x))
            trainingLists.append(splitValues)

        # print(trainingLists[:10])



if __name__ == "__main__":
    main()
