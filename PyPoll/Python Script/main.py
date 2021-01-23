import os
import csv


election_data = os.path.join("..",'resources','election_data.csv')


# Read in the CSV file
with open(election_data, 'r') as csvfile:

    # Split the data on commas
    csv_reader = csv.reader(csvfile, delimiter=',')

    #header = next(csvreader)

    CSV_header = next(csv_reader)
    #print(CSV_header)

    VoterID=[]
    County=[]
    Candidate=[]
    

    for row in csv_reader:
        #print (row)

        VoterID.append((row[0]))
        County.append((row[1]))
        Candidate.append((row[2]))
        




    Khan = Candidate.count("Khan")
    Correy = Candidate.count("Correy")
    Li = Candidate.count("Li")
    Otooley = Candidate.count("O'Tooley")

    print("Election Results")
    print("------------------")
    print(f'Total Voters: {len(VoterID)}')
    print("------------------")
    print(f'Kahn %',((Khan/len(VoterID))*100))
    print(f'Corry %',((Correy/len(VoterID))*100))
    print(f'Li %',((Li/len(VoterID))*100))
    print(f'OTooley %',((Otooley/len(VoterID))*100))
    print("------------------")
    print(f'winner is ')
   
    
    #print(count)  
    # print(f'Total:', sum(column2))
    # print(f'Average Change:', sum(column2)/len(column2))
    # print(f"Greatest Increase in Profits:", max(column2))
    # print(f'Greatest Decrease In Profits:', min(column2))




# f =  open("output.txt", "w")
# print(f'Total Months: {len(date)}', file= f)  
# print(f'Total:', sum(column2), file= f)
# print(f'Average Change:', sum(column2)/len(column2), file= f)
# print(f"Greatest Increase in Profits:", max(column2), file= f)
# print(f'Greatest Decrease In Profits:', min(column2), file= f)

    print("Election Results", file=f)
    print("------------------", file=f)
    print(f'Total Voters: {len(VoterID)}', file=f)
    print("------------------", file=f)
    print(f'Kahn %',((Khan/len(VoterID))*100), file=f)
    print(f'Corry %',((Correy/len(VoterID))*100),file=f )
    print(f'Li %',((Li/len(VoterID))*100), file=f)
    print(f'OTooley %',((Otooley/len(VoterID))*100), file=f)
    print("------------------", file=f)
    print(f'winner is ', file=f)

# f.close()