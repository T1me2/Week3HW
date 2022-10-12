import os
# from os import path

# Module for reading CSV files
import csv
from telnetlib import theNULL
from pyparsing import col

csvpath = os.path.join('..', 'Resources', 'election_data.csv')


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #set ballot counters
    TotalC_C_S = 0
    TotalD_D = 0 
    TotalR_A_D = 0 
    #initialize total vote variable
    Tvotes = 0
    


    for row in csvreader:
        #if vote cast for ccs count their vote
        if row[2] == "Charles Casper Stockham":
            TotalC_C_S += 1
        #if vote cast for dg count their vote
        elif row[2] == "Diana DeGette":
            TotalD_D += 1
        #if vote cast for rad count their vote
        elif row[2] == "Raymon Anthony Doane":
            TotalR_A_D += 1
        #total all votes   
        Tvotes = TotalC_C_S + TotalD_D + TotalR_A_D

        #find the winner
        winner = max(TotalC_C_S, TotalD_D, TotalR_A_D)
        if winner == TotalC_C_S:
            winner = "Charles Casper Stockham"
        elif winner == TotalD_D:
            winner = "Diana DeGette"
        elif winner == TotalR_A_D:
            winner = "Raymon Anthony Doane"

    CCS_pct = (TotalC_C_S/Tvotes)
    DD_pct = (TotalD_D/Tvotes)
    RAD_pct = (TotalR_A_D/Tvotes)

   #print results
    print("Election Results")
    print("---------------------------")
    print("Total Votes:", Tvotes)
    print("---------------------------")
    print("Charles Casper Stockham:", f"{CCS_pct:.3%}", "(", TotalC_C_S, ")")
    print("Diana DeGette:", f"{DD_pct:.3%}","(", TotalD_D,")")
    print("Raymon Anthony Doane:", f"{RAD_pct:.3%}", "(", TotalR_A_D, ")")
    print("---------------------------")
    print("Winner:", winner)
    print("---------------------------")

    #Write results to txt file
    output_path = os.path.join("output", "El_Results.txt")

    #with open("El_Results.txt") as file:
     #   for line in file

      #  txtwriter = text

  #  f = 'El_Results.txt'
   # with open(file, 'w') as text:
   #     text.write("slkdjfa")

    f = open("El_Results.txt", "w+",)
    f.write("Election Results\n")
    f.write("---------------------------\n")
    f.write("Total Votes:" + f"{Tvotes}\n")
    f.write("---------------------------")
    f.write("Charles Casper Stockham:"+ f"{CCS_pct:.3%}"+ "("+ f"{TotalC_C_S}" + ")\n")
    f.write("Diana DeGette:"+ f"{DD_pct:.3%}"+"("+ f"{TotalD_D}" +")\n")
    f.write("Raymon Anthony Doane:"+ f"{RAD_pct:.3%}"+ "("+ f"{TotalR_A_D}" + ")\n")
    f.write("---------------------------\n")
    f.write("Winner:"+ f"{winner}\n")
    f.write("---------------------------\n")
    f.close()