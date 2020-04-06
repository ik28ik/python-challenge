# Dependencies
import os
import csv

# Set variables
total_votes=0
winning_count=0
candidate_option = []
candidate_votes = {}

# Files to load and output
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
output_file = os.path.join("..", "Analysis","election_data_output.txt")


# Read the csv and convert it into a list of dictionaries
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Extract the candidate name from each row
    for row in csvreader:
        candidate_list=row[2]
        total_votes=total_votes+1
        #  If the candidate does not match any existing candidate then add it to the list of candidates in the running
        if candidate_list not in candidate_option:
            candidate_option.append(candidate_list) 
            candidate_votes[candidate_list]=0
        candidate_votes[candidate_list]=candidate_votes[candidate_list]+1

  # Retrieve vote count and percentage      
for candidate in candidate_votes:
    votes=candidate_votes.get(candidate)
    vote_percent=float(votes/total_votes)*100
    vote_percent=round(vote_percent,2)

     # Determine winning vote count and candidate      
    if (votes>winning_count):
        winning_count=votes
        winning_candidate=candidate
        

# Print the output (to terminal)
print("\nElection Results\n")
print("-----------------------------------\n")
print(f'Total Votes: {total_votes}\n')
print("-----------------------------------\n")
for candidate in candidate_votes:
    votes=candidate_votes.get(candidate)
    vote_percent=float(votes/total_votes)*100
    vote_percent=round(vote_percent,2)
        
    print(candidate, vote_percent, votes)
print("\n-----------------------------------\n")
print(f'Winner: {winning_candidate}\n')
print("-----------------------------------")


# Print the results and export the data to our text file
with open(output_file,"w", newline='') as txt_file:
    writer=csv.writer(txt_file)

    print("\nElection Results\n", file=txt_file)
    print("-----------------------------------\n", file=txt_file)
    print(f'Total Votes: {total_votes}\n', file=txt_file)
    print("-----------------------------------\n", file=txt_file)
    for candidate in candidate_votes:
        votes=candidate_votes.get(candidate)
        vote_percent=float(votes/total_votes)*100
        vote_percent=round(vote_percent,2)
        
        print((candidate, vote_percent, votes), file=txt_file)
    print("\n-----------------------------------\n", file=txt_file)
    print(f'Winner: {winning_candidate}\n', file=txt_file)
    print("-----------------------------------", file=txt_file)


















