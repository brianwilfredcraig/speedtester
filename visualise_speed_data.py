import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 10000)

urlToData = 'https://raw.githubusercontent.com/brianwilfredcraig/speedtester/master/output_speedtest.csv'
df = pd.read_csv(urlToData)
# df.info()

format_dict = {'DateTime':'{:%Y-%m-%d %H:%M}', 'Down':'{0:,.2f}', 'Up':'{0:,.2f}', 'Ping':'{0:,.2f}'}
df['DateTime'] = df['Date'] + ' ' + df['Time']
df['DateTime'] = pd.to_datetime(df['DateTime'])
# df.info()

dfReformat = df[['DateTime', 'Down', 'Up', 'Ping']]
# dfReformat.info()

dfSortedByDateTimeDSC = dfReformat.sort_values(by ='DateTime', ascending=False )
dfSortedByDateTimeDSC.head(4).style.format(format_dict)

dfReformat.describe()

dfSortedByDownASC = dfReformat.sort_values(by ='Down' )
dfSortedByDownASC.head().style.format(format_dict)

dfSortedByDownDSC = dfReformat.sort_values(by ='Down', ascending=False )
dfSortedByDownDSC.head().style.format(format_dict)

# df.info()
dfDownMedianByDate = df.groupby('Date').median()
dfDownMaxByDate = df.groupby('Date').max()
dfDownMinByDate = df.groupby('Date').min()
# dfDownMedianByDate.info()

dfDownMedianByDate.reset_index(level=0, inplace=True)
dfDownMaxByDate.reset_index(level=0, inplace=True)
dfDownMinByDate.reset_index(level=0, inplace=True)
# dfDownMedianByDate.info()

dfDownMedianByDate['Date'] = pd.to_datetime(dfDownMedianByDate['Date'])
dfDownMaxByDate['Date'] = pd.to_datetime(dfDownMaxByDate['Date'])
dfDownMinByDate['Date'] = pd.to_datetime(dfDownMinByDate['Date'])
# dfDownMedianByDate.info()

import matplotlib.pyplot as plt
plt.plot(dfDownMedianByDate['Date'], dfDownMedianByDate['Down'], label='Download') 
plt.xticks(rotation='vertical')
plt.title('Down by Date (Median)')
plt.show()

plt.plot(dfDownMaxByDate['Date'], dfDownMaxByDate['Down'], label='Download') 
plt.xticks(rotation='vertical')
plt.title('Down by Date (Max)')
plt.show()

plt.plot(dfDownMinByDate['Date'], dfDownMinByDate['Down'], label='Download') 
plt.xticks(rotation='vertical')
plt.title('Down by Date (Min)')
plt.show()