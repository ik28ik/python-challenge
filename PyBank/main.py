

import os
import csv
total_net_list = []
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
        
    for i in range(len(total_net_list)-1):
            change.append(int(total_net_list[i+1]) - int(total_net_list[i]))
            average_change=sum(change) /len(change)
            average_change=round(average_change,2)
      
        
            greatest_increase=int(max(change))
            greatest_decrease=int(min(change))

    
    

    print("Financial Analysis")
    print("-----------------------------------------------")
    print("Total Months:  " + str(months_count))
    print(f'Total:, ${total_net}')

        
    print(f'Average  Change: ${average_change}')
    print(f'Greatest Increase in Profits: ${greatest_increase}') 
    print(f'Greatest Decrease in Profits: ${greatest_decrease}')
    print("-----------------------------------------------")
    
    
with open(output_file,"w", newline='') as textfile:
    writer=csv.writer(textfile)

    print("Financial Analysis", file=textfile)
    print("-----------------------------------------------", file=textfile)
    print("Total Months:  " + str(months_count), file=textfile)
    print(f'Total:, ${total_net}', file=textfile)

        
    print(f'Average  Change: ${average_change}', file=textfile)
    print(f'Greatest Increase in Profits: ${greatest_increase}', file=textfile)
    print(f'Greatest Decrease in Profits: ${greatest_decrease}', file=textfile)
    print("-----------------------------------------------", file=textfile)
    
       