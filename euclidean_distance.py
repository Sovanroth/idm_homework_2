import math

def euclidean_distance(x, y):
    if len(x) != len(y):
        raise ValueError("Both objects must have the same number of attributes")

    squared_distances = [(a - b) ** 2 for a, b in zip(x, y)]
    sum_of_squares = sum(squared_distances)
    distance = math.sqrt(sum_of_squares)
    return distance

obj1 = [0, 3, 4, 5]
obj2 = [7, 6, 3, -1]

distance = euclidean_distance(obj1, obj2)
print(f"The Euclidean distance between obj1 and obj2 is: {distance}")
