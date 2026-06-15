"""
* * * * *
  * * * * 
    * * * 
      * * 
        * 
"""
n = 5

for i in range(1, 1+n):
    for j in range(1, i):
        print("   ", end="")
    # for j in range(1, n-i+2):
    for j in range(n-i+1,0,-1):
        print(str(i)+str(j)+" ", end="")
    print()