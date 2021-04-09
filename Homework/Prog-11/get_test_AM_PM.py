import json
data = json.load(open('th_weather_39.json'))
l = [  
    "AM_PM_weather_description_by_region(data, '2021-04-06')",
    "AM_PM_weather_description_by_region(data, '2021-04-07')",
    "AM_PM_weather_description_by_region(data, '2021-04-08')",
    "AM_PM_weather_description_by_region(data, '2021-04-09')",
    "AM_PM_weather_description_by_region(data, '2021-04-10')",
    "AM_PM_weather_description_by_region(data, '2021-04-11')",
]
with open('AM_PM.py','a+') as f : 
    for i in l :
        exec('result = %s' % i)
        f.write("\t\"assert %s == %s\"," %(i,result))
        f.write('\n')