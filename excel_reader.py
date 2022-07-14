# # Reading an excel file using Python
# import xlrd
 
# # Give the location of the file
# loc = "marks_sheet.xlsx"
 
# # To open Workbook
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)
 
# # For row 0 and column 0
# print(sheet.cell_value(0, 0))


import pandas as pd    
    
# Read the file    
data = pd.read_csv("marks_sheet.csv", low_memory=False)

    
# Output the number of rows    
print("Total rows: {0}".format(len(data)))    
    
# See which headers are available    
print(data.head(2))
print(data.dtypes)

data1 = data['Name']
greater_than_500 = data[data['Marks'] > 500 ]
print('Names - ', data1)

for i in data1 :
    print('some data --- ', i)


print("data2", '\n' ,data2)


names = list(data['Name'])
marks = list(data['Marks'])

print('Printing Names...', names)
print('printing marks---', marks)

# for i in names: 
#     print(i)

