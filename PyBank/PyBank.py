# First Import Modules
import os 
import csv

#create path for csv file
budget_csv = os.path.join('budget_data.csv')

#Set Variables
Total_Months=0
Net_P/L=0
Monthly_Change=[]
Monthly_Count=[]
Greatest_Increase=0
Greatest_Increase_Month=0
Greatest_Decrease=0
Greatest_Decrease_Month=0

#open file with csv reader
with open(budget_csv, newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")

    #Read the Header Row First
    csv_header = next(csvreader)

    #Calculate months
    Total_Months += 1





