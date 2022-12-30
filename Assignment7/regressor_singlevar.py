# Brian Moye
# CS470 - Assignment 7
# September 27, 2022
# Most of the code was provided by Dr. Terwilliger with some few modifications made by me.

import numpy as np
from sklearn import linear_model
import sklearn.metrics as sm
import matplotlib.pyplot as plt
import pandas as pd

# Input file containing data
input_file = 'MLB2018-19-1.csv' 

# Read data
data = pd.read_csv(input_file).to_numpy()

# BA vs Wins
#X, y = data[:, 1:2], data[:, -1]

# OPS vs Wins
#X, y = data[:, 2:3], data[:, -1]

# ERA vs Wins
#X, y = data[:, 3:4], data[:, -1]

# WHIP vs Wins
X, y = data[:, 4:5], data[:, -1]

# Train and test split
num_training = int(0.5 * len(X))
num_test = len(X) - num_training

# Training data
X_train, y_train = X[:num_training], y[:num_training]

# Test data
X_test, y_test = X[num_training:], y[num_training:]

# Create linear regressor object
regressor = linear_model.LinearRegression()

# Train the model using the training sets
regressor.fit(X_train, y_train)

# Predict the output
y_test_pred = regressor.predict(X_test)

# Plot outputs
plt.scatter(X_test, y_test, color='green')
plt.plot(X_test, y_test_pred, color='black', linewidth=4)
plt.xticks(())
plt.yticks(())
plt.show()

# Compute performance metrics
print("Linear regressor performance:")
print("Mean absolute error =", round(sm.mean_absolute_error(y_test, y_test_pred), 2))
print("Mean squared error =", round(sm.mean_squared_error(y_test, y_test_pred), 2)) 
print("Median absolute error =", round(sm.median_absolute_error(y_test, y_test_pred), 2)) 
print("Explain variance score =", round(sm.explained_variance_score(y_test, y_test_pred), 2))  # type: ignore
print("R2 score =", round(sm.r2_score(y_test, y_test_pred), 2))    # type: ignore
