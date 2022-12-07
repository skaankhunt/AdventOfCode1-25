f = open("input.txt", "r")
input = f.read().splitlines()
f.close()

blankspaces = 0
for x in input:
    if x == '':
        blankspaces += 1

calories = [0] * (blankspaces + 1)

elfcount = 0

for i in input:
    if i == '':
        elfcount += 1
    else:
        calories[elfcount] += int(i)

print("The elf carrying the most calories is carrying:")
print(max(calories))

sum = 0
for z in range(0,3):
    sum += max(calories)
    calories[calories.index(max(calories))] = 0
print("The calorie sum of the three most loaded elves is:")
print(sum)





