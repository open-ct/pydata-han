import pandas as pd
import getscore as gs

data = pd.read_excel(r'out_0712.xlsx')

P3_codelist = []
mm60311_CODElist = []
mm60321_CODElist = []
mm60341_CODElist = []
xiaowang = []
xiaowangcompare = []
xiaoming = []
xiaozhang = []
xiaoli = []
xiaohua = []
mm60351_CODElist = []
P4_codelist = []
mm60411_CODElist = []
mm60421_CODElist = []
mm60441_CODElist = []
mm60442_CODElist = []
shouru = []
jiage = []
mm60461_CODElist = []

for index, row in data.iterrows():
    P3 = row['P3']
    P3_CODE = gs.compareP3(P3)
    P3_codelist.append(P3_CODE)
    mm60311 = row['MM60311'] # 依赖mm60331
    mm60331_CODE = row['MM60331_CODE']
    mm60311_CODE = gs.get60311(mm60311, mm60331_CODE)
    mm60311_CODElist.append(mm60311_CODE)

    mm60321 = row['MM60321'] 
    mm60321_CODE = gs.get60321(mm60321)
    mm60321_CODElist.append(mm60321_CODE)

    mm60331 = row['MM60331_new']
    mm60331_formula = gs.get331(mm60331)
    wang = gs.cal331(mm60331, mm60331_formula, 2, 2, 1, 9.1, 7.15, 1.61, 1, 2, 1.61, 9.1)
    xiaowang.append(wang)
    ming = gs.cal331(mm60331, mm60331_formula, 4, 1, 3, 9.8, 7.82, 1.54, 1, 4, 7.82, 9.8)
    xiaoming.append(ming)
    zhang = gs.cal331(mm60331, mm60331_formula, 3, 4, 5, 9.3, 6.54, 1.47, 3, 5, 9.3, 1.47)
    xiaozhang.append(zhang)
    li = gs.cal331(mm60331, mm60331_formula, 5, 5, 4, 10.1, 6.32, 1.51, 4, 5, 1.51, 10.1)
    xiaoli.append(li)
    hua = gs.cal331(mm60331, mm60331_formula, 1, 3, 2, 8.5, 6.93, 1.58, 1, 3, 8.5, 6.93)
    xiaohua.append(hua)

    mm60341_An = [row['MM60341'], row['MM60342'], row['MM60343'], row['MM60344'], row['MM60345']]
    mm60341_List = [wang, ming, zhang, li, hua]
    mm60341_CODE = gs.get60341(mm60341_An, mm60341_List, mm60331)
    mm60341_CODElist.append(mm60341_CODE)

    mm60351 = row['MM60351'] # 依赖mm60331和mm60341
    mm60351_CODE = gs.get60351(mm60351, mm60331_CODE, [wang, ming, zhang, li, hua])
    mm60351_CODElist.append(mm60351_CODE)


    P4 = row['P4']
    P4_CODE = gs.compareP3(P4)
    P4_codelist.append(P4_CODE)

    mm60411 = row['MM60411'] #
    mm60411_CODE = gs.get60411(mm60411)
    mm60411_CODElist.append(mm60411_CODE)

    mm60421 = row['MM60421'] #
    mm60421_CODE = gs.get60421(mm60421)
    mm60421_CODElist.append(mm60421_CODE)

    mm60431 = row['MM60431_new']
    mm60432 = row['MM60432_new']
    mm60441 = row['MM60441'] # 和计算mm60431算式比较
    shouru_right = gs.cal431(mm60431, 90000, 50000, 10, 8, 0.55, 0.5)
    shouru.append(shouru_right)
    mm60441_CODE = gs.compareFor(mm60441, shouru_right, mm60431)
    mm60441_CODElist.append(mm60441_CODE)

    mm60442 = row['MM60442'] # 和计算mm60432算式比较
    jiage_right = gs.cal431(mm60432, 90000, 50000, 10, 8, 0.55, 0.5)
    jiage.append(jiage_right)
    mm60442_CODE = gs.compareFor(mm60442, jiage_right, mm60432)
    mm60442_CODElist.append(mm60442_CODE)
    
    mm60461 = row['MM60461'] # mm60461的答案取决于461-464
    mm60462 = row['MM60462']
    mm60463 = row['MM60463']
    mm60464 = row['MM60464']
    mm60461_CODE = gs.get60461([mm60461, mm60462, mm60463, mm60464])
    mm60461_CODElist.append(mm60461_CODE)

col_name = data.columns.tolist()

col_name.insert(col_name.index('P3')+1, 'P3_CODE')
data = data.reindex(columns=col_name)
data['P3_CODE'] = P3_codelist

col_name.insert(col_name.index('MM60311')+1, 'MM60311_CODE')
data = data.reindex(columns=col_name)
data['MM60311_CODE'] = mm60311_CODElist

col_name.insert(col_name.index('MM60321')+1, 'MM60321_CODE')
data = data.reindex(columns=col_name)
data['MM60321_CODE'] = mm60321_CODElist

col_name.insert(col_name.index('MM60341')+1, 'wang')
data = data.reindex(columns=col_name)
data['wang'] = xiaowang

col_name.insert(col_name.index('MM60342')+1, 'ming')
data = data.reindex(columns=col_name)
data['ming'] = xiaoming

col_name.insert(col_name.index('MM60343')+1, 'zhang')
data = data.reindex(columns=col_name)
data['zhang'] = xiaozhang

col_name.insert(col_name.index('MM60344')+1, 'li')
data = data.reindex(columns=col_name)
data['li'] = xiaoli

col_name.insert(col_name.index('MM60345')+1, 'hua')
data = data.reindex(columns=col_name)
data['hua'] = xiaohua

col_name.insert(col_name.index('MM60341'), 'MM60341_CODE')
data = data.reindex(columns=col_name)
data['MM60341_CODE'] = mm60341_CODElist

col_name.insert(col_name.index('MM60351')+1, 'MM60351_CODE')
data = data.reindex(columns=col_name)
data['MM60351_CODE'] = mm60351_CODElist

col_name.insert(col_name.index('MM60431')+1, 'shouru')
data = data.reindex(columns=col_name)
data['shouru'] = shouru

col_name.insert(col_name.index('MM60432')+1, 'jiage')
data = data.reindex(columns=col_name)
data['jiage'] = jiage

col_name.insert(col_name.index('P4')+1, 'P4_CODE')
data = data.reindex(columns=col_name)
data['P4_CODE'] = P4_codelist

col_name.insert(col_name.index('MM60411')+1, 'MM60411_CODE')
data = data.reindex(columns=col_name)
data['MM60411_CODE'] = mm60411_CODElist

col_name.insert(col_name.index('MM60421')+1, 'MM60421_CODE')
data = data.reindex(columns=col_name)
data['MM60421_CODE'] = mm60421_CODElist

col_name.insert(col_name.index('MM60441')+1, 'MM60441_CODE')
data = data.reindex(columns=col_name)
data['MM60441_CODE'] = mm60441_CODElist

col_name.insert(col_name.index('MM60442')+1, 'MM60442_CODE')
data = data.reindex(columns=col_name)
data['MM60442_CODE'] = mm60442_CODElist

col_name.insert(col_name.index('MM60461')+1, 'MM60461_CODE')
data = data.reindex(columns=col_name)
data['MM60461_CODE'] = mm60461_CODElist

data.to_excel('a_out_0714.xlsx')