import sys

# python comparePredictions.py predictions.txt predictionsSVM.txt 
def main():
    if len(sys.argv) != 3:
        print("Please execute with 2 arguments")
        exit()

    file1Name = sys.argv[1]
    file2Name = sys.argv[2]

    with open(file1Name) as file1, open(file2Name) as file2:
        file1List = []
        for line in file1:
            file1List.append(line)

        file2List = []
        for line in file2:
            file2List.append(line)

        same = 0
        for i in range(len(file1List)):
            if file1List[i] == file2List[i]:
                same += 1
        
        print(str(same) + " / " + str(len(file1List)) + " = " + str(float(same) / float(len(file1List))))
            
if __name__ == "__main__":
    main()
