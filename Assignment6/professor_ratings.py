# Brian Moye
# CS470
# September 19, 2022
# Assignment 6
# Much of this code was taken from examples provided by Dr. Terwilliger

import matplotlib.pyplot as plt
import pandas as pd

inputFile = 'ratings.csv'

data = pd.read_csv(inputFile, names=["Professor", "Score"], index_col=0)

data.plot.bar(title="Professor Ratings")
plt.show()