import subprocess,glob,os
from difflib import context_diff

def test(fn,caseno,lin,lsol) :
    print('----------- Case %d -----------' % caseno)
    result = subprocess.Popen(['python',fn], shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.STDOUT)
    stdout = result.communicate(input='\n'.join(lin).encode())
    if os.name == 'nt': 
        try : out = [e+'\n' for e in stdout[0].decode().split('\r\n')[:-1]]
        except : out = [e+'\n' for e in stdout[0].decode('ISO-8859-1').split('\r\n')[:-1]]
    elif os.name == 'posix': out = [e+'\n' for e in stdout[0].decode().split('\n')[:-1]]
    c = 0
    for line in context_diff(lsol, out, fromfile='Solution %d' % caseno,tofile='Output %d' % caseno) :
        print(line,end='')
        c += 1
    if c == 0 : 
        print('-------- Case %d Pass! --------' % caseno)
        return True 
    print('-------- Check Case %d --------' % caseno)
    return False

for i in glob.glob('*'): 
    if i.startswith('633') and i.endswith('21.py') : filename = i
lines = open(filename).readlines()[:-1] + open('function_for_test.py').readlines()
foutn = '%s_with-test-func.py' % filename.replace('.py','')
fout = open(foutn,'w')
for i in lines : fout.writelines(i)
fout.close()

sol = [['Weather Report:',
        ' (0) List all stations',
        ' (1) Temperatures at selected stations',
        ' (2) Top K max & min temperature stations',
        ' (3) Temperatures at the peak stations',
        ' (4) Temperatures at the nearby stations',
        ' (5) Average temperatures in the region',
        'Select 0,1,2,3,4,5: Station name: Chaing Rai Agromet. 16.1°c',
        'Lampang Agromet. 20.2°c',
        'Nan Agromet. 18.7°c',
        'Loei Agromet. 19.8°c',
        'Sakon Nakhon Agromet. 21.0°c',
        'Nakhon Phanom Agromet. 22.0°c',
        'Si Samrong Agromet. 23.0°c',
        'Doi Mu Soe Agromet. 14.4°c',
        'Tha Phra Agromet. 22.7°c',
        'Pichit Agromet. 24.8°c',
        'Takfa Agromet. 25.0°c',
        'Chainat Agromet. 25.0°c',
        'Roi Et Agromet. 23.0°c',
        'Ubon Ratchathani Agromet. 22.1°c',
        'Si Saket Agromet. 23.4°c',
        'U Thong Agromet. 24.4°c',
        'Pakchong Agromet. 22.2°c',
        'Surin Agromet. 23.2°c',
        'Bang Na Agromet. 27.4°c',
        'Huai Pong Agromet. 25.7°c',
        'Phliu  Agromet. 22.5°c',
        'Nong Phlub Agromet. 23.7°c',
        'Sawi Agromet. 23.0°c',
        'Surat Thani Agromet. 21.6°c',
        'Nakhonsi Thammarat Agromet. 22.3°c',
        'Phatthalung Agromet. 23.5°c',
        'Kho Hong Agromet. 24.3°c',
        'Yala Agromet. 21.7°c',
    ],
    [
        'Weather Report:',
        ' (0) List all stations',
        ' (1) Temperatures at selected stations',
        ' (2) Top K max & min temperature stations',
        ' (3) Temperatures at the peak stations',
        ' (4) Temperatures at the nearby stations',
        ' (5) Average temperatures in the region',
        'Select 0,1,2,3,4,5: K: Doi Mu Soe Agromet. 14.4°c',
        'Mae Hong Son 15.3°c',
        'Pilot Station 27.9°c',
        'Samut Prakarn 27.7°c',
    ],
    [
        'Weather Report:',
        ' (0) List all stations',
        ' (1) Temperatures at selected stations',
        ' (2) Top K max & min temperature stations',
        ' (3) Temperatures at the peak stations',
        ' (4) Temperatures at the nearby stations',
        ' (5) Average temperatures in the region',
        'Select 0,1,2,3,4,5: Narathiwat 23.4°c',
        'Chiang Rai 17.5°c',
        'Mae Sariang 16.0°c',
        'Ubon Ratchathani Agromet. 22.1°c',
    ],
    [
        'Weather Report:',
        ' (0) List all stations',
        ' (1) Temperatures at selected stations',
        ' (2) Top K max & min temperature stations',
        ' (3) Temperatures at the peak stations',
        ' (4) Temperatures at the nearby stations',
        ' (5) Average temperatures in the region',
        'Select 0,1,2,3,4,5: Main station: How many nearby stations? Mae Hong Son 15.3°c',
        'Chiang Mai 18.3°c',
        'Mae Sariang 16.0°c',
        'Doi Ang Kang 18.9°c',
    ],
    [
        'Weather Report:',
        ' (0) List all stations',
        ' (1) Temperatures at selected stations',
        ' (2) Top K max & min temperature stations',
        ' (3) Temperatures at the peak stations',
        ' (4) Temperatures at the nearby stations',
        ' (5) Average temperatures in the region',
        'Select 0,1,2,3,4,5: Region (N,E,W,S,C,NE): Average temperature = 22.1°c',
        'Tak 21.1°c',
        'Mae Sot 19.5°c',
        'Bhumibol Dam 21.0°c',
        'Doi Mu Soe Agromet. 14.4°c',
        'Umphang 16.0°c',
        'Ratcha Buri 24.0°c',
        'Kanchana Buri 25.3°c',
        'Thong Phaphum 23.8°c',
        'Phetcha Buri 25.5°c',
        'Prachuap Khirikhan 24.6°c',
        'Hua Hin 26.0°c',
        'Nong Phlub Agromet. 23.7°c',
    ]
        ]
inp = [
        ['1','agro'],
        ['2','2'],
        ['3'],
        ['4','Mae hong son','3'],
        ['5','W'],
    ]
d = {}
for i in range(len(sol)) :
    if test(foutn,i+1,inp[i],[e+'\n' for e in sol[i]]) : d['Case %d' % (i+1)] = 'Pass'
    else : d['Case %d' % (i+1)] = 'Fail'
print('Summary',d)