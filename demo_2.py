from datetime import date, datetime, time
from operator import inv
import numpy as np
import pandas as pd
from pandas.core.construction import array

years = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

bt = datetime.now()
print('------开始运行时间：', bt, '------')

# 读取表格
df = pd.read_excel("C:/Users/LIU.JIANG/Desktop/1.xlsx", sheet_name=1)

companys = pd.unique(df['公司名称'].values).tolist()

# company = companys[0]
# year = 2019
# explore_invs = 0
# use_invs = 0
# s_year = year - 3
# e_year = year - 1
# invs = df[(df['公司名称'] == company) & (df['年份'] == year)]['主分类号'].apply(lambda x: x[0:4])
# q_invs = df[(df['公司名称'] == company) & (df['年份'] <= e_year) & (s_year <= df['年份'])]['主分类号'].dropna().apply(lambda x: x[0:4])
# set_invs = pd.unique(q_invs.values).tolist()
# for inv in invs:
#     if inv in set_invs:
#         use_invs += 1
#     else:
#         explore_invs += 1

# print('公司名称: ', company)
# print('年份: ', year)
# print('专利总数: ', len(invs))
# print('利用式创新: ', use_invs)
# print('探索式创新: ', explore_invs)
###############################################################
out_arrs = []
cols = ['公司名称', '年份', '专利总数', '利用式创新', '探索式创新']
for company in companys:
    for year in years:
        explore_invs = 0
        use_invs = 0
        s_year = year - 3
        e_year = year - 1
        invs = df[(df['公司名称'] == company) & (df['年份'] == year)]['主分类号'].dropna().apply(lambda x: x[0:4])
        q_invs = df[(df['公司名称'] == company) & (df['年份'] <= e_year) & (s_year <= df['年份'])]['主分类号'].dropna().apply(lambda x: x[0:4])
        set_invs = pd.unique(q_invs.values).tolist()
        for inv in invs:
            if inv in set_invs:
                use_invs += 1
            else:
                explore_invs += 1

        out_arrs.append([company, year, len(invs), use_invs, explore_invs])

new_excel = pd.DataFrame(np.array(out_arrs), columns = cols)
new_excel.to_excel("C:/Users/LIU.JIANG/Desktop/test_1.xlsx")

et = datetime.now()
print('------结束运行时间：', et, '------')
run_time = (et - bt).seconds
print('------耗时：', run_time, 's------')
