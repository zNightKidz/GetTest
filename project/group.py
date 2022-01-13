#!/usr/bin/python
# -*- coding: UTF-8 -*-
import csv
import os

if not os.path.exists(r'分组'):
    os.mkdir('分组')
with open(r'人名单.csv', encoding="utf-8") as file:
    csv_read = csv.reader(file,delimiter='\t')

    # for number in range(0,10):
    #     print('文件名称循环',number)
    #     filepath = '分组/尾号'+str(number)+'.csv'
    #     if not os.path.isfile(filepath):
    #         with open(filepath,'w', encoding="utf-8") as f:
    #             f.write('姓名，电话')
    #             f.write('\n')

        # with open (filepath,'a',encoding="utf-8") as writefile:
        #     for item in csv_read:
        #         if item[0][-1:] == str(number) and item[0][-1:]>="1":
        #             print(item)
        #             csv.writer(writefile,delimiter='\t').writerow(item)
    csvfilespath = r'分组'
    for dirpath,dirname,filenames in os.walk(csvfilespath):
        for file in filenames:
            print(file)
            mycsvfile = csvfilespath+'/'+file
            print('mycsvfile:',mycsvfile)
            with open(mycsvfile,'a',encoding='utf-8') as writefile:
                print('打开csv文件')
                for item in csv_read:
                    print(item)
                    if (os.path.splitext(mycsvfile))[0][-1:] == (item[0][-1:]):
                        print(item,mycsvfile)
                        csv.writer(writefile,delimiter='\t').writerow(item)