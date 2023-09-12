import pandas as pd
import os
import xlrd
import seaborn as sns

"""Concatenate all 10 datasets"""
# current work directory
path = os.getcwd()

# show all files
files = os.listdir(path)
print(files)

files_needed = ['dataframe/dataframe_albuquerque.xlsx',
                'dataframe/dataframe_colorado.xlsx',
                'dataframe/dataframe_indianapolis.xlsx',
                'dataframe/dataframe_las_vegas.xlsx',
                'dataframe/dataframe_miami.xlsx',
                'dataframe/dataframe_new_york.xlsx',
                'dataframe/dataframe_philadelphia.xlsx',
                'dataframe/dataframe_san_diego.xlsx',
                'dataframe/dataframe_san_francisco.xlsx',
                'dataframe/dataframe_washington.xlsx'
                ]

# initialize dataframe
df_combined = pd.DataFrame()

for f in files_needed:
    df_combined = df_combined.append(pd.read_excel(f, 'Sheet1'))
print(df_combined)


"""Data cleaning"""
# Check for missing data
df_combined.info()

# check for at leas one missing value in row
print(df_combined[df_combined.isna().any(axis=1)])

df_combined1 = df_combined.dropna()
df_combined1.info()

sns.heatmap(df_combined1.isna(), yticklabels=False, cbar=False, cmap='BuPu')

df_combined2 = df_combined1.reset_index(drop=True)
print(df_combined2)

"""Check for outliers and doubles"""

print(f'Check for outliers and doubles: {df_combined2.duplicated().sum()}')

print(df_combined2.loc[df_combined2.duplicated(), :])

# drop all duplicate results
df_combines_drop = df_combined2.drop_duplicates()
print(df_combines_drop)

df_combined3 = df_combines_drop.reset_index(drop=True)
print(df_combined3)


#%%
