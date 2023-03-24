import csv

filepath = '/Users/JA/NU-VIRT-DATA-PT-02-2023-U-LOLC/02-Homework/03-Python/Starter_Code/PyBank/Resources/budget_data.csv'
# Read CSV File
with open(str(filepath)) as csv_file:
    next(csv_file)
    csv_reader = csv.reader(csv_file, delimiter=',')

# Create a variable that hold profit/loss column
    profit_losses = []
    
#Create a variable that holds date values
    dates = []
# Create counter to keep track of total month count
    month_counter = 0

# Create Variable that hold total profit/losses
    total_amount = 0

#Create Greatest Profit variable set equal to 0
    greatest_profit = 0

# Create a variable that hold greatest increase index
    greatest_increase_index = 0

#Create greatest profit date value which is the date that corresponds with greatest increase month to month
    greatest_profit_date = ""

#Create Greatest Decrease variable set equal to 0
    greatest_decrease = 0
# Create a variable to hold the indec for greatest decrease 
    greatest_decrease_index = 0
#Create greatest decrease date value which is the date that corresponds with greatest decrease month to month month to month
    greatest_decrease_date = ""
    
#Create a list that holds the changes in value each month to month set equal to empty list
    month_to_month = []

#Create a variable that holds the sum of month to month
    month_to_month_sum = 0
# Loops through each row and adds 1 to month counter
    for row in csv_reader:
        month_counter += 1

# add each profit/loss value to profit loss list
        profit_losses.append(row[1])

# add each date to dates list
        dates.append(row[0])

# Loops through 'profit/loss' column and adds/subtracts from total_amount variable
        total_amount += int(row[1])

# Loops through profit/loss column and subtracts the next cell from the previous to get the change from month to month
        #month_to_month.append((int(row[1]) + 1) - int(row[1]))

# Loops through profit_losses and finds the difference between the next cell and the current cell
for i in range(len(profit_losses) - 1):

# Loops through profit/loss column and subtracts the next cell from the previous to get the change from month to month
    month_to_month.append(int((profit_losses[i + 1])) - int(profit_losses[i]))
    

# Loops through and adds all the month to month changes together 
for i in range(len(month_to_month)):
    month_to_month_sum += month_to_month[i]

# Loops through 'profit/loss' column and compares each value to one another to find the greatest value
    if greatest_profit >= int(month_to_month[i]):
        greatest_profit += 0
    else:
        greatest_profit = int(month_to_month[i])
        greatest_increase_index = i
        

# Loops through 'profit/loss' column and compares each value to one another to find the smallest value
    if greatest_decrease <= int(month_to_month[i]):
        greatest_decrease += 0
    else:
        greatest_decrease = int(month_to_month[i])
        greatest_decrease_index = i
        


greatest_decrease_date = dates[greatest_decrease_index + 1]
greatest_profit_date = dates[greatest_increase_index + 1]
    
        


# Finds the average of month to month list
average_change = round(int(month_to_month_sum)/int(month_counter - 1), 2)

# Print out analysis to terminal

print('Financial Analysis')

print('-----------------------------------')

print(f"Total Amount: {total_amount}")

print(f"Total Months: {month_counter}")

print(f"Greatest increase in profits: {greatest_profit_date} (${greatest_profit})")

print(f"Greatest decrease in profits: {greatest_decrease_date} (${greatest_decrease})")

print(f"Average Change: ${average_change}")

#print(month_to_month)

# Write to text file

with open('PyBank.txt', 'w') as txtfile:
    txtfile.write(f"Total Amount: {total_amount}\n\n")
    txtfile.write(f"Total Months: {month_counter}")
    txtfile.write(f"Greatest increase in profits: {greatest_profit_date} (${greatest_profit})\n")
    txtfile.write(f"Greatest decrease in profits: {greatest_decrease_date} (${greatest_decrease})\n")
    txtfile.write(f"Average Change: ${average_change}\n")

