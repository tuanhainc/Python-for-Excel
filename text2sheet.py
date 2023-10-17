import openpyxl

backup = input('Press Enter to use sample text file  ')
while len(backup)>1:
    try:
        file = input('File name: ')
        fhand = open(file,'r')
        break
    except:
        print('No text file found')
        backup = input('Press Enter to use sample text file  ')

fhand = open('spam.txt','r')
wb = openpyxl.Workbook()
sheet = wb.active

lines = list()
row = 0
for line in fhand:
    row += 1
    lines.append(line)
    sheet.cell(row=row,column=1).value = lines[row-1]
    print(lines[row-1])
    print(row)


fhand.close()
wb.save('text2sheet.xlsx')


# python text2sheet.py
