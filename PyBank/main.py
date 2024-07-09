# Import dependencies
import os
import csv

# Set the path for the file
csvpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Resources', 'budget_data.csv')

# Set the output of the text file
results_txt = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'analysis', 'Final_Analysis.txt')

# Set variables
totalmonths = []
profits = []
pc = []

# Open the budget_data CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        totalmonths.append(row[0])
        profits.append(int(row[1]))

# Calculate the monthly changes in profits
for i in range(len(profits) - 1):
    pc.append(profits[i+1] - profits[i])

# Calculate the results
total_months = len(totalmonths)
sum_profits = sum(profits)
avg_change = round(sum(pc) / len(pc), 2)
greatest_increase = totalmonths[pc.index(max(pc))+1]
greatest_decrease = totalmonths[pc.index(min(pc))+1]
g_increase = max(pc)
g_decrease = min(pc)

# Prepare the output
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Profits: ${sum_profits}\n"
    f"Average Revenue Change: ${avg_change}\n"
    f"Greatest Increase in Profits: {greatest_increase} (${g_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease} (${g_decrease})\n"
)

# Print the results to the terminal
print(output)

# Write the results to a text file
with open(results_txt, 'w') as txtfile:
    txtfile.write(output)
