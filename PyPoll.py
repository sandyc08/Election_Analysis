# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of all candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular vote.

# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: perform analysis.
    print(election_data)

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
        file_reader = csv.reader(election_data)

        # Read the header row.
        headers = next(file_reader)

        # Print each row in the CSV file.
        for row in file_reader:
            # Add to the total vote count.
            total_votes += 1
        
            # Print the candidate name from each row.
            candidate_name = row [2]

            if candidate_name not in candidate_options:
                # Add it to the list of the candidates.
                candidate_options.append(candidate_name)
                # 2. Begin tracking that candidate's vote count.
                candidate_votes[candidate_name] = 0
            # 3. Add a vote to that candidate's count.
            candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:
#Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Print the candidate_vote dictionary
    print(candidate_votes)

    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidate, their voter count, and percentage to the 
        # terminal             
        # Determine winning vote count, winning percentage and candidate
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        # save the candidate results to our text file.
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        # Print the winning_candidates' results to the terminal.
        winning_candidate_summary = (
            f"------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n")
    
    # print(winning_candidate_summary)
    # save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)