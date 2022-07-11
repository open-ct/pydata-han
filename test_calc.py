from tabnanny import check
from unittest import result
import pandas as pd
import io
import sys

from py import process
from sqlalchemy import column
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
# 通过以上语句可以在vscode终端里成功print中文
path = r'Ain.csv'
data = pd.read_csv(path)
manu = pd.read_csv(r'a_manu.csv')

file = open("error.txt", "w")

process = []
xiaowang = []
xiaoming = []
xiaozhang = []
xiaoli = []
xiaohua = []
mm60331code = []
mm60431code = []
mm60432code = []
mm60451code = []
code_dict = {}

def getfomula(f):
    s = str(f)
    s = s.replace('该同学50米跑的排名', 'RR')
    s = s.replace('该同学实心球的排名', 'BR')
    s = s.replace('该同学立定跳远的排名', 'JR')
    s = s.replace('该同学50米跑的成绩', 'RS')
    s = s.replace('该同学实心球的成绩', 'BS')
    s = s.replace('该同学立定跳远的成绩', 'JS')
    s = s.replace('该同学表现最好项目的排名', 'GR')
    s = s.replace('该同学表现最差项目的排名', 'WR')
    s = s.replace('该同学表现最好项目的成绩', 'GS')
    s = s.replace('该同学表现最差项目的成绩', 'WS')
    return s

def formatCheck(f):
    checkList = ['RR', 'BR', 'JR', 'RS', 'BS', 'JS', 'GR', 'WR', 'GS', 'WS']
    return ""

def getCalcu(formula, f, RR, BR, JR, RS, BS, JS, GR, WR, GS, WS):
    f = f.replace('RR', str(RR))
    f = f.replace('BR', str(BR))
    f = f.replace('JR', str(JR))
    f = f.replace('RS', str(RS))
    f = f.replace('BS', str(BS))
    f = f.replace('JS', str(JS))
    f = f.replace('GR', str(GR))
    f = f.replace('WR', str(WR))
    f = f.replace('GS', str(GS))
    f = f.replace('WS', str(WS))
    f = f.replace('÷', '/')
    f = f.replace('×', '*')
    result = ""
    try:
        result = eval(f)
        print(f + "=" + str(eval(f)))
    except SyntaxError:
        file.write("SyntaxError   " + str(formula) + "\n")
        return ""
    except NameError:
        file.write("NameError   " + str(formula) + "\n")
        return ""
    except TypeError:
        file.write("TypeError   " + str(formula) + "\n")
        return ""
    return result

for index, row in manu.iterrows():
    l = []
    l.append(row['MM60331'])
    l.append(row['MM60431'])
    l.append(row['MM60432'])
    l.append(row['MM60451'])
    key = str(row['id'])
    code_dict[key] = l
    # print(type(key))

for index, row in data.iterrows():
    id = row['ticket_id']
    print(type(id))
    code = code_dict[str(id)]
    mm60331code.append(code[0])
    mm60431code.append(code[1])
    mm60432code.append(code[2])
    mm60451code.append(code[3])
    formula = row['MM60331']
    s = getfomula(formula)
    process.append(s)
    wang = getCalcu(formula, s, 2, 2, 1, 9.1, 7.15, 1.61, 1, 2, 1.61, 9.1)
    xiaowang.append(wang)
    ming = getCalcu(formula, s, 4, 1, 3, 9.8, 7.82, 1.54, 1, 4, 7.82, 9.8)
    xiaoming.append(ming)
    zhang = getCalcu(formula, s, 3, 4, 5, 9.3, 6.54, 1.47, 3, 5, 9.3, 1.47)
    xiaozhang.append(zhang)
    li = getCalcu(formula, s, 5, 5, 4, 10.1, 6.32, 1.51, 4, 5, 1.51, 10.1)
    xiaoli.append(li)
    hua = getCalcu(formula, s, 1, 3, 2, 8.5, 6.93, 1.58, 1, 3, 8.5, 6.93)
    xiaohua.append(hua)

col_name = data.columns.tolist()

col_name.insert(col_name.index('MM60331')+1, 'Formula')
data = data.reindex(columns=col_name)
data['Formula'] = process

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

col_name.insert(col_name.index('MM60331')+1, 'MM60331_CODE')
data = data.reindex(columns=col_name)
data['MM60331_CODE'] = mm60331code

col_name.insert(col_name.index('MM60431')+1, 'MM60431_CODE')
data = data.reindex(columns=col_name)
data['MM60431_CODE'] = mm60431code

col_name.insert(col_name.index('MM60432')+1, 'MM60432_CODE')
data = data.reindex(columns=col_name)
data['MM60432_CODE'] = mm60432code

col_name.insert(col_name.index('MM60451')+1, 'MM60451_CODE')
data = data.reindex(columns=col_name)
data['MM60451_CODE'] = mm60451code

data.to_excel('out.xlsx')
file.close()
