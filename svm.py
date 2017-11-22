# Support Vector Machine attempt
import sys


# python svm.py train.txt attr.txt
def main(): 
    if len(sys.argv) != 3:
        print("Please execute with 2 arguments <Training File> <Attribute File>")
        exit()

    trainingFileName = sys.argv[1]
    attributeFileName = sys.argv[2]

    # Reading in data from training file
    with open(trainingFileName) as trainingFile, open(attributeFileName) as attributeFile:
        trainingLists = []
        for line in trainingFile:
            splitValues = list(x for x in line.split())
            trainingLists.append(splitValues)

        print(trainingLists[:10])



if __name__ == "__main__":
    main()
