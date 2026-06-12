"""

* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

"""

num = 5
for i in range(1, 1+num):
    line = "" 
    for j in range(1, 1+num):
        if(i==1 or i==num or j==1 or j == num):
            line = line + "* "
        else:
            line = line + "  "

    print(line)