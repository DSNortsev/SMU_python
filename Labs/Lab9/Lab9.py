

# Step 1:  Create a data frame from median_income.csv
#          Print the head to get a feel for the table

import pandas as pd
import matplotlib.pyplot as plt

df_income = pd.read_csv('median_income.csv')
df_income.head()

# Step 2:  Create a data frame from nst-est2019-01.csv
#          Print the head to get a feel for the table

df_nst= pd.read_csv('nst-est2019-01.csv')
df_nst.head()

# Step 3:  Merge the two data frames together

df_merged = pd.merge(df_income, df_nst, left_on='State or territory',
									    right_on='State',
									    how='inner')[['State', '2018 Median Income', '2019 Estimate']]
df_merged.head()

# Step 4:  Create a scatter plot using the 2019 Population Estimate as the X-axis
#          and the 2018 Median Income as the Y-axis
#          Do you see any connection in the data?

plt.scatter(df_merged['2019 Estimate'], df_merged['2018 Median Income'])
plt.xlabel('2019 Population Estimate')
plt.ylabel('2018 Median Income')
plt.show()

# Step 5:  Save the merged data frame to "merged.csv"

df_merged.to_csv('merged.csv', index=False) 
