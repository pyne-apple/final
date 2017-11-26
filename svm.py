# Support Vector Machine attempt
import sys
import general
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import VarianceThreshold
from sklearn import preprocessing
from sklearn import tree
from sklearn.linear_model import SGDClassifier
from sklearn.neural_network import MLPClassifier


# python svm.py attr.txt train.txt prelim.txt
def main():
    if len(sys.argv) != 4:
        print("Please execute with 3 arguments <Attribute File> <Training File> <Predict File>")
        exit()

    attributeFileName = sys.argv[1]
    trainingFileName = sys.argv[2]
    predictFileName = sys.argv[3]

    attributeList, trainingAttrNPA, trainingClassNPA = general.getData(attributeFileName, trainingFileName)
    r_before, c_before = trainingAttrNPA.shape
    #print(r_before, c_before)

    # Scale
    min_max_scaler = preprocessing.MinMaxScaler()
    trainingAttrNPA = min_max_scaler.fit_transform(trainingAttrNPA)
    # trainingAttrNPA = preprocessing.scale(trainingAttrNPA)

    if predictFileName:
        _, predictAttrNPA, _ = general.getData(
            attributeFileName, predictFileName)
        predictAttrNPA = min_max_scaler.transform(predictAttrNPA)

    # Find and remove attributes that aren't helpful
    # Removes all features that are have one value (probably 0.0) in more than x% of the samples in the form (x * (1 - x))
    featureSelection = VarianceThreshold(0)
    # Note, this doesn't also remove the columns in attributeList, so don't use attributeList after this
    # consider removing attributeList from the general.getData() return tuple
    trainingAttrNPA = featureSelection.fit_transform(trainingAttrNPA) 

    if predictFileName:
        predictAttrNPA = featureSelection.transform(predictAttrNPA)
        # print(predictAttrNPA.shape)
    
    r_after, c_after = trainingAttrNPA.shape
    # print("Columns removed: " + str(c_before - c_after) + " / " + str(c_before) + " = " + str(float(c_before - c_after)/float(c_before)) + "%")

    # Test while building model ************************************
    # # Split into training and test
    attr_train, attr_test, class_train, class_test = train_test_split(
        trainingAttrNPA, trainingClassNPA, test_size=0.33)

    # # Test split
    # # print(attr_test.tolist())
    # # print(attr_train.shape)
    # # print(attr_test.shape)
    # # print(class_train.shape)
    # # print(class_test.shape)

    #SVM CLASSIFIER: classifier = svm.SVC(kernel='linear', C=1.0) 70% accuracy
    # classifier = svm.SVC(kernel='linear', C=2.0, decision_function_shape="ovr") #70 % accuracy
    #classifier = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1) #52% accuracy
    #classifier = MLPClassifier(solver='sgd', alpha=1e-5,hidden_layer_sizes=(3, 2), random_state=1) #70%

    #classifier = MLPClassifier(solver='sgd', alpha=1e-5, hidden_layer_sizes=(5,),random_state=1) #70-72%
    classifier = MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(130,), random_state=1) #71-72% (highest so far)
    #classifier = SGDClassifier(loss="perceptron", penalty="elasticnet") #64%
    classifier.fit(attr_train, class_train)

    # predictions = classifier.predict(attr_test)
    #print(len(predictions), len(attr_test))
    # accuracy = accuracy_score(class_test, predictions)

    # train_score = classifier.score(attr_train, class_train)

    # print("Train accuracy is: " + str(train_score))
    # print("Test accuracy is: " + str(accuracy))

    predictions = classifier.predict(predictAttrNPA)

    for c in predictions:
        print(c)

if __name__ == "__main__":
    main()
