# Brian Moye
# CS470 - Assignment 7
# September 27, 2022
# Most of the code was provided by Dr. Terwilliger with some few modifications made by me.

import numpy as np
from sklearn import linear_model
import sklearn.metrics as sm
import pandas as pd

# Put the training and testing into a function so I could see all the results together.
def train_and_test(X, y):
    # Split data into training and testing 
    num_training = int(0.5 * len(X))
    num_test = len(X) - num_training

    # Training data
    X_train, y_train = X[:num_training], y[:num_training]

    # Test data
    X_test, y_test = X[num_training:], y[num_training:]

    # Create the linear regressor model
    linear_regressor = linear_model.LinearRegression()

    # Train the model using the training sets
    linear_regressor.fit(X_train, y_train)

    # Predict the output
    y_test_pred = linear_regressor.predict(X_test)

    # Measure performance
    print("Linear Regressor performance:")
    print("Mean absolute error =", round(sm.mean_absolute_error(y_test, y_test_pred), 2))
    print("Mean squared error =", round(sm.mean_squared_error(y_test, y_test_pred), 2))
    print("Median absolute error =", round(sm.median_absolute_error(y_test, y_test_pred), 2))
    print("Explained variance score =", round(sm.explained_variance_score(y_test, y_test_pred), 2))  # type: ignore
    print("R2 score =", round(sm.r2_score(y_test, y_test_pred), 2))  # type: ignore
    print()

def main():
    # Input file containing data
    input_file = 'MLB2018-19-1.csv' 

    # Read data
    data = pd.read_csv(input_file).to_numpy()

    # BA && OPS vs Wins
    X, y = data[:, 1:3], data[:, -1]
    print("BA && OPS vs Wins:")
    train_and_test(X, y)
    
    # BA && ERA vs Wins
    X, y = data[:, 1:4:2], data[:, -1]
    print("BA && ERA vs Wins:")
    train_and_test(X, y)
    
    # BA && WHIP vs Wins
    X, y = data[:, 1:5:3], data[:, -1]
    print("BA && WHIP vs Wins:")
    train_and_test(X, y)
    
    # OPS && ERA vs Wins
    X, y = data[:, 2:4], data[:, -1]
    print("OPS && ERA vs Wins:")
    train_and_test(X, y)
    
     # OPS && WHIP vs Wins
    X, y = data[:, 2:5:2], data[:, -1]
    print("OPS && WHIP vs Wins:")
    train_and_test(X, y)

    # ERA && WHIP vs Wins
    X, y = data[:, 3:5], data[:, -1]
    print("ERA && WHIP vs Wins:")
    train_and_test(X, y)
    
    # BA && OPS && ERA && WHIP vs Wins
    X, y = data[:, 1:5], data[:, -1]
    print("BA && OPS && ERA && WHIP vs Wins:")
    train_and_test(X, y)
    
main()