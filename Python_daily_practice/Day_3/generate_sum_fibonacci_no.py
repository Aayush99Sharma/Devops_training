#Generate all Fibonacci numbers up to a given maximum number.
# Approach 1

max_num = 50  
   
fibs = [0, 1]

while True:
    next_fib = fibs[-1] + fibs[-2]
    if next_fib > max_num:
       break
    fibs.append(next_fib)
    
sum = 0
for i in range(len(fibs)):
    sum += fibs[i]
    
    

print(f"Fibonacci numbers up to {max_num} are: {fibs}")
print("the sum is",(sum))



#Approach 2 using functiom
def generate_fibonacci_up_to(max_num):
   
    fibs = [0, 1]
    while True:
        next_fib = fibs[-1] + fibs[-2]
        if next_fib > max_num:
            break
        fibs.append(next_fib)
    return fibs


max_num = 50  
fibonacci_numbers = generate_fibonacci_up_to(max_num)
print(f"Fibonacci numbers up to {max_num} are: {fibonacci_numbers}")
