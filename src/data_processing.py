import pandas as pd
import json
from os import makedirs, path


# Load the JSON file
with open('/github_analysis/src/data/json/repo_commits.json') as f:
    data = json.load(f)

# Prepare the data for the DataFrame
rows = []
for key, values in data.items():
    for value in values:
        rows.append({'project': key, 'commit_date': value})

# Create the DataFrame
df = pd.DataFrame(rows)

# Create day of the week, month, and year columns
df['commit_date'] = pd.to_datetime(df['commit_date'])
df['day_of_week'] = df['commit_date'].dt.day_name()  # Use full day names
df['day_of_month'] = df['commit_date'].dt.day
df['month'] = df['commit_date'].dt.strftime('%b')
df['year'] = df['commit_date'].dt.year

print(df)

# Define the order for months and days of the week
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Convert month and day_of_week to categorical types with the specified order
df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True)  # type: ignore
df['day_of_week'] = pd.Categorical(df['day_of_week'], categories=day_order, ordered=True)  # type: ignore

print(df)

# Pivot the data to create a heatmap with days of the week as rows and month-year as columns
df_pivot = df.pivot_table(
    index='day_of_month',
    columns='month',
    values='commit_date',
    aggfunc='size',
    fill_value=0,
    observed=False
)
print(df_pivot)

# Save the DataFrame to a CSV file
data_dir = "/github_analysis/src/data/csv"
makedirs(data_dir, exist_ok=True)
df_pivot.to_csv(path.join(data_dir, "repo_commits.csv"))
# df.to_csv(path.join(data_dir, "repo_commits.csv"), index=False)