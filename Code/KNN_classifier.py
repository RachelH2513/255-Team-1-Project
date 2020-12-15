import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)
pd.options.display.float_format = "{:.2f}".format

#########################################################
#                   Load Data from Csv                  #
#########################################################
data = pd.read_csv("../Data/wine.csv")

# Convert DataFrame into NumPy array
data_array = data.to_numpy()
X = pd.DataFrame(data_array, columns=data.columns)

X.head() # Return the first 5 rows
# print(X)

# Convert Cultivar types into dummy variables.
y = data['Cultivars'] 
y = pd.get_dummies(y) 
y.head()
# print(y)

# Check for null values.
print(X.shape)
print(y.shape)

#########################################################
#             Normalize variables Variables             #
#########################################################
from sklearn.preprocessing import StandardScaler

standard_scaler = StandardScaler()

standard_scaler.fit(X) # fit scaler to feature
scaled_features = standard_scaler.transform(X) # Transform features into scaled feature

# Need to convert scaled features into a dataframe
data_features = pd.DataFrame(scaled_features,columns=X.columns)
data_features.head()
# print(data_features)


#########################################################
#          Split Data into Training and Test            #
#########################################################
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(scaled_features, y, test_size=0.20)

#########################################################
#                    KNN Algorithm                      #
#########################################################
# Implement the k-nearest neighbors
# Number of neighbors = 5

from sklearn.neighbors import KNeighborsClassifier

KNN_Classifier = KNeighborsClassifier(n_neighbors=5)
KNN_Classifier.fit(X_train, y_train)

prediction = KNN_Classifier.predict(X_test) # Prediction


#############################################################################
#         Confusion matrix, precision, recall, f1-score of KNN Algorithm    # 
#############################################################################

from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test.values.argmax(axis=1), prediction.argmax(axis=1)))
print(classification_report(y_test,prediction))

#############################################################################
#                          Accuracy of KNN  Algorithm                       #
#############################################################################

from sklearn import metrics
print("Model Accuracy:",metrics.accuracy_score(y_test, prediction))