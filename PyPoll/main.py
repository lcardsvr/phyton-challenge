import csv
import os

# Path for the source data
csvpath=os.path.join('Resources','election_data.csv')

# # Read file from election_data.csv file


with open(csvpath, newline='') as f:
    reader = csv.reader(f)
    election_data = list(reader)


# print(election_data)

# Ballot_ID_list contains the list with ballot IDs - Available but not required for calculations
# County_list contains the list with Counties where election votes took place - Available but not required for calculations
# Candidate_list contains the list of Candidates that obtained a vote

Ballot_ID_list =[]
County_list =[]
Candidate_list =[]

#list_length Contails the number of rows + 1 (as it has a header)

list_length= len(election_data)



for row in range(1,list_length):
    Ballot_ID_list.append(election_data[row][0])
    County_list.append(election_data[row][1])
    Candidate_list.append(election_data[row][2])


# The list "candidates" contains the names of the people who received a vote
candidates = []


#The cycle verifies if the candidate being checked does not exist and adds it
#to the list if that is the case

for candidate in Candidate_list:
    if not candidate in candidates:
        candidates.append(candidate)


# The total number of candidates is the length of the "candidates" list
num_candidates = len(candidates)

# The list "votes" contains the total number of votes 

votes=[]

#The cycle counts the number of votes per candidate

for candidate in candidates:
    votes.append(Candidate_list.count(candidate))


# print (candidates)
# print(votes)

# The list "vote_percentage" contains the percentage of votes per candidate

vote_percentage=[]

#Total number of votes
total_votes = sum (votes)

for vote in votes:
    vote_percentage.append(vote/total_votes*100)


# print (vote_percentage)

# The position of the winner in the list is where the maximum percentage is found
pos_winner = vote_percentage.index(max(vote_percentage))

print (pos_winner)


## In screen summary

print ("Election Results\n")
print ("-------------------------\n")
print (f"Total Votes: {total_votes}\n")
print ("-------------------------\n")

## Loop to get Candidate with his/her vote percetange and total votes

for i in range(num_candidates):
    print (f"{candidates[i]}: {vote_percentage[i]:.3f}% ({votes[i]})\n")

## Gets the candidates with the maximum number of votes as the winner
print ("-------------------------\n")
print (f"Winner: {candidates[pos_winner]}\n")
print ("-------------------------\n")


#### In File summary Writing

#Output path information \analysis\results.txt
output_path=os.path.join('analysis','results.txt')

file = open(output_path,"w")

file.write ("Election Results\n")
file.write ("-------------------------\n")
file.write (f"Total Votes: {total_votes}\n")
file.write ("-------------------------\n")

## Loop to get Candidate with his/her vote percetange and total votes

for i in range(num_candidates):
    file.write (f"{candidates[i]}: {vote_percentage[i]:.3f}% ({votes[i]})\n")

## Gets the candidates with the maximum number of votes as the winner
file.write ("-------------------------\n")
file.write (f"Winner: {candidates[pos_winner]}\n")
file.write ("-------------------------\n")

file.close()

