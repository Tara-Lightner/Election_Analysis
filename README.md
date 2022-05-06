# Election Analysis

## Overview of Election Audit Project
This project demonstrates mastery of Python through: 
- Creating scripts using VSCode and using the command line that read, writes, and stores data from files or in arrays.
- Perform mathematical operations, utilizing knowledge of variables, arrays, conditionals, Boolean, and loops.
- Understand and appropriately declare variables using the correct Python data types including integers, floating-point decimal numbers, and strings.
- Use decision statements, logical operations for complex comparisons, and repetition statements to run code more than once.
- Write data to screen outputs.


## Background/ Application for Use
This project represents a simulation in which, a client and the Board of Elections employee, needed assistance in an election audit tabulating an election of a Congressional district.  They were previously using excel and wanted to automate the process.  The assignment was accepted to help automate the reporting process and create a certified vote count report using Python. The big goal is to use this pilot code and test it, before explaining it to other congressional districts, senatorial districts, and local elections.  The client originally requested the report to include the following:

- The total number of votes cast
- The total number of votes for each candidate
- The percentage of votes for each candidate
- The Winner of the election

 The client submitted the certified vote count report to the election commission. Before rolling out the code to other districts they requested a few additional specifications including:
- The voter turnout per county
- The percentage of votes per county listed with the total count
- The county with the highest turnout

## Deliverables
- Election Results Printed from Command Line (Git Bash)
![Election Results through command line: this file can be found in Election_Analysis/analysis/Deliverable_1_Election_Results_Command Line.PNG](https://github.com/Tara-Lightner/Election_Analysis/blob/main/analysis/Deliverable_1_Election_Results_Command%20Line.PNG)
- Election Results Saved to a Text File (election_analysis.txt)
![Election Results saved as a text file: this file can be found in Election_Analysis/analysis/Deliverable_2_Election_Results_Text_File.PNG](https://github.com/Tara-Lightner/Election_Analysis/blob/main/analysis/Deliverable_2_Election_Results_Text_File.PNG)
- This Written Analysis of the Election Audit

## Conclusion
### Results: Election Outcome Analysis
How many votes were cast in this congressional election?
- 369,711 district votes were cast for this congressional election.
What was the breakdown of the number of votes and the percentage of total votes for each county in the precinct; which county had the largest number of votes?
- **County Makeup: Vote Count & Percentage of Total**
  - *<u>**Denver**, with the largest county turnout, </u> cast a county total of 306,055 making up 82.8% of the total district votes.
   - **Jefferson** cast a county total of 38,885 votes making up 10.5% of the total votes cast 
   - **Arapahoe** cast a county total of 24,801 votes making up 6.7% of the total district votes.
Provide a breakdown of the number of votes and the percentage of the total votes each candidate received; Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
- **Candidate Summary: Percentage and Count**
  - <u>**Diana DeGette**, election winner</u>, receiving 73.8% of total votes, consisting of 272,892 votes
  - **Charles Casper Stockham** received 23.0% of total votes, made up of 85,213 votes
  - **Raymon Anthony Doane** received 3.1% of total votes, made up of 11,606 votes

### A statement to the election commission
As is the script created for you has been a successful demonstration of report creation and can be used to expand to other congressional districts, senatorial districts, and local elections with minimal work on your teams’ end.  As we have discussed your team is familiar with excel and uses CSV files regularly as the mechanism to capture total votes from all sources.  Using this file as an input you will be able to successfully and quickly automate the certified report creation process.  On my computer, I was able to do so in roughly two minutes.  

What will you need to create future reports? 

As you will be able to continue to use this script for your district in future years, as candidates change, and other districts adopt this process minimal training will be needed. The few steps one needs to prep the CSV file to run the script on include:
 - Storing the file, you will be executing in the correctly named and properly organized folder.
 - Moving the old file out of the folder, storing it elsewhere.
 - Replacing the file desired to be turned into a report and using the correct file name.
 - Make sure to include the following columns, with correct titles, in the correct order
   - Column A: Ballot ID
   - Column B: County
   - Column C: Candidate
To demonstrate that you are currently capable of utilizing this for any combination of counties and candidates for any election allow me to provide you with a few examples.
### A Couple Examples:

##### Example 1:  As we know candidates are likely to change.  Here is an example of your district with new candidates.

![New_Candidates.PNG](Resources%5CEx_New_Candidates.PNG)
![alt](https://github.com/Tara-Lightner/Election_Analysis/blob/main/analysis/election_analysis_Example_New_Candidates.txt)

##### Example 2: As more districts will want to take advantage of this report automation, here is an example of putting in new counties for another district.
![New_District.PNG](Resources%5CEx_New_District.PNG)

### Challenges and Difficulties Encountered
There were many challenges and lessons learned along the way.  One of my biggest frustrations was trying to run my code inside VSCode using the play button vs. trying to launch it from the command line.  I had to change my file path code back and forth to get it to run using the play button because it was launching from a folder at a higher level and not from where my python script was located. I thought I had to make it work for both deliverables to get the assignment done correctly.  I even tried using a direct path, but this did not resolve it.  I think the error was that I had my VSCode opened from my MSU folder which is the overarching folder I have all my boot camp work in.  
####
#### Another issue that I had was in deciding to use the provided code from the challenge_starter_code or to get the output to format both the Print Statement and the election analysis txt the same way.  Below is the image of the formatting for the results requirements:
![Required Print Statement Output Solution](https://github.com/Tara-Lightner/Election_Analysis/blob/main/analysis/Module3_Requirement_Challenge_election_results_Print_Statement.png)
vs. The Required Output for the Election Analysis Text File: 
![Required Text File Output with different formating](https://github.com/Tara-Lightner/Election_Analysis/blob/main/analysis/Module3_Requirement_Challenge_election_results_txt_Results.png)
####
#### In general, the lack of continuity was bothersome in the reporting.  Why would there be a title for County Votes, but not for Candidate Results? Additionally, why would one section be single-lined and the other double-lined.   The largest count is titled about the county section, yet the winner is below the candidate section.  It is redundant to print the same specs for the winning candidate twice.  The space could have been used better.



