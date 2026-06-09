"""
num -> 
	count
	each digit power count
	add
	compare -> same
"""

num = 153
copy = num
sum = 0

# count area
count = 0
while(num>0):
    # last_digit = num%10
    num = num//10
    count = count + 1
    
num = copy

# power area
while(num>0):
    last_digit = num%10
    num = num//10
    pow = count
    result = 1
    while(pow>0):
        result = result * last_digit
        pow = pow - 1
    # sum area
    sum = result + sum

num = copy

# compare area
if(sum == num):
    print(f"{num} is armstrong number")
else:
    print(f"{num} is not armstrong number")

