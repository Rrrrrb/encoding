import pandas as pd

# Sample data
data = {'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red', 'Red', 'Green']}
df = pd.DataFrame(data)

# Frequency encoding
frequency_encoded = df['Color'].value_counts().to_dict()
df['Color_encoded'] = df['Color'].map(frequency_encoded)

# Display the original and encoded DataFrame
print("Original DataFrame:")
print(df[['Color']])
print("\nDataFrame with Frequency Encoding:")
print(df)

# value_counts(): This counts the frequency of each unique value in the "Color" column.
# map(): The frequencies are then mapped back to the original column, creating a new encoded column with these frequencies.