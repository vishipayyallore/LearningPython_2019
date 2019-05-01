import openpyxl as excel

filepath = '../Data/students.xlsx'

workbook = excel.load_workbook(filepath)
currentsheet = workbook['Mar2019']



for row in range( 2, currentsheet.max_row+1):
    sum = 0

    for col in range(3, currentsheet.max_column):
        sum += int(currentsheet.cell(row, col).value)
    
    total = currentsheet.cell(row, currentsheet.max_column)
    total.value = sum

workbook.save(filepath)

    