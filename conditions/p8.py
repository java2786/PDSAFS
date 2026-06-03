# find if given number is divisible by 5, 11 or both

num = 55

if(num%5==0 and num%11==0):
    print("Divisible by both 5 and 11")
elif(num%5==0):
    print("Divisible by 5")
elif(num%11==0):
    print("Divisible by 1")
else:
    print("Nothing")