import array as Bundle

marks = Bundle.array("i")

marks.append(76)
marks.append(45)
marks.append(82)
marks.append(81)
marks.append(76)



# print(marks)
# print(type(marks))


# print("firt value",marks[0])

# print(len(marks))


for i in range(len(marks)):
    print(f"Index: {i}, Marks: {marks[i]}")