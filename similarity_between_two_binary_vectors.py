def simple_matching_coef(x, y):
    if len(x) != len(y):
        raise ValueError("Both vectors must have the same length")

    matching_elements = sum(a == b for a, b in zip(x, y))
    total_elements = len(x)

    similarity = matching_elements / total_elements
    return similarity

def jaccard_coef(x, y):
    if len(x) != len(y):
        raise ValueError("Both vectors must have the same length")

    intersection_size = sum(a and b for a, b in zip(x, y))
    union_size = sum(a or b for a, b in zip(x, y))

    similarity = intersection_size / union_size if union_size != 0 else 0
    return similarity

x = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y = [0, 0, 0, 0, 0, 0, 1, 0, 0, 1]

smc_result = simple_matching_coef(x, y)
jc_result = jaccard_coef(x, y)

print(f"Simple Matching Coefficient: {smc_result}")
print(f"Jaccard Coefficient: {jc_result}")
