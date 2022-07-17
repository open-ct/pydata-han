
from decimal import MAX_EMAX
from itertools import count
from turtle import right
from unittest import result
import pandas as pd

file = open("error1.txt", "w")

def compareUp(right, answer):
    if (pd.isna(right) or pd.isna(answer) or right=="" or answer==""):
        return False
    try:
        right = float(right)
        answer = float(answer)
    except ValueError:
        return False
    if (right < 10):
        right = right * 10
        answer = answer * 10
    try:
        r = [int(right), round(right), int(100*right), round(100*right)]
        print(r)
    except OverflowError:
        return False
    a1 = int(answer)
    a2 = round(answer)
    if (a1 in r):
        return True
    if (a2 in r):
        return True
    return False

def compare(right, answer):
    # 考虑：原答案、原答案四舍五入的结果
    # 考虑：正确答案、正确答案四舍五入的结果
    # 仅考虑整数部分、若两者有相同情况则返回true
    if (pd.isna(right) or pd.isna(answer) or right=="" or answer==""):
        return False
    try:
        right = float(right)
        answer = float(answer)
    except ValueError:
        return False
    if (right < 10):
        right = right * 10
        answer = answer * 10
    try:
        r = [int(right), round(right)]
    except OverflowError:
        return False
    a1 = int(answer)
    a2 = round(answer)
    if (a1 in r):
        return True
    if (a2 in r):
        return True
    return False

def compareZ(code104, right, answer):
    if (pd.isna(right) or pd.isna(answer) or right=="" or answer==""):
        return 99
    try:
        right = float(right)
        answer = float(answer)
    except ValueError:
        return 70
    result = compare(right, answer)
    if (result):
        if (code104 != 40):
            if (answer == 450):
                return 74
            elif(answer >= 440 and answer <= 460):
                return 41
            elif (answer < 440):
                return 42
            elif (answer > 460):
                return 43
        else:
            return 40
    else:
        if (answer == 450):
            return 74
        elif(answer >= 440 and answer <= 460):
            return 71
        elif (answer < 440):
            return 72
        elif (answer > 460):
            return 73
    return 70

def compareFor(answer, right, formula):
    try:
        eval(formula)
        return 70
    except:
        pass
    if (pd.isna(right) or pd.isna(answer) or right=="" or answer==""):
        return 99
    if (compareUp(right, answer)):
        return 40
    return 70


def compareP3(input):
    # 是否会出现序列数字不为4个的情况？
    s = str(input)
    s = s.replace(' ', '')
    if (s == ""):
        return 99
    l = s.split(',')
    if (len(l) < 4):
        return 99
    count = 0
    if (l[0] == 'B'):
        count = count + 1
    if (l[1] == 'D'):
        count= count + 1
    if (l[2] == 'A'):
        count= count + 1
    if (l[3] == 'C'):
        count= count + 1
    if (count == 0):
        return 70
    elif (count == 1):
        return 10
    elif (count == 2):
        return 20
    elif (count == 3):
        return 30
    else:
        return 40

def get60107(mm71, mm72, mm60105):
    if (pd.isna(mm71) or pd.isna(mm72) or mm71=="" or mm72==""):
        return 99
    if (mm60105 == 40 and mm71 =='A' and mm72 == 'D'):
        return 20
    if (mm60105 == 40 and mm71 =='A' and mm72 == 'A'):
        return 40 
    if (mm60105 in [71, 41] and mm71 =='A' and mm72 == 'A'):
        return 41
    if (mm60105 in [72, 42] and mm71 =='B' and mm72 == 'D'):
        return 42
    if (mm60105 in [73, 43] and mm71 =='B' and mm72 == 'C'):
        return 43
    if (mm60105 == 74 and mm71 =='A' and mm72 == 'B'):
        return 44
    return 70

def get60108(answer, mm60102_CODE):
    blank = 0
    count = 0
    for i in range(4):
        if (pd.isna(answer[i]) or answer[i] == ""):
            blank = blank + 1
    if (blank == 4):
        return 99
    if (answer[0] == 'A'):
        count = count + 1
    if (answer[1] == 'C'):
        count= count + 1
    if (answer[2] == 'B'):
        count= count + 1
    if (answer[3] == 'A'):
        count= count + 1
    if (count == 2):
        return 10
    if (count == 3):
        return 20
    if (count == 4):
        return 40
    if (mm60102_CODE == 30 and answer[0] == 'A' and answer[1] == 'A' and answer[2] == 'B' and answer[3] == 'A'):
        return 41
    return 70

def get60311(answer, mm60331_CODE):
    if (answer == "" or pd.isna(answer)):
        return 99
    if (answer == "D"):
        return 40
    if (answer == 'A' and mm60331_CODE in [31, 35, 41, 45]):
        return 30
    if (answer == 'B' and mm60331_CODE in [32, 36, 42, 46]):
        return 31
    if (answer == 'C' and mm60331_CODE in [33, 37, 43, 47]):
        return 32
    return 70

def get60101(answer):
    if (answer == "" or pd.isna(answer)):
        return 99
    if (answer == "C"):
        return 40
    return 70

def get60321(answer):
    if (answer == "" or pd.isna(answer)):
        return 99
    if (answer == "D"):
        return 40
    if (answer == "C"):
        return 20
    return 70

def get60411(answer):
    if (answer == "" or pd.isna(answer)):
        return 99
    if (answer == "B"):
        return 40
    return 70

def get60421(answer):
    if (answer == "" or pd.isna(answer)):
        return 99
    if (answer == "C"):
        return 40
    if (answer == "B"):
        return 20
    return 70

def get60102(answer):
    if (answer == "" or pd.isna(answer)):
        return 99
    s = str(answer)
    s = s.replace(' ', '')
    l = s.split(',')
    right = ['A', 'D', 'E', 'H']
    right
    if (len(l) == 2 and l[0] in right and l[1] in right):
        return 20
    if (len(l) == 3 and l[0] in right and l[1] in right and l[2] in right):
        return 20
    if (len(l) == 4 and l[0] in right and l[1] in right and l[2] in right and l[3] in right):
        return 40
    if (len(l) == 5):
        if ('G' in l):
            return 30
        else:
            return 31
    return 70

def get60341(answer, right, formula):
    try:
        eval(formula)
        return 70
    except:
        pass
    # 空白是全部空白吗？
    count = 0
    blank = 0
    for i in range(5):
        if (pd.isna(answer[i]) or answer[i] == ""):
            blank = blank + 1
    if (blank == 5):
        return 99
    for i in range(5):
        if (pd.isna(answer[i]) or pd.isna(right[i])):
            continue
        if (compare(answer[i], right[i])):
            count = count + 1
    if (count == 0):
        return 70
    if (count == 1):
        return 71
    if (count == 2):
        return 10
    if (count == 3):
        return 20
    if (count == 4):
        return 30
    if (count == 5):
        return 40

def cal331(formula, f, RR, BR, JR, RS, BS, JS, GR, WR, GS, WS):
    f = str(f)
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

def cal104(formula, f, E, L, V, W, T, C, G, U, D, P):
    f = str(f)
    f = f.replace('L', str(L))
    f = f.replace('V', str(V))
    f = f.replace('C', str(C))
    f = f.replace('G', str(G))
    f = f.replace('D', str(D))
    f = f.replace('P', str(P))
    f = f.replace('E', str(E))
    f = f.replace('T', str(T))
    f = f.replace('W', str(W))
    f = f.replace('U', str(U))
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
    return str(result)

def cal431(f, Y, y, A, a, B, b):
    f = str(f)
    f = f.replace('Y', str(Y))
    f = f.replace('y', str(y))
    f = f.replace('A', str(A))
    f = f.replace('B', str(B))
    f = f.replace('a', str(a))
    f = f.replace('b', str(b))
    f = f.replace('÷', '/')
    f = f.replace('×', '*')
    result = ""
    try:
        result = eval(f)
        print(f + "=" + str(eval(f)))
    except SyntaxError:
        file.write("SyntaxError   " + str(f) + "\n")
        return ""
    except NameError:
        file.write("NameError   " + str(f) + "\n")
        return ""
    except TypeError:
        file.write("TypeError   " + str(f) + "\n")
        return ""
    except ZeroDivisionError:
        file.write("ZeroDivisionError   " + str(f) + "\n")
        return ""
    except OverflowError:
        file.write("OverflowError   " + str(f) + "\n")
        return ""
    return result


def get331(f):
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

def get104(f):
    s = str(f)
    s = s.replace('每人每天要刷2次牙', 'E')
    s = s.replace('牙刷的长度为18厘米', 'L')
    s = s.replace('漱口杯的容量为500毫升', 'V')
    s = s.replace('水龙头1分钟会流出3升水', 'W')
    s = s.replace('每次刷牙平均需要3分钟', 'T')
    s = s.replace('刷牙时的水温为25摄氏度', 'C')
    s = s.replace('每次刷牙要使用1厘米牙膏', 'G')
    s = s.replace('每次正常刷牙使用1升水（用于漱口、冲洗牙刷等）', 'U')
    s = s.replace('每周7天', 'D')
    s = s.replace('家中包括4个成员', 'P')
    return s


def get60351(answer, mm60331, l):
    max_student = l.index(max(l))
    min_student = l.index(min(l))
    max_student = ['A', 'B', 'C', 'D', 'E'][max_student]
    min_student = ['A', 'B', 'C', 'D', 'E'][min_student]
    if (answer == '' or pd.isna(answer)):
        return 99
    if (mm60331 in [10, 72] and answer == max_student):
        return 20
    if (mm60331 in [20, 38] and answer == max_student):
        return 30
    if (mm60331 in [30, 31, 32, 33, 40, 41, 42, 43] and answer == min_student):
        return 40
    if (mm60331 in [34, 35, 36, 37, 44, 45, 46, 47] and answer == max_student):
        return 41
    return 70

def get60461(answer):
    count = 0
    blank = 0
    right = ['B', 'A', 'A', 'B']
    for i in range(4):
        if (pd.isna(answer[i]) or answer[i] == ""):
            blank = blank + 1
    if (blank == 4):
        return 99
    for i in range(4):
        if (pd.isna(answer[i]) or pd.isna(right[i])):
            continue
        if (answer[i] == right[i]):
            count = count + 1
    if (count == 1):
        return 10
    if (count == 2):
        return 20
    if (count == 3):
        return 30
    if (count == 4):
        return 40
    return 70