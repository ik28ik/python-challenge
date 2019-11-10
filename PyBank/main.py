

import os
import csv
total_net_list = []
total_change = []
change =[]
i=0 

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
output_file = os.path.join("..", "Analysis","pybank.txt")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        total_net_list.append(int(row[1]))
        months_count = len(total_net_list)
        total_net=sum(total_net_list)
        total_change.append(row[1])
    for i in range(len(total_change)-1): 
            
        change.append(int(total_change[i]) - int(total_change[i+1]))
        average_change=sum(change) /len(change)
        average_change=round(average_change,2)
      
        
        greatest_increase=int(max(change))
        greatest_decrease=int(min(change))
    
    with open(output_file, "w", newline='') as textfile:

        print("Financial Analysis", file=textfile)
        print("-----------------------------------------------", file=textfile)
        print("Total Months:  " + str(months_count),file=textfile)
        print(f'Total:, (${total_net}',file=textfile)
        print(f'Average  Change: {average_change}', file=textfile)
        print(f'Greatest Increase in Profits: {greatest_increase}',file=textfile)  
        print(f'Greatest Decrease in Profits: {greatest_decrease}',file=textfile)
        print("-----------------------------------------------", file=textfile)

with open(output_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row)
        
