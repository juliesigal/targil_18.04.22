from datetime import datetime, timedelta
import json

with open(r"mini_json_dataset.json") as f:  #load json data
    data = json.load(f)

total_dict = {}

for i in data['duties']:    #check the objects in duties
    j = i['duty_events']
    for each in j:      #check the objects in duty events
        dict_start = {}
        a = i['duty_id']
        if each['duty_event_type'] == 'sign_on':
            #check if sign on type exist
            start = each['start_time']
            for k in data['vehicles']:  # check the objects in vehicles
                l = k['vehicle_events']
                for row in l:  # check the objects in vehicles events
                    dict_end = {}
                    if row['duty_id'] == str(a):
                        if row['vehicle_event_type'] == 'deadhead':
                            end = row['end_time']
                            total_dict[a] = {'start_time': start, 'end_time': end}
                            break
                        else:
                            end = '0.00:00'
                            total_dict[a] = {'start_time': start, 'end_time': end}
        else:
            # check if taxi type exist
            if each['duty_event_type'] == 'taxi':
                end = each['end_time']
                for k in data['vehicles']:  # check the objects in vehicles
                    l = k['vehicle_events']
                    for row in l:  # check the objects in vehicles events
                        dict_end = {}
                        if row['duty_id'] == str(a):
                            if row['vehicle_event_type'] == 'pre_trip':
                                start = row['start_time']
                                total_dict[a] = {'start_time': start, 'end_time': end}
                                break
for k in data['vehicles']:  # check the objects in vehicles
    l = k['vehicle_events']
    for row in l:
        a = row['duty_id']
        if a in total_dict.keys():
            continue
        else:
            if row['vehicle_event_type'] == 'pre_trip':
                start = row['start_time']
                end = row['end_time']
                total_dict[a] = {'start_time': start, 'end_time': end}
                continue




def print_result():
    i = 1
    total_lst = [['DUTY ID','START TIME', 'END TIME']]
    while i < 145:
        temp_lst = []
        for j in total_dict.keys():
            if int(j) == i:
                temp_lst.append(j)
                a = total_dict[j]['start_time'].split(".")[1]
                temp_lst.append(a)
                b = total_dict[j]['end_time'].split(".")[1]
                temp_lst.append(b)
                continue
        i += 1
        total_lst.append(temp_lst)
    for i in total_lst:
        for j in i:
            print(str(j), end=" ")
        print()

print_result()
