import time
import sys
dash = '-'*60
cfn = open(__file__).readlines()
id_name = cfn[1].strip().split()
print(dash)
print('Prog-12: COVID-19: The Latest Wave testcases by Meen')
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

for i in range(len(cfn)) :
    if 'for' in cfn[i] or 'while' in cfn[i]: 
        print('!'*60)
        print('Loop found at line no. %d. Please recheck' % i)
        print('!'*60)
        sys.exit(0)
start = time.time()
result = {}




# The Case number is corresponds with linenumber-40
# For example Case 1 is line 41, Case 2 is line 42 and so on
# You can copy that entire line and paste it in your code and then remove the " sign 
# from the front and back assert just means check if the statement is True
test = [
    "assert max_new_cases_province(data,'2021-04-01','2021-04-01') == ('Samut Sakhon', 11)",
    "assert max_new_cases_province(data,'2021-04-01','2021-04-02') == ('Bangkok', 27)",
    "assert max_new_cases_province(data,'2021-04-01','2021-04-03') == ('Bangkok', 59)",
    "assert max_new_cases_province(data,'2021-04-01','2021-04-04') == ('Bangkok', 94)",
    "assert max_new_cases_province(data,'2021-04-01','2021-04-05') == ('Bangkok', 140)",
    "assert max_new_cases_province(data,'2021-04-01','2021-04-06') == ('Bangkok', 296)",
    "assert max_new_cases_province(data,'2021-04-01','2021-04-07') == ('Bangkok', 512)",
    "assert max_new_cases_province(data,'2021-04-01','2021-04-08') == ('Bangkok', 607)",
    "assert max_new_cases_province(data,'2021-04-01','2021-04-09') == ('Bangkok', 875)",
    "assert max_new_cases_province(data,'2021-04-01','2021-04-10') == ('Bangkok', 1060)",
    "assert max_new_cases_province(data,'2021-04-01','2021-04-11') == ('Bangkok', 1296)",
    "assert max_new_cases_province(data,'2021-04-01','2021-04-12') == ('Bangkok', 1433)",
    "assert max_new_cases_province(data,'2021-04-01','2021-04-13') == ('Bangkok', 1627)",
    "assert max_new_cases_province(data,'2021-04-01','2021-04-14') == ('Bangkok', 1978)",
    "assert max_new_cases_province(data,'2021-04-01','2021-04-15') == ('Bangkok', 2387)",
    "assert max_new_cases_province(data,'2021-04-01','2021-04-16') == ('Bangkok', 2699)",
    "assert max_new_cases_province(data,'2021-04-02','2021-04-02') == ('Bangkok', 20)",
    "assert max_new_cases_province(data,'2021-04-02','2021-04-03') == ('Bangkok', 52)",
    "assert max_new_cases_province(data,'2021-04-02','2021-04-04') == ('Bangkok', 87)",
    "assert max_new_cases_province(data,'2021-04-02','2021-04-05') == ('Bangkok', 133)",
    "assert max_new_cases_province(data,'2021-04-02','2021-04-06') == ('Bangkok', 289)",
    "assert max_new_cases_province(data,'2021-04-02','2021-04-07') == ('Bangkok', 505)",
    "assert max_new_cases_province(data,'2021-04-02','2021-04-08') == ('Bangkok', 600)",
    "assert max_new_cases_province(data,'2021-04-02','2021-04-09') == ('Bangkok', 868)",
    "assert max_new_cases_province(data,'2021-04-02','2021-04-10') == ('Bangkok', 1053)",
    "assert max_new_cases_province(data,'2021-04-02','2021-04-11') == ('Bangkok', 1289)",
    "assert max_new_cases_province(data,'2021-04-02','2021-04-12') == ('Bangkok', 1426)",
    "assert max_new_cases_province(data,'2021-04-02','2021-04-13') == ('Bangkok', 1620)",
    "assert max_new_cases_province(data,'2021-04-02','2021-04-14') == ('Bangkok', 1971)",
    "assert max_new_cases_province(data,'2021-04-02','2021-04-15') == ('Bangkok', 2380)",
    "assert max_new_cases_province(data,'2021-04-02','2021-04-16') == ('Bangkok', 2692)",
    "assert max_new_cases_province(data,'2021-04-03','2021-04-03') == ('Bangkok', 32)",
    "assert max_new_cases_province(data,'2021-04-03','2021-04-04') == ('Bangkok', 67)",
    "assert max_new_cases_province(data,'2021-04-03','2021-04-05') == ('Bangkok', 113)",
    "assert max_new_cases_province(data,'2021-04-03','2021-04-06') == ('Bangkok', 269)",
    "assert max_new_cases_province(data,'2021-04-03','2021-04-07') == ('Bangkok', 485)",
    "assert max_new_cases_province(data,'2021-04-03','2021-04-08') == ('Bangkok', 580)",
    "assert max_new_cases_province(data,'2021-04-03','2021-04-09') == ('Bangkok', 848)",
    "assert max_new_cases_province(data,'2021-04-03','2021-04-10') == ('Bangkok', 1033)",
    "assert max_new_cases_province(data,'2021-04-03','2021-04-11') == ('Bangkok', 1269)",
    "assert max_new_cases_province(data,'2021-04-03','2021-04-12') == ('Bangkok', 1406)",
    "assert max_new_cases_province(data,'2021-04-03','2021-04-13') == ('Bangkok', 1600)",
    "assert max_new_cases_province(data,'2021-04-03','2021-04-14') == ('Bangkok', 1951)",
    "assert max_new_cases_province(data,'2021-04-03','2021-04-15') == ('Bangkok', 2360)",
    "assert max_new_cases_province(data,'2021-04-03','2021-04-16') == ('Bangkok', 2672)",
    "assert max_new_cases_province(data,'2021-04-04','2021-04-04') == ('Bangkok', 35)",
    "assert max_new_cases_province(data,'2021-04-04','2021-04-05') == ('Narathiwat', 95)",
    "assert max_new_cases_province(data,'2021-04-04','2021-04-06') == ('Bangkok', 237)",
    "assert max_new_cases_province(data,'2021-04-04','2021-04-07') == ('Bangkok', 453)",
    "assert max_new_cases_province(data,'2021-04-04','2021-04-08') == ('Bangkok', 548)",
    "assert max_new_cases_province(data,'2021-04-04','2021-04-09') == ('Bangkok', 816)",
    "assert max_new_cases_province(data,'2021-04-04','2021-04-10') == ('Bangkok', 1001)",
    "assert max_new_cases_province(data,'2021-04-04','2021-04-11') == ('Bangkok', 1237)",
    "assert max_new_cases_province(data,'2021-04-04','2021-04-12') == ('Bangkok', 1374)",
    "assert max_new_cases_province(data,'2021-04-04','2021-04-13') == ('Bangkok', 1568)",
    "assert max_new_cases_province(data,'2021-04-04','2021-04-14') == ('Bangkok', 1919)",
    "assert max_new_cases_province(data,'2021-04-04','2021-04-15') == ('Bangkok', 2328)",
    "assert max_new_cases_province(data,'2021-04-04','2021-04-16') == ('Bangkok', 2640)",
    "assert max_new_cases_province(data,'2021-04-05','2021-04-05') == ('Narathiwat', 94)",
    "assert max_new_cases_province(data,'2021-04-05','2021-04-06') == ('Bangkok', 202)",
    "assert max_new_cases_province(data,'2021-04-05','2021-04-07') == ('Bangkok', 418)",
    "assert max_new_cases_province(data,'2021-04-05','2021-04-08') == ('Bangkok', 513)",
    "assert max_new_cases_province(data,'2021-04-05','2021-04-09') == ('Bangkok', 781)",
    "assert max_new_cases_province(data,'2021-04-05','2021-04-10') == ('Bangkok', 966)",
    "assert max_new_cases_province(data,'2021-04-05','2021-04-11') == ('Bangkok', 1202)",
    "assert max_new_cases_province(data,'2021-04-05','2021-04-12') == ('Bangkok', 1339)",
    "assert max_new_cases_province(data,'2021-04-05','2021-04-13') == ('Bangkok', 1533)",
    "assert max_new_cases_province(data,'2021-04-05','2021-04-14') == ('Bangkok', 1884)",
    "assert max_new_cases_province(data,'2021-04-05','2021-04-15') == ('Bangkok', 2293)",
    "assert max_new_cases_province(data,'2021-04-05','2021-04-16') == ('Bangkok', 2605)",
    "assert max_new_cases_province(data,'2021-04-06','2021-04-06') == ('Bangkok', 156)",
    "assert max_new_cases_province(data,'2021-04-06','2021-04-07') == ('Bangkok', 372)",
    "assert max_new_cases_province(data,'2021-04-06','2021-04-08') == ('Bangkok', 467)",
    "assert max_new_cases_province(data,'2021-04-06','2021-04-09') == ('Bangkok', 735)",
    "assert max_new_cases_province(data,'2021-04-06','2021-04-10') == ('Bangkok', 920)",
    "assert max_new_cases_province(data,'2021-04-06','2021-04-11') == ('Bangkok', 1156)",
    "assert max_new_cases_province(data,'2021-04-06','2021-04-12') == ('Bangkok', 1293)",
    "assert max_new_cases_province(data,'2021-04-06','2021-04-13') == ('Bangkok', 1487)",
    "assert max_new_cases_province(data,'2021-04-06','2021-04-14') == ('Bangkok', 1838)",
    "assert max_new_cases_province(data,'2021-04-06','2021-04-15') == ('Bangkok', 2247)",
    "assert max_new_cases_province(data,'2021-04-06','2021-04-16') == ('Bangkok', 2559)",
    "assert max_new_cases_province(data,'2021-04-07','2021-04-07') == ('Bangkok', 216)",
    "assert max_new_cases_province(data,'2021-04-07','2021-04-08') == ('Bangkok', 311)",
    "assert max_new_cases_province(data,'2021-04-07','2021-04-09') == ('Bangkok', 579)",
    "assert max_new_cases_province(data,'2021-04-07','2021-04-10') == ('Bangkok', 764)",
    "assert max_new_cases_province(data,'2021-04-07','2021-04-11') == ('Bangkok', 1000)",
    "assert max_new_cases_province(data,'2021-04-07','2021-04-12') == ('Bangkok', 1137)",
    "assert max_new_cases_province(data,'2021-04-07','2021-04-13') == ('Bangkok', 1331)",
    "assert max_new_cases_province(data,'2021-04-07','2021-04-14') == ('Bangkok', 1682)",
    "assert max_new_cases_province(data,'2021-04-07','2021-04-15') == ('Bangkok', 2091)",
    "assert max_new_cases_province(data,'2021-04-07','2021-04-16') == ('Bangkok', 2403)",
    "assert max_new_cases_province(data,'2021-04-08','2021-04-08') == ('Narathiwat', 146)",
    "assert max_new_cases_province(data,'2021-04-08','2021-04-09') == ('Bangkok', 363)",
    "assert max_new_cases_province(data,'2021-04-08','2021-04-10') == ('Bangkok', 548)",
    "assert max_new_cases_province(data,'2021-04-08','2021-04-11') == ('Bangkok', 784)",
    "assert max_new_cases_province(data,'2021-04-08','2021-04-12') == ('Bangkok', 921)",
    "assert max_new_cases_province(data,'2021-04-08','2021-04-13') == ('Bangkok', 1115)",
    "assert max_new_cases_province(data,'2021-04-08','2021-04-14') == ('Bangkok', 1466)",
    "assert max_new_cases_province(data,'2021-04-08','2021-04-15') == ('Bangkok', 1875)",
    "assert max_new_cases_province(data,'2021-04-08','2021-04-16') == ('Bangkok', 2187)",
    "assert max_new_cases_province(data,'2021-04-09','2021-04-09') == ('Bangkok', 268)",
    "assert max_new_cases_province(data,'2021-04-09','2021-04-10') == ('Bangkok', 453)",
    "assert max_new_cases_province(data,'2021-04-09','2021-04-11') == ('Bangkok', 689)",
    "assert max_new_cases_province(data,'2021-04-09','2021-04-12') == ('Bangkok', 826)",
    "assert max_new_cases_province(data,'2021-04-09','2021-04-13') == ('Bangkok', 1020)",
    "assert max_new_cases_province(data,'2021-04-09','2021-04-14') == ('Bangkok', 1371)",
    "assert max_new_cases_province(data,'2021-04-09','2021-04-15') == ('Bangkok', 1780)",
    "assert max_new_cases_province(data,'2021-04-09','2021-04-16') == ('Bangkok', 2092)",
    "assert max_new_cases_province(data,'2021-04-10','2021-04-10') == ('Bangkok', 185)",
    "assert max_new_cases_province(data,'2021-04-10','2021-04-11') == ('Bangkok', 421)",
    "assert max_new_cases_province(data,'2021-04-10','2021-04-12') == ('Chiang Mai', 603)",
    "assert max_new_cases_province(data,'2021-04-10','2021-04-13') == ('Chiang Mai', 854)",
    "assert max_new_cases_province(data,'2021-04-10','2021-04-14') == ('Chiang Mai', 1173)",
    "assert max_new_cases_province(data,'2021-04-10','2021-04-15') == ('Bangkok', 1512)",
    "assert max_new_cases_province(data,'2021-04-10','2021-04-16') == ('Bangkok', 1824)",
    "assert max_new_cases_province(data,'2021-04-11','2021-04-11') == ('Bangkok', 236)",
    "assert max_new_cases_province(data,'2021-04-11','2021-04-12') == ('Chiang Mai', 435)",
    "assert max_new_cases_province(data,'2021-04-11','2021-04-13') == ('Chiang Mai', 686)",
    "assert max_new_cases_province(data,'2021-04-11','2021-04-14') == ('Chiang Mai', 1005)",
    "assert max_new_cases_province(data,'2021-04-11','2021-04-15') == ('Bangkok', 1327)",
    "assert max_new_cases_province(data,'2021-04-11','2021-04-16') == ('Bangkok', 1639)",
    "assert max_new_cases_province(data,'2021-04-12','2021-04-12') == ('Chiang Mai', 246)",
    "assert max_new_cases_province(data,'2021-04-12','2021-04-13') == ('Chiang Mai', 497)",
    "assert max_new_cases_province(data,'2021-04-12','2021-04-14') == ('Chiang Mai', 816)",
    "assert max_new_cases_province(data,'2021-04-12','2021-04-15') == ('Chiang Mai', 1094)",
    "assert max_new_cases_province(data,'2021-04-12','2021-04-16') == ('Bangkok', 1403)",
    "assert max_new_cases_province(data,'2021-04-13','2021-04-13') == ('Chiang Mai', 251)",
    "assert max_new_cases_province(data,'2021-04-13','2021-04-14') == ('Chiang Mai', 570)",
    "assert max_new_cases_province(data,'2021-04-13','2021-04-15') == ('Bangkok', 954)",
    "assert max_new_cases_province(data,'2021-04-13','2021-04-16') == ('Bangkok', 1266)",
    "assert max_new_cases_province(data,'2021-04-14','2021-04-14') == ('Bangkok', 351)",
    "assert max_new_cases_province(data,'2021-04-14','2021-04-15') == ('Bangkok', 760)",
    "assert max_new_cases_province(data,'2021-04-14','2021-04-16') == ('Bangkok', 1072)",
    "assert max_new_cases_province(data,'2021-04-15','2021-04-15') == ('Bangkok', 409)",
    "assert max_new_cases_province(data,'2021-04-15','2021-04-16') == ('Bangkok', 721)",
    "assert max_new_cases_province(data,'2021-04-16','2021-04-16') == ('Bangkok', 312)",
    "assert most_similar(data,'Krabi') == Nong Bua Lamphu",
    "assert most_similar(data,'Bangkok') == Khon Kaen",
    "assert most_similar(data,'Kanchanaburi') == Phang Nga",
    "assert most_similar(data,'Kalasin') == Phitsanulok",
    "assert most_similar(data,'Kamphaeng Phet') == Nakhon Pathom",
    "assert most_similar(data,'Khon Kaen') == Ratchaburi",
    "assert most_similar(data,'Chanthaburi') == Rayong",
    "assert most_similar(data,'Chachoengsao') == Prachuap Khiri Khan",
    "assert most_similar(data,'Chonburi') == Phuket",
    "assert most_similar(data,'Chai Nat') == Sakon Nakhon",
    "assert most_similar(data,'Chaiyaphum') == Nonthaburi",
    "assert most_similar(data,'Chumphon') == Samut Songkhram",
    "assert most_similar(data,'Trang') == Songkhla",
    "assert most_similar(data,'Trat') == Saraburi",
    "assert most_similar(data,'Tak') == Samut Sakhon",
    "assert most_similar(data,'Nakhon Nayok') == Trat",
    "assert most_similar(data,'Nakhon Pathom') == Kamphaeng Phet",
    "assert most_similar(data,'Nakhon Phanom') == Phitsanulok",
    "assert most_similar(data,'Nakhon Ratchasima') == Nakhon Si Thammarat",
    "assert most_similar(data,'Nakhon Si Thammarat') == Trang",
    "assert most_similar(data,'Nakhon Sawan') == Kalasin",
    "assert most_similar(data,'Nonthaburi') == Sing Buri",
    "assert most_similar(data,'Narathiwat') == Chaiyaphum",
    "assert most_similar(data,'Nan') == Uthai Thani",
    "assert most_similar(data,'Bueng Kan') == Nonthaburi",
    "assert most_similar(data,'Buriram') == Lopburi",
    "assert most_similar(data,'Pathum Thani') == Rayong",
    "assert most_similar(data,'Prachuap Khiri Khan') == Chachoengsao",
    "assert most_similar(data,'Prachinburi') == Chachoengsao",
    "assert most_similar(data,'Pattani') == Kanchanaburi",
    "assert most_similar(data,'Phra Nakhon Si Ayutthaya') == Phetchaburi",
    "assert most_similar(data,'Phayao') == Phrae",
    "assert most_similar(data,'Phang Nga') == Kanchanaburi",
    "assert most_similar(data,'Phatthalung') == Chiang Rai",
    "assert most_similar(data,'Phichit') == Phang Nga",
    "assert most_similar(data,'Phitsanulok') == Kalasin",
    "assert most_similar(data,'Phuket') == Nakhon Pathom",
    "assert most_similar(data,'Maha Sarakham') == Sakon Nakhon",
    "assert most_similar(data,'Mukdahan') == Amnat Charoen",
    "assert most_similar(data,'Yala') == Nakhon Sawan",
    "assert most_similar(data,'Yasothon') == Amnat Charoen",
    "assert most_similar(data,'Ranong') == Satun",
    "assert most_similar(data,'Rayong') == Chanthaburi",
    "assert most_similar(data,'Ratchaburi') == Khon Kaen",
    "assert most_similar(data,'Roi Et') == Chiang Mai",
    "assert most_similar(data,'Lopburi') == Buriram",
    "assert most_similar(data,'Lampang') == Ranong",
    "assert most_similar(data,'Lamphun') == Phetchaburi",
    "assert most_similar(data,'Sisaket') == Ranong",
    "assert most_similar(data,'Sakon Nakhon') == Maha Sarakham",
    "assert most_similar(data,'Songkhla') == Sisaket",
    "assert most_similar(data,'Satun') == Ranong",
    "assert most_similar(data,'Samut Prakan') == Pathum Thani",
    "assert most_similar(data,'Samut Songkhram') == Phetchabun",
    "assert most_similar(data,'Samut Sakhon') == Tak",
    "assert most_similar(data,'Saraburi') == Trat",
    "assert most_similar(data,'Sa Kaeo') == Bangkok",
    "assert most_similar(data,'Sing Buri') == Songkhla",
    "assert most_similar(data,'Suphan Buri') == Ubon Ratchathani",
    "assert most_similar(data,'Surat Thani') == Phra Nakhon Si Ayutthaya",
    "assert most_similar(data,'Surin') == Krabi",
    "assert most_similar(data,'Sukhothai') == Prachinburi",
    "assert most_similar(data,'Nong Khai') == Trang",
    "assert most_similar(data,'Nong Bua Lamphu') == Krabi",
    "assert most_similar(data,'Amnat Charoen') == Mukdahan",
    "assert most_similar(data,'Udon Thani') == Maha Sarakham",
    "assert most_similar(data,'Uttaradit') == Nakhon Sawan",
    "assert most_similar(data,'Uthai Thani') == Nan",
    "assert most_similar(data,'Ubon Ratchathani') == Phetchabun",
    "assert most_similar(data,'Ang Thong') == Saraburi",
    "assert most_similar(data,'Chiang Rai') == Lampang",
    "assert most_similar(data,'Chiang Mai') == Ratchaburi",
    "assert most_similar(data,'Phetchaburi') == Lamphun",
    "assert most_similar(data,'Phetchabun') == Ubon Ratchathani",
    "assert most_similar(data,'Loei') == Prachinburi",
    "assert most_similar(data,'Phrae') == Phayao",
    "assert most_similar(data,'Mae Hong Son') == Nakhon Sawan",

]
print('Testing %d testcases' % len(test))
print(dash)
data = read_data('TH_COVID_EN.csv')
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
    'Case 1-136 is from max_new_cases_province',
    'Case 137-213 is most_similar'
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