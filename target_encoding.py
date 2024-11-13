import pandas as pd

# Sample data
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C'],
    'Target': [1, 0, 1, 1, 0, 1, 0]
}
df = pd.DataFrame(data)

# Calculate mean of target variable for each category
target_mean = df.groupby('Category')['Target'].mean()

# Map the mean target value back to the original DataFrame
df['Category_encoded'] = df['Category'].map(target_mean)

# Display the original and encoded DataFrame
print("Original DataFrame:")
print(df[['Category', 'Target']])
print("\nDataFrame with Target Encoding:")
print(df)

# groupby('Category')['Target'].mean(): Computes the mean of the target variable for each category in "Category."
# map(target_mean): Maps these mean values back to the original "Category" column, creating an encoded column.