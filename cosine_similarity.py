import math

def cosine_similarity(x, y):
    if len(x) != len(y):
        raise ValueError("Both objects must have the same number of attributes")

    dot_product = sum(a * b for a, b in zip(x, y))
    magnitude_x = math.sqrt(sum(a ** 2 for a in x))
    magnitude_y = math.sqrt(sum(b ** 2 for b in y))

    similarity = dot_product / (magnitude_x * magnitude_y)
    return similarity

# Example usage
obj1 = [0, 3, 4, 5]
obj2 = [7, 6, 3, -1]

similarity = cosine_similarity(obj1, obj2)
print(f"The cosine similarity between obj1 and obj2 is: {similarity}")
