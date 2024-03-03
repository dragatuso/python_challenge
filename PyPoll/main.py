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

#Define values for storing the votes of each candidate
charles_votes = 0
diana_votes = 0
raymond_votes = 0

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

        if row[2] == "Charles Casper Stockham":
            charles_votes = charles_votes + 1

        elif row[2] == "Diana DeGette":
            diana_votes = diana_votes + 1

        elif row[2] == "Raymon Anthony Doane":
            raymond_votes = raymond_votes + 1

    #Calculate the % of votes obtained by each candidate
    charles_votes_perc=charles_votes/vote_count*100
    diana_votes_perc=diana_votes/vote_count*100
    raymond_votes_perc=raymond_votes/vote_count*100

    #Format the % above to having 3 decimals
    charles_votes_perc_formatted_value = "{:.3f}".format(charles_votes_perc)
    diana_votes_perc_formatted_value = "{:.3f}".format(diana_votes_perc)
    raymond_votes_perc_formatted_value = "{:.3f}".format(raymond_votes_perc)
                          
    #Print total votes, the line formats and empty rows below
    print("Total Votes: " + str(vote_count))
    print(" ")
    print("-" * 25)
    print(" ")

    #Print votes and % received by each candidate
    print("Charles Casper Stockham: " + str(charles_votes_perc_formatted_value)+"% " + "(" +str(charles_votes)+")")
    print(" ")
    print("Diana DeGette: " + str(diana_votes_perc_formatted_value)+"% " + "(" +str(diana_votes)+")")
    print(" ")
    print("Raymon Anthony Doane: " + str(raymond_votes_perc_formatted_value)+"% " + "(" +str(raymond_votes)+")")
    print(" ")
    print("-" * 25)
    print(" ")