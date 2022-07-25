import pandas as pd


data1 = pd.read_excel(r'ticket_log_PBL_testing3.xlsx')
A1 = data1[data1['contest_id'].str.contains('高阶能力测试B|高阶能力测试C')]
Z1 = data1[data1['contest_id'].str.contains('数学建模')]
A1.to_excel('A1.xlsx')
Z1.to_excel('Z1.xlsx')

data2 = pd.read_excel(r'ticket_log_PBL_testing3.xlsx', sheet_name='Result 2')
A2 = data2[data2['contest_id'].str.contains('高阶能力测试B|高阶能力测试C')]
Z2 = data2[data2['contest_id'].str.contains('数学建模')]
A2.to_excel('A2.xlsx')
Z2.to_excel('Z2.xlsx')


data3 = pd.read_excel(r'ticket_log_PBL_testing3.xlsx', sheet_name='Result 3')
A3 = data3[data3['contest_id'].str.contains('高阶能力测试B|高阶能力测试C')]
Z3 = data3[data3['contest_id'].str.contains('数学建模')]
A3.to_excel('A3.xlsx')
Z3.to_excel('Z3.xlsx')

data4 = pd.read_excel(r'ticket_log_PBL_testing3.xlsx', sheet_name='Result 4')
A4 = data4[data4['contest_id'].str.contains('高阶能力测试B|高阶能力测试C')]
Z4 = data4[data4['contest_id'].str.contains('数学建模')]
A4.to_excel('A4.xlsx')
Z4.to_excel('Z4.xlsx')

A = pd.concat([A1, A2, A3, A4])
Z = pd.concat([Z1, Z2, Z3, Z4])

A.to_excel('A.xlsx')
Z.to_excel('Z.xlsx')