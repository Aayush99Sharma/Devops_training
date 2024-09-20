# find sum of odd number by taking input or using list
list = input("write your number: ")

sum = 0
count = 0

for num in list.split():
    num = int (num)
    if num % 2 != 0:
        sum += num
        count += 1 
    


if count > 0:
   average = sum / count
   print("the average is ",average)
   
else:
    print("No odd number found")
  





# Using list 

list = [1,2,3,4]

sum = 0
count = 0

for num in list:
 
    if num % 2 != 0:
        sum += num
        count += 1 
    


if count > 0:
   average = sum / count
   print("the average is ",average)
   
else:
    print("No odd number found")
  
