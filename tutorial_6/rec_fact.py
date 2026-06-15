def getFactorial(num):
    r = 0
    print(num)
    if(num==1):
        r = 1
    else:
        r = getFactorial(num - 1) * num
    print(num)
    return r


fact = getFactorial(5)

print(fact)