import pandas as pd
from datetime import datetime

time_dict = {}
stop_time_dict = {}
data = pd.read_excel(r'A.xlsx')

datetimeFormat = '%Y-%m-%dT%H:%M:%S.%f+08:00'
datetimeFormat2 = '%Y-%m-%dT%H:%M:%S+08:00'

for index, row in data.iterrows():
    id = str(row['ticket_id'])
    timestamp = str(row['timestamp'])
    if (id not in time_dict.keys()):
        time_dict[id] = []
        time_dict[id].append(timestamp)
    else:
        time_dict[id].append(timestamp)

for key, value in time_dict.items():
    stop_time_dict[key] = value[-1]

data2 = pd.read_excel(r'a_out_0714.xlsx')

stoptime_new_list = []
time_new_list = []
empty = 0

for index, row in data2.iterrows():
    print(index)
    id = str(row['ticket_id'])
    P1_CODE = row['P3_CODE']
    MM60101_CODE = row['MM60311_CODE']
    if (pd.isna(row['stop_time']) and (int(P1_CODE) != 99 or int(MM60101_CODE) != 99)):
        if (id in stop_time_dict.keys()):
            timestamp = stop_time_dict[id]
            stoptime_new_list.append(timestamp)
            try:
                date2 = datetime.strptime(str(timestamp), datetimeFormat)
            except ValueError:
                date2 = datetime.strptime(str(timestamp), datetimeFormat2)
        else:
            empty = empty + 1
            stoptime_new_list.append("")
            time_new_list.append("")
            continue
    elif (pd.isna(row['stop_time']) and int(P1_CODE) == 99 and int(MM60101_CODE) == 99):
        empty = empty + 1
        stoptime_new_list.append("")
        time_new_list.append("")
        continue
    else:
        stoptime_new_list.append("")
        try:
            date2 = datetime.strptime(str(row['stop_time']), datetimeFormat)
        except ValueError:
            date2 = datetime.strptime(str(row['stop_time']), datetimeFormat2)
    try:
        date1 = datetime.strptime(str(row['start_time']), datetimeFormat)
    except ValueError:
        date1 = datetime.strptime(str(row['start_time']), datetimeFormat2)
    delta = date2 - date1
    miao = delta.seconds
    fen = round(miao/60, 2)
    time_new_list.append(fen)

col_name = data2.columns.tolist()

col_name.insert(col_name.index('stop_time')+1, 'stoptime_new')
data2 = data2.reindex(columns=col_name)
data2['stoptime_new'] = stoptime_new_list

col_name.insert(col_name.index('cost_time')+1, 'time_new')
data2 = data2.reindex(columns=col_name)
data2['time_new'] = time_new_list
            
data2.to_excel('a_out_0719.xlsx')