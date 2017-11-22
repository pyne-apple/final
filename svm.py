# Support Vector Machine attempt
import sys
import general


# python svm.py attr.txt train.txt
def main():
    if len(sys.argv) != 3:
        print("Please execute with 2 arguments <Attribute File> <Training File>")
        exit()

    attributeFileName = sys.argv[1]
    trainingFileName = sys.argv[2]

    attributeList, trainingLists = general.getData(attributeFileName, trainingFileName)


if __name__ == "__main__":
    main()
