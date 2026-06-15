# num = 153 =>  
# count digit -> c
# each digit power c
# sum
# match with original number
# if same -> armstrong

"""
153
c = 3
1^3 + 5+3 + 3^3 
1 + 125 + 27
153
"""

for i in range(10000):
    num = i
    copy = num
    count = 0
    sum = 0

    while(num>0):
        num = num // 10
        count = count + 1
    num = copy

    while(num>0):
        ld = num % 10
        num = num // 10
        sum = sum + ld**count
    num = copy

    if(num == sum):
        print(f"{num} is Armstrong number")
