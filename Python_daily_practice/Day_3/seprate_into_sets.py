# seprate a list into two diff set based on odd and even no 
list = [1,3,6,6,8,8]

s1 = set()
s2 = set()

for i in range(0,len(list)):
    if list[i]%2 != 0:
       s1.add(list[i])

for i in range(0,len(list)):
    if list[i]%2 == 0:
       s2.add(list[i])
       
print(s1)
print(s2)


# seprate list into 2 sets in terms of odd and even no also find an average of each sets
list = [1,3,6,6,8,8]

s1 = set()
s2 = set()

sum1 = 0
sum2 =0
c1 = 0
c2 = 0
for i in range(0,len(list)):
    if list[i] % 2 != 0:
     s1.add(list[i])
     sum1 += list[i]
     c1 += 1

for j in range(0,len(list)):
    if list[j] % 2 == 0:
      s2.add(list[j])
      sum2 += list[j]
      c2 += 1
      
print(s1)
print(s2)
print(sum1/c1)
print(sum2/c2)


