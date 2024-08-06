import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('performanceGlobRes.csv')


df_stocksqlite = df.iloc[:, 0:2]
df_timestampsqlite = df.iloc[:, 2:4]
df_hctree = df.iloc[:, 4:6]


df_stocksqlite.columns = df_timestampsqlite.columns = df_hctree.columns = ['Query Type', 'Execution Time']

average_execution_time_stocksqlite = df_stocksqlite.groupby('Query Type').mean().reset_index()
average_execution_time_stocksqlite['System'] = 'StockSqlite'

average_execution_time_timestampsqlite = df_timestampsqlite.groupby('Query Type').mean().reset_index()
average_execution_time_timestampsqlite['System'] = 'Timestamp Implemented Sqlite'

average_execution_time_hctree = df_hctree.groupby('Query Type').mean().reset_index()
average_execution_time_hctree['System'] = 'HCtree'


average_execution_time = pd.concat([average_execution_time_stocksqlite, average_execution_time_timestampsqlite, average_execution_time_hctree])


fig, ax = plt.subplots(figsize=(10, 6))


sns.barplot(x='Query Type', y='Execution Time', hue='System', data=average_execution_time, ax=ax)

ax.set_title('Average Query Execution Time Comparison', fontsize=16, weight='bold')
ax.set_xlabel('Query Type', fontsize=14)
ax.set_ylabel('Average Execution Time (seconds)', fontsize=14)

ax.legend(fontsize=12)

plt.savefig('averagePerformanceResult.png', bbox_inches='tight')
