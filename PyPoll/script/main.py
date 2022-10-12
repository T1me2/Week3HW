import os
# from os import path

# Module for reading CSV files
import csv
from telnetlib import theNULL
from pyparsing import col

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

#Lists of candidates to store data
#C_C_S = []
#D_D = []
#R_A_D = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    
    TotalC_C_S = 0
    TotalD_D = 0 
    TotalR_A_D = 0 
    Tvotes = 0
    test = 0

    for row in csvreader:
        if row[2] == "Charles Casper Stockham":
            TotalC_C_S += 1
            test += 1
        elif row[2] == "Diana DeGette":
            TotalD_D += 1
        elif row[2] == "Raymon Anthony Doane":
            TotalR_A_D += 1
        Tvotes = TotalC_C_S + TotalD_D + TotalR_A_D
        winner = max(TotalC_C_S, TotalD_D, TotalR_A_D)
        if winner == TotalC_C_S:
            winner = "Charles Casper Stockham"
        elif winner == TotalD_D:
            winner = "Diana DeGette"
        elif winner == TotalR_A_D:
            winner = "Raymon Anthony Doane"

    print("Election Results")
    print("---------------------------")
    print("Total Votes:", Tvotes)
    print("---------------------------")
    print("Charles Casper Stockham:", TotalC_C_S)
    print("Diana DeGette:", TotalD_D)
    print("Raymon Anthony Doane:", TotalR_A_D)
    print("---------------------------")
    print("Winner:", winner)
    print("---------------------------")

    