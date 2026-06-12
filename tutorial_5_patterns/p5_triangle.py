"""

* * * * *
* * * *
* * *
* * 
*

"""

num = 5
for i in range(num, 0, -1):
    # print(i)
    line = "" 
    for j in range(1, 1+i):
        line = line + "* "
    print(line)