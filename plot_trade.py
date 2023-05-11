# -*- coding: utf-8 -*-
"""
Created on Thu May 11 12:28:09 2023

@author: nadam
"""

#Economic data: Trade

#--------------------------------------------------------------------------------------------------------------#
#One of the most important variables is trade, as numerous studies have shown that countries with open economies
#tend to have higher per capita GDP and faster growth rates. Trade determinants such as exports, imports, 
#and openness have been found to have a direct and positive influence on economic growth. 
#--------------------------------------------------------------------------------------------------------------#

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("economy_and_growth_north_africa.csv")
# Rename the "Egypt, Arab Rep." row to "Egypt"
df.loc[df["Country Name"] == "Egypt, Arab Rep.", "Country Name"] = "Egypt"

# Filter the data to include only the desired indicators and countries
indicators = ['NE.EXP.GNFS.CD', 'NE.IMP.GNFS.CD']
# NE.EXP.GNFS.CD refers to Exports of goods and services (current US$)
# NE.IMP.GNFS.CD refers to Imports of goods and services (current US$)

countries = ['Algeria', 'Egypt', 'Libya', 'Morocco', 'Tunisia']
df_filtered = df[df['Indicator Code'].isin(indicators) & df['Country Name'].isin(countries)]

# Pivot the data to create separate columns for exports and imports
df_pivot = df_filtered.pivot_table(index=['Country Name', 'Year'], columns='Indicator Name', values='Value').reset_index()

# Calculate the trade balance as the difference between exports and imports
df_pivot['Trade Balance'] = df_pivot['Exports of goods and services (current US$)'] - df_pivot['Imports of goods and services (current US$)']

# Loop through the countries and create a separate graph for each one
for country in countries:
    # Filter the data for the current country
    df_country = df_pivot[df_pivot['Country Name'] == country]
    
    # Create the graph
    plt.plot(df_country['Year'], df_country['Exports of goods and services (current US$)'], color='darkblue', label='Exports')
    plt.plot(df_country['Year'], df_country['Imports of goods and services (current US$)'], color='darkred', label='Imports')
    plt.title(f'Trade balance for {country}')
    plt.xlabel('Year')
    plt.ylabel('Amount (current US$)')
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'{country}_balance_trade.png', dpi=300)
    plt.show()
