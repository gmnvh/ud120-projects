#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

'''
L6Q13 - How many data points (people) are in the Enron ?
'''
print 'Number of people: ', len(enron_data)

'''
L6Q14 - For each person, how many features are available ?
'''

# Get first element and check number of features
first = enron_data.keys()[0]
features = len(enron_data[first])

# Check if everybody has the same number of features than the first one
for person in enron_data:
    if len(enron_data[person]) != features:
        print person, 'has different size of features'

print 'Number of features is: ', features

'''
L6Q15 -  How many POIs are there in the E+F dataset?
'''
number_of_poi = 0
for person in enron_data:
    if enron_data[person]["poi"] == 1:
        number_of_poi += 1
        
print 'Number of poi in the E+F database is: ', number_of_poi

'''
L6Q16 -  How many POIs are there in the file poi_names.txt ?
'''
file_poi_names = ["Lay Kenneth", "Skilling Jeffrey", "Howard Kevin", "Krautz Michael",
             "Yeager Scott", "Hirko Joseph", "Shelby Rex", "Bermingham David",
             "Darby Giles", "Mulgrew Gary", "Bayley Daniel", "Brown James",
             "Furst Robert", "Fuhs William", "Causey Richard", "Calger Christopher",
             "DeSpain Timothy", "Hannon Kevin", "Koenig Mark", "Forney John",
             "Rice Kenneth", "Rieker Paula", "Fastow Lea", "Fastow Andrew",
             "Delainey David", "Glisan Ben", "Richter Jeffrey", "Lawyer Larry",
             "Belden Timothy", "Kopper Michael", "Duncan David", "Bowen Raymond",
             "Colwell Wesley", "Boyle Dan", "Loehr Christopher"]
           
print 'Number of POI in the file is: ', len(file_poi_names)

'''
L6Q18 -  What is the total value of the stock belonging to James Prentice?
'''

# Print name of the features
first = enron_data.keys()[0]
print "Feature names are"
for features in enron_data[first]:
    print features

print "Stocks for James Prentice are ", enron_data["PRENTICE JAMES"]["total_stock_value"]
        
'''
L6Q19 -  How many email messages do we have from Wesley Colwell to persons of interest?
'''
print "E-mails to POI from Wesley Colwell were ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

'''
L6Q20 -  What’s the value of stock options exercised by Jeffrey K Skilling?
'''
print "Stock options for Jeffrey K Skilling is", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

'''
L6Q34 - Of these three individuals (Lay, Skilling and Fastow), who took home the most money (largest value of “total_payments” feature)?

How much money did that person get?
'''
ind = ["LAY KENNETH L", "SKILLING JEFFREY K", "FASTOW ANDREW S"]

for person in ind:
    print person, " took ", "${:0,.0f}".format(enron_data[person]["total_payments"])
    
'''
L6Q26 - How is an unfilled feature denoted?
'''
for person in enron_data:
    print enron_data[person]["total_payments"]
    
'''
L6Q27 - How many folks in this dataset have a quantified salary? What about a known email address?
'''
folks_with_salary = 0

for person in enron_data:
    salary = enron_data[person]["salary"]
    if salary != "NaN":
        folks_with_salary += 1
print "Folks with salary: ", folks_with_salary

folks_with_email = 0

for person in enron_data:
    email = enron_data[person]["email_address"]
    if email != "NaN":
        folks_with_email += 1
print "Folks with email: ", folks_with_email 

'''
L6Q29 - What percentage of people in the dataset have NaN for their total payments?
'''
people_without = 0
people_total = 0

for person in enron_data:
    payments = enron_data[person]["total_payments"]
    people_total += 1
    if payments == "NaN":
        people_without += 1
        
print "People with NaN as total payments is ", people_without, " : " , 100*(float(people_without)/float(people_total)), "%"

'''
L6Q30 - What percentage of POI in the dataset have NaN for their total payments?
'''
people_without = 0
people_total = 0

for person in enron_data:
    poi = enron_data[person]["poi"]
    payments = enron_data[person]["total_payments"]
    people_total += 1
    if poi == True and payments == "NaN":
        people_without += 1
        
print "POI with NaN as total payments is ", people_without, "against ", people_total, " people"
