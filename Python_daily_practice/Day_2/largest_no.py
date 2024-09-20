def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

nums = [40, 15, 98, 25, 3]
largest_num = find_largest(nums)
print(f"The largest number is {largest_num}")