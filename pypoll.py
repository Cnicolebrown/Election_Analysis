import csv
import os

#assign a variable to load a file from a path
file_to_load = os.path.join("resources", "election_results.csv")

with open(file_to_load) as election_data:
    print(election_data)

#create a filename variable to a direct or indirect path to the file
#assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)


    #read and print the header row
    headers = next(file_reader)
    print(headers)


