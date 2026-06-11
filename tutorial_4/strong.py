# Find if given number is strong number
# 1 4 5 
# 1 24 120
i = 1
while(i<1000):
    num = i
    copy = num
    sum = 0

    while(num>0):
        ld = num % 10
        num = num // 10

        fact_num = ld
        result = 1

        while(fact_num>0):
            result = result * fact_num
            fact_num = fact_num - 1

        sum = sum + result

    if(sum==copy):
        print(f"{copy} is strong number")

    i = i + 1