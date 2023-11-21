def manhattan_distance(x, y):
    if len(x) != len(y):
        raise ValueError("Both objects must have the same number of attributes")

    distances = [abs(a - b) for a, b in zip(x, y)]
    distance = sum(distances)
    return distance

obj1 = [0, 3, 4, 5]
obj2 = [7, 6, 3, -1]

distance = manhattan_distance(obj1, obj2)
print(f"The Manhattan distance between obj1 and obj2 is: {distance}")
