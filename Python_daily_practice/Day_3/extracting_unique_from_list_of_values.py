
test_dict = {
    'gfg': [5, 6, 7, 8],
    'is': [10, 11, 7, 5],
    'best': [6, 12, 10, 8],
    'for': [1, 2, 5]
}

unique_values = set()

for key in test_dict:
    for value in test_dict[key]:
        unique_values.add(value)  
        
print("Unique values:", unique_values)
