#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 4 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
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
from sklearn import tree
from sklearn.metrics import accuracy_score

'''
L4Q37

Get a decision tree up and running as a classifier, setting 
min_samples_split=40. It will probably take a while to train. What’s the 
accuracy?
'''

clf = tree.DecisionTreeClassifier(min_samples_split=40)

clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
acc = accuracy_score(pred, labels_test)
print 'Accracy with min_samples_split=40: ', acc

'''
L4Q38

What's the number of features in your data? (Hint: the data is organized into 
a numpy array where the number of rows is the number of data points and the 
number of columns is the number of features; so to extract this number, 
use a line of code like len(features_train[0]).)
'''
print 'Number of features: ',len(features_train[0])
#########################################################


