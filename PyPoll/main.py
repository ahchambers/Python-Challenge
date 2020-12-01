import os
import csv

#Create counters
total_votes=0
candidate_options=[]
candidate_votes={}
winning_candidate=""
winning_count=0

#Create file to save
file_to_output=os.path.join("Analysis", "Voting_Analysis.txt")


#Open file
csv_path=os.path.join("Resources", "election_data.csv")
with open (csv_path) as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=',')
    next(csv_reader, None)

    #Create file with no header
    line=next(csv_reader, None)

    #Loop through each row and calculate summary info
    for row in csv_reader:
        total_votes=total_votes+1
        candidate_name=row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]=candidate_votes[candidate_name]+1

with open(file_to_output, "w") as txt_file:

    #Print votes
    votes=(
    f"Election Results\n"
    f"--------------------------\n"
    f"Total Votes: {(total_votes)}\n"
    f"--------------------------\n")
    print(votes)
    txt_file.write(votes)

    #Loop through each row and determine winner
    for candidate in candidate_votes:
        votes=candidate_votes.get(candidate)
        vote_percentage=float(votes)/float(total_votes)*100

        if (votes > winning_count):
            winning_count=votes
            winning_candidate=candidate

        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)
        txt_file.write(voter_output)

    #Print winner
    winner=(
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"-------------------------\n"
    )
    print(winner)
    txt_file.write(winner)


