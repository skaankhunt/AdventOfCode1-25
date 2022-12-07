# opponent choice / your choice
# A / X - Rock
# B / Y - Paper
# C / Z - Scissors

#First column is what opponent is going to play
#Second column is what you should play in response

#The winner is the player with highest score
#Total score is the sum of scores for each round
#The score for a single round is the score for the shape you selected
#1 - Rock, 2 - Paper, 3 - Scissors + the score for the outcome of the round (0 if you lost, 3 if the round was a draw, 6 if you won)

#Calculate the score if you follow the Elf's guide

#Read the input.txt file and store the data in a list
with open('input.txt', 'r') as f:
    data = f.readlines()
f.close()

#Remove the newline character from each element in the list
data = [x.strip() for x in data]

#Create a function that calculates the score for a single round
def calculate_score(opponent_choice, your_choice):
    #Create a dictionary to store the scores for each round
    your_scores = {'X': 1, 'Y': 2, 'Z': 3}
    opponent_scores = {'A': 1, 'B': 2, 'C': 3}
    #Calculate the score for the round
    #For draw, add 3 to the score
    if your_scores[your_choice] == opponent_scores[opponent_choice]:
        score = your_scores[your_choice] + 3
    #If not draw
    else:
        #If your choice is rock
        if your_choice == 'X':
            if opponent_choice == 'B':
                score = your_scores[your_choice] + 0
            else:
                score = your_scores[your_choice] + 6
        #If your choice is paper
        if your_choice == 'Y':
            if opponent_choice == 'C':
                score = your_scores[your_choice] + 0
            else:
                score = your_scores[your_choice] + 6
        #If your choice is scissors
        if your_choice == 'Z':
            if opponent_choice == 'A':
                score = your_scores[your_choice] + 0
            else:
                score = your_scores[your_choice] + 6
    #Return the score
    return score

#Find, loop over and calculate your_choice and opponent_choice
total_score = 0
for lines in data:
    total_score += calculate_score(lines[0], lines[2])

#Print the total score
print(total_score)



