import os
import csv

# Define the path to the CSV file
csvpath = os.path.join('Resources/election_data.csv')

# Open the CSV file
with open (csvpath) as csv_file:  
    # Read the CSV data        
        csv_read = csv.reader( csv_file)  
    # Convert the CSV data into a list
        Data = list(csv_read)
    # Extract the headers and remove them from the data    
        Headers = Data[0]
        Data.pop(0) 
    # Calculate the total number of votes
        Total_Votes = len(Data)
        
#################

# Create a dictionary to store candidate votes

Candidates = {}
for vote in Data:
    if vote[2] in Candidates.keys():
        Candidates[vote[2]]+=1
    else:
        Candidates[vote[2]]=1

#################

# Find the winner and their total votes
winner = ""
max_vote = 0
candidate_print = []

# Calculate the percentage of votes for each candidate and determine the winner
for c,v in Candidates.items():
    candidate_print.append("{}: {:.3f}% ({})".format(c,v/Total_Votes*100,v))

    if v>max_vote:
        max_vote = v
        winner = c
      
##################

# Prepare the output lines
line1 = "Election Results"
line2 = "-------------------------"
line3 = "Total Votes: {}".format(Total_Votes)
line4 = "Winner: {}".format(winner)

# Print the results to the console
print(line1)
print(line2)
print(line3)
print(line2)
for line in candidate_print:
   print(line)
print(line2)   
print(line4)
print(line2)
###############

# Write the results to a text file
with open("./analysis/analysis.txt", "w") as file:
    file.write(line1+"\n")
    file.write(line2+"\n")
    file.write(line3+"\n")
    file.write(line2+"\n")
    for line in candidate_print:
        file.write(line+"\n")    
    file.write(line2+"\n") 
    file.write(line4+"\n") 
    file.write(line2)      
