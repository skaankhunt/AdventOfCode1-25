# Every section has a unique ID number
# Each Elf is assigned a range of section IDs
# Some of the assignments overlap
# Input is a list of the section assignments for each pair

# Part 1
# Save input.txt as a list of strings
# Split each string into a list of two strings

input = []
with open('input.txt') as f:
    for line in f:
        input.append(line.split())

group_assignments = []

for line in input:
    for string in line:
        #print(string)
        group_assignments.append(string.split(","))

induvidual_assignments = []
for string in group_assignments:
    for assignment in string:
        induvidual_assignments.append(assignment.split("-"))

#print(induvidual_assignments)

count = 0
i = 0
j = 0

print(induvidual_assignments)


with open("output.txt", "a") as f:
    while j < (len(induvidual_assignments) / 2):
        if int(induvidual_assignments[i][0]) >= int(induvidual_assignments[i+1][0]):
            if int(induvidual_assignments[i][1]) <= int(induvidual_assignments[i+1][1]):
                count += 1
                print("Count + 1")
                print(induvidual_assignments[i])
                print(induvidual_assignments[i+1])
                f.write(str(induvidual_assignments[i]) + " " + str(induvidual_assignments[i+1]) + "\n")
        elif int(induvidual_assignments[i+1][0]) >= int(induvidual_assignments[i][0]):
            if int(induvidual_assignments[i+1][1]) <= int(induvidual_assignments[i][1]):
                count += 1
                print("Count + 1")
                print(induvidual_assignments[i])
                print(induvidual_assignments[i+1])
                f.write(str(induvidual_assignments[i]) + " " + str(induvidual_assignments[i+1]) + "\n")
                
        i += 2
        j += 1


print(count)
