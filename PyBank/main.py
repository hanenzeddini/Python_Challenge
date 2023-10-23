import os
import csv
# Initialize the variable to store net profit
Net_Profit = 0

# Define the path to the CSV file
csvpath = os.path.join('Resources/budget_data.csv')

# Open the CSV file
with open (csvpath) as csv_file:  
        csv_read = csv.reader( csv_file) 

        # Read the CSV data and extract headers 
        Data = list(csv_read)
        Headers = Data[0]

        # Remove headers from the data
        Data.pop(0) 

         # Calculate the total number of months
        Total_Months = len(Data)
       
#############   
# Calculate the net profit by summing up all the profits/losses     
for i in range (0, len(Data)):
    Net_Profit += int(Data[i][1])

############
# Initialize variables for calculating changes
Changes = 0


# Calculate the sum of changes between months
for i in range (0,len(Data)-1):
    Changes += int(Data[i+1][1]) - int(Data[i][1])

 # Calculate the average change   
Avg_changes = Changes / (len (Data)-1) 

############

# Initialize variables to track the greatest increase and decrease in profits
Greatest_Increase = 0
Greatest_Increase = 0
Date_Increase =""

# Find the greatest increase and decrease in profits
for i in range (0,len(Data)-1):
    Increase = int(Data[i+1][1]) - int(Data[i][1])
    if Increase > Greatest_Increase:
        Greatest_Increase = Increase
        Date_Increase = Data[i+1][0]

Greatest_Decrease = 0
Date_Decrease =""
for i in range (0,len(Data)-1):
    Decrease = int(Data[i+1][1]) - int(Data[i][1])
    if Decrease < Greatest_Decrease:
        Greatest_Decrease = Decrease
        Date_Decrease = Data[i+1][0]
      
##############

# Prepare the output lines  
line1 = "Financial Analysis"
line2 = "----------------------------"
line3 = "Total Months: {}".format(Total_Months)
line4 = "Total: ${}".format(Net_Profit)
line5 = "Average Change: ${:.2f}".format(Avg_changes)
line6 = "Greatest Increase in Profits: {} (${})".format(Date_Increase,Greatest_Increase)
line7 = "Greatest Decrease in Profits: {} (${})".format(Date_Decrease,Greatest_Decrease)

# Print the results to the console
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(line7)
#############

# Write the results to a text file
with open("./analysis/analysis.txt", "w") as file:
     file.write(line1+"\n")
     file.write(line2+"\n")
     file.write(line3+"\n")
     file.write(line4+"\n")
     file.write(line5+"\n")
     file.write(line6+"\n")
     file.write(line7)