import os
import csv

# Print the current working directory
print("Current Working Directory:", os.getcwd())

# Specify the path to the CSV file election_data.csv
csv_path = os.path.join('Resources', 'election_data.csv')

# Initialize variables
total_votes = 0
candidates_votes = {}

# Open and read the data from the CSV file
with open(csv_path) as data:
    reader = csv.reader(data, delimiter=",")
    header = next(reader)  # Skip the header row

    # Loop over the rows to make calculations
    for row in reader:
        candidate_name = row[2]  # Get the candidate name from the current row

        # Check if candidate name is in the dictionary. If not, add it with an initial count of zero
        if candidate_name not in candidates_votes:
            candidates_votes[candidate_name] = 0

        # Add votes to each candidate in increments of 1
        candidates_votes[candidate_name] += 1

        # Calculate the total votes in increments of 1
        total_votes += 1

# Print the outcomes in the console
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Loop to find out how many votes & percentage per candidate and print to console
for candidate_name, votes in candidates_votes.items():
    percent = (votes / total_votes) * 100
    print(f"{candidate_name}: {percent:.3f}% ({votes})")

# Finding out who won
winner = max(candidates_votes, key=candidates_votes.get)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Specify the output file path
output_path = os.path.join("analysis", "PyPoll_analysis.txt")

# Open the file in write mode and redirect the print statements to the file
with open(output_path, "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("-------------------------\n")
    for candidate_name, votes in candidates_votes.items():
        percent = (votes / total_votes) * 100
        textfile.write(f"{candidate_name}: {percent:.3f}% ({votes})\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("-------------------------\n")
