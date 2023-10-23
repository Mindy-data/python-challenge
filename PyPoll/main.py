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

output=(
    f"Election Results\n"
    f"--------------------------\n"
    f"Total Votes:{total_votes}\n"
    f"--------------------------\n"
)

with open(txtpath,"w") as txtfile:
    txtfile.write(output)
    print(output)

    
    for w, w_v in candidates.items():
            percentage= w_v/ total_votes * 100
            output = (
                f"{w}: {percentage:.3f}% {(w_v)}\n"

            )
            txtfile.write(output)
            print(output)
            if w_v > won_votes:
                winner = w
                won_votes = w_v

    output=(
        f"--------------------------\n"
        f"Winner: {winner}\n"
        f"--------------------------\n"

    )
    txtfile.write(output)
    print(output)