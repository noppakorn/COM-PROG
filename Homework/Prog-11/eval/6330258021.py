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
    return {reg:[(-val[0],val[1],val[2]) for val in values[:K]] for reg,values in sorted(d.items())}
         
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
    return sorted([(key,max(d[key])) if key in d else (key,0.0) for key in range(0,24,3)])
        
def AM_PM_weather_description_by_region(data, date):
    d = {}
    for values in data.values():
        reg = values['city']['region']
        if reg not in d: d[reg] = {'AM':{},'PM':{}}
        for val in values['list']:
            dt_text = val['dt_txt'].split()
            if dt_text[0] != date : continue
            for wea in val['weather'] :
                wea_desc = wea['description']
                if int(dt_text[1].split(':')[0]) < 12 : 
                    if wea_desc not in d[reg]['AM'] : d[reg]['AM'][wea_desc] = -1
                    else : d[reg]['AM'][wea_desc] -= 1
                else : 
                    if wea_desc not in d[reg]['PM'] : d[reg]['PM'][wea_desc] = -1
                    else : d[reg]['PM'][wea_desc] -= 1
    out = {}
    for key,values in sorted(d.items()):
        out[key] = {}
        if len(values['AM']) > 0 :
            out[key]['AM'] = sorted([(y,x) for x,y in values['AM'].items()])[0][1]
        if len(values['PM']) > 0 :
            out[key]['PM'] = sorted([(y,x) for x,y in values['PM'].items()])[0][1]
    return out

def most_varied_weather_provinces(data):
    d = {}
    for values in data.values():
        name = values['city']['name']
        if name not in d : d[name] = []
        for val in values['list']:
            for wea in val['weather'] :
                d[name].append(wea['description'])
    cd = {}
    for i,j in sorted(d.items()):
        ls = len(set(j))
        if ls not in cd : cd[ls] = {i}
        else : cd[ls].add(i)
    return cd[max(cd.keys())]
        
def main():
    #print(top_K_max_temp_by_region(json.load(open('weather_5_40.json')), 1))
    #print(top_K_max_temp_by_region(json.load(open('weather_5_40.json')), 4))
    print(average_temp_by_date(json.load(open('weather_5_40.json')), 'E'))
    print(average_temp_by_date(json.load(open('weather_5_40.json')), 'S'))
    print(average_temp_by_date(json.load(open('weather_5_40.json')), 'NE'))
    print(average_temp_by_date(json.load(open('weather_5_40.json')), 'ALL'))
    #print(max_rain_in_3h_periods(json.load(open('weather_3_40_all_rain.json')), 'N', '2021-04-28'))
    #print(max_rain_in_3h_periods(json.load(open('weather_3_40_no_rain.json')),  'W', '2021-04-29'))
    #print(max_rain_in_3h_periods(json.load(open('weather_5_40.json')), 'C', '2021-04-30'))
    #print(max_rain_in_3h_periods(json.load(open('weather_10_40.json')), 'ALL', '2021-05-01'))
    #print(max_rain_in_3h_periods(json.load(open('weather_10_40.json')), 'ALL', '2021-05-01'))
    #print(AM_PM_weather_description_by_region(json.load(open('weather_5_40_1.json')), '2021-05-01'))
    #print(most_varied_weather_provinces(json.load(open('weather_5_40_2.json'))))
    exec(open('eval.py').read())
main()