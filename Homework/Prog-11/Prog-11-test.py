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
    "assert average_temp_by_date(data, 'C') == [('2021-04-06',28.395740740740735),('2021-04-07', 28.821388888888887),('2021-04-08', 30.702083333333334),('2021-04-09', 31.940138888888896),('2021-04-10', 31.774027777777786),('2021-04-11', 30.828333333333333)]",
    "assert average_temp_by_date(data, 'E') == [('2021-04-06', 28.506333333333334), ('2021-04-07', 28.919), ('2021-04-08', 28.357999999999997), ('2021-04-09', 30.100250000000006), ('2021-04-10', 29.88675), ('2021-04-11', 29.740000000000002)]",
    "assert average_temp_by_date(data, 'N') == [('2021-04-06', 21.47916666666667), ('2021-04-07', 26.742708333333326), ('2021-04-08', 28.78999999999999), ('2021-04-09', 30.37937500000001), ('2021-04-10', 29.014166666666664), ('2021-04-11', 28.22416666666666)]",
    "assert average_temp_by_date(data, 'NE') == [('2021-04-06', 30.630238095238095), ('2021-04-07', 28.294642857142858), ('2021-04-08', 31.05017857142857), ('2021-04-09', 31.009999999999994), ('2021-04-10', 31.15964285714285), ('2021-04-11', 29.378571428571433)]",
    "assert average_temp_by_date(data, 'S') == [('2021-04-06', 27.736250000000002), ('2021-04-07', 27.223750000000003), ('2021-04-08', 27.476874999999996), ('2021-04-09', 27.734531249999993), ('2021-04-10', 27.745937500000007), ('2021-04-11', 27.8125)]",
    "assert average_temp_by_date(data, 'W') == [('2021-04-06', 28.77875), ('2021-04-07', 28.356875000000002), ('2021-04-08', 29.423125000000002), ('2021-04-09', 30.708125), ('2021-04-10', 30.065312499999994), ('2021-04-11', 29.435)]",
    "assert average_temp_by_date(data, 'ALL') == [('2021-04-06', 27.650897435897416), ('2021-04-07', 28.044198717948728), ('2021-04-08', 29.37711538461539), ('2021-04-09', 30.308141025641), ('2021-04-10', 29.99567307692307), ('2021-04-11', 29.266410256410254)]",
    "assert max_rain_in_3h_periods(data, 'ALL', '2021-04-07') == [(0, 3.52),(3, 4.81),(6, 5.66),(9, 1.45),(12, 10.68),(15, 13.35),(18, 3.66),(21, 4.64)]",
	"assert AM_PM_weather_description_by_region(data, '2021-04-06') == {'C': {'AM': 'light rain', 'PM': 'light rain'}, 'E': {'AM': 'light rain', 'PM': 'overcast clouds'}, 'N': {'AM': 'light rain', 'PM': 'few clouds'}, 'NE': {'AM': 'broken clouds', 'PM': 'overcast clouds'}, 'S': {'AM': 'light rain', 'PM': 'light rain'}, 'W': {'AM': 'light rain', 'PM': 'light rain'}}",
	"assert AM_PM_weather_description_by_region(data, '2021-04-07') == {'C': {'AM': 'broken clouds', 'PM': 'light rain'}, 'E': {'AM': 'light rain', 'PM': 'light rain'}, 'N': {'AM': 'clear sky', 'PM': 'clear sky'}, 'NE': {'AM': 'overcast clouds', 'PM': 'light rain'}, 'S': {'AM': 'light rain', 'PM': 'overcast clouds'}, 'W': {'AM': 'broken clouds', 'PM': 'light rain'}}",
	"assert AM_PM_weather_description_by_region(data, '2021-04-08') == {'C': {'AM': 'clear sky', 'PM': 'clear sky'}, 'E': {'AM': 'overcast clouds', 'PM': 'light rain'}, 'N': {'AM': 'clear sky', 'PM': 'scattered clouds'}, 'NE': {'AM': 'few clouds', 'PM': 'clear sky'}, 'S': {'AM': 'overcast clouds', 'PM': 'light rain'}, 'W': {'AM': 'broken clouds', 'PM': 'scattered clouds'}}",
	"assert AM_PM_weather_description_by_region(data, '2021-04-09') == {'C': {'AM': 'few clouds', 'PM': 'light rain'}, 'E': {'AM': 'broken clouds', 'PM': 'light rain'}, 'N': {'AM': 'clear sky', 'PM': 'few clouds'}, 'NE': {'AM': 'scattered clouds', 'PM': 'broken clouds'}, 'S': {'AM': 'light rain', 'PM': 'light rain'}, 'W': {'AM': 'scattered clouds', 'PM': 'broken clouds'}}",
	"assert AM_PM_weather_description_by_region(data, '2021-04-10') == {'C': {'AM': 'light rain', 'PM': 'overcast clouds'}, 'E': {'AM': 'light rain', 'PM': 'overcast clouds'}, 'N': {'AM': 'clear sky', 'PM': 'broken clouds'}, 'NE': {'AM': 'broken clouds', 'PM': 'broken clouds'}, 'S': {'AM': 'light rain', 'PM': 'light rain'}, 'W': {'AM': 'light rain', 'PM': 'broken clouds'}}",
	"assert AM_PM_weather_description_by_region(data, '2021-04-11') == {'C': {'AM': 'overcast clouds'}, 'E': {'AM': 'light rain'}, 'N': {'AM': 'overcast clouds'}, 'NE': {'AM': 'overcast clouds'}, 'S': {'AM': 'overcast clouds'}, 'W': {'AM': 'broken clouds'}}",
    "assert most_varied_weather_provinces(data) == {'Phichit', 'Ratchaburi'}",
]
data = json.load(open('th_weather_39.json'))
for i in range(len(test)) :
    i += 1
    try : 
        print('Testing Case %d ' % i,end='')
        exec(test[i-1])
        result[i] = 'P'
        print(': P')
    except AssertionError:
        print(': -')
        print('The output of testcases %d is wrong' % i)
        result[i] = '-'
    except Exception as e: 
        print(': X')
        print('Error at testcases no. %d\nError Details:\n    %s' % (i,e))
        result[i] = 'X'
    print(dash)
print(' '.join(id_name[1:]))
print('Report:')
notes = [
    'Case 1 is from top_K_max_temp_by_region',
    'Case 2-8 is average_temp_by_date',
    'Case 10-15 is AM_PM_weather_description_by_region',
    #'Case 12 is most_varied_weather_provinces',
]
print('Notes:')
for i in notes : print('\t'+i)
print('Result: ')
for i in range(1,len(result)+1):
    if i % 5 == 1 : print('\t%02d: %s' % (i,result[i]),end='')
    else : print(' %02d: %s' % (i,result[i]),end='')
    if i % 5 == 0 : print()
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