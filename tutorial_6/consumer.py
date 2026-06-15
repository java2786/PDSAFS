from factorial import getFactorial 

getFactorial()
print("==========")
i = 0
while(i<10):
    fact = getFactorial(i)
    print(f"Factorial of {i} is {fact}")
    i+=1

