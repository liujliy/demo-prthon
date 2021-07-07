from datetime import date, datetime, time
import numpy as np
import pandas as pd
from pandas.core.construction import array


def filterValue(name, year) :
    lDate = datetime(year - 3, 1, 1)
    rDate = datetime(year, 1, 1)
    cmp_df = df[(df['申请（专利权）人'] == name) & (df['公开（公告）日'] < rDate) & (lDate <= df['公开（公告）日'])]

    fl = cmp_df['分类号'].values
    count = set()
    for i in fl:
        arr = i.split(';')
        for j in arr:
            count.add(j[0:4])
    return len(count)

bt = datetime.now()
print('-----开始运行时间：', bt, '---------')

df = pd.read_excel("C:/Users/LIU.JIANG/Desktop/1.xlsx")

df['公开（公告）日'] = pd.to_datetime(df['公开（公告）日'])
companys = df.drop_duplicates(['申请（专利权）人'])['申请（专利权）人'].values

arr = []
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
for c in companys:
    for y in years:
            tmp = [c, y, filterValue(c, y)]
            arr.append(tmp)

new_excel = pd.DataFrame(np.array(arr), columns=['申请（专利权）人', '年份', '非重复IPC专利数'])
new_excel.to_excel("C:/Users/LIU.JIANG/Desktop/test.xlsx")

et = datetime.now()
print('-----结束运行时间：', et, '---------')
run_time = (et - bt).seconds
print('-----耗时：', run_time, '---------')