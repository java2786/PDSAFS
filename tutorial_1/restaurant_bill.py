print("========Welcome to my shop========")
print("===========Our Menu===============")
print()

item_1_price = 15
item_2_price = 12
item_3_price = 25
item_4_price = 30

item_1_qt = 0
item_2_qt = 0
item_3_qt = 0
item_4_qt = 0

item_1_bill = 0
item_2_bill = 0
item_3_bill = 0
item_4_bill = 0


print(f"1. Samosa      - Rs {item_1_price}")
print(f"2. Tea         - Rs {item_2_price}")
print(f"3. Burger      - Rs {item_3_price}")
print(f"4. Momos      - Rs {item_4_price}")
print()

item_1_qt = int(input("Enter samosa quantity: "))
item_2_qt = int(input("Enter tea quantity: "))
item_3_qt = int(input("Enter burger quantity: "))
item_4_qt = int(input("Enter Momos quantity: "))

item_1_bill = item_1_price * item_1_qt
item_2_bill = item_2_price * item_2_qt
item_3_bill = item_3_price * item_3_qt
item_4_bill = item_4_price * item_4_qt

print()
print("Item   Quantity     Price    Total")
print("----------------------------------")
print(f"Samosa  {item_1_qt}           Rs {item_1_price}    Rs {item_1_bill}")
print(f"Tea     {item_2_qt}           Rs {item_2_price}    Rs {item_2_bill}")
print(f"Burger  {item_3_qt}           Rs {item_3_price}    Rs {item_3_bill}")
print(f"Momos  {item_4_qt}           Rs {item_4_price}    Rs {item_4_bill}")
print()

total = item_1_bill + item_2_bill + item_3_bill + item_4_bill
print(f"Total bill {total}")