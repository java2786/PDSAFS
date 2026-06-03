# Input a 3-digit number and print the sum of its digits.

num = 429
sum = 0

last_digit = num % 10       # 9
num = num // 10             # 42
sum = sum + last_digit

# num = 42
last_digit = num % 10       # 2
num = num // 10             # 4
sum = sum + last_digit

# num = 4
last_digit = num % 10       # 4
num = num // 10             # 0
sum = sum + last_digit

print(sum)
