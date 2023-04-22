# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 14:59:53 2023

@author: nadam
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the Excel file
gdp_indicators = pd.read_excel('gdp_indicators.xlsx')

# Filter the data to only include GDP per capita values
gdp_data = gdp_indicators[gdp_indicators['Indicator Name'] == 'GDP (current US$)']

# Pivot the data to have years as columns and countries as rows
gdp_pivot = gdp_data.pivot(index='Country Name', columns='Year', values='Value')

# Plot the data using a five-way plot
gdp_pivot.plot(subplots=True, layout=(1, 5), figsize=(20, 5))

# Set the titles for the plot
fig = plt.gcf()
fig.suptitle('GDP per capita', fontsize=16)
for i, ax in enumerate(fig.axes):
    ax.set_title(gdp_pivot.index[i])
    
# Show the plot
plt.show()

