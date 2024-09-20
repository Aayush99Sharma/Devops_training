my_list = [1, 2, 3, 4, 5, 6]

n = 0              
for element in my_list:
    n += 1

mid = n // 2

for i in range(mid):
    my_list[i], my_list[n-1 -i] = my_list[n-1-i], my_list[i]

print(my_list)
