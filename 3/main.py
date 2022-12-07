# Every item type is identified by a single lowercase or uppercase letter
# Eeach rucksack always has the same number of items in each of it's two compartments
# First half of characters represent items in the first compartment
# Second half of characters represent items in the second compartment

# To priotitize item arrangement, every item can be converted to a priority
# Lowercase itemm types a through z have proirity 1 through 26
# Uppercase item types A through Z have priority 27 through 52

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
    i = 0
    for first_letter in first_compartments:
        if first_letter in second_compartments:
            common_letters.append(first_letter)
            # Delete the letter from the second compartment
            second_compartments = second_compartments[:i] + second_compartments[i+1:]
        +i
        """
        for second_letter in second_compartments:
            if first_letter == second_letter:
                common_letters.append(first_letter)
                break
        """
    print(first_compartments)
    print(second_compartments)
    print(common_letters)
    print("\n")
        # First compartment - aabcde
        # Second compartment - aabklju

    # Find the priority of each common letter
    for line in common_letters:
        for letter in line:
            if letter.islower():
                priorities += (ord(letter) - 96)
            else:
                priorities += (ord(letter) - 38)

# Print priority score
print(priorities)





