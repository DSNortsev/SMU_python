import pandas as pd
import matplotlib.pyplot as plt

# Read csv file and create DataFrame
df = pd.read_csv('weather.csv')
# Convert Date.Full feature to datatime type 
df['Date.Full'] = pd.to_datetime(df['Date.Full'])
# Select weather for Dallas,TX in 2016
df_dallas = df.loc[(df['Station.Location'] == 'Dallas, TX')\
                   & (df['Date.Full'].dt.year.eq(2016)),\
                   ['Data.Precipitation', 'Date.Full', 'Date.Month', 'Data.Temperature.Avg Temp']]

df_dallas_per_month = df_dallas[['Date.Month', 'Data.Precipitation']]\
                        .groupby('Date.Month')\
                        .mean()\
                        .reset_index()\
                        .round(2)
df_dallas_per_month.to_csv('dallas_weather.csv')

# Select two columns Date.Month and Data.Precipitation,
# Groupby Data.Month, calculate mean value for each month
# Reset index and round all mean values to 2 decimal points

df_dallas_per_month = df_dallas[['Date.Month', 'Data.Precipitation']]\
                        .groupby('Date.Month')\
                        .mean()\
                        .reset_index()\
                        .round(2)
df_dallas_per_month.to_csv('dallas_weather.csv')

fig, ax = plt.subplots(3, 1, figsize=(10, 20))


df_dallas['Data.Precipitation'].plot(kind='hist',
                                     ax=ax[0],
                                     title='Dallas Weekly Rainfall 2016').set(xlabel='Rainfall (Inches)',
                                                                              ylabel='# of Weeks')

df_dallas.plot(kind='scatter',
               ax=ax[1],
               x='Data.Temperature.Avg Temp',
               y='Data.Precipitation',
               title='Dallas Avg Temp vs. Rainfall (Weekly)').set(xlabel='Avg Temp',
                                                                  ylabel='Rainfall (Inches)')
df_dallas_per_month.plot(kind='bar',
               ax=ax[2],
               x='Date.Month',
               y='Data.Precipitation',
               title='Dallas Montly Rainfall 2016',
               legend=False).set(xlabel='Month',
                                 ylabel='Total Rainfall (Inches)')
plt.savefig("test.png")
plt.show()
