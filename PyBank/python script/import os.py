import os
import csv


budget_data = os.path.join('..','resources','budget_data.csv')


# Read in the CSV file
with open(budget_data, 'r') as csvfile:

    # Split the data on commas
    csv_reader = csv.reader(csvfile, delimiter=',')

    #header = next(csvreader)

    CSV_header = next(csv_reader)
    #print(CSV_header)
    column2=[]
    date=[]
    total=[]
    change=[]

    for row in csv_reader:
        #print (row)
        profit=(row[1])

        column2.append(float(profit))
        date.append((row[0]))
    
    for profit in column2:

        

    

    #total=
    #average_change=
    #greatest_increase_in_profits=
    #greatest_decrease_in_profits=

    print(f'Total Months: {len(date)}')  
    print(f'Total:', sum(column2))
    print(f'Average Change:', sum(column2)/len(column2))
    print(f"Greatest Increase in Profits:", max(column2))
    print(f'Greatest Decrease In Profits:', min(column2))



#output_path = os.path.join("..", "analysis", "Analysis.txt")
# with open(output_path, 'w', newline='') as txtfile
    
#     print(f'Total Months: {len(date)}', file=output_path)  
#     print(f'Total:', sum(column2), file=output_path)
#     print(f'Average Change:', sum(column2)/len(column2), file=output_path)
#     print(f"Greatest Increase in Profits:", max(column2), file=output_path)
#     print(f'Greatest Decrease In Profits:', min(column2), file=output_path)
#output_path = os.path.join("..", "analysis", "outputtext.txt")
f =  open("output.txt", "w")
print(f'Total Months: {len(date)}', file= f)  
print(f'Total:', sum(column2), file= f)
print(f'Average Change:', sum(column2)/len(column2), file= f)
print(f"Greatest Increase in Profits:", max(column2), file= f)
print(f'Greatest Decrease In Profits:', min(column2), file= f)

f.close()
