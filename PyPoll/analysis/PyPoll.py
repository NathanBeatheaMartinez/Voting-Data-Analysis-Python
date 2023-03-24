import csv

filepath = '/Users/JA/NU-VIRT-DATA-PT-02-2023-U-LOLC/02-Homework/03-Python/Starter_Code/PyPoll/Resources/election_data.csv'
# Read CSV File
with open(str(filepath)) as csv_file:
    next(csv_file)
    csv_reader = csv.reader(csv_file, delimiter=',')

    

# Create a variable to hold the total votes count
    total_vote_count = 0

# Create an empty list to hold your candidates and empty list to delete duplicate names
    candidate_list = []
    refined_list = []

# Create a variable to hold each candidates vote count
    charles_vote_count = 0
    diana_vote_count = 0
    raymon_vote_count = 0

# Create a variable to hold each candidates name to compare to use for comparative analysis
    candidate_1_name = 'Charles Casper Stockham'
    candidate_2_name = 'Diana DeGette'
    candidate_3_name = 'Raymon Anthony Doane'


# Loops through each row and adds to voter count for each vote
    for row in csv_reader:
            total_vote_count += 1
   

# Loops through 'Candidate' column and adds name to candidate list
            candidate_list.append(row[2])

# Loops through candidates column and adds +1 to count for each time the candidates name appears
            if row[2] == candidate_1_name:
                charles_vote_count += 1
            elif row[2] == candidate_2_name:
                diana_vote_count += 1
            else:
                raymon_vote_count += 1

# Create a variable that calculates each candidates percentage of votes
    charles_vote_percentage = round((charles_vote_count / total_vote_count) * 100, 3)
    diana_vote_percentage = round((diana_vote_count / total_vote_count) * 100, 3)
    raymon_vote_percentage = round((raymon_vote_count / total_vote_count) * 100, 3)

# Create a variable that holds the winner of the election 
    winner = ''
    
    
    print('Election Results')
    print('--------------------------')
    print(f"Total Votes: {total_vote_count}")
    print('--------------------------')

# Loops through candidate_list and removes duplicate names
for name in candidate_list:
    if name not in refined_list:
        refined_list.append(name)
    
# If statement to compare each candidate variable and find greatest value of votes (winner of election)
    if charles_vote_count >= diana_vote_count and charles_vote_count >= raymon_vote_count:
         winner = candidate_1_name
    elif diana_vote_count >= charles_vote_count and diana_vote_count >= raymon_vote_count:
         winner = candidate_2_name
    else:
         winner = candidate_3_name


# Print out analysis to terminal

print(f"{refined_list[0]}: {charles_vote_percentage}% ({charles_vote_count})")
print(f"{refined_list[1]}: {diana_vote_percentage}% ({diana_vote_count})")
print(f"{refined_list[2]}: {raymon_vote_percentage}% ({raymon_vote_count})")
print('--------------------------')
print(f"Winner: {winner}")
print('--------------------------')

with open('PyPoll.txt', 'w') as file:
    file.write(f"\n{refined_list[0]}: {charles_vote_percentage}% ({charles_vote_count})")
    file.write(f"\n{refined_list[1]}: {diana_vote_percentage}% ({diana_vote_count})")
    file.write(f"\n{refined_list[2]}: {raymon_vote_percentage}% ({raymon_vote_count})")
    file.write(f"\nWinner: {winner}")