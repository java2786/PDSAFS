# calculate courier charges based on package weight.

w = 6
bill = 0
if(w > 5):
    w = w - 5
    bill = w * 30 +  2*50 + 3*40
elif(w>2):
    w = w - 2
    bill = w * 40 + 2*50
else:
    bill = w * 50


print(bill)