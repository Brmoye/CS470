# Brian Moye
# CS470
# September 19, 2022
# Assignment 6
# Much of this code was taken from examples provided by Dr. Terwilliger

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
from sklearn import linear_model 
from utilities import visualize_classifier

inputFile = 'roster.csv'
title = "HS GPA and Math ACT"

# Create label encoder
encoder = preprocessing.LabelEncoder()

# Read data from file and convert to numpy array
data = pd.read_csv(inputFile).to_numpy()
# Store only desired values
X, y = data[:, 3:-1], data[:, -1]

input_labels = ['A', 'B', 'C', 'D', 'F']

# Fit the labels
encoder.fit(input_labels)
encoded_values = encoder.transform(y)

# Create the logistic regression classifier
classifier = linear_model.LogisticRegression(solver='liblinear', C=100)

# Train the classifier
classifier.fit(X, encoded_values)

# Visualize the performance of the classifier 
visualize_classifier(classifier, X, encoded_values, title)  # type: ignore
