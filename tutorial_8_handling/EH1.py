try:
    samosa_qty = int(input("Enter samosa qty: "))
    bill = int(input("Enter total bill: "))
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    print(f"Welcome {name}, you are {age} years old.")

    print(f"Price per Samosa: {bill/samosa_qty}")
except ZeroDivisionError:
    print("You are dividing num by zero, not posssible. Human error")
except ValueError:
    print("Your input can not be converted into number")
else:
    print("Bye Bye")
finally:
    print("Always runs")