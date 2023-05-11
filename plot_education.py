# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 20:22:02 2023

@author: nadam
"""

#Non-economic data: Education
#We are going to analyze the effect of education utilizing the Barro-lee metric on the GDP growth.
#This data represents the average years of total schooling for individuals aged 25 and above in 
#four North African countries: Tunisia, Egypt, Libya, and Algeria. 

import pandas as pd
import matplotlib.pyplot as plt

# Load education dataset
edu_df = pd.read_csv("education_north_africa.csv")

# Filter for Barro-Lee indicator for total years of schooling among population 25+
edu_bl_df = edu_df[edu_df['Indicator Code'] == 'BAR.SCHL.25UP']

#%%
#Evolution of the average schooling years: Barro-Lee indicator
#The idea that education has a positive effect on economic growth is known as the "human capital theory." 
#The basic premise is that education and training make workers more productive, leading to increased economic 
#output and growth.
#We will need to reorganoize our data set since it is sectioned as follows
#--------------#------------------------
#   Column 1   # Country Name
#--------------#------------------------
#   Column 2   # Country ISO3
#--------------#------------------------
#   Column 3   # Year
#--------------#------------------------
#   Column 4   # Indicator Name
#--------------#------------------------
#   Column 5   # Indicator Code
#--------------#------------------------
#   Column 6   # Value

# Pivot the dataframe to put each country in a separate column
pivot_df = edu_bl_df.pivot_table(index=['Country Name', 'Year'], columns='Indicator Code', values='Value').reset_index()

#the final dataframe pivot_df  will have one row for each unique combination of country name and year, 
#with a column for each unique indicator code.

# Set the 'Year' column as the x-axis and plot each country's BL average years of schooling over time
fig, ax = plt.subplots()
for country in pivot_df['Country Name'].unique():
    country_df = pivot_df[pivot_df['Country Name'] == country]
    ax.plot(country_df['Year'], country_df['BAR.SCHL.25UP'], label=country)

# Add legend and title to the plot
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel("Year")
ax.set_ylabel("BL Average Years of Schooling, \nAge 25+, Total")
ax.set_title("Evolution of Barro-Lee Indicator \nfor North African Countries")

# Set tight layout and save the figure
plt.tight_layout()
plt.savefig("barro_lee_indicator.png", dpi=300)
# Show the plot
plt.show()

#%%

#We are goig now to create a scatter plot that displays the relationship between two variables 
#for North African countries: the Barro Lee indicator "BL average years of schooling, age 25+, total" 
#and the GDP growth rate.

#Creating a scatter plot 
# Load economy and growth dataset
econ_df = pd.read_csv("economy_and_growth_north_africa.csv")

# Merge education and economy datasets on country name, year, and ISO3 code
merged_df = pd.merge(edu_bl_df, econ_df, on=['Country Name', 'Country ISO3', 'Year'])

# Create scatter plot with BL average years of schooling on x-axis and GDP growth rate on y-axis
plt.scatter(merged_df['Value_x'], merged_df['Value_y'])

# Add labels and title to plot
plt.xlabel("BL Average Years of Schooling, Age 25+, Total")
plt.ylabel("GDP Growth Rate")
plt.title("Relationship between Education \nand Economic Growth in North Africa")

# # Set tight layout and save the figure
plt.tight_layout()
plt.savefig("Relationship between Education and Economic Growth in North Africa.png", dpi=300)
# Show plot
plt.show()
