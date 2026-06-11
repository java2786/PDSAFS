num = 8
result = ""

while(num>0):
    rem = num%2
    num = num//2
    result = str(rem) + result

print(result)
