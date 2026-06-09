"""
Find biggest number:
23, 52, 16
"""

a = 231
b = 616
c = 522

if(a>b):
    if(a>c):
        print("1.",a)
    else:
        print("2.",c)
else:
    if(b>c):
        print("3.",b)
    else:
        print("4.",c)