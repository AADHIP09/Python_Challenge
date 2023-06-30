import os
import csv

# joining path
budget_data = os.path.join(".." , "Resources", "budget_data.csv")

result_file = os.path.join("Analysis", "Py_Bank_Analysis.txt")
# open and read csv
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # skip header row
    print(f"Header: {csv_header}")

    # creating lists to store Month count, Profit/Loss value and change between each row
    months = []
    Profit_Loss = []
    change = []

    #read through each row of data after header
    for row in csvreader:
        Profit_Loss.append(int(row[1]))
        months.append(row[0])

    for x in range(1, len(Profit_Loss)):
        change.append((int(Profit_Loss[x]) - int(Profit_Loss[x-1])))
    
    # calculate average revenue change
    revenue_average = sum(change) / len(change)
    
    # calculate total length of months
    total_months = len(months)

    # greatest increase in revenue
    greatest_increase = max(change)
    # greatest decrease in revenue
    greatest_decrease = min(change)


    # printing the Results to terminal
    print("Financial Analysis")

    print("------------------------")

    print("Total months: " + str(total_months))

    print("Total: " + "$" + str(sum(Profit_Loss)))

    print("Average change: " + "$" + str(revenue_average))

    print("Greatest Increase in Profits: " + str(months[change.index(max(change))+1]) + " " + "$" + str(greatest_increase))

    print("Greatest Decrease in Profits: " + str(months[change.index(min(change))+1]) + " " + "$" + str(greatest_decrease))

#Creating variable to hold values to output to text file
output_txt = (
    f"Financial Analysis\n"
    f"------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${str(sum(Profit_Loss))}\n"
    f"Average  Change: ${str(revenue_average)}\n"
    f"Greatest Increase in Profits: {str(months[change.index(max(change))+1])}$  {str(greatest_increase)}\n"
    f"Greatest Decrease in Profits: {str(months[change.index(min(change))+1])}$ {str(greatest_decrease)}\n"
    f"```\n")

#output to text file
with open(result_file, "a") as txt_file:
    txt_file.write("-----------------------\n")
    txt_file.write(output_txt)
