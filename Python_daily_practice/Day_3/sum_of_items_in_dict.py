# Define the dictionary
test_dict = {
    'gfg': [5, 6, 7, 8],
    'is': [10, 11, 7, 5],
    'best': [6, 12, 10, 8],
    'for': [1, 2, 5]
}

total_sum = 0

for values in test_dict.values():
    total_sum += sum(values)

print("Sum of all items in the dictionary:", total_sum)
