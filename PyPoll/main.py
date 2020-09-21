import os
import csv

#Open file
csv_path=os.path.join("election_data.csv")
with open (csv_path) as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=',')
    next(csv_reader, None)

    #Create file with no header
    line=next(csv_reader, None)

    #Set variables
    total_votes=0
    candidate=line[2]
    candidates=[]

    vote_counts=[]

    #Loop through each row 
    for row in csv_reader:
        total_votes=total_votes+1

        candidates.append(line[2])
        
    


print("Election Results")
print("--------------------------")
print(f'Total Votes: {(total_votes)}')
print("--------------------------")
print(candidate_name)


        
