import os
import csv


# To Open the CSV file  
csvpath = os.path.join('Resources/election_data.csv')
with open (csvpath) as csv_file:  
        csv_read = csv.reader( csv_file)  
    
        Data = list(csv_read)
        Headers = Data[0]
        Data.pop(0) 

        Total_Votes = len(Data)
        
################

Candidates = {}
for vote in Data:
    if vote[2] in Candidates.keys():
        Candidates[vote[2]]+=1
    else:
        Candidates[vote[2]]=1

#################
winner = ""
max_vote = 0
candidate_print = []
for c,v in Candidates.items():
    candidate_print.append("{}: {:.3f}% ({})".format(c,v/Total_Votes*100,v))

    if v>max_vote:
        max_vote = v
        winner = c
      
##################
line1 = "Election Results"
line2 = "-------------------------"
line3 = "Total Votes: {}".format(Total_Votes)
line4 = "Winner: {}".format(winner)
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
