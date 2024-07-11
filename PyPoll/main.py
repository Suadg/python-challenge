import pandas as pd 

# Filepath to the CSV file
filepath= "./PyPoll/Resources/election_data.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(filepath, sep=",")

# Calculate total votes
total_votes = df['Ballot ID'].count()

# Get unique candidates
candidates = df['Candidate'].unique()

# Calculate the number of votes per candidate
number_of_votes_per_candidate = df.groupby('Candidate').agg({'Ballot ID' : 'count'})

# Calculate the percentage of votes per candidate
percentage_per_candidate = (number_of_votes_per_candidate['Ballot ID'] / total_votes) * 100

# Sort the percentages in descending order
percentage_per_candidate = percentage_per_candidate.sort_values(ascending=False)

# Get the winner
winner = percentage_per_candidate.index[0]

# Create a new DataFrame with the results
results_df = pd.DataFrame({
    'Candidate': percentage_per_candidate.index,
    'Percentage of Votes': percentage_per_candidate.values,
    'Total Votes': number_of_votes_per_candidate['Ballot ID'].values
})

# Add a column with the formatted percentage of votes
results_df['Percentage of Votes'] = results_df['Percentage of Votes'].map('{:.3f}%'.format)

# Create the election results as a string
results_str = f'''
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
'''

for index, row in results_df.iterrows():
    results_str += f"{row['Candidate']}: {row['Percentage of Votes']} ({row['Total Votes']})\n"

results_str += f'''
-------------------------
Winner: {winner}
-------------------------
'''

# Write the results to a CSV file
with open('./PyPoll/analysis/election_results.csv', 'w') as f:
    f.write(results_str)
