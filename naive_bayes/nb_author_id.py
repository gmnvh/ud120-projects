#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
'''
    History
    ------------------------------------------------------
    01/22/2018 GMN Mini-project init implementation
'''

from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()

# Training
clf.fit(features_train, labels_train)

# Prediction
pred = clf.predict(features_test)

# Print 5 first tests label / predictions
print labels_test[0:5]
print pred[0:5]

# Calculate accuracy
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(pred, labels_test)
print (' accurancy: ', accuracy)
#########################################################


