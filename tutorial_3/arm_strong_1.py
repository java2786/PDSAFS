n = int(input("Enter your number: "))
saved = n
sum = 0

last_digit = n%10 #3
n = n//10#15
cube = last_digit * last_digit * last_digit #27
sum = sum + cube#27

last_digit = n%10 #5
n = n//10#1
cube = last_digit * last_digit * last_digit #125
sum = sum + cube#152

last_digit = n%10 #1
n = n//10#0
cube = last_digit * last_digit * last_digit #1
sum = sum + cube#153

n = saved
if(n == sum):
    print("Armstrong Number")
else:
    print("Not Armstrong")

