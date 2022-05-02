#add our dependencies
import csv
import os

#assign a variable to load a file from a path
file_to_load = os.path.join("resources", "election_results.csv")

#assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")


#initialize a total vote counter.
total_votes = 0

#candidate options
candidate_options = []
#Declare the empty dictionary
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)


    #read and print the header row
    headers = next(file_reader)


    #print each row in the cvs file
    for row in file_reader:
        #2. add to the total vote counter
        total_votes += 1 

        #print the candidate name from each row
        candidate_name = row[2]

        #if the candidate does not match any existing condidate...
        if candidate_name not in candidate_options:
            #add it to the list of candidates
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        #add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

#print the candidate lists
print(candidate_votes)

#determine the percentage of votes for each candidate by looping through the counts.
#1. iterate through the candidate list.
for candidate_name in candidate_votes:
    #2. retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    #3. Calculate the percentage of votes.
    votes_percentage= float(votes) / float(total_votes) * 100

    #to do: print out each candidate's name, vote count, and percentage of 
    #votes to the terminal

    if (votes > winning_count) and (votes_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = votes_percentage
        winning_candidate = candidate_name
    #4. print the candidate name and percentage of votes
    print(f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
