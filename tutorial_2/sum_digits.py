# Input a 3-digit number and print the sum of its digits.

num = 987
sum = 0

last_digit = num % 10    # 1
num = num // 10         # 48
sum = sum + last_digit

last_digit = num % 10   # 8
num = num // 10         # 4
sum = sum + last_digit

last_digit = num % 10   # 4
num = num // 10         # 0
sum = sum + last_digit

print(sum)


