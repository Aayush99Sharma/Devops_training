# Approach 1
nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]

remove_duplicate = set(nums)

print(remove_duplicate)

#approach 2


lst = [1, 2, 2, 3, 3, 4, 5, 5, 6]

result = []
result.append(lst[0])


for i in range(1, len(lst)):
    if lst[i] != lst[i - 1]:
        result.append(lst[i])

print(result)
