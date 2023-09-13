from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
from data_change import df_c_change

"""Convert all numbers to integers"""
# Bedrooms
# check if column is a numeric element
is_numeric_dtype(df_c_change['Bedrooms'])  # False

# check if column is a str element
is_string_dtype(df_c_change['Bedrooms'])  # True
# convert
df_c_change['Bedrooms'] = df_c_change['Bedrooms'].astype(int)

# Bathrooms
# check if column is a numeric element
is_numeric_dtype(df_c_change['Bathrooms'])  # False

# check if column is a str element
is_string_dtype(df_c_change['Bathrooms'])  # True

# convert
# df_c_change['Bathrooms'] = df_c_change['Bathrooms'].astype(int) # error int() with base 10: '3 Ba'
# solve
# df_c_change['Bathrooms'] = df_c_change['Bathrooms'].apply(lambda x: 0 if '' in x else x)
# df_c_change['Bathrooms'] = df_c_change['Bathrooms'].astype(int)
is_numeric_dtype(df_c_change['Bathrooms'])  # True

# Area sqft
# check if column is a numeric element
is_numeric_dtype(df_c_change['Area(Sqft)'])  # False

# check if column is a str element
is_string_dtype(df_c_change['Area(Sqft)'])  # True
# convert
df_c_change['Area(Sqft)'] = df_c_change['Area(Sqft)'].astype(int)
is_numeric_dtype(df_c_change['Area(Sqft)'])  # True

# Year build
# check if column is a numeric element
# is_numeric_dtype(df_c_change['Year Built']) # False

# check if column is a str element
# is_string_dtype(df_c_change['Year Built']) # True
# convert
# df_c_change['Year Built'] = df_c_change['Year Built'].astype(int)
# is_numeric_dtype(df_c_change['Year Built'])

# we have error year build == no info
# df_c_change[df_c_change['Year Built'] == 'No Info']

# solve this error
# df_c_change['Year Built'] = df_c_change['Year Built'].apply(lambda x: 0 if 'No Info' in x else x) # float error


# save in str
# df_c_change['Year Built'] = df_c_change['Year Built'].astype(str)
# df_c_change['Year Built'] = df_c_change['Year Built'].astype(int)
is_numeric_dtype(df_c_change['Year Built'])  # True
# df_c_change['Year Built'].value_counts()
# transform float in int
# df_c_change['Year Built'] = df_c_change['Year Built'].apply(lambda x: x.replace('.0', '') if '.0' in x else x)

# verify if we have '.0' float in data
# df_c_change['Year Built'].value_counts()

df_c_change

"""Price in $"""
is_numeric_dtype(df_c_change['Price($)'])  # False

# convert
# df_c_change['Price($)'] = df_c_change['Price($)'].astype(int)
# error invalid literal for int() with base 10: '330.000'

# df_c_change['Price($)'] = df_c_change['Price($)'].apply(lambda x: x.replace('.', '') if '.' in x else x)
# df_c_change['Price($)'] = df_c_change['Price($)'].astype(int)
# invalid literal for int() with base 10: '294900+'

# df_c_change['Price($)'] = df_c_change['Price($)'].apply(lambda x: x.replace('+', '') if '+' in x else x)
# df_c_change['Price($)'] = df_c_change['Price($)'].astype(int)

is_numeric_dtype(df_c_change['Price($)'])  # True

# """Craete new price/sqft"""
# df_c_change['price/sqft'] = df_c_change['Price($)'] / df_c_change['Area(Sqft)']
#
# df_c_change['price/sqft'] = df_c_change['price/sqft'].round(2)
# df_c_change

"""Save dataframe in Excell"""
# df_c_change.to_excel('cleaned_data.xlsx', index=False)
# %%

#%%
