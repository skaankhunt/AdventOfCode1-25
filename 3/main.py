# Part 1
# Every item type is identified by a single lowercase or uppercase letter
# Eeach rucksack always has the same number of items in each of it's two compartments
# First half of characters represent items in the first compartment
# Second half of characters represent items in the second compartment

# To priotitize item arrangement, every item can be converted to a priority
# Lowercase itemm types a through z have proirity 1 through 26
# Uppercase item types A through Z have priority 27 through 52

# Part 2
# Elves are divided into groups of three
# Eeach elf carries a badge that identifies their group
# The badge is the only item type carried by all three Elves
# At most, two of the Elves will be carrying any other item type
# Find the sum of priorities from all Elf groups


# Open input.txt and read contents into a list
with open('input.txt', 'r') as f:
    rucksacks = f.readlines()

# Remove newline characters from each rucksack
rucksacks = [rucksack.strip() for rucksack in rucksacks]

priorities = 0

# Split each rucksack into two compartments
for lines in rucksacks:
    first_compartments = lines[:len(lines)//2]
    second_compartments = lines[len(lines)//2:]
    
    # Find letters that appear in both compartments
    common_letters = []
    for first_letter in first_compartments:
        if first_letter in second_compartments:
            common_letters.append(first_letter)

    # Find the priority of each common letter
    if common_letters[0].islower():
        priorities += (ord(common_letters[0]) - 96)
    else:
        priorities += (ord(common_letters[0]) - 38)

# Part 2
# Find item types that appear in all three rucksacks
group_lines = []
group = []
for line in rucksacks:
    if len(group) == 3:
        group_lines.append(group)
        group = []
    group.append(line)
group_lines.append(group)

# Find the item types that appear in all three rucksacks and add their priorities
badge = []
badge_priorities = 0
for group in group_lines:
    for letter in group[0]:
        if letter in group[1] and letter in group[2]:
            if letter.islower():
                badge_priorities += (ord(letter[0]) - 96)
            else:
                badge_priorities += (ord(letter[0]) - 38)
            break

# Print priority score
print(priorities)

# Print badge priority score
print(badge_priorities)





