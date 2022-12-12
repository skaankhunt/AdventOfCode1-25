# Find start-of-packet marker
# start-of-packet marker is the index + 1 of the last character in a sequence of 4 all different characters
# start-of-message marker is the index + 1 of the last character in a sequence of 14 all different characters

# Answer: data 1 - 7, data 2 - 5, data 3 - 6, data 4 - 10, data 5 - 11

# Read the file input.txt and store in a list
with open('input.txt', 'r') as f:
    data = f.read()

# Store the first 4 characters of each data in a list
packet = []

# Loop over each data in the list
counter = 0
for i in data:
    counter += 1
    if len(packet) < 14:
        packet.append(i)
        continue
    else:
        # Remove the first character, move the others to the left and add the next character
        packet.pop(0)
        packet.append(i)
        # Check if the characters are all different
        if len(set(packet)) == len(packet):
            print("The first start-of-message marker is at position : " , counter)
            break
            
    


    
# Loop over each character in the data and check if it is a start-of-packet marker
for i in range(len(data)):
    # If the character is a start-of-packet marker, print the index + 4
    if data[i] != data[i+1]:
        if data[i] != data[i+2] and data[i+1] != data[i+2]:
            if data[i] != data[i+3] and data[i+1] != data[i+3] and data[i+2] != data[i+3]:
                if data[i] != data[i+4] and data[i+1] != data[i+4] and data[i+2] != data[i+4] and data[i+3] != data[i+4]:
                    print("The first start-of-packet marker is at position : " + str(i+4))
                    break


# If the character is a start-of-message marker, print the index + 14
for i in range(len(data)):
    if data[i] != data[i+1]:
        if data[i] != data[i+2] and data[i+1] != data[i+2]:
            if data[i] != data[i+3] and data[i+1] != data[i+3] and data[i+2] != data[i+3]:
                if data[i] != data[i+4] and data[i+1] != data[i+4] and data[i+2] != data[i+4] and data[i+3] != data[i+4]:
                    if data[i] != data[i+5] and data[i+1] != data[i+5] and data[i+2] != data[i+5] and data[i+3] != data[i+5] and data[i+4] != data[i+5]:
                        if data[i] != data[i+6] and data[i+1] != data[i+6] and data[i+2] != data[i+6] and data[i+3] != data[i+6] and data[i+4] != data[i+6] and data[i+5] != data[i+6]:
                            if data[i] != data[i+7] and data[i+1] != data[i+7] and data[i+2] != data[i+7] and data[i+3] != data[i+7] and data[i+4] != data[i+7] and data[i+5] != data[i+7] and data[i+6] != data[i+7]:
                                if data[i] != data[i+8] and data[i+1] != data[i+8] and data[i+2] != data[i+8] and data[i+3] != data[i+8] and data[i+4] != data[i+8] and data[i+5] != data[i+8] and data[i+6] != data[i+8] and data[i+7] != data[i+8]:
                                    if data[i] != data[i+9] and data[i+1] != data[i+9] and data[i+2] != data[i+9] and data[i+3] != data[i+9] and data[i+4] != data[i+9] and data[i+5] != data[i+9] and data[i+6] != data[i+9] and data[i+7] != data[i+9] and data[i+8] != data[i+9]:
                                        if data[i] != data[i+10] and data[i+1] != data[i+10] and data[i+2] != data[i+10] and data[i+3] != data[i+10] and data[i+4] != data[i+10] and data[i+5] != data[i+10] and data[i+6] != data[i+10] and data[i+7] != data[i+10] and data[i+8] != data[i+10] and data[i+9] != data[i+10]:
                                            if data[i] != data[i+11] and data[i+1] != data[i+11] and data[i+2] != data[i+11] and data[i+3] != data[i+11] and data[i+4] != data[i+11] and data[i+5] != data[i+11] and data[i+6] != data[i+11] and data[i+7] != data[i+11] and data[i+8] != data[i+11] and data[i+9] != data[i+11] and data[i+10] != data[i+11]:
                                                if data[i] != data[i+12] and data[i+1] != data[i+12] and data[i+2] != data[i+12] and data[i+3] != data[i+12] and data[i+4] != data[i+12] and data[i+5] != data[i+12] and data[i+6] != data[i+12] and data[i+7] != data[i+12] and data[i+8] != data[i+12] and data[i+9] != data[i+12] and data[i+10] != data[i+12] and data[i+11] != data[i+12]:
                                                    if data[i] != data[i+13] and data[i+1] != data[i+13] and data[i+2] != data[i+13] and data[i+3] != data[i+13] and data[i+4] != data[i+13] and data[i+5] != data[i+13] and data[i+6] != data[i+13] and data[i+7] != data[i+13] and data[i+8] != data[i+13] and data[i+9] != data[i+13] and data[i+10] != data[i+13] and data[i+11] != data[i+13] and data[i+12] != data[i+13]:
                                                        if data[i] != data[i+14] and data[i+1] != data[i+14] and data[i+2] != data[i+14] and data[i+3] != data[i+14] and data[i+4] != data[i+14] and data[i+5] != data[i+14] and data[i+6] != data[i+14] and data[i+7] != data[i+14] and data[i+8] != data[i+14] and data[i+9] != data[i+14] and data[i+10] != data[i+14] and data[i+11] != data[i+14] and data[i+12] != data[i+14] and data[i+13] != data[i+14]:
                                                            print("The first start-of-message marker is at position : " + str(i+14))
                                                            break



        

    



