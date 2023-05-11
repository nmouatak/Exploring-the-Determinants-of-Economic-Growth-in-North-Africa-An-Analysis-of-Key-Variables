# -*- coding: utf-8 -*-
"""
Created on Thu May 11 12:36:50 2023

@author: nadam
"""


#Economic data: Foreign Direct Investment

#--------------------------------------------------------------------------------------------------------------#
#FDI is another important variable that has been found to have a direct and positive impact on economic growth, 
#particularly in developing countries. FDI inflows can bring in new technology and know-how, 
#leading to positive externalities and productivity gains. While there may be some contradictions 
#in the literature regarding the relationship between trade and growth, overall, these variables play a 
#significant role in determining the rate and trajectory of economic growth.
#--------------------------------------------------------------------------------------------------------------#

import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a pandas dataframe
df = pd.read_csv('economy_and_growth_north_africa.csv')
# Rename the "Egypt, Arab Rep." row to "Egypt"
df.loc[df["Country Name"] == "Egypt, Arab Rep.", "Country Name"] = "Egypt"

# Filter the data to include only FDI and countries in North Africa for the years 2001, 2011 and 2021
indicator_code = 'BX.KLT.DINV.CD.WD'
# Define the countries and years of interest
countries = ['Algeria', 'Egypt', 'Libya', 'Morocco', 'Tunisia']
years = [2001, 2011, 2021]

df_filtered = df[df['Indicator Code'] == indicator_code]
df_filtered = df_filtered[df_filtered['Country Name'].isin(countries)]

# Pivot the data to create separate columns for each year
df_pivot = df_filtered.pivot_table(index=['Country Name', 'Country ISO3'], columns='Year', values='Value').reset_index()

# Set the country name as the index
df_pivot = df_pivot.set_index('Country Name')
df_pivot = df_pivot.sort_values(2021)
#%%

# Define colors for positive and negative values
colors = {'positive': 'green', 'negative': 'red'}
#the color of the bars in the bar graphs are based on whether the values are positive or negative.

# Plot the horizontal bar graphs for each year
for year in years:
    ax = df_pivot.plot(kind='barh', y=year, figsize=(10,5), color=[colors['positive' if val >= 0 else 'negative'] for val in df_pivot[year]])
    ax.set_xlabel('FDI Inflows (Billion US$)')
    ax.set_ylabel('Country Name')
    ax.set_title(f'FDI Inflows in {year}')
    plt.tight_layout()
    plt.savefig(f'FDI_inflows_country_{year}.png', dpi=300)
    plt.show()
