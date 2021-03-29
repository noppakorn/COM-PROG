stations = {
    'BON HEIR RAI Buak Buak' : {
        'lat':  20,
        'long': 100,
        'temp': 25.5,
    },
    'MAE MUENG SI haha' : {
        'lat':  30,
        'long': 90,
        'temp': 27.5,
    },
    'EIEI' : {
        'lat':  50,
        'long': 20,
        'temp': 155555.5,
    },
    'e I e I z A HaHA BUAK' : {
        'lat':  21,
        'long': 230,
        'temp': 25.5,
    },
    'meenmeen' : {
        'lat':  100,
        'long': 200,
        'temp': 29.5,
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
# Case 0 at line 40
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
    "assert peak_stations(stations) == ['BON HEIR RAI Buak Buak', 'meenmeen', 'EIEI', 'akkkkmeen']"
    
    ]
print('----------------------------------------------------------------------------------------------------------------')
print('Case 0-5: approx_match Case 6-7: top_k_max_temp_stations Case 7-8: top_k_min_temp_stations Case 9: peak_stations')
print('----------------------------------------------------------------------------------------------------------------')
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