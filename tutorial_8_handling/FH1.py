
filename = './songs.txt'

with open(filename, 'r') as file:
    lines = file.readlines()
    
    for line in lines:
        print(line, end="")

with open(filename, 'a') as file:
    file.write("Tuesday\n")
    file.write("Wednesday\n")
    