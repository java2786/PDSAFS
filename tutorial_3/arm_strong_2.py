# print last_digit.
num = 432
saved = num
last_digit = num % 10 # 3
cube_1 = last_digit*last_digit*last_digit # 27
num = num // 10 # 15

last_digit = num % 10 # 5
cube_2 = last_digit*last_digit*last_digit # 125
num = num // 10 # 1

last_digit = num % 10 # 1
cube_3 = last_digit*last_digit*last_digit # 1
sum = cube_1+cube_2+cube_3 # 27+125+1 = 153

n = saved
if(n == sum):
    print("Armstrong Number")
else:
    print("Not Armstrong")
