def is_armstrong(num):
    digits = str(num)
    num_digits = len(digits)
    total = sum(int(digit) ** num_digits for digit in digits)
    return total == num
num = 153
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
