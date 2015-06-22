#!/usr/bin/python


"""
    starter code for the evaluation mini-project
    start by copying your trained/tested POI identifier from
    that you built in the validation mini-project

    the second step toward building your POI identifier!

    start by loading/formatting the data

"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.cross_validation import train_test_split

feat_train, feat_test, lbl_train, lbl_test = train_test_split (features, labels, test_size = 0.3, random_state = 42)

from sklearn.tree import DecisionTreeClassifier

dtc = DecisionTreeClassifier ()
dtc.fit (feat_train, lbl_train)
pred = dtc.predict (feat_test)

from sklearn.metrics import accuracy_score

print accuracy_score (pred, lbl_test)

print len (feat_test)

print sum (lbl_test)

print 25.0/29

from sklearn.metrics import precision_score, recall_score

print precision_score (lbl_test, pred)

print recall_score (lbl_test, pred)
