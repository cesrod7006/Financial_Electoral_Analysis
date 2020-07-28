#import modules
import os 
import csv

#path for csv file
poll_csv = os.path.join('python-challenge/PyPoll/Resources/election_data.csv')

#create and set intial variables
count=0
candidate_list=[]
unique_candidate=[]
vote_count=[]
vote_percent=[]

#open file with csv reader
with open(poll_csv,newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Read the Header Row First
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

    print('------------------------------------------')
    print('Election Results')
    print('------------------------------------------')
    print('Total Votes:' + str(count))
    print('------------------------------------------')
    print('Candidate ' + 'Percentage of Votes ' + 'Vote Count')
    print(str(unique_candidate[0]) , str(round(vote_percent[0],1))+'%' , str(vote_count[0]))
    print(str(unique_candidate[1]) , str(round(vote_percent[1],1))+'%' , str(vote_count[1]))
    print(str(unique_candidate[2]) , str(round(vote_percent[2],1))+'%' , str(vote_count[2]))
    print(str(unique_candidate[3]) , str(round(vote_percent[3],1))+'%' , str(vote_count[3]))
    print('-------------------------------------------')
    print('Winner:' + str(winner))

with open(os.path.join('python-challenge/PyPoll','Election_Analysis.txt'), 'w') as text:
    text.write('-------------------------------------\n')
    text.write('Election Analysis' + '\n')
    text.write('-------------------------------------\n\n')
    text.write('Candidate ' + 'Percentage of Votes ' + ' Vote Count' + '\n')
    text.write(str(unique_candidate[0]) + str(round(vote_percent[0],1))+'%' + str(vote_count[0]) + '\n')
    text.write(str(unique_candidate[1]) + str(round(vote_percent[1],1))+'%' + str(vote_count[1]) + '\n')
    text.write(str(unique_candidate[2]) + str(round(vote_percent[2],1))+'%' + str(vote_count[2]) + '\n')
    text.write(str(unique_candidate[3]) + str(round(vote_percent[3],1))+'%' + str(vote_count[3]) + '\n')
    text.write('-------------------------------------\n\n')
    text.write('Winner:' + str(winner) + '\n')