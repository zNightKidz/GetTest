import xlrd

book = xlrd.open_workbook("F:/任务执行/首钢设备表/首钢设备资源表.xlsx")

sheet = book.sheet_by_name('Hostname')

print("行数：",sheet.nrows)

print("列数：",sheet.ncols)

for i in range(sheet.nrows):
	print(sheet.row_values(i))
