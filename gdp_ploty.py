# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 10:32:04 2023

@author: nadam
"""

import pandas as pd

# Load the data from the Excel file
north_africa_gdp = pd.read_excel('north_africa_gdp.xlsx')

# Keep only the relevant indicators
relevant_indicators = ['GDP (current US$)', 'GDP growth (annual %)', 'GDP per capita (current US$)']


# Filter the data to only include the three indicators of interest
gdp_data = north_africa_gdp.loc[north_africa_gdp['Indicator Name'].isin(relevant_indicators)]


#The .loc method is used to select specific rows and columns from a Pandas DataFrame using labels. 
#It allows you to filter the data in a DataFrame based on the values in the columns or index.
#For example, in the code you provided, the .loc method is used to select rows from the north_africa_gdp 
#DataFrame where the Indicator Name column matches one of the indicators in the relevant_indicators list.
#The resulting DataFrame gdp_data will only include rows where the Indicator Name is one of the three 
#indicators of interest, and can be used for further data analysis or manipulation.


# Group the data by Indicator Name and Year
grouped_data = gdp_data.groupby(['Indicator Name', 'Year'], as_index=False)['Value'].mean()

# Unstack the Year column to have each year in a different column
unstacked_data = grouped_data.set_index(['Indicator Name', 'Year'])['Value'].unstack()

# Reset the index to have the three indicators as rows again
final_data = unstacked_data.reset_index()

# Show the final data
print(final_data)