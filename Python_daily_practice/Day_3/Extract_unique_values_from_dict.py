# Extract unique values from dict
my_dict = {
    'a': 1,
    'b': 2,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 4
}

s1 = set()

for i in my_dict.values():
    s1.add(i)
    
print(s1)


  
