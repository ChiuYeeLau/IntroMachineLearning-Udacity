#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

poi_num = 0

for key in enron_data:
	if enron_data [key]['poi'] == True:
		poi_num += 1

# print poi_num

# print enron_data ['PRENTICE JAMES']

# print enron_data ['Colwell Wesley'.upper()]

'''
for key in enron_data:
	if 'Skilling Jeffrey'.upper () in key:
		print key
		print enron_data [key]

for key in enron_data:
	if 'Skilling Jeffrey'.upper () in key:
		print key
		print enron_data [key]['total_payments']
	if 'Lay Kenneth'.upper () in key:
		print key
		print enron_data [key]['total_payments']
	if 'Fastow Andrew'.upper () in key:
		print key
		print enron_data [key]['total_payments']

'''

nan_poi = 0
nan_poi_nan = 0
nan_pay = 0

import numpy

for key in enron_data:
	if enron_data [key]['poi'] == True:
		nan_poi += 1
	if enron_data [key]['total_payments'] == 'NaN':
		nan_pay += 1
	if enron_data [key]['poi'] == True and enron_data [key]['total_payments'] == 'NaN':
		nan_poi_nan += 1

print nan_poi_nan * 1.0/nan_poi
print nan_poi
print nan_poi_nan
print nan_pay
