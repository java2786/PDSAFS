# bmi = w / (hm*hm)

w = float(input("Enter you weight (kg): "))   # 70
hf = int(input("Enter you height (feet): "))    # 5
hi = int(input("Enter you height (inch): "))    # 8


h = ((hf*12 + hi) * 2.54)/100 # h in meter

bmi = w / (h*h)

# 18 - 25

if(bmi<18.5):
    print("Underweight")
elif(bmi< 25):
    print("Normal")
elif(bmi<30):
    print("Overweight")
else:
    print("Obese")