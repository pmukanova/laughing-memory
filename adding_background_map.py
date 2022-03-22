import pandas as pd
import contextily
import matplotlib.pyplot as plt

# Read the restaurants csv file
restaurants = pd.read_csv("//Users/perizatmenard/Documents/advanced_python/laughing-memory/data/paris/paris_restaurants.csv")

# Import contextily


# A figure of all restaurants with background
fig, ax = plt.subplots()
ax.plot(restaurants["x"], restaurants["y"], 'o', markersize=1)
contextily.add_basemap(ax)
plt.show()