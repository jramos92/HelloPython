'''
Created on 31 ene. 2020

@author: jramosm
'''
import xlrd

workbook = xlrd.open_workbook("C:\\Users\\jramosm\\Downloads\\timelog.xlsx")
workbook = xlrd.open_workbook("C:\\Users\\jramosm\\Downloads\\timelog.xlsx", on_demand = True)
worksheet = workbook.sheet_by_index(0)
first_row = [] # The row where we stock the name of the column
for col in range(worksheet.ncols):
    first_row.append( worksheet.cell_value(0,col) )
    
# tronsform the workbook to a list of dictionnary
data =[]
for row in range(1, worksheet.nrows):
    elm = {}
    for col in range(worksheet.ncols):
        elm[first_row[col]]=worksheet.cell_value(row,col)
    data.append(elm)
    
# print(data)

data.count("Desarrollo")

