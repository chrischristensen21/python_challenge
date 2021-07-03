# Your task is to create a Python script that analyzes the records to calculate each of the following:
    #The total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    #The average of the changes in "Profit/Losses" over the entire period
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in losses (date and amount) over the entire period

import os

import csv

csvpath = os.path.join('Resources', 'budget_data.csv')


with open(csvpath) as csvfile:

  
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

  
  