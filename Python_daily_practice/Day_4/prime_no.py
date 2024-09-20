


def is_prime(j):
    if j < 2:
        return False
    
    for k in range(2,(j//2)+1):
        if j % k == 0:
            return False
    return True

list = [10,2,3,4,5,6,7,97]
#result = is_prime(list)
result = {i: is_prime(i) for i in list }
print (result)