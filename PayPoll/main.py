# Define the path to the CSV file
csv_file = "election_data.csv"

# Open and read the CSV file
with open(csv_file, "r") as file:
    csv_reader = csv.reader(file)

    # Skip the header row
    next(csv_reader)

    # Loop through each row in the CSV
    for row in csv_reader:
        # Count total votes
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # Check if the candidate is already in the candidates dictionary
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            # If not, add the candidate to the dictionary and set their vote count to 1
            candidates[candidate_name] = 1

# Initialize a variable to store the results
results = []

# Iterate through the candidates and calculate their percentage of votes
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, votes, percentage))

    # Find the candidate with the most votes
for candidate, votes, percentage in results:
    if votes > max_votes:
        max_votes = votes
        winner = candidate

        # Print the results to the console
print("Election Results")
print("-" * 30)
print(f"Total Votes: {total_votes}")
print("-" * 30)

for candidate, votes, percentage in results:
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-" * 30)
print(f"Winner: {winner}")
print("-" * 30)

# Define the output file path
output_file = "election_results.txt"

# Open the file and write the results to it
with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write("-" * 30 + "\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-" * 30 + "\n")

    for candidate, votes, percentage in results:
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    file.write("-" * 30 + "\n")
    file.write(f"Winner: {winner}\n")
    file.write("-" * 30 + "\n")

    