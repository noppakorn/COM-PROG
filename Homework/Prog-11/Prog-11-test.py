import time
import sys
import json
dash = '-'*50
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
test = [
    "assert top_K_max_temp_by_region(data,2) == {'C': [(38.54, 'Sukhothai Thani', '2021-04-09 06:00:00'),(38.18, 'Phitsanulok', '2021-04-09 06:00:00')],'E': [(36.45, 'Prachin Buri','2021-04-09 06:00:00'),(36.15, 'Chachoengsao','2021-04-09 09:00:00')],'N': [(38.98, 'Mae Hong Son', '2021-04-10 06:00:00'),(38.73, 'Mae Hong Son', '2021-04-10 09:00:00')],'NE': [(37.31, 'Surin', '2021-04-06 09:00:00'),(37.29, 'Ubon Ratchathani','2021-04-10 09:00:00')],'S': [(34.93, 'Yala','2021-04-10 06:00:00'),(34.74, 'Yala', '2021-04-07 06:00:00')],'W': [(38.97, 'Kanchanaburi','2021-04-09 09:00:00'),(38.11, 'Kanchanaburi', '2021-04-09 06:00:00')]}",
    "assert average_temp_by_date(data, 'C') == [('2021-04-06',28.395740740740735),('2021-04-07', 28.821388888888887),('2021-04-08', 30.702083333333334),('2021-04-09', 31.940138888888896),('2021-04-10', 31.774027777777786),('2021-04-11', 30.828333333333333)]",
    "assert max_rain_in_3h_periods(data, 'ALL', '2021-04-07') == [(0, 3.52),(3, 4.81),(6, 5.66),(9, 1.45),(12, 10.68),(15, 13.35),(18, 3.66),(21, 4.64)]",
    "assert AM_PM_weather_description_by_region(data, '2021-04-09') == {'C': {'AM': 'few clouds','PM': 'light rain'},'E': {'AM': 'broken clouds', 'PM': 'light rain'},'N': {'AM': 'clear sky','PM': 'clear sky'},'NE': {'AM': 'scattered clouds', 'PM': 'broken clouds'},'S': {'AM': 'light rain', 'PM': 'light rain'},'W': {'AM': 'scattered clouds', 'PM': 'broken clouds'}}",
    "assert most_varied_weather_provinces(data) == {'Phichit', 'Ratchaburi'}"
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
print("'P' = Pass, '-' = Wrong Output, 'X' = Error")
print('Notes : Case 1-5 is from PDF')
print('Result :', result)
errors = {i:j for i,j in result.items() if j != 'P'}
if len(errors) > 0 : 
    print('Errors :', errors)
    print('Go fix your error(s) and try again. Good Luck!')
else : print('All tests passes! Say Thanks to Meen!')
print('Execution Time :',time.time()-start, 'seconds')
print(dash)