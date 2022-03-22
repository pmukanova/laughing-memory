# Import pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read the restaurants csv file
restaurants = pd.read_csv("//Users/perizatmenard/Documents/advanced_python/laughing-memory/data/paris/paris_restaurants.csv")

# Inspect the first rows of restaurants
print(restaurants.head())

# Make a plot of all points
fig, ax = plt.subplots()
ax.plot(restaurants['x'], restaurants['y'], 'o')
plt.show()
