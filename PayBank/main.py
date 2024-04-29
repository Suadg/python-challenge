import os 
import csv
budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")

# Open and read csv
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csv_reader:

# Define variables      
dates = []
totalmonths = 0 
totalprofit = 0
totalchanges = 0
newvalue = 0
lastmonthprofit = None
grtsincrease = ['',0]
grtsdecrease = ['',9999999999]

for row in csv_reader:
       
        dates.append(row [0])
        value = int(row[1])
        totalprofit += value
        if lastmonthprofit is not None:
            change = value - lastmonthprofit
            totalchanges = change
            newvalue += 1
            if change > grtsincrease [1]:
                grtsincrease = (row[0], change)
            if change < grtsdecrease [1]:
                grtsdecrease = (row[0], change)

        lastmonthprofit = value
totalmonths = len(dates)
if newvalue >0:
    averagechanges = totalchanges/newvalue
else:
    averagechanges = 0

#Print Headers
print("Financial Anlysis")
print('-----------------------')

#Print total months
print(f'Total Months: {totalmonths}')
print(f'Total: {totalprofit}')
print(f'Average Change: {averagechanges}')
print(f'Greateest Increase: {grtsincrease}')
print(f'Greateest Decrease: {grtsdecrease}')

#Print in textile
output = open('PybankLP.txt', 'w')
output.write("Financial Anlysis\n")
output.write('-----------------------')
output.write(f'Total Months: {totalmonths}\n')
output.write(f'Total: {totalprofit}\n')
output.write(f'Average Change: {averagechanges}\n')
output.write(f'Greateest Increase: {grtsincrease}\n')
output.write(f'Greateest Decrease: {grtsdecrease}\n')
