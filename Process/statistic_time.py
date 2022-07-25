import pandas as pd

data_a = pd.read_excel(r'a_out_0719.xlsx')
data_z = pd.read_excel(r'z_out_0719.xlsx')

level0to3 = 0
level3to6 = 0
level6to9 = 0
level9to12 = 0
level12to15 = 0
levelabove15 = 0

level0to5 = 0
level5to10 = 0
level10to15 = 0
level15to20 = 0
level20to25 = 0
level25to30 = 0
levelabove30 = 0

print("A")
for index, row in data_a.iterrows():
    if (pd.isna(row['time_new'])):
        continue
    fen = float(row['time_new'])
    if (fen <= 5):
        level0to5 = level0to5 + 1
    elif (fen > 5 and fen <= 10):
        level5to10 = level5to10 + 1
    elif (fen > 10 and fen <= 15):
        level10to15 = level10to15 + 1
    elif (fen > 15 and fen <= 20):
        level15to20 = level15to20 + 1
    elif (fen > 20 and fen <= 25):
        level20to25 = level20to25 + 1
    elif (fen > 25 and fen <= 30):
        level25to30 = level25to30 + 1
    else:
        levelabove30 = levelabove30 + 1
print(level0to5, level5to10, level10to15, level15to20, level20to25, level25to30, levelabove30)

print("z")
for index, row in data_z.iterrows():
    if (pd.isna(row['time_new'])):
        continue
    fen = float(row['time_new'])
    if (fen <= 3):
        level0to3 = level0to3 + 1
    elif (fen > 3 and fen <= 6):
        level3to6 = level3to6 + 1
    elif (fen > 6 and fen <= 9):
        level6to9 = level6to9 + 1
    elif (fen > 9 and fen <= 12):
        level9to12 = level9to12 + 1
    elif (fen > 12 and fen <= 15):
        level12to15 = level12to15 + 1
    else:
        levelabove15 = levelabove15 + 1

print(level0to3, level3to6, level6to9, level9to12, level12to15,levelabove15)