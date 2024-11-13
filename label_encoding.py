from sklearn.preprocessing import LabelEncoder

# Sample data
colors = ['Red', 'Blue', 'Green', 'Blue', 'Red']

# Initialize the LabelEncoder
label_encoder = LabelEncoder()

# Fit and transform the data
encoded_labels = label_encoder.fit_transform(colors)

# Print the original and encoded values
print("Original labels:", colors)
print("Encoded labels:", encoded_labels)

# To decode back to the original labels
decoded_labels = label_encoder.inverse_transform(encoded_labels)
print("Decoded labels:", decoded_labels)

# fit_transform: Encodes the labels as integers.
# inverse_transform: Decodes the encoded integers back to the original labels.