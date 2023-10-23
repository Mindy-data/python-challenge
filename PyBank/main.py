import os

import csv

csvpath = os.path.join("Resources","budget_data.csv")
txtpath = os.path.join("analysis","budget_analysis.txt")

total_months = 0
total_prof_loss = 0


l_profit= []
losses= []

greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
    
#Read the CSV file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    first=next(csvreader)
    total_months = total_months + 1
    total_prof_loss = total_prof_loss + int(first[1])
    previous = int(first[1])

    
    # Read each row of data after the header
    for row in csvreader:
        
        total_months = total_months + 1
        
        #The net total profits/losses over entire period
        total_prof_loss = total_prof_loss + int(row[1])
        
        #Changes in profits/losses over entire period and then the average of those changes
        netchange = int(row[1]) - previous
        l_profit += [netchange]
        previous = int(row[1])
        
    
        #Greatest increase in profits over the entire period
        if netchange > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = netchange
        

        #Greatest decrease in profits over the entire period
        if netchange < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = netchange
    
#Calculate the average change    
average_change = sum(l_profit) / len(l_profit)
  
#All of my print statements    
output = (
    f"Financial Analysis\n"
    f"------------------------------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_prof_loss}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )

with open(txtpath,"w") as txtfile:
 txtfile.write(output)


 print(output)
 print(average_change)

