# import dependencies
import os
import csv

# the election data is in a folder called Resources that lives at the same level as main.py
election_data_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Resources', 'election_data.csv')
# Define file paths
csvpath = os.path.join('Resources', 'election_data.csv')
results_txt = os.path.join('analysis', 'pypoll_results.txt')

totalVotes = 0 # total rows 

# empty dictionary to catch votes should be:
# votesPerCandidate = {
#   "candidate_one": votes as int
# }
votesPerCandidate = {}

# open the election_data
with open(election_data_csv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

# Read the header row first
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

# Read each row of data after the header
    for row in csvreader:
        totalVotes += 1
        if row[2] not in votesPerCandidate:
            votesPerCandidate[row[2]] = 1
        else:
            votesPerCandidate[row[2]] += 1   
        
