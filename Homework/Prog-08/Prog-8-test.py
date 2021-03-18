import subprocess,glob
from difflib import context_diff
def test(fn,caseno,lin,lsol) :
    print('----------- Case %d -----------' % caseno)
    result = subprocess.Popen(['python',fn], shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.STDOUT)
    stdout = result.communicate(input='\n'.join(lin).encode())
    out = [e+'\n' for e in stdout[0].decode().split('\r\n')[:-1]]
    c = 0
    for i in context_diff(lsol, out, fromfile='Solution %d' % caseno,tofile='Output %d' % caseno) :
        print(i,end='')
        c += 1
    if c == 0 : 
        print('Case %d Pass' % caseno)
        return True 
    print('-------- Check Case %d --------' % caseno)
    return False
sol = [['File name = Use feature hashing ? (y,Y,n,N) -------------------',
        'char count = 81',
        'alphanumeric count = 61',
        'line count = 4',
        'word count = 19',
        "BoW = [['555', 1], ['age', 1], ['best', 1], ['times', 2], ['wisdom', 1], ['worst', 1]]"],
        ['File name = Use feature hashing ? (y,Y,n,N) M = -------------------',
        'char count = 81',
        'alphanumeric count = 61',
        'line count = 4',
        'word count = 19',
        'BoW = [[1, 1], [2, 3], [3, 3]]'],
        ['File name = Use feature hashing ? (y,Y,n,N) Try again.',            
        'Use feature hashing ? (y,Y,n,N) Try again.',            
        'Use feature hashing ? (y,Y,n,N) Try again.',            
        'Use feature hashing ? (y,Y,n,N) M = -------------------',            
        'char count = 81',            
        'alphanumeric count = 61',            
        'line count = 4',            
        'word count = 19',            
        'BoW = [[0, 2], [1, 1], [3, 2], [7, 1], [8, 1]]']
        ]
inp = [
    ['sample.txt','n'],
    ['sample.txt','y','4'],
    ['sample.txt','OK','Krub','Yes','Y','10']
    ]

for i in glob.glob('*') :
    if i.startswith('633') and i.endswith('21.py') : filename = i
d = {}
for i in range(len(sol)) :
    if test(filename,i+1,inp[i],[e+'\n' for e in sol[i]]) : d['Case %d' % (i+1)] = 'Pass'
    else : d['Case %d' % (i+1)] = 'Fail'
print('Summary',d)