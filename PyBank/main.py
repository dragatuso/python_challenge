#Modules
import os
import csv

#Print title
print("Financial Analysis")
print(" ")
print("-" * 28)
print(" ")

#Set path for file
csvpath = os.path.join('PyBank','budget_data.csv')

#Define a counter for total number of rows to calculate total months
row_count = 0

#Define the total value of the profit/losses
total_profit_losses = 0

#Create a list to store the profit/losses changes
profit_losses_changes = []
#Create a list to store the changes dates
profit_losses_changes_dates = []

#Define current month Profit/Losses value and previous month Profit/Losses value
current_month_value = 0
previous_month_value = 0

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
        
        #Sum the values of profits and losses in each row and accumulate it in the total_profits_losses variable defined
        total_profit_losses = total_profit_losses + int(row[1])

        #From the second row with data, store the changes in profit/losses in the created list
        if row_count != 1:
            profit_losses_changes.append(int(row[1])-previous_month_value)
            profit_losses_changes_dates.append(row[0])
        
        #After the changes calculation, set the new previous value to calculate the difference in the next row
        previous_month_value = int(row[1])
        
    #Print the Total Months and leave a row empty
    print("Total Months: " + str(row_count))
    print(" ")
    
    #Print the net total amount of profits/losses and leave a row empty
    print("Total: " + "$" + str(total_profit_losses))
    print(" ")
    
    #Calculate the average of the changes in profit/losses
    average_profit_losses = sum(profit_losses_changes) / len(profit_losses_changes)
    #Format the value to having 2 decimals
    formatted_value = "{:.2f}".format(average_profit_losses)
    #Print the average change and leave a row empty
    print("Average Change: " + "$" + str(formatted_value))
    print(" ")

    #Calculate the maximum value on the created list
    greatest_increase = max(profit_losses_changes)
    #Calculate the date of greatest increase
    date_greatest_increase = profit_losses_changes_dates[profit_losses_changes.index(greatest_increase)]
    #Print the value and leave a row empty
    print("Greatest Increase in Profits: " + str(date_greatest_increase) + " ($" + str(greatest_increase) + ")")
    print(" ")

    #Calculate the minimum value on the created list
    greatest_decrease = min(profit_losses_changes)
    #Calculate the date of greatest decrease
    date_greatest_decrease = profit_losses_changes_dates[profit_losses_changes.index(greatest_decrease)]
    #Print the value and leave a row empty
    print("Greatest Decrease in Profits: " + str(date_greatest_decrease) + " ($" + str(greatest_decrease) + ")")
    print(" ")