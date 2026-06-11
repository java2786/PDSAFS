# 2 8 => 2^2 + 8^2 => 68 => 36 + 64 => 100 => 1+0+0 => 1 -> stop when single digit
num = 89
copy = num
sum = 0
while(num>0):
    ld = num%10
    num = num//10
    sum = sum + (ld*ld)

    if(num==0 and sum>9):
        num = sum
        sum = 0

if(sum==1):
    print(copy,"Happy number")
else:
    print(copy,"Unhappy number")