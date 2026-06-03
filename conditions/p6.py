# Input a 3-digit number and how many even digits are there.

num = 429
evens = 0

last_digit = num % 10       
if(last_digit%2==0):
    evens = evens + 1
num = num // 10             

last_digit = num % 10       
if(last_digit%2==0):
    evens = evens + 1
num = num // 10             

last_digit = num % 10       
if(last_digit%2==0):
    evens = evens + 1
num = num // 10             

print(evens)