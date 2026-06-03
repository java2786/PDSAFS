unit = float(input("Enter your units: "))
bill = 0

if(unit <= 100):
    bill = unit * 1.5
elif(unit<=200):
    fp = 100
    sp = unit - 100 
    bill = fp*1.5 + sp*2.5
else:
    fp = 100
    sp = 100 
    tp = unit - 200 
    bill = fp*1.5 + sp*2.5 + tp*3.5

print(f"Bill for #{unit} units is Rs {bill}/-")