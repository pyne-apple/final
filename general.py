import numpy as np

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

# returns tuple (attributeList, trainingAttrNPA, trainingClassNPA)
def getData(attributeFileName, trainingFileName):
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
                newAttr.type = "cont"  # continuous
                if (attrVal2 is not None):
                    newAttr.rangeBeg, newAttr.rangeEnd = (
                        int(x) for x in attrVal2.split(".."))
            elif (attrVal1 == "0,1"):
                newAttr.type = "bit"
            else:
                newAttr.type = "offset"  # A quick hack to handle 2001,2002,2003,2004,2005,2006
                newAttr.offset = 2001
                newAttr.rangeBeg = 0
                newAttr.rangeEnd = 5

            attributeList.append(newAttr)

        # Check attributes where read correctly
        #for attr in attributeList:
        #    attr.print()

        trainingAttrLists = []
        trainingClassList = []
        for line in trainingFile:
            splitValues = []
            for i, x in enumerate(line.split()):
                # If class value
                if (attributeList[i].name == "Class"):
                    trainingClassList.append(int(x))
                # If floating point attribute
                elif (attributeList[i].type == "cont"):
                    splitValues.append(float(x))
                # If integer attribute
                else:
                    splitValues.append(int(x))
            trainingAttrLists.append(splitValues)

        #print(trainingAttrLists[:10])

        # Convert to numpy arrarys
        trainingAttrNPA = np.array(trainingAttrLists)
        trainingClassNPA = np.array(trainingClassList)

        # print(trainingAttrNPA)
        # print(trainingClassNPA)
        # print(trainingAttrNPA.tolist())

    return (attributeList, trainingAttrNPA, trainingClassNPA)
