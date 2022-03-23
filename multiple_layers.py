import pandas as pd
import contextily
import matplotlib.pyplot as plt
import geopandas

# Read the restaurants csv file
restaurants = pd.read_csv("//Users/perizatmenard/Documents/advanced_python/laughing-memory/data/paris/paris_restaurants.csv")

# Load the restaurants dataset
restaurants = geopandas.read_file("paris_restaurants.geosjon")

# Take a subset of the African restaurants
african_restaurants = restaurants[restaurants['type'] == 'African restaurant']

# Make a multi-layered plot
fig, ax = plt.subplots(figsize=(10, 10))
restaurants.plot(ax=ax, color='grey')
african_restaurants.plot(ax=ax, color='red')
# Remove the box, ticks and labels
ax.set_axis_off()
plt.show()