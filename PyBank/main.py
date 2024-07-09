# Import dependencies
import os
import csv

# Define file paths
csvpath = os.path.join('Resources', 'budget_data.csv')
results_txt = os.path.join('analysis', 'pybank_results.txt')

# Initialize variables
totalmonths = []
profits = []
pc = []

# Method 2 using CSV Module
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    
    for row in csvreader:
        totalmonths.append(row[0])
        profits.append(int(row[1]))

for i in range(len(profits) - 1):
    pc.append(profits[i+1] - profits[i])

total_months = len(totalmonths)
sum_profits = sum(profits)
avg_change = sum(pc) / len(pc)
greatest_increase_month = totalmonths[pc.index(max(pc)) + 1]
greatest_decrease_month = totalmonths[pc.index(min(pc)) + 1]
g_increase = max(pc)
g_decrease = min(pc)

# Prepare the output text
output = (
    f"Financial Analysis\n"
    f"---------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Profits: ${sum_profits}\n"
    f"Average Revenue Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${g_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${g_decrease})\n"
)

# Print the results to the terminal
print(output)

# Write the results to a text file
with open(results_txt, 'w') as txtfile:
    txtfile.write(output)
