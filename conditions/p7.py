# Input a 3-digit number and sum of squares of each.

num = 429
sum = 0

last_digit = num % 10       
sum = sum + (last_digit * last_digit)
num = num // 10             

last_digit = num % 10       
sum = sum + (last_digit * last_digit)
num = num // 10             

last_digit = num % 10       
sum = sum + (last_digit * last_digit)
num = num // 10             


print(sum)