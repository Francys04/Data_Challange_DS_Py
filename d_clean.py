import pandas as pd
import os
import xlrd


"""Concatenate all 10 datasets"""
# current work directory
path = os.getcwd()

#show all files
files = os.listdir(path)
print(files)

files_needed = ['dataframe_albuquerque.xlsx',
                'dataframe_colorado.xlsx',
                'dataframe_indianapolis.xlsx',
                'dataframe_las_vegas.xlsx',
                'dataframe_miami.xlsx',
                'dataframe_new_york.xlsx',
                'dataframe_philadelphia.xlsx',
                'dataframe_san_diego.xlsx',
                'dataframe_san_francisco.xlsx',
                'dataframe_washington.xlsx'
                ]

# initialize dataframe
df_combined = pd.DataFrame()

for f in files_needed:
    df_combined = df_combined.append(pd.read_excel(f,'Sheet1'))
print(df_combined)

