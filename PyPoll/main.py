import os
import csv

# Read the data from the file
csv_path = os.path.join('Resources', 'election_data.csv')  # Update with your file path

# Initialize variables
total_votes = 0
candidates = {}
winner_name = ""
winner_votes = 0

# Open the CSV file and perform calculations
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)  # Skip the header row
    for row in csvreader:
        # Count total votes
        total_votes = total_votes + 1

        # Get candidate name from row
        candidate_name = row[2]

        # Increment votes for candidate or add candidate if not present
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else:
            candidates[candidate_name] = candidates[candidate_name] + 1

        # Update winner information
        if candidates[candidate_name] > winner_votes:
            winner_name = candidate_name
            winner_votes = candidates[candidate_name]

# Calculate total votes and votes for each candidate
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    candidates[candidate] = {"votes": votes, "percentage": percentage}

# Print results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, stats in candidates.items():
    print(f"{candidate}: {stats['percentage']:.3f}% ({stats['votes']})")
print("-------------------------")
print(f"Winner: {winner_name}")
print("-------------------------")

# Export results to the PyPoll_results.txt
with open("analysis/PyPoll_results.txt", "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n") 
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, stats in candidates.items():
        file.write(f"{candidate}: {stats['percentage']:.3f}% ({stats['votes']})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner_name}\n")
    file.write("-------------------------\n")