import seaborn as sns
from d_clean import df_combined


# check the missing value
sns.heatmap(df_combined.isna(), yticklabels=False, cbar=False, cmap='BuPu')




# %%

#%%
