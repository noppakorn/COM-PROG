import time
import sys
import json
dash = '-'*60
cfn = open(__file__).readlines()
id_name = cfn[1].strip().split()
print(dash)
print('Prog-11: Weather report (EP.2) testcases by Meen')
try : print('Name:',id_name[2],id_name[3])
except:
    print(dash)
    print("Please add exec(open('%s').read())\nto the end of the main() function of your code." % __file__[-15:])
    print('Then run you code not this file!!')
    print(dash)
    sys.exit(0)
id = id_name[1]
print('ID:',id)
if len(id) != 10 or __file__[-13:-3] != id :
    print('----- Check your id and File Name -----')
    sys.exit()
print('Please Check if your information is correct')
print(dash)
time.sleep(1)
start = time.time()
result = {}
# The Case number is corresponds with linenumber-30
# For example Case 1 is line 31, Case 2 is line 32 and so on
# You can copy that entire line and paste it in your code and then remove the " sign 
# from the front and back assert just means check if the statement is True
test = [
    "assert top_K_max_temp_by_region(data,2) == {'C': [(38.54, 'Sukhothai Thani', '2021-04-09 06:00:00'),(38.18, 'Phitsanulok', '2021-04-09 06:00:00')],'E': [(36.45, 'Prachin Buri','2021-04-09 06:00:00'),(36.15, 'Chachoengsao','2021-04-09 09:00:00')],'N': [(38.98, 'Mae Hong Son', '2021-04-10 06:00:00'),(38.73, 'Mae Hong Son', '2021-04-10 09:00:00')],'NE': [(37.31, 'Surin', '2021-04-06 09:00:00'),(37.29, 'Ubon Ratchathani','2021-04-10 09:00:00')],'S': [(34.93, 'Yala','2021-04-10 06:00:00'),(34.74, 'Yala', '2021-04-07 06:00:00')],'W': [(38.97, 'Kanchanaburi','2021-04-09 09:00:00'),(38.11, 'Kanchanaburi', '2021-04-09 06:00:00')]}",
    "assert top_K_max_temp_by_region(data,10) == {'C': [(38.54, 'Sukhothai Thani', '2021-04-09 06:00:00'), (38.18, 'Phitsanulok', '2021-04-09 06:00:00'), (37.88, 'Sukhothai Thani', '2021-04-09 09:00:00'), (37.7, 'Nakhon Sawan', '2021-04-10 09:00:00'), (37.66, 'Nakhon Sawan', '2021-04-09 06:00:00'), (37.53, 'Nakhon Sawan', '2021-04-09 09:00:00'), (37.5, 'Suphan Buri', '2021-04-10 06:00:00'), (37.44, 'Nakhon Sawan', '2021-04-08 09:00:00'), (37.43, 'Chainat', '2021-04-09 09:00:00'), (37.42, 'Suphan Buri', '2021-04-09 06:00:00')], 'E': [(36.45, 'Prachin Buri', '2021-04-09 06:00:00'), (36.15, 'Chachoengsao', '2021-04-09 09:00:00'), (35.85, 'Chachoengsao', '2021-04-09 06:00:00'), (35.5, 'Chachoengsao', '2021-04-10 06:00:00'), (35.49, 'Prachin Buri', '2021-04-10 06:00:00'), (35.09, 'Prachin Buri', '2021-04-09 09:00:00'), (34.91, 'Prachin Buri', '2021-04-10 09:00:00'), (34.16, 'Prachin Buri', '2021-04-07 06:00:00'), (34.09, 'Chon Buri', '2021-04-09 06:00:00'), (34.04, 'Chachoengsao', '2021-04-07 06:00:00')], 'N': [(38.98, 'Mae Hong Son', '2021-04-10 06:00:00'), (38.73, 'Mae Hong Son', '2021-04-10 09:00:00'), (38.32, 'Mae Hong Son', '2021-04-09 06:00:00'), (38.27, 'Phrae', '2021-04-09 06:00:00'), (37.74, 'Lampang', '2021-04-09 09:00:00'), (37.64, 'Lampang', '2021-04-09 06:00:00'), (37.61, 'Lamphun', '2021-04-10 06:00:00'), (37.36, 'Mae Hong Son', '2021-04-08 09:00:00'), (37.19, 'Lampang', '2021-04-10 06:00:00'), (37.05, 'Mae Hong Son', '2021-04-08 06:00:00')], 'NE': [(37.31, 'Surin', '2021-04-06 09:00:00'), (37.29, 'Ubon Ratchathani', '2021-04-10 09:00:00'), (37.22, 'Surin', '2021-04-10 09:00:00'), (36.89, 'Buriram', '2021-04-09 06:00:00'), (36.85, 'Kalasin', '2021-04-08 09:00:00'), (36.79, 'Surin', '2021-04-09 06:00:00'), (36.58, 'Buriram', '2021-04-10 09:00:00'), (36.58, 'Udon Thani', '2021-04-08 09:00:00'), (36.5, 'Surin', '2021-04-10 06:00:00'), (36.48, 'Buriram', '2021-04-10 06:00:00')], 'S': [(34.93, 'Yala', '2021-04-10 06:00:00'), (34.74, 'Yala', '2021-04-07 06:00:00'), (34.67, 'Yala', '2021-04-09 06:00:00'), (34.16, 'Yala', '2021-04-08 06:00:00'), (33.37, 'Chumphon', '2021-04-09 06:00:00'), (33.29, 'Chumphon', '2021-04-08 06:00:00'), (32.74, 'Nakhon Si Thammarat', '2021-04-09 06:00:00'), (32.61, 'Yala', '2021-04-07 09:00:00'), (32.6, 'Nakhon Si Thammarat', '2021-04-08 06:00:00'), (32.33, 'Nakhon Si Thammarat', '2021-04-10 06:00:00')], 'W': [(38.97, 'Kanchanaburi', '2021-04-09 09:00:00'), (38.11, 'Kanchanaburi', '2021-04-09 06:00:00'), (37.45, 'Kanchanaburi', '2021-04-08 09:00:00'), (37.44, 'Kanchanaburi', '2021-04-10 06:00:00'), (37.27, 'Ratchaburi', '2021-04-09 06:00:00'), (36.47, 'Ratchaburi', '2021-04-09 09:00:00'), (36.31, 'Kanchanaburi', '2021-04-07 09:00:00'), (36.24, 'Kanchanaburi', '2021-04-08 06:00:00'), (36.16, 'Ratchaburi', '2021-04-08 06:00:00'), (36.13, 'Ratchaburi', '2021-04-08 09:00:00')]}",
    "assert average_temp_by_date(data, 'C') == [('2021-04-06',28.395740740740735),('2021-04-07', 28.821388888888887),('2021-04-08', 30.702083333333334),('2021-04-09', 31.940138888888896),('2021-04-10', 31.774027777777786),('2021-04-11', 30.828333333333333)]",
    "assert average_temp_by_date(data, 'E') == [('2021-04-06', 28.506333333333334), ('2021-04-07', 28.919), ('2021-04-08', 28.357999999999997), ('2021-04-09', 30.100250000000006), ('2021-04-10', 29.88675), ('2021-04-11', 29.740000000000002)]",
    "assert average_temp_by_date(data, 'N') == [('2021-04-06', 21.47916666666667), ('2021-04-07', 26.742708333333326), ('2021-04-08', 28.78999999999999), ('2021-04-09', 30.37937500000001), ('2021-04-10', 29.014166666666664), ('2021-04-11', 28.22416666666666)]",
    "assert average_temp_by_date(data, 'NE') == [('2021-04-06', 30.630238095238095), ('2021-04-07', 28.294642857142858), ('2021-04-08', 31.05017857142857), ('2021-04-09', 31.009999999999994), ('2021-04-10', 31.15964285714285), ('2021-04-11', 29.378571428571433)]",
    "assert average_temp_by_date(data, 'S') == [('2021-04-06', 27.736250000000002), ('2021-04-07', 27.223750000000003), ('2021-04-08', 27.476874999999996), ('2021-04-09', 27.734531249999993), ('2021-04-10', 27.745937500000007), ('2021-04-11', 27.8125)]",
    "assert average_temp_by_date(data, 'W') == [('2021-04-06', 28.77875), ('2021-04-07', 28.356875000000002), ('2021-04-08', 29.423125000000002), ('2021-04-09', 30.708125), ('2021-04-10', 30.065312499999994), ('2021-04-11', 29.435)]",
    "assert average_temp_by_date(data, 'ALL') == [('2021-04-06', 27.650897435897416), ('2021-04-07', 28.044198717948728), ('2021-04-08', 29.37711538461539), ('2021-04-09', 30.308141025641), ('2021-04-10', 29.99567307692307), ('2021-04-11', 29.266410256410254)]",
    "assert max_rain_in_3h_periods(data,'N','2021-04-06') == [(0, 0.0), (3, 0.0), (6, 6.94), (9, 4.49), (12, 0.35), (15, 0.1), (18, 0.25), (21, 0.67)]",
    "assert max_rain_in_3h_periods(data,'N','2021-04-07') == [(0, 0.0), (3, 0.0), (6, 0.0), (9, 0.0), (12, 0.0), (15, 0.33), (18, 0.36), (21, 0.36)]",
    "assert max_rain_in_3h_periods(data,'N','2021-04-08') == [(0, 1.31), (3, 0.12), (6, 0.0), (9, 0.0), (12, 0.0), (15, 0.0), (18, 0.0), (21, 0.0)]",
    "assert max_rain_in_3h_periods(data,'N','2021-04-09') == [(0, 0.0), (3, 0.0), (6, 0.0), (9, 0.0), (12, 0.0), (15, 0.0), (18, 0.0), (21, 0.12)]",
    "assert max_rain_in_3h_periods(data,'N','2021-04-10') == [(0, 0.21), (3, 0.13), (6, 0.0), (9, 0.38), (12, 6.95), (15, 2.88), (18, 0.0), (21, 0.0)]",
    "assert max_rain_in_3h_periods(data,'N','2021-04-11') == [(0, 0.27), (3, 0.0), (6, 0.0), (9, 0.0), (12, 0.0), (15, 0.0), (18, 0.0), (21, 0.0)]",
    "assert max_rain_in_3h_periods(data,'E','2021-04-06') == [(0, 0.0), (3, 0.0), (6, 4.23), (9, 1.83), (12, 1.37), (15, 0.94), (18, 0.48), (21, 3.43)]",
    "assert max_rain_in_3h_periods(data,'E','2021-04-07') == [(0, 2.73), (3, 4.81), (6, 0.99), (9, 1.45), (12, 0.63), (15, 2), (18, 2.72), (21, 4.64)]",
    "assert max_rain_in_3h_periods(data,'E','2021-04-08') == [(0, 0.22), (3, 3.82), (6, 1.91), (9, 1.22), (12, 0.35), (15, 0.47), (18, 1.32), (21, 1.63)]",
    "assert max_rain_in_3h_periods(data,'E','2021-04-09') == [(0, 3.62), (3, 3.34), (6, 1.5), (9, 0.7), (12, 0.0), (15, 0.56), (18, 0.49), (21, 3.14)]",
    "assert max_rain_in_3h_periods(data,'E','2021-04-10') == [(0, 4.01), (3, 1.82), (6, 1.06), (9, 0.96), (12, 0.47), (15, 0.0), (18, 1.29), (21, 1.57)]",
    "assert max_rain_in_3h_periods(data,'E','2021-04-11') == [(0, 2.37), (3, 2.61), (6, 0.0), (9, 0.0), (12, 0.0), (15, 0.0), (18, 0.0), (21, 0.0)]",
    "assert max_rain_in_3h_periods(data,'W','2021-04-06') == [(0, 0.0), (3, 0.0), (6, 0.9), (9, 0.24), (12, 0.66), (15, 3.8), (18, 3.24), (21, 0.0)]",
    "assert max_rain_in_3h_periods(data,'W','2021-04-07') == [(0, 0.1), (3, 0.49), (6, 0.33), (9, 0.41), (12, 10.68), (15, 13.35), (18, 3.66), (21, 0.0)]",
    "assert max_rain_in_3h_periods(data,'W','2021-04-08') == [(0, 0.0), (3, 0.0), (6, 0.0), (9, 0.91), (12, 16.38), (15, 2.35), (18, 0.0), (21, 0.0)]",
    "assert max_rain_in_3h_periods(data,'W','2021-04-09') == [(0, 0.0), (3, 0.0), (6, 0.0), (9, 0.0), (12, 0.52), (15, 0.0), (18, 0.0), (21, 0.0)]",
    "assert max_rain_in_3h_periods(data,'W','2021-04-10') == [(0, 0.28), (3, 0.0), (6, 0.21), (9, 0.21), (12, 0.98), (15, 1.55), (18, 0.0), (21, 0.9)]",
    "assert max_rain_in_3h_periods(data,'W','2021-04-11') == [(0, 1.08), (3, 0.0), (6, 0.0), (9, 0.0), (12, 0.0), (15, 0.0), (18, 0.0), (21, 0.0)]",
    "assert max_rain_in_3h_periods(data,'S','2021-04-06') == [(0, 0.0), (3, 0.0), (6, 2.46), (9, 3.96), (12, 4.76), (15, 2.28), (18, 0.85), (21, 3.42)]",
    "assert max_rain_in_3h_periods(data,'S','2021-04-07') == [(0, 1.58), (3, 2.55), (6, 5.66), (9, 1.19), (12, 1.87), (15, 1.2), (18, 0.5), (21, 0.0)]",
    "assert max_rain_in_3h_periods(data,'S','2021-04-08') == [(0, 0.0), (3, 0.0), (6, 0.31), (9, 1.06), (12, 1.62), (15, 4.75), (18, 2.08), (21, 2.79)]",
    "assert max_rain_in_3h_periods(data,'S','2021-04-09') == [(0, 2), (3, 0.43), (6, 0.25), (9, 1.45), (12, 3.22), (15, 4.57), (18, 4.01), (21, 1.76)]",
    "assert max_rain_in_3h_periods(data,'S','2021-04-10') == [(0, 2.19), (3, 1.35), (6, 3.42), (9, 6.61), (12, 7.52), (15, 8.05), (18, 0.85), (21, 0.79)]",
    "assert max_rain_in_3h_periods(data,'S','2021-04-11') == [(0, 0.84), (3, 0.0), (6, 0.0), (9, 0.0), (12, 0.0), (15, 0.0), (18, 0.0), (21, 0.0)]",
    "assert max_rain_in_3h_periods(data,'C','2021-04-06') == [(0, 0.0), (3, 0.0), (6, 0.75), (9, 8.96), (12, 5.54), (15, 26.08), (18, 2.21), (21, 3.57)]",
    "assert max_rain_in_3h_periods(data,'C','2021-04-07') == [(0, 3.52), (3, 1.27), (6, 0.11), (9, 0.6), (12, 0.32), (15, 2.32), (18, 1.64), (21, 2.11)]",
    "assert max_rain_in_3h_periods(data,'C','2021-04-08') == [(0, 4.32), (3, 0.12), (6, 0.0), (9, 0.0), (12, 0.12), (15, 0.26), (18, 0.0), (21, 0.12)]",
    "assert max_rain_in_3h_periods(data,'C','2021-04-09') == [(0, 0.24), (3, 0.0), (6, 0.0), (9, 0.35), (12, 0.36), (15, 0.59), (18, 0.81), (21, 0.37)]",
    "assert max_rain_in_3h_periods(data,'C','2021-04-10') == [(0, 1.94), (3, 1.26), (6, 0.48), (9, 0.13), (12, 1.34), (15, 0.66), (18, 0.36), (21, 0.14)]",
    "assert max_rain_in_3h_periods(data,'C','2021-04-11') == [(0, 0.41), (3, 2.49), (6, 0.0), (9, 0.0), (12, 0.0), (15, 0.0), (18, 0.0), (21, 0.0)]",
    "assert max_rain_in_3h_periods(data,'NE','2021-04-06') == [(0, 0.0), (3, 0.0), (6, 1.34), (9, 1.94), (12, 1.28), (15, 0.17), (18, 1.27), (21, 2.16)]",
    "assert max_rain_in_3h_periods(data,'NE','2021-04-07') == [(0, 2.29), (3, 0.3), (6, 0.64), (9, 0.54), (12, 0.54), (15, 0.31), (18, 1.54), (21, 0.81)]",
    "assert max_rain_in_3h_periods(data,'NE','2021-04-08') == [(0, 0.28), (3, 0.0), (6, 0.0), (9, 0.0), (12, 0.0), (15, 0.0), (18, 0.0), (21, 1.6)]",
    "assert max_rain_in_3h_periods(data,'NE','2021-04-09') == [(0, 0.85), (3, 0.0), (6, 0.0), (9, 0.1), (12, 0.13), (15, 0.62), (18, 0.19), (21, 0.88)]",
    "assert max_rain_in_3h_periods(data,'NE','2021-04-10') == [(0, 0.69), (3, 0.2), (6, 0.0), (9, 0.0), (12, 0.0), (15, 0.16), (18, 0.0), (21, 0.0)]",
    "assert max_rain_in_3h_periods(data,'NE','2021-04-11') == [(0, 0.4), (3, 0.44), (6, 0.0), (9, 0.0), (12, 0.0), (15, 0.0), (18, 0.0), (21, 0.0)]",
    "assert max_rain_in_3h_periods(data,'ALL','2021-04-06') == [(0, 0.0), (3, 0.0), (6, 6.94), (9, 8.96), (12, 5.54), (15, 26.08), (18, 3.24), (21, 3.57)]",
    "assert max_rain_in_3h_periods(data,'ALL','2021-04-07') == [(0, 3.52), (3, 4.81), (6, 5.66), (9, 1.45), (12, 10.68), (15, 13.35), (18, 3.66), (21, 4.64)]",
    "assert max_rain_in_3h_periods(data,'ALL','2021-04-08') == [(0, 4.32), (3, 3.82), (6, 1.91), (9, 1.22), (12, 16.38), (15, 4.75), (18, 2.08), (21, 2.79)]",
    "assert max_rain_in_3h_periods(data,'ALL','2021-04-09') == [(0, 3.62), (3, 3.34), (6, 1.5), (9, 1.45), (12, 3.22), (15, 4.57), (18, 4.01), (21, 3.14)]",
    "assert max_rain_in_3h_periods(data,'ALL','2021-04-10') == [(0, 4.01), (3, 1.82), (6, 3.42), (9, 6.61), (12, 7.52), (15, 8.05), (18, 1.29), (21, 1.57)]",
    "assert max_rain_in_3h_periods(data,'ALL','2021-04-11') == [(0, 2.37), (3, 2.61), (6, 0.0), (9, 0.0), (12, 0.0), (15, 0.0), (18, 0.0), (21, 0.0)]",
    "assert AM_PM_weather_description_by_region(data, '2021-04-06') == {'C': {'AM': 'light rain', 'PM': 'light rain'}, 'E': {'AM': 'light rain', 'PM': 'overcast clouds'}, 'N': {'AM': 'light rain', 'PM': 'few clouds'}, 'NE': {'AM': 'broken clouds', 'PM': 'overcast clouds'}, 'S': {'AM': 'light rain', 'PM': 'light rain'}, 'W': {'AM': 'light rain', 'PM': 'light rain'}}",
    "assert AM_PM_weather_description_by_region(data, '2021-04-07') == {'C': {'AM': 'broken clouds', 'PM': 'light rain'}, 'E': {'AM': 'light rain', 'PM': 'light rain'}, 'N': {'AM': 'clear sky', 'PM': 'clear sky'}, 'NE': {'AM': 'overcast clouds', 'PM': 'light rain'}, 'S': {'AM': 'light rain', 'PM': 'overcast clouds'}, 'W': {'AM': 'broken clouds', 'PM': 'light rain'}}",
    "assert AM_PM_weather_description_by_region(data, '2021-04-08') == {'C': {'AM': 'clear sky', 'PM': 'clear sky'}, 'E': {'AM': 'overcast clouds', 'PM': 'light rain'}, 'N': {'AM': 'clear sky', 'PM': 'scattered clouds'}, 'NE': {'AM': 'few clouds', 'PM': 'clear sky'}, 'S': {'AM': 'overcast clouds', 'PM': 'light rain'}, 'W': {'AM': 'broken clouds', 'PM': 'scattered clouds'}}",
    "assert AM_PM_weather_description_by_region(data, '2021-04-09') == {'C': {'AM': 'few clouds', 'PM': 'light rain'}, 'E': {'AM': 'broken clouds', 'PM': 'light rain'}, 'N': {'AM': 'clear sky', 'PM': 'few clouds'}, 'NE': {'AM': 'scattered clouds', 'PM': 'broken clouds'}, 'S': {'AM': 'light rain', 'PM': 'light rain'}, 'W': {'AM': 'scattered clouds', 'PM': 'broken clouds'}}",
    "assert AM_PM_weather_description_by_region(data, '2021-04-10') == {'C': {'AM': 'light rain', 'PM': 'overcast clouds'}, 'E': {'AM': 'light rain', 'PM': 'overcast clouds'}, 'N': {'AM': 'clear sky', 'PM': 'broken clouds'}, 'NE': {'AM': 'broken clouds', 'PM': 'broken clouds'}, 'S': {'AM': 'light rain', 'PM': 'light rain'}, 'W': {'AM': 'light rain', 'PM': 'broken clouds'}}",
    "assert AM_PM_weather_description_by_region(data, '2021-04-11') == {'C': {'AM': 'overcast clouds'}, 'E': {'AM': 'light rain'}, 'N': {'AM': 'overcast clouds'}, 'NE': {'AM': 'overcast clouds'}, 'S': {'AM': 'overcast clouds'}, 'W': {'AM': 'broken clouds'}}",
    "assert most_varied_weather_provinces(data) == {'Phichit', 'Ratchaburi'}",
]
print('Testing %d testcases' % len(test))
print(dash)
data = json.load(open('th_weather_39.json'))
#for i in range(10):
for i in range(len(test)) :
    i += 1
    try : 
        exec(test[i-1])
        result[i] = 'P'
    except AssertionError:
        print('Case %d ' % i,end='')
        print(': -')
        print('The output of testcases %d is wrong' % i)
        result[i] = '-'
        print(dash)
    except Exception as e: 
        print('Case %d ' % i,end='')
        print(': X')
        print('Error at testcases no. %d\nError Details:\n    %s' % (i,e))
        result[i] = 'X'
        print(dash)
print(' '.join(id_name[1:]))
print('Report:')
notes = [
    'Case 1-2 is from top_K_max_temp_by_region',
    'Case 3-9 is average_temp_by_date',
    'Case 10-51 is max_rain_in_3h_periods',
    'Case 52-57 is AM_PM_weather_description_by_region',
    'Case 58 is most_varied_weather_provinces',
]
print('Notes:')
for i in notes : print('\t'+i)
print('Result: ')
for i in range(1,len(result)+1):
    if i % 7 == 1 : print('\t%02d: %s' % (i,result[i]),end='')
    else : print(' %02d: %s' % (i,result[i]),end='')
    if i % 7 == 0 : print()
    elif i == len(result) : print()
    else : print(',',end='')
print("'P' = Pass, '-' = Wrong Output, 'X' = Error")
errors = {i:j for i,j in result.items() if j != 'P'}
print(dash)
if len(errors) > 0 : 
    print('Errors :', errors)
    print('Go fix your error(s) and try again. Good Luck!')
else : print('All tests passes! Say Thanks to Meen!')
print(dash)
print('Execution Time :',time.time()-start, 'seconds')
print(dash)