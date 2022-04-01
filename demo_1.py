from datetime import date, datetime, time
import numpy as np
import pandas as pd
from pandas.core.construction import array


def dealExcelData(start):
    startY = 2010 + start
    endY = 2011 + start
    # 根据年份筛选
    filetr_df = df[(df['年份'] <= endY) & (startY <= df['年份'])]
    out_arr = []
    # 遍历表格内容，根据专利人的值进行分割重组
    for index, row in filetr_df.iterrows():
        names = row['专利人'].split('；')
        for name in names:
            if len(name) > 3:
                row['专利人'] = name
                out_arr.append(list(row.values))

    # 将处理过的数据写入到新的表中
    # new_excel = pd.DataFrame(np.array(out_arr), columns=df.columns.values)
    # new_excel.to_excel("C:/Users/LIU.JIANG/Desktop/test.xlsx")
    # 计算出每个公司所具有的发明数
    dict = {}
    for i in range(len(out_arr)):
        tmp = out_arr[i][10]
        if tmp in dict:
            dict[tmp]["public"].append(out_arr[i][7])
        else:
            dict[tmp] = {
                "provice": out_arr[i][4],
                "public": [out_arr[i][7]]
            }

    lst = list(dict.items())
    tag = 1
    length = len(lst)
    if length < 256:
        dealMxtData(lst, 0, length, startY, endY, tag)
    else:
        tmp_start = 0
        tmp_end = 0
        tmp_policy = 1
        for i in range(length):
            if lst[i][1]["provice"] != tmp_policy:
                tmp_end = i
                tmp_policy = lst[i][1]["provice"]
            if ((i - tmp_start) > 254):
                if tmp_start == tmp_end:
                    dealMxtData(lst, tmp_start, i, startY, endY, tag)
                    tmp_start = i
                    tmp_end = i
                else:
                    dealMxtData(lst, tmp_start, tmp_end, startY, endY, tag)
                    tmp_start = tmp_end
                tag += 1
            if i == length - 1:
                dealMxtData(lst, tmp_start, length, startY, endY, tag)


def dealMxtData(dict, start, end, startY, endY, tag):
    # 生成矩阵(计算公司之间的公开号交集)
    length = end - start
    mtx = np.zeros((length, length))
    m = 0
    cols = []
    for i in range(start, end):
        n = 0
        for j in range(start, end):
            if i != j:
                mtx[m][n] = len(set(dict[i][1]["public"]).intersection(set(dict[j][1]["public"])))
            n = n + 1
        m = m + 1
        cols.append(dict[i][0])

    new_excel = pd.DataFrame(np.array(mtx), index=cols, columns=cols)
    new_excel.to_excel("C:/Users/LIU.JIANG/Desktop/data/" +
                        str(startY) + "-" + str(endY) + "_" + str(tag) + ".xlsx")


bt = datetime.now()
print('-----开始运行时间：', bt, '---------')

# 读取表格
df = pd.read_excel("C:/Users/LIU.JIANG/Desktop/4.xlsx", sheet_name=1)


# dealExcelData(9)
for m in range(11):
    dealExcelData(m)

et = datetime.now()
print('-----结束运行时间：', et, '---------')
run_time = (et - bt).seconds
print('-----耗时：', run_time, 's---------')
