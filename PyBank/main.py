#Modules
import os
import csv

#Print title
print("Financial Analysis")
print("-" * 28)

#Set path for file
csvpath = os.path.join('PyBank','budget_data.csv')

#Open the CSV file
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Read all rows and print them
    # for row in csvreader:
    #     print(row)

    
