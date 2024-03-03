#Modules
import os
import csv

#Print title
print("Financial Analysis")
print("-" * 28)

#Set path for file
csvpath = os.path.join('PyBank','budget_data.csv')

#Define a counter for total number of rows to calculate total months
row_count = 0

#Define a sum for total profits/losses
total_profit_losses = 0

#Define a variable to calculate the greatest increase
greatest_increase = 0

#Define a list with the profit/losses changes
profit_losses_changes = []

#Open the CSV file
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Read the header row first
    csv_header = next(csvreader)
        
    #Read each row of data after the header
    #Loop thorugh the rows in the CSV file
    for row in csvreader:
        #Count the number of rows
        row_count = row_count + 1
        #sum the values of profits and losses in each row and accumulate it in the total_profits_losses variable defined
        total_profit_losses = total_profit_losses + int(row[1])
    
    #Print the Total Months
    print("Total Months: " + str(row_count))

    #Print the net total amount of profits/losses
    print("Total: " + "$" + str(total_profit_losses))
    
