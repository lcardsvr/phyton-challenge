import csv
import os


# Path for the source data
csvpath=os.path.join('Resources','budget_data.csv')

# # Read file from budget_date.csv file

with open(csvpath, newline='') as f:
    reader = csv.reader(f)
    budgetdata = list(reader)

# Date_List contains the list with dates
# pl_list contains the list with Profit/Losses per month

date_list =[]
pl_list =[]

#list_length Contails the number of rows + 1 (as it has a header)

list_length= len(budgetdata)



for date in range(1,list_length):
    date_list.append(budgetdata[date][0])
    pl_list.append(budgetdata[date][1])


# Converting each value in the Profit/losses to integer

for i in range (len(pl_list)):
    pl_list[i]=int(pl_list[i])


# Change contains the list of monthly change (i.e Change(i) = PL Value(month(i)-PL Value(month(i-1) ))
Change = []

for i in range (1,len(pl_list)):
    Change.append(pl_list[i]- pl_list[i-1])

#Months is equal to the number of rows in date_list

Months = str(len(date_list))

#Total Profit/Loss is the sum of all the elements of the pl_list
Total = sum(pl_list)

# The Average Change is the average of the Change list. Average = Sum/Num of items
avg_change = sum(Change)/len(Change)

#The Greatest Increase in Profits is the maximum value in the Change list
max_inc_profit = max(Change)

# Position of the Greatest Increase in Profits in the Change list
max_pos = Change.index(max_inc_profit)

# The month of the Greatest Increase in Profits is max_pos + 1 in the date_list
date_max_inc_profit = date_list[max_pos+1]

#The Greatest Decrease in Profits is the minimum value in the Change list
max_dec_profit = min(Change)

# Position of the Greatest Decrease in Profits in the Change list
min_pos = Change.index(max_dec_profit)

# The month of the Greatest Decrease in Profits is min_pos + 1 in the date_list
date_max_dec_profit = date_list[min_pos+1]


## In screen summary

print ("Financial Analysis\n")
print ("----------------------------\n")
print (f"Total Months: {Months}\n")
print (f"Total: ${Total}\n")
print (f"Average Change: ${avg_change:.2f}\n")
print (f"Greatest Increase in Profits: {date_max_inc_profit} (${max_inc_profit})\n")
print (f"Greatest Decrease in Profits: {date_max_dec_profit} (${max_dec_profit})\n")


#### In File summary Writing

#Output path information \analysis\results.txt
output_path=os.path.join('analysis','results.txt')

file = open(output_path,"w")


file.write ("Financial Analysis\n")
file.write  ("----------------------------\n")
file.write  (f"Total Months: {Months}\n")
file.write (f"Total: ${Total}\n")
file.write (f"Average Change: ${avg_change:.2f}\n")
file.write (f"Greatest Increase in Profits: {date_max_inc_profit} (${max_inc_profit})\n")
file.write (f"Greatest Decrease in Profits: {date_max_dec_profit} (${max_dec_profit})\n")

file.close()
