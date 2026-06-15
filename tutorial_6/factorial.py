def getFactorial(num=1):
    if(num==0 or num==1):
        return 1
    else:
        n = num
        result = 1

        for i in range(2, n+1):
            result = result * i
            
        return result

