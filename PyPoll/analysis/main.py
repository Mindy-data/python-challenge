import os

import csv

csvpath = os.path.join("Resources","election_data.csv")
txtpath = os.path.join("analysis","voting_analysis.txt")

percentage = []
total_votes = 0
won_votes = 0
winner = ""
candidates = {}


#Read the CSV file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    #My for loop to total up total_votes
    for row in (csvreader):
        voter_id, county, candidate = row

        total_votes= total_votes + 1
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

    #My for loop to capture the # of votes, the winner votes and the percentage of the vote        
    #add .items so you don't write over the keys (candidate names)
    for w, w_v in candidates.items():
        percentage.append((w_v/ total_votes) * 100)
        if w_v > won_votes:
            winner = w
            won_votes = w_v

#Keys are the names of the candidates, this stores the names into a list
candidates_names = list(candidates.keys())


output=(
    f"Election Results\n"
    f"--------------------------\n"
    f"Total Votes:{total_votes}\n"
    f"--------------------------\n"
    f"{candidates}: {percentage}% {(won_votes)}\n"
    f"--------------------------\n"
    f"Winner: {winner}\n"
    f"--------------------------\n"
)


with open(txtpath,"w") as txtfile:
    txtfile.write(output)


print(output)