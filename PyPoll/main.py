
import os
import csv

total_votes=0
winning_count=0
candidate_option = []
candidate_votes = {}

csvpath = os.path.join('..', 'Resources', 'election_data.csv')
output_file = os.path.join("..", "Analysis","election_data_output.txt")



with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        candidate_list=row[2]
        total_votes=total_votes+1
        if candidate_list not in candidate_option:
            candidate_option.append(candidate_list) 
            candidate_votes[candidate_list]=0
        candidate_votes[candidate_list]=candidate_votes[candidate_list]+1
       
for candidate in candidate_votes:
    votes=candidate_votes.get(candidate)
    vote_percent=float(votes/total_votes)*100
    vote_percent=round(vote_percent,2)
          
    if (votes>winning_count):
        winning_count=votes
        winning_candidate=candidate
        


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


















