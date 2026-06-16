""" 

* * * *  
*       *
*       *
* * * *  
*       *
*       *
* * * *  

* * * * * 
*       *
*       *
*       *
* * * * *
*       *
*       *
*       *
* * * * *

"""

num = 5

# for i in range(1,2*num):
#     for j in range(1,1+num):
#         # print("* ",end="")
#         if(i==1 and j==num) or (i==num and j==num) or (i+1==2*num and j==num):
#             print(".  ",end="")
#         elif(i==1 or j==1 or j==num or i+1==2*num or i==num):
#             print("*  ",end="")
#         else:
#             # print(str(i)+str(j)+" ",end="")
#             print(".  ",end="")
    
#     print()



for i in range(1,1+num):
    for j in range(1,1+num):
        if(i==1 or i+j==num+1):
            print("* ",end="")
        else:
            # print(str(i)+str(j)+" ",end="")
            print("  ",end="")
    
    print()




