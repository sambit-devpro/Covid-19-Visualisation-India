'''Visualising Covid dataset'''

#Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#Importing Dataset
%matplotlib inline
plt.style.use('fivethirtyeight')
df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv', parse_dates=['Date'])


#Worldwide cases graph
df['Total Cases'] = df[['Confirmed', 'Recovered', 'Deaths']].sum(axis=1)
worldwide_df = df.groupby(['Date']).sum()
worldwide_df.head()
w = worldwide_df.plot(figsize=(20,15))
w.set_xlabel('Date')
w.set_ylabel('Number of cases WW')
w.title.set_text('Worldwide COVID insights')
plt.show()

#India vs world graph
ind_df = df[df['Country']=='India'].groupby(['Date']).sum()
ind_df.head().groupby(['Date']).sum()
fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111)
ax.plot(worldwide_df[['Total Cases']], label='Worldwide')
ax.plot(ind_df[['Total Cases']], label = 'India')
ax.set_xlabel('Date')
ax.set_ylabel('Number of cases in India')
ax.title.set_text('Worldwide vs India COVID insights')
plt.legend(loc= 'upper left')
plt.show()

#Daily trend for India calculations
ind_df = ind_df.reset_index()
ind_df.head()
ind_df['Daily Confirmed'] = ind_df['Confirmed'].sub(ind_df['Confirmed'].shift())
ind_df['Daily Deaths'] = ind_df['Deaths'].sub(ind_df['Deaths'].shift())
ind_df['Daily Recovered'] = ind_df['Recovered'].sub(ind_df['Recovered'].shift())

#Daily Confirmed vs Daily Recoveries India Graph
fig = plt.figure(figsize=(20,8))
ax = fig.add_subplot(111)
ax.bar(ind_df['Date'], ind_df['Daily Confirmed'], color = 'b', label = 'India daily confirmed')
ax.bar(ind_df['Date'], ind_df['Daily Recovered'], color = 'g', label = 'India daily recovered')
ax.set_xlabel('Date')
ax.set_ylabel('Number')
ax.title.set_text('Daily Confirmed vs Daily Recovered')
plt.show()

#Daily Confirmed vs Daily Deaths India Graph
fig = plt.figure(figsize=(20,8))
dd = fig.add_subplot(111)
dd.bar(ind_df['Date'], ind_df['Daily Confirmed'], color = 'b', label = 'India daily confirmed')
dd.bar(ind_df['Date'], ind_df['Daily Deaths'], color = 'r', label = 'India daily deaths')
dd.set_xlabel('Date')
dd.set_ylabel('Number')
dd.title.set_text('Daily Confirmed vs Daily Deaths')
plt.show()
