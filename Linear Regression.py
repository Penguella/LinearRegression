
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
import seaborn as sns
#Specifying size of the figure.
plt.figure(figsize=(15, 10))

#Reading data from a csv file using Pandas module.
data = pd.read_csv("Cars_India_dataset.csv")

#Fetching the values from the csv file to create an object of Independent and Dependent variable.
X = data['Fuel Efficiency'].values
Y = data['Displacement'].values

plt.scatter(X,Y,color='blue',label="Scatter Plot of Variables")
#plt.plot(X,Y,color='red',label="Regression Line")
sns.regplot(X,Y)
plt.xlabel("Fuel Efficiency")
plt.ylabel("Displacement")

plt.legend()
plt.show()






