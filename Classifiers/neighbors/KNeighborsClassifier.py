"""
Created on Sat Dec 12 22:33:30 2020

@author: Prashastha Mudannayake
"""

# Step of creating a classifier
# 1. Calculate Euclidean Distance
# 2. Get neareast neighbors
# 3. Make a prediction

from math import sqrt

# Step1: Function to calculate Euclidean distance between 2 vects
def euclidean_dist(row1, row2):
    dist = 0.0
    for i in range(len(row1) - 1):
        dist += (row2[i] - row1[i])**2
    return sqrt(dist)    

# Step2: Locate most similar neighbors
def get_neighbors(train, test_row, n_neighbors):
    distL = list()
    for train_row in train:
        dist = euclidean_dist(train_row, test_row)
        distL.append((train_row, dist))
    distL.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(n_neighbors):
        neighbors.append(distL[i][0])
    return neighbors    
    
# Step 3: Makclassification prediction with neighbors
def predict_class(train, test_row, n_neighbors):
    neighbors = get_neighbors(train, test_row, n_neighbors)
    output_vals = [row[-1] for row in neighbors]
    prediction = max(set(output_vals), key=output_vals.count)
    return prediction

dataset = [[2.7810836,2.550537003,1],
 	[1.465489372,2.362125076,0],
 	[3.396561688,4.400293529,0],
 	[1.38807019,1.850220317,0],
 	[3.06407232,3.005305973,0],
 	[7.627531214,2.759262235,1],
 	[5.332441248,2.088626775,1],
 	[6.922596716,1.77106367,1],
 	[8.675418651,-0.242068655,1],
 	[7.673756466,3.508563011,1]]

prediction = predict_class(dataset, dataset[5], 3)
print('Expected %d, Predicted %d' % (dataset[5][-1], prediction))