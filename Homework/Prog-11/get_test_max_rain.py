import json
data = json.load(open('th_weather_39.json'))
with open('max_rain.py','a+') as f:
    for i in ('N', 'E', 'W', 'S', 'C', 'NE', 'ALL') : 
        for j in ('2021-04-06','2021-04-07','2021-04-08','2021-04-09','2021-04-10','2021-04-11',) :
            exec("result = max_rain_in_3h_periods(data,'%s','%s')" % (i,j))
            f.write("\t\"assert max_rain_in_3h_periods(data,'%s','%s') == %s\"\n" % (i,j,result))