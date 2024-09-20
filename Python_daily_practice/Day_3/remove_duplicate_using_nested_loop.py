list = [1,22,22,44,44,5,5]

unique_list = []

for i in range(0,len(list)):
    bool = False
    for j in range(0,len(unique_list)):
        if list[i] == unique_list[j]:
            bool = True
            break
    if not bool:
        unique_list.append(list[i])
        unique_list.sort()
    
print(unique_list)




