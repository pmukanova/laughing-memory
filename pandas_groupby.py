import pandas as pd
import contextily
import matplotlib.pyplot as plt
import geopandas

# Read the restaurants csv file
restaurants = pd.read_csv("//Users/perizatmenard/Documents/advanced_python/laughing-memory/data/paris/paris_restaurants.csv")

# Load the restaurants data
restaurants = geopandas.read_file("paris_restaurants.geosjon")

# Calculate the number of restaurants of each type
type_counts = restaurants.groupby(restaurants["type"]).size()

# Print the result
print(type_counts)