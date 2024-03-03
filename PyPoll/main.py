#Modules
import os
import csv

#Print title
print("Election Results")
print(" ")
print("-" * 25)
print(" ")

#Set path for file
csvpath = os.path.join('PyPoll','Resources/election_data.csv')

#Define a counter for total number of rows to calculate total votes
votes_count = 0

#Open the CSV file
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Read the header row first
    csv_header = next(csvreader)
    