for i in range(11):    
    num = i
    result = ""

    while(num>0):
        result = str(num % 2) + result
        num = num//2

    print(f"{i} -> {result}")

