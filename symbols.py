import xlrd
import myexception
import sys

#This fundction will take the 'Company name' from the user
#and searches in the excel file called'book.xslx' for the symbol of the company
#and returns the same.

def symbol_name():
    query =raw_input(" Enter the company name: ").title()   #converts the input to camelcase
    excelfile=xlrd.open_workbook("symbols.xlsx")
    sheet=excelfile.sheet_by_index(0)
    for row_index in range(sheet.nrows):
        for col_index in range(sheet.ncols):
            try:
                if query in sheet.cell(row_index,col_index).value:
                    symbol=sheet.row_values(row_index)[1]    
            except CustomError,arg:
                raise CustomError("Query not found")
                print 'Error:',arg.msg
                sys.exit(0)
                
    return symbol
