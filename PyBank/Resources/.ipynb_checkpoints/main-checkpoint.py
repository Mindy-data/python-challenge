import os

import csv

csvpath = os.path.join("budget_data.csv")

#Create Financial Analysis Title
title = "Financial Analysis"
print(title)

#Create line
print("-----------------------------------------------------")

#Read the CSV file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    total_months = 0
    total_prof_loss = 0
    #total_profits = 0
    #total_losses = 0
    
    # Read each row of data after the header
    for row in csvreader:
        
        total_months = total_months + 1
        #print(row)
        
        #The net total profits/losses over entire period
        total_prof_loss = total_prof_loss + int(row[1])
        

        #Changes in profits/losses over entire period and then the average of those changes
        #total_profits = sum(int(row[1]>0)
        #total_losses = sum(int(row[1]<0)
        
        #average_change = total_profits - total_losses / total_months
        
        #average_change.append(str(percent) + "%")

        #Greatest increase in profits over the entire period
        

        #Greatest decrease in profits over the entire period
    
    
    
    
    
    
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_prof_loss}")

