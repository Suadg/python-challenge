# import dependencies
import os
import csv

# Set the path for the file
csvpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Resources', 'election_data.csv')

# Set the output of the text file in the 'analysis' folder
output_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'analysis')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

results_txt = os.path.join(output_folder, 'Final_Analysis.txt')

# Create lists to store data

# Votes
total_votes = 0

# A complete list of candidates who received votes 
candidate_options = []

# The percentage of votes each candidate won 
candidate_vote_percentages = []

# The total number of votes each candidate won
total_votes_candidates = {}

# The winner of the election based on popular vot
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvfile)
    
# Print each row in the CSV file.
    for row in csvreader:
        
        # Add total votes
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add to the list of candidates
            candidate_options.append(candidate_name)
            
            # Candidate's vote count
            total_votes_candidates[candidate_name] = 0

        # Add a vote to that candidates's count
        total_votes_candidates[candidate_name] += 1
        
        # Set variable for output file
output_file = os.path.join("analysis", "election_analysis.txt")

with open(output_file, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:}\n"
        f"-------------------------\n"
    )
    print(election_results, end="")
    
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    
    for candidate_name in total_votes_candidates:
        # Retrieve vote count and percentage.
        votes = total_votes_candidates[candidate_name]
        candidate_vote_percentages = float(votes) / float(total_votes) * 100
        candidate_results = f"{candidate_name}: {candidate_vote_percentages:.1f}% ({votes:})\n"

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        
    # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (candidate_vote_percentages > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = candidate_vote_percentages
            
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)
    
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)