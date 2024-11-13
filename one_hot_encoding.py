# Function to perform one-hot encoding
def one_hot_encode(categories):
    # Get unique categories
    unique_categories = list(set(categories))
    # Create an empty list to store the one-hot encoded vectors
    one_hot_encoded = []

    # Iterate through each category in the input list
    for category in categories:
        # Initialize a list of zeros for one-hot encoding
        encoding = [0] * len(unique_categories)
        # Set the index corresponding to the category to 1
        encoding[unique_categories.index(category)] = 1
        # Append the encoded vector to the result
        one_hot_encoded.append(encoding)
    
    return one_hot_encoded, unique_categories


# Sample categorical data
categories = ['cat', 'dog', 'bird', 'dog', 'cat']

# Perform one-hot encoding
encoded, unique_categories = one_hot_encode(categories)

# Display the results
print("Unique Categories:", unique_categories)
print("One-Hot Encoded Vectors:")
for vec in encoded:
    print(vec)
