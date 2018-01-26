#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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

from sklearn import svm
from sklearn.metrics import accuracy_score

# L3Q28 - Using a linear kernel, what is the accuracy of the classifier ?
# L3Q29 - Is it faster or slower than Naive Bayes ?

clf_linear = svm.SVC(kernel='linear')

t0 = time()
clf_linear.fit(features_train, labels_train)
pred = clf_linear.predict(features_test)
accuracy = accuracy_score(pred, labels_test)
print 'Linear kernel - accuracy ', accuracy
print "Fit and prediction time:", round(time()-t0, 3), "s"


# L3Q30 Re-do with just 1% of the data. What the accuracy now ?

features_train_reduced = features_train[:len(features_train)/100] 
labels_train_reduced = labels_train[:len(labels_train)/100]

t0 = time()
clf_linear.fit(features_train_reduced, labels_train_reduced)
pred = clf_linear.predict(features_test)
accuracy = accuracy_score(pred, labels_test)
print 'Linear kernel with 1% of the data - accuracy ', accuracy
print "Fit and prediction time:", round(time()-t0, 3), "s"

# L3Q32 Re-do with 1% of the data and rbf kernel

clf_rbf = svm.SVC(kernel='rbf')

t0 = time()
clf_rbf.fit(features_train_reduced, labels_train_reduced)
pred = clf_rbf.predict(features_test)
accuracy = accuracy_score(pred, labels_test)
print 'Rbf kernel with 1% of the data - accuracy ', accuracy
print "Fit and prediction time:", round(time()-t0, 3), "s"

# L3Q33 - Try differente values for C

c_values = [1.0, 10.0, 100.0, 1000.0, 10000.0]

for c in c_values:
    clf_rbf = svm.SVC(kernel='rbf', C=c)

    t0 = time()
    clf_rbf.fit(features_train_reduced, labels_train_reduced)
    pred = clf_rbf.predict(features_test)
    accuracy = accuracy_score(pred, labels_test)
    print 'Rbf kernel with 1% of the data and C = ', c, ' - accuracy ', accuracy
    print "Fit and prediction time:", round(time()-t0, 3), "s"

# L3Q35 - Using C=10000 try the full database

clf_rbf = svm.SVC(kernel='rbf', C=10000.0)

t0 = time()
clf_rbf.fit(features_train, labels_train)
pred = clf_rbf.predict(features_test)
accuracy = accuracy_score(pred, labels_test)
print 'Rbf kernel and C=10000 - accuracy ', accuracy
print "Fit and prediction time:", round(time()-t0, 3), "s"  

# L3Q36 - Class values for 10, 26 and 50

clf_rbf = svm.SVC(kernel='rbf', C=10000.0)

t0 = time()
clf_rbf.fit(features_train_reduced, labels_train_reduced)
pred_reduced = clf_rbf.predict(features_test)
print 'Class values for 10, 26 and 50'
print pred_reduced[10], pred_reduced[26], pred_reduced[50]

# L3Q37 - There are over 1700 test events--how many are predicted 
# to be in the “Chris” (1) class? (Use the RBF kernel, C=10000., 
# and the full training set.)

print 'Prediction length: ', len(pred)
print 'Predictions for Chris(1)', len([a for a in pred if a == 1])
#########################################################


