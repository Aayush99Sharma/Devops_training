#Approach 1 using bubble sort

arr = [18, 15, 81, 26, 42]
# Bubble sort implementation
n = len(arr)
for i in range(n):
    for j in range(0, n - i - 1):
        # Swap if the element found is greater than the next element
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

second_largest = arr[-2]
print(second_largest)

#Approach 2 Using inbuilt sort
list = [18, 15, 81, 26, 42]
# Sort the list and remove duplicates
sorted_arr = sorted(list(set(arr)))

second_largest = sorted_arr[-2]

print(second_largest)

