# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 12:25:42 2020

@author: Prashastha Mudannayake
"""

from csv import reader
#from math import sqrt
 
# Load a CSV file
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

# String column --> Float
def str_col_to_float(dataset, col):
    for row in dataset:
        row[col] = float(row[col].strip())
        
# String column --> Integer
def str_col_to_int(dataset, col):
    class_vals = [row[col] for row in dataset]
    class_set = set(class_vals) #to get unique class vals
    lookup = dict()
    for i, val in enumerate(class_set):
        lookup[val] = i
        print('[%s] => %d' % (val, i))
    for row in dataset:
        row[col] = lookup[row[col]] #dict not callable
    return lookup    
        
data = load_csv('iris.csv')
str_col_to_float(data, 0)
str_col_to_float(data, 1)
str_col_to_float(data, 2)
str_col_to_float(data, 3)
str_col_to_int(data, 4)
print(data)