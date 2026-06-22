
filename = './students.dat'

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# marks = []
# for i in range(3):
#     marks.append(int(input(f"Enter marks for subject #{i+1}")))
name = "Ramesh"
age = 21
marks = [54, 73, 81]

student_dict = {"name": name, "age": age, "marks": marks}

with open(filename, 'w') as file:
    file.write(str(student_dict))
