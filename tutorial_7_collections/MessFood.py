"""
Python - Data Types -> Collections

The next morning, there is total confusion over leftover hostel food. Write a short Python script (10-15 lines) using at least one list, one tuple, one set, and one dictionary to manage:

- A list of hostel mates who want leftovers
- A tuple of fixed leftover items and quantities (the quantity can't increase)
- A set to remove duplicate names if someone asked twice
- A dictionary assigning who gets which item

===============================================
"""

students = ["amit", "suresh"]
students.append("dinesh")
students.append("mukesh")
students.append("suresh")
students.append("mukesh")
students.append("dinesh")
students.append("amit")
students.append("aman")



unique_stds = set(students)
print(f"Total students: {len(unique_stds)}")

# available_food = {"paratha": 2, "poha": 2}
# available_food['paratha'] = 1

# changes should not be possible
available_food = ("Paratha",3,"Poha",2)
paratha_qty = available_food[1]
poha_qty = available_food[3]

# Dictionary -> pair
# name -> food => tuple - decrease food count
students_foods = {}

for std in unique_stds:
	if(paratha_qty>0):
		paratha_qty = paratha_qty - 1
		students_foods[std]="Paratha"
	elif(poha_qty>0):
		poha_qty = poha_qty - 1
		students_foods[std]="Poha"
	else:
		students_foods[std]="No Food"

print(students_foods)
