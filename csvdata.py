import csv
import pandas
import myexception
import sys


#This function will read a Column named high in csv file
#and returns maximum price
def high_price(filename):
    try:
        csvfile = pandas.read_csv(filename)
    except FileNotFoundError:
        print "Wrong path or not file found"
        sys.exit(0)
  
    try:
        high=max(csvfile['High'])
    except CustomError,arg:
        raise CustomError("column not found")
        print 'Error:',arg.msg
        sys.exit(0)
        
    return high

#This function will read a Column named low in csv file
#and returns minimum price
def low_price(filename):
    try:
        csvfile = pandas.read_csv(filename)
    except FileNotFoundError:
        print "Wrong path or not file found"
        sys.exit(0)

    try:
        low=min(csvfile['Low'])
    except CustomError,arg:
        raise CustomError("column not found")
        print 'Error:',arg.msg
        sys.exit(0)
                
    return low

#This function will will take high and low values
#and will return their repesctive dates

def date_of_value(value):
    with open('test.csv') as f:
        next(f)
        reader=csv.reader(f)
        for row in reader:
            if value == float(row[2]) or value == float(row[3]):
                date_of_value=row[0]

    
    return date_of_value
 

