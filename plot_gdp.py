# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 13:48:59 2023

@author: nadam
"""

#-----------------------------------------------------------------------------------------------------------#
#In this analysis, we will be examining the evolution of GDP growth rate for selected North African countries 
#with a base year of 2014. Specifically, we will focus on Algeria, Egypt, Morocco, Libya, and Tunisia. 
#GDP growth rate is a key indicator of economic growth, and its evolution provides insight into the overall 
#health and trajectory of a country's economy. 
#Economic growth has been a topic of interest to researchers and economists for centuries, 
#and various theories and models have been developed to explain the determinants of growth. 
#However, there is still no consensus on the key factors that foster growth. 
#Therefore, our aim in this analysis is to offer our point of view on the main factors that influence economic 
#growth and how they have evolved over time. 
#-----------------------------------------------------------------------------------------------------------#

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%%

##Reading and cleaning the data
# Load the data into a pandas dataframe
df = pd.read_csv("economy_and_growth_north_africa.csv")
# Rename the "Egypt, Arab Rep." row to "Egypt"
df.loc[df["Country Name"] == "Egypt, Arab Rep.", "Country Name"] = "Egypt"
# Filter the dataframe to only include GDP growth (annual %) data
#The indicator code of NY.GDP.PCAP.KD.ZG referes to GDP per capita growth
df = df[(df['Indicator Code'] == 'NY.GDP.PCAP.KD.ZG') & (df['Year'] >= 2014)]
# Pivot the dataframe so that each country is a column and each year is a row
df = pd.pivot_table(df, values='Value', index='Year', columns='Country Name')
# Normalize the data to the base year of 2014
df = df / df.loc[2014]

#%%
# Plot the data: GDP growth Rate
fig, ax = plt.subplots()
for col in df.columns:
    plt.plot(df[col], label=col)
ax.set_title('GDP per capita growth (Base year = 2014)')
ax.set_xlabel('Year')
ax.set_ylabel('annual (%)')
plt.legend()
plt.tight_layout()
plt.savefig('gdp_north_africa.png', dpi=300)
plt.show()
