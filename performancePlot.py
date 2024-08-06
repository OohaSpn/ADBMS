import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV data into a pandas DataFrame
df = pd.read_csv('performanceResult.csv')

# Set the style of the plot to be more advanced
sns.set_style("whitegrid")

# Create a figure and axis for the plot
fig, ax = plt.subplots()

# Define colors for the lines
colors = ['red', 'blue']

# Loop through each type of query
for i, query_type in enumerate(df['Query Type'].unique()):
    # Create a line plot for each type of query
    sns.lineplot(x=df[df['Query Type'] == query_type].index, 
                 y="Execution Time", 
                 data=df[df['Query Type'] == query_type], 
                 label=query_type, 
                 linewidth=2.5, 
                 marker='o', 
                 ax=ax, 
                 color=colors[i % len(colors)])

# Set the title and labels of the plot
ax.set_title('Query Execution Time For Timestamp Implemented Sqlite', weight='bold')
ax.set_xlabel('Index')
ax.set_ylabel('Execution Time (s)')

# Add a legend
ax.legend()

# Save the plot as a PNG image
plt.savefig('performanceResult.png')
