# Real input

containers_dict = {
    'container1': ["Q", "M", "G", "C", "L"],
    'container2': ["R", "D", "L", "C", "T", "F", "H", "G"],
    'container3': ["V", "J", "F", "N", "M", "T", "W", "R"],
    'container4': ["J", "F", "D", "V", "Q", "P"],
    'container5': ["N", "F", "M", "S", "L", "B", "T"],
    'container6': ["R", "N", "V", "H", "C", "D", "P"],
    'container7': ["H", "C", "T"],
    'container8': ["G", "S", "J", "V", "Z", "N", "H", "P"],
    'container9': ["Z", "F", "H", "G"],
}
# Read input.txt to variable
with open('input.txt', 'r') as f:
    input = f.read()

"""
# Test input
containers_dict = {
    'container1': ["Z", "N"],
    'container2': ["M", "C", "D"],
    'container3': ["P"],
}
# Read test.txt to variable
with open('test.txt', 'r') as f:
    input = f.read()
"""

# Split input into lines
input = input.splitlines()

# Split line into words and append to lists
move_from = []
move_amount = []
move_to = []
for line in input:
    line = line.split()
    move_from.append(line[3])
    move_to.append(line[5])
    move_amount.append(line[1])
move_amount = [eval(i) for i in move_amount]

# Part 1
"""
# Loop over the amount of characters to move
for i in range(len(move_from)):
    #print("From container" + str(move_from[i]) + " to " + "container" + str(int(move_to[i])))
    for j in range(int(move_amount[i])):
        # Append the characters to new container
        containers_dict['container' + str(move_to[i])].append(containers_dict['container' + str(move_from[i])][len(containers_dict['container' + str(move_from[i])])-1])
        #print(containers_dict['container' + str(move_from[i])][len(containers_dict['container' + str(move_from[i])])-1])
        containers_dict['container' + str(move_from[i])].pop()
"""
print("Start :")
for i in range(len(containers_dict)):
    print("Container" + str(i+1) + " - " + str(containers_dict['container' + str(i+1)]))

# Part 2
for i in range(len(move_from)):
    lenght_from = len(containers_dict['container' + str(move_from[i])]) - 1
    b = lenght_from
    a = b + 1 - move_amount[i]

    print("Line : " + str(i+1))
    print("Move amount = " + str(move_amount[i]))
    print("Lenght of move_from = " + str(len(containers_dict['container' + str(move_from[i])])-1))
    print("a = " + str(a))
    print("b = " + str(b))
    
    if move_amount[i] == 1:
        containers_dict['container' + str(move_to[i])].append(containers_dict['container' + str(move_from[i])][len(containers_dict['container' + str(move_from[i])])-1])
        print(containers_dict['container' + str(move_from[i])][len(containers_dict['container' + str(move_from[i])])-1])
        containers_dict['container' + str(move_from[i])].pop()
    else:
        containers_dict['container' + str(move_to[i])].extend(containers_dict['container' + str(move_from[i])][a:b+1])
        print(containers_dict['container' + str(move_from[i])][a:b+1])
        for x in range(move_amount[i]):
            containers_dict['container' + str(move_from[i])].pop()

print("Finished")
for i in range(len(containers_dict)):
    print("Container" + str(i+1) + " - " + str(containers_dict['container' + str(i+1)]))

# Print the containers
print("The containers on top are: ", end="")
for i in range(len(containers_dict)):
    #print("Container" + str(i+1) + " - " + str(containers_dict['container' + str(i+1)][len(containers_dict['container' + str(i+1)])-1]))
    print(str(containers_dict['container' + str(i+1)][len(containers_dict['container' + str(i+1)])-1]), end="")

#CJGQVJDTL

