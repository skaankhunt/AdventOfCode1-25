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
    temp = move_amount[i]
    print("Line : " + str(i+1))
    #print("Amount to move : " + str(move_amount[i]))
    #print("Available amount : " + str(len(containers_dict['container' + str(move_from[i])])))
    available_amount = len(containers_dict['container' + str(move_from[i])])
    amount_to_move = move_amount[i]
    if amount_to_move > available_amount:
        print("Not enough characters to move")

    for j in range(move_amount[i]):
        if temp >= 3:
            # Append the 3 last characters to new container
            containers_dict['container' + str(move_to[i])].append(containers_dict['container' + str(move_from[i])][len(containers_dict['container' + str(move_from[i])])-3])
            containers_dict['container' + str(move_to[i])].append(containers_dict['container' + str(move_from[i])][len(containers_dict['container' + str(move_from[i])])-2])
            containers_dict['container' + str(move_to[i])].append(containers_dict['container' + str(move_from[i])][len(containers_dict['container' + str(move_from[i])])-1])
            
            #print("Moving : " + containers_dict['container' + str(move_from[i])][len(containers_dict['container' + str(move_from[i])])-3] + " From container" + str(move_from[i]) + " to " + "container" + str(int(move_to[i])))
            #print("Moving : " + containers_dict['container' + str(move_from[i])][len(containers_dict['container' + str(move_from[i])])-2] + " From container" + str(move_from[i]) + " to " + "container" + str(int(move_to[i])))
            #print("Moving : " + containers_dict['container' + str(move_from[i])][len(containers_dict['container' + str(move_from[i])])-1] + " From container" + str(move_from[i]) + " to " + "container" + str(int(move_to[i])))

            # Delete the appended characters from old container
            containers_dict['container' + str(move_from[i])].pop()
            containers_dict['container' + str(move_from[i])].pop()
            containers_dict['container' + str(move_from[i])].pop()
            
            #print("Container" + str(move_from[i]) + " now looks like this : " + str(containers_dict['container' + str(move_from[i])]))
            #print("Container" + str(move_to[i]) + " now looks like this : " + str(containers_dict['container' + str(move_to[i])]))

            temp -= 3
            #print("Remaining amount to move : " + str(temp))
            if temp == 0:
                print("Done moving.. Next line!")
                break

        elif temp == 2:
            # Append the 2 last characters to new container
            containers_dict['container' + str(move_to[i])].append(containers_dict['container' + str(move_from[i])][len(containers_dict['container' + str(move_from[i])])-2])
            containers_dict['container' + str(move_to[i])].append(containers_dict['container' + str(move_from[i])][len(containers_dict['container' + str(move_from[i])])-1])
            
            #print("Moving : " + containers_dict['container' + str(move_from[i])][len(containers_dict['container' + str(move_from[i])])-2] + " From container" + str(move_from[i]) + " to " + "container" + str(int(move_to[i])))
            #print("Moving : " + containers_dict['container' + str(move_from[i])][len(containers_dict['container' + str(move_from[i])])-1] + " From container" + str(move_from[i]) + " to " + "container" + str(int(move_to[i])))
            
            # Delete the appended characters from old container
            containers_dict['container' + str(move_from[i])].pop()
            containers_dict['container' + str(move_from[i])].pop()

            #print("Container" + str(move_from[i]) + " now looks like this : " + str(containers_dict['container' + str(move_from[i])]))
            #print("Container" + str(move_to[i]) + " now looks like this : " + str(containers_dict['container' + str(move_to[i])]))

            temp -= 2
            
            #print("Remaining amount to move : " + str(temp))
            
            if temp == 0:
                print("Done moving.. Next line!")
                break

        elif temp == 1:
            # Append the last character to new container
            containers_dict['container' + str(move_to[i])].append(containers_dict['container' + str(move_from[i])][len(containers_dict['container' + str(move_from[i])])-1])
            
            #print("Moving : " + containers_dict['container' + str(move_from[i])][len(containers_dict['container' + str(move_from[i])])-1] + " From container" + str(move_from[i]) + " to " + "container" + str(int(move_to[i])))
            
            # Delete the appended characters from old container
            containers_dict['container' + str(move_from[i])].pop()
            
            #print("Container" + str(move_from[i]) + " now looks like this : " + str(containers_dict['container' + str(move_from[i])]))
            #print("Container" + str(move_to[i]) + " now looks like this : " + str(containers_dict['container' + str(move_to[i])]))
            
            temp -= 1

            #print("Remaining amount to move : " + str(temp))
            print("Done moving.. Next line!")
            break
        else:
            print("Done moving.. Next line!")
            break

print("Finished")
for i in range(len(containers_dict)):
    print("Container" + str(i+1) + " - " + str(containers_dict['container' + str(i+1)]))

# Print the containers
print("The containers on top are: ", end="")
for i in range(len(containers_dict)):
    #print("Container" + str(i+1) + " - " + str(containers_dict['container' + str(i+1)][len(containers_dict['container' + str(i+1)])-1]))
    print(str(containers_dict['container' + str(i+1)][len(containers_dict['container' + str(i+1)])-1]), end="")

#CJGQVJDTL

