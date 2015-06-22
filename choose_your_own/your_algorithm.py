#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

from time import time

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
#################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary


from sklearn import neighbors

n_neighbors = 22

clf_knn = neighbors.KNeighborsClassifier(n_neighbors)

t_0 = time ()

clf_knn = clf_knn.fit (features_train, labels_train)

print "training time: ", round(time() - t_0, 3), "s"

t_1 = time ()

pred_knn = clf_knn.predict (features_test)

print "prediction time: ", round(time() - t_1, 3), "s"

from sklearn.metrics import accuracy_score

print "accuracy of knn: ", accuracy_score (pred_knn, labels_test)


'''
from sklearn.ensemble import AdaBoostClassifier

clf_adb = AdaBoostClassifier ()

t_0 = time ()

pred_adb = clf_adb.fit (features_train, labels_train).predict (features_test)

print "training time: ", round(time() - t_0, 3), "s"

from sklearn.metrics import accuracy_score

print "accuracy of adaboost: ", accuracy_score (pred_adb, labels_test)
'''

'''
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=19)
t0 = time()
clf = clf.fit(features_train, labels_train)
print "Training: ", round(time() - t0, 3), "s"
t1 = time()
pred = clf.predict(features_test)
print "Prediction: ", round(time() - t1, 3), "s"
print "Accuracy: ", accuracy_score(pred, labels_test)
'''

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
