# Support Vector Machine attempt
import sys
import general
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# python svm.py attr.txt train.txt
def main():
    if len(sys.argv) != 3:
        print("Please execute with 2 arguments <Attribute File> <Training File>")
        exit()

    attributeFileName = sys.argv[1]
    trainingFileName = sys.argv[2]

    attributeList, trainingAttrNPA, trainingClassNPA = general.getData(attributeFileName, trainingFileName)

    # Split into training and test
    attr_train, attr_test, class_train, class_test = train_test_split(
        trainingAttrNPA, trainingClassNPA, test_size=0.33)

    # print(attr_train)
    # print() 
    # print(attr_test)
    # print() 
    # print(class_train)
    # print() 
    # print(class_test)
    # print()

    # classifier = svm.SVC(kernel='linear', C=1.0)
    # classifier.fit(attr_train, class_train)

    # predictions = classifier.predict(attr_test)
    # accuracy = accuracy_score(class_test, predictions)

    # print("Accuracy is: " + str(accuracy))

    # First row of train.txt, should be 1
    # print(classifier.predict([0.0, 0.0, 1.0, 1.26, 1.17, 0.72, 4.59, 0.45, 0.765, 0.54, 0.495, 0.81, 0.54, 0.81, 1.08, 56.745, 0.81, 0.855, 28.2293, 38.9354, 1.2466, 2.16, 0.0, 4.5512, 0.2054, 0.045, 0.0, 0.0, 305.1977, 49.4312, 5134.4333, 20.6963, 6.5127, 69.39, 763.56, 13.5, 9.18, 0.45, 13.14, 4.95, 0.99, 0.81, 0.54, 7188.84, 117.27, 14022.09, 243.45, 51.84, 1.216, 19.904, 0.464, 0.1493, 0.016, 0.3573, 0.156, 0.032, 0.0293, 0.016, 20.28, 2.1667, 23.6747, 2.9213, 1.1027, 97.082, 60.0, 189.7367, 228.4732, 0.0, 2543.1269, 2778.3628, 6259.6565, 0.0, 0.0, 94.8683, 510.0124, 885.1316, 84.8528, 150.1301, 1.1028, 1.1564, 1.1455, 1.1092, 1.0699, 1.0979, 1.0699,
    #                    1.0548, 1.1347, 1.0472, 1.1271, 1.1247, 1.1168, 1.1376, 1.1382, 8.1964, 40.4703, 7.0, 2.6667, 1.2, 5.36, 3.9333, 1.7143, 1.8333, 1.2, 13.9982, 11.2192, 12.0266, 10.5905, 8.7917, 0.0178, 0.5467, 0.0489, 0.0089, 0.0044, 0.0178, 0.04, 0.0089, 0.0044, 0.0044, 0.9511, 0.0178, 0.0267, 0.0933, 0.0711, 0.003084, 0.033936, 0.0006, 0.000408, 2e-05, 0.000584, 0.00022, 4.4e-05, 3.6e-05, 2.4e-05, 0.319504, 0.005212, 0.623204, 0.01082, 0.002304, 14.591, 1.1355, 0.0678, 0.5082, 2004.0, 1153.0, 1149.87, 1.4, 4.0, 3.0, 4.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 3.0, 3.0, 6.0, 1.0, 1.0, 3.0, 4.0, 6.0, 5.0, 5.0, 4.0, 3.0, 2.0, 2.0, 1.0, 3.0, 0.0, 0.0, 0.0, 0.0]))

if __name__ == "__main__":
    main()
