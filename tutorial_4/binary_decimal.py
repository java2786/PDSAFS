num = 1010
count = 0
sum= 0
while(num>0):
    result= (2**count) *(num%10)
    sum = sum +result
    num = num//10
    count = count+1

print(sum)