def jaccard_similarity(x, y):
    if len(x) != len(y):
        raise ValueError("Both objects must have the same number of attributes")

    intersection_size = len(set(x).intersection(y))
    union_size = len(set(x).union(y))

    similarity = intersection_size / union_size if union_size != 0 else 0
    return similarity

obj1 = [0, 3, 4, 5]
obj2 = [7, 6, 3, -1]

similarity = jaccard_similarity(obj1, obj2)
print(f"The Jaccard similarity between obj1 and obj2 is: {similarity}")
