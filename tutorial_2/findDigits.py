# Check if a number has exactly 3 digits

a = 32
a = a // 10         # remove last digit
if(a == 0):
    print("Single digit")
else:
    a = a // 10         # remove last digit
    if(a == 0):
        print("two digit")
    else:
        a = a // 10         # remove last digit
        if(a == 0):
            print("three digit")
        else:
            print("More than 3 digits")