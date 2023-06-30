import os
import csv

# join path
poll_data = os.path.join(".." , "Resources" , "election_data.csv")

result_file = os.path.join ("Analysis", "PyPoll_Analysis.txt")

#open and read csv
with open(poll_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # skip header row
    print(f"Header: {csv_header}")

    vote_count = []
    Candidate_names = {}

    Winner_votes = 0 
# reading through each row of data in the csv
    for row in csvreader:
        vote_count.append(row[0])
        candidate = row[2]
        if candidate in Candidate_names: 
            Candidate_names[candidate] += 1
        else:
            Candidate_names[candidate] = 1 
        
   # printing results to terminal
    print("-----------------------")
    print("Election Results:")
    print("-----------------------")
    print(f" Total Votes:  {len(vote_count)}")
    print("-----------------------")
    Output_total = (
    f"Election Results\n"
    f"--------------------------\n"
    f"Total Votes: {len(vote_count)}\n"
    f"--------------------------\n"
    )

    # output to text file 
    with open(result_file, "w") as txt_file:  
        txt_file.write(Output_total)
        txt_file.write("Vote Summary \n")
        txt_file.write("----------------------------\n")

#calculating individual vote count and percentages per candidate

    for name in Candidate_names: 
        
        percent = ((Candidate_names[name])/(len(vote_count))) * 100
        
        candidate_output_txt = f"{name} : {round(percent, 2)}% ({Candidate_names[name]})\n"        
        candidate_output = f"{name} : {round(percent, 2)}% ({Candidate_names[name]})"

        print (candidate_output)
        
                
        # output to text file
        with open(result_file, "a") as txt_file:
            txt_file.write(candidate_output_txt)
            
# calculating winning candidate's name 
    for name in Candidate_names:    

        if Candidate_names[name] > Winner_votes: 
            Winner_votes = Candidate_names[name]
            Winner_name = name
# creating variable to store output & printing output to terminal    
winner_output = ( 
            f" Winner: {Winner_name}\n" 
            f"-----------------------\n"
            )
print("-----------------------")        
print(winner_output)

# output to text file        
with open(result_file, "a") as txt_file:
    txt_file.write("-----------------------\n")
    txt_file.write(winner_output)


        









    
    
    