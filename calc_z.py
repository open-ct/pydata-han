import pandas as pd
import getscore as gs

data = pd.read_excel(r'z_out_0713_修改后.xlsx')
# manu = pd.read_csv(r'z_manu.csv')
code_dict = {}

p1_CODElist = []
mm60101_CODElist = []
mm60102_CODElist = []
mm60104_CODElist = []
mm60105_CODElist = []
mm60107_CODElist = []
mm60108_CODElist = []

shui_list = []
'''
for index, row in manu.iterrows():
    key = str(row['id'])
    value = str(row['MM60104'])
    code_dict[key] = value
    
'''
for index, row in data.iterrows():
    # id = row['ticket_id']
    # mm60104_CODE = code_dict[str(id)]
    # mm60104_CODElist.append(mm60104_CODE)
    p1 = row['P1']
    p1_CODE = gs.compareP3(p1)
    p1_CODElist.append(p1_CODE)

    mm60101 = row['MM60101']
    mm60101_CODE = gs.get60101(mm60101)
    mm60101_CODElist.append(mm60101_CODE)

    mm60102 = row['MM60102']
    mm60102_CODE = gs.get60102(mm60102)
    mm60102_CODElist.append(mm60102_CODE)

    mm60104 = row['MM60104_new']
    mm60104_CODE = row['MM60104_CODE']
    shui = gs.cal104(mm60104, gs.get104(mm60104), 2, 18, 500, 3, 3, 25, 1, 1, 7, 4)
    shui_list.append(shui)
    mm60105 = row['MM60105']
    mm60105_CODE = gs.compareZ(mm60104_CODE, shui, mm60105)
    mm60105_CODElist.append(mm60105_CODE)

    mm601071, mm601072 = row['MM601071'], row['MM601072']
    mm60107_CODE = gs.get60107(mm601071, mm601072, mm60105_CODE)
    mm60107_CODElist.append(mm60107_CODE)

    mm60108 = [row['MM601081'], row['MM601082'], row['MM601083'], row['MM601084']]
    mm60108_CODE = gs.get60108(mm60108, mm60102_CODE)
    mm60108_CODElist.append(mm60108_CODE)

    

col_name = data.columns.tolist()

col_name.insert(col_name.index('P1')+1, 'P1_CODE')
data = data.reindex(columns=col_name)
data['P1_CODE'] = p1_CODElist

col_name.insert(col_name.index('MM60101')+1, 'MM60101_CODE')
data = data.reindex(columns=col_name)
data['MM60101_CODE'] = mm60101_CODElist

col_name.insert(col_name.index('MM60102')+1, 'MM60102_CODE')
data = data.reindex(columns=col_name)
data['MM60102_CODE'] = mm60102_CODElist

'''
col_name.insert(col_name.index('MM60104')+1, 'MM60104_CODE')
data = data.reindex(columns=col_name)
data['MM60104_CODE'] = mm60104_CODElist
'''
col_name.insert(col_name.index('MM60105')+1, 'shui')
data = data.reindex(columns=col_name)
data['shui'] = shui_list

col_name.insert(col_name.index('MM60105')+2, 'MM60105_CODE')
data = data.reindex(columns=col_name)
data['MM60105_CODE'] = mm60105_CODElist

col_name.insert(col_name.index('MM601072')+1, 'MM60107_CODE')
data = data.reindex(columns=col_name)
data['MM60107_CODE'] = mm60107_CODElist

col_name.insert(col_name.index('MM601084')+1, 'MM60108_CODE')
data = data.reindex(columns=col_name)
data['MM60108_CODE'] = mm60108_CODElist


data.to_excel('z_out_0714.xlsx')