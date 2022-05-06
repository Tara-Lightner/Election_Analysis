import csv
import os

#Assessing the file to open it, read it, analyse it and close it
# 1.) Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'
# 2.) Open the election results and read the file.
# election_data = open(file_to_load, 'r')
# 3.) To do: perform analysis.
#print(election_data)
# 4.) Close the file.
# election_data.close()

# or open and close with the with statment added
# Open the election results and read the file
# 1.) Open with the with statement in which python closes it
with open(file_to_load) as election_data:
# 2.) To do: perform analysis.
     print(election_data)


# The data we need to retrieve.
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Percentage of votes each candidate won
# 4. Total number of votes each candidate received
# 5. The winner of the election based on popular vote

# To Use the datetime module
# 1.) import datetime
import datetime as dt
# 2.) Declare the now variable to hold time right now
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)