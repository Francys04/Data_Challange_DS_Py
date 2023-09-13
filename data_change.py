"""Rename price column and update existing dataframe"""
from d_clean import df_combined3
import pandas as pd

df_c_change = df_combined3.rename(columns={'Price': 'Price($)'})
print(df_c_change)

# price data: cut '$' in price
df_c_change['Price($)'] = df_c_change['Price($)'].str.strip('$')
print(df_c_change)

# price data: cut ',' in price
df_c_change['Price($)'] = df_c_change['Price($)'].str.replace(',', '')
print(df_c_change)

"""Change area column"""
df_c_change = df_c_change.rename(columns={'Area': 'Area(Sqft)'})
print(df_c_change)

# area data: cut 'sqft' string element
df_c_change['Area(Sqft)'] = df_c_change['Area(Sqft)'].str.strip(' sqft')
print(df_c_change)

# area data: cut',' string element
df_c_change['Area(Sqft)'] = df_c_change['Area(Sqft)'].str.replace(',', '')
print(df_c_change)

"""Bedrooms data: cut 'Beds' str elements"""
df_c_change['Bedrooms'] = df_c_change['Bedrooms'].str.strip(' Beds')
print(df_c_change)

df_c_change['Bedrooms'].value_counts()

# bedrooms data: "Studio" = 1 room
# this line of code replace Studio with '1', if we have 3 bedrooms is not a studio and remain the initail int
df_c_change['Bedrooms'] = df_c_change['Bedrooms'].apply(lambda x: 1 if 'Studio' in x else x)
print(df_c_change)

# verify if we have some data which not need it
if 'Studio' in df_c_change.values:
    print('Element is in the dataframe')

"""Bathrooms Data: Cut 'Bath' string element"""
df_c_change['Bathrooms'] = df_c_change['Bathrooms'].str.strip(' Ba')
print(df_c_change)

"""Parking data: y/n"""
# verify count of parking data
df_c_change['Parking'].value_counts()

# verify if y/n parking
df_c_change['Parking'] = df_c_change['Parking'].apply(
    lambda x: 'yes' if 'Garage' in x or 'Carport' in x or 'Car' in x or 'Open' in x
    else 'no')
df_c_change['Parking'].value_counts()

df_c_change
# %%
df_c_change['Price($)'] = df_c_change['Price($)'].str.replace(',', '')
print(df_c_change)