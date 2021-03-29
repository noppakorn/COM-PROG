stations = {
    'BON HEIR RAI Buak Buak' : {
        'lat':  20,
        'long': 100,
        'temp': 25.5,
    },
    'MAE MUENG SI haha' : {
        'lat':  21,
        'long': 50,
        'temp': 27.5,
    },
    'EIEI' : {
        'lat':  50,
        'long': 21,
        'temp': 155555.5,
    },
    'e I e I z A HaHA BUAK' : {
        'lat':  21,
        'long': 100,
        'temp': 26,
    },
    'meenmeen' : {
        'lat':  100,
        'long': 200,
        'temp': 28,
    },
    'akkkkmeen' : {
        'lat':  31,
        'long': 250,
        'temp': 29.5,
    },
    'Akkkkmeen2' : {
        'lat':  30,
        'long': 246,
        'temp': 27.5,
    }
}
# Case 0 at line 40 and so on
testcases = [
    "assert sorted(approx_match(stations,'haha')) == ['MAE MUENG SI haha', 'e I e I z A HaHA BUAK']",
    "assert sorted(approx_match(stations,'eiEI')) == ['EIEI', 'e I e I z A HaHA BUAK']",
    "assert sorted(approx_match(stations,'bon h ei R rai')) == ['BON HEIR RAI Buak Buak']",
    "assert sorted(approx_match(stations,'b u a k')) == ['BON HEIR RAI Buak Buak', 'e I e I z A HaHA BUAK']",
    "assert sorted(approx_match(stations,'kaub')) == []",
    "assert top_k_max_temp_stations(stations,2) == ['EIEI', 'akkkkmeen']",
    "assert top_k_max_temp_stations(stations,3) == ['EIEI', 'akkkkmeen', 'meenmeen']",
    "assert top_k_min_temp_stations(stations,2) == ['BON HEIR RAI Buak Buak', 'e I e I z A HaHA BUAK']",
    "assert top_k_min_temp_stations(stations,4) == ['BON HEIR RAI Buak Buak', 'e I e I z A HaHA BUAK', 'Akkkkmeen2', 'MAE MUENG SI haha']",
    "assert peak_stations(stations) == ['BON HEIR RAI Buak Buak', 'meenmeen', 'EIEI', 'akkkkmeen']",
    "assert average_temp(stations,['BON HEIR RAI Buak Buak','MAE MUENG SI haha','meenmeen','e I e I z A HaHA BUAK']) == 26.75",
    "assert average_temp(stations,['akkkkmeen','MAE MUENG SI haha','meenmeen','Akkkkmeen2']) == 28.125",
    "assert k_nearby_stations(stations,'meenmeen',2) == ['EIEI', 'MAE MUENG SI haha']",
    "assert k_nearby_stations(stations,'BON HEIR RAI Buak Buak',3) == ['e I e I z A HaHA BUAK', 'MAE MUENG SI haha', 'EIEI']",
    ]
print('------------------------------------------------------------------------------------------')
print('Prog-09: Weather Report Special Testcases by Meen for use in this group only')
print('Case 0-4: approx_match Case 5-7: top_k_max_temp_stations Case 7-8: top_k_min_temp_stations')
print('Case 9: peak_stations Case 10-11: average_temp Case 12-13: k_nearby_stations')
print('------------------------------------------------------------------------------------------')
d,f = {},{}
for i in range(len(testcases)) :
    try : 
        exec(testcases[i])
        d['Case %d' % i] = 'Pass'
    except AssertionError :
        print('Case %d Failed' % i)
        d['Case %d' % i] = 'Failed'
        f['Case %d' % i] = 'Failed'
print('Summary:',d)
if len(f) > 0: print('Failed Case:',f)
else: print('All tests passes!')