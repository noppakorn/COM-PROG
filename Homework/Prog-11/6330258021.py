# Prog-11: Weather report (EP.2)
# 6330258021 Noppakorn Jiravaranun

import json
import math

def top_K_max_temp_by_region(data, K):
    d = {}
    for values in data.values() :
        reg = values['city']['region']
        name = values['city']['name']
        if reg not in d:
            d[reg] = [(-i['main']['temp'],name,i['dt_txt']) for i in values['list']]
        else : 
            for j in values['list']:
                d[reg].append((-j['main']['temp'],name,j['dt_txt']))
    for e in d: d[e].sort()
    return {reg:[(-val[0],val[1],val[2]) for val in values[:min(len(values),K)]] for reg,values in sorted(d.items())}
         
def average_temp_by_date(data, region):
    d = {}
    for values in data.values() :
        if region == 'ALL' or values['city']['region'] == region : 
            for val in values['list'] : 
                day = val['dt_txt'].split()[0]
                if day not in d : d[day] = [val['main']['temp']]
                else : d[day].append(val['main']['temp'])
    return sorted([(key,sum(values)/len(values)) for key,values in d.items()])

def max_rain_in_3h_periods(data, region, date):
    d = {}
    for values in data.values() :
        if region == 'ALL' or values['city']['region'] == region : 
            for val in values['list']:
                dt_text = val['dt_txt'].split()
                if dt_text[0] == date and 'rain' in val:
                    hour = int(dt_text[1].split(':')[0])
                    if hour not in d : d[hour] = [val['rain']['3h']]
                    else : d[hour].append(val['rain']['3h'])
    return sorted([(key,max(values)) for key,values in d.items()])
        
def AM_PM_weather_description_by_region(data, date):
    d = {}
    for values in data.values():
        reg = values['city']['region']
        if reg not in d: d[reg] = {'AM':{},'PM':{}}
        for val in values['list']:
            dt_text = val['dt_txt'].split()
            if dt_text[0] != date : continue
            wea_desc = val['weather'][0]['description']
            if int(dt_text[1].split(':')[0]) < 12 : 
                if wea_desc not in d[reg]['AM'] : d[reg]['AM'][wea_desc] = -1
                else : d[reg]['AM'][wea_desc] -= 1
            else : 
                if wea_desc not in d[reg]['PM'] : d[reg]['PM'][wea_desc] = -1
                else : d[reg]['PM'][wea_desc] -= 1
    return {key:{'AM' : sorted([(y,x) for x,y in values['AM'].items()])[0][1], 'PM' : sorted([(y,x) for x,y in values['PM'].items()])[0][1]} for key,values in sorted(d.items())}

def most_varied_weather_provinces(data):
    d = {}
    for values in data.values():
        name = values['city']['name']
        if name not in d : d[name] = [val['weather'][0]['description'] for val in values['list']]
        else :
            for val in values['list']: d[name].append(val['weather'][0]['description'])
    cd = {}
    for i,j in sorted(d.items()):
        ls = len(set(j))
        if ls not in cd : cd[ls] = {i}
        else : cd[ls].add(i)
    return cd[max(cd.keys())]
        
def main():
    data = json.load(open('th_weather_39.json'))
    print(top_K_max_temp_by_region(data, 2))
    print(average_temp_by_date(data, 'C'))
    print(max_rain_in_3h_periods(data, 'ALL', '2021-04-07'))
    print(AM_PM_weather_description_by_region(data, '2021-04-09'))
    print(most_varied_weather_provinces(data))
main()