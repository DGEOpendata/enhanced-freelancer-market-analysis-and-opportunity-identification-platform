python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
datafile = 'DL06-Freelance-Activities-ADRA-OD-010-AFR.xlsx'
data = pd.read_excel(datafile)

# Step 2: Inspect the data
print(data.head())

# Step 3: Analyze the data
# Example: Count of activities by category
activity_counts = data['Category'].value_counts()

# Step 4: Visualization
plt.figure(figsize=(10, 6))
sns.barplot(x=activity_counts.values, y=activity_counts.index)
plt.xlabel('Number of Activities')
plt.ylabel('Categories')
plt.title('Count of Freelancer Activities by Category')
plt.show()

# Step 5: Save insights to file
activity_counts.to_csv('activity_counts.csv', index=True)
