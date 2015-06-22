#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### the words (features) and authors (labels), already largely processed
### these files should have been created from the previous (Lesson 10) mini-project.
words_file = "word_data_overfit.pkl" ### like the file you made in the last mini-project 
authors_file = "email_authors_overfit.pkl"  ### this too
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (remainder go into training)
### feature matrices changed to dense representations for compatibility with classifier
### functions in versions 0.15.2 and earlier
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]



### your code goes here
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier ()
dt.fit (features_train, labels_train)
dt_pred = dt.predict (features_test)

from sklearn.metrics import accuracy_score

print accuracy_score (dt_pred, labels_test) 

importances = dt.feature_importances_
import numpy as np
indices = np.argsort(importances)[::-1]
print 'Feature Ranking: '
for i in range(10):
    print "{} feature no.{} ({})".format(i+1,indices[i],importances[indices[i]])
