"""Import, Output dataset & PostgreSQL"""
import pandas as pd
import psycopg2

from sqlalchemy import create_engine
import matplotlib.pyplot as plt


# output data

real_estate_df = pd.read_excel('cleaned_data.xlsx')

real_estate_df.info()

"""PostgreSQL"""
# engine = create_engine('postgresql://postgres:sandu1997@localhost:5432')
# real_estate_df.to_sql('real_estate', engine)

"""How many results/rows do we have for each location"""
real_estate_df['Location'].value_counts()

# SELECT "Location", count(*) from real_estate group by "Location"

"""Matplotlib"""
data = real_estate_df['Location']
p = plt.hist(data, bins=20, color='red')
plt.xticks(rotation='vertical')
plt.title('Number of results/rows')
plt.show()

"""What is the average/min/max price for all(!) observed locations"""
pd.set_option('display.float_format', lambda x: '%.2f' % x)
real_estate_df['Price($)'].describe()
# check min result
min_result = real_estate_df.loc[real_estate_df['Price($)'] == 1895]
min_result
# %%
# check max result
max_result = real_estate_df.loc[real_estate_df['Price($)'] == 169000000]
max_result

# SQL
# select max("Price($)") from real_estate;
# select "Location", max("Price($)") from real_estate group by "Location";


"""What is the mean price per sqft for each(!) location"""
mean_price_sqft = real_estate_df.groupby('Location')['price/sqft'].mean().sort_values(ascending=False)

# SQL
# select "Location", avg("price/sqft") from real_estate group by "Location";

# Matplotlib
mean_price_sqft.plot(cmap='seismic', style='.-')
plt.xticks(rotation='vertical')

"""what is the highest price per sqft in San Francisco"""
# Pandas
real_estate_df[real_estate_df['Location'] == 'San Francisco']['price/sqft'].max()

# show the row
row = real_estate_df.loc[real_estate_df['price/sqft'] == 3903.51]
# print(row) # 5417  765 Market St #32D         2  ...  San Francisco     3903.51

# SQL
# select "Location", max("price/sqft")
# from real_estate
# where "Location" = 'San Francisco'
# group by "Location";


"""What is the mean house price & mean price/sqft for each location"""
real_estate_df.groupby(['Location'])['Price($)', 'price/sqft'].mean().sort_values(by='Price($)', ascending=False)

real_estate_df.groupby(['Location'])['Price($)'].mean().sort_values(ascending=False).plot(
    title='Mean Price in $', kind='bar', color='green')
real_estate_df.groupby(['Location'])['price/sqft'].mean().sort_values(ascending=False).plot(
    title='Mean Price/Sqft in $', kind='bar', color='blue')
plt.ticklabel_format(useOffset=False, style='plain', axis='y')

plt.show()


"""How manu bathrooms and bedrooms does the house with the highest price Las Vegas have"""

real_estate_df[real_estate_df['Location'] == 'Las Vegas']['Price($)'].idxmax()  # 1850
real_estate_df.loc[1850]

# SQL
# select *
# from real_estate
# where "Location" = 'Las Vegas' and "Price($)" = '27450000'


"""Is there a correlation between Mean House Price and Mean Price per Sqft"""

p1 = real_estate_df.groupby(['Location'])['Price($)', 'Price($)'].mean()
p1
#%%

p2 = real_estate_df.groupby(['Location'])['Price($)', 'price/sqft'].mean()
p2

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(p1, color='red')
ax2.plot(p2, color='orange')

ax1.set_xlabel('Location')
ax1.set_ylabel('Mean Price in $', color='green')
ax2.set_ylabel('Price per Sqft in $', color='yellow')

fig.set_figheight(6)
fig.set_figwidth(6)


fig.autofmt_xdate(rotation=45)
plt.grid(True)

fig.show()














# %%
real_estate_df[real_estate_df['Location'] == 'Las Vegas']['Price($)'].idxmax()