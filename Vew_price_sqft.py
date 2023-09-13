from convert_num_int import df_c_change

"""Create new column price/sqft"""

df_c_change['price/sqft'] = df_c_change['Price($)']//df_c_change['Area(Sqft)']






#%%
df_c_change['price/sqft'] = df_c_change['Price($)']//df_c_change['Area(Sqft)']
