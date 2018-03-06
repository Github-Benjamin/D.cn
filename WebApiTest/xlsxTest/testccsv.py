# coding: utf-8
import csv

#    打开方式还可以使用file对象

csvfile = open('orderx-export.csv', 'wb')
writer = csv.writer(csvfile)

writer.writerow(['姓名', '年龄', '电话'])

data = [
    ('小河', '25', '1234567'),
    ('小芳', '18', '789456')
]

writer.writerows(data)

csvfile.close()