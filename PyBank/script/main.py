import os
# from os import path

# Module for reading CSV files
import csv
from telnetlib import theNULL

from pyparsing import col

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


    line = 0
    TotalPL = 0
    TotalM = 0
    Totalchange = 0
    Averagechange = 0
    prow = 1088983
    priorPL = 0
    priorlinechange = 1443517
    priorLchange=1443517
    challenger = 0
    Lchallenger = 0

    for row in csvreader:
        #reset linechange to zero
        linechange = 0
        #profit & loss
        PL = int(row[1])
        #change between prior P&L and current P&L
        linechange = PL - prow
        #find best month
        if priorlinechange < linechange:
            challenger = linechange 
            bestmonth = row[0]    
        #find worst month
        if priorLchange > linechange:
            Lchallenger = linechange 
            worstmonth = row[0]    
        #for worst month comparison
        priorLchange = Lchallenger
        #for best month comparison 
        priorlinechange = challenger
        #prior row value below linechange so prior value used in calculation
        prow = int(row[1])
        #add line changes for total months
        Totalchange += linechange
        #find average change
        if TotalM == 85:
            Averagechange = round(Totalchange/TotalM, 2)
        TotalPL += PL
        TotalM += 1
        
    print("Financial Analysis")
    print("---------------------------------")
    print("Total months: ", TotalM)
    print("Total: $",TotalPL)
    #print("prow", prow)
    #print("linechange", linechange) 
    #print("Totalchange", Totalchange)
    print("Averagechange", Averagechange)
    print("Greatest Increase in Profits: ", bestmonth ,"$", "(",challenger,")")
    print("Greatest Decrease in Profits: ", worstmonth ,"$", "(",Lchallenger,")")

