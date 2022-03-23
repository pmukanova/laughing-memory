# Import GeoPandas
import geopandas
import pandas as pd
import matplotlib.pyplot as plt

# Read the restaurants csv file
districts = geopandas.read_file("//Users/perizatmenard/Documents/advanced_python/laughing-memory/data/paris/paris_districts.gpkg")


# Inspect the first rows
print(districts.head())

# Make a quick visualization of the districts
districts.plot()
plt.show()

# Check what kind of object districts is
print(type(districts))

# Check the type of the geometry attribute
print(type(districts.geometry))

# Inspect the first rows of the geometry
print(districts.geometry.head())

# Inspect the area of the districts
print(districts.geometry.area)