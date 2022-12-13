# Read file and store in a two dimensional array
with open('input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
count = 0

# Loop over rows
for row in range(len(content)):
    # Check if tree is at top or bottom of list
    if row == 0 or row == len(content[row]) - 1:
            count += 1
            continue
    else:
        # Loop over columns
        for column in range(len(content[row])):
            # Check if tree is at most left or right of list
            if column == 0 or column == len(content[row]) - 1:
                count += 1
                continue
                # If tree is not at edge of list, check all 4 directions
            else:
                # Check up
                if content[row][column] > max(content[:row][column]):
                    count += 1
                # Check down
                elif content[row][column] > max(content[row+1:][column]):
                    count += 1
                # Check left
                elif content[row][column] > max(content[row][:column+1]):
                    count += 1
                # Check right
                elif content[row][column] > max(content[row][column+1:]):
                    count += 1

print(count)


    
