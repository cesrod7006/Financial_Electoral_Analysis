#import modules
import os 
import csv

#path for csv file
poll_csv = os.path.join('Resources','election')

#create and set intial variables
count=0
candidate_list=[]
unique_candidate=[]
vote_count=[]
vote_percent=[]

with open(poll_csv,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)

    for row in csvreader:
        #count total votes
        count += 1
        #Get candidates name and put in the list 
        candidate_list.append(row[2])
    
    # Create a set from the candidatelist to get the unique candidate names
    for x in set(candidate_list):
        unique_candidate.append(x)
        # y is the total number of votes per candidate
        y = candidate_list.count(x) 
        vote_count.append(y)
        # z is the percent of total votes per candidate
        z = (y/count)*100
        vote_percent.append(z)

    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]

