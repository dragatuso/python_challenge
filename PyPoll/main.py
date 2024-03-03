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
vote_count = 0

#Create a list for storing the cadidates' names
candidates = []



#Open the CSV file
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Read the header row first
    csv_header = next(csvreader)
    
    #Read each row of data after the header
    #Loop thorugh the rows in the CSV file
    for row in csvreader:
        #Count the number of rows which are equivalent to the number of votes
        vote_count = vote_count + 1

        #Fill the list with the name of the candidates every time we loop through a new name, but only if that name is not already part of the list
        if candidates.count(row[2]) < 1:
           candidates.append(row[2])

                
    #print(candidates)
                
                


    
    #Print total votes, the line formats and empty rows below
    print("Total Votes: " + str(vote_count))
    print(" ")
    print("-" * 25)
    print(" ")