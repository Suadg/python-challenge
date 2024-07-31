# importing dependency
import os
import csv

# Read the data from the file
csv_path=os.path.join('Resources', 'election_data.csv')  # Update with your file path

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
    file.write("-------------------------\n")# Declare / Import the dependencies
import os
import csv

# Specify the path to the CSV file election_data.csv
file_path = os.path.join('Resources', 'election_data.csv')

# Variables to store total votes
total_votes = 0

# Create a dictionary to store the number of votes each candidate receives
candidates_votes = {}

# Open and read the data of the CSV file.
with open(file_path) as data:
# Initiate the reader
    reader = csv.reader(data, delimiter=",")
# Skip the header row when looping through the data
    header = next(reader)
# Start your loop over the rows to make calculations
    for row in reader:
# Get the candidate name from the current row.
# Names are in index 2
        candidate_name = str(row[2])

# Check if candidate name is in the dictionary. If not, adds candidates with initial count of ceroif candidate_name not in candidates_votes:
candidates_votes[candidate_name] = 0

# Add votes to each candidate in increments of 1 using += operator
candidates_votes[candidate_name] += 1

# Calculate the total votes in increments of 1 using += operator
total_votes += 1

# Print the outcomes in the console
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

#Loop to find out how many votes & % per candidate and print to console
# This loop has to be here rather than before the 'Print outcomes' section
# otherwise, it won't print all of the candidates in the format required
for candidate_name, totalVotesCandidate in candidates_votes.items():

# Calculate the percentage of each candidate's votes
    percent = (totalVotesCandidate / total_votes) * 100
    #Format the percentage to round to 3 decimals
    percentFormat = float(round(percent,3))

# Variable to save the results to print out
    result = f"{candidate_name}: {percentFormat}% ({totalVotesCandidate})"
    print(result)

# Finding out who won and printing it out to console
# Store in 'winner' variable. Use the max function for the maximum value
# Search these values through the candidates_votes dictionary
# Use the get method to retrieve the value associated with the key
winner = max(candidates_votes, key=candidates_votes.get)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Specify the output file path
output_path = os.path.join("analysis", "PyPoll_analysis.txt")

# Open the file in write mode and redirect the print statements to the file
with open(output_path, "w") as textfile:

# Inicialize the txt.writer function to write the variable we created
    csvwriter = csv.writer(textfile)

# Writing the 'Election Results' and the 'Total Votes' to the txt file
# csvwriter.writerow([""])  Write within parenthesis the outcomes to be written
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow(["-------------------------"])

# Writing the candidates with their number of votes and the percentage of such votes
# This for loop has to be repeated here. Otherwise it is not printing
# all of the candidates and their outcome in the format required in the txt file
    for candidate_name, totalVotesCandidate in candidates_votes.items():
        percent = (totalVotesCandidate / total_votes) * 100
        percentFormat = float(round(percent, 3))
        result = f"{candidate_name}: {percentFormat}% ({totalVotesCandidate})"

# Writing the result to the text file
        csvwriter.writerow([f"{result}"])

# Writing the winner with it's format to the txt file
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["-------------------------"])