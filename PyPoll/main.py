# import dependencies
import os
import csv

# Set the path for the file
election_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Resources', 'election_data.csv')
# Set the output of the text file
results_txt = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'analysis', 'Final_Analysis.txt')

# Create dictionaries to store data
total_votes = 0
candidate_options = []
total_votes_candidates = {}

# Open and read csv
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)  # Skip header row
    
# Loop through each row in the CSV file
    for row in csvreader:
        try:
            # Check if the row has at least 3 columns (index 2 exists)
            if len(row) >= 3:
                # Add to the total vote count
                total_votes += 1

                # Get the candidate name from each row (assuming candidate name is in the third column, index 2)
                candidate_name = row[2]

                # If the candidate does not match any existing candidate...
                if candidate_name not in candidate_options:
                    # Add to the list of candidates
                    candidate_options.append(candidate_name)

                    # Initialize candidate's vote count
                    total_votes_candidates[candidate_name] = 0

                # Add a vote to that candidate's count
                total_votes_candidates[candidate_name] += 1
            else:
                print(f"Issue with row: {row}")  # Print a message for rows with less than 3 columns

        except IndexError:
            print(f"IndexError: {row}")  # Print the row causing the IndexError
            continue  # Skip this row and move to the next one

# Open the output file and write the results
with open(results_txt, "w") as txt_file:
# Print the final vote count to the terminal.
    election_results = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n"
    )
    print(election_results, end="")
    
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    
    # Initialize variables for tracking the winning candidate
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0

    # Iterate through each candidate and calculate their vote percentage
    for candidate_name in candidate_options:
        # Retrieve vote count for the candidate
        votes = total_votes_candidates[candidate_name]

        # Calculate the percentage of votes received
        vote_percentage = (votes / total_votes) * 100

        # Generate candidate results string
        candidate_results = f"{candidate_name}: {vote_percentage:.3f}% ({votes:,})\n"

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)

        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and winning candidate.
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.3f}%\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

